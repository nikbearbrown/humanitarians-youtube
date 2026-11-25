# FACTCHECK — It Tested Clean

Week ending 2026-11-20 · `ai-` track.

Every figure comes from `skew_evidence.py`, shipped in this folder. Seed
`20261120`, `numpy` only — the logistic regression, the AUC and the PSI are
written by hand rather than imported, so the script keeps the toolkit's
dependency floor and reproduces exactly.

**The experimental contract.** The model is fit **once**, on correct data,
converges, and is never retrained or modified. The standardiser is fitted on
train and frozen, and applied identically on both paths. The *only* thing that
varies between conditions is how one feature — a 30-day spend aggregate — is
computed at the moment of prediction.

---

## Verified — on screen or spoken

| # | Claim | Verdict | Source |
|---|---|---|---|
| 1 | 40,000 rows, 70/30 time-ordered split | ✅ | `N`, `TRAIN_FRAC` |
| 2 | Offline AUC **0.7975**, accuracy **73.4%** at threshold 0.5 | ✅ | `offline.auc`, `offline.acc` |
| 3 | Offline accuracy is identical under all four skews | ✅ | By construction — the offline test reads the unmodified warehouse array |
| 4 | 30-day window served as 7-day → **64.2%** (−9.2 pts) | ✅ | `skews[0]` |
| 5 | Dollars served as cents → **41.5%** (−31.9 pts) | ✅ | `skews[1]` |
| 6 | Aggregate 80% complete → **72.9%** (−0.5 pts) | ✅ | `skews[2]` |
| 7 | 12% of lookups filled with 0 → **72.0%** (−1.4 pts) | ✅ | `skews[3]` |
| 8 | Mean predicted probability: offline **0.42**, cents **0.99** | ✅ | `offline.mean_score`, `skews[1].mean_score` |
| 9 | 41.5% is worse than majority-class guessing at **59.1%** | ✅ | `offline.majority_class_acc` = 0.5912, base rate 0.4088 |
| 10 | PSI on the serving log: **5.91** and **2.04** on the two big skews | ✅ | `skews[*].psi` |
| 11 | PSI on the warehouse: **0.001**, the same for all four | ✅ | `monitoring.warehouse_psi` = 0.0011. Same by construction: the warehouse array is untouched, so the comparison is train-vs-test on identical data |
| 12 | PSI thresholds quoted (<0.1 fine, 0.1–0.25 investigate, >0.25 act) | ✅ | Stated in the script as a field rule of thumb, not as a standard |

## Corrections applied during the build

**1 — The first model was badly fit, and it would have demonstrated the wrong
thing.** The initial version fitted logistic regression on **unstandardised**
features with too few epochs. It reached AUC 0.61, overflowed `exp`, and — the
tell — two of the four "skews" *improved* the score. A monotone rescale of one
feature was raising AUC, which means the fit was over-weighting that feature,
not that skew is harmless. Shipping it would have been a demonstration of a
broken model dressed up as a demonstration of skew.

Fixed by standardising on train statistics, clipping the logit, and fitting to
convergence (4,000 epochs). Offline AUC 0.7975, and every skew now degrades
the model.

**2 — The angle I expected did not survive contact with the data.** I went in
expecting "the quiet skews are the deadly ones" — that the cases a drift check
misses would be the ones that hurt most. **The opposite is true here:** the
two low-PSI skews cost 0.5 and 1.4 points, while the two that trip the alarm
cost 9.2 and 31.9. Drift checking, pointed at the right data, works.

That angle was dropped rather than written around. The finding that replaced
it is better and is the reel's landing: the problem is not the sensitivity of
the check but **where it is pointed**.

## Claims considered and cut

- **"Drift detection doesn't work."** Contradicted by row 10. The reel says
  the opposite — pointed at the serving log, it catches the damaging cases.
- **Any figure for how common training-serving skew is in industry.** No
  source. The reel says what it *does*, never how often it happens.
- **AUC as the headline.** Measured and in the JSON, but accuracy at the
  deployed threshold is what a product actually acts on, and AUC understates
  calibration damage: under the cents skew AUC falls to 0.59 while accuracy
  falls below majority-class guessing. One metric on screen, the honest one.
- **The log-loss column.** Computed, correct, and cut for room.
- **Naming a feature-store product.** Not relevant and would date the reel.

## Scope

Synthetic data from a stated generative process, one tabular binary classifier,
one skewed feature at a time. The four skews are a **chosen catalogue** of
ordinary pipeline disagreements, not a sample of real incidents, and the reel
does not present them as one. Nothing here measures deep learning, streaming
features under real load, or multi-feature interactions.
