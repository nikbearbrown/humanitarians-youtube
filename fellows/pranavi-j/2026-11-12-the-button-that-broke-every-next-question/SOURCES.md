# Sources — The Button That Broke Every Next Question

This is a real Project 29 (`mycroft`) engineering report, not a general topic explainer. Every
on-screen claim traces to this week's real fix in the repo, not an external source.

1. **`Regulatory_QA/frontend/src/App.jsx`** (current/post-fix state) — the real
   `MAX_SELECTABLE_FEEDS = 10` constant and the real `handleToggle`/`handleSelectAll` logic that
   caps both selection paths at it, plus the real comment explaining the constant ties to the
   backend's own limit. Read directly from the file on disk this session (read-only, not modified).
   Full path: `scripts/mycroft-main/Core_Components/Regulatory_QA/frontend/src/App.jsx`.
2. **`Regulatory_QA/frontend/src/components/ChatInterface.jsx`** (current/post-fix state) — the
   real error-reason-extraction block in the `catch` clause of `handleSubmit`, reading
   `error.response?.data?.detail` (string or FastAPI's list-of-`{msg}` shape) before falling back
   to `error.message`. Full path:
   `scripts/mycroft-main/Core_Components/Regulatory_QA/frontend/src/components/ChatInterface.jsx`.
3. **`scripts/regulatory-intel/E1-VERIFICATION.md`** — this week's own write-up of the bug, both
   fix diffs (`App.jsx`'s cap, `ChatInterface.jsx`'s error-reason extraction), and the verification
   table (5 checks against the extracted logic, including the real captured FastAPI 422 body for an
   oversized 15-item `feed_ids` list). Used verbatim in B02/B03's pre-fix code, B04's diff, and
   B05's harness results.
4. **`/Users/pranavijs/mycroft/logs/RUN_LOG.md`**, entry dated `2026-11-12` ("Project 29 regulatory
   frontend: E1 fix") — the Recipe/Inputs/Commands-actions/Outputs/Result/Open-issues framing this
   video's B01–B06 follow. The "Open issues" line (no UI cap indicator added; not verified against
   a running `vite` build/browser session) is quoted in B06's honest-limit cards.
5. **`Regulatory_QA/backend/app/models.py`** (`FeedQuery.feed_ids`, `max_items=10`) and
   **`app/config.py`** (`max_context_feeds: int = 10`) — the real backend limit the frontend fix
   makes the UI respect; named, not shown as a full file dump, in B02/B03.
6. **`verification/verify_feed_cap.js`** and **`verification/verify_feed_cap_output.txt`** (this
   project folder) — the Node.js harness built and run this session: extracts the real,
   current `handleToggle`/`handleSelectAll` logic from `App.jsx` on disk and the real, current
   error-reason-extraction block from `ChatInterface.jsx` on disk (each confirmed to match
   verbatim, exactly once), reconstructs the pre-fix version of each by undoing the exact diff from
   `E1-VERIFICATION.md`, and runs both — unmodified, spliced into a small Node `vm` driver script —
   against the 5 scenarios `E1-VERIFICATION.md`'s own table describes, including the real captured
   422 body for the 15-`feed_ids` case. Used verbatim in B05.
7. **`Regulatory_QA/frontend/src/components/FeedList.jsx`** — named (not shown verbatim) as the
   component whose "Select All" button is the real, unguarded, most-discoverable trigger for this
   bug; confirmed untouched by the E1 fix (per `E1-VERIFICATION.md`'s "What's NOT touched").

No external (non-`mycroft`) sources used. No real third-party product, vendor, or individual named.
No real feed item titles or regulator names are shown — B02/B03/B04/B05 quote selection logic,
limits, and the real 422 message only.
