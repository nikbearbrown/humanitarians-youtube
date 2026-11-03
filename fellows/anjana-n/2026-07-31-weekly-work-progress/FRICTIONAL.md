# Friction Log: Week 5 (Phase 5)

**Project:** Mycroft — ECIS + Decision Scorecard
**Week:** July 26 – August 1, 2026

---

## 1. Focus of the week

- **Scaling:** ingesting and processing 10–15 new AI-sector tickers, running the full extraction pipeline, and populating ChromaDB.
- **Data integrity:** fixing filing date parsing and re-extracting signals with the corrected dates.
- **Outcome resolution:** a caching layer and batch resolution.
- **Evaluation:** the first multi-ticker Scorecard evaluation.
- **Fine-tuning:** error categorization and the fine-tuning decision.
- **Feedback loops:** calibration watchdog, orchestration learning graph, and vindication aggregation.
- **Dashboard:** multi-ticker updates.
- **Outputs:** the Signal Distribution Dashboard (Claude artifact) and "When to Stop Prompting and Start Fine-Tuning."

## 2. What was tried, and what was expected

- **Scaling.** Expectation: code built in Weeks 3–4 would run on new tickers with only the inputs changing.
- **Dates.** Expectation: EDGAR filing dates would reliably match earnings call dates.
- **Normalizer.** Expectation: the Week 2 normalizer would handle new tickers' transcripts.
- **Caching.** Expectation: the cache would save redundant yfinance fetches without side effects.
- **Thresholds.** Expectation: thresholds for the feedback loops could be set from observed distributions rather than defaults.
- **Evaluation.** Open question going in: whether the LLM reader's Brier skill score would clear zero against the keyword baseline.

## 3. Points of resistance, and next steps taken

### EDGAR filing date parsing (load-bearing)
- **What happened:** some 8-K filings used the filing acceptance date instead of the earnings call date.
- **Why it mattered:** a 1–3 business day gap is small enough to look harmless. It is large enough to move the price fetch window across an earnings reaction, so a "correct" grade could flip to "incorrect."
- **Next step:**
  - Filename dates cross-referenced against filing metadata.
  - Period-of-report date set as the canonical `transcript_date`.
  - Affected signals re-extracted.
- **Lesson:** this is the same class of silent data integrity error the project is designed to catch in others, and it nearly contaminated the project's own evaluation.

### New ticker transcript formats
- **What surfaced:** formats the normalizer missed:
  - non-standard section headers
  - guidance embedded in exhibit attachments
  - speaker label formats the regex missed
- **Next step:** normalization logic updated for each case, then re-run.
- **Lesson:** the Week 2 friction recurring at scale. Normalization is never finished when sources are heterogeneous.

### Caching layer stale outcomes
- **What happened:** the cache key left out `transcript_date`. Re-extracted signals with corrected dates were served outcomes resolved against the old, wrong dates.
- **Next step:** `transcript_date` added to the cache key.
- **Lesson:** a cache that doesn't know its data changed serves wrong answers with the confidence of right ones.

### Interpreting the first Scorecard numbers
- **What resisted:** at N≈50, Murphy decomposition alone does not say whether poor performance is terminal (lack of skill) or treatable (calibration error).
- **Next step:** errors categorized by root cause before any conclusion about the model was drawn.

### Setting feedback-loop thresholds
- **The trade-off:**
  - **Watchdog:** too sensitive, and it recalibrates on noise; too conservative, and genuine drift goes undetected.
  - **Learning graph and vindication:** the false-negative threshold and the adjustment rates shape how fast the system rebalances.
- **Next step:** all values set from observed distributions, not defaults.

## 4. AI and other contributions: accepted, changed, rejected

### Gru (SDD session)
- Documented the week's architectural decisions.

### Eddy
- Reviewed "When to Stop Prompting and Start Fine-Tuning" before publication.

### Claude
- Built the Signal Distribution Dashboard.
- It visualizes signals by ticker, reader, confidence level, and guidance direction.

## 5. Understood now, and still unresolved

### Understood
- **Silent errors:** the most dangerous bugs this week produced plausible outputs from wrong data: dates, formats, and the cache. The project's core principle applies to its own infrastructure.
- **Fine-tuning scope:** most errors are not a fundamental model limitation. They fall into two groups:
  - **Retrieval gaps:** implicit guidance without temporal context. A retrieval problem, not a model problem.
  - **Maintained-vs-none boundary:** a prompt boundary problem, addressable through targeted fine-tuning.
- **Decision:** targeted fine-tuning on the maintained/none boundary, not broad retraining. Resolves the question open since Week 2.

### Unresolved
- **vLLM vs. Ollama:** still pending, carried from Week 3.
- **Targeted fine-tuning:** whether it actually closes the maintained/none gap.
- **Thresholds:** whether the empirically derived values hold as more outcomes resolve.
