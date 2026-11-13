# FACTCHECK — The Button That Broke Every Next Question

Status: **RESOLVED — fellow reviewed 2026-11-12. Cleared for Gate P (narration lock).**

| # | Beat | Claim (as spoken/shown) | Verdict | Source / derivation | Fix if needed |
|---|---|---|---|---|---|
| 1 | B02/B03 | The chat endpoint hard-caps context to 10 feeds (`FeedQuery.feed_ids`, `max_items=10` in `models.py`, matching `config.py`'s `max_context_feeds: int = 10`) | PASS — verbatim from `E1-VERIFICATION.md`'s "The bug" section, naming both the Pydantic field and the config setting | `Regulatory_QA/backend/app/models.py`; `app/config.py`; `E1-VERIFICATION.md` | — |
| 2 | B02/B03 | `App.jsx` loads up to 100 feeds (`feedsAPI.listFeeds({ limit: 100 })`); pre-fix, `FeedList.jsx`'s "Select All" called `handleSelectAll()`, which selected every loaded feed with no cap | PASS — verbatim read of the real, current `App.jsx`'s `loadData()` (`limit: 100`, unchanged by this fix) and the real pre-fix `handleSelectAll` body quoted in `E1-VERIFICATION.md`'s "The bug" | `Regulatory_QA/frontend/src/App.jsx` (current); `E1-VERIFICATION.md` | — |
| 3 | B02 | On the live DB (411 rows), clicking "Select All" selects close to 100 feeds | PASS — verbatim from `E1-VERIFICATION.md` ("On the live `mycroft_intelligence` DB (411 rows), clicking it selects close to 100 feeds") and `RUN_LOG.md`'s 2026-11-12 entry ("the live DB has 411 rows, so ordinary use selects close to 100 feeds"). **Caveat, kept out of narration:** this is a qualitative "close to 100," not an exact count — the real number depends on how many of the 411 live rows the `limit: 100` fetch returns, which this session did not re-query live (see item 8 below). This project's own harness (`verify_feed_cap.js`, Test 1) demonstrates the *pre-fix* `handleSelectAll` is unbounded by running it directly against a synthetic 411-row list and showing it selects all 411 — a deliberately more extreme input than the real ~100-feed fetch, chosen to demonstrate "no cap at all" unambiguously, not a claim that a real browser session selects 411. Narration says "close to a hundred" (matching the documented real behavior), never 411 — see FRICTIONAL.md for how this distinction surfaced during the build | `E1-VERIFICATION.md`; `RUN_LOG.md` 2026-11-12; `verification/verify_feed_cap_output.txt` | Keep narration at "close to a hundred," never claim the harness's 411-row test is itself the real browser count |
| 4 | B03 | `ChatInterface.jsx`'s pre-fix catch block showed only `'Failed to get response: ' + error.message`, which for a 422 is just `"Request failed with status code 422"`, never `error.response.data.detail` | PASS — verbatim from the real diff in `E1-VERIFICATION.md`'s "The fix" ("-" line) and confirmed this session by reconstructing the exact pre-fix block via string substitution against the real, current `ChatInterface.jsx` on disk, with a hard check that the post-fix block occurs exactly once before trusting the reconstruction (`verification/verify_feed_cap.js`) | `Regulatory_QA/frontend/src/components/ChatInterface.jsx` (current); `E1-VERIFICATION.md` | — |
| 5 | B04 | The fix: `App.jsx` adds `MAX_SELECTABLE_FEEDS = 10` and caps both `handleToggle` (an `else if (newSet.size < MAX_SELECTABLE_FEEDS)` guard) and `handleSelectAll` (`feeds.slice(0, MAX_SELECTABLE_FEEDS)`); `ChatInterface.jsx` adds a `detail`/`reason` extraction before building `errorMessage` | PASS — exact diff matches `E1-VERIFICATION.md`'s "The fix" section and the real, current source of both files on disk, confirmed by reading the live files directly (not from the markdown alone) | `Regulatory_QA/frontend/src/App.jsx`; `src/components/ChatInterface.jsx`; `E1-VERIFICATION.md` | — |
| 6 | B04 | `handleToggle` is capped too, not just `handleSelectAll` — otherwise a user could reach the same outage via 11 individual clicks | PASS — verbatim rationale from `E1-VERIFICATION.md`'s "The fix" section | `E1-VERIFICATION.md` | — |
| 7 | B05 | Live verification table: (1) `handleSelectAll` against a 411-feed list selects exactly 10; (2) 15 sequential `handleToggle` calls stop adding at 10; (3) untoggling at the cap then adding a new feed frees a slot and stays capped at 10; (4) error-extraction against the real captured 422 body for 15 `feed_ids` — old `"Request failed with status code 422"`, new `"List should have at most 10 items after validation, not 15"`; (5) with no `response.data.detail`, falls back to `error.message` unchanged. 5 checks, 7 assertions, all PASS | PASS — matches `E1-VERIFICATION.md`'s own verification table and `RUN_LOG.md`'s 2026-11-12 entry exactly ("All 5 behavioral checks pass"). Independently reproduced this session via `verification/verify_feed_cap.js`: the real, current `handleToggle`/`handleSelectAll` and error-extraction logic (confirmed to match the real source files verbatim, exactly once each) were spliced unmodified into a Node `vm` driver and run against these 5 scenarios, plus a reconstructed pre-fix version of each for comparison — all 7 assertions pass, captured in `verification/verify_feed_cap_output.txt`. The real 422 message text ("List should have at most 10 items after validation, not 15") is quoted verbatim from `E1-VERIFICATION.md`'s own captured FastAPI `TestClient` response for a 15-item `feed_ids` list — this is a smaller, deliberately-oversized test input used to generate a concrete, real validation message, **not** the real browser session's ~100-feed "Select All" overselect count (those are two different numbers; see item 3) | `scripts/regulatory-intel/E1-VERIFICATION.md`; `RUN_LOG.md` 2026-11-12; `verification/verify_feed_cap.js`, `verification/verify_feed_cap_output.txt` | Narration/table must not conflate the 15-`feed_ids` test case (used for the captured 422 message) with the ~100-feed "Select All" overselect scenario (B02/B03) — keep them as two distinct, correctly-labeled numbers |
| 8 | B06 | Honest limit 1: no full `vite build`/browser end-to-end check was done — `node_modules` is not installed in this environment; relied on a Node harness running the extracted logic plus the IDE's own static diagnostics (zero new errors on either edited file) | PASS — verbatim from `E1-VERIFICATION.md`'s "Verification" section and `RUN_LOG.md`'s 2026-11-12 "Open issues"/"Commands / actions" lines | `E1-VERIFICATION.md`; `RUN_LOG.md` 2026-11-12 | — |
| 9 | B06 | Honest limit 2: no visual indicator (disabled state/tooltip) was added once the cap is reached — selection silently stops growing past 10, with no UI feedback explaining why; a reasonable follow-up, not required to close the functional bug | PASS — verbatim from `E1-VERIFICATION.md`'s "What's NOT touched" section and `RUN_LOG.md`'s 2026-11-12 "Open issues" line | `E1-VERIFICATION.md`; `RUN_LOG.md` 2026-11-12 | — |
| 10 | B06 | The backend's `max_items=10` limit and `max_context_feeds` setting are untouched — this fix makes the frontend respect the backend's existing limit, not loosen it. `FeedList.jsx`, `Stats.jsx`, `Header.jsx` are untouched | PASS — verbatim from `E1-VERIFICATION.md`'s "What's NOT touched" section | `E1-VERIFICATION.md` | — |
| 11 | B07 | Takeaway: "the most obvious button in the interface is exactly the one that needs to respect the system's real limits, and showing the real reason on failure is what turns an outage into something a user can fix" | PASS — editorial framing of the mechanism established in B02–B05, not a new factual claim requiring separate citation | — | — |

## Dramatization check

No beat claims this bug was observed to break a real user's live session in production — B02/B03's
"close to a hundred" framing and B05's harness numbers are the real, documented figures
`E1-VERIFICATION.md` and `RUN_LOG.md` report from this week's own investigation (a live FastAPI
`TestClient` run against the real `app.models.FeedQuery`, not an observed end-user incident),
independently reproduced this session via a harness run against the real extracted logic. B06's two
honest limits (no `vite build`/browser check; no UI cap indicator added) are stated at full weight,
not smoothed into a claim that the fix is fully, end-to-end verified. No invented statistics beyond
what `E1-VERIFICATION.md` and `RUN_LOG.md` state. The distinction between the ~100-feed real overselect
scenario and the 15-`feed_ids` test case used to capture the real 422 message (item 7 above) is kept
visible in both FACTCHECK and the script, not blurred into a single number.

## Resolved 2026-11-12

1. Confirmed every quoted code line and diff against the real, current `App.jsx` and
   `ChatInterface.jsx` on disk and `E1-VERIFICATION.md`, not from memory or paraphrase.
2. Confirmed B05's harness table by actually running `verification/verify_feed_cap.js` this session
   and cross-checking its output against `E1-VERIFICATION.md`'s and `RUN_LOG.md`'s own independently
   reported results — all agree exactly (5 checks, 7 assertions, same real 422 message text).
3. Confirmed B06's honest limits (the no-`vite`-build caveat and the no-UI-indicator gap) are carried
   forward verbatim from `E1-VERIFICATION.md`/`RUN_LOG.md`, not re-measured, escalated, or softened
   this session.
4. Confirmed `/Users/pranavijs/mycroft` was not modified by this session (`git status --short` before
   and after this project's research/verification work shows only the same pre-existing, unrelated
   changes both times — see `FRICTIONAL.md`).
5. Confirmed the ~100-feed "Select All" overselect figure (B02/B03) and the 15-`feed_ids` test case
   behind the captured 422 message (B05) are two distinct numbers, kept separately labeled throughout
   — not conflated (item 7 above).

Gate P (narration review) can proceed.
