# Weekly Report: Week 14 (Phase 14)

**Project:** Mycroft — ECIS (Earnings Call Intelligence System) + Decision Scorecard
**Week:** September 27 – October 3, 2026
**Total hours:** 36.5

---

## Summary

- Focus shifted from new extraction capabilities to hardening the infrastructure beneath them:
  - ChromaDB optimization
  - database performance tuning
  - data quality and lineage
  - statistical rigor in evaluation
  - Grafana monitoring
  - concept drift detection
- **ChromaDB:** HNSW tuning (ef_construction 200→512, M 16→48) raised Recall@10 from 0.89 to 0.94 on held-out queries.
- **Evaluation:** bootstrap confidence intervals, paired permutation tests, and a power analysis module were added.
- **Key finding:** at n≈45, power for medium effect sizes is about 0.6.
  - Roughly 40% of real model differences would go undetected.
  - Subtle model comparisons are not trusted until the dataset grows.
- **Grafana:** dashboards for reader health, extraction latency, and signal throughput, plus alert rules.
- **Outputs:**
  - two Claude artifacts
  - two Substack articles
  - two videos

---

## Work Completed

### ChromaDB Optimization

#### 1. Collection Management Strategy
*Development · ChromaDB Optimization*
- Designed and implemented a collection management strategy.
- Compared separate collections per ticker against unified collections with metadata filtering, to find the best retrieval performance.
- **Deliverable:** collection management configuration and strategy document
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/embedding/embedder.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/embedding/README.md
- **Status:** Complete

#### 2. Embedding Versioning System
*Development · ChromaDB Optimization*
- Tracks which MiniLM checkpoint produced each vector.
- Supports re-embedding on a model upgrade without data loss.
- **Deliverable:** embedding versioning module with checkpoint tracking
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/embedding/versioning.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/embedding/embedder.py
- **Status:** Complete

#### 3. HNSW Index Parameter Tuning
*Development · ChromaDB Optimization*
- Tuned the HNSW parameters ef_construction and M to balance retrieval quality against speed for financial text embeddings.
- **Deliverable:** optimized HNSW index configuration
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/embedding/hnsw.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/config/settings.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/embedding/embedder.py
- **Status:** Complete

#### 4. Few-Shot Exemplar Store Cleanup
*Development · ChromaDB Optimization*
- Deduplicated the few-shot exemplars and rebalanced them across direction classes.
- Improves retrieval consistency and reduces class imbalance in exemplar selection.
- **Deliverable:** cleaned and rebalanced exemplar store
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/embedding/exemplar_cleanup.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/embedding/exemplar_store.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/main.py
- **Status:** Complete

#### 5. Retrieval Quality Validation
*Development · ChromaDB Optimization*
- Tested retrieval quality before and after optimization to quantify the improvement in exemplar selection accuracy.
- **Deliverable:** retrieval quality comparison report (pre vs. post optimization)
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/embedding/hnsw.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/tests/test_phase14.py
- **Status:** Complete

### Database Performance

#### 6. Connection Pooling Configuration
*Development · Database Performance*
- Configured psycopg2 connection pooling for PostgreSQL: pool sizing, min/max connections, and idle timeout.
- **Deliverable:** connection pool configuration with tuned parameters
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/db/pool.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/db/postgres.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/config/settings.py
- **Status:** Complete

#### 7. Query Performance Monitoring Setup
*Development · Database Performance*
- Configured pg_stat_statements and enabled slow query logging.
- Ran EXPLAIN ANALYZE on the top dashboard queries to identify optimization targets.
- **Deliverable:** query monitoring setup with slow query logging enabled
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/db/query_monitor.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/main.py
- **Status:** Complete

#### 8. Outcome Resolver Caching Layer
*Development · Database Performance*
- Resolved outcomes now persist in a TimescaleDB hypertable.
- This removes redundant yfinance API calls for dates already fetched.
- **Deliverable:** outcome caching layer with TimescaleDB persistence
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/scoring/price_cache.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/scoring/outcome_resolver.py
- **Status:** Complete

### Data Quality & Lineage

#### 9. Data Profiling Module
*Development · Data Quality & Lineage*
- Generates summary statistics automatically for each ingestion batch: distributions, missing values, and outliers.
- **Deliverable:** data profiling module with automated batch analysis
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/quality/profiler.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/main.py
- **Status:** Complete

#### 10. Data Lineage Tracking Implementation
*Development · Data Quality & Lineage*
- Traces each final signal back through every transformation step, from raw transcript to decision log.
- **Deliverable:** data lineage tracking module with full provenance chains
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/quality/lineage.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/extraction/triangulator.py
- **Status:** Complete

#### 11. Data Completeness Monitoring
*Development · Data Quality & Lineage*
- Flags, for each ticker:
  - missing FMP coverage
  - yfinance gaps
  - ChromaDB population gaps
- **Deliverable:** completeness monitoring with gap detection alerts
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/quality/completeness.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/dashboard/views.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/main.py
- **Status:** Complete

#### 12. Schema Evolution Strategy via Alembic
*Development · Data Quality & Lineage*
- Standardized schema evolution through Alembic migrations.
- New columns and tables can be added without breaking existing pipeline code.
- **Deliverable:** Alembic migration templates and schema evolution guidelines
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/alembic/
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/docs/data-quality.md
- **Status:** Complete

### Evaluation Framework

#### 13. Bootstrap Confidence Intervals for Scorecard Metrics
*Development · Evaluation Framework*
- Reports uncertainty bounds alongside the Brier score, skill score, and ECE.
- **Deliverable:** confidence interval computation module for Scorecard metrics
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/scoring/bootstrap.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/scoring/scorer.py
- **Status:** Complete

#### 14. Statistical Significance Testing on Model Differences
*Development · Evaluation Framework*
- Paired permutation tests check whether performance differences between Qwen and Llama are statistically significant or just noise.
- **Deliverable:** significance testing module with paired permutation tests
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/scoring/significance.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/scoring/evaluation.py
- **Status:** Complete

#### 15. Power Analysis Module
*Development · Evaluation Framework*
- Computes the minimum sample size needed for reliable metric comparisons, given the current variance in model evaluations.
- **Deliverable:** power analysis module with sample size recommendations
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/scoring/power.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/scoring/evaluation.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/main.py
- **Status:** Complete

### Grafana Setup

#### 16. Grafana Installation & Data Source Configuration
*Development · Grafana Setup*
- Installed Grafana and configured PostgreSQL as the primary data source for the pipeline monitoring dashboards.
- **Deliverable:** Grafana instance connected to PostgreSQL data source
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/grafana/
- **Status:** Complete

#### 17. Reader Health Dashboard
*Development · Grafana Setup*
- Tracks, for every pipeline reader over time:
  - success rate
  - failure rate
  - abstention rate
  - average confidence
- **Deliverable:** reader health Grafana dashboard with per-reader metrics
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/grafana/
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/extraction/health.py
- **Status:** Complete

#### 18. Extraction Latency Dashboard
*Development · Grafana Setup*
- Shows per-reader latency percentiles (p50, p95, p99), retry overhead, and batch processing time.
- **Deliverable:** extraction latency Grafana dashboard with percentile tracking
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/grafana/
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/extraction/latency.py
- **Status:** Complete

#### 19. Signal Throughput Dashboard
*Development · Grafana Setup*
- Shows signals per batch, direction distribution over time, and the escalation category breakdown.
- **Deliverable:** signal throughput Grafana dashboard with trend analysis
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/grafana/
- **Status:** Complete

### Inference Reliability

#### 20. Concept Drift Detection Module
*Development · Inference Reliability*
- Monitors shifts in the relationship between language patterns and guidance direction over time.
- Uses PSI and KL divergence on feature distributions.
- **Deliverable:** concept drift detection module with PSI/KL divergence monitoring
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/scoring/drift.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/main.py
- **Status:** Complete

#### 21. Prediction Model Decay Tracking
*Development · Inference Reliability*
- Extended the calibration watchdog to the prediction layer.
- Adds rolling accuracy monitoring and automatic alerts when model performance degrades.
- **Deliverable:** extended calibration watchdog with prediction layer monitoring
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/prediction/decay_watch.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/main.py
- **Status:** Complete

### Dashboard

#### 22. Grafana Alert Rules Configuration
*Development · Dashboard*
- Configured three alert rules:
  - calibration drift: ECE > 0.10
  - reader health anomalies: failure rate > 10%
  - extraction latency spikes: p95 > 30s
- **Deliverable:** Grafana alert rules for calibration, health, and latency thresholds
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/grafana/
- **Status:** Complete

#### 23. Grafana Theme & Dashboard Organization
*Development · Dashboard*
- Applied a dark theme and grouped dashboard panels logically to streamline monitoring.
- **Deliverable:** themed and organized Grafana dashboard layout
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/grafana/
- **Status:** Complete

### Debugging

#### 24. Debugging & Issue Resolution
*Development · Debugging*
- Identified and resolved issues across the pipeline. The main ones:
  - **Permutation tests:** p-values were unstable at 500 permutations.
  - **PSI binning:** equal-width bins misled on skewed features.
  - **ChromaDB:** changing HNSW parameters crashed it.
- **Deliverable:** resolved issues and verified fixes
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/tests/test_phase14.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/quality/completeness.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/scoring/drift.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/db/init_db.py
- **Status:** Complete

### Research

#### 25. ChromaDB Optimization Patterns Research
*Research · ChromaDB Optimization*
- Researched ChromaDB optimization for financial text retrieval:
  - collection management strategies
  - embedding versioning approaches
  - HNSW index tuning techniques
- **Deliverable:** research notes on ChromaDB optimization patterns
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/research
- **Status:** Complete

#### 26. Grafana Integration & Data Quality Engineering Research
*Research · Grafana & Data Quality*
- Researched:
  - Grafana integration patterns for ML pipeline monitoring
  - data profiling methods
  - lineage tracking approaches
- **Deliverable:** research notes on Grafana integration and data quality engineering
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/research
- **Status:** Complete

### Writing

#### 27. Substack Article: "From Transcript to Trade Signal in Under 60 Seconds"
*Writing · Substack Article*
- Explores how latency in financial NLP pipelines translates to business value.
- Walks through the ECIS pipeline's processing chain.
- **Deliverable:** published Substack article
- **Link:** https://mycroftproject.substack.com/p/transcript-to-trade-signal-pipeline-latency
- **Status:** Complete (published)

#### 28. Substack Article: "Data Lineage Isn't Optional"
*Writing · Substack Article*
- Covers building provenance chains in a financial AI system.
- Describes end-to-end lineage tracking from raw transcript to prediction.
- **Deliverable:** published Substack article
- **Link:** https://mycroftproject.substack.com/p/data-lineage-provenance-financial-ai
- **Status:** Complete (published)

### Artifacts

#### 29. Earnings Signal Timeline
*Artifact · Claude Artifact*
- Interactive chart mapping extracted signals against actual stock price movement for any company.
- Reaction windows are highlighted.
- **Deliverable:** Claude Artifact: Earnings Signal Timeline
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/artifacts
- **Status:** Complete

#### 30. Reader Health Monitor
*Artifact · Claude Artifact*
- Simulated Grafana-style dashboard showing extraction latency percentiles, signal throughput, and reader agreement rates.
- **Deliverable:** Claude Artifact: Reader Health Monitor
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/artifacts
- **Status:** Complete

### Video

Both videos follow the same split.
- **Concept, ideas, narration, and direction:** original work.
- **Assembly:** Claude, using the video generation tool created by Humanitarians AI.

#### 31. Video: "ECIS Episode 9: Weekly Project Update"
*Documentation · Video Production*
- Weekly Mycroft ECIS project update covering Week 14 development progress and key technical decisions.
- **Deliverable:** Video: ECIS Episode 9
- **Links:**
  - https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-10-02-ecis-explained
  - https://drive.google.com/drive/folders/1cmuifmONniYXUfM26KO_2GqJ3oSKnvlk
- **Status:** Complete

#### 32. Video: "Context Window Explainer"
*Documentation · Video Production*
- STEM educational video explaining context windows in large language models.
- Covers tokenization, attention mechanisms, and practical implications.
- **Deliverable:** Video: Context Window Explainer
- **Links:**
  - https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-10-02-context-window-explainer
  - https://drive.google.com/drive/folders/1d__3scCkeKfPPCyXvvAaesOk6ePpn7fR
- **Status:** Complete
