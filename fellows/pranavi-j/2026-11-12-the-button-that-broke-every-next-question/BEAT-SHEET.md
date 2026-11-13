# Beat Sheet (APPROVED — Gate P, 2026-11-12): "The Button That Broke Every Next Question"

**Creator:** Sai Pranavi J. | Weekly work video
**Format:** `work-report`, same register as this fellow's prior Project 29 reports
**Phase:** 2 — approved for narration lock / audio generation.

---

## Premise

**What this covers:** a real bug found and fixed this week (E1) in Project 29's regulatory
intelligence frontend (`mycroft`), `Regulatory_QA/frontend/src/{App.jsx, components/ChatInterface.jsx}`.
The chat endpoint (`POST /api/chat`) hard-caps context to 10 feeds — enforced by Pydantic on
`FeedQuery.feed_ids` (`models.py`, `max_items=10`) and documented as an intentional RAG context-size
limit (`config.py`'s `max_context_feeds: int = 10`). Nothing on the frontend respected that limit:
`App.jsx` loads up to 100 feeds, and `FeedList.jsx`'s prominent, unguarded "Select All" button —
the single most discoverable, inviting action in the feed panel, top of the list, no disabled state,
no tooltip — called `handleSelectAll()`, which selected every loaded feed with no cap at all. On the
real, live `mycroft_intelligence` DB (411 rows), clicking it selects close to 100 feeds, and any
question asked afterward is guaranteed to fail backend validation with HTTP 422. Compounding it,
`ChatInterface.jsx`'s error handler only ever showed axios's generic `error.message` — for a non-2xx
response that's just `"Request failed with status code 422"` — and never read
`error.response.data.detail`, where FastAPI actually puts the real validation reason. The user saw a
meaningless, network-sounding error with zero indication the real problem was "you selected too many
feeds."

**The fix:** `App.jsx` now caps both selection paths (`handleSelectAll` AND individual `handleToggle`
clicks) at the same `MAX_SELECTABLE_FEEDS = 10` the backend enforces — capping only the button would
leave the exact same outage reachable via 11 individual clicks. `ChatInterface.jsx`'s catch block now
extracts `error.response.data.detail` (a plain string, or FastAPI's list-of-`{msg}` shape) before
falling back to `error.message`, as defense-in-depth for any other validation error the backend might
return.

**What this deliberately avoids:** no claim that a `vite build`/browser end-to-end check confirmed
this in a running app — `node_modules` is not installed in this environment, out of scope for a
two-line logic fix. Verification relied on a Node.js harness extracting and running the real,
patched logic directly, plus the IDE's own static diagnostics (zero new errors on either edited
file). No visual indicator (disabled state/tooltip) was added once the cap is reached — selection
silently stops growing past 10 with no UI feedback explaining why; a reasonable follow-up, not
required to close the functional bug. Kept as an honest, full-weight caveat (B06), not smoothed over.

**Source status:** real Project 29 (`mycroft`) engineering fix, closed 2026-11-12
(`Regulatory_QA/frontend/src/App.jsx`, `src/components/ChatInterface.jsx`; see `RUN_LOG.md`'s
2026-11-12 entry and `E1-VERIFICATION.md`). Independently re-verified this session via a Node.js
harness (`verification/verify_feed_cap.js`) that extracts the real, current `handleToggle`/
`handleSelectAll` logic from `App.jsx` on disk and the real, current error-reason-extraction logic
from `ChatInterface.jsx` on disk, reconstructs the pre-fix version of each by undoing the exact
documented diff, and runs both — unmodified — against the same 5 behavioral scenarios
`E1-VERIFICATION.md`'s own verification table describes. See `SOURCES.md` and `FACTCHECK.md`.

---

## Legibility Contract (what's on screen at each claim)

| Beat | On-screen artifact | Legibility note |
|---|---|---|
| B00 Title | Title card, silent | No narration |
| B01 Exec summary | Fellow name + one-line plain-language summary | Narrated, matches program's fixed format |
| B02 Hook | The backend's real 10-feed cap next to Select All's real "no cap" code | Verbatim from `models.py`/`App.jsx` (pre-fix), not paraphrased |
| B03 Setup | The real pre-fix `handleSelectAll`/`handleToggle`, the real backend limit, and the real pre-fix generic error line | Verbatim from `App.jsx`/`ChatInterface.jsx` (pre-fix) and `E1-VERIFICATION.md` |
| B04 Discovery/fix | The real diff for both files, matches `E1-VERIFICATION.md`'s "The fix" exactly | Real diff, not illustrative |
| B05 Verification | The real before/after results from this session's own Node harness (5 checks, 7 assertions) | Real measured results, not illustrative |
| B06 Honest limits | What was NOT verified (no `vite build`/browser check) and what was NOT added (no UI cap indicator) | Full weight, no softening |
| B08 Sign-off | Brand card | @HumanitariansAI, in for Sai Pranavi J. |

---

## Beats

**B00. Title (silent, ~0:00–0:04)**
Visual: title card — "The Button That Broke Every Next Question" + @HumanitariansAI. No narration.

**B01. Exec summary (~0:04–0:21)**
VO: "Hi, I'm Sai Pranavi J. This video is about a button labeled 'Select All,' sitting right at the
top of a feed list, that could silently break every question you asked afterward — and an error
message that never once told you why."
Visual: name card, one-line summary text on screen as it's spoken.

**B02. Hook (~0:21–0:41)**
VO: "Our chat assistant has a hard limit: ten feeds per question, a deliberate cap on how much
context goes to the model. The feed panel loads up to a hundred items. And the single most obvious
thing to click, 'Select All,' had no limit at all."
Visual: two tiles — the backend's real 10-feed cap, versus Select All's real pre-fix code with no
cap, visually flagged as a mismatch.

**B03. Setup (~0:41–1:10)**
VO: "Here's the real code. Select All used to set every loaded feed selected, no limit, no check.
The backend's own feed query caps feed ids at ten items, by design, so the model's context doesn't
blow up. And when that cap got violated, the chat's error handler only ever showed axios's own
generic message: request failed with status code four twenty two. The real reason FastAPI sent back
was sitting right there in the response. The code just never read it."
Visual: the real pre-fix `handleSelectAll`/`handleToggle`, the backend's real `max_items=10` field,
and the real pre-fix generic error line, shown verbatim.

**B04. Discovery and fix (~1:10–1:33)**
VO: "The fix caps selection at ten, in both places: the button, and clicking feeds one at a time,
because eleven individual clicks would hit the exact same outage. And the chat's error handler now
reads the server's real reason first, falling back to the generic message only when there isn't
one."
Visual: the real diff: `MAX_SELECTABLE_FEEDS = 10` added and both selection paths capped in `App.jsx`;
the real detail-extraction block added to `ChatInterface.jsx`'s catch clause.

**B05. Verification (~1:33–2:02)**
VO: "I extracted both fixes into a live Node harness and ran five checks. Select All against a four
hundred eleven feed table now selects exactly ten. Fifteen individual clicks in a row stop adding at
ten. Untoggling one and adding another still holds the cap. And the error message that used to read
'request failed with status code four twenty two' now reads the real reason: list should have at
most ten items after validation, not fifteen. All seven assertions across those five checks pass."
Visual: the real before/after table from this session's own harness (5 checks, old behavior vs. new
behavior, the real captured 422 message text).

**B06. Honest limits (~2:02–2:32)**
VO: "Two honest limits. First: this was verified against the extracted logic in a Node harness, not
a running browser build — node modules isn't installed here, so there was no full vite build or
end-to-end browser check, only the I-D-E's own static diagnostics, which came back with zero new
errors. Second: nothing was added to actually tell the user selection stopped growing at ten — no
disabled state, no tooltip. It just silently stops. That's a reasonable follow-up, not done yet."
Visual: 2 honest-limit cards, side by side, full weight, no softening language.

**B07. Takeaway (~2:32–2:43)**
VO: "The most obvious button in the interface is exactly the one that needs to respect the system's
real limits — and when something does fail, showing the real reason is what turns an outage into
something a user can actually fix."
Visual: statement card.

**B08. Sign-off (~2:43–2:45)**
VO: "Explained with Claude Code."
Visual: brand card — @HumanitariansAI, in for Sai Pranavi J..

---

## Production Gate Self-Check (pre-review)

- [ ] B02/B03's quoted code and backend limit shown verbatim, match the real pre-fix `App.jsx`/
      `ChatInterface.jsx` and `models.py`/`config.py`
- [ ] B04's diff matches the real committed fix exactly (per `E1-VERIFICATION.md`)
- [ ] B05's table uses real measured harness results from this session, not illustrative numbers;
      matches `E1-VERIFICATION.md`'s own verification table exactly (5 checks, 7 assertions, the real
      captured 422 message text for the 15-feed_ids test case)
- [ ] B06's honest limits kept at full weight, not softened: no `vite build`/browser end-to-end check,
      no UI indicator added for the cap
- [ ] Silent title card present; brand/fellow sign-off card present
- [ ] No claim that this was observed to break a real user's session in production — this closes a
      confirmed, reproducible defect, verified via extracted-logic harness, not an observed incident

**Estimated runtime:** ~2:45 (draft estimate; real timing measured after Kokoro audio generation, per
the toolkit's audio-first rule — see `SHOTLIST.md` for the measured total).

---

## Gate P — approved

Fellow reviewed and approved this beat-by-beat outline 2026-11-12. See `FACTCHECK.md`. Cleared to
generate Kokoro audio and proceed to previz.
