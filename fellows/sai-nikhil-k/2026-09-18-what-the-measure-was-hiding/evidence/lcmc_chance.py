"""Executed evidence for weekly_updates/09-18-2, beat B02 (the math beat).

Verifies the algebra typeset on screen by running Prot2Vec's OWN shipped
functions -- prot2vec.evaluation.projection.neighborhood_preservation and
.local_continuity_meta_criterion -- on seeded random data.

Claim under test: raw neighbourhood overlap NP(k) has a non-zero floor even
when the projection carries no information, and that floor is k / (n - 1).
LCMC(k) = NP(k) - k/(n-1) is therefore the chance-corrected quantity.

Run:  PYTHONPATH=<repo>/src python3 lcmc_chance.py
"""
import numpy as np
from prot2vec.evaluation.projection import (
    neighborhood_preservation,
    local_continuity_meta_criterion,
)

SEED, N, D, K, TRIALS = 20260918, 90, 64, 10, 40

def main() -> None:
    rng = np.random.default_rng(SEED)
    np_vals, lcmc_vals = [], []
    for _ in range(TRIALS):
        # X_low carries no information about X_high: an independent draw.
        X_high = rng.standard_normal((N, D))
        X_low = rng.standard_normal((N, 2))
        np_vals.append(neighborhood_preservation(X_high, X_low, n_neighbors=K))
        lcmc_vals.append(local_continuity_meta_criterion(X_high, X_low, n_neighbors=K))
    predicted = K / (N - 1)
    print(f"seed={SEED}  n={N}  d={D}  k={K}  trials={TRIALS}")
    print(f"numpy {np.__version__}")
    print()
    print(f"predicted chance overlap  k/(n-1) = {K}/{N-1} = {predicted:.4f}")
    print(f"measured  NP(k)   mean = {np.mean(np_vals):.4f}   sd = {np.std(np_vals):.4f}")
    print(f"measured  LCMC(k) mean = {np.mean(lcmc_vals):+.4f}  sd = {np.std(lcmc_vals):.4f}")
    print()
    print(f"worked example from the README's quick.yaml run (n=90, k=10):")
    print(f"  a raw overlap of 0.200 is LCMC = 0.200 - {predicted:.4f} = {0.2 - predicted:+.4f}")
    print(f"  LCMC ceiling  1 - k/(n-1) = {1 - predicted:.4f}")

if __name__ == "__main__":
    main()
