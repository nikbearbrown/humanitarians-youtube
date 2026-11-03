**Repository:** [https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis](https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis)

# Mycroft ECIS — Phase 13 — Signal-Level Analytics, Market Impact Analytics, and Database Migration

**Timeline:** September 20, 2026 – September 26, 2026

**Scope:** Linguistic feature engineering, market reaction analytics, impact-weighted scoring, and migration of the persistence layer to PostgreSQL with TimescaleDB.

---

## Linguistic Analytics

## Language Complexity
- Flesch-Kincaid and Gunning Fog indices per transcript
- Quarter-over-quarter deltas per company
- Complexity spikes before guidance changes may indicate caution or obfuscation

## Hedging Index
- **Ratio:** hedging phrases to definitive statements
  - Hedging: "we believe", "approximately", "subject to", "may", "could"
  - Definitive: "we will", "we expect", "guidance is", "we are raising"
- **Computed per section:**
  - Prepared remarks: intentional, IR-reviewed hedging
  - Q&A: hedging that reflects genuine uncertainty
- Stored on each signal record

## Forward-Looking Density
- Each chunk classified as forward- or backward-looking using:
  - Tense markers
  - Temporal references
  - Guidance language patterns
- Reported as the percentage of forward-looking chunks per transcript
- Used as a triangulator weighting factor

## Tone Shift Detection
- **Compares quarter over quarter:**
  - Mean FinBERT sentiment
  - Sentiment variance
  - Positive/negative chunk proportions
- **Significance:** two-sample Kolmogorov–Smirnov test

## Linguistic Feature Vector
- Combines readability, hedging, forward-looking density, and tone-shift magnitude
- Added to the prediction feature set; validated accuracy gains on the held-out temporal split

## Market Impact Analytics

## Reaction Magnitude
- Absolute excess return at each horizon, stored alongside the binary correctness flag
  - Example: a +12% reaction confirms a raise more strongly than a +0.5% reaction

## Pre-Signal Drift
- Excess return over the 5 and 10 trading days before the call
- Same-direction drift implies the move was already priced in, which lowers the signal's exploitable value

## Reaction Timing
- **Post-call windows:** same day, 1–3 days, 1–2 weeks, 30+ days
- Distinguishes immediate pricing from delayed reaction
- Compares reaction speed for raised vs. lowered guidance

## Abnormal Volume
- Daily volume over the 5 days around the call vs. the 30-day trailing average
- A volume ratio above 2.0 flags the guidance as material new information

## Impact-Weighted Scorecard
- Brier score and skill score contributions weighted by reaction magnitude
- Prevents low-impact correct calls from dominating the metrics
- Dashboard toggle between equal-weighted and impact-weighted views

## Database Migration

## PostgreSQL
- Signals, outcomes, and agents databases migrated from SQLite
- **Access layer:** psycopg2 with connection pooling and parameterized queries
- **Integrity verification:** row counts and checksums compared against SQLite exports

## Indexing Strategy
- **Composite indexes:**

| Table | Index |
|---|---|
| Signals | `ticker + transcript_date` |
| Outcomes | `ticker + horizon` |
| Signals | `direction + calibrated_confidence` |
| Signals | `model + source_method` |

- Benchmarked before and after on the most frequent dashboard queries
- Indexing rationale documented

## TimescaleDB
- Hypertable for daily prices, volume, sector ETF prices, and volatility
- Automatic time-based partitioning
- Cached yfinance data migrated into the hypertable
- Outcome resolver reads locally, eliminating redundant API calls

## Alembic
- Baseline revision generated from the current schema
- All future schema changes go through migrations with upgrade and downgrade paths

## Materialized Views
- **Pre-computed aggregations:**
  - Rolling 50-signal Brier score per reader
  - Per-ticker quarterly signal volume
  - Confidence-tier aggregates
  - Correlation matrices
- Refreshed after each extraction batch, reducing dashboard load time

## Dashboard
- **Linguistic profiles:**
  - Per-company sparklines for readability, hedging, and tone shift
  - Sortable by largest quarter-over-quarter change
- **Market impact:**
  - Confidence vs. reaction magnitude scatter plot, coloured by direction
  - Pre-signal drift histogram split by correctness
  - Volume-spike overlay on the signal timeline
- **Database health panel:**
  - Query latency
  - Table sizes
  - Index hit rates

## Validation
- Full re-run on PostgreSQL with all Phase 13 features enabled
- Scorecard metrics matched the SQLite baseline, confirming no integrity loss
- Materialized views produce results identical to on-the-fly computation
- Dashboard load times benchmarked before and after migration
