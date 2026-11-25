# FACTCHECK — claude-liam-cross-entropy

Verdicts: PASS · CORRECTED · EXEMPT. "Run" = recomputed by `experiment.py` (pure Python; output saved in `experiment_output.txt`).

| # | Beat | Claim | Verdict | Source | Fix |
|---|---|---|---|---|---|
| 1 | B00, B02 | Softmax of scores 2.0, 1.0, 0.1 gives shares 0.659, 0.242, 0.099 (66%, 24%, 10%), summing to 1 | PASS | run | — |
| 2 | B00, B03 | With cat as the right answer, loss = −ln 0.659 = 0.417 | PASS | run | — |
| 3 | B03 | Loss is minus the natural log of the share given to the right answer (single-example cross-entropy with a one-hot target) | PASS | definition | — |
| 4 | B04 | −ln p: p=0.9 → 0.105, 0.5 → 0.693, 0.1 → 2.303, 0.01 → 4.605 | PASS | run | narration rounds to 0.1, 0.7, 2.3, 4.6 |
| 5 | B00 | "A 1% share costs 4.6, a 50% share costs 0.7" | PASS | run (4.605, 0.693) | — |
| 6 | B05 | Model A true-class shares 0.9, 0.9, 0.1; Model B 0.6, 0.6, 0.4; both get 2 of 3 right (share > 0.5): accuracy 67% | PASS | run | "right" means the largest share; with 3 classes shown as a two-way share on screen — see #7 |
| 7 | B05 | Mean loss A = 0.84, B = 0.65 | PASS | run: 0.8378, 0.6460 | Screen says "mean loss"; examples are the true-class shares only, stated on screen as Q1–Q3 |
| 8 | B06 | Gradient of the loss w.r.t. each score is share − answer (answer is 1 for the right class, 0 otherwise) | PASS | derivation: d(−ln softmax)/dz_i = p_i − y_i | equation on screen |
| 9 | B06 | Slopes −0.341, +0.242, +0.099 | PASS | run | — |
| 10 | B06 | One step, size 1.0: scores 2.0, 1.0, 0.1 → 2.341, 0.758, 0.001; loss 0.417 → 0.264 | PASS | run: new shares 0.768, 0.158, 0.074; loss 0.2636 | scores applied directly (not through network weights); said "the score", not "the weights" |
| 11 | B07 | Share 0 gives infinite loss | PASS | −ln 0 = ∞ | — |
| 12 | B07 | Clipping at 1e-12 gives 27.63 | PASS | run | "one in a trillion" = 1e-12 |
| 13 | B07 | One such mistake outweighs a thousand near-perfect answers (1,000 × −ln 0.99 = 10.05 < 27.63) | PASS | run arithmetic | bar labelled "1,000 answers at 99%" and 10.05 |
| 14 | BVDT, BHTF | Class costs when each class is right: 0.417, 1.417, 2.317 | PASS | run: 0.417, −ln 0.2424 = 1.417, 2.317 | — |
| 15 | B07 | Real code clips probabilities before the log | PASS | standard practice (epsilon clip / log-sum-exp) | worded as "real code clips" |
