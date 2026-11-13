# Weekly Report: Week 4 (Phase 4)

**Project:** Mycroft — ECIS (Earnings Call Intelligence System) + Decision Scorecard
**Week:** July 19 – July 25, 2026
**Total hours:** 27.5

---

## Summary

- LangGraph orchestration pipeline completed:
  - top-level graph
  - escalation classifier (Category A/B/C/D)
  - conflict resolution subgraph
  - checkpointing and streaming observability
- Scoring layer completed:
  - point-in-time-safe outcome resolver (yfinance)
  - scoring engine: Brier, Brier skill score, ECE, Murphy decomposition
  - Platt + isotonic recalibration
- Streamlit dashboard built with four views.
- Debugging covered three areas: LangGraph routing, SQLite locking, and calibration visualization.
- One Claude artifact and one Substack article completed.

---

## Work Completed

### 1. Top-Level Pipeline Graph
*Development · LangGraph Pipeline*
- Full pipeline graph: ingestion → chunking → first-pass → escalation → extraction → join → triangulation → deduplication → logging.
- **Deliverable:** complete LangGraph pipeline graph
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/graphs/pipeline_graph.py
- **Status:** Complete

### 2. Escalation Classifier (Category A/B/C/D)
*Development · LangGraph Pipeline*
- Conditional routing by confidence category.
- **Deliverable:** escalation classifier with configurable thresholds (stored in SQLite agent state)
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/graphs/orchestration_agent.py
- **Status:** Complete

### 3. Conflict Resolution Subgraph
*Development · LangGraph Pipeline*
- Context retrieval, disagreement prompt, LLM resolution, vindication recording.
- **Deliverable:** conflict resolution subgraph
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/graphs/conflict_subgraph.py
- **Status:** Complete

### 4. Pipeline Checkpointing + Streaming Observability
*Development · LangGraph Pipeline*
- Configured checkpointing and streaming for pipeline observability.
- **Deliverable:** pipeline observability layer
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/graphs/pipeline_graph.py
- **Status:** Complete

### 5. Outcome Resolver + yfinance Price Fetching
*Development · Scoring Layer*
- Fetches stock and benchmark prices at the signal date and at 30- and 90-day horizons via yfinance.
- Point-in-time discipline is enforced architecturally: the resolver queries by date, so it cannot access future prices.
- **Deliverable:** outcome resolver with point-in-time-safe price fetching
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/scoring/outcome_resolver.py
- **Status:** Complete

### 6. Scoring Engine (Brier, ECE, Murphy)
*Development · Scoring Layer*
- Brier score, Brier skill score (vs. keyword baseline), ECE, and Murphy decomposition via scikit-learn.
- Design decisions on ECE binning for skewed distributions and on small-sample Murphy decomposition.
- **Deliverable:** complete scoring engine (4 metrics)
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/scoring/metrics.py
- **Status:** Complete

### 7. Recalibration Module (Platt Scaling + Isotonic Regression)
*Development · Scoring Layer*
- Implemented both methods.
- **Deliverable:** recalibration module with cross-validated method selection
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/scoring/recalibrator.py
- **Status:** Complete

### 8. Streamlit Dashboard: Full Build
*Development · Streamlit Dashboard*
- Four views:
  - **Signal Explorer:** searchable, filterable table
  - **Reader Comparison:** side-by-side metrics
  - **Calibration Curves:** Plotly charts, with sparse-data handling
  - **Agent Activity Log:** decision timeline
- **Deliverable:** complete Streamlit dashboard (4 views)
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/src/ecis/dashboard
- **Status:** Complete

### 9. Debugging: LangGraph Routing + SQLite Locking + Calibration Viz
*Development · Debugging*
- **LangGraph routing:** conditional edges routed the entire batch to one node; the graph was restructured to partition by category.
- **SQLite locking:** Streamlit reads conflicted with scoring engine writes.
- **Calibration viz:** curves were misleading with sparse data.
- **Deliverable:** bug fixes across the pipeline, database, and visualization layers
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/src/ecis/graphs
- **Status:** Complete

### 10. LangGraph Streaming + Streamlit Integration
*Research · Integration*
- Explored integration patterns for LangGraph streaming output with Streamlit's rerun model.
- **Deliverable:** integration patterns documented
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/research
- **Status:** Complete

### 11. Substack Article: "Attention Patterns in FinBERT"
*Writing · Substack Article*
- Examines FinBERT's attention patterns on earnings call text, using gradient-based attribution to identify which tokens drive sentiment classification.
- Asks whether the model focuses on actual guidance language or on surrounding boilerplate.
- Looks at how attention shifts at the 512-token truncation boundary.
- Explains why systematic attention to safe harbour disclaimers creates false signals in the extraction pipeline.
- **Deliverable:** published Substack article
- **Link:** https://mycroftproject.substack.com/p/attention-patterns-in-finbert-what
- **Status:** Complete (published)

### 12. Escalation Routing Simulator
*Artifact · Claude Artifact*
- Interactive component that simulates Category A/B/C/D escalation routing.
- Input confidence levels and reader agreement patterns to see which downstream path triggers.
- **Deliverable:** Claude Artifact: Escalation Routing Simulator
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/artifacts
- **Status:** Complete
