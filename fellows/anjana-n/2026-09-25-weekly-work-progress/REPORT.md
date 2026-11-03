# Weekly Report: Week 13 (Phase 13)

**Project:** Mycroft — ECIS (Earnings Call Intelligence System) + Decision Scorecard
**Week:** September 20 – September 26, 2026
**Total hours:** 38.75

---

## Summary

The pipeline expanded along three new axes this week.

- **Linguistic analytics** (how executives speak, not just what they say):
  - readability (Flesch-Kincaid, Gunning Fog)
  - hedging index
  - forward-looking statement density
  - tone shift across quarters
- **Market impact analytics** (how the market actually responded to each signal):
  - reaction magnitude
  - pre-signal drift
  - reaction timing
  - abnormal volume
  - impact-weighted Scorecard
- **Database migration:** SQLite to PostgreSQL, adding:
  - TimescaleDB hypertables
  - composite indexes
  - Alembic versioning
  - materialized views

Key finding: pre-signal drift showed that some signals were already priced in before the call.

Dashboard additions:
- linguistic sparklines
- market impact scatter
- drift histogram with a volume-spike overlay
- database health panel

Outputs: two Claude artifacts, two Substack articles, and two videos.

---

## Work Completed

### Signal-Level Analytics

#### 1. Readability Scoring (Flesch-Kincaid, Gunning Fog) Per Transcript
*Development · Signal-Level Analytics*
- Added Flesch-Kincaid and Gunning Fog readability scores per transcript.
- Gives a quantitative measure of linguistic complexity, which may correlate with how hard a signal is to extract.
- **Deliverable:** per-transcript readability scoring (Flesch-Kincaid + Gunning Fog)
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/extraction/linguistics.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/main.py
- **Status:** Complete

#### 2. Hedging Index: Hedging Phrases vs. Definitive Statements Ratio
*Development · Signal-Level Analytics*
- Built a hedging index: the ratio of hedging phrases to definitive statements in each section.
- Quantifies how certain management sounds on the call.
- **Deliverable:** hedging index per section
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/extraction/linguistics.py
- **Status:** Complete

#### 3. Forward-Looking Statement Density Per Transcript
*Development · Signal-Level Analytics*
- Scores each transcript on how much future-oriented language it contains relative to backward-looking reporting.
- **Deliverable:** forward-looking statement density scoring
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/extraction/linguistics.py
- **Status:** Complete

#### 4. Tone Shift Detection: FinBERT Sentiment Comparison Across Consecutive Quarters
*Development · Signal-Level Analytics*
- Compares FinBERT sentiment scores for the same company across consecutive quarters.
- Flags significant sentiment changes between reporting periods.
- **Deliverable:** tone shift detection across consecutive quarters
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/extraction/linguistics.py
- **Status:** Complete

#### 5. Linguistic Feature Vector Integration into Prediction Model
*Development · Signal-Level Analytics*
- Added readability, hedging index, forward-looking density, and tone shift as features in the prediction model.
- **Deliverable:** linguistic feature vector integrated into prediction model
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/prediction/features.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/extraction/linguistics.py
- **Status:** Complete

### Market Impact Analytics

#### 6. Reaction Magnitude Scoring: Absolute Excess Return
*Development · Market Impact Analytics*
- Scores how strongly the market responded to each earnings call signal, using absolute excess return.
- **Deliverable:** reaction magnitude scoring (absolute excess return)
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/prediction/features.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/extraction/linguistics.py
- **Status:** Complete

#### 7. Pre-Signal Drift Analysis: 5- and 10-Day Pre-Call Excess Return
*Development · Market Impact Analytics*
- Measures excess returns over the 5 and 10 days before each earnings call.
- Detects whether the market was already positioning ahead of the call.
- **Deliverable:** pre-signal drift analysis (5/10-day windows)
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/scoring/outcome_resolver.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/scoring/price_cache.py
- **Status:** Complete

#### 8. Reaction Timing Analysis: Same-Day Through 30+ Day Windows
*Development · Market Impact Analytics*
- Measures how quickly the market incorporates earnings call information.
- Uses four windows: same-day, 1-day, 5-day, and 30+ day.
- **Deliverable:** reaction timing analysis (multi-window)
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/scoring/outcome_resolver.py
- **Status:** Complete

#### 9. Abnormal Volume Detection vs. 30-Day Trailing Average
*Development · Market Impact Analytics*
- Compares trading volume around earnings call dates against the 30-day trailing average to flag abnormal volume.
- **Deliverable:** abnormal volume detection
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/scoring/price_cache.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/scoring/outcome_resolver.py
- **Status:** Complete

#### 10. Impact-Weighted Scorecard Integration
*Development · Market Impact Analytics*
- Brought reaction magnitude and the other market impact metrics into the Scorecard, so accuracy can be weighted by market impact.
- **Deliverable:** impact-weighted Scorecard integration
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/scoring/scorer.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/dashboard/views.py
- **Status:** Complete

### Database Migration

#### 11. PostgreSQL Setup and Schema Migration from SQLite
*Development · Database Migration*
- Set up PostgreSQL and migrated the full schema from SQLite:
  - signals
  - outcomes
  - agent decisions
  - predictions
  - checkpoint store
- **Deliverable:** PostgreSQL database with migrated schema
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/db/postgres.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/db/init_db.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/db/pool.py
- **Status:** Complete

#### 12. Indexing Strategy: Composite Indexes
*Development · Database Migration*
- Designed and implemented composite indexes, tuned for the most frequent query patterns on the signal and outcome tables.
- **Deliverable:** composite indexing strategy implemented
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/db/init_db.py
- **Status:** Complete

#### 13. TimescaleDB Hypertable for Time-Series Market Data
*Development · Database Migration*
- Configured a TimescaleDB hypertable for time-series market data.
- Enables efficient time-range queries and automated data retention policies.
- **Deliverable:** TimescaleDB hypertable for market data
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/scoring/price_cache.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/db/init_db.py
- **Status:** Complete

#### 14. Alembic Setup for Schema Migration Versioning
*Development · Database Migration*
- Set up Alembic for versioned schema migrations, so database state changes are reproducible across environments.
- **Deliverable:** Alembic migration framework configured
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/alembic/
- **Status:** Complete

#### 15. Materialized Views for Rolling Scorecard Metrics
*Development · Database Migration*
- Created materialized views that pre-compute rolling Scorecard metrics, to speed up the dashboard.
- **Deliverable:** materialized views for rolling Scorecard metrics
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/db/views.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/main.py
- **Status:** Complete

#### 16. Database Migration Testing and Validation
*Development · Database Migration*
- End-to-end testing of the migration against the SQLite baseline:
  - migrated data
  - query correctness
  - performance benchmarks
- **Deliverable:** migration testing and validation complete
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/tests/test_phase11-13.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/db/init_db.py
- **Status:** Complete

### Dashboard

#### 17. Linguistic Profile Sparklines: Readability, Hedging, Tone Shift Per Company
*Development · Dashboard*
- Added per-company sparklines showing readability, hedging index, and tone shift trends over time.
- **Deliverable:** linguistic profile sparklines in dashboard
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/dashboard/views.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/dashboard/app.py
- **Status:** Complete

#### 18. Market Impact Scatter: Confidence vs. Reaction Magnitude
*Development · Dashboard*
- Added a scatter plot of signal confidence against market reaction magnitude.
- **Deliverable:** market impact scatter view in dashboard
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/dashboard/views.py
- **Status:** Complete

#### 19. Pre-Signal Drift Histogram and Volume Spike Overlay
*Development · Dashboard*
- Added a histogram of the pre-signal drift distribution, with abnormal volume spikes overlaid.
- **Deliverable:** pre-signal drift + volume spike view in dashboard
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/dashboard/views.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/scoring/outcome_resolver.py
- **Status:** Complete

#### 20. Database Health Panel: Query Latency, Table Sizes, Index Hit Rates
*Development · Dashboard*
- Added a post-migration panel monitoring query latency, table sizes, and index hit rates.
- **Deliverable:** database health panel in dashboard
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/db/query_monitor.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/dashboard/views.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/grafana/dashboards/extraction_latency.json
- **Status:** Complete

### Debugging

#### 21. Debugging and Issue Resolution
*Development · Debugging*
- Debugging across the analytics features, the database migration, and the dashboard integration. Main issues:
  - hedging and sentiment double-counting the same spans
  - TimescaleDB hypertable creation order
  - the KS test on short transcripts
  - materialized view refresh timing
- **Deliverable:** issues identified and resolved
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/tests/test_phase11-13.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/extraction/linguistics.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/scoring/outcome_resolver.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/db/postgres.py
- **Status:** Complete

### Research

#### 22. Analytics Methods Research
*Research · Signal-Level Analytics*
- Researched:
  - readability metrics methodology
  - hedging detection approaches
  - statistical testing for tone shift
  - market microstructure literature on post-earnings drift and abnormal volume
- **Deliverable:** analytics methods research
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/research
- **Status:** Complete

#### 23. Database Architecture Research
*Research · Database Migration*
- Evaluated:
  - PostgreSQL vs. MySQL
  - TimescaleDB vs. InfluxDB for time-series workloads
  - connection pooling strategies
  - materialized view refresh patterns
- **Deliverable:** database architecture research
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/research
- **Status:** Complete

### Artifacts

#### 24. Schema Migration Diff Viewer
*Artifact · Claude Artifact*
- Interactive side-by-side comparison of the SQLite and PostgreSQL schemas.
- Shows table structures, index definitions, and the migration change log, with differences highlighted.
- **Deliverable:** Claude Artifact: Schema Migration Diff Viewer
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/artifacts
- **Status:** Complete

#### 25. Materialized View Performance Dashboard
*Artifact · Claude Artifact*
- Interactive dashboard of materialized view refresh times, before/after query latency, and cache hit rates.
- **Deliverable:** Claude Artifact: Materialized View Performance Dashboard
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/artifacts
- **Status:** Complete

### Writing

#### 26. Substack Article: "Connection Pooling Matters: The Infrastructure Problem No Model Upgrade Can Fix"
*Writing · Substack Article*
- Explains why connection pooling is a critical infrastructure decision for ML systems with concurrent read/write workloads.
- Draws on the earlier SQLite locking issues and the PostgreSQL migration.
- **Deliverable:** published Substack article
- **Link:** https://mycroftproject.substack.com/p/connection-pooling-ml-pipeline-postgresql
- **Status:** Complete (published)

#### 27. Substack Article: "Why Prompts Can Create Invisible Errors"
*Writing · Substack Article*
- Examines how prompt engineering can introduce silent errors.
- These are outputs that look correct but contain structural mistakes that surface-level validation misses.
- **Deliverable:** published Substack article
- **Link:** https://mycroftproject.substack.com/p/invisible-prompt-errors-financial-nlp
- **Status:** Complete (published)

### Video

Both videos follow the same split.
- **Concept, ideas, narration, and direction:** original work.
- **Assembly:** Claude, using the video generation tool created by Humanitarians AI.

#### 28. Video: "ECIS Episode 8"
*Documentation · Video Production*
- Weekly Mycroft project update covering:
  - signal-level analytics (readability, hedging, tone shift)
  - market impact analytics (reaction magnitude, pre-signal drift, abnormal volume)
  - the PostgreSQL + TimescaleDB migration
- **Deliverable:** Video: ECIS EP8
- **Links:**
  - https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-09-25-ecis-explained
  - https://drive.google.com/drive/folders/1eZm09UfVd6K983PznG7eGJXnrszWY_0E
- **Status:** Complete

#### 29. Video: "Vector DB Explainer"
*Documentation · Video Production*
- STEM explainer on how vector databases work. Covers:
  - embedding storage and indexing
  - approximate nearest neighbor search
  - how vector databases enable semantic retrieval in NLP pipelines
- **Deliverable:** Video: Vector DB Explainer
- **Links:**
  - https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-09-25-vector-db-explainer
  - https://drive.google.com/drive/folders/1wbNyPe1w2Y6TaORFW0H3u6A9fK6v8wQD
- **Status:** Complete
