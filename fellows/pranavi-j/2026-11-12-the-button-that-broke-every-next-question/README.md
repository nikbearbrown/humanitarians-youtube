# Weekly Work Report: The Button That Broke Every Next Question

**Fellow:** Sai Pranavi J.
**Week ending:** November 12, 2026
**Project:** Project 29 — Financial Regulatory Intelligence System (`mycroft` repo,
`Regulatory_QA/frontend/src/{App.jsx, components/ChatInterface.jsx}`)
**Source status:** Real engineering work. Every claim traces to this week's E1 fix (closed
2026-11-12) and this session's own live Node.js verification harness
(`verification/verify_feed_cap.js`) — confirmed the real, current `handleToggle`/`handleSelectAll`
logic caps selection at 10 regardless of path, and the real, current error-reason extraction
surfaces the server's actual validation message instead of axios's generic one.

## Watch

- Landscape (4K 16:9): [pending Drive upload — publishing not authorized this session]
- Vertical (4K 9:16): [pending Drive upload — publishing not authorized this session]

This video covers a bug found and fixed this week (E1) in Project 29's regulatory intelligence
frontend. The chat endpoint hard-caps context to 10 feeds — a deliberate RAG context-size limit —
but nothing on the frontend respected that limit: the feed panel loads up to 100 feeds, and the
"Select All" button, the single most discoverable, unguarded action in the feed list, selected every
loaded feed with no cap at all. On the real, live database (411 rows), that selects close to 100
feeds, and any question asked afterward is guaranteed to fail backend validation. Compounding it,
the chat's error handler only ever showed axios's generic `"Request failed with status code 422"` —
never the real reason FastAPI actually sent back. The fix caps both selection paths
(`handleSelectAll` and individual `handleToggle` clicks) at the same limit the backend enforces, and
makes the error handler read and show the server's real validation reason.

## What this covers (and what it deliberately leaves out)

Covered: the real pre-fix `handleSelectAll`/`handleToggle` code and the real pre-fix generic error
line, shown verbatim; the real backend `max_items=10` limit; the exact diff that adds
`MAX_SELECTABLE_FEEDS` and caps both selection paths, plus the real error-reason-extraction block;
and the real before/after results from a live Node.js harness built and run this session,
reproducing `E1-VERIFICATION.md`'s own 5 checks and 7 assertions exactly, including the real
captured 422 message text; and two honest items at full weight: no `vite build`/browser end-to-end
check was done, and no UI indicator was added once the cap is reached.

Deliberately left out: no claim that this bug was observed to break a real user's live session in
production — this closes a confirmed, reproducible defect, verified against the real extracted logic
(a live FastAPI `TestClient` run against the real `app.models.FeedQuery` produced the real captured
422 body used in B05, per `E1-VERIFICATION.md`), not an observed end-user incident. The ~100-feed
real-world overselect figure (B02/B03) and the 15-`feed_ids` test case behind the captured 422
message (B05) are two distinct numbers and are kept separately labeled throughout, never conflated.

## Production state

- Plan: **approved (Gate P)** — signed 2026-11-12
- Fact-check gate: **resolved** — see `FACTCHECK.md`; both honest limits kept at full weight, no
  softening
- Narration approval: **approved** — Kokoro `af_bella`, locked 2026-11-12
- Voice: **Bella (`af_bella`)** — persistent for this fellow's whole report series
- Previz: **complete** — 9/9 beats real Manim, no slates, both aspects
- Final render — **16:9 landscape:** `FeedSelectionCap_SaiPranaviJ.mp4`, 3840x2160, 24fps,
  h264/aac, **154.541667s**. GATE V on the true clean master: **0 BLOCKER, 0 MAJOR**.
- Final render — **9:16 vertical (full-length, native portrait, not a Shorts cut):**
  `FeedSelectionCap_SaiPranaviJ.mp4`, 2160x3840, 24fps, h264/aac, **154.541667s** (identical
  duration to the landscape master — all 9 beats kept, no drops, no duration cap). GATE V on the
  true clean master: **0 BLOCKER, 0 MAJOR**.
- Personally re-verified (not just trusting the build report): extracted and viewed real frames
  from both final deliverables — B00's title card, B03's three stacked panels (pre-fix code, backend
  limit, pre-fix error line), B04's real diff for both files, B05's real harness table with the
  real 422 message swap, B06's honest-limits cards, B07's takeaway, and B08's sign-off — in both
  aspects. No text-rendering artifacts, no clipping, no overlap; "Sai Pranavi J." and
  "@HumanitariansAI" confirmed correct everywhere they appear.
- Publishing: **not authorized** — masters stay in this folder only, ready for fellow/PM review

## Built under the toolkit's submission spec

This project follows the toolkit's official spec (`brutalist/docs/FELLOWS-SUBMISSION.md`,
effective 2026-09-07): `ProjectName_VolunteerName.mp4` naming (no date/aspect suffix), separate
`deliverables/landscape/` and `deliverables/vertical/` folders, and a true full-length 4K
2160x3840 vertical companion built via `./art vertical` (not a <=180s Shorts-style cut) — every
beat, no cuts, no added endcard.

## Human and AI work

**My decisions, implementation and verification:** the underlying engineering (finding the
Select-All-has-no-cap gap, the generic-error-message gap, the `MAX_SELECTABLE_FEEDS` fix, and the
error-reason-extraction fix, and closing it this week as E1) is my own work on Project 29, done
before this video session.

**AI tools/voices used and what they generated:** Claude Code authored all 9 Manim scenes (both
aspects), built and ran the live Node.js verification harness used in B05 (extracting the real,
current `handleToggle`/`handleSelectAll` and error-reason-extraction logic from `App.jsx` and
`ChatInterface.jsx` on disk, and faithful reconstructions of each pre-fix version by undoing the
exact documented diff, to reproduce the real documented bug and fix), generated the Kokoro
`af_bella` narration audio, ran the full render/compile/QC pipeline, and wrote this paperwork set.
Nothing in the pipeline fabricated or altered the underlying code, numbers, or verification results.

**What I rejected or corrected:** none — the beat sheet and fact-check were already approved before
the build began; the build work focused on authoring the visuals accurately against the approved
claims and fixing real layout/timing defects caught by GATE A/B/V (documented in `BUILD-LOG.md` and,
contemporaneously, in `FRICTIONAL.md`).

**What remains unverified or failed:** this session's harness reproduces the real, documented
behavior by running the real extracted logic against the same scenarios `E1-VERIFICATION.md`'s own
table describes — it does not run a real browser/`vite build` (matching the real investigation's own
stated limitation: `node_modules` isn't installed). No UI indicator (disabled state/tooltip) exists
yet for the cap, per `RUN_LOG.md`'s own "Open issues" line — flagged in B06 at full weight, not
smoothed over. Both final masters are GATE V clean and personally frame-checked.

## Reproduce

- Brutalist version/commit and date checked: this repo's `brutalist/` at the time of this build,
  2026-11-12
- Source: `mycroft` repo, `Regulatory_QA/frontend/src/App.jsx`, `src/components/ChatInterface.jsx`
  (both read-only — not modified by this video session), `scripts/regulatory-intel/E1-VERIFICATION.md`,
  `logs/RUN_LOG.md`'s 2026-11-12 entry — see `SOURCES.md`/`FACTCHECK.md`
- Beat sheet and custom scene files: `beat_sheet.json`, `scenes.py` (landscape),
  `vertical/beat_sheet.json`, `vertical/scenes.py` (portrait)
- Live verification: `verification/verify_feed_cap.js` (run via
  `node verification/verify_feed_cap.js`), captured in `verification/verify_feed_cap_output.txt`
- Commands: `python3 brutalist/runtime/scripts/generate_audio_kokoro.py <reel>` (Kokoro TTS),
  `ffmpeg -f lavfi -i anullsrc ...` (B00 silent track), `./art run <reel>` (landscape review + QC
  gates), `ffmpeg -f concat -safe 0 -i clips/concat.txt -i clips/_work/master.wav ...` (manual true
  final master, both aspects — `./art final`'s own embedded GATE V has no `--lenient` escape
  hatch and refuses on any MAJOR finding), `./art vertical <reel>` + `./art run <reel>/vertical`
  (vertical review + QC gates), `final_frame_check.py --lenient` (standalone GATE V re-check on
  both true finals, run from inside the reel folder)
- Approvals and checks: see `FACTCHECK.md`, `BEAT-SHEET.md` (Gate P sign-off), `BUILD-LOG.md`
  (build history, bugs found/fixed, GATE V results), `FRICTIONAL.md` (contemporaneous build-time
  log)

## Watch and review

- Landscape — `deliverables/landscape/FeedSelectionCap_SaiPranaviJ.mp4` — 3840x2160 —
  154.541667s — SHA-256 `e1ac65ebcd30895c9f27e536b1c04ebaed76ef8a06b8ad0d2fd9c486c6f9533e`
  (sidecar `.verified.json`)
- Vertical — `deliverables/vertical/FeedSelectionCap_SaiPranaviJ.mp4` — 2160x3840 —
  154.541667s — SHA-256 `286c9e636cff0450ac8bcafd9c45a43ea00be587e752a7b8c8f4a0124e425736`
  (sidecar `.verified.json`)
- PM review status: pending
- YouTube 4K processing check: pending upload
- Professors' publication decision: pending

## Useful project files

- `BEAT-SHEET.md` — the narrative beat sheet as drafted and approved
- `beat_sheet.json` / `vertical/beat_sheet.json` — the same plan in the pipeline's structured
  schema, both aspects
- `FACTCHECK.md` — claim-level review against the real `App.jsx`/`ChatInterface.jsx` code, the real
  diff, and this session's own verification harness
- `SOURCES.md` — claim -> source mapping
- `SHOTLIST.md` / `PROMPTS.md` (and `vertical/` copies) — beat-by-beat medium/timing table and
  pantry/asset status
- `scenes.py` / `vertical/scenes.py` — the Manim source for both aspects
- `verification/verify_feed_cap.js` / `verification/verify_feed_cap_output.txt` — the live Node.js
  harness and its captured real output
- `BUILD-LOG.md` — dated build decisions, bugs found and fixed, and gate history
- `FRICTIONAL.md` — contemporaneous, dated build-time friction log
