#!/usr/bin/env python3
"""gpt2_inspect.py — open the smallest GPT-2 on this machine and count what Wolfram describes.

Wolfram (2023) does his examples with "the simplest GPT-2 model (from 2019)" and
states, for GPT-2: 12 attention blocks, 12 attention heads per block, embedding
vectors of length 768, a 768x768 fully connected weight matrix after the heads,
and about 50,000 tokens. This script reads the same public checkpoint
(openai-community/gpt2, model.safetensors from the local Hugging Face cache) and
measures each of those from the tensors themselves, plus the total number of
weights, which he does not state.

Then it re-runs his first figure — the top five next words after "The best
thing about AI is its ability to" — with a forward pass written out in plain
NumPy below (about 30 lines: embeddings, 12 x [layer norm, attention, MLP],
logits). No transformers library: the system install's transformers fails to
import (accelerate -> boto3), and writing the pass out is the reel's point
anyway: every part is simple arithmetic. Matching his percentages checks the
implementation.

The head count is not stored in the file; it comes from the checkpoint's
config.json (n_head). Every other number is a tensor shape.

Run:  python3 evidence/gpt2_inspect.py > evidence/gpt2_inspect.out
"""
import datetime
import glob
import hashlib
import json
import platform
from pathlib import Path

import numpy as np
import safetensors
import tokenizers
from safetensors.numpy import load_file
from tokenizers import ByteLevelBPETokenizer

CACHE = Path.home() / ".cache/huggingface/hub/models--openai-community--gpt2/snapshots"
PROMPT = "The best thing about AI is its ability to"

snap = Path(sorted(glob.glob(str(CACHE / "*")))[0])
W = load_file(str(snap / "model.safetensors"))
cfg = json.loads((snap / "config.json").read_text())
tok = ByteLevelBPETokenizer(str(snap / "vocab.json"), str(snap / "merges.txt"))

print(f"date        {datetime.datetime.now().isoformat(timespec='seconds')}")
print(f"machine     {platform.machine()} · macOS {platform.mac_ver()[0]}")
print(f"python      {platform.python_version()} · numpy {np.__version__} · "
      f"safetensors {safetensors.__version__} · tokenizers {tokenizers.__version__}")
print(f"checkpoint  openai-community/gpt2 @ {snap.name}")
print(f"sha256      model.safetensors "
      f"{hashlib.sha256((snap / 'model.safetensors').read_bytes()).hexdigest()}")

# ---------------------------------------------------------------- counting
# h.N.attn.bias is the causal mask (a constant buffer), not a learned weight.
learned = {k: v for k, v in W.items() if k.split(".")[-2:] != ["attn", "bias"]}
blocks = sorted({int(k.split(".")[1]) for k in learned if k.startswith("h.")})
total = sum(v.size for v in learned.values())
n_vocab, n_embd = W["wte.weight"].shape
n_head = cfg["n_head"]
proj = W["h.0.attn.c_proj.weight"]

print()
print("ARCHITECTURE (tensor shapes in model.safetensors; heads from config.json)")
print(f"  attention blocks          {len(blocks)}")
print(f"  heads per block           {n_head}   (n_embd {n_embd} / n_head = {n_embd // n_head} per head)")
print(f"  embedding length          {n_embd}")
print(f"  token vocabulary          {n_vocab}")
print(f"  position table            {W['wpe.weight'].shape}")
per_block = sum(v.size for k, v in learned.items() if k.startswith("h.0."))
print(f"  weights per block         {per_block:,}  (block 0; all {len(blocks)} equal: "
      f"{all(sum(v.size for k, v in learned.items() if k.startswith(f'h.{i}.')) == per_block for i in blocks)})")
print(f"  final layer norm          {W['ln_f.weight'].size + W['ln_f.bias'].size}")
print(f"  post-attention projection {proj.shape}  (h.0.attn.c_proj.weight)")
print(f"  learned tensors           {len(learned)}  (+{len(W) - len(learned)} mask buffers not counted)")
print(f"  weights, total            {total:,}  = {total / 1e6:.1f} million")
print(f"  h.0 c_proj stats          mean {proj.mean():+.5f}  std {proj.std():.5f}  "
      f"min {proj.min():+.3f}  max {proj.max():+.3f}")


# ---------------------------------------------------------------- the forward pass
def layer_norm(x, g, b, eps=1e-5):
    m = x.mean(-1, keepdims=True)
    v = ((x - m) ** 2).mean(-1, keepdims=True)
    return (x - m) / np.sqrt(v + eps) * g + b


def gelu(x):
    return 0.5 * x * (1 + np.tanh(np.sqrt(2 / np.pi) * (x + 0.044715 * x ** 3)))


def softmax(x):
    e = np.exp(x - x.max(-1, keepdims=True))
    return e / e.sum(-1, keepdims=True)


def next_word_probs(ids):
    T = len(ids)
    x = W["wte.weight"][ids] + W["wpe.weight"][:T]            # token + position
    mask = np.triu(np.full((T, T), -1e10), 1)                   # look back only
    for i in blocks:
        p = f"h.{i}."
        a = layer_norm(x, W[p + "ln_1.weight"], W[p + "ln_1.bias"])
        q, k, v = np.split(a @ W[p + "attn.c_attn.weight"] + W[p + "attn.c_attn.bias"], 3, -1)
        heads = []
        for h in range(n_head):
            s = slice(h * n_embd // n_head, (h + 1) * n_embd // n_head)
            att = softmax(q[:, s] @ k[:, s].T / np.sqrt(n_embd // n_head) + mask)
            heads.append(att @ v[:, s])
        x = x + np.concatenate(heads, -1) @ W[p + "attn.c_proj.weight"] + W[p + "attn.c_proj.bias"]
        m = layer_norm(x, W[p + "ln_2.weight"], W[p + "ln_2.bias"])
        m = gelu(m @ W[p + "mlp.c_fc.weight"] + W[p + "mlp.c_fc.bias"])
        x = x + m @ W[p + "mlp.c_proj.weight"] + W[p + "mlp.c_proj.bias"]
    x = layer_norm(x[-1], W["ln_f.weight"], W["ln_f.bias"])
    return softmax(x @ W["wte.weight"].T)                       # one score per token


ids = tok.encode(PROMPT).ids
probs = next_word_probs(ids)
print()
print(f"NEXT WORD after {PROMPT!r}  ({len(ids)} tokens: {ids})")
for i in np.argsort(-probs)[:5]:
    print(f"  {tok.decode([int(i)])!r:16} {100 * probs[i]:.1f}%   ({probs[i]:.6f})")
print("  Wolfram's figure: learn 4.5%, predict 3.5%, make 3.2%, understand 3.1%, do 2.9%")
