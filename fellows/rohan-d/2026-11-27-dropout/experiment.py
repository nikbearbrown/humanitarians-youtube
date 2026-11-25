"""Every number the dropout film shows (numpy; seed 6 for the worked mask, 11 for the five more, 3 for the 10,000)."""
import numpy as np, itertools
a = np.arange(1, 9, dtype=float)          # eight unit activations 1..8, sum 36
print("activations", a.tolist(), "sum", a.sum(), "sum of squares", float((a ** 2).sum()))
rng = np.random.default_rng(6)
p = 0.5
mask = (rng.random(8) >= p).astype(float)  # 1 = kept
print("mask (1 = kept):", mask.astype(int).tolist(), "kept:", [int(x) for x, m in zip(a, mask) if m])
print("kept sum", float((a * mask).sum()), " scaled x2 output", float((a * mask).sum() / (1 - p)))
print("-- five more masks (scaled outputs):")
rng2 = np.random.default_rng(11)
outs = []
for _ in range(5):
    m = (rng2.random(8) >= p).astype(float)
    outs.append(float((a * m).sum() / (1 - p)))
print(outs)
big = np.random.default_rng(3)
M = (big.random((10000, 8)) >= p).astype(float)
o = (M * a).sum(axis=1) / (1 - p)
print("10,000 masks: mean scaled output", round(float(o.mean()), 3), " unscaled mean", round(float((M * a).sum(axis=1).mean()), 3), " std", round(float(o.std()), 3))
print("exact average over all 2^8 = 256 masks (scaled):",
      float(np.mean([ (np.array(m) * a).sum() / (1 - p) for m in itertools.product([0, 1], repeat=8)])))
print("-- spread by drop probability (exact std of scaled output)")
for pp in (0.1, 0.5, 0.9):
    print(f"p {pp}: scale {1/(1-pp):.3f}  std {np.sqrt((a**2).sum() * pp / (1 - pp)):.2f}")
