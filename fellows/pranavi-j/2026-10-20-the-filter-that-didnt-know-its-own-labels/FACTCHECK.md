# FACTCHECK — The Filter That Didn't Know Its Own Labels

Status: **RESOLVED — fellow reviewed 2026-10-20. Cleared for Gate P (narration lock).**

| # | Beat | Claim (as spoken/shown) | Verdict | Source / derivation | Fix if needed |
|---|---|---|---|---|---|
| 1 | B03 | `SourceFeed` is a 5-value fixed enum: SEC Press Releases, Federal Register - Securities, FINRA Enforcement News, CFTC Regulations, Investment Advisor Rules | PASS — verbatim read of the `SourceFeed(str, Enum)` class, lines 12-17 | `Regulatory_QA/backend/app/models.py` | — |
| 2 | B03 | The real classifier, `identifySource()`, builds a dynamic label `` `Federal Register - ${creator}` `` for Federal Register items whose issuing agency isn't SEC/CFTC/FINRA | PASS — verbatim read of the `identifySource` function body inside the `Normalize Data` node's `jsCode` | `scripts/regulatory-intel/workflow.dev.json` (`Normalize Data` node); corroborated by `UNKNOWN-SOURCE-INVESTIGATION.md`'s worked example, `Federal Register's dc:creator reliably carries the actual issuing agency's full name` | — |
| 3 | B04 | The fix is a 2-line diff in `feeds.py`: `Optional[SourceFeed]` -> `Optional[str]` (param), and `source_feed.value if source_feed else None` -> `source_feed` (pass-through); the now-unused `SourceFeed` import is also dropped | PASS — exact diff matches commit `565e84e`, `git -C /Users/pranavijs/mycroft show 565e84e` | `scripts/mycroft-main/Core_Components/Regulatory_QA/backend/app/routers/feeds.py`, commit `565e84e` | — |
| 4 | B04 | The CRUD layer (`FeedCRUD.list_feeds`) already treated `source_feed` as a plain string — the `.value` accessor was the only enum-specific code, and removing it changes nothing downstream | PASS — read `crud.py`'s `list_feeds`: `if source_feed: conditions.append("source_feed = %s"); params.append(source_feed)` — no enum-specific handling, SQL bind is a plain string either way | `Regulatory_QA/backend/app/crud.py` | — |
| 5 | B05 | Live before/after TestClient table: pre-fix dynamic label -> 422 (enum validation error, exact message matches Pydantic's real output); post-fix dynamic label -> 200, mocked CRUD received the exact unmodified string; a known fixed-enum label (`SEC Press Releases`) passes 200 unchanged in both versions | PASS — real output from this session's own harness (`verification/verify_source_feed.py`), re-run and captured to `verification/verify_source_feed_output.txt`. Post-fix router is the real, current `app.routers.feeds` module (unmodified import). Pre-fix router is a byte-for-byte reconstruction of the parent-commit endpoint signature (confirmed against `git show 565e84e`'s diff context), mounted in an isolated FastAPI app so the real 422 can be reproduced without mutating the working tree or requiring a live Postgres instance. | — |
| 6 | B06 | "Nothing shows this 422 ever hit a real user — the frontend doesn't currently send this parameter at all" | PASS — true; this is the same frontend-behavior fact already established and fact-checked in the prior week's report (`2026-10-15-the-alert-that-waited-for-a-second-item/FACTCHECK.md` #6: "not yet triggered in practice because the frontend doesn't currently pass `source_feed` as a query param"). Not re-verified against a newer frontend commit this session — carried forward as still true absent evidence otherwise; phrased as a known absence of incident, not a verified non-occurrence for all time. | Must stay phrased as "nothing shows," not "confirmed never happened" |
| 7 | B06 | "This verification mocked the database layer — it doesn't confirm a live query against a database that actually contains rows with these dynamic labels" | PASS — true and by design: `verify_source_feed.py` patches `FeedCRUD.list_feeds` with `unittest.mock.patch`, so no live Postgres connection is made or required. This is an honest scope limit on today's verification, not a claim that the fix itself is incomplete — the SQL path (`source_feed = %s` with a plain string bind) is unchanged by this fix and was already string-typed. | Must stay phrased as a verification-scope limit, not an engineering gap |

## Dramatization check

No beat claims this 422 was ever observed in a real request from the live frontend or a real
operator — B06 states plainly the frontend doesn't currently send this parameter, so this is a
preventative fix for a latent defect, not a fix for an observed outage or incident. No invented
statistics (e.g., no claim about how many Federal Register items actually carry a dynamic label
in the live database — not measured this session, not stated on screen).

## Open items (resolve before Gate P)

None identified — all claims trace directly to the real commit diff (`565e84e`), the real source
files (`models.py`, `workflow.dev.json`, `crud.py`), and this session's own live TestClient
harness output, captured verbatim in `verification/verify_source_feed_output.txt`.
