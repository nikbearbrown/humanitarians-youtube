# FACTCHECK — claude-liam-dropout

Verdicts: PASS · CORRECTED · EXEMPT. "Run" = recomputed by `experiment.py` (numpy; seeds 6, 11, 3). Activations 1…8 (sum 36, sum of squares 204); inverted dropout: keep with probability 1 − p, scale survivors by 1/(1 − p).

| # | Beat | Claim | Verdict | Source | Fix |
|---|---|---|---|---|---|
| 1 | B02 | Activations 1…8 sum to 36 | PASS | arithmetic | — |
| 2 | B02 | Seed-6 mask at p = 0.5 keeps units 1, 5, 6, 7 (sum 19) | PASS | run | — |
| 3 | B03 | Survivors scaled by 1/(1 − 0.5) = 2; output 38 | PASS | run | — |
| 4 | B04 | Five more masks give outputs 18, 40, 44, 22, 28 | PASS | run (seed 11) | — |
| 5 | B04 | 10,000 masks: mean scaled output 35.98 | PASS | run: 35.981 | — |
| 6 | B05 | Unscaled mean is 18 (half of 36) | PASS | exact: E = (1 − p)·36 = 18; run 17.99 | — |
| 7 | B06 | 2⁸ = 256 masks; average of the 256 scaled outputs is exactly 36 | PASS | run | stated "for a plain sum"; for nonlinear networks the test-time rule is an approximation |
| 8 | B07 | Std of scaled output: p 0.1 → 4.76, 0.5 → 14.28, 0.9 → 42.85 | PASS | exact formula √(Σa²·p/(1−p)); run | "about five, fourteen, forty-three" |
| 9 | B07 | Forgetting to turn dropout off at test time gives run-to-run different answers | PASS | follows from random masks | — |
| 10 | B01 | Dropout can be viewed as training many thinned networks that share weights | PASS | standard (Srivastava et al., 2014) | framed as a view, not a proof |
| 11 | BHTF | Means ≈ 36 for every p; std ≈ 4.8, 14.3, 42.9 | PASS | run | "about" |
