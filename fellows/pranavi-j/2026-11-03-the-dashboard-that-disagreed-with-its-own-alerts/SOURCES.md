# Sources — The Dashboard That Disagreed With Its Own Alerts

This is a real Project 29 (`mycroft`) engineering report, not a general topic explainer. Every
on-screen claim traces to this week's real fix in the repo, not an external source.

1. **`Regulatory_QA/backend/app/crud.py`** (`FeedCRUD.get_stats()`, current/post-fix state) — the
   real SQL that buckets severity by `impact_level = 'Critical'/'High'/'Medium'/'Low'`, plus the
   real in-code comment explaining why (`impact_level` is "the column email generation and every
   other consumer treats as authoritative... not re-derived from urgency_score"). Read directly
   from the file on disk this session (read-only, not modified). Full path:
   `scripts/mycroft-main/Core_Components/Regulatory_QA/backend/app/crud.py`.
2. **`scripts/regulatory-intel/D1-VERIFICATION.md`** — this week's own write-up of the bug, the
   fix diff (pre-fix `urgency_score` cutoffs vs. post-fix `impact_level` filters), and the
   verification table (Critical/High/Medium/Low, old vs. new, against the real live DB). Used
   verbatim in B03's pre-fix SQL and B04's diff; cross-checked against this session's own harness
   in B05.
3. **`/Users/pranavijs/mycroft/logs/RUN_LOG.md`**, entry dated `2026-11-03` ("Project 29
   regulatory dashboard: D1 fix") — the Recipe/Inputs/Commands-actions/Outputs/Result/Open-issues
   framing this video's B01–B06 follow. The "Open issues" line (the unwindowed-only verification
   caveat, and the `impact_level` `NULL`-row non-coverage) is quoted in B06's second honest-limit
   card.
4. **`verification/verify_dashboard_stats.py`** and
   **`verification/verify_dashboard_stats_output.txt`** (this project folder) — the Python
   harness built and run this session: extracts the real SQL from `get_stats()` in `crud.py` on
   disk (confirmed to match verbatim, exactly once), reconstructs the pre-fix SQL by undoing the
   exact diff from `D1-VERIFICATION.md`, and runs both — unmodified — via `sqlite3`'s
   `FILTER(WHERE ...)` aggregate support against a synthetic 411-row dataset engineered to
   reproduce `D1-VERIFICATION.md`'s own reported live-DB counts exactly. Used verbatim in B05.
   This session could not reach the live Postgres `mycroft_intelligence` DB directly (no working
   `DATABASE_URL` in this shell's environment — see `FRICTIONAL.md`), so this harness reproduces
   the mechanism and the documented numbers; it is not a second live DB query, and the harness's
   own docstring and this project's `FACTCHECK.md` (#4) say so plainly.
5. **`Regulatory_QA/frontend/src/components/Stats.jsx`** — the one frontend consumer of
   `get_stats()`'s response, confirming the `urgency_distribution.critical`/`.high` key names are
   unchanged by the fix (named, not shown verbatim, in B04's framing).
6. **`scripts/regulatory-intel/C3-VERIFICATION.md`** — last week's fix in the alert email
   (`Generate Email`'s `effectiveImpact()`), named in this video's continuity framing
   (BEAT-SHEET.md premise) as the investigation that first flagged this dashboard defect without
   fixing it.

No external (non-`mycroft`) sources used. No real third-party product, vendor, or individual named.
The regulator/agency names that could appear in this pipeline's own existing data (SEC, CFTC,
FINRA) are not shown in this video — B03/B04/B05 quote SQL and aggregate counts only, not
individual feed items.
