**Repository:** [https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis](https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis)

# Mycroft ECIS — Phase 16 — Guidance Models

**Timeline:** October 11, 2026 – October 17, 2026

**Scope:** Q&A dodge detection, financial-domain embedding fine-tuning, competitive positioning classification, and a six-model guidance revision predictor.

---

## Q&A Dodge Detection

## Q&A Section Parser
- Pairs each analyst question with its management response
- **Methods:**
  - Normalized speaker labels
  - Question-mark detection
  - Turn-taking heuristics
- Handles multi-part questions and follow-ups
- **Output:** structured Q&A pairs with speaker identity, section index, and character offsets

## Cross-Encoder Reranker
- **Model:** `ms-marco-MiniLM` cross-encoder
- Scores question–answer relevance, capturing:
  - Semantic alignment
  - Topic match
  - Directness of the response
- Provides a stronger basis for dodge detection than embedding cosine similarity

## Question Type Classifier
- **Categories:**
  - Forward-looking (guidance, outlook, projections)
  - Backward-looking (past results)
  - Clarification (follow-ups, detail requests)
  - Confrontational (challenging assumptions)
- Fine-tuned on labelled earnings call Q&A data
- Dodge scores weighted by question importance, so dodging confrontational or forward-looking questions is penalized more

## Dodge Score Aggregation
- Per-speaker dodge scores, weighted by question type
- Call-level aggregate score
- Quarter-over-quarter trend tracking per company
- Spikes above the company's historical average are flagged
- Stored in PostgreSQL alongside signal data

## Embedding and Sentiment Upgrades

## Financial Q&A Sentence-BERT
- Fine-tuned on paired Q&A segments from the transcript corpus
- Evaluated by retrieval accuracy on held-out Q&A pairs
- Replaces generic MiniLM embeddings for:
  - Dodge scoring
  - Semantic similarity
  - Downstream feature engineering

## FinBERT Ensemble
- Averages predictions across multiple FinBERT checkpoints
- Applied to:
  - Dodge-scoring sentiment context
  - Market share language scoring
  - Revision feature engineering
- Validated to have lower variance than single-checkpoint inference

## Competitive Positioning Classification

## Lexicon-Based Classifier
- **Offensive lexicon:** "gaining share", "expanding into", "capturing", "growing faster than", "taking market"
- **Defensive lexicon:** "maintaining position", "protecting margins", "defending", "holding steady", "retaining"
- FinBERT-scored context disambiguates phrases whose meaning depends on surrounding text
- Scores each call on an offensive–defensive spectrum

## Zero-Shot Classifier
- **Model:** BART-large-MNLI
- Offensive / defensive / neutral classification without a curated lexicon
- Robust to novel phrasing
- Compared with the lexicon classifier to:
  - Measure agreement
  - Find language the lexicon misses

## Stance Detection Model
- Fine-tuned on transcript examples with explicit competitive positioning
- Evaluated with bootstrap CIs against the lexicon and zero-shot classifiers
- **Final score:** ensemble of all three classifiers

## Shift Tracking
- Detects directional flips (offensive ↔ defensive) and gradual drift quarter over quarter
- Outputs a directional change score with the contributing phrases
- Timeline view shows each company's positioning trajectory

## Guidance Revision Predictor

## Feature Engineering
- **Features:**
  - Hedging index
  - Management confidence score
  - Guidance specificity change
  - CEO–CFO divergence
  - Dodge score
  - Market share language shift
  - Forward-looking density delta
  - FinBERT sentiment delta vs. the prior quarter
  - Relative sector mood
- Normalized and stored as versioned feature vectors in PostgreSQL

## Models

| Model | Purpose |
|---|---|
| Logistic regression | Interpretable coefficients |
| XGBoost | Non-linear interactions |
| Random Forest | Bagging-based variance reduction |
| LightGBM | Fast training for rapid feature iteration |
| MLP (64 → 32, ReLU, dropout, early stopping) | Interactions tree models may miss |
| CatBoost | Native categorical handling for sector and speaker role |

- **Training discipline:**
  - Time-aware cross-validation to prevent lookahead bias
  - Identical folds across all models

## Model Selection
- **Metrics:** accuracy, precision, recall, F1, and Brier score, each with bootstrap CIs
- Paired permutation tests across all model pairs
- **Selection:** best model as primary, second-best as fallback
- Feature-importance rankings documented from the tree-based models

## Dashboard
- **Dodge scores:** trends per company and per speaker, broken down by question type
- **Market share language:** offensive/defensive timeline with flip alerts
- **Guidance revisions:** revision probabilities, contributing factors, and a model comparison table
- **Global filters:** company, quarter, model

## Validation
- Full pipeline re-run with Phase 16 features enabled
- Dodge scoring validated across Q&A sections of the 25-ticker corpus
- Positioning classifiers agree on direction for the majority of calls
- Revision predictor benchmarked against a naive "no revision" baseline
- Fine-tuned Sentence-BERT confirmed to improve retrieval quality across downstream analytics
