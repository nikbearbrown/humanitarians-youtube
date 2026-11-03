# Weekly Report: Week 16 (Phase 16)

**Project:** Mycroft — ECIS (Earnings Call Intelligence System) + Decision Scorecard
**Week:** October 11 – October 17, 2026
**Total hours:** 37.0

---

## Summary

- Three new analytical capabilities:
  - **Q&A dodge scoring:** detects when executives evade analyst questions.
  - **Market share language scoring:** classifies offensive vs. defensive competitive positioning.
  - **Guidance revision predictor:** trained across six model architectures.
- **Predictor result:** on this small tabular dataset, tree ensembles outperformed the MLP.
  - LightGBM: 0.72 AUC
  - XGBoost: 0.71
  - CatBoost: 0.71
  - Random Forest: 0.70
  - MLP: 0.66
  - Logistic regression: 0.65
- **Dodge scoring:** weighted by question importance. A dodged forward-looking question counts for more than a dodged clarification.
- **Other work:**
  - a FinBERT ensemble for stable sentiment scoring
  - three new dashboard views: dodge trends, market share language timeline, revision probability
- **Outputs:**
  - one Claude artifact
  - one Substack article
  - two videos

---

## Work Completed

### Q&A Dodge Scoring

#### 1. Q&A Section Parsing & Question Extraction
*Development · Q&A Dodge Scoring*
- Built a Q&A section parser using speaker labels and question-mark detection.
- Extracts analyst questions and pairs each with management's response for dodge analysis.
- **Deliverable:** Q&A parsing module with question-answer pair extraction
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/guidance_models/qa_parser.py
- **Status:** Complete

#### 2. Semantic Similarity with Cross-Encoder Reranking
*Development · Q&A Dodge Scoring*
- Scores question-answer relevance for dodge detection in two stages:
  - sentence embeddings for semantic similarity
  - a cross-encoder reranker (ms-marco-MiniLM) for accuracy
- **Deliverable:** semantic similarity module with cross-encoder reranking pipeline
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/guidance_models/reranker.py
- **Status:** Complete

#### 3. Question Type Classifier
*Development · Q&A Dodge Scoring*
- Classifies analyst questions into four types:
  - forward-looking
  - backward-looking
  - clarification
  - confrontational
- Dodge scores are weighted by question type.
- **Deliverable:** question type classifier with importance-weighted scoring
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/guidance_models/question_types.py
- **Status:** Complete

#### 4. Dodge Score Aggregation & Trend Tracking
*Development · Q&A Dodge Scoring*
- Computes dodge scores per call and per speaker.
- Tracks trends across quarters to detect changes in management responsiveness.
- **Deliverable:** dodge score aggregation with quarterly trend tracking
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/guidance_models/dodge.py
- **Status:** Complete

#### 5. Sentence-BERT Fine-Tuning for Financial Q&A
*Development · Q&A Dodge Scoring*
- Fine-tuned Sentence-BERT on financial Q&A pairs.
- Improves embedding quality for question-answer similarity across all dodge detection features.
- **Deliverable:** fine-tuned Sentence-BERT model for financial Q&A embeddings
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/guidance_models/sbert.py
- **Status:** Complete

### Market Share Language

#### 6. Offensive vs. Defensive Language Classifier
*Development · Market Share Language*
- Combines a curated lexicon with FinBERT-scored context.
- Identifies competitive positioning language in earnings calls.
- **Deliverable:** lexicon-based offensive/defensive classifier with FinBERT context
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/guidance_models/market_share.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/guidance_models/finbert_ensemble.py
- **Status:** Complete

#### 7. Zero-Shot Competitive Positioning Classifier
*Development · Market Share Language*
- Uses BART-large-MNLI to classify language as offensive, defensive or neutral.
- Works without relying on a hand-curated lexicon.
- **Deliverable:** zero-shot competitive positioning classifier (BART-large-MNLI)
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/guidance_models/market_share.py
- **Status:** Complete

#### 8. Stance Detection Model for Financial Text
*Development · Market Share Language*
- Trained a stance detection model fine-tuned on financial text to recognize competitive positioning language.
- Captures nuanced market share intent beyond keyword matching.
- **Deliverable:** fine-tuned stance detection model for financial competitive language
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/guidance_models/market_share.py
- **Status:** Complete

#### 9. Market Share Language Scoring & Trend Tracking
*Development · Market Share Language*
- Places each earnings call on the offensive-defensive spectrum.
- Tracks quarterly shifts and flags directional flips in competitive positioning.
- **Deliverable:** market share language scoring with directional flip detection
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/guidance_models/market_share.py
- **Status:** Complete

### Guidance Revision Predictor

#### 10. Feature Engineering for Revision Prediction
*Development · Guidance Revision Predictor*
- Engineered a feature vector for guidance revision prediction, combining:
  - hedging index
  - confidence score
  - guidance specificity change
  - CEO–CFO divergence
  - dodge score
  - market share language shift
- **Deliverable:** feature engineering pipeline for revision prediction
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/guidance_models/revision_features.py
- **Status:** Complete

#### 11. Logistic Regression & XGBoost Training
*Development · Guidance Revision Predictor*
- Trained logistic regression and XGBoost classifiers for guidance revision prediction.
- Matches the existing prediction architecture, with temporal train-test splits.
- **Deliverable:** trained logistic regression and XGBoost revision predictors
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/guidance_models/revision_models.py
- **Status:** Complete

#### 12. Random Forest & LightGBM Training
*Development · Guidance Revision Predictor*
- Trained Random Forest and LightGBM classifiers to add diversity to the ensemble.
- Evaluated their complementary strengths on tabular financial feature vectors.
- **Deliverable:** trained Random Forest and LightGBM revision predictors
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/guidance_models/revision_models.py
- **Status:** Complete

#### 13. MLP Neural Network Training
*Development · Guidance Revision Predictor*
- Trained a small MLP (64/32) to capture non-linear feature interactions.
- Compared its performance against tree-based methods on small tabular financial data.
- **Deliverable:** trained MLP neural network for revision prediction
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/guidance_models/revision_models.py
- **Status:** Complete

#### 14. CatBoost Training with Categorical Features
*Development · Guidance Revision Predictor*
- Trained a CatBoost classifier with native categorical handling for the sector and speaker role variables.
- Uses ordered boosting for robustness on a small dataset.
- **Deliverable:** trained CatBoost revision predictor with categorical encoding
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/guidance_models/revision_models.py
- **Status:** Complete

#### 15. Model Evaluation & Statistical Comparison
*Development · Guidance Revision Predictor*
- Evaluated all revision predictor models with bootstrap confidence intervals.
- Compared each against a naive baseline.
- Ran paired permutation tests across every model pair to check whether performance differences are statistically significant.
- **Deliverable:** model evaluation report with bootstrap CIs and permutation tests
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/guidance_models/revision_models.py
- **Status:** Complete

#### 16. FinBERT Ensemble for Stable Sentiment Scoring
*Development · Guidance Revision Predictor*
- Runs multiple FinBERT checkpoints and averages their predictions.
- Gives stable sentiment scores to every downstream feature.
- **Deliverable:** FinBERT multi-checkpoint ensemble module
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/guidance_models/finbert_ensemble.py
- **Status:** Complete

### Dashboard

#### 17. Dodge Score Trend View
*Development · Dashboard*
- Shows dodge scores per company and per speaker, with quarterly trend lines.
- **Deliverable:** dodge score trend dashboard view
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/dashboard/views.py
- **Status:** Complete

#### 18. Market Share Language Shift Timeline
*Development · Dashboard*
- Timeline with offensive and defensive indicators showing competitive positioning changes over time.
- **Deliverable:** market share language shift timeline view
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/dashboard/views.py
- **Status:** Complete

#### 19. Guidance Revision Probability View
*Development · Dashboard*
- Shows revision probability with its contributing factors.
- Compares all trained revision predictors.
- **Deliverable:** guidance revision probability dashboard view with model comparison
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/dashboard/views.py
- **Status:** Complete

### Debugging

#### 20. Debugging & Issue Resolution
*Development · Debugging*
- Identified and resolved issues across the pipeline. The main ones:
  - **Sentence-BERT:** overfitting during fine-tuning.
  - **MLP:** gradient instability.
  - **CatBoost:** a categorical encoding conflict.
- **Deliverable:** resolved issues and verified fixes
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/tests/test_phase16.py
- **Status:** Complete

### Research

#### 21. Q&A Response Analysis & Dodge Detection Research
*Research · Q&A Analysis*
- Researched Q&A response analysis techniques and dodge detection methods in NLP.
- Reviewed semantic similarity approaches for measuring question-answer alignment.
- **Deliverable:** research notes on Q&A dodge detection techniques
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/research
- **Status:** Complete

#### 22. Competitive Positioning Language Research
*Research · Competitive Positioning*
- Researched competitive positioning language in financial communications.
- Covered offensive vs. defensive language frameworks and stance detection approaches.
- **Deliverable:** research notes on competitive positioning language analysis
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/research
- **Status:** Complete

#### 23. Guidance Revision Prediction & Ensemble Methods Research
*Research · Ensemble Methods*
- Researched guidance revision prediction approaches and ensemble methods for financial NLP.
- Evaluated model diversity strategies for tabular financial data.
- **Deliverable:** research notes on ensemble methods for financial prediction
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/research
- **Status:** Complete

### Writing

#### 24. Substack Article: "Does Deep Learning Help When the Data Is Small?"
*Writing · Substack Article*
- Compares an MLP against XGBoost, LightGBM and CatBoost on a small tabular financial dataset.
- Explains why tree ensembles still outperform neural networks on structured data.
- **Deliverable:** published Substack article
- **Link:** https://mycroftproject.substack.com/p/deep-learning-small-data-tree-ensembles-tabular
- **Status:** Complete (published)

### Artifact

#### 25. Permutation Test Playground
*Artifact · Claude Artifact*
- Interactive artifact comparing two model versions side by side.
- Runs permutation tests live and shows whether a performance improvement is statistically significant or attributable to noise.
- **Deliverable:** Claude Artifact: Permutation Test Playground
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/artifacts
- **Status:** Complete

### Video

Both videos follow the same split.
- **Concept, ideas, narration, and direction:** original work.
- **Assembly:** Claude, using the video generation tool created by Humanitarians AI.

#### 26. Video: "ECIS Episode 11: Weekly Project Update"
*Documentation · Video Production*
- Weekly Mycroft ECIS project update covering Week 16 progress, including Q&A dodge scoring and the guidance revision predictor.
- **Deliverable:** Video: ECIS Episode 11
- **Links:**
  - https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-10-16-retrieval-pipeline-explainer
  - https://drive.google.com/drive/folders/1nhuXcSs3NBvBfnIoYChnB1pp2Ih_J6ll
- **Status:** Complete

#### 27. Video: "What a Retrieval Pipeline Looks Like in Production"
*Documentation · Video Production*
- STEM educational video on production retrieval pipeline architecture, covering:
  - embedding and indexing
  - query rewriting
  - reranking and filtering
  - the latency budget
- **Deliverable:** Video: What a Retrieval Pipeline Looks Like in Production
- **Links:**
  - https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-10-16-retrieval-pipeline-explainer
  - https://drive.google.com/drive/folders/12lmxHJh3ymFt53A_vrxpRrEOYg4OmM2h
- **Status:** Complete
