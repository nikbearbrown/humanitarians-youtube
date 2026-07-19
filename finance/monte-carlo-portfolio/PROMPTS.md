# PROMPTS — monte-carlo-portfolio

## B01 — PROBLEM slate
Visual: fan of GBM paths diverging over 30 years
Caption: "10,000 paths. One distribution. No single answer."

## B06 — SUMMARY slate
Comparison: base P5 vs regime-switching P5 (40% lower)
Caption: "The tail tells the truth."

## B07 — NEXT STEPS slate
Headline: "Add withdrawals — probability of ruin"
4% rule: withdraw 4% per year, simulate ruin probability

## B08 — NEXT STEPS 2 slate
Code: Cholesky decomp for correlated GBM
L = np.linalg.cholesky(corr_matrix)
Z = rng.normal(0, 1, (n, steps, n_assets)) @ L.T
