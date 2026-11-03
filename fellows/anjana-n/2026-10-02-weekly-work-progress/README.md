**Repository:** [https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis](https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis)

# Mycroft ECIS — Phase 14 — ChromaDB Optimization, Data Quality, Evaluation Framework, and Grafana

**Timeline:** September 27, 2026 – October 3, 2026

**Scope:** Vector store optimization, database performance tuning, data quality and lineage, statistical rigor in evaluation, drift monitoring, and Grafana observability.

---

## ChromaDB Optimization
- **Collection strategy:**
  - Unified collection with ticker, date, and section metadata filters, replacing per-ticker collections
  - Simplifies management and enables cross-ticker retrieval
  - Naming conventions and metadata schema documented
- **Embedding versioning:**
  - Model identifier and version hash stored per vector
  - Supports re-embedding on upgrade while keeping prior versions for A/B retrieval comparison
- **HNSW tuning:**
  - Parameters `ef_construction`, `M`, `ef_search` tuned against a held-out relevance set
  - Benchmarked recall@5 and recall@10
  - Optimized for the quality–speed trade-off in exemplar and temporal retrieval
- **Exemplar store cleanup:**
  - Near-duplicates removed (cosine similarity > 0.95)
  - Classes rebalanced (raised / lowered / maintained / none)
  - Adversarial maintained/none examples added
  - Retrieval validated before and after

## PostgreSQL Performance
- **Connection pooling:**
  - Pool size, minimum and maximum connections, idle timeout, and recycling
  - Tuned for concurrent Streamlit load
- **Query monitoring:**
  - `pg_stat_statements` enabled
  - Slow-query logging at 100 ms
  - `EXPLAIN ANALYZE` on the top dashboard queries
- **Query refactoring:** two queries performing sequential scans refactored to use the composite indexes

## Outcome Resolver Caching
- Resolved price data persisted in the TimescaleDB hypertable
- Hypertable checked before any yfinance request
- **Full 25-ticker resolution time:** reduced from hours to minutes on subsequent runs

## Data Quality
- **Data profiling, after each ingestion batch:**
  - Distribution summaries
  - Missing-value counts
  - IQR outlier detection on confidence and returns
  - Categorical frequencies
  - Results stored in PostgreSQL
- **Data lineage:** JSON provenance chain per signal covering:
  - Raw file and cleaned text
  - Chunk and fast-pass results
  - Escalation category and LLM output
  - Conflict resolution
  - Triangulation inputs and weights
  - Deduplication decision and final validated signal
- **Completeness monitoring:** per-ticker flags for:
  - Missing consensus estimates
  - Price gaps
  - Unpopulated ChromaDB entries
  - Unresolved outcomes past their evaluation horizon
- **Schema evolution standard:**
  - All changes go through Alembic migrations with upgrade and downgrade paths
  - Nullable columns preferred
  - Defaults required for non-nullable additions
  - Migrations tested on staging first

## Evaluation Framework
- **Bootstrap confidence intervals:**
  - 1,000 resamples, 95% CI
  - Applied to Brier score, skill score, ECE, and information ratio
- **Paired permutation tests:**
  - 10,000 permutations per model pair (Llama, Mistral, Qwen)
  - p-values reported in the reader comparison table
- **Power analysis:**
  - Minimum resolved-signal count needed to detect a given effect size at 80% power, per metric and model pair
  - Informs ticker-expansion decisions

## Drift Monitoring
- **Concept drift:**
  - Population Stability Index (PSI) and KL divergence on feature distributions over rolling quarterly windows
  - Alerts surfaced in Grafana
- **Prediction decay:**
  - Calibration watchdog extended to the prediction layer
  - Tracks rolling accuracy, ECE, and skill
  - An alert and retraining proposal fire after 10 consecutive predictions below the naive momentum baseline

## Grafana Observability
- **Setup:**
  - PostgreSQL data source with TimescaleDB query macros
  - Dark theme
  - Folders for reader health, pipeline performance, and data quality
- **Dashboards:**

| Dashboard | Panels | Alerts |
|---|---|---|
| Reader health | Success, failure, abstention, and average confidence per reader; vote distribution; verification confirm / revise / reject rates | Failure rate > 10%; abstention spikes |
| Extraction latency | p50 / p95 / p99 per reader; retry overhead; batch duration; latency heatmap by chunk quality | p95 > 30 s |
| Signal throughput | Signals per batch; direction mix over time; A/B/C/D escalation breakdown; per-ticker completeness | ECE > 0.10 |

## Validation
- Full re-run with all Phase 14 features enabled
- ChromaDB optimization improved retrieval recall without degrading extraction accuracy
- Grafana dashboards reflect live pipeline state
- End-to-end runtime improvement benchmarked from caching and connection pooling
