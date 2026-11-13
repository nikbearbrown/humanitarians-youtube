# Friction Log: Week 13 (Phase 13)

**Project:** Mycroft — ECIS + Decision Scorecard
**Week:** September 20 – September 26, 2026

---

## 1. Focus of the week

- **Linguistic analytics:**
  - readability scores
  - hedging index
  - forward-looking density
  - tone shift (KS test)
  - integration into the prediction model
- **Market impact analytics:**
  - reaction magnitude
  - pre-signal drift
  - reaction timing
  - abnormal volume
  - impact-weighted Scorecard
- **Database migration:**
  - PostgreSQL
  - composite indexes
  - TimescaleDB hypertables
  - Alembic
  - materialized views
  - migration testing
- **Dashboard:**
  - linguistic sparklines
  - market impact scatter
  - drift histogram with volume overlay
  - database health panel
- **Research:** analytics methods and database architecture.
- **Outputs:**
  - two Claude artifacts
  - two Substack articles
  - two videos

## 2. What was tried, and what was expected

- **NLP layers:** expected each one (hedging, sentiment, readability) to run independently without interfering.
- **Signal value:** expected extracted signals to carry new information to the market at the time of the call.
- **Migration:** expected it to be largely a well-documented path: PostgreSQL, TimescaleDB, Alembic.
- **KS test:** expected the Kolmogorov-Smirnov test to work for comparing sentiment distributions on every transcript.
- **Materialized views:** expected them to speed up the dashboard immediately.

## 3. Points of resistance, and next steps taken

### Hedging and sentiment double-counting (load-bearing)
- **What happened:** phrases like "we remain cautiously optimistic" were counted twice. "Cautiously" triggered hedging detection and "optimistic" triggered positive sentiment.
  - Both scores looked reasonable on their own.
  - The combined signal was inflated because the same text was being counted through two lenses.
- **Next step:** reordered the pipeline so hedging is detected first and its spans are masked before sentiment scoring.
- **Lesson:** the interaction was invisible while each NLP layer ran on its own. The tools couldn't see it; it took understanding what both layers were doing.

### Some signals were already priced in
- **What happened:** pre-signal drift showed that 5-day pre-call excess returns sometimes moved in the same direction as the extracted signal. The market had the information first.
- **What it means:** this is not a pipeline failure. It is information about each signal's novelty, which the system had no way to surface before this week.
- **Related finding:** signals that correlate with immediate price movement aren't necessarily the best. Delayed reactions (5-day window) sometimes correlated more strongly with high-confidence signals.

### Defining "excess" and "normal"
- **What resisted:**
  - Reaction magnitude needed a proper definition of excess return: subtract the sector ETF return, not just measure the raw price change. This builds on the Week 12 sector normalization.
  - "Normal" volume was also hard to define. A 30-day trailing average is distorted by earnings-adjacent volume spikes from other companies in the sector.
- **Next step:** sector-relative excess return, with the volume baseline sensitivity recorded.

### TimescaleDB hypertable creation order
- **What happened:** the hypertable was created after inserting data, which fails.
- **Next step:** dropped and recreated the table with hypertable conversion first, then re-inserted the data. About 30 minutes were lost.
- **Lesson:** a documentation-order problem. The migration script had been written to preserve data first.

### Alembic autogenerate missed ChromaDB
- **What happened:** Alembic only tracks SQLAlchemy models, so ChromaDB collection changes aren't versioned through it.
- **Next step:** a separate, unplanned versioning approach for ChromaDB collections.
- **Lesson:** an architectural gap. There are two persistence layers with different versioning mechanisms and no single source of truth for schema state. It's a minor issue now, but at 100 tickers it would be a provenance failure.

### KS test on short transcripts
- **What happened:** some calls have very short Q&A sections (3–4 exchanges), too few data points for a meaningful KS test.
- **Next step:** added a minimum sample size gate, with a fallback to a simple mean comparison for short calls.
- **Still open:** how many exchanges is "enough" is a judgment call with no clean answer.

### Materialized view refresh timing
- **What happened:** the first implementation refreshed views on every dashboard load, which defeated the purpose of materialization.
- **Next step:** switched to a scheduled refresh, with a staleness indicator in the dashboard that makes the refresh lag visible rather than hidden.

### Preserving provenance through the migration
- **What resisted:** live data had to be migrated without breaking signal provenance chains or the lineage JSON.
- **Next step:**
  - Composite indexes chosen by profiling the dashboard's actual query patterns.
  - Migration validated end to end against the SQLite baseline.

## 4. AI and other contributions: accepted, changed, rejected

### Claude + Humanitarians AI video generation tool
- **Original work:** the concept, ideas, narration, and direction for both videos.
- **Claude's part:** assembled the videos using the video generation tool created by Humanitarians AI.

### Claude (artifacts)
- **Schema Migration Diff Viewer:** SQLite vs. PostgreSQL schemas side by side, with index definitions and a highlighted migration change log.
- **Materialized View Performance Dashboard:** view refresh times, before/after query latency, and cache hit rates.

### Gru (SDD session)
- SDD work on the updated architecture.

### Eddy
- Reviewed both Week 13 articles before publication.

## 5. Understood now, and still unresolved

### Understood
- **Closing feedback loops changes what the system can see:** market impact data revealed whether signals were novel or already priced in.
- **NLP layers interact:** span-level masking and ordering matter when several detectors read the same text.
- **Statistical tests have preconditions:** applying a test below its assumptions produces a number that looks like a result but isn't.
- **Versioning:** a hybrid storage system needs a versioning story for every persistence layer, not just the relational one.
- **Making lag visible:** the staleness indicator is more honest than hiding refresh delay.

### Unresolved
- **ChromaDB versioning gap:** separate versioning is needed so there is a single source of truth.
- **KS test sample-size threshold:** the minimum number of exchanges is undetermined.
- **Multi-sector tickers:** the sector ETF mapping is carried from Week 12.
- **Routing complexity decision:** carried from Week 11.
- **Signal decay horizon weighting:** carried from Week 10.
