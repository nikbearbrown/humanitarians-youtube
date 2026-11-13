# Sources — The Filter That Didn't Know Its Own Labels

This is a real Project 29 (`mycroft`) engineering report, not a general topic explainer. Every
on-screen claim traces to this fellow's own work product from this week, not an external source.

1. **`scripts/mycroft-main/Core_Components/Regulatory_QA/backend/app/routers/feeds.py`**, commit
   `565e84e` on branch `feature/regulatory-intelligence-hardening` (not yet pushed) — the real
   before/after diff used in B04 (`Optional[SourceFeed]` -> `Optional[str]`, dropped `.value`
   accessor, dropped unused `SourceFeed` import). `git -C /Users/pranavijs/mycroft show 565e84e`.
2. **`scripts/mycroft-main/Core_Components/Regulatory_QA/backend/app/models.py`** — the real
   `SourceFeed(str, Enum)` class (5 fixed values) shown verbatim in B03.
3. **`scripts/regulatory-intel/workflow.dev.json`** (`Normalize Data` node, `identifySource()`
   function body) — the real dynamic-label-building logic
   (`` return `Federal Register - ${creator}`; ``) shown in B03, confirming the classifier emits
   labels outside the fixed enum.
4. **`scripts/regulatory-intel/UNKNOWN-SOURCE-INVESTIGATION.md`** — prior investigation
   corroborating that `identifySource()`'s Federal Register branch reliably reads the issuing
   agency from `dc:creator` and routes anything outside SEC/CFTC/FINRA to the dynamic
   `Federal Register - {creator}` label (dated 2026-08-30, still current).
5. **`scripts/mycroft-main/Core_Components/Regulatory_QA/backend/app/crud.py`** — `FeedCRUD.list_feeds`,
   confirming `source_feed` was already handled as a plain string at the SQL layer, used in B04's
   claim that the CRUD layer needed no change.
6. **`verification/verify_source_feed.py`** and **`verification/verify_source_feed_output.txt`**
   (this project folder) — the live FastAPI `TestClient` harness built and run this session: mounts
   the real, current `app.routers.feeds` router (post-fix) with `FeedCRUD.list_feeds` mocked via
   `unittest.mock.patch`, and separately reconstructs the exact pre-fix endpoint signature (matching
   `git show 565e84e`'s diff context) in an isolated app to reproduce the real 422. Used verbatim in
   B05.
7. **`/Users/pranavijs/humanitarians-youtube/fellows/pranavi-j/2026-10-15-the-alert-that-waited-for-a-second-item/FACTCHECK.md`**
   (item #6) — the prior week's report, which first flagged this exact `source_feed` compatibility
   gap as "identified, not yet fixed." Used in B01's continuity line and B06's honest-limit framing
   (the frontend-doesn't-send-this-param fact is carried forward from that fact-check, not
   re-verified against a newer frontend commit this session).

No external (non-`mycroft`) sources used. No real third-party product, vendor, or individual named
beyond the real regulator/agency names already public in the pipeline's own source labels (SEC,
CFTC, FINRA, Federal Register, Department of Labor — used only as a realistic example of a dynamic
label, not a claim about that specific agency's filings).
