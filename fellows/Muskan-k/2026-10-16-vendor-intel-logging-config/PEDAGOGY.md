# PEDAGOGY — Loud by Default. (claude-hai · Vendor Intelligence weekly update, ~2.5min)

**Genre:** weekly project update / changelog (neutral framing). Two tickets:
structured logging, and a validated Settings class.

**Light throughline (verdict):** make problems visible — a warning you can't filter
is one you won't see; config that fails silently fails at the worst time. Fail loud.

**Audience (HAI):** followers of the Fellows' build; anyone shipping pipelines where
observability and config hygiene matter.

## Act structure
- B00 ASK (composer) — the incident: observability broke because a warning was a print ✓
- B01 TICKET 1 PROBLEM — 225 prints, 0 logging; a print is invisible; it hid 3 bugs ✓
- B02 TICKET 1 FIX — 76 prints → logging (9 files); kept 83 CLI report-prints; levels by
  what the code does next; auto-pass fixed by hand; LOG_LEVEL=WARNING drops noise ✓
- B03 TICKET 2 PROBLEM — 36 scattered os.getenv; silent fallback; fails deep & mislocated ✓
- B04 TICKET 2 FIX — one settings.py; blank = absent; require() reports all missing at
  once; grouped by concern; absorbed/deleted models.py ✓
- B05 verdict · B06 handoff (find the silent print / unvalidated getenv) · B07 outro ✓
- Body B01–B04 = 4K PIL cards; Claude UI only at B00/B05/B06/B07 (ILLUSTRATE LAW).

## Correctness (DOUBLE-CHECK LAW — verbatim from the change log)
- 225 print() calls, zero logging; a print is invisible to filters/aggregators/alerts.
- The incident: Langfuse handler silently broken because its warning was a print; the
  same blind spot hid the phantom traces and the fail-open entity check.
- 76 prints → logging across 9 files (news_collector 16, supervisor 18, github 10, arxiv
  9, edgar 8, api/main 7, langfuse_helper 4, db 2, llm 2). 83 CLI prints kept (verify,
  setup_check, run_all, audit_entities, seed, eval_runner) — the report is the product.
- Levels by what the code does next: WARNING (degraded, continuing), ERROR (work lost),
  INFO (progress). Automated pass was wrong (37 err / 29 info, "log.error('WARNING:…')")
  — corrected by hand. LOG_LEVEL=WARNING drops progress; third-party loggers suppressed.
- 36 scattered os.getenv with inline defaults → silent wrong config. New
  collector/settings.py (149 lines): blank = absent; require() reports every missing key
  at once; grouped by concern (postgres/groq/neo4j/edgar/github/langfuse); has() for
  optional deps. Absorbed and deleted collector/models.py (committed 72a97a5 — reverses
  last week's consolidation; intentional).
- Verified: 12 touched modules import cleanly under both import styles; 17 unit tests pass.

## Caveats kept off the cards (for honesty, mentioned here)
- Dual-path imports: collector/db.py is imported both as `db` and `collector.db`; each
  module now carries a try/except for both paths — ugly; the proper fix (make collector a
  real package) was deliberately deferred.
- A stale BEDROCK_MODEL (amazon.nova-micro-v1:0, missing the us. profile prefix) was
  found; nothing read it. llm.py left hardcoded so this refactor changes no behaviour —
  flagged for someone to align or delete.

## Narration review (GATE P)
Listen for: is the incident (silent print broke observability) the hook? Are the counts
(225 / 76 / 83 / 36) exact and legible? Is the models.py-deletion flagged honestly?

VERDICT: PASS 