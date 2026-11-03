"""encoder.py — real sentence embeddings from all-MiniLM-L6-v2, in numpy.

WHY THIS FILE EXISTS. The reel compares sparse retrieval against DENSE
retrieval, so the dense side has to be real. Faking embeddings — or hand-tuning
similarity scores to make the demo land — would make every number in the output
beats a fabrication.

`sentence-transformers` and `transformers` are not installed on this machine,
but the real model weights are in the local HuggingFace cache and `tokenizers`
is available. So this loads those weights directly and runs the 6-layer BERT
forward pass in numpy: the same architecture, the same weights, the same mean
pooling and L2 normalisation that sentence-transformers applies for
`all-MiniLM-L6-v2`. The embeddings are genuine.

Two things are implemented by hand because their libraries are absent:
  1. `read_safetensors` — the safetensors container is an 8-byte little-endian
     header length, a JSON header, then raw tensor bytes. That is the whole
     format; no dependency needed.
  2. `encode` — embeddings -> 6 x (self-attention, FFN) -> mean-pool over the
     attention mask -> L2 normalise.

Verified behaviourally by `python encoder.py` (see __main__): identical text
scores 1.000, paraphrases score high, unrelated text scores low. A broken
forward pass would produce noise and destroy that ordering.
"""
import json
import os
import struct

import numpy as np
from tokenizers import Tokenizer

MODEL_DIR = os.path.expanduser(
    "~/.cache/huggingface/hub/models--sentence-transformers--all-MiniLM-L6-v2"
    "/snapshots/1110a243fdf4706b3f48f1d95db1a4f5529b4d41"
)
N_LAYERS = 6
N_HEADS = 12
HIDDEN = 384
HEAD_DIM = HIDDEN // N_HEADS
EPS = 1e-12


def read_safetensors(path: str) -> dict:
    """Parse a .safetensors file into {name: ndarray} without the library."""
    with open(path, "rb") as f:
        header_len = struct.unpack("<Q", f.read(8))[0]
        header = json.loads(f.read(header_len))
        blob = f.read()
    dtypes = {"F32": np.float32, "I64": np.int64}
    out = {}
    for name, meta in header.items():
        if name == "__metadata__":
            continue
        start, end = meta["data_offsets"]
        arr = np.frombuffer(blob[start:end], dtype=dtypes[meta["dtype"]])
        out[name] = arr.reshape(meta["shape"])
    return out


def layer_norm(x, w, b):
    mu = x.mean(-1, keepdims=True)
    var = x.var(-1, keepdims=True)
    return (x - mu) / np.sqrt(var + EPS) * w + b


def gelu(x):
    return 0.5 * x * (1.0 + np.tanh(np.sqrt(2.0 / np.pi) * (x + 0.044715 * x ** 3)))


def softmax(x, axis=-1):
    x = x - x.max(axis=axis, keepdims=True)
    e = np.exp(x)
    return e / e.sum(axis=axis, keepdims=True)


class MiniLM:
    def __init__(self, model_dir: str = MODEL_DIR):
        self.w = read_safetensors(os.path.join(model_dir, "model.safetensors"))
        self.tok = Tokenizer.from_file(os.path.join(model_dir, "tokenizer.json"))
        self.tok.enable_truncation(max_length=256)
        self.tok.enable_padding()

    def encode(self, texts):
        """-> (n, 384) float32, L2-normalised. Dot product IS cosine similarity."""
        enc = self.tok.encode_batch(list(texts))
        ids = np.array([e.ids for e in enc], dtype=np.int64)
        mask = np.array([e.attention_mask for e in enc], dtype=np.float32)
        w = self.w

        # ── embeddings ──────────────────────────────────────────────────────
        seq = ids.shape[1]
        x = (w["embeddings.word_embeddings.weight"][ids]
             + w["embeddings.position_embeddings.weight"][:seq][None]
             + w["embeddings.token_type_embeddings.weight"][0][None, None])
        x = layer_norm(x, w["embeddings.LayerNorm.weight"], w["embeddings.LayerNorm.bias"])

        # additive attention mask: 0 for real tokens, -inf for padding
        bias = (1.0 - mask)[:, None, None, :] * -1e9

        # ── 6 transformer layers ────────────────────────────────────────────
        for i in range(N_LAYERS):
            p = f"encoder.layer.{i}."
            n, s = x.shape[0], x.shape[1]

            def heads(mat, vec):
                # (n, s, H) -> (n, heads, s, head_dim)
                y = x @ mat.T + vec
                return y.reshape(n, s, N_HEADS, HEAD_DIM).transpose(0, 2, 1, 3)

            q = heads(w[p + "attention.self.query.weight"], w[p + "attention.self.query.bias"])
            k = heads(w[p + "attention.self.key.weight"], w[p + "attention.self.key.bias"])
            v = heads(w[p + "attention.self.value.weight"], w[p + "attention.self.value.bias"])

            att = softmax(q @ k.transpose(0, 1, 3, 2) / np.sqrt(HEAD_DIM) + bias)
            ctx = (att @ v).transpose(0, 2, 1, 3).reshape(n, s, HIDDEN)

            ctx = ctx @ w[p + "attention.output.dense.weight"].T + w[p + "attention.output.dense.bias"]
            x = layer_norm(ctx + x,
                           w[p + "attention.output.LayerNorm.weight"],
                           w[p + "attention.output.LayerNorm.bias"])

            h = gelu(x @ w[p + "intermediate.dense.weight"].T + w[p + "intermediate.dense.bias"])
            h = h @ w[p + "output.dense.weight"].T + w[p + "output.dense.bias"]
            x = layer_norm(h + x,
                           w[p + "output.LayerNorm.weight"],
                           w[p + "output.LayerNorm.bias"])

        # ── mean pooling over real tokens, then L2 normalise ────────────────
        m = mask[:, :, None]
        pooled = (x * m).sum(1) / np.maximum(m.sum(1), 1e-9)
        return (pooled / np.linalg.norm(pooled, axis=1, keepdims=True)).astype(np.float32)


if __name__ == "__main__":
    # Behavioural check: a wrong forward pass produces noise and cannot hold
    # this ordering.
    m = MiniLM()
    texts = [
        "Does the company help pay for grad school?",
        "Tuition Reimbursement Policy: the company reimburses approved degree coursework.",
        "Does the company help pay for grad school?",
        "Parking garage access badges are issued by facilities.",
    ]
    e = m.encode(texts)
    print(f"identical   {float(e[0] @ e[2]):.3f}   (expect 1.000)")
    print(f"paraphrase  {float(e[0] @ e[1]):.3f}   (expect clearly high)")
    print(f"unrelated   {float(e[0] @ e[3]):.3f}   (expect clearly low)")
