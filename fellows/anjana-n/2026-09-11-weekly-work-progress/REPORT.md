# Weekly Report: Week 11 (Phase 11)

**Project:** Mycroft — ECIS (Earnings Call Intelligence System) + Decision Scorecard
**Week:** September 6 – September 12, 2026
**Total hours:** 30.25

---

## Summary

- A prediction system was built on top of the extraction and scoring pipeline. The system now uses its own outputs to forecast next-quarter guidance direction.
- **Features:**
  - per-company, per-quarter feature vectors from the decision log
  - stock return since last earnings
  - sector signal aggregate
- **Models:** logistic regression and XGBoost, trained with a strict temporal split and compared against two baselines (always-predict-maintained and naive momentum).
- **Results:**
  - Logistic regression beat always-predict-maintained and marginally beat momentum.
  - XGBoost overfit at this dataset size.
- **Prediction log:** append-only and pre-registered, so forecasts are locked before each earnings call.
- **New features and dashboard views:**
  - per-speaker Scorecard breakdown
  - reader health monitor
  - extraction latency logging
  - confidence histogram
  - forecast view
  - prediction vs. actual timeline
- **Outputs:** two Claude artifacts, two Substack articles and two videos.

---

## Work Completed

### Prediction System

#### 1. Build Per-Company Per-Quarter Feature Vector from Decision Log
*Development · Prediction System*
- Constructed per-company, per-quarter feature vectors from the decision log. The features are:
  - prior direction
  - confidence
  - trend label
  - trend length
  - days since last call
- **Deliverable:** per-company per-quarter feature vector pipeline
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/prediction/features.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/main.py
- **Status:** Complete

#### 2. Pull Stock Return and Sector Signal Aggregate as Features
*Development · Prediction System*
- Added two more prediction features: stock return since last earnings, and sector-level signal aggregates.
- **Deliverable:** stock return + sector signal aggregate features
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/prediction/features.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/scoring/price_cache.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/scoring/sector.py
- **Status:** Complete

#### 3. Train Logistic Regression / XGBoost Classifier for Next-Quarter Direction
*Development · Prediction System*
- Trained logistic regression and XGBoost classifiers to predict next-quarter guidance direction.
- Used a strict temporal split to preserve point-in-time discipline.
- **Deliverable:** trained prediction classifiers (logistic regression + XGBoost) with temporal split
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/prediction/models.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/main.py
- **Status:** Complete

#### 4. Compare Against Baselines (Always-Predict-Maintained, Naive Momentum)
*Development · Prediction System*
- Benchmarked the prediction models against two baselines: always-predict-maintained and naive momentum.
- **Deliverable:** baseline comparison results
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/prediction/baselines.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/prediction/scorecard.py
- **Status:** Complete

#### 5. Prediction Scorecard (Brier, Skill Score, Calibration)
*Development · Prediction System*
- Built a prediction-specific Scorecard with three measures:
  - Brier score
  - skill score against the baselines
  - calibration metrics
- **Deliverable:** prediction Scorecard
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/prediction/scorecard.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/main.py
- **Status:** Complete

#### 6. Add Prediction Log to SQLite (Pre-Registered, Append-Only)
*Development · Prediction System*
- Added a prediction log to SQLite.
- Predictions are pre-registered before the earnings call and stored append-only, which keeps the audit trail intact.
- **Deliverable:** prediction log in SQLite (pre-registered, append-only)
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/prediction/log.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/db/init_db.py
- **Status:** Complete

#### 7. Integrate Research Findings into Prediction Model Architecture
*Development · Prediction System*
- Brought findings from the model candidate evaluation and the time series exploration into the prediction model architecture.
- **Deliverable:** prediction model architecture updated with research findings
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/prediction/models.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/prediction/features.py
- **Status:** Complete

### Feature Development

#### 8. Per-Speaker Scorecard Breakdown
*Development · Feature Development*
- Split Scorecard metrics by speaker role to validate the Week 9 weight multipliers (CFO 1.0 / CEO 0.8 / analyst 0.3).
- **Deliverable:** per-speaker Scorecard breakdown; weight multiplier validation
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/scoring/scorer.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/extraction/speaker_roles.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/dashboard/views.py
- **Status:** Complete

#### 9. Reader Health Monitor
*Development · Feature Development*
- Tracks each reader's success, failure and abstention rates per batch, with dashboard alerting.
- Surfaces degraded reader performance before it affects downstream signal quality.
- **Deliverable:** reader health monitor with dashboard alerts
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/extraction/health.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/main.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/dashboard/app.py
- **Status:** Complete

#### 10. Extraction Latency Logging Per Reader Per Chunk
*Development · Feature Development*
- Logs extraction latency for each reader on each chunk.
- Enables latency-accuracy analysis and reader performance profiling.
- **Deliverable:** per-reader per-chunk latency logging
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/extraction/latency.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/graphs/pipeline_graph.py
- **Status:** Complete

### Dashboard

#### 11. Confidence Distribution Histogram View
*Development · Dashboard*
- Added a histogram view of the confidence distribution across signals.
- **Deliverable:** confidence distribution histogram in dashboard
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/dashboard/views.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/dashboard/app.py
- **Status:** Complete

#### 12. Forecast View: Predicted Direction, Confidence, Key Drivers
*Development · Dashboard*
- Added a forecast view showing, for each upcoming earnings call, the predicted direction, the confidence level and the key feature drivers.
- **Deliverable:** forecast view in dashboard
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/dashboard/views.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/prediction/models.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/dashboard/app.py
- **Status:** Complete

#### 13. Prediction vs. Actual Timeline Per Ticker
*Development · Dashboard*
- Added a timeline view of prediction accuracy over time for each ticker, with predicted direction overlaid on the actual outcome.
- **Deliverable:** prediction vs. actual timeline view in dashboard
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/dashboard/views.py
- **Status:** Complete

### Debugging

#### 14. Debugging and Issue Resolution
*Development · Debugging*
- Resolved issues across the prediction system and the new feature integration.
- Main issues: data leakage in the sector aggregate feature, and collapsed evaluation levels in the prediction Scorecard.
- **Deliverable:** issues identified and resolved
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/tests/test_phase11-13.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/prediction/models.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/prediction/log.py
- **Status:** Complete

### Research

#### 15. Revised ML Model Candidates for Prediction
*Research · Prediction System*
- Evaluated alternative ML model candidates for the prediction layer beyond logistic regression and XGBoost.
- **Deliverable:** ML model candidate assessment
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/research
- **Status:** Complete

#### 16. Time Series Model Exploration
*Research · Prediction System*
- Explored time series modeling approaches for predicting guidance direction.
- **Deliverable:** time series model feasibility assessment
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/research
- **Status:** Complete

#### 17. Consensus Estimates API Exploration
*Research · Prediction System*
- Explored consensus estimates APIs as potential additional feature sources for the prediction model.
- **Deliverable:** consensus estimates API assessment
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/research
- **Status:** Complete

### Artifacts

#### 18. Prediction Feature Importance Viewer
*Artifact · Claude Artifact*
- Interactive artifact showing, for each ticker, the feature vector breakdown, the model coefficient weighting and a sector consensus comparison.
- Shows which features drive predictions for each company.
- **Deliverable:** Claude Artifact: Prediction Feature Importance Viewer
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/artifacts
- **Status:** Complete

#### 19. Latency vs. Accuracy Scatter
*Artifact · Claude Artifact*
- Interactive artifact plotting each signal's latency against its Scorecard accuracy.
- Points are color-coded by reader, with sliders for exploring thresholds.
- **Deliverable:** Claude Artifact: Latency vs. Accuracy Scatter
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/artifacts
- **Status:** Complete

### Writing

#### 20. Substack Article: "Logistic Regression vs. XGBoost for Guidance Direction Forecasting"
*Writing · Substack Article*
- Compares logistic regression and XGBoost for predicting next-quarter guidance direction.
- Examines the interpretability vs. performance trade-off, grounded in the ECIS prediction Scorecard results.
- **Deliverable:** published Substack article
- **Link:** https://mycroftproject.substack.com/p/logistic-regression-vs-xgboost-guidance-forecasting
- **Status:** Complete (published)

#### 21. Substack Article: "Extraction Latency as a Signal"
*Writing · Substack Article*
- Argues that extraction latency per reader per chunk is not just an infrastructure metric but an information signal.
- Longer extraction times may indicate linguistic complexity that correlates with signal uncertainty.
- **Deliverable:** published Substack article
- **Link:** https://mycroftproject.substack.com/p/extraction-latency-signal-financial-nlp
- **Status:** Complete (published)

### Video

Both videos follow the same split:
- **Concept, ideas, narration and direction:** original work.
- **Assembly:** Claude, using the video generation tool created by Humanitarians AI.

#### 22. Video: "ECIS Episode 6"
*Video · Video Production*
- Weekly Mycroft project update covering:
  - the prediction system build
  - per-speaker Scorecard validation
  - reader health monitoring
  - the forecast dashboard view
- **Deliverable:** Video: ECIS EP6
- **Links:**
  - https://www.youtube.com/watch?v=Wjebghtt8rQ
  - https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-09-11-ecis-explained
  - https://drive.google.com/drive/folders/1VnK_DOZScqLAkux7fT9q286O8S6M_Tsz
- **Status:** Complete

#### 23. Video: "Inside a Transformer Layer"
*Video · Video Production*
- STEM explainer on the internal mechanics of a transformer layer.
- Covers how self-attention, feed-forward networks and layer normalization work together to process and represent sequential text.
- **Deliverable:** Video: Inside a Transformer Layer
- **Links:**
  - https://www.youtube.com/watch?v=ZwgNiyJOABI
  - https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-09-11-transformer-layer
  - https://drive.google.com/drive/folders/1s67qkp03dgxIX2_WfMDzyDRMjF0YEFjM
- **Status:** Complete
