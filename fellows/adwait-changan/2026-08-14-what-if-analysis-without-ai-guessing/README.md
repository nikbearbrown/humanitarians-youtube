# What-If Analysis Without AI Guessing

**Fellow:** Adwait Changan · **this week** · **Project:** Mycroft Finance Investigator
**Voice:** Kokoro `am_onyx` ("Onyx, in for Humanitarians AI") · **Channel:** @HumanitariansAI
**Builder:** `cli-explainer` · **Register:** Pragmatist · **Aspect:** 16:9 · **14 beats, ~4 min**

Finance teams need scenario analysis, but an agent must not quietly turn illustrative assumptions
into forecasts or recommendations. This week's `scenario.py` binds every scenario to the exact
verified baseline run and its CSV hashes, accepts only explicit `AMOUNT` or `PERCENT_OF_ACTUAL`
assumptions, preserves source and assumption lineage, rejects duplicates / non-finite / negative
results, and does deterministic arithmetic with **no external LLM**. From the verified actual EBITDA
baseline of **$230,000**: +5% revenue → **$275,500**; −$20,000 COGS → **$250,000**; a balanced
operating exercise → **$252,300**. The machine log and human decision pack are stamped
`SIMULATION_NOT_FORECAST` · `Recommendation: NONE` · `Decision: HUMAN_REQUIRED` ·
`PENDING_HUMAN_REVIEW`. The project suite reaches **32 passing tests**.

**Honesty:** deterministic sensitivities, not forecasts/probabilities/recommendations/approvals.

## Files
- `beat_sheet.json` (source of truth) · `FLOW-REVIEW.md` (watch-free flow + Codex prompt)
- `PEDAGOGY.md` · `FACTCHECK.md` · `SOURCES.md` · `BUILD-PROMPT.md` · `BUILD-LOG.md` · `_qc/REPORT.md`, `qc-sheet.png`

**Git note:** `*.mp4`/`*.mp3` gitignored. Rendered master delivered as
`WhatIfAnalysisWithoutAIGuessing_AdwaitChangan_2026-08-14.mp4`.
