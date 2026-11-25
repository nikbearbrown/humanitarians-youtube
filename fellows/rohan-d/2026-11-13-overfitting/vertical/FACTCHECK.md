# FACTCHECK — claude-liam-overfitting

Verdicts: PASS · CORRECTED · EXEMPT. "Run" = recomputed by `experiment.py` (numpy polyfit, seeds 3 / 99 / 5; output saved in `experiment_output.txt`).

| # | Beat | Claim | Verdict | Source | Fix |
|---|---|---|---|---|---|
| 1 | B02 | 8 points drawn from y = 2x plus Gaussian noise (sd 0.25), seed 3 | PASS | run | stated as "scattered around a rising line" |
| 2 | B02 | Degree 1: train error 0.099, test error 0.074 (mean squared error, 200 fresh points) | PASS | run: 0.0987, 0.0737 | — |
| 3 | B03 | Degree 7 through 8 points has train error 0 | PASS | 8 points determine a degree 7 polynomial exactly; run 0.0000 | — |
| 4 | B04 | Degree 7 test error 0.221, about three times the line's 0.074 | PASS | run: 0.2211 / 0.0737 = 3.0 | — |
| 5 | B05 | Train error falls monotonically from 0.099 to 0 across degrees 1–7 | PASS | run: .0987 .0913 .0851 .0358 .0308 .0012 .0000 | — |
| 6 | B05 | Test error is near 0.08 through degree 3, then 0.139 at degrees 4–5, up to 0.221 | PASS | run: .0737 .0834 .0831 .1390 .1390 .2109 .2211 | "near point oh eight" covers 0.074–0.083 |
| 7 | B06 | With 40 points, degree 7: train 0.035, test 0.066 | PASS | run: 0.0353, 0.0655 | — |
| 8 | B06, BVDT | Gap shrinks (0.221 train-test gap vs 0.030) | PASS | run | not narrated as a number |
| 9 | B07 | Irreducible test error ≈ noise variance 0.25² = 0.0625 | PASS | derivation; degree 1 test 0.074 is near it | "about" in narration |
| 10 | B07 | A training error of zero sits below that floor | PASS | 0 < 0.0625 | — |
| 11 | B00, BVDT | Training error always falls as flexibility grows (nested polynomial models, least squares) | PASS | nested fits cannot increase training error; run confirms | stated for this model family |
| 12 | BHTF | With 40 points degree 7 test error falls near the noise floor | PASS | run: 0.0655 vs 0.0625 | Check line says "near" |
