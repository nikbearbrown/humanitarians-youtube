# SOURCES — Overfitting, When a Perfect Score Lies

There is no single source article. This is a concept film written from standard references, and every number shown is executed locally.

## References
- T. Hastie, R. Tibshirani, J. Friedman, *The Elements of Statistical Learning*, 2nd ed. (Springer, 2009):
  - §2.4, squared-error loss
  - §7.2–7.3, test error and the bias–variance decomposition; Fig. 7.1 is the classic training-vs-test curve
  - §7.10, cross-validation and the "wrong way" to select
- G. James, D. Witten, T. Hastie, R. Tibshirani, *An Introduction to Statistical Learning* (Springer), §2.2, assessing model accuracy and the U-shaped test MSE.
- C. M. Bishop, *Pattern Recognition and Machine Learning* (Springer, 2006), §1.1, polynomial curve fitting on noisy sin(2πx) data. This is the textbook ancestor of this film's demo. Here the curve is sin(πx) on [−1, 1], and no figure is redrawn.
- G. C. Cawley, N. L. C. Talbot (2010), "On Over-fitting in Model Selection and Subsequent Selection Bias in Performance Evaluation", *JMLR* 11: the B07 point.
- M. Belkin, D. Hsu, S. Ma, S. Mandal (2019), "Reconciling modern machine-learning practice and the classical bias–variance trade-off", *PNAS* 116(32): why B01 and the verdict say "can mean" and not "means".

## Executable evidence
- `demo/overfit_demo.py` (pure Python + numpy) writes `demo/evidence.json` and `demo/RUN-LOG.txt`.
- Run environment: Python 3.12.13, numpy 2.5.5, Windows 11.
- Runtime is about 7 s. Two consecutive runs are byte-identical (sha256 `4c615e57…2113`).
- `make_sheet.py` reads every on-screen number from `evidence.json`. It also asserts that every spoken figure (numbers as words) still matches the evidence, so a re-run with changed data fails loudly instead of drifting.

## Corrections applied (DOUBLE-CHECK LAW)
- **BVDT:** "usually means the noise was memorized" became "can mean". Interpolating models can generalize (Belkin et al. 2019). See FACTCHECK #1.
- **B07:** the "peeked score beat the noise floor four times in ten" statistic was dropped. It reflects small-sample skew, not selection, so it was replaced by a controlled comparison. See FACTCHECK #20.
- **BHTF rubric:** "zero in training" became "essentially zero". Naive `np.polyfit` is ill-conditioned at degree 15. See FACTCHECK #22.
- **De-dating:** no model names, parameter counts or dates appear in the narration.

## Seeds
| What | Seed |
|---|---|
| The film's dataset (16 train / 1,000 test) | numpy `default_rng(15)` |
| Extra training points for B06 (nested after the 16) | `default_rng(16)` |
| 500-dataset robustness check (B05 chip) | `default_rng(1000)` |
| Pick-by-validation experiment (B07, 1,000 trials) | `default_rng(2024)` |
| Hesitant writer | `claude-liam-overfitting-b01` |
| Outro mascot and polarity | slug `claude-liam-overfitting` |

Seed 15 was fixed before results were inspected. Its degree sweep is typical: the 500-dataset medians have the same shape.
