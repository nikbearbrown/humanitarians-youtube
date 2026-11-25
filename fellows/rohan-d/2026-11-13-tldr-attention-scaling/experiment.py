"""S2 key case: why divide attention scores by sqrt(d_k)?
Real computation, seeded. q, k components iid N(0,1) (paper footnote 4 assumption).
Run: python experiment.py > experiment_output.txt
"""
import numpy as np

SEED = 7
rng = np.random.default_rng(SEED)
N_KEYS = 6        # one query attends over 6 keys
TRIALS = 20000

def softmax(x):
    e = np.exp(x - x.max(axis=-1, keepdims=True))
    return e / e.sum(axis=-1, keepdims=True)

print(f"seed={SEED} keys={N_KEYS} trials={TRIALS}")
print(f"{'d_k':>5} | {'var(q.k)':>9} | {'std raw':>8} | {'max w raw':>9} | {'max w scaled':>12} | {'grad raw':>8} | {'grad scaled':>11}")
for d in (4, 16, 64, 256, 512, 2048):
    q = rng.standard_normal((TRIALS, 1, d))
    k = rng.standard_normal((TRIALS, N_KEYS, d))
    s = (q * k).sum(-1)                 # raw dot products, shape (TRIALS, N_KEYS)
    s_scaled = s / np.sqrt(d)
    p_raw, p_sc = softmax(s), softmax(s_scaled)
    # softmax saturation: mean of the largest weight, and mean of the largest
    # diagonal Jacobian entry p(1-p) (the gradient that can flow back)
    gr = (p_raw * (1 - p_raw)).max(-1).mean()
    gs = (p_sc * (1 - p_sc)).max(-1).mean()
    print(f"{d:>5} | {s.var():>9.2f} | {s.std():>8.2f} | {p_raw.max(-1).mean():>9.3f} | {p_sc.max(-1).mean():>12.3f} | {gr:>8.4f} | {gs:>11.4f}")

# One concrete, reproducible instance for the film: a single query, d=512
rng = np.random.default_rng(SEED)
q = rng.standard_normal(512); K = rng.standard_normal((N_KEYS, 512))
s = K @ q
print("\nINSTANCE d_k=512, one query, 6 keys")
print("raw scores   :", np.round(s, 1))
print("raw softmax  :", np.round(softmax(s), 3))
print("scaled scores:", np.round(s / np.sqrt(512), 2))
print("scaled softmax:", np.round(softmax(s / np.sqrt(512)), 3))
rng = np.random.default_rng(SEED)
q = rng.standard_normal(4); K = rng.standard_normal((N_KEYS, 4))
s = K @ q
print("\nINSTANCE d_k=4, one query, 6 keys")
print("raw scores   :", np.round(s, 2))
print("raw softmax  :", np.round(softmax(s), 3))
