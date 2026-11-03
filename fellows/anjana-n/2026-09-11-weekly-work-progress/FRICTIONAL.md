# Friction Log: Week 11 (Phase 11)

**Project:** Mycroft — ECIS + Decision Scorecard
**Week:** September 6 – September 12, 2026

---

## 1. Focus of the week

- **Prediction system:**
  - feature vectors from the decision log
  - stock return and sector aggregate features
  - logistic regression and XGBoost training with a temporal split
  - baseline comparison
  - prediction Scorecard
  - pre-registered, append-only prediction log
  - integration of research findings
- **New features:**
  - per-speaker Scorecard breakdown
  - reader health monitor
  - extraction latency logging
- **Dashboard:**
  - confidence histogram
  - forecast view
  - prediction vs. actual timeline
- **Research:**
  - ML model candidates
  - time series exploration
  - consensus estimates APIs
- **Outputs:**
  - two Claude artifacts
  - two Substack articles
  - two videos

## 2. What was tried, and what was expected

- **The system's own outputs:** expected the decision log to supply features predictive of next-quarter guidance direction.
- **Model complexity:** expected XGBoost to outperform logistic regression, given its extra flexibility.
- **Prior confidence:** expected it to be a useful predictive feature.
- **Sector aggregate:** expected it to be a clean, point-in-time-safe feature.
- **Scoring:** expected the prediction Scorecard to reuse the signal Scorecard's approach of grading against stock performance.
- **Latency:** the hypothesis was that slow inference correlates with model uncertainty and lower accuracy.

## 3. Points of resistance, and next steps taken

### Data leakage in the sector aggregate feature (load-bearing)
- **What happened:** the strict temporal split exposed a leakage bug.
  - The sector signal aggregate was computed from the full dataset, including the test quarter.
  - Companies that reported later in the quarter had their peers' actual guidance directions built into the feature, so the model was seeing the future.
- **Next step:** compute the aggregate only from companies that reported before the prediction target date.
- **Lesson:** this is the same look-ahead contamination the raw/verified gate was built to prevent in the signal layer. It almost slipped through in the prediction layer. The system's own discipline nearly failed to apply to itself.

### Collapsed evaluation levels (load-bearing)
- **What happened:** the prediction Scorecard initially graded predictions against stock performance, as the signal Scorecard does, rather than against extracted guidance direction.
- **Why it mattered:** this collapsed two levels into one. It became impossible to tell two failure modes apart, and each needs a different remedy:
  - **prediction errors:** the model guessed wrong about what the company would say
  - **market efficiency effects:** the company said the right thing, but the market had already priced it in
- **Next step:** separated the two levels.
  - **Level 1:** prediction vs. actual extracted guidance direction.
  - **Level 2:** guidance vs. stock performance.
- **Lesson:** a conceptual error, not a code error. The implementation worked perfectly while producing meaningless results.

### Feature selection surprises
- **What resisted:** prior confidence was surprisingly weak. A high-confidence signal last quarter doesn't predict next quarter's direction.
- **Next step:** dropped prior confidence, which improved both models.
  - Trend length and the sector signal aggregate were the strongest features.

### Model complexity as a liability
- **What happened:** logistic regression beat always-predict-maintained but only marginally beat naive momentum. XGBoost overfit and did worse than logistic regression on the held-out quarter.
- **Next step:** logistic regression with 8 features is the production model until the dataset grows substantially.
  - With 25 tickers across a few quarters, complexity hurts.
- **Lesson:** this is the project's original question, applied to the prediction layer: the sophisticated approach must justify its complexity over the simple baseline.

### Locking predictions
- **What resisted:** the temptation to allow prediction updates as new information arrives before the call.
- **Next step:** predictions are locked at submission time and stored append-only. This mirrors the signal log's pre-registration and prevents post-hoc fitting.

### Latency as a signal
- **What happened:** initial results show a correlation between latency and accuracy, but not one strong enough to justify a latency-based confidence penalty.
- **Next step:** keep logging to build the dataset, and decide once there is data.

## 4. AI and other contributions: accepted, changed, rejected

### Claude + Humanitarians AI video generation tool
- **Original work:** the concept, ideas, narration and direction for both videos.
- **Claude's part:** assembled the videos, using the video generation tool created by Humanitarians AI.

### Claude (artifacts)
- **Prediction Feature Importance Viewer:** shows the feature vector breakdown per ticker, the model coefficient weighting and a sector consensus comparison.
- **Latency vs. Accuracy Scatter:** plots per-signal latency against Scorecard accuracy, color-coded by reader, with threshold sliders.

### Gru (SDD session)
- Documented the prediction system architecture, the feature selection rationale and the two-level Scorecard design.

### Eddy
- Reviewed both Week 11 articles before publication.

## 5. Understood now, and still unresolved

### Understood
- **Point-in-time discipline:** it has to be re-applied at every new layer. The signal gate didn't protect the feature engineering.
- **Evaluation levels:** they must stay separate, so that a model error can be told apart from a market effect.
- **Small datasets:** at this data size, simpler models win; complexity has to be earned.
- **Prior confidence:** it isn't predictive of the next quarter, which is counter-intuitive but reported as found.
- **Pre-registration:** it now applies to predictions as well as signals.

### Unresolved
- **Latency as a signal:** continue logging; evaluate once the dataset is larger.
- **Consensus estimates API:** whether to integrate it as additional features.
- **Signal decay horizon weighting:** carried from Week 10.
- **Routing complexity decision:** carried forward.
