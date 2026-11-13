# FRICTIONAL.md — How the Tutor Stays Grounded in Your Textbook

This is an append-only log. Never rewrite an earlier entry.

## 2026-09-23: source research (AI-TUTOR-SOURCE.md)

**Tried / expected:** I expected the book's docs and the 2026-09-18 reference reel to describe the tutor accurately enough to script from.

**Where it resisted:** they don't. Reading the current code (`medhavi-cancer@b8b6c21`) shows three things:
- The analyzer ignores the open page, and retrieval runs over the whole book.
- Live memory is the hub's API, not SQLite. `lib/chat-memory/sqlite.ts` isn't imported anywhere.
- The source cards are retrieval results sent before the model call, not citations.

The reference reel's "uses this chapter as context" line is contradicted.

**Contribution:**
- Claude Code read the code and drafted AI-TUTOR-SOURCE.md with line references.
- Prarthana set the no-claim list and approved the document.

**Understood / open:**
- The production model, hybrid-search flag and prompt file can't be seen from the repo.

## 2026-09-23: planning

**Tried:**
- A 16-beat plan, about 3 minutes, with 10 real-footage beats.
- Capture plans adapted from the reference's proven step names.

**Where it resisted:**
- **Clicking a source card.** The capture driver has no step for clicking a card, which is a `div`. It can only click by exact text, so the card title must be known before the run. The fix: a pilot run, plus a provisional title ("5.4.2 Gene Amplification") that makes the run abort rather than fake anything if it's wrong.
- **Clear is disabled on an empty chat.** A memory reset can't be scripted cleanly. It would also delete the account's stored tutor turns, possibly across books. Left as Prarthana's decision, not scripted.
- **The mechanism diagram.** No library composition gives a labelled flow in both 16:9 and 9:16 at 4K. `FluencySourceFlow` is 1920×1080 with no 916 variant. So B10 is a design card (`GroundingFlow`), not a slate.
- **Vertical capture.** The driver records only 3840×2160, so the 9:16 companion's panel legibility is unresolved.

**Found in passing:** the suggestion chips are fixed templates filled with the page title, not model-generated. Recorded as an addendum in FACTCHECK.md.

**Contribution:**
- Claude Code drafted the plan and narration.
- Prarthana set the three wording rules and the no-manufacture list.

**Open:**
- Account type
- Outro choice (ClaudeTitleOutro per the skill vs. MedhavyOutro)
- Vertical approach
- Whether to author `GroundingFlow` in the toolkit or reel-locally

## 2026-09-23: planning revision after review

**Decided by Prarthana:**
- The account is admin. There is no student branch.
- Her name in the hub header must be masked before recording.
- The outro is `ClaudeTitleOutro`, as the skill requires.
- `GroundingFlow` stays local to this folder.
- Vertical is a separate portrait composition.
- No memory clear without her decision.
- The narration is cut to 430–460 words, with a plain-language B10.

**Where it resisted:**
- **Name masking.** Planning the masking exposed a gap: the admin header shows a *single-word* first name (`AdminDashboard.tsx:578-580`). The toolkit driver's mask only catches two-word names inside list or card containers, and its leak check ignores names. The stock driver would have recorded the name and reported a clean run. That is not acceptable when masking must happen before capture, and the toolkit can't be edited. So the plan is a reel-local wrapper that adds a runtime-supplied mask term and a fail-closed leak check. It is pending approval and not yet written.
- **Vertical from a 1600-CSS capture.** The panel is only about 1008 device px wide, so a portrait reframe upscales it by about 2.1×. Flagged; the remedy is still an open decision.

**Changes:**
- Narration went from 517 to 451 words.
- B10 is now six plain steps with no implementation terms.
- The UI label "Top sources used" is no longer spoken.
- B08/B09 are included only if V2/V3 are observed.
- Conditional lines carry a word-budget trim table.

**Contribution:**
- Claude Code revised the planning files and found the masking gap from source.
- Prarthana made the decisions above.

## 2026-09-23: wrapper design and portrait-source plan

**Decided by Prarthana:**
- The masking wrapper is approved, local to this folder.
  - The name comes only from the environment.
  - There is a literal-name leak check; a leak means abort and delete.
  - The design is reviewed before the wrapper is written.
- Vertical option B: 1280×720 CSS at DPR 3, gated by a layout test that sends no tutor requests.
- Landscape runs first, then a stop for review.
- No automatic memory clear.
- Nothing leaves the machine: no git actions.

**Where it resisted, while designing:**
- **Deletion on failure.** The toolkit driver only discards a leaky capture at the *end* of a successful run. A crash midway would leave the raw WebM and screenshots behind. So the wrapper must abort on the first leak and delete on any failure.
- **Background tab.** The driver checks only the active tab, but the hub tab keeps recording after the book opens. The wrapper checks every open page.
- **In-place text changes.** The toolkit observer ignores text changed in place, so the wrapper adds a `characterData` observer.
- **What counts as visible.** A strict "anywhere in the DOM" check would always trip on the Next.js payload in `<script>` tags. The check is therefore on rendered text and input values, backed by a human frame review.
- **Memory carryover.** Each run's tutor turns become recent conversation context for the next run: pilot → real → portrait. This is flagged as a likely interference point; any clear stays Prarthana's decision.
- **Different portrait answers.** The portrait take will produce different answers, so its narration must be re-checked against its own footage.

**Contribution:**
- Claude Code designed the wrapper and the plans.
- Prarthana set the requirements.
- Nothing has been written or run yet.

## 2026-09-24: pilot capture and review

**Ran:**
- `save_session.py`: Prarthana signed in herself.
- `run-signin`: signed out.
- `run-pilot`: masked; Prarthana ran it from her own shell with `MW_MASK_TEXT` set.

**Result:** exit code 0, all DOM leak checks passed, and no canary in either video.

**Redaction review:**
- Header-strip crops of every hub frame read "Admin account" from the first rendered frame.
- No names, emails or codes appeared on screen.
- The temporary sheets were then deleted.

**Where it resisted:**
- **The follow-up was off-screen.** The reopened panel sat scrolled to the top, so the follow-up and its reply streamed off-screen. V6 couldn't be observed. The plan now scrolls the messages to the bottom first and captures the reply top early.
- **"Three cards" was wrong on screen.** Three cards render, but only about 1.5 fit the panel width, so "three show at first" would have been false in the footage. The line was rewritten.

**Decided by Prarthana:**
- No memory clear.
- Verified behaviours are locked into the narration.
- The off-topic cards are described modestly.
- "Thanks!" is dropped from the corrected run.

## 2026-09-24 to 2026-09-29: production (wrapper, captures, render, exports)

**Wrapper.**
- `capture/capture_masked.py` was built to the reviewed design.
- It loads the toolkit's `capture_admin.py` as a module and extends its `MASK` in memory, so there is no Playwright patching and no toolkit edit.
- It passed its offline self-test, 11/11, against `file://` pages with the dummy term `Testname`.
- A control run confirmed the stock mask alone would have left the single-word header name visible.

**Captures.**
- Prarthana signed in herself and set the mask term privately for each signed-in run.
- Runs, all masked and all with clean redaction reviews: `run-signin`, `run-pilot`, `run-book`, `run-portrait-test`, `run-portrait`.
- **Pilot fixes carried into `run-book`:**
  - the follow-up had been off-screen
  - the "three cards" claim was false on screen
  - "Thanks!" was dropped
- **Portrait take:**
  - The layout test passed before any tutor request was sent.
  - The take showed the follow-up question and its drifted cards, but not the reply body, which sat below the 720-px panel edge.
  - Vertical B11 was therefore worded from the code ("still receives recent conversation context") rather than from footage.
- Tutor memory was never cleared.

**Portrait framing and QC fixes.**
- The first PanelFocus916 crops cut text lines at the frame edges, which the frame QC flagged.
- Crops were reworked so no text line crosses an edge:
  - `clipX` panel-column masks for B05–B08 and B11
  - a sidebar-column mask for B04
  - full-page fits for B03 and B09
- `vertical-windows.json` records the final framing.

**Remotion browser start-up.**
- Remotion intermittently failed with "Timed out … trying to connect to the browser" under WSL, and each time the render retried once and succeeded.
- One portrait clip (B03) failed with a compositor SIGKILL. The cause was two 4K render jobs running at once. After that, all renders ran strictly one at a time, and B03 re-rendered cleanly on its own.
- A second, self-inflicted problem: an edit and a still render once ran as parallel tool calls, so the still showed old code. It was diagnosed with a visible marker, and from then on every render ran only after the edit was verified on disk.

**Python 3.10 compatibility.** The toolkit's `prepare_media.py` calls `hashlib.file_digest` (Python 3.11+), and WSL has 3.10.12. It was run unmodified with an in-memory backport of that one function (BUILD-PROMPT.md §4).

**Contrast and type-gate fixes.**
- **Landscape:** GATE T flagged GroundingFlow's terracotta border and connectors as low-contrast accent text (2.74:1). They became ink and ink-soft, and GATE T then passed.
- **Vertical text sizes:** GATE T §8.1 (72 px floor at 3840) failed B01, B10 and B15.
  - **B01:** the "What I Checked" card was removed and the line enlarged, in the vertical only.
  - **B10:** portrait text was raised to Inter 68 / EB Garamond 90, the step numbers removed, and the pills wrapped.
- **Vertical overlap:** GATE T's measurements passed but a visual check caught the footnote overlapping step 06. The portrait side note was dropped to fit the title-safe box; B05's narration keeps that point.
- **Vertical underfill:** Gate V then flagged underfill on B01 (19%) and B13 (51%). Both got documented `qc.sparse_by_design` waivers.

**Vertical B15 locked-outro exception.**
- GATE T still fails on B15, because `ClaudeTitleOutro916`'s "@NikBearBrown" handle measures 49 px against the 72 px floor.
- The component is locked (OUTRO-LOCK.md) and Prarthana isn't permitted to modify it.
- With her approval, the vertical was exported by direct `compile.py`. Gate V still ran on the candidate, and the file was accepted after a phone-width by-eye check showed the handle is readable.
- The automated vertical type gate is **not** reported as passing.

**Final exports.**
- **Landscape:** `claude-liam-medhavy-how-the-tutor-stays-grounded.mp4` (3840×2160, 167.93 s), via `./art final`, all gates passing.
- **Vertical:** `claude-liam-medhavy-how-the-tutor-stays-grounded-vertical.mp4` (2160×3840, 167.93 s), with the exception above.
- Hashes are in QC-REPORT.md.

**Handoff.**
- Prarthana uploaded both finals to Google Drive.
- Source and docs were then cleaned up locally for her manual GitHub upload.
- No git command was run by the agent, and nothing was published to YouTube.
- PM review and the professors' publication decision are pending.

**Contribution:**
- Claude Code built the wrapper and scenes, ran the renders, QC and fixes, and drafted these docs.
- Prarthana made every approval and exception decision, ran the signed-in captures, and handled the uploads.
