**Repository:** [https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis](https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis)

# Mycroft ECIS — Phase 4 — Pipeline Orchestration, Scoring, and Dashboard

**Timeline:** July 19, 2026 – July 25, 2026

**Scope:** End-to-end LangGraph pipeline, escalation routing, conflict resolution, outcome resolution, scoring, recalibration, dashboard, and API.

---

## Top-Level Pipeline Graph
- **Eleven nodes:**
  1. Ingestion
  2. Chunking
  3. Fast-pass (keyword and FinBERT in parallel)
  4. Escalation classification
  5. LLM extraction (conditional)
  6. Conflict resolution (conditional)
  7. Pass-through (conditional)
  8. Join
  9. NER enrichment
  10. Triangulation
  11. Deduplication and logging
- **Typed state** flows through every node
- **Resolved — batch routing:**
  - LangGraph conditional edges return a single node name, so whole batches were routed to one node
  - Restructured so chunks are partitioned into per-category state lists, and each downstream node consumes its own list

## Escalation Classifier
- **Routing categories:**

| Category | Condition | Route |
|---|---|---|
| A | Fast-pass readers agree, high confidence | LLM confirmation |
| B | Ambiguous | LLM deep reasoning |
| C | Directional disagreement | Conflict resolution |
| D | No signal from either reader | Skip LLM |

- **Adaptive thresholds:** stored in SQLite agent state for adjustment over time
- **Impact:** 60–80% reduction in LLM inference calls

## Conflict Resolution Subgraph
- **Four nodes:**
  1. Context retrieval (three-chunk window from ChromaDB)
  2. Disagreement prompt construction
  3. LLM resolution
  4. Vindication recording (correct reader, conflict type, context)

## Checkpointing and Streaming
- State persisted to SQLite after every node
- Node-level streaming for real-time execution monitoring

## Outcome Resolver
- **Price data:** stock and sector benchmark ETF prices via yfinance
  - At the signal date and at +30, +90, and +180 days
- **Computed per horizon:**
  - Stock return
  - Benchmark return
  - Excess return
- **Pre-registered grading rules:**

| Direction | Correct when |
|---|---|
| Raised | Excess return > 0 |
| Lowered | Excess return < 0 |
| Maintained | \|Excess return\| ≤ 2% |

## Scoring Engine
- **Brier score:** mean squared error between predicted probability and outcome
- **Brier skill score:** improvement over the keyword baseline
- **Expected calibration error (ECE):** gap between stated confidence and observed accuracy, binned by confidence
- **Murphy decomposition:** separates calibration error from resolution
- **Information ratio:** mean excess return divided by its standard deviation

## Recalibration
- **Methods:**
  - Platt scaling: two-parameter sigmoid on logits
  - Isotonic regression: non-parametric monotonic fit
- **Method selection by sample size:** Platt for small samples, isotonic for large samples
- Raw and calibrated confidence both retained on every record

## Streamlit Dashboard
- **Signal explorer:**
  - Filterable table: ticker, direction, raw and calibrated confidence, quote, source, date, verification status
  - Drill-down into reasoning trace, NER entities, and self-consistency votes
- **Reader comparison:** Brier score, skill score, ECE, Murphy components, information ratio, signal count, and verdict per reader
- **Calibration curves:** Plotly reliability diagrams with a diagonal reference line
  - Minimum bin-size threshold and low-sample annotations, added after sparse bins produced misleading jagged curves
- **Agent activity log:** chronological timeline of autonomous decisions
- **RAG query interface (in progress):** natural-language search with metadata filtering and cited passages
- **Resolved — SQLite locking under Streamlit reruns:** fixed with:
  - Connection pooling
  - Context managers
  - Separate read and write paths

## FastAPI Service
- `POST`: submit a transcript and receive extracted signals
- `GET`: retrieve the current scoring report
- Served with Uvicorn
