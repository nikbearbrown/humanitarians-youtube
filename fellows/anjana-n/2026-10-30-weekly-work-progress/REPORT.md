# Weekly Report: Week 18 (Phase 18)

**Project:** Mycroft — ECIS (Earnings Call Intelligence System) + Decision Scorecard


**Week:** October 25 – October 31, 2026


**Total hours:** 32.5

---

## Summary

Week 18 built the pipeline's trust infrastructure.

- **Calibration:**
  - Platt scaling, isotonic regression, and temperature scaling, with the method chosen per signal type.
  - All six guidance revision models recalibrated.
  - Expected calibration error tracked per model and per signal type.
- **Key finding:** the system was overconfident on hedging and dodge signals and underconfident on tone shift.
  - Hedging and dodge: predicted 0.8, observed 0.65.
  - Tone shift: predicted 0.6, observed 0.75.
- **Signal contradiction detection:** the first capability that reasons across several signals at once.
  - It detects conflicting signals within the same call.
  - It scores how severe each conflict is.
  - It infers what the conflict implies.
- **Explainability:** SHAP feature attribution across the tree models, with plain-English explanations for each prediction.
- **Out-of-distribution (OOD) detection:** Mahalanobis distance plus an isolation forest, with automatic confidence reduction on flagged transcripts.

---

## Work Completed

### Calibration

#### 1. Platt Scaling per Signal Type
*Development · Calibration*
- Fitted Platt scaling (logistic regression on model outputs vs. actual outcomes) separately for each signal type.
- Produces well-calibrated probability estimates.
- **Deliverable:** Platt scaling calibration fitted per signal type
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/reliability/calibrate.py
- **Status:** Complete

#### 2. Isotonic Regression Calibration
*Development · Calibration*
- Fitted isotonic regression as an alternative calibration method.
- Compared its fit against Platt scaling across all signal types and sample sizes.
- **Deliverable:** isotonic regression calibration with Platt comparison results
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/reliability/calibrate.py
- **Status:** Complete

#### 3. Calibration Validation & Reliability Diagrams
*Development · Calibration*
- Binned predictions into deciles and plotted expected vs. observed accuracy.
- Assesses calibration quality for each model and signal type.
- **Deliverable:** calibration reliability diagrams with decile-binned validation
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/reliability/calibrate.py
- **Status:** Complete

#### 4. MLP Temperature Scaling
*Development · Calibration*
- Applied temperature scaling to the MLP's outputs.
- Calibrates its probabilities without changing how well it separates classes.
- **Deliverable:** temperature-scaled MLP probability outputs
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/reliability/calibrate.py
- **Status:** Complete

#### 5. Guidance Revision Model Recalibration
*Development · Calibration*
- Recalibrated the probability outputs of all six guidance revision models: logistic regression, XGBoost, Random Forest, LightGBM, CatBoost, and MLP.
- Each model uses its best-fitting calibration method.
- **Deliverable:** recalibrated probability outputs for all six revision models
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/reliability/calibrate.py
- **Status:** Complete

#### 6. Expected Calibration Error Computation
*Development · Calibration*
- Computed expected calibration error (ECE) per model and per signal type.
- Gives a single-number summary of calibration quality for monitoring and comparison.
- **Deliverable:** ECE metrics per model and signal type
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/reliability/calibrate.py
- **Status:** Complete

### Signal Contradiction

#### 7. Contradiction Rule Definition
*Development · Signal Contradiction*
- Defined rules for conflicting signal combinations:
  - bullish tone with rising hedging
  - high confidence with a high dodge score
  - offensive language with declining specificity
- **Deliverable:** contradiction rule set with signal pair definitions
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/reliability/contradictions.py
- **Status:** Complete

#### 8. Contradiction Detection Module
*Development · Signal Contradiction*
- Scans all signals within each earnings call for conflicts under the defined rules.
- **Deliverable:** contradiction detection module with intra-call scanning
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/reliability/contradictions.py
- **Status:** Complete

#### 9. Contradiction Severity Scoring
*Development · Signal Contradiction*
- Scores each detected contradiction by signal strength and type importance.
- Prioritizes the most impactful conflicts.
- **Deliverable:** severity scoring module with signal-weighted contradiction ranking
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/reliability/contradictions.py
- **Status:** Complete

#### 10. Contradiction Resolution Logic
*Development · Signal Contradiction*
- Determines what each contradiction implies: uncertainty or a mixed outlook.
- Based on the contradiction's type and context.
- **Deliverable:** contradiction resolution module with implication classification
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/reliability/contradictions.py
- **Status:** Complete

#### 11. Contradiction Storage in PostgreSQL
*Development · Signal Contradiction*
- Stores contradiction flags, severity scores, and resolution outcomes in PostgreSQL alongside the signal records.
- **Deliverable:** contradiction data persisted in PostgreSQL
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/db/init_db.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/analytics/store.py
- **Status:** Complete

### Explainability

#### 12. SHAP Integration Across Tree Models
*Development · Explainability*
- Integrated SHAP across XGBoost, LightGBM, Random Forest, and CatBoost.
- Gives consistent feature attribution across all tree-based revision predictors.
- **Deliverable:** SHAP integration for all tree-based models
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/reliability/shap_explain.py
- **Status:** Complete

#### 13. Per-Prediction SHAP Waterfall Generation
*Development · Explainability*
- Generates and stores a SHAP waterfall for every guidance revision prediction, showing each feature's contribution.
- **Deliverable:** SHAP waterfall generation and storage pipeline
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/reliability/shap_explain.py
- **Status:** Complete

#### 14. Natural Language Explanation Templates
*Development · Explainability*
- Templates that turn the top SHAP contributors into plain-English descriptions.
- **Deliverable:** natural language explanation templates for SHAP features
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/reliability/explanations.py
- **Status:** Complete

#### 15. Explanation Generation Pipeline
*Development · Explainability*
- Produces readable summaries for each prediction.
- Example: "flagged because hedging rose 40% while CEO–CFO divergence hit a 4-quarter high".
- **Deliverable:** automated explanation generation pipeline
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/reliability/explanations.py
- **Status:** Complete

### OOD Detection

#### 16. Mahalanobis Distance OOD Detector
*Development · OOD Detection*
- Fitted Mahalanobis distance on the training feature distribution.
- Detects out-of-distribution (OOD) transcripts that fall outside what the model has learned.
- **Deliverable:** Mahalanobis distance OOD detector fitted on training data
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/reliability/ood.py
- **Status:** Complete

#### 17. OOD Threshold Calibration
*Development · OOD Detection*
- Set the OOD threshold from a held-out validation set.
- The threshold sits at the 95th percentile of training distances, balancing detection against false alarms.
- **Deliverable:** calibrated OOD threshold from validation data
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/reliability/ood.py
- **Status:** Complete

#### 18. Isolation Forest Secondary Detector
*Development · OOD Detection*
- Added an isolation forest as a second OOD detector, for robustness alongside Mahalanobis distance.
- **Deliverable:** isolation forest secondary OOD detector
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/reliability/ood.py
- **Status:** Complete

#### 19. OOD Confidence Reduction
*Development · OOD Detection*
- Automatically reduces confidence on OOD-flagged transcripts by a configurable factor.
- Stops unreliable predictions from passing through at full confidence.
- **Deliverable:** configurable confidence reduction for OOD-flagged transcripts
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/reliability/ood.py
- **Status:** Complete

#### 20. OOD Score Storage
*Development · OOD Detection*
- Stores OOD scores with transcript metadata in PostgreSQL for monitoring, trend analysis, and the dashboard.
- **Deliverable:** OOD scores persisted in PostgreSQL transcript metadata
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/reliability/refresh.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/db/init_db.py
- **Status:** Complete

### Dashboard

#### 21. Calibration Curve Viewer
*Development · Dashboard*
- Calibration curves that can be filtered by signal type, model, and quarter.
- **Deliverable:** calibration curve dashboard view with multi-filter toggle
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/dashboard/views.py
- **Status:** Complete

#### 22. Contradiction Alert Panel
*Development · Dashboard*
- Per-call breakdown of conflicting signals, with severity scores and resolution outcomes.
- **Deliverable:** contradiction alert dashboard panel
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/dashboard/views.py
- **Status:** Complete

#### 23. SHAP Waterfall Charts
*Development · Dashboard*
- Per-prediction charts showing how much each feature contributed to each guidance revision prediction.
- **Deliverable:** SHAP waterfall chart dashboard view
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/dashboard/views.py
- **Status:** Complete

#### 24. OOD Anomaly Feed
*Development · Dashboard*
- Lists flagged transcripts with their scores and confidence adjustments.
- **Deliverable:** OOD anomaly feed dashboard view
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/dashboard/views.py
- **Status:** Complete

#### 25. Prediction Explanation Display
*Development · Dashboard*
- Shows the plain-English explanation alongside each prediction.
- **Deliverable:** prediction explanation text dashboard display
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/dashboard/views.py
- **Status:** Complete

### Debugging

#### 26. Debugging & Testing
*Development · Debugging*
- Resolved issues across the calibration, contradiction detection, explainability, and OOD modules. The main ones:
  - isotonic regression overfitting on small subsets
  - a SHAP–CatBoost categorical conflict
  - a singular covariance matrix in Mahalanobis distance
- Ran integration testing across all the new components.
- **Deliverable:** resolved issues and verified fixes
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/tests/test_phase18.py
- **Status:** Complete

### Research

#### 27. Confidence Score Distribution Review
*Research · Calibration*
- Reviewed confidence score distributions across all signal types.
- Looked for systematic over- or under-confidence.
- **Deliverable:** research notes on confidence distribution analysis
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/research
- **Status:** Complete

#### 28. Platt Scaling vs. Isotonic Regression Tradeoffs
*Research · Calibration*
- Studied when each calibration method is preferable, especially for small sample sizes.
- **Deliverable:** research notes on calibration method selection
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/research
- **Status:** Complete

#### 29. Intra-Call Signal Conflict Frequency Analysis
*Research · Signal Contradiction*
- Measured how often signals conflict within the same call, to set baseline contradiction rates and inform detection thresholds.
- **Deliverable:** research notes on intra-call signal conflict patterns
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/research
- **Status:** Complete

### Writing

#### 30. Substack Article: "Inside the Four-Bit Number That Made Fine-Tuning Cheap"
*Writing · Substack Article*
- Examines NF4, double quantization, and paged optimizers, which together make it possible to train an 8B model on a single GPU.
- Explores the tradeoff each technique introduces.
- **Deliverable:** published Substack article
- **Link:** https://mycroftproject.substack.com/p/qlora-nf4-four-bit-fine-tuning-single-gpu
- **Status:** Complete (published)

### Artifact

#### 31. Pipeline Evolution Timeline
*Artifact · Claude Artifact*
- Interactive, scrollable timeline from Phase 1 to Phase 18.
- Each phase is a clickable node showing the capabilities added, the models introduced, and how the features connect.
- **Deliverable:** Claude Artifact: Pipeline Evolution Timeline
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/artifacts
- **Status:** Complete

### Video

Both videos follow the same split:
- **Concept, ideas, narration, and direction:** original work.
- **Assembly:** Claude, using the video generation tool created by Humanitarians AI.

#### 32. Video: "ECIS Episode 13: Weekly Project Update"
*Documentation · Video Production*
- Weekly Mycroft ECIS project update covering Week 18 progress: calibration, contradiction detection, and explainability.
- **Deliverable:** Video: ECIS Episode 13
- **Links:**
  - https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-10-30-ecis-explained
  - https://drive.google.com/drive/folders/1klBky8EUmX9enNkT9Oogro15lO03a5n_
- **Status:** Complete

#### 33. Video: "What Distributed Training Actually Looks Like"
*Documentation · Video Production*
- STEM educational video on distributed training architecture.
- Covers data-parallel vs. model-parallel training, gradient synchronization, and all-reduce communication.
- **Deliverable:** Video: Distributed Training Explainer
- **Links:**
  - https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-10-30-distributed-training-explainer
  - https://drive.google.com/drive/folders/1KzVPPTFcm3LRt-pdS2RzfmoMEkXQ6ofM
- **Status:** Complete