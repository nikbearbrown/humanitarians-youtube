"""kv_cache_toy.py — executable evidence for claude-hai-kv-caching.

A single-head causal attention layer with random (seeded) weights. It decodes the
same sequence two ways and checks they agree:

  uncached — at every step, re-project K and V for ALL tokens so far and recompute
             the full causal attention matrix (what a model without a cache must do)
  cached   — at every step, project K and V for the NEW token only, append them to
             a cache, and attend with the new token's single query

It counts the work each way (K/V projections, query-key scores) and prints the
KV-cache size formula for one published model shape (Llama 2 7B: 32 layers,
32 heads x 128 dims, fp16, no grouped-query attention).

Toy weights; the counts are exact for this layer, not a benchmark of any real model.
"""
import numpy as np

SEED = 7
D = 16          # model / head width for the toy
N = 12          # tokens decoded

rng = np.random.default_rng(SEED)
Wq, Wk, Wv = (rng.standard_normal((D, D)) / np.sqrt(D) for _ in range(3))
X = rng.standard_normal((N, D))      # the token embeddings, one row per token


def softmax(z):
    z = z - z.max(axis=-1, keepdims=True)
    e = np.exp(z)
    return e / e.sum(axis=-1, keepdims=True)


def uncached():
    outs, kv_proj, scores = [], 0, 0
    for t in range(1, N + 1):
        x = X[:t]
        Q, K, V = x @ Wq, x @ Wk, x @ Wv      # recompute every row
        kv_proj += t
        S = Q @ K.T / np.sqrt(D)
        S = np.where(np.tril(np.ones((t, t))) > 0, S, -np.inf)   # causal mask
        scores += t * (t + 1) // 2
        outs.append((softmax(S) @ V)[-1])     # only the last row is the new output
    return np.array(outs), kv_proj, scores


def cached():
    outs, kv_proj, scores = [], 0, 0
    Kc, Vc = np.empty((0, D)), np.empty((0, D))
    for t in range(1, N + 1):
        x = X[t - 1:t]
        q = x @ Wq
        Kc = np.vstack([Kc, x @ Wk])          # append, never recompute
        Vc = np.vstack([Vc, x @ Wv])
        kv_proj += 1
        s = q @ Kc.T / np.sqrt(D)
        scores += t
        outs.append((softmax(s) @ Vc)[0])
    return np.array(outs), kv_proj, scores


a, kv_u, sc_u = uncached()
b, kv_c, sc_c = cached()
print(f"seed={SEED} d={D} tokens={N}")
print(f"max |uncached - cached| = {np.abs(a - b).max():.2e}   (same outputs)")
print(f"K/V projections  uncached={kv_u}  cached={kv_c}")
print(f"query-key scores uncached={sc_u}  cached={sc_c}")

print("\nwork for ONE new token at position t (query-key scores):")
print(f"{'t':>6} {'uncached t(t+1)/2':>20} {'cached t':>10}")
for t in (10, 100, 1000):
    print(f"{t:>6} {t * (t + 1) // 2:>20,} {t:>10,}")

L, H, DH, BYTES = 32, 32, 128, 2
per_tok = 2 * L * H * DH * BYTES
print(f"\nKV cache = 2 (K and V) x layers x heads x head_dim x bytes x tokens")
print(f"Llama 2 7B shape: 2 x {L} x {H} x {DH} x {BYTES} B = {per_tok:,} B = {per_tok / 2**20:.2f} MiB per token")
for n in (1024, 2048, 4096):
    print(f"{n:>6} tokens -> {per_tok * n / 2**30:.2f} GiB")
