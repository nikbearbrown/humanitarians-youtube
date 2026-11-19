# Sources — The Dashboard That Forgot What Day It Was

This is a real Project 29 (`mycroft`) engineering report, not a general topic explainer. Every
on-screen claim traces to this week's real fix in the repo, not an external source.

1. **`Regulatory_QA/backend/app/crud.py`** (current/post-fix state) — the real `FeedCRUD.get_stats()`
   function: the unwindowed severity-count query (no `WHERE created_at` clause), the unwindowed
   `total_feeds` `COUNT(*)`, `source_distribution`'s untouched 30-day window, and
   `recent_activity`'s untouched 14-day window, plus the real in-code comment explaining the fix
   and pointing at `F1-VERIFICATION.md`. Read directly from the file on disk this session
   (read-only, not modified). Full path:
   `scripts/mycroft-main/Core_Components/Regulatory_QA/backend/app/crud.py`.
2. **`scripts/regulatory-intel/F1-VERIFICATION.md`** — this week's own write-up of the bug, the
   fix diff (removing `WHERE created_at >= NOW() - INTERVAL '7 days'` from the severity query),
   and the verification table (old 0/0/0/0, new 33/98/280/0 against the live 411-row DB). Used
   verbatim in B02/B03's setup, B04's diff, and B05's verification numbers.
3. **`/Users/pranavijs/mycroft/logs/RUN_LOG.md`**, entry dated `2026-11-19` ("Project 29
   regulatory dashboard: F1 fix") — the Recipe/Inputs/Commands-actions/Outputs/Result/Open-issues
   framing this video's beats follow. The "Open issues" line (`source_distribution`'s own
   unaddressed 30-day window; not verified against a live running backend/frontend session) is
   quoted in B06's honest-limit cards.
4. **`Regulatory_QA/frontend/src/components/Stats.jsx`** — the real on-screen card labels quoted
   verbatim in B02/B03: `"Total Feeds"`, `"Critical"`, `"High Priority"`, `"Selected"`
   (`StatCard` components reading `stats.total_feeds`, `urgency.critical`, `urgency.high`).
   Confirmed untouched by the F1 fix.
5. **`Regulatory_QA/frontend/src/App.jsx`** — the real `feedsAPI.listFeeds({ limit: 100 })` call
   (unchanged since last week's E1 fix) that determines the top-100 slice `FeedList.jsx` renders;
   named and quoted in B03/B05. Confirmed untouched by the F1 fix.
6. **`verification/verify_stale_stats_window.py`** and
   **`verification/verify_stale_stats_window_output.txt`** (this project folder) — the live
   Python/psycopg2 harness built and run this session: extracts the real, current severity SQL
   from `crud.py` on disk (confirmed to match verbatim, exactly once), reconstructs the pre-fix
   query by re-adding exactly the removed `WHERE` clause, and runs both — unmodified — directly
   against the real, live `mycroft_intelligence` Postgres DB (411 rows, `localhost:5431`), plus a
   separate replication of `list_feeds()`'s actual default ordering/limit against the same live
   DB. All 13 assertions pass. Used verbatim in B02/B05.
7. **D1-VERIFICATION.md** and
   **`2026-11-03-the-dashboard-that-disagreed-with-its-own-alerts/`** (this fellow's prior video)
   — named, not re-derived, as the source of the "matches last week's independently verified
   counts exactly" claim in B05 (D1's own unwindowed `impact_level` counts: Critical 33 / High 98
   / Medium 280, identical to this week's post-fix numbers — confirming F1 is a time-window
   defect, not a data-integrity issue).

No external (non-`mycroft`) sources used. No real third-party product, vendor, or individual named.
No real feed item titles or regulator names are shown — B02/B03/B04/B05 quote the SQL window, the
dashboard's label text, and count numbers only.
