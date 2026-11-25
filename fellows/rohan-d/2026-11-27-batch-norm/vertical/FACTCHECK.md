# FACTCHECK — claude-liam-batch-norm

Verdicts: PASS · CORRECTED · EXEMPT. "Run" = recomputed by `experiment.py` (numpy; seed 4 for the regression and batch-size runs).

| # | Beat | Claim | Verdict | Source | Fix |
|---|---|---|---|---|---|
| 1 | B02, B03 | Batch A = [2,4,6,8]: mean 5, variance 5, std 2.236 | PASS | run | "two point two four" |
| 2 | B03 | A − mean = [−3,−1,1,3]; normalized [−1.3416, −0.4472, 0.4472, 1.3416] | PASS | run | rounded to 1.34, 0.45 |
| 3 | B04 | Batch B = [200,400,600,800]: mean 500, std 223.6 → same normalized values | PASS | run | "two hundred twenty-four" |
| 4 | B05 | Condition number of the raw problem (features ~5, ~500, plus a constant) is 3,182,113 | PASS | run: eigenvalues 0.0897, 6.41, 285,336 | "three million"; synthetic regression (40 points, seed 4) |
| 5 | B05 | Normalized features: condition number 1.4 | PASS | run: eigenvalues 0.844, 1.0, 1.156 | — |
| 6 | B05 | Normalized, GD at step 1/λmax is within 0.001 of the optimal loss in 4 steps | PASS | run | step size 0.865 |
| 7 | B05 | Raw features at the largest stable step (1/λmax ≈ 0.000004) have not reached that in 100,000 steps | PASS | run: None | "hasn't arrived after a hundred thousand" |
| 8 | B06 | γ=2, β=1 on the normalized A gives [−1.6833, 0.1056, 1.8944, 3.6833] | PASS | run | rounded |
| 9 | B07 | Std of the batch mean for N(0,1) data: size 1 → 1.00, 2 → 0.71, 8 → 0.35, 32 → 0.18 | PASS | run (≈ 1/√size) | — |
| 10 | B07 | A batch of one normalizes to 0 | PASS | run (ε = 1e-5 in the denominator) | — |
| 11 | B01, B05 | Batch norm in the original paper was motivated by internal covariate shift; the optimization-conditioning view used here is the common modern explanation | EXEMPT | Santurkar et al. 2018 argue smoothing, not covariate shift | film claims only the conditioning effect it computes |
