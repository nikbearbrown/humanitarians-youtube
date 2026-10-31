# Friction Log: Week 18 (Phase 18)

**Project:** Mycroft — ECIS + Decision Scorecard
**Week:** October 25 – October 31, 2026

---

## 1. Focus of the week

- **Calibration:**
  - Platt scaling and isotonic regression per signal type
  - temperature scaling for the MLP
  - recalibration of the six revision models
  - expected calibration error tracking
- **Signal contradiction detection:** rules, detection, severity scoring, resolution logic, and storage.
- **Explainability:** SHAP across the tree models, per-prediction waterfalls, and plain-English explanations.
- **Out-of-distribution detection:** Mahalanobis distance, an isolation forest, threshold calibration, and confidence reduction.
- **Dashboard:**
  - calibration curves
  - contradiction alerts
  - SHAP waterfalls
  - OOD feed
  - prediction explanations

## 2. What was tried, and what was expected

- **Confidence scores:** expected to be roughly accurate across signal types before calibration.
- **Isotonic regression:** expected to give a better calibration fit than Platt scaling across all signal types.
- **Signals:** expected to be evaluated independently, as in earlier weeks.
- **SHAP:** expected to work the same way across all four tree models.
- **Mahalanobis distance:** expected to work directly on the existing feature set.

## 3. Points of resistance, and next steps taken

### The system was most wrong where it was most confident (load-bearing)
- **What happened:** calibration curves revealed two problems.
  - **Overconfidence:** on hedging and dodge signals, the system predicted 0.8 but observed accuracy was 0.65.
  - **Underconfidence:** on tone shift, it predicted 0.6 but observed accuracy was 0.75.
- **Next step:**
  - Each signal type now gets its own calibration method.
  - Isotonic regression is used where the calibration curve is uneven, and Platt scaling where it is smooth.
- **Why it matters:** the hedging and dodge signals are the pipeline's newest and most complex. Every confidence threshold set before this week now needs review.

### Isotonic regression overfit on small subsets
- **What happened:** signal types with fewer than 50 samples produced step functions with single-sample bins. The method memorized individual points instead of learning a curve.
- **Next step:**
  - Added a minimum bin size of 10.
  - Sparse signal types now fall back to Platt scaling.
  - About 35 minutes went into diagnosing the erratic curves.
- **Lesson:** the same pattern as the Week 13 KS test. A method used below its sample-size requirements produces output that looks like a result but isn't, so low-sample cases always need a simpler fallback.

### SHAP and CatBoost categorical conflict
- **What happened:** SHAP expected numeric inputs, but CatBoost passes categorical features natively.
- **Next step:** wrapped CatBoost's SHAP computation in a numeric-only adapter.
- **Lesson:** this is the second time CatBoost's native categorical handling has clashed with another tool. The first was the Week 16 encoding conflict. It raises the question of whether that feature is worth the maintenance cost.

### Singular covariance matrix in Mahalanobis distance
- **What happened:** highly correlated features made the covariance matrix singular, so the distance calculation failed.
- **Next step:** added a Ledoit-Wolf shrinkage estimator for regularization. Diagnosing the error took about 25 minutes.
- **Lesson:** feature selection and OOD detection depend on each other. The redundant features removed in Week 17 would have caused exactly this failure.

### Contradictions carry meaning
- **What resisted:** deciding what a conflict between signals actually means.
- **Next step:** each contradiction type was linked to a likely explanation.

  - **High confidence + high dodge score:** selective transparency, with confidence on disclosed topics and evasion on others.
  - **Offensive language + declining specificity:** aspirational signaling without supporting detail.

### Choosing what to explain
- **What resisted:** the top three SHAP features are not always the most useful explanation. Sometimes the fourth tells the real story.
- **Next step:** explanation templates were designed with that judgment in mind, rather than simply filling in the top values.

## 4. AI and other contributions: accepted, changed, rejected

### Claude + Humanitarians AI video generation tool
- **Original work:** the concept, ideas, narration, and direction for both videos.
- **Claude's part:** assembled the videos using the video generation tool created by Humanitarians AI.

### Claude (artifact)
- **Pipeline Evolution Timeline:** a scrollable timeline from Phase 1 to Phase 18, showing the capabilities, models, and features added in each phase.

### Gru (SDD session)
- Documented this week's architecture changes.

### Eddy
- Reviewed "Inside the Four-Bit Number That Made Fine-Tuning Cheap" before publication.

## 5. Understood now, and still unresolved

### Understood
- **Confidence needs measuring.** Without calibration, the newest and most complex signals were the most overconfident.
- **No single calibration method fits every signal type.** The shape of each calibration curve decides which one to use.
- **Statistical methods need a fallback** for small samples.
- **Contradictions are signals in their own right.** Conflicting signals within a call say something about how management is communicating.
- **A well-conditioned feature space matters.** Distance-based detection only works when the features aren't heavily redundant.

### Unresolved
- **Pre-calibration confidence thresholds:** all thresholds set before Week 18 need review.
- **CatBoost integration cost:** whether its native categorical handling justifies the adapters it keeps requiring.
- **Sarcasm vs. idiom boundary:** carried from Week 17.
