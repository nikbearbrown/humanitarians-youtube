# Weekly Report: Week 20 (Phase 20)

**Project:** Mycroft — ECIS (Earnings Call Intelligence System) + Decision Scorecard

**Week:** November 8 – November 14, 2026

**Total hours:** 34.5

---

## Summary

Week 20 added four capabilities.

- **Time-series models:** the system can now learn from how signals change over time.
  - LSTM and GRU sequence models trained on 4–8 quarters of history, compared against the tree-based models with bootstrap confidence intervals
  - a three-state Hidden Markov Model that labels each sector bullish, bearish, or transitional, used as context by every prediction model
- **Analyst intelligence:**
  - analyst identity resolution
  - per-analyst question patterns
  - question difficulty scoring
  - analyst-management alignment
  - dodge scores now adjusted for how hard the question was
- **Temporal feature engineering:**
  - lag features (previous three quarters)
  - momentum
  - acceleration
  - rolling z-scores
- **Agentic RAG:** the conversational agent can now combine two sources in one answer, with sources cited.
  - meaning-based search over transcripts in ChromaDB
  - SQL over the signal database in PostgreSQL
- **Dashboard additions:**
  - sequence model forecasts
  - a regime indicator panel
  - analyst profile cards
  - momentum and acceleration sparklines

---

## Work Completed

### Time-Series Models

#### 1. LSTM Network Architecture & Training
*Development · Time-Series Models*
- Designed and trained an LSTM on sequences of 4–8 quarters of signal features per company.
- Tuned the hidden size and dropout regularization for guidance direction prediction.
- **Deliverable:** trained LSTM model with tuned architecture
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/timeseries/sequences.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/timeseries/recurrent.py
- **Status:** Complete

#### 2. GRU Variant Training & Comparison
*Development · Time-Series Models*
- Trained a GRU on the same input structure as the LSTM.
- Compared training speed, convergence, and prediction accuracy against the LSTM.
- **Deliverable:** trained GRU model with LSTM comparison results
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/timeseries/recurrent.py
- **Status:** Complete

#### 3. Sequence Model vs. Tree-Based Model Comparison
*Development · Time-Series Models*
- Compared the LSTM and GRU against the existing tree-based models (XGBoost, LightGBM, Random Forest, CatBoost) using bootstrap confidence intervals.
- Tests whether modeling sequences over time improves prediction.
- **Deliverable:** model comparison report with bootstrap CIs across all architectures
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/timeseries/recurrent.py
- **Status:** Complete

#### 4. Hidden Markov Model Regime Detection
*Development · Time-Series Models*
- Fitted a three-state Hidden Markov Model on sector-level signal aggregates:
  - bullish
  - bearish
  - transitional
- Assigns a market regime label to each quarter.
- **Deliverable:** HMM regime detector with three-state sector-level classification
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/timeseries/hmm.py
- **Status:** Complete

#### 5. Regime Labels as Context Feature
*Development · Time-Series Models*
- Added the regime labels as a context feature to every prediction model.
- Lets the models behave differently in different market states.
- **Deliverable:** regime-conditioned prediction pipeline integration
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/timeseries/hmm.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/timeseries/momentum.py
- **Status:** Complete

### Analyst Intelligence

#### 6. Analyst Identity Extraction & Normalization
*Development · Analyst Intelligence*
- Resolves individual analyst names across calls and maps each analyst to their firm.
- Allows each analyst to be tracked consistently from call to call.
- **Deliverable:** analyst identity resolution module with firm mapping
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/timeseries/analysts.py
- **Status:** Complete

#### 7. Per-Analyst Question Pattern Tracking
*Development · Analyst Intelligence*
- Tracks each analyst's questioning style:
  - who asks harder questions
  - who is consistently bullish or bearish
- **Deliverable:** analyst question pattern tracker with behavioral profiling
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/timeseries/analysts.py
- **Status:** Complete

#### 8. Question Difficulty Scoring
*Development · Analyst Intelligence*
- Scores how rigorous each analyst's questions are, based on:
  - the mix of question types
  - how often they follow up
  - how often their questions are confrontational
- **Deliverable:** question difficulty scoring module with multi-factor rating
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/timeseries/difficulty.py
- **Status:** Complete

#### 9. Difficulty-Normalized Dodge Scoring
*Development · Analyst Intelligence*
- Adjusts dodge scores by how hard the analyst's question was.
- Dodging a tough question now counts differently from dodging an easy one.
- **Deliverable:** difficulty-normalized dodge score integration
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/timeseries/difficulty.py
- **Status:** Complete

#### 10. Analyst-Management Alignment Scoring
*Development · Analyst Intelligence*
- Measures how closely each analyst's framing matches management's language.
- Detects whether an analyst's stance is sympathetic or adversarial.
- **Deliverable:** analyst-management alignment scoring module
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/timeseries/alignment.py
- **Status:** Complete

### Feature Engineering

#### 11. Lag Features (t-1, t-2, t-3)
*Development · Feature Engineering*
- Adds each signal's values from the previous three quarters as extra features, giving the models historical context.
- **Deliverable:** lag feature engineering module with multi-quarter lookback
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/timeseries/lag_features.py
- **Status:** Complete

#### 12. Momentum Features
*Development · Feature Engineering*
- Quarter-over-quarter rate of change for each signal, capturing how fast it is moving and in which direction.
- **Deliverable:** momentum feature computation module
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/timeseries/momentum.py
- **Status:** Complete

#### 13. Acceleration Features
*Development · Feature Engineering*
- Rate of change of momentum.
- Detects turning points where a signal's trend is reversing or speeding up.
- **Deliverable:** acceleration feature computation for inflection detection
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/timeseries/momentum.py
- **Status:** Complete

#### 14. Rolling Z-Score Normalization
*Development · Feature Engineering*
- Normalizes each feature against recent values.
- Readings are judged relative to the current market regime rather than all history.
- **Deliverable:** rolling z-score normalization module
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/timeseries/momentum.py
- **Status:** Complete

### Agentic RAG

#### 15. ChromaDB Transcript Retrieval Connection
*Development · Agentic RAG*
- Connected the conversational agent to the ChromaDB transcript store.
- Enables meaning-based search over earnings call text.
- **Deliverable:** RAG-to-ChromaDB transcript retrieval integration
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/timeseries/rag.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/embedding/embedder.py
- **Status:** Complete

#### 16. PostgreSQL Signal Database Retrieval
*Development · Agentic RAG*
- Connected the agent to the PostgreSQL signal database.
- Enables SQL queries over signals, outcomes, and analytics.
- **Deliverable:** RAG-to-PostgreSQL signal database integration
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/timeseries/rag.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/intelligence/execute.py
- **Status:** Complete

#### 17. Hybrid Retrieval Pipeline
*Development · Agentic RAG*
- Combines two kinds of search in a single query:
  - meaning-based search over transcripts
  - SQL over structured signals
- Answers draw on both the text and the data.
- **Deliverable:** hybrid semantic + SQL retrieval pipeline
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/timeseries/rag.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/intelligence/agent.py
- **Status:** Complete

#### 18. End-to-End RAG Testing
*Development · Agentic RAG*
- Tested the full path: a plain-English question goes through intent parsing and hybrid retrieval to a synthesized answer with sources.
- **Deliverable:** end-to-end RAG test results and validation
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/tests/test_phase20.py
- **Status:** Complete

### Dashboard

#### 19. LSTM/GRU Prediction Output Views
*Development · Dashboard*
- Shows LSTM and GRU forecasts with confidence bands, alongside the tree-based predictions.
- **Deliverable:** LSTM/GRU prediction dashboard views with confidence bands
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/dashboard/views.py
- **Status:** Complete

#### 20. Regime Indicator Panel
*Development · Dashboard*
- Shows the current detected regime for each sector, with a history of past regimes.
- **Deliverable:** regime indicator dashboard panel with historical timeline
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/dashboard/views.py
- **Status:** Complete

#### 21. Analyst Profile Cards
*Development · Dashboard*
- Shows each analyst's difficulty score, question patterns, and alignment with management.
- **Deliverable:** analyst profile card dashboard view
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/dashboard/views.py
- **Status:** Complete

#### 22. Momentum & Acceleration Sparklines
*Development · Dashboard*
- Small trend lines for each signal and company, showing speed of change and turning points at a glance.
- **Deliverable:** momentum/acceleration sparkline dashboard view
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/dashboard/views.py
- **Status:** Complete

### Debugging

#### 23. Debugging & Testing
*Development · Debugging*
- Resolved issues across the time-series models, analyst intelligence, feature engineering, and RAG integration.
- Ran end-to-end testing across all the new components.
- **Deliverable:** resolved issues and verified fixes
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/tests/test_phase20.py
- **Status:** Complete

### Research

#### 24. LSTM/GRU Architecture Review for Financial Sequences
*Research · Time-Series Models*
- Reviewed LSTM and GRU architectures for modeling sequences of financial signals.
- Covered input structure, hidden size, and regularization for quarterly guidance data.
- **Deliverable:** research notes on LSTM/GRU for financial signal sequences
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/research
- **Status:** Complete

#### 25. HMM Regime Detection in Financial Literature
*Research · Regime Detection*
- Studied Hidden Markov Model approaches to market regime detection.
- Covered how states are defined, how observations are modeled, and how transition probabilities are estimated.
- **Deliverable:** research notes on HMM regime detection methods
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/research
- **Status:** Complete

#### 26. Analyst Speaker Label Audit
*Research · Analyst Intelligence*
- Audited analyst speaker labels across the 25-ticker corpus.
- Checked name resolution, firm mapping coverage, and consistency across calls.
- **Deliverable:** analyst speaker label audit report
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/research
- **Status:** Complete

### Writing

#### 27. Substack Article: "Deep Learning for Time Series: LSTMs, N-BEATS, and Transformers Compared"
*Writing · Substack Article*
- Compares LSTMs, N-BEATS, and transformers for time-series forecasting.
- Argues that on financial data, rigorous evaluation matters more than the choice of architecture.
- **Deliverable:** published Substack article
- **Link:** https://mycroftproject.substack.com/p/deep-learning-for-time-series-lstms
- **Status:** Complete (published)

### Artifact

#### 28. LSTM vs. Tree Model Showdown
*Artifact · Artifact*
- Interactive side-by-side comparison for any company.
- Shows LSTM/GRU predictions against tree-based predictions, with performance metrics and confidence bands.
- **Deliverable:** Artifact: LSTM vs. Tree Model Showdown
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/artifacts
- **Status:** Complete

### Video

Both videos follow the same split:
- **Concept, ideas, narration, and direction:** original work.
- **Assembly:** Claude, using the video generation tool created by Humanitarians AI.

#### 29. Video: "ECIS Episode 15: Weekly Project Update"
*Documentation · Video Production*
- Weekly Mycroft ECIS project update. Covers:
  - LSTM/GRU sequence models
  - HMM regime detection
  - analyst difficulty-normalized dodge scores
  - RAG-powered agent querying
- **Deliverable:** Video: ECIS Episode 15
- **Links:**
  - https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-11-13-ecis-explained
  - https://drive.google.com/drive/folders/1VuL_1Lpa8AA0eVSAJeNUrWUkF4Abus-L
- **Status:** Complete

#### 30. Video: "Time Series Explainer"
*Documentation · Video Production*
- STEM educational video on time series. Covers:
  - why row order matters
  - trend, seasonality, and residual decomposition
  - stationarity
  - forecasting methods
  - time-based evaluation splits
- **Deliverable:** Video: Time Series Explainer
- **Links:**
  - https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-11-13-time-series-explainer
  - https://drive.google.com/drive/folders/1bung95gnt2lAK_bqqZGtlcl-KEl52IVW
- **Status:** Complete