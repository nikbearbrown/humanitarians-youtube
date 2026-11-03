**Repository:** [https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis](https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis)

# Mycroft ECIS — Phase 11 — Prediction System and System Monitoring

**Timeline:** September 6, 2026 – September 12, 2026

**Scope:** Next-quarter guidance prediction, pre-registered prediction logging and scoring, operational monitoring, and forecast visualization.

---

## Prediction Feature Vector
- **Signal-derived features (per company, per quarter):**
  - Prior-quarter direction and confidence
  - Trend label and trend length
  - Days since the last earnings call
- **Market-derived features:**
  - Pre-call momentum: stock return since the last call, relative to the sector ETF
  - 30-day realized volatility heading into the call
- **Sector features:**
  - Share of peers that raised, lowered, or maintained in the same quarter
- **Data sources:** the signals and outcomes databases plus yfinance only

## Prediction Models
- **Primary:** logistic regression on an 8-feature vector, kept simple because of the dataset size
- **Comparison:** XGBoost, to test non-linear interactions
- **Temporal split:** trained on all prior quarters, tested on the most recent held-out quarter
- **No leakage:** every feature is computed only from data available before the target date

## Baselines

| Baseline | Strategy |
|---|---|
| Majority class | Always predict maintained |
| Naive momentum | Predict the prior quarter's direction |

- Both baselines are strong because of the class imbalance toward maintained
- The prediction model must beat both to justify deployment

## Prediction Scorecard
- **Metrics:**
  - Brier score
  - Skill score against both baselines
  - ECE
  - Murphy decomposition
- **Two-level evaluation:**
  - **Prediction accuracy:** predicted vs. extracted guidance direction
  - **Prediction value:** whether the predicted guidance anticipates stock performance

## Prediction Log
- Append-only SQLite table following the same pre-registered design as the signal log
- **Fields:**
  - Ticker, predicted direction, predicted confidence
  - Feature vector snapshot
  - Model version and timestamp
- Predictions are written before the call, never modified, and graded after extraction

## Per-Speaker Scorecard
- Brier score, skill score, ECE, and information ratio computed separately for CFO, CEO, and analyst signals
- Validates the speaker multipliers (1.0 / 0.8 / 0.3) and identifies needed adjustments

## Reader Health Monitor
- **Per-batch metrics, per reader:**
  - Success and failure rates
  - Abstention rate
  - Average confidence
  - Retry count
- **Storage:** agents database
- **Dashboard alerts:**
  - Failure-rate anomalies (e.g. FinBERT rising from a 2% to a 20% failure rate)
  - LLM abstention spikes

## Confidence Distribution Analysis
- Plotly histogram of raw vs. calibrated confidence, split by model
- **Reveals:**
  - Clustering (e.g. 0.6–0.8)
  - Gaps (e.g. 0.3–0.4)
  - Whether the confidence gate is well placed

## Extraction Latency Logging
- **Wall-clock time per reader, per chunk:**

| Reader | Typical latency |
|---|---|
| Keyword | Microseconds |
| FinBERT | Milliseconds |
| NER | Milliseconds |
| LLM (incl. self-consistency and verification) | Seconds |

- Retry overhead logged separately in the agents database
- Supports analysis of the relationship between latency and accuracy

## Dashboard
- **Forecast view, per upcoming call:**
  - Predicted direction and confidence
  - Key feature drivers
  - Historical per-company accuracy
  - Agreement with the sector aggregate
- **Prediction vs. actual timeline:**
  - Per-ticker, colour-coded by correctness
  - Hover shows the feature vector and confidence at prediction time

## Model Research
- **Tabular models evaluated:** logistic regression, XGBoost, random forest
- **Sequential models evaluated:** ARIMA, Prophet, LSTM
- **Finding:** the data is too sparse for sequential models
  - LSTM in particular needs far more observations per ticker
- **Decision:** logistic regression remains primary, with XGBoost for comparison

## Architecture Integration (In Progress)
- Feature pipeline being adapted to support both tabular and sequential input formats
- Training loop restructured for model swapping without changes to features or evaluation
