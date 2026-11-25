"""BHTF transfer check: q,k components with variance 4 (std 2), d_k=64."""
import numpy as np
rng = np.random.default_rng(7)
d = 64; n = 200000
q = 2 * rng.standard_normal((n, d)); k = 2 * rng.standard_normal((n, d))
s = (q * k).sum(1)
print("var(q.k) =", round(s.var(), 1), " expected 4*4*64 =", 4*4*64)
print("var(q.k/sqrt(d)) =", round((s/np.sqrt(d)).var(), 1), " expected 16")
print("var(q.k/(4*sqrt(d))) =", round((s/(4*np.sqrt(d))).var(), 3), " expected 1")
