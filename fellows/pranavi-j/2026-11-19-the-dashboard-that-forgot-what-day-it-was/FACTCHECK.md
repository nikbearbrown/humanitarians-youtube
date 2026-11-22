# FACTCHECK — The Dashboard That Forgot What Day It Was

Status: **RESOLVED — fellow reviewed 2026-11-19. Cleared for Gate P (narration lock).**

| # | Beat | Claim (as spoken/shown) | Verdict | Source / derivation | Fix if needed |
|---|---|---|---|---|---|
| 1 | B02/B03 | The live `mycroft_intelligence` DB's fixture data has `created_at` between 2026-07-14 and 2026-07-24; today is 2026-11-19, four months later | PASS — confirmed this session by querying `MIN(created_at)`/`MAX(created_at)` directly against the live DB (`verification/verify_stale_stats_window_output.txt`): `2026-07-14 16:18:57` to `2026-07-24 13:56:56` | `verification/verify_stale_stats_window.py` output; `F1-VERIFICATION.md` | — |
| 2 | B02/B03 | `get_stats()`'s severity query was filtered to `WHERE created_at >= NOW() - INTERVAL '7 days'`; `total_feeds` is an unwindowed `COUNT(*)`; `list_feeds()` (backing `FeedList.jsx`, including E1's "Select All") applies no date filter at all | PASS — verbatim read of the real `crud.py` on disk (the pre-fix clause is quoted exactly from `F1-VERIFICATION.md`'s diff; the real post-fix `crud.py` has no `WHERE created_at` clause on the severity query, confirmed to match verbatim exactly once by `verify_stale_stats_window.py`) | `Regulatory_QA/backend/app/crud.py`; `F1-VERIFICATION.md` | — |
| 3 | B03 | The real `Stats.jsx` card labels are "Total Feeds", "Critical", "High Priority" | PASS — verbatim read of `Stats.jsx`'s `StatCard` components this session | `Regulatory_QA/frontend/src/components/Stats.jsx` | — |
| 4 | B03/B05 | The feed list's default fetch is `limit: 100` (`App.jsx`'s `feedsAPI.listFeeds({ limit: 100 })`), ordered `ORDER BY created_at DESC, urgency_score DESC` (`crud.py`'s `list_feeds`), no date filter | PASS — verbatim read of both files this session | `Regulatory_QA/frontend/src/App.jsx`; `Regulatory_QA/backend/app/crud.py` | — |
| 5 | B04 | The fix: drop the 7-day `WHERE` clause from the severity-count query only; `source_distribution`'s 30-day window and `recent_activity`'s 14-day window left untouched (the latter is an intentional time series; the former isn't directly contradicted by an adjacent always-visible panel) | PASS — matches `F1-VERIFICATION.md`'s "The fix" section exactly, and confirmed against the real, current `crud.py` on disk: the severity query has no date filter, `source_distribution` still has `WHERE created_at >= NOW() - INTERVAL '30 days'`, `recent_activity` still has `WHERE created_at >= NOW() - INTERVAL '14 days'` | `Regulatory_QA/backend/app/crud.py`; `F1-VERIFICATION.md` | — |
| 6 | B05 | Live verification: the real pre-fix (7-day-windowed) query returns 0/0/0/0 against the live DB; the real, current post-fix (unwindowed) query returns Critical 33 / High 98 / Medium 280 / Low 0; the feed list's real top-100 slice (same live DB, no date filter) contains 24 Critical- and 8 High-tagged rows | PASS — independently reproduced this session via `verification/verify_stale_stats_window.py`, run directly against the real, live `mycroft_intelligence` Postgres DB (not a synthetic reconstruction — this session's DB connection was reachable, unlike D1's). All 13 assertions pass, captured in `verification/verify_stale_stats_window_output.txt`. Numbers match `F1-VERIFICATION.md`'s own reported table exactly | `scripts/regulatory-intel/F1-VERIFICATION.md`; `verification/verify_stale_stats_window.py`, `verification/verify_stale_stats_window_output.txt` | — |
| 7 | B05 | The post-fix 33/98/280/0 count matches D1's own independently-verified unwindowed `impact_level` counts exactly, confirming this is a time-window defect, not a data-integrity issue | PASS — verbatim from `F1-VERIFICATION.md`'s "Verification" section; D1's own `verify_dashboard_stats.py` output (this fellow's 2026-11-03 project) reports the identical Critical 33 / High 98 / Medium 280 figures for the real unwindowed `impact_level` distribution | `F1-VERIFICATION.md`; `2026-11-03-the-dashboard-that-disagreed-with-its-own-alerts/verification/verify_dashboard_stats.py` | — |
| 8 | B06 | Honest limit 1: `source_distribution`'s 30-day window has the same structural staleness risk as the one just fixed, but was not changed this round — not directly contradicted by an always-visible adjacent list the way severity was; a reasonable follow-up, not required to close this bug | PASS — verbatim from `RUN_LOG.md`'s 2026-11-19 "Open issues" line and `F1-VERIFICATION.md`'s "What's NOT touched" section | `RUN_LOG.md` 2026-11-19; `F1-VERIFICATION.md` | — |
| 9 | B06 | Honest limit 2: not verified against a live running backend/frontend session — no server process was up this session; verified only via direct SQL replication of the exact query text against the live DB | PASS — verbatim from `RUN_LOG.md`'s 2026-11-19 "Open issues" line | `RUN_LOG.md` 2026-11-19 | — |
| 10 | B06 | `total_feeds`, `source_distribution`, `recent_activity`, and the `/api/feeds/stats` route are otherwise untouched; D1's `impact_level`-bucketing fix is untouched; `list_feeds()` and the frontend (`FeedList.jsx`, `Stats.jsx`, `App.jsx`) are untouched | PASS — verbatim from `F1-VERIFICATION.md`'s "What's NOT touched" section | `F1-VERIFICATION.md` | — |
| 11 | B07 | Takeaway: "a dashboard's summary is only as honest as the window it looks through, and a window that quietly stops matching the data underneath it is worse than no window at all" | PASS — editorial framing of the mechanism established in B02–B05, not a new factual claim requiring separate citation | — | — |

## Dramatization check

No beat claims this bug was observed to break a real user's live session in a running browser —
B05's numbers are the real, documented figures from this session's own live-DB query run, matching
`F1-VERIFICATION.md`'s and `RUN_LOG.md`'s independently reported results exactly. B06's two honest
limits (`source_distribution`'s own unaddressed 30-day window; no live browser/frontend session)
are stated at full weight, not smoothed into a claim that the fix is fully, end-to-end verified
against a running app. No invented statistics beyond what `F1-VERIFICATION.md` and `RUN_LOG.md`
state. The post-fix 33/98/280/0 figures and D1's own identical unwindowed counts (item 7 above) are
correctly attributed to their respective sessions, not blurred into a single claim of one
investigation.

## Resolved 2026-11-19

1. Confirmed every quoted date, SQL clause, label string, and diff against the real, current
   `crud.py`, `Stats.jsx`, and `App.jsx` on disk and `F1-VERIFICATION.md`, not from memory or
   paraphrase.
2. Confirmed B05's verification numbers by actually running
   `verification/verify_stale_stats_window.py` this session directly against the real, live
   `mycroft_intelligence` Postgres DB and cross-checking its output against `F1-VERIFICATION.md`'s
   and `RUN_LOG.md`'s own independently reported results — all agree exactly (0/0/0/0 ->
   33/98/280/0; 24 Critical / 8 High in the top-100 slice).
3. Confirmed B06's honest limits (the unaddressed `source_distribution` window and the no-live-
   session caveat) are carried forward verbatim from `F1-VERIFICATION.md`/`RUN_LOG.md`, not
   re-measured, escalated, or softened this session.
4. Confirmed `/Users/pranavijs/mycroft` was not modified by this session (`git status --short`
   before and after this project's research/verification work shows only the same pre-existing,
   unrelated `package-lock.json` changes in other components both times — see `FRICTIONAL.md`).
5. Confirmed the post-fix 33/98/280/0 figures and D1's own identical unwindowed counts are kept
   correctly attributed (item 7 above), not conflated into a single investigation's claim.

Gate P (narration review) can proceed.
