# Weekly Report: Week 12 (Phase 12)

**Project:** Mycroft — ECIS (Earnings Call Intelligence System) + Decision Scorecard
**Week:** September 13 – September 19, 2026
**Total hours:** 30.75

---

## Summary

- The prediction system now works across companies and against expectations:
  - **Cross-company signals:** a correlation matrix with leading/lagging indicator detection.
  - **Consensus estimates:** integrated via the FMP API, with a guidance surprise score.
- Evaluation was refined in two ways:
  - **Confidence-stratified evaluation:** exposed a bimodal pattern that the aggregate was hiding.
  - **Sector-normalized scoring:** replacing SPY with sector ETFs flipped several signals from correct to incorrect, showing that earlier aggregate metrics were overstated.
- The feature engineering pipeline was made model-agnostic, so models can be swapped without re-engineering it.
- Dashboard updates: surprise score in the Signal Explorer, a correlation heatmap, and a confidence-stratified Scorecard view.
- Outputs:
  - two Claude artifacts
  - one Substack article
  - two videos

---

## Work Completed

### Prediction System

#### 1. Complete Prediction Model Architecture Integration
*Development · Prediction System*
- Completed the prediction model architecture integration carried over from Week 11.
- **Deliverable:** prediction model architecture fully integrated
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/prediction/models.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/prediction/features.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/main.py
- **Status:** Complete

#### 2. Refine Feature Engineering Pipeline for Model Swapping Flexibility
*Development · Prediction System*
- Refined the feature engineering pipeline so that models can be swapped without re-engineering the feature layer.
- Supports logistic regression, XGBoost, and future candidates.
- **Deliverable:** model-agnostic feature engineering pipeline
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/prediction/features.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/prediction/models.py
- **Status:** Complete

#### 3. Consensus Estimates Integration via FMP API
*Development · Prediction System*
- Integrated analyst consensus estimates per ticker per quarter via the FMP API, as additional prediction features.
- **Deliverable:** consensus estimates integrated (FMP API)
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/prediction/consensus.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/prediction/features.py
- **Status:** Complete

#### 4. Guidance Surprise Score
*Development · Prediction System*
- Compares the extracted guidance direction against the consensus expectation.
- Quantifies how far actual guidance deviates from what analysts predicted.
- **Deliverable:** guidance surprise score (extracted direction vs. consensus)
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/prediction/surprise.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/prediction/consensus.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/main.py
- **Status:** Complete

#### 5. Cross-Company Signal Correlation Matrix
*Development · Prediction System*
- Built a correlation matrix showing which tickers' guidance changes predict which others.
- Surfaces supply chain, competitive, and sector-level signal propagation patterns.
- **Deliverable:** cross-company signal correlation matrix
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/extraction/correlation.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/main.py
- **Status:** Complete

#### 6. Leading/Lagging Indicator Detection Across Correlated Tickers
*Development · Prediction System*
- Detects which correlated companies' guidance changes arrive first and which follow.
- **Deliverable:** leading/lagging indicator detection
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/extraction/correlation.py
- **Status:** Complete

#### 7. Confidence-Stratified Evaluation
*Development · Prediction System*
- Split Scorecard evaluation into high, medium, and low confidence tiers.
- Tests whether the system's confidence levels correspond to actual differences in accuracy.
- **Deliverable:** confidence-stratified Scorecard evaluation
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/scoring/scorer.py
- **Status:** Complete

#### 8. Sector-Normalized Scoring
*Development · Prediction System*
- Replaced the SPY benchmark with sector-specific ETFs for outcome grading.
- Gives a more meaningful measure of relative performance within each industry.
- **Deliverable:** sector-normalized scoring (sector ETFs replacing SPY)
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/scoring/sector.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/scoring/outcome_resolver.py
- **Status:** Complete

### Dashboard

#### 9. Add Surprise Score to Signal Explorer
*Development · Dashboard*
- Added the guidance surprise score to the Signal Explorer view.
- **Deliverable:** surprise score visible in Signal Explorer
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/dashboard/app.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/dashboard/views.py
- **Status:** Complete

#### 10. Correlation Heatmap View
*Development · Dashboard*
- Added an interactive heatmap of ticker-to-ticker signal correlation patterns.
- **Deliverable:** correlation heatmap view in dashboard
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/dashboard/views.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/dashboard/app.py
- **Status:** Complete

#### 11. Confidence-Stratified Scorecard View
*Development · Dashboard*
- Added a view showing Scorecard metrics split by confidence tier.
- **Deliverable:** confidence-stratified Scorecard view in dashboard
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/dashboard/views.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/scoring/scorer.py
- **Status:** Complete

### Debugging

#### 12. Debugging and Issue Resolution
*Development · Debugging*
- Debugging across the prediction system features, the correlation matrix, and the dashboard integration.
- Main issues:
  - a ChromaDB population race condition
  - sector ETF mapping edge cases
- **Deliverable:** issues identified and resolved
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/tests/test_phase11-13.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/prediction/consensus.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/extraction/correlation.py
- **Status:** Complete

### Research

#### 13. Analysis of Cross-Company Correlation Patterns
*Research · Prediction System*
- Analyzed which cross-company signal correlations are genuine and which are spurious at the current sample size.
- Evaluated the statistical significance of the detected leading/lagging relationships.
- **Deliverable:** cross-company correlation analysis; genuine vs. spurious assessment
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/research
- **Status:** Complete

#### 14. Architecture Review
*Research · Architecture*
- Reviewed the overall system architecture with the new components included: the prediction system, the correlation matrix, and sector-normalized scoring.
- **Deliverable:** architecture review
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/architecture
- **Status:** Complete

### Artifacts

#### 15. Model Comparison Arena: Logistic Regression vs. XGBoost
*Artifact · Claude Artifact*
- Interactive head-to-head comparison of logistic regression and XGBoost on the prediction task.
- Covers accuracy, calibration, feature importance differences, and per-ticker performance.
- **Deliverable:** Claude Artifact: Model Comparison Arena
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/artifacts
- **Status:** Complete

#### 16. Prediction Feature Correlation Explorer
*Artifact · Claude Artifact*
- Interactive correlation matrix of all prediction features.
- Supports filtering, sorting, and drill-down into individual feature pairs.
- **Deliverable:** Claude Artifact: Prediction Feature Correlation Explorer
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/artifacts
- **Status:** Complete

### Writing

#### 17. Substack Article: "From SQLite to PostgreSQL + TimescaleDB"
*Writing · Substack Article*
- Examines when an ML project outgrows its database: the scaling inflection points and the migration trade-offs.
- Explains why time-series-native storage changes which queries are practical for financial signal systems.
- **Deliverable:** published Substack article
- **Link:** https://mycroftproject.substack.com/p/sqlite-postgresql-timescaledb-ml-pipeline
- **Status:** Complete (published)

### Video

Both videos follow the same split.
- **Concept, ideas, narration, and direction:** original work.
- **Assembly:** Claude, using the video generation tool created by Humanitarians AI.

#### 18. Video: "ECIS Episode 7"
*Video · Video Production*
- Weekly Mycroft project update. Covers:
  - cross-company signal correlation
  - consensus estimates integration
  - guidance surprise scoring
  - confidence-stratified evaluation
  - sector-normalized scoring
- **Deliverable:** Video: ECIS EP7
- **Links:**
  - https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-09-18-ecis-explained
  - https://drive.google.com/drive/folders/16xVbLc724aBClwvYLqwmFe7NLzH7me4R
- **Status:** Complete

#### 19. Video: "Embeddings Explainer"
*Video · Video Production*
- STEM explainer on how text embeddings work. Covers:
  - word-level representations through to sentence embeddings
  - how vector similarity captures semantic meaning
  - how embeddings power retrieval in the ECIS pipeline
- **Deliverable:** Video: Embeddings Explainer
- **Links:**
  - https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-09-18-embeddings-explainer
  - https://drive.google.com/drive/folders/1yZhSYdkvtlZOv1zxxPtIbraw2nOHYi0S
- **Status:** Complete
