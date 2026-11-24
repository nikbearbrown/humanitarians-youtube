# PROOF — plain-language self-review (12-point rubric)

_Drafted by Claude for Boopesh to confirm after watching._

| # | Rubric point | How this film does it | Honest grade |
|---|---|---|---|
| 1 | One clear question | "Can a fraud model be 99.9 % accurate and still useless?" (B00, B10) | strong |
| 2 | Framework | four boxes → recall and precision → cutoff → cost of each mistake (B40–B60) | strong |
| 3 | Reusable rubric | "check recall, precision and cost, not accuracy" when the target is rare (B70) | strong |
| 4 | Worked example | real run on 85,443 test transactions; every chart from `results.json` / `curves.npz` | strong |
| 5 | Math shown properly | two typeset formulas only (recall, precision), each with a plain-words question | good |
| 6 | Falsifiability / sanity | the baseline makes the trap measurable: 99.8 % with 0 caught; two models with equal accuracy and 66 vs 127 caught | good |
| 7 | Edge / limits | synthetic data, chosen separability, invented cost ratio, real systems use more signals, fraud drifts (B60, B70) | good |
| 8 | Active task | B80 prompt: rerun with a 10:1 cost ratio, report the new cutoff and frauds lost | good |
| 9 | Friction recorded | FRICTIONAL.md: blocked Kaggle, class_sep change, 1 in 580 vs 600, trimmed length | good |
| 10 | Sources | dataset description read from a verbatim copy; paper venue from search (⚠️ marked) | partial |
| 11 | Disclosure | AI voice disclosed in the first sentence and on the outro | strong |
| 12 | Length / pacing | landscape 2:23, Short 0:53, both < 3 min | ok |

Weakest point: no real data. The film shows the trap with synthetic data at the real fraud rate; how well these
particular models would do on real transactions is not tested here.
