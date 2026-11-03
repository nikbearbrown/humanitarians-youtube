# Friction Log: Week 16 (Phase 16)

**Project:** Mycroft — ECIS + Decision Scorecard
**Week:** October 11 – October 17, 2026

---

## 1. Focus of the week

- **Q&A dodge scoring:**
  - Q&A parsing
  - cross-encoder relevance scoring
  - question type classifier
  - dodge aggregation and trends
  - Sentence-BERT fine-tuning
- **Market share language:**
  - lexicon + FinBERT classifier
  - zero-shot BART-large-MNLI
  - stance detection model
  - spectrum scoring with flip detection
- **Guidance revision predictor:** feature engineering, then six models:
  - logistic regression
  - XGBoost
  - Random Forest
  - LightGBM
  - MLP
  - CatBoost
- **Evaluation and scoring:**
  - model evaluation with bootstrap CIs and permutation tests
  - FinBERT ensemble
- **Dashboard:**
  - dodge trend view
  - market share language timeline
  - revision probability view
- **Research:**
  - dodge detection
  - competitive positioning language
  - ensemble methods
- **Outputs:**
  - one Claude artifact
  - one Substack article
  - two videos

## 2. What was tried, and what was expected

- **Sentence-BERT:** expected fine-tuning on financial Q&A pairs to improve question-answer relevance scoring directly.
- **MLP:** expected it to capture non-linear feature interactions and compete with tree ensembles on revision prediction.
- **CatBoost:** expected its native categorical handling to give it an edge on the sector and speaker role variables.
- **Semantic similarity:** expected similarity alone to be enough to judge whether an answer addresses a question.
- **Offensive vs. defensive language:** expected classification to be largely a matter of matching phrases.

## 3. Points of resistance, and next steps taken

### What counts as a dodge? (load-bearing)
- **What resisted:**
  - Judging whether an answer is a dodge requires a model of what an adequate answer would have been. That counterfactual doesn't exist in the data.
  - Semantic relevance alone treats every evaded question the same.
- **Next step:** dodge scores are weighted by question importance.
  - A dodged forward-looking question signals more about undisclosed information than a dodged clarification.
  - A backward-looking evasion may simply reflect poor recall or data access.
- **Lesson:** detecting evasion depends on understanding what evasion looks like, then encoding that understanding in the scoring function.

### Sentence-BERT fine-tuning overfit
- **What happened:** the model overfit within 2 epochs.
  - Training pairs were too homogeneous: question-answer pairs from the same call shared vocabulary and structure.
  - The model was learning co-occurrence within a call, not semantic question-answer relevance.
- **Next step:**
  - Added hard negatives: answers to different questions on the same call.
  - This forces the model to learn semantic relevance rather than surface similarity.
  - Retraining cycles cost about 50 minutes.

### MLP gradient instability
- **What happened:** a learning rate of 1e-3 caused loss spikes; 1e-5 barely moved.
- **Next step:**
  - Settled on 3e-4 with a warmup scheduler.
  - Training became stable, but the MLP still reached only 0.66 AUC.
- **Lesson:** fixing training stability is an engineering problem. The underperformance itself is structural: there isn't enough data for the architecture to capture interactions that tree ensembles find natively.

### CatBoost categorical encoding conflict
- **What happened:**
  - Features were already one-hot encoded upstream.
  - CatBoost's native categorical handling was therefore receiving pre-encoded inputs, making it functionally identical to XGBoost.
- **Next step:** branched the pipeline. Raw categoricals now go to CatBoost, and one-hot encoding is kept for the other models.
- **Lesson:** a shared feature pipeline can silently neutralize a model's distinctive capability. The branch adds maintenance cost.

### Choosing a production model
- **Results:**
  - LightGBM: 0.72 AUC
  - XGBoost: 0.71
  - CatBoost: 0.71
  - Random Forest: 0.70
  - MLP: 0.66
  - Logistic regression: 0.65
- **What resisted:** the 0.01 AUC gap between LightGBM and XGBoost likely falls within the confidence intervals.
- **Next step:** the production choice is weighed on more than AUC: interpretability, calibration quality and maintenance cost. Logistic regression stays as the interpretability baseline.

### Context-dependent competitive language
- **What resisted:** the same phrase shifts meaning across contexts.
  - "Expanding into adjacent markets" is offensive.
  - "Protecting our core business" is defensive.
  - "Investing in customer retention" could go either way.
- **Next step:** FinBERT handles context disambiguation, and zero-shot BART-large-MNLI handles edge cases. When to let zero-shot override FinBERT needs a judgment framework, not a single threshold.

## 4. AI and other contributions: accepted, changed, rejected

### Claude + Humanitarians AI video generation tool
- **Original work:** the concept, ideas, narration and direction for both videos.
- **Claude's part:** assembled the videos using the video generation tool created by Humanitarians AI.

### Claude (artifact)
- **Permutation Test Playground:**
  - Compares two model versions side by side.
  - Runs permutation tests live, showing whether an improvement is significant or noise.

### Gru (SDD session)
- Documented this week's architecture changes.

### Eddy
- Reviewed "Does Deep Learning Help When the Data Is Small?" before publication.

## 5. Understood now, and still unresolved

### Understood
- **Tree ensembles beat the MLP on small tabular data:** the MLP's underperformance is structural, not a hyperparameter problem.
- **Training data matters:** it determines what a fine-tuned model actually learns. Hard negatives redirected Sentence-BERT from co-occurrence to relevance.
- **Shared pipelines can hide capabilities:** they can neutralize what makes a model distinct, as one-hot encoding did to CatBoost.
- **Dodge detection needs a notion of informational demand:** semantic similarity alone is not enough.
- **Transferred models work in finance:** general-purpose models transfer usefully into financial text, including a web-search cross-encoder and an NLI zero-shot classifier.

### Unresolved
- **LightGBM vs. XGBoost:** the production choice is still open.
- **LightGBM–XGBoost AUC gap:** needs a targeted permutation test on that specific pair.
- **NLP vs. consensus value:** carried from Week 15.
- **Power analysis:** n≈45 is still insufficient. Carried from Week 14; model comparisons now use bootstrap CIs.
- **ChromaDB versioning and operational tooling:** carried from Weeks 13–14.
