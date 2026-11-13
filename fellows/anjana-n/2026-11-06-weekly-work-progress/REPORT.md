# Weekly Report: Week 19 (Phase 19)

**Project:** Mycroft — ECIS (Earnings Call Intelligence System) + Decision Scorecard

**Week:** November 1 – November 7, 2026

**Total hours:** 30.75

---

## Summary

Week 19 added three new capabilities.

- **Uncertainty quantification:** each forecast now carries a measure of how uncertain it is.
  - conformal prediction intervals
  - Monte Carlo dropout on the MLP
  - disagreement across the six revision models
  - selective prediction, which abstains when uncertainty is too high
- **Cross-company intelligence:** how language shifts spread between companies.
  - contagion modeling
  - supply chain language propagation
  - temporal lag modeling
  - leading indicator identification
- **Agentic foundation:** the first version of the conversational agent from the next-period plan.
  - a LangGraph conversational agent
  - an intent parser
  - tool routing
  - query execution
  - response synthesis
- **Dashboard additions:**
  - prediction interval bands
  - uncertainty indicators
  - a contagion network graph
  - temporal lag curves
  - a chat interface prototype

---

## Work Completed

### Uncertainty Quantification

#### 1. Conformal Prediction Intervals
*Development · Uncertainty Quantification*
- Produces prediction intervals around point estimates without assuming any particular distribution.
- Gives calibrated uncertainty bands for each forecast.
- **Deliverable:** conformal prediction module with calibrated interval generation
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/intelligence/conformal.py
- **Status:** Complete

#### 2. Monte Carlo Dropout on MLP
*Development · Uncertainty Quantification*
- Runs the MLP several times with dropout left on.
- Uses the spread of the results as an uncertainty estimate.
- **Deliverable:** Monte Carlo dropout inference module with variance computation
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/intelligence/dropout.py
- **Status:** Complete

#### 3. Ensemble Disagreement as Uncertainty Feature
*Development · Uncertainty Quantification*
- Measures how much the six guidance revision models disagree on each prediction.
- Uses that disagreement as an explicit uncertainty feature.
- **Deliverable:** ensemble disagreement uncertainty feature module
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/intelligence/disagreement.py
- **Status:** Complete

#### 4. Selective Prediction with Abstention
*Development · Uncertainty Quantification*
- The system declines to issue a forecast when uncertainty exceeds a configurable threshold.
- Keeps unreliable predictions from reaching downstream users.
- **Deliverable:** selective prediction module with configurable abstention threshold
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/intelligence/selective.py
- **Status:** Complete

#### 5. Prediction Interval & Uncertainty Storage
*Development · Uncertainty Quantification*
- Stores the following in PostgreSQL alongside each forecast:
  - prediction intervals
  - Monte Carlo variance
  - ensemble disagreement scores
  - abstention flags
- Used for monitoring and dashboard display.
- **Deliverable:** uncertainty metrics persisted in PostgreSQL forecast records
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/intelligence/refresh.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/db/init_db.py
- **Status:** Complete

### Cross-Company Intelligence

#### 6. Contagion Modeling
*Development · Cross-Company Intelligence*
- Detects when one company's language shift comes before similar shifts at its sector peers.
- Points to possible patterns in how information spreads between companies.
- **Deliverable:** contagion detection module with sector-level shift tracking
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/intelligence/contagion.py
- **Status:** Complete

#### 7. Supply Chain Language Propagation
*Development · Cross-Company Intelligence*
- Tracks supplier hedging patterns that predict customer guidance revisions along supply chain relationships.
- **Deliverable:** supply chain propagation module with supplier-customer linkage
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/intelligence/supply_chain.py
- **Status:** Complete

#### 8. Temporal Lag Modeling
*Development · Cross-Company Intelligence*
- Measures the delay between a language signal appearing and the price reacting, for each signal type.
- Identifies timing windows that could be acted on.
- **Deliverable:** temporal lag estimation module with per-signal-type delay curves
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/intelligence/lag.py
- **Status:** Complete

#### 9. Leading Indicator Identification
*Development · Cross-Company Intelligence*
- Detects which companies' language shifts predict sector-wide moves.
- Ranks companies by how far ahead their signals appear.
- **Deliverable:** leading indicator identification with company-level lead rankings
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/intelligence/contagion.py
- **Status:** Complete

#### 10. Cross-Company Intelligence Storage
*Development · Cross-Company Intelligence*
- Stores contagion scores, temporal lag estimates, and propagation links in PostgreSQL for querying and visualization.
- **Deliverable:** cross-company intelligence data persisted in PostgreSQL
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/intelligence/refresh.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/db/init_db.py
- **Status:** Complete

### Agentic Foundation

#### 11. Conversational Agent Architecture
*Development · Agentic Foundation*
- Designed and built a conversational agent in LangGraph.
- Keeps track of context so it can handle follow-up questions across the ECIS system.
- **Deliverable:** LangGraph-based conversational agent with state management
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/intelligence/agent.py
- **Status:** Complete

#### 12. Intent Parser
*Development · Agentic Foundation*
- Sorts each user question into one of four types:
  - retrieval
  - comparison
  - analysis
  - explanation
- Sends it to the matching processing pipeline.
- **Deliverable:** intent classification module with four query type categories
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/intelligence/intent.py
- **Status:** Complete

#### 13. Tool Routing
*Development · Agentic Foundation*
- Connects the agent to the right part of the system for each question type:
  - the signal database
  - the prediction engine
  - the analytics modules
- **Deliverable:** tool routing module with database and analytics connections
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/intelligence/execute.py
- **Status:** Complete

#### 14. Query Execution Pipeline
*Development · Agentic Foundation*
- Turns plain-English questions into structured database and analytics calls.
- Handles extracting parameters and assembling the query.
- **Deliverable:** natural language to structured query execution pipeline
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/intelligence/execute.py
- **Status:** Complete

#### 15. Response Synthesis
*Development · Agentic Foundation*
- Builds structured answers from the retrieved data.
- Combines tables, computed metrics, and short explanations.
- **Deliverable:** response synthesis module with multi-format answer composition
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/intelligence/agent.py
- **Status:** Complete

### Dashboard

#### 16. Prediction Interval Bands on Forecast View
*Development · Dashboard*
- Shows conformal prediction intervals as shaded bands around each forecast on the timeline.
- **Deliverable:** forecast timeline with prediction interval bands
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/dashboard/views.py
- **Status:** Complete

#### 17. Uncertainty Indicators per Prediction
*Development · Dashboard*
- Shows Monte Carlo variance, ensemble disagreement, and abstention status next to each forecast.
- **Deliverable:** per-prediction uncertainty indicator dashboard display
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/dashboard/views.py
- **Status:** Complete

#### 18. Cross-Company Contagion Network Graph
*Development · Dashboard*
- Interactive network graph of how language shifts spread between companies.
- Arrows show the direction of influence.
- **Deliverable:** cross-company contagion network graph view
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/dashboard/views.py
- **Status:** Complete

#### 19. Temporal Lag Curve Visualizations
*Development · Dashboard*
- Charts the delay between signals and price moves, by signal type and by company.
- **Deliverable:** temporal lag curve dashboard view
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/dashboard/views.py
- **Status:** Complete

#### 20. Agentic Chat Interface Prototype
*Development · Dashboard*
- A chat panel for asking the ECIS system questions in plain English.
- Shows how each question was classified and which tools were used.
- **Deliverable:** agentic chat interface prototype dashboard panel
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/dashboard/views.py
- **Status:** Complete

### Debugging

#### 21. Debugging & Testing
*Development · Debugging*
- Resolved issues across the uncertainty quantification, cross-company intelligence, and agentic modules.
- Ran integration testing across all the new components.
- **Deliverable:** resolved issues and verified fixes
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/tests/test_phase19.py
- **Status:** Complete

### Research

#### 22. Conformal Prediction Methods Review
*Research · Uncertainty Quantification*
- Reviewed conformal prediction methods for financial time series.
- Assessed which distribution-free interval approaches suit guidance revision forecasts.
- **Deliverable:** research notes on conformal prediction for financial data
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/research
- **Status:** Complete

#### 23. Cross-Company Signal Correlation Audit
*Research · Cross-Company Intelligence*
- Audited existing cross-company signal correlations to find:
  - patterns
  - coverage gaps
  - opportunities for contagion and propagation modeling
- **Deliverable:** research notes on existing cross-company signal patterns
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/research
- **Status:** Complete

#### 24. LangChain vs. LangGraph Evaluation for Agentic Layer
*Research · Agentic Architecture*
- Compared LangChain and LangGraph for the conversational layer.
- Assessed state management, tool integration, and routing.
- **Deliverable:** research notes on agentic framework selection
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/research
- **Status:** Complete

### Writing

#### 25. Substack Article: "Mixture of Experts"
*Writing · Substack Article*
- Explains the Mixture of Experts (MoE) architecture.
- Maps it to earnings calls, where structurally different passages could naturally route to specialized experts.
- Covers memory cost, how sensitive the router is to quantization, and expert routing as an interpretability signal.
- **Deliverable:** published Substack article
- **Link:** https://mycroftproject.substack.com/p/mixture-of-experts-financial-text-routing
- **Status:** Complete (published)

### Artifact

#### 26. Agentic Query Demo
*Artifact · Claude Artifact*
- Interactive artifact that accepts plain-English questions about the ECIS system.
- Shows for each question:
  - how it was classified (retrieval, comparison, analysis, or explanation)
  - which tools were chosen
  - the structured response
- **Deliverable:** Claude Artifact: Agentic Query Demo
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/artifacts
- **Status:** Complete

### Video

Both videos follow the same split.
- **Concept, ideas, narration, and direction:** original work.
- **Assembly:** Claude, using the video generation tool created by Humanitarians AI.

#### 27. Video: "ECIS Episode 14: Weekly Project Update"
*Documentation · Video Production*
- Weekly Mycroft ECIS project update. Covers:
  - uncertainty bands
  - selective abstention
  - cross-company language propagation
  - the conversational agent interface
- **Deliverable:** Video: ECIS Episode 14
- **Links:**
  - https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-11-06-ecis-explained
  - https://drive.google.com/drive/folders/1ysPtFvku6cnpYUk8tTwBoHPfHQzjCOAn
- **Status:** Complete

#### 28. Video: "MoE Explainer: Mixture of Experts"
*Documentation · Video Production*
- STEM educational video on Mixture of Experts.
- Shows how one large network is replaced by several specialist sub-networks and a learned router, so only a fraction of the model runs for each token.
- **Deliverable:** Video: MoE Explainer
- **Links:**
  - https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-11-06-moe-explainer
  - https://drive.google.com/drive/folders/1uyryieZQ6wX4oC7eCjpFrt3nNW86yCSc
- **Status:** Complete
