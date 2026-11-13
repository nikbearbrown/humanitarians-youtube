# PEDAGOGY — Hardening. (claude-hai · Vendor Intelligence weekly update, ~2.5min)

**Genre:** weekly project update / changelog (neutral framing). Three reliability
fixes on the vendor-intelligence collectors.

**Light throughline (verdict):** fix it in one place, fail loudly instead of silently,
and never hang.

**Audience (HAI):** followers of the Fellows' build; anyone writing data pipelines
that call external services.

## Act structure
- B00 ASK (composer) — three fixes, all about failing badly ✓
- B01 ONE SOURCE OF TRUTH — model ID was in 3 files; Groq retired it → both collectors
  broke; now one file (collector/models.py), env-overridable ✓
- B02 THE SILENT BUG — 10-K/A: get_filings("10-K") prefix-matches amendments; .latest()
  grabbed one with no Item 1 → extraction silently stored nothing (AMD extraction_ok:false);
  fixed to pick exact 10-K (AMD FAILED→OK; NVDA & SNOW unchanged) ✓
- B03 NO MORE HANGS — timeouts on Postgres / Neo4j / Bedrock; before, only ArXiv had one;
  verified via unroutable IP (~10s) ✓
- B04 verdict · B05 handoff (hunt silent failures + missing timeouts) · B06 outro ✓
- Body B01–B03 = 4K PIL cards; Claude UI only at B00/B04/B05/B06 (ILLUSTRATE LAW).

## Correctness (DOUBLE-CHECK LAW — verbatim from the change log)
- New collector/models.py: GROQ_MODEL + GROQ_REASONING_EFFORT (env-overridable);
  imported by edgar_collector.py, news_collector.py, setup_check.py.
- Specific retired-model string kept off-screen to avoid dating; the breakage is the point.
- 10-K/A: get_filings(form="10-K") is a prefix match → includes 10-K/A amendments;
  amendments have no Item 1 Business; .latest() picked one → silent empty extraction;
  fix = next((f for f in tenk_filings if f.form == "10-K"), None). Verified on live
  EDGAR: AMD FAILED→OK, NVDA and SNOW unchanged.
- Timeouts: db.py connect 10s / statement 30s; agents/tools.py Neo4j connect 10s /
  max_transaction_retry_time 15s; agents/llm.py Bedrock read 30s / connect 10s / bounded
  retries. Previously only the ArXiv HTTP call had a timeout. Verified via unroutable IP
  (~10s to give up). All env-overridable.

## PROOF note (genre caveat)
A changelog, not a framework-first explainer — teaching rubric scores modestly by design.
Production gate should PASS: every claim carries a legible on-screen value, all from the
creator's own work (and two of three are verified: AMD FAILED→OK; ~10s give-up).

## Narration review (GATE P)
Listen for: is B02 (the silent bug) landed as the scariest — "stored as success with
empty data"? Are the timeout values exact and legible? Is the theme one line?

VERDICT: PASS