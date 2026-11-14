**Repository:** [https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis](https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis)

# Mycroft ECIS — Phase 20 — Time-Series Models, Analyst Intelligence, Temporal Features, and Agentic RAG

**Timeline:** November 8, 2026 – November 14, 2026

**Scope:** Phase 20 covers four areas:
- sequence models and market regime detection
- analyst-level behavior tracking
- temporal feature engineering
- retrieval-augmented generation (RAG) for the conversational agent

---

## Time-Series Models
- **LSTM:** trained on input sequences of 4–8 quarters of signal features per company, with tuned hidden size and dropout.
- **GRU:** trained on the same input structure, and compared with the LSTM on training speed, convergence, and accuracy.
- **Sequence vs. tree models:** LSTM and GRU compared against XGBoost, LightGBM, Random Forest, and CatBoost using bootstrap confidence intervals.
- **Hidden Markov Model:** three states (bullish, bearish, transitional), fitted on sector-level signal aggregates, with a regime label for each quarter.
- **Regime context:** the regime label is passed to every prediction model as a context feature.

## Analyst Intelligence
- **Identity resolution:** analyst names are normalized across calls and mapped to their firms.
- **Question patterns:** tracks each analyst's question difficulty and whether they lean bullish or bearish.
- **Difficulty scoring:** based on three measures:
  - the mix of question types
  - follow-up rate
  - confrontational ratio
- **Difficulty-normalized dodge scores:** dodging a tough analyst's question counts differently from dodging an easy one.
- **Alignment scoring:** measures how closely an analyst's framing matches management's language, from sympathetic to adversarial.

## Temporal Feature Engineering
- **Lag features:** every signal at t-1, t-2, and t-3 quarters.
- **Momentum:** quarter-over-quarter rate of change.
- **Acceleration:** rate of change of momentum, to detect turning points.
- **Rolling z-scores:** normalization relative to the current regime.

## Agentic RAG
- **Transcript retrieval:** semantic search over earnings call transcripts in ChromaDB.
- **Signal retrieval:** SQL queries over the PostgreSQL signal database.
- **Hybrid retrieval:** both sources combined in a single query.
- **End-to-end flow:** a question goes through intent parsing and hybrid retrieval to a synthesized answer that attributes its sources.

## Dashboard
- **Sequence model forecasts:** LSTM and GRU predictions with confidence bands, shown alongside the tree-based models.
- **Regime indicator panel:** each sector's current regime, with a historical timeline.
- **Analyst profile cards:** difficulty, question patterns, and alignment for each analyst.
- **Sparklines:** momentum and acceleration for each signal and company.

## Validation
- **Bootstrap comparison:** sequence models vs. tree-based models, using bootstrap confidence intervals.
- **End-to-end testing:** RAG and integration tests (`tests/test_phase20.py`).