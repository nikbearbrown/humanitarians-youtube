# Friction Log: Week 14 (Phase 14)

**Project:** Mycroft — ECIS + Decision Scorecard
**Week:** September 27 – October 3, 2026

---

## 1. Focus of the week

- **ChromaDB optimization:**
  - collection strategy
  - embedding versioning
  - HNSW tuning
  - exemplar cleanup
  - retrieval validation
- **Database performance:**
  - connection pooling
  - query monitoring
  - outcome caching in TimescaleDB
- **Data quality and lineage:**
  - profiling
  - end-to-end lineage
  - completeness monitoring
  - schema evolution via Alembic
- **Evaluation framework:**
  - bootstrap confidence intervals
  - paired permutation tests
  - power analysis
- **Grafana:**
  - installation
  - reader health, latency, and throughput dashboards
  - alert rules
  - theme and layout
- **Inference reliability:**
  - concept drift detection (PSI/KL divergence)
  - prediction model decay tracking
- **Outputs:**
  - two Claude artifacts
  - two Substack articles
  - two videos

## 2. What was tried, and what was expected

- **Model comparisons:** the comparisons from earlier weeks (Qwen vs. Llama vs. Mistral) were expected to be reliable at the current sample size.
- **Permutation tests:** 500 permutations were expected to give stable significance results.
- **PSI binning:** default equal-width bins were expected to measure distribution shift fairly on every feature.
- **HNSW parameters:** expected to be adjustable on an existing ChromaDB collection.
- **Drift:** the expectation was that detected drift would point to a clear action.

## 3. Points of resistance, and next steps taken

### Power analysis undercut confidence in prior comparisons (load-bearing)
- **What happened:** at n≈45 calls, power for medium effect sizes is about 0.6. Roughly 40% of real model differences would go undetected.
- **Why it matters:** every earlier model comparison is now bracketed by the knowledge that it may have lacked the power to detect real but moderate differences.
- **Next step:** subtle model comparisons are not trusted until the dataset grows. Fine-grained conclusions wait for more data.

### Permutation test p-value instability
- **What happened:** with 500 permutations, reruns gave different significance conclusions. It took about 40 minutes to identify the instability.
- **Next step:** increased to 5,000+ permutations for stable results.
- **Lesson:** catching this required running the test more than once and comparing the results. That is not default behavior.

### PSI binning on skewed features
- **What happened:** equal-width bins gave misleading PSI on skewed features. The hedging ratio, for example, is right-skewed.
- **Next step:** switched to quantile-based binning and recomputed all baseline distributions.
- **Lesson:** the monitoring tool gave wrong answers because its default configuration assumed symmetric distributions.

### HNSW parameter change crashed ChromaDB
- **What happened:** changing M on an existing collection crashed ChromaDB twice. There is no in-place migration path for HNSW index parameters.
- **Next step:** rebuilt the collection from stored embeddings.
- **Result:** with ef_construction 200→512 and M 16→48, Recall@10 rose from 0.89 to 0.94 on held-out queries.
- **Lesson:** an operational limitation that isn't prominently documented. It connects to the Week 13 ChromaDB versioning gap. ChromaDB's operational tooling doesn't match its retrieval quality.

### Interpreting drift
- **What resisted:** PSI flags distribution shift. It doesn't say why.
  - A shift could be genuine semantic change, such as management adapting its language patterns.
  - It could also be distributional noise, such as seasonal variation or sector rotation.
- **Next step:** drift is interpreted by weighing these competing explanations, since each implies a different response.
  - The monitor flags the shift.
  - Deciding what the shift means is a separate step.

### Deciding what lineage must trace
- **What resisted:** knowing which transformation steps could silently corrupt a signal, and where provenance could break.
- **Next step:** lineage traces every step, from raw transcript to decision log, so any signal can be reconstructed in a post-hoc audit.

## 4. AI and other contributions: accepted, changed, rejected

### Claude + Humanitarians AI video generation tool
- **Original work:** the concept, ideas, narration, and direction for both videos.
- **Claude's part:** assembled the videos using the video generation tool created by Humanitarians AI.

### Claude (artifacts)
- **Earnings Signal Timeline:** extracted signals mapped against stock price movement, with reaction windows highlighted.
- **Reader Health Monitor:** a simulated Grafana-style dashboard with latency percentiles, throughput, and reader agreement rates.

### Gru (SDD session)
- Documented the architecture.

### Eddy
- Reviewed both Week 14 articles before publication.

## 5. Understood now, and still unresolved

### Understood
- **Metrics need uncertainty bounds:** a Scorecard number without a confidence interval overstates what is known.
- **Statistical tests need checking:** too few permutations produce unstable conclusions.
- **Tool defaults:** monitoring tools can mislead when their defaults don't match the data, as with equal-width bins on skewed features.
- **Retrieval tuning:** it improved measurably, but ChromaDB lacks safe in-place migration for index parameters.
- **Drift detection is half the job:** interpreting the cause is the other half.

### Unresolved
- **Sample size:** about 45 calls is not enough for reliable detection of medium effect sizes. The dataset needs to grow.
- **ChromaDB operations:** the HNSW migration gap remains, though embedding versioning is now built.
- **Sector ETF mapping for multi-sector tickers:** carried from Week 12.
- **Routing complexity decision:** carried from Week 11.
- **Signal decay horizon weighting:** carried from Week 10.
