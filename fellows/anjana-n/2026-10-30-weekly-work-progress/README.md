**Repository:** [https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis](https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis)

# Mycroft ECIS — Phase 18 — Calibration, Signal Contradiction, Explainability, and OOD Detection

**Timeline:** October 25, 2026 – October 31, 2026

**Scope:** Probability calibration, intra-call signal contradiction detection, SHAP-based explainability with plain-English explanations, and out-of-distribution detection.

---

## Probability Calibration
- **Platt scaling:** logistic regression on model outputs vs. actual outcomes, fitted separately for each signal type.
- **Isotonic regression:** alternative method, compared against Platt scaling for each signal type and sample size.
  - Minimum bin size of 10.
  - Falls back to Platt scaling for signal types with fewer than 50 samples.
- **Temperature scaling:** applied to MLP outputs.
- **Revision model recalibration:** all six models recalibrated with the best-fit method for each:
  - logistic regression
  - XGBoost
  - Random Forest
  - LightGBM
  - CatBoost
  - MLP
- **Validation:** decile binning with expected vs. observed accuracy (reliability diagrams).
- **Expected calibration error:** computed per model and per signal type.
- **Finding:**
  - Hedging and dodge signals were overconfident: predicted 0.8, observed 0.65.
  - Tone shift was underconfident: predicted 0.6, observed 0.75.



## Explainability
- **SHAP:** integrated across XGBoost, LightGBM, Random Forest, and CatBoost.
  - CatBoost uses a numeric-only adapter.
- **Waterfalls:** generated and stored for every guidance revision prediction.
- **Plain-English templates:** describe the most important contributing features.
- **Explanation pipeline:** produces readable summaries.
  - Example: "flagged because hedging rose 40% while CEO–CFO divergence hit a 4-quarter high".

## Out-of-Distribution (OOD) Detection
- **Mahalanobis distance:** fitted on the training feature distribution.
  - A Ledoit-Wolf shrinkage estimator prevents singular covariance matrices.
- **Threshold:** the 95th percentile of training distances, set on a held-out validation set.
- **Isolation forest:** a secondary detector with contamination set to 0.05.
- **Confidence reduction:** flagged transcripts automatically lose confidence by a configurable factor.
- **Storage:** OOD scores are stored with transcript metadata in PostgreSQL.

## Dashboard
- **Calibration curves:** filterable by signal type, model, and quarter.
- **Contradiction alerts:** shown per call, with severity and resolution.
- **SHAP waterfall charts:** one per prediction.
- **OOD anomaly feed:** flagged transcripts with their scores.
- **Explanations:** the plain-English explanation appears alongside each prediction.

## Validation
- **Calibration:** curves checked per model and per signal type with decile-binned reliability diagrams.
- **Integration testing:** run across all new modules (`tests/test_phase18.py`).