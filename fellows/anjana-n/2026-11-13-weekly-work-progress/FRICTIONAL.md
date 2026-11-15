# Friction Log: Week 20 (Phase 20)

**Project:** Mycroft — ECIS + Decision Scorecard

**Week:** November 8 – November 14, 2026

---

## 1. Focus of the week

- **Time-series models:**
  - LSTM and GRU sequence models
  - comparison with the tree-based models
  - a three-state Hidden Markov Model for market regimes
  - regime labels used as a context feature
- **Analyst intelligence:**
  - identity resolution
  - question patterns
  - difficulty scoring
  - difficulty-normalized dodge scores
  - analyst-management alignment
- **Feature engineering:** lag features, momentum, acceleration, and rolling z-scores.
- **Agentic RAG:** hybrid retrieval combining transcript search (ChromaDB) with SQL over signals (PostgreSQL).
- **Dashboard:**
  - sequence model views
  - regime panel
  - analyst profile cards
  - momentum sparklines

## 2. What was tried, and what was expected

- **LSTM sequences:** expected 8-quarter input sequences to give the LSTM the most history to learn from.
- **HMM:** expected to find the same three regimes each time it was fitted.
- **Analyst names:** expected fuzzy matching on names to resolve analysts reliably across calls.
- **Dodges:** expected every dodge to count the same, regardless of who asked the question.

## 3. Points of resistance, and next steps taken

### The LSTM stopped learning on long sequences (load-bearing)
- **What happened:** on 8-quarter sequences, the loss stopped improving after epoch 3. Gradient clipping at 1.0 helped a little but did not fix it.
- **Next step:**
  - Switched to shorter sequences of 4–6 quarters.
  - Explicit lag features now carry the older history, instead of relying on the LSTM's memory.
  - About 45 minutes of training runs went into diagnosing it.
- **Lesson:**
  - Rather than adding complexity to stretch the model's memory, the long-range context was moved into simple features.
  - This is the same pattern as earlier small-sample fallbacks: when a sophisticated method hits its limit, fall back to a simpler approach that works.

### HMM regimes changed between runs
- **What happened:** three random initializations produced three different regime labelings, because the model settled into different solutions each time.
- **Next step:**
  - Emission parameters are now initialized from k-means clusters on the signal aggregates.
  - The model is fitted 10 times and the best fit is kept.
  - About 30 minutes.
- **Still open:** None

### Analyst names were wrongly merged
- **What happened:** the same analyst can appear differently. Matching on names alone wrongly merged different analysts who share common surnames.
- **Next step:** names are now anchored on the analyst's firm before matching.
- **Still open:** None

### Not every dodge is equal
- **What resisted:** a CEO dodging a tough analyst's question means more than dodging an easy one, but earlier dodge scores treated them the same.
- **Next step:** dodge scores are now adjusted by how difficult each analyst's questions tend to be. The system has to model who asked a question to judge how significant a dodge is.

### The same signal means different things in different markets
- **What resisted:** rising hedging carries a different meaning depending on market conditions.
  - In a bullish regime, it is an early warning.
  - In a bearish regime, it is confirmation.
- **Next step:** the HMM's regime label is passed to every prediction model as context.

## 4. AI and other contributions: accepted, changed, rejected

### Claude + Humanitarians AI video generation tool
- **Original work:** the concept, ideas, narration, and direction for both videos.
- **Claude's part:** assembled the videos using the video generation tool created by Humanitarians AI.

### Claude (artifact)
- **LSTM vs. Tree Model Showdown:** compares LSTM/GRU predictions against tree-based predictions for any company, with confidence bands.

### Gru (SDD session)
- Documented this week's architecture changes.

### Eddy
- Reviewed "Deep Learning for Time Series: LSTMs, N-BEATS, and Transformers Compared" before publication.

## 5. Understood now, and still unresolved

### Understood
- **Sequences show what snapshots can't.** A four-quarter rise in hedging tells a different story from a single spike.
- **Long-range context can come from features.** It doesn't always have to come from model memory.
- **Fitting methods need stable starting points.** Without them, they can produce different answers each run.
- **Who asks the question matters.** Social context, such as how tough an analyst usually is, is part of the analysis, not separate from it.

### Unresolved
- None