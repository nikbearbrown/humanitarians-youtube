# PEDAGOGY — Rate Limits, Fixed. (claude-hai · Vendor Intelligence weekly update, ~2.5–3min)

**Genre:** weekly project update / changelog (neutral framing, per creator's prior
choice). Six rate-limiting changes after a collector run stopped after 2 of 50.

**Light throughline (verdict only):** pace ahead of the limit, read the real wait,
degrade gracefully (skip one, don't abort), and log the truth.

**Audience (HAI):** followers of the Fellows' build who want to see a real
reliability bug diagnosed and fixed.

## Act structure
- B00 ASK (composer) — the run died after 2 of 50; three faults ✓
- B01 THE FAILURE — the three compounding faults (parser 180s, 2 tries, abort-all) ✓
- B02 THE PACER (change #1) — token-budget pacer: wait before overflow, not after a 429 ✓
- B03 THE DETAILS (changes #2–#5) — parser fix (2.79s→3s), retries 2→6, throttle vs
  wall (>300s), skip-one-not-all ✓
- B04 VERIFIED — 10 calls / ~18k tokens / 8k budget → waited 57s,58s → 10/10, 0 aborts,
  all correct ✓
- B05 verdict (one-pager, includes the honest message fix, change #6) · B06 handoff
  (audit one retry) · B07 outro ✓
- Body B01–B04 = 4K PIL cards; Claude UI only at B00/B05/B06/B07 (ILLUSTRATE LAW).

## Correctness (DOUBLE-CHECK LAW — verbatim from the change log)
- Run stopped after 2 of 50 companies (this morning); three compounding faults.
- Token-budget pacer: ~51 lines; `_await_token_budget()` + `_record_usage()`; rolling
  60-second window; `TOKENS_PER_MINUTE` from `GROQ_TOKENS_PER_MINUTE`.
- Retry-after parser: old regex `try again in (\d+)m([\d.]+)s` required minutes; Groq
  sends `try again in 2.79s`; never matched → 180s fallback; 3s waits became 3min.
  New pattern makes minutes optional.
- `max_attempts` 2 → 6.
- Throttle vs exhaustion: only a wait > 300s returns `hit_rate_limit=True` and stops.
- Exhausting retries skips one headline and continues (was: abort whole run).
- Message `[RATE LIMIT] Hit Groq daily limit` → `[QUOTA] Groq quota exhausted`, only
  when true, with a completed-companies count.
- Verified: 10 calls, ~18,000 tokens vs 8,000/min → paced (57s, 58s) → 10/10, 0 abort
  signals, all classifications correct (previously aborted). No invented figures.

## PROOF note (genre caveat)
A changelog, not a framework-teaching explainer — PROOF's teaching rubric will score
modestly by design. The production gate should PASS: every claim carries a legible
on-screen number, all from the creator's own log.

## Narration review (GATE P)
Listen for: are the numbers exact and legible? Does B02 land "pace, don't react"?
Is B04 clearly the same run that failed, now passing?

VERDICT: PASS 