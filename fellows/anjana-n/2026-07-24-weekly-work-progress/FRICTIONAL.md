# Friction Log: Week 4 (Phase 4)

**Project:** Mycroft — ECIS + Decision Scorecard
**Week:** July 19 – July 25, 2026

---

## 1. Focus of the week

- LangGraph orchestration:
  - top-level pipeline graph
  - escalation classifier (A/B/C/D)
  - conflict resolution subgraph
  - checkpointing and streaming
- Scoring layer:
  - yfinance outcome resolver
  - Brier / skill score / ECE / Murphy scoring engine
  - Platt + isotonic recalibration
- Streamlit dashboard: four views.
- Debugging: routing, SQLite concurrency, calibration visualization.
- Research: LangGraph–Streamlit streaming integration; video production tooling.
- Writing: "Attention Patterns in FinBERT."
- Artifact: Escalation Routing Simulator.

## 2. What was tried, and what was expected

- **Routing.** Expectation: LangGraph conditional edges would split a batch of chunks across downstream nodes by category.
- **Database access.** Expectation: the components built separately (Streamlit reads, scoring engine writes) would share the SQLite databases without conflict.
- **Calibration curves.** Expectation: the curves would give a fair picture of system calibration from the available resolved outcomes.
- **Parameters.** Expectation: the proposal's specifications would be enough to set the key values:
  - "high confidence"
  - "Platt for small, isotonic for larger"
  - ECE binning
- **Point-in-time.** Expectation: the Week 1 point-in-time principle would carry into price fetching without extra design.

## 3. Points of resistance, and next steps taken

### LangGraph conditional edge routing (load-bearing)
- **The mismatch:** a routing function returns a single node name. The first implementation sent the entire batch to one node, all to the LLM path or all to conflict resolution, never a mix.
- **Next step:**
  - Restructured the graph to partition chunks into category-specific lists within state.
  - Downstream nodes now pull from their own list.
  - Several nodes and their state read/write patterns changed.
- **Lesson:** a mismatch between the framework's abstraction and the actual problem only showed up when the batch didn't split.

### SQLite locking between Streamlit and the scoring engine
- **The collision:** Streamlit's rerun model opens new connections on every interaction. Signal explorer reads from `signals.db` collided with scoring engine writes to `outcomes.db`, causing locking errors.
- **Next step:** connection pooling with proper context managers, and separate read and write paths.
- **Lesson:** a concurrency problem that only surfaced once separately built components shared a database.

### Calibration curves with sparse data
- **What looked wrong:** with ~50 resolved outcomes, most confidence bins held fewer than 3 points. The curves came out jagged and made the system look badly miscalibrated.
- **The actual issue:** insufficient data, not miscalibration.
- **Next step:** a minimum bin size threshold, plus annotations flagging low-count bins.
- **Lesson:** a chart can be technically correct and still communicate the wrong conclusion. This is the Fluency Trap again: a confident-looking chart telling the wrong story.

### Parameters the proposal leaves open
- **Escalation threshold:** the A/B boundary sets compute spend and the missed-signal rate at once. Stored in SQLite agent state, not hardcoded, because the right values can only be found by observing the system.
- **ECE binning:** fixed-width vs. adaptive bins, chosen for a distribution clustered at 0.6–0.8.
- **Murphy decomposition:** bin handling at N≈50.
- **Platt vs. isotonic:** both fail in known ways at N≈50.
  - Both were implemented, with a watchdog selecting by cross-validated ECE.
  - Rolling window: 50 signals.
  - Trigger: ECE > 0.10.

### Point-in-time discipline made operational
- The outcome resolver queries prices by date, never by "latest," so future prices are structurally inaccessible.

## 4. AI and other contributions: accepted, changed, rejected

### Gru (SDD session)
- Documented the pipeline architecture, the scoring layer decisions, and the escalation threshold rationale.

### Eddy
- Reviewed "Attention Patterns in FinBERT" before publication.

### Claude
- Built the Escalation Routing Simulator: input confidence levels and agreement patterns, see which path triggers.
- The routing logic was designed in the build; the artifact makes it visible.

## 5. Understood now, and still unresolved

### Understood
- **Proposal limits:** the proposal gives direction, but parameter values (thresholds, boundaries, binning) have to come from judgment and observation.
- **Framework abstractions:** a framework's abstractions can silently mismatch the problem. Routing by batch is not routing by item.
- **Shared resources:** shared databases need explicit concurrency design once separately built components meet.
- **Presentation integrity:** honest reporting includes how the system presents its own data. A data-starved chart can mislead as much as one that hides real miscalibration.
- **Point-in-time:** this is now enforced in code, not only in principle.

### Unresolved
- **Escalation threshold:** the right A/B value, still to be found by observing system behavior.
- **Recalibration method:** whether Platt or isotonic actually performs better once more outcomes resolve.
- **Fine-tuning:** whether to revise the QLoRA approach for the actual compute budget. Carried from Week 2.
- **vLLM vs. Ollama:** decision pending. Carried from Week 3.
- **Week 5 scope:** not yet set. End-to-end testing, hand-labeling, scoring validation, integration testing, and the video are all candidates.
