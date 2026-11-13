**Repository:** [https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis](https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis)

# Mycroft ECIS — Phase 17 — Signal Quality, Linguistic Depth, and Feature Engineering

**Timeline:** October 18, 2026 – October 24, 2026

**Scope:** Signal reliability analysis, transcript quality gating, advanced linguistic classification, automated feature selection, and embedding drift monitoring.

---

## Signal Quality

## Signal Decay by Type
- **Signal types analyzed:**
  - Hedging index
  - Tone-shift magnitude
  - Confidence score
  - Dodge score
  - Forward-looking density
  - Market share language score
- Correlation with excess returns at 1, 2, 5, 10, 20, 30, and 60 days
- **Output:** a half-life per signal type, marking where predictive power falls below statistical significance
- Drives time-horizon weighting, with recent data emphasized for short-lived signals

## False Positive Analysis
- **Population:** signals with confidence > 0.7 and an incorrect direction
- **Context captured per case:**
  - Contributing features
  - Transcript context
  - Sector
  - Market conditions
- **Root-cause clusters:**
  - Ambiguous language
  - Misread sarcasm
  - Section misattribution
  - Context-dependent phrases
  - Anomalous market conditions
- **Outputs:**
  - A false positive pattern report
  - Filtering rules that apply a reduced confidence modifier to signals matching known patterns

## Multi-Quarter Signal Chaining
- **Rolling sequences tracked per company:**
  - Hedging streaks (rising / falling)
  - Confidence trajectory (improving / stable / declining)
  - Dodge score momentum
  - Guidance specificity drift
- Sustained patterns outweigh single-quarter spikes
  - Example: three quarters of rising hedging with falling confidence count as sustained deterioration
- Chain length, direction, and per-ticker trend summaries stored in PostgreSQL

## Earnings Call Quality Scoring
- **Scoring dimensions:**
  - Transcription completeness (all expected sections present)
  - Q&A availability and length
  - Speaker-label coverage
  - Text coherence, using sentence-level perplexity as a proxy for transcription errors
  - Formatting consistency
- Calls below a configurable threshold receive reduced weight in sector aggregation and cross-company comparison
- Scores stored with transcript metadata

## Linguistic Depth

## Speech Act Classification
- **Model:** fine-tuned DeBERTa on labelled earnings call sentences
- **Classes:**

| Class | Example |
|---|---|
| Promise | "We will deliver" |
| Commitment | "We are committed to" |
| Hedged intention | "We hope to", "We aim to" |
| Prediction | "We expect", "We anticipate" |
| Deflection | "We'll see", "It remains to be seen" |
| Assertion | "We achieved", "Revenue grew" |

- Per-call speech act distributions, with quarter-over-quarter shift tracking

## Discourse Structure Analysis
- **Patterns detected:**
  - Front-loading
  
  - Progressive disclosure
  - Deflection
- **Method:** sentiment trajectory across prepared remarks
- Flags negative information that appears deliberately positioned for minimal impact
- Benchmarked against each company's historical structure

## Metaphor and Analogy Tracking
- **Detection methods:**
  - Semantic incongruity detection
  - Curated financial metaphor lexicon ("headwinds", "tailwinds", "runway", "pipeline", "moat", "inflection point")
- Figurative-to-concrete ratio per call and per speaker
- Significant increases vs. the historical average are flagged as possible obscuring of specifics

## Sarcasm and Irony Detection
- **Model:** fine-tuned RoBERTa on conversational data with financial domain adaptation
- Targets analyst–management exchanges where positive surface sentiment conflicts with skeptical context
- Detected segments are adjusted or excluded in downstream FinBERT scoring
- Sarcasm frequency per call tracked as a meta-signal for contentious Q&A

## Feature Engineering

## Automated Feature Selection
- **Three complementary methods:**
  - Recursive feature elimination with the primary XGBoost model
  - Permutation importance across all prediction targets
  - LASSO shrinkage on the logistic regression models
- **Rules:**
  - Features in the bottom 10% across all three methods are flagged for removal
  - Features correlated above 0.85 with another feature are flagged as redundant
- **Audit report:** marginal contribution, redundancy, and a keep / monitor / drop recommendation for each feature
- Applied across all prediction and classification models

## Feature Interaction Discovery
- ANOVA-based pairwise interaction testing across all feature pairs
- Identifies synergistic combinations
  - Example: high dodge score + rising hedging + defensive language
- Top interactions added as engineered features
- Gains validated with paired permutation tests

## Embedding Drift Monitoring
- **Per-quarter checks on the fine-tuned Sentence-BERT space:**
  - Cosine distance of the batch centroid from the historical centroid
  - Intra-cluster variance for bullish, bearish, and hedging language
- PSI > 0.1 flags a need for re-fine-tuning on recent transcripts
- Alerts surfaced in Grafana alongside the concept drift metrics

## Dashboard
- **Signal quality:**
  - Decay curves with half-life markers
  - False positive root-cause breakdown
  - Signal chain visualizations
  - Transcript quality distribution with low-quality flags
- **Linguistic depth:**
  - Speech act distributions
  - Discourse structure indicators
  - Metaphor density trends
  - Sarcasm highlights in Q&A
- **Feature engineering:**
  - Feature importance with selection recommendations
  - Top interactions
  - Embedding drift time series
- **Global filters:** signal type, quality tier, quarter

## Validation
- **Decay:** half-lives validated, and short-lived signals receive appropriate horizon weighting
- **False positive filtering:** reduces high-confidence errors without removing true positives
- **Signal chains:** correctly identify sustained trends
- **Speech act classifier:** accuracy benchmarked on held-out labelled data
- **Feature pruning:** improves prediction accuracy
- **Embedding drift:** aligns with the Phase 14 concept drift detection
