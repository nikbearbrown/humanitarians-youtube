# SOURCES — It Tested Clean

Week ending 2026-11-20 · `ai-` track.

## Primary evidence — generated here

| File | What it establishes |
|---|---|
| `skew_evidence.py` | The whole argument: a correctly fitted model, four ordinary serving-time feature disagreements, the accuracy each costs, and what a standard drift check reports depending on where it is pointed |
| `skew_results.json` | Machine-readable output; the beat sheet is populated **from this file**, never retyped |

**Seed `20261120`**, `numpy.random.default_rng`, no wall clock.

**No sklearn.** Logistic regression (batch gradient descent), AUC (rank-based,
ties averaged) and PSI are implemented in the script. That is deliberate: the
toolkit's dependency floor is numpy + scipy, and adding a dependency for one
reel is not worth it when the needed maths is thirty lines. It also means the
fit is fully inspectable — which mattered, because the first version of it was
wrong (see `FACTCHECK.md`, correction 1).

### Reproduce

```bash
python skew_evidence.py
```

Seconds to run.

## Method, stated plainly

- **Data:** 40,000 rows, time-ordered, 70/30 split. Features are tenure,
  recency and a 30-day spend aggregate. The label is drawn from a logistic
  function of the standardised features with stated coefficients.
- **Model:** logistic regression, batch gradient descent to convergence on
  features standardised with **train** statistics. The standardiser is frozen
  and applied identically on both paths — the skew is upstream of it.
- **The skews:** each replaces the serving-time value of one feature with a
  plausible alternative computation. None raises; every one returns a
  well-formed number.
- **Metrics:** accuracy at the shipped threshold (0.5) as the headline, with
  AUC, log loss and mean predicted probability alongside. Accuracy is the
  headline because it is what a product acts on, and because AUC understates
  calibration damage.
- **PSI:** ten quantile bins fitted on the training distribution, computed
  twice — once against the values the model actually received, once against
  the warehouse table.

## Prior work this is consistent with

The phenomenon is well known in ML engineering; the reel re-derives it rather
than citing it, and no figure is taken from any of these.

- **Sculley et al. (2015)**, *Hidden Technical Debt in Machine Learning
  Systems*, NeurIPS — training/serving skew as a named failure mode.
- **Breck et al. (2019)**, *Data Validation for Machine Learning*, SysML —
  the argument for validating what the serving path actually produces. Cited
  on screen in a previous reel (`ai-both-sides-passed`, 2026-10-30), not here.

## Not used

No screenshots, no lifted figures, no vendor benchmarks, no estimate of how
common skew is in practice.
