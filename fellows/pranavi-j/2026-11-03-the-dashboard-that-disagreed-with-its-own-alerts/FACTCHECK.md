# FACTCHECK — The Dashboard That Disagreed With Its Own Alerts

Status: **RESOLVED — fellow reviewed 2026-11-03. Cleared for Gate P (narration lock).**

| # | Beat | Claim (as spoken/shown) | Verdict | Source / derivation | Fix if needed |
|---|---|---|---|---|---|
| 1 | B02/B03 | Every item gets a raw `urgency_score` (0–10) and an `impact_level` label; the alert email reads `impact_level`, the dashboard's `get_stats()` ignores it and re-derives its own tiers from `urgency_score` | PASS — verbatim read of `get_stats()`'s own in-code comment ("bucketed from impact_level, the column email generation and every other consumer treats as authoritative... not re-derived from urgency_score, which disagrees with impact_level on a real fraction of rows") and the current SQL itself in `Regulatory_QA/backend/app/crud.py` | `Regulatory_QA/backend/app/crud.py` (`FeedCRUD.get_stats()`) | — |
| 2 | B03 | Pre-fix cutoffs: `urgency_score >= 8` Critical, `BETWEEN 6 AND 7` High, `BETWEEN 4 AND 5` Medium, `<= 3` Low | PASS — verbatim from `D1-VERIFICATION.md`'s "The fix" diff (`-` lines); confirmed this session by reconstructing the exact pre-fix SQL via string substitution against the real, current post-fix SQL in `crud.py`, with a hard check that the post-fix block occurs exactly once before trusting the reconstruction (`verification/verify_dashboard_stats.py`) | `scripts/regulatory-intel/D1-VERIFICATION.md`; `Regulatory_QA/backend/app/crud.py` | — |
| 3 | B04 | The fix: 4 `FILTER` lines now read `impact_level = 'Critical'/'High'/'Medium'/'Low'` instead of the `urgency_score` cutoffs; same windowing/response shape; `Stats.jsx` needs no change | PASS — exact diff matches `D1-VERIFICATION.md`'s "The fix" section and the real, current SQL in `crud.py` on disk, confirmed by reading the live file directly (not from the markdown alone); `Stats.jsx` reads `urgency.critical`/`urgency.high` off the unchanged `urgency_distribution` key, confirmed via `RUN_LOG.md`'s 2026-11-03 entry ("Checked Stats.jsx, the only frontend consumer... key names had to stay exactly the same") | `Regulatory_QA/backend/app/crud.py`; `D1-VERIFICATION.md`; `RUN_LOG.md` 2026-11-03 | — |
| 4 | B05 | Live before/after table: old (`urgency_score` cutoffs) Critical=32, High=139, Medium=240, Low=0; new (`impact_level` column) Critical=33, High=98, Medium=280, Low=0; 62/411 rows (15%) land in a different tier; old method overcounts High by 41 items (30% inflated) | PASS — matches `D1-VERIFICATION.md`'s own table and `RUN_LOG.md`'s 2026-11-03 entry exactly, both reporting results from the real, live `mycroft_intelligence` DB (411 rows). Independently reproduced this session via `verification/verify_dashboard_stats.py`: the real, current SQL (post-fix) and a reconstruction of the real pre-fix SQL (built by undoing the exact documented diff, confirmed to match the real file's post-fix block exactly once) were both run, unmodified, against a synthetic 411-row table engineered to reproduce this exact aggregate distribution — all 13 assertions pass, captured in `verification/verify_dashboard_stats_output.txt`. This session could not reach the live Postgres DB directly (no working `DATABASE_URL` in this shell's environment — the backend's own `pydantic_settings` `Settings` class requires it from a `.env` file this session does not have loaded; same category of settings/env friction this fellow's 2026-10-20 report documented fighting with its own FastAPI harness), so this is a reconstruction run against a dataset matching the documented live counts, not a fresh live query — stated plainly in the harness's own docstring and in `FRICTIONAL.md`, not claimed as a second live measurement | `scripts/regulatory-intel/D1-VERIFICATION.md`; `RUN_LOG.md` 2026-11-03; `verification/verify_dashboard_stats.py`, `verification/verify_dashboard_stats_output.txt` | Narration/table must not claim this session re-queried the live DB a second time — it reproduces the real, documented counts via the real extracted SQL run against an engineered dataset |
| 5 | B06 | Honest limit 1: only `get_stats()`'s urgency/severity query changed — `total_feeds`, `source_distribution`, `recent_activity`, the `/api/feeds/stats` route, `Stats.jsx`, and `impact_level`'s own computation (how it's set or corrected) are all untouched | PASS — verbatim from `D1-VERIFICATION.md`'s "What's NOT touched" section; corroborated by reading `get_stats()`'s current body directly — only the one SQL block differs from the reconstructed pre-fix version | `D1-VERIFICATION.md`; `Regulatory_QA/backend/app/crud.py` | — |
| 6 | B06 | Honest limit 2: verified unwindowed, against the full real 411-row table; the endpoint's actual 7-day/30-day rolling windows were NOT re-verified against live production data, because the fixture's `created_at` range (14–24 Jul 2026) is months stale and returns all-zero under that window on both old and new queries — a property of the stale fixture, not the fix | PASS — verbatim from `D1-VERIFICATION.md`'s "Verification" section and `RUN_LOG.md`'s 2026-11-03 "Open issues" line ("Not verified against a live, actively-populated deployment of this dashboard... the 7-day/30-day windowed queries themselves are unverified against real recent data, only the underlying bucketing logic"). This session's own harness (`verify_dashboard_stats.py`) also runs both queries unwindowed, for the same documented reason — stated explicitly in its docstring, not silently assumed | `D1-VERIFICATION.md`; `RUN_LOG.md` 2026-11-03 | Must stay phrased as an open, unresolved caveat, not folded into a claim that the fix is fully verified end-to-end |
| 7 | B06 | `impact_level` only takes 3 of its 4 possible values in the current data (`Low` never produced by the fixture set) — not a defect, just means the `low` bucket reads 0 under both old and new query | PASS — verbatim from `RUN_LOG.md`'s 2026-11-03 entry | `RUN_LOG.md` 2026-11-03 | — |
| 8 | B07 | Takeaway: "a dashboard that re-derives its own answer from a different number than everyone else isn't measuring the same thing" | PASS — editorial framing of the mechanism established in B02/B03, not a new factual claim requiring separate citation | — | — |

## Dramatization check

No beat claims an operator was ever observed acting on a wrong dashboard number in a real incident
— B05's numbers are the real, live-DB-derived counts `D1-VERIFICATION.md` and `RUN_LOG.md` report,
independently reproduced this session via a harness run against the real extracted SQL (not a
claim that this session re-queried the live DB a second time — see FACTCHECK #4). The unwindowed-
only verification caveat (B06) is stated at full weight, not smoothed into a claim that production
behavior was fully confirmed. No invented statistics beyond what `D1-VERIFICATION.md` and
`RUN_LOG.md` state.

## Continuity with this fellow's prior reports

This is the direct follow-up to last week's report ("The Correction That Never Reached The
Email," C3) — that video's B06 flagged this exact `get_stats()` defect as "found, not fixed this
week." This week's B01/premise names that continuity explicitly, and the numbers have moved
slightly (57/411 as spotted during the C3 investigation -> 62/411 confirmed live this week,
per `RUN_LOG.md`'s 2026-11-03 entry, "grown slightly... consistent with a live-queried table") —
this video uses the current, final 62/411 number throughout, not the earlier C3-era estimate.

## Resolved 2026-11-03

1. Confirmed every quoted SQL line and diff against the real, current `crud.py` on disk and
   `D1-VERIFICATION.md`, not from memory or paraphrase.
2. Confirmed B05's harness table by actually running `verification/verify_dashboard_stats.py` this
   session and cross-checking its output against `D1-VERIFICATION.md`'s and `RUN_LOG.md`'s own
   independently reported tables — all three agree exactly.
3. Confirmed B06's honest limits (both the "what's not touched" list and the unwindowed-only
   verification caveat) are carried forward verbatim from `D1-VERIFICATION.md`/`RUN_LOG.md`, not
   re-measured, escalated, or softened this session.
4. Confirmed `/Users/pranavijs/mycroft` was not modified by this session (`git status --short`
   before and after this project's research/verification work shows only the same pre-existing,
   unrelated changes both times — see `FRICTIONAL.md`).

Gate P (narration review) can proceed.
