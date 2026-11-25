"""Real sentence embeddings for the embedding-space beat (all-MiniLM-L6-v2, ONNX, run locally).

    python3 embed.py > embed.json

Mean-pooled, L2-normalised 384-dimension vectors (the model card's recipe), projected to 2-D with
PCA (numpy SVD). The film plots these 2-D points; the cosine similarities are from the full vectors.
"""
import json
import numpy as np
import onnxruntime as ort
from huggingface_hub import hf_hub_download
from tokenizers import Tokenizer

REPO, REV = 'sentence-transformers/all-MiniLM-L6-v2', '1110a243fdf4706b3f48f1d95db1a4f5529b4d41'
GROUPS = {   # chosen from four candidate sets as the one whose 2-D projection separates best (silhouette 0.70)
    'animals': ['cat', 'dog', 'horse', 'rabbit'],
    'fruit': ['apple', 'banana', 'mango', 'cherry'],
    'sports': ['football', 'tennis', 'soccer', 'basketball'],
    'music': ['guitar', 'piano', 'violin', 'drums'],
}
QUERY = 'kitten'

tok = Tokenizer.from_file(hf_hub_download(REPO, 'tokenizer.json', revision=REV))
tok.enable_padding(pad_id=0, pad_token='[PAD]')
sess = ort.InferenceSession(hf_hub_download(REPO, 'onnx/model.onnx', revision=REV))


def embed(texts):
    enc = tok.encode_batch(texts)
    ids = np.array([e.ids for e in enc], dtype=np.int64)
    mask = np.array([e.attention_mask for e in enc], dtype=np.int64)
    feeds = {'input_ids': ids, 'attention_mask': mask, 'token_type_ids': np.zeros_like(ids)}
    feeds = {k: v for k, v in feeds.items() if k in {i.name for i in sess.get_inputs()}}
    hidden = sess.run(None, feeds)[0]
    m = mask[..., None].astype(np.float32)
    v = (hidden * m).sum(1) / m.sum(1)
    return v / np.linalg.norm(v, axis=1, keepdims=True)


words = [w for ws in GROUPS.values() for w in ws]
group_of = {w: g for g, ws in GROUPS.items() for w in ws}
V = embed(words + [QUERY])
X = V - V[:-1].mean(0)
_, _, vt = np.linalg.svd(X[:-1], full_matrices=False)
P = X @ vt[:2].T
sim = V @ V.T
q = len(words)
nearest = sorted(((float(sim[q, i]), w) for i, w in enumerate(words)), reverse=True)

# within-group vs across-group mean cosine
within = [sim[i, j] for i in range(q) for j in range(q) if i < j and group_of[words[i]] == group_of[words[j]]]
across = [sim[i, j] for i in range(q) for j in range(q) if i < j and group_of[words[i]] != group_of[words[j]]]
print(json.dumps({
    'model': REPO, 'revision': REV, 'dimensions': int(V.shape[1]), 'projection': 'PCA, 2 components',
    'points': [{'word': w, 'group': group_of.get(w, 'query'), 'x': round(float(P[i, 0]), 4), 'y': round(float(P[i, 1]), 4)}
               for i, w in enumerate(words + [QUERY])],
    'query': QUERY, 'nearest_to_query': [{'word': w, 'cosine': round(s, 3)} for s, w in nearest[:5]],
    'farthest_from_query': [{'word': w, 'cosine': round(s, 3)} for s, w in nearest[-3:]],
    'pairs': {f'{a}~{b}': round(float(sim[words.index(a), words.index(b)]), 3)
              for a, b in [('cat', 'dog'), ('cat', 'guitar'), ('apple', 'mango'), ('football', 'soccer'), ('piano', 'banana')]},
    'mean_cosine_within_group': round(float(np.mean(within)), 3),
    'mean_cosine_across_groups': round(float(np.mean(across)), 3),
}, indent=1))
