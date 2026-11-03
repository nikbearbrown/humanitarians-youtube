**Repository:** [https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis](https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis)

# Mycroft ECIS — Phase 12 — Consensus Integration, Cross-Company Analysis, and Evaluation Refinement

**Timeline:** September 13, 2026 – September 19, 2026

**Scope:** Completion of the modular prediction architecture, analyst consensus integration, guidance surprise scoring, cross-company correlation, and refined evaluation methodology.

---

## Prediction Architecture Completion
- Modular training loop for logistic regression and XGBoost on a shared feature pipeline
- Model versioning recorded on every prediction log entry
- Verified that swapping models preserves the prediction Scorecard chain

## Feature Pipeline Refinement
- **Single-quarter tickers:** excluded from trend features
- **Missing yfinance data:** falls back to sector-only features
- **Sector aggregates with fewer than 3 reporting peers:** flagged as low-confidence
- **Normalization:** z-score per feature across the training set, for logistic regression stability

## Analyst Consensus Integration
- Consensus EPS and revenue estimates per ticker and quarter, sourced from FMP
- **New feature:** delta between the latest extracted guidance and consensus

| Delta | Implied direction |
|---|---|
| Large positive (guiding above consensus) | Raised |
| Large negative (guiding below consensus) | Lowered |
| Small | Maintained |

## Guidance Surprise Score
- Magnitude of deviation between the extracted direction and the consensus-implied direction
  - Example: raising when consensus expected maintained scores high
  - Example: raising when consensus also expected a raise scores low
- Stored on the signal record and exposed in the signal explorer

## Cross-Company Signal Correlation
- Pairwise correlation of guidance direction over rolling quarterly windows
- Clustering identifies supply-chain links and shared demand drivers
- **Storage:** matrix persisted in SQLite and refreshed after each extraction batch
- Pairs with correlation above 0.7 flagged for the dashboard

## Leading and Lagging Indicators
- Time-lagged cross-correlation at a one-quarter offset
- Classifies companies as leading or lagging their peers
- Leaders treated as early indicators of sector-wide guidance shifts
- Results stored in the agents database

## Confidence-Stratified Evaluation
- **Tiers:** high (> 0.8), medium (0.5–0.8), low (< 0.5)
- Brier score, skill score, ECE, and information ratio computed per tier
- Tests whether confidence carries real information; marginal differences between tiers trigger recalibration

## Sector-Normalized Scoring
- Excess return computed against sector ETFs (e.g. SMH for semiconductors, IGV for software) instead of SPY
- Removes sector-wide movements
  - Example: a stock up 5% while its sector rose 8% is graded as underperforming
- Outcomes schema extended to store both broad-market and sector-normalized excess returns

## Dashboard
- **Surprise analysis:**
  - Sortable surprise-score column
  - Surprise distribution histogram
  - Surprise vs. calibrated confidence scatter plot
- **Correlation heatmap:**
  - Ticker × ticker grid with coefficient and overlapping-quarter count on hover
  - Dendrogram clustering
  - Toggle between contemporaneous and one-quarter-lagged correlation
- **Confidence-stratified Scorecard:**
  - Per-tier bar charts for Brier score, skill score, and ECE
  - Per-tier calibration curves

## Combined Evaluation
- Full extraction and prediction re-run with all Phase 12 features enabled
- Scorecard run with sector-normalized returns and confidence stratification across 25 tickers
- Confirmed that consensus features improve prediction accuracy over the Phase 11 baseline
