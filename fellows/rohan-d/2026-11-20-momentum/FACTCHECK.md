# FACTCHECK — claude-liam-momentum

Verdicts: PASS · CORRECTED · EXEMPT. "Run" = recomputed by `experiment.py` (pure numpy; deterministic, no seeds). Loss f(x,y) = 0.5(x² + 25y²), start (4, 1), step size 0.07, heavy-ball update v ← βv + ∇f, θ ← θ − ηv.

| # | Beat | Claim | Verdict | Source | Fix |
|---|---|---|---|---|---|
| 1 | B02 | Plain descent (β=0) reaches loss < 0.01 in 47 steps | PASS | run | — |
| 2 | B02 | Plain path zigzags: y = 1, −0.75, 0.563, −0.422, 0.316 … | PASS | run (y multiplied by 1 − 0.07·25 = −0.75 each step) | — |
| 3 | B03 | Momentum update is v ← βv + gradient, then move against v | PASS | heavy-ball (Polyak) form with unit-weight gradient | stated on screen |
| 4 | B03 | β=0 is plain descent | PASS | algebra | — |
| 5 | B03 | β=0.8 "remembers roughly the last five slopes" | PASS | effective window 1/(1−β) = 5 | "roughly" in narration |
| 6 | B04 | β=0.5 reaches loss < 0.01 in 20 steps | PASS | run | — |
| 7 | B05 | Across-valley slopes steps 1–5: 25, −18.75, −7.81, 11.33, 1.07; velocity 25, −6.25, −10.94, 5.86, 4.0 | PASS | run | narration rounds to 25, −19, −8, 11 |
| 8 | B05 | Along-valley velocity grows from 4.0 to 6.18 | PASS | run: 4.0, 5.72, 6.18, 5.98, 5.46 | "to over six" |
| 9 | B06 | Steps to loss < 0.01: β 0→47, 0.5→20, 0.8→29, 0.9→53, 0.95→99, 0.99→none in 200 | PASS | run | — |
| 10 | B07 | β=0.9: x reaches −2.169 at step 11 | PASS | run | "minus two point two" |
| 11 | B07 | β=0.99: loss at step 200 = 1.108 | PASS | run | "one point one" |
| 12 | B00, BVDT | "A little more than halves the steps" (47 → 20) | PASS | 20/47 = 0.43 | — |
| 13 | BHTF | Same counts reproduce with the prompt's update rule | PASS | run uses exactly that rule | — |
