# Weekly Work Report: The Alert That Waited for a Second Item

**Fellow:** Sai Pranavi J.
**Week ending:** October 15, 2026
**Project:** Project 29 — Financial Regulatory Intelligence System (`mycroft` repo, `scripts/regulatory-intel/`)
**Source status:** Real engineering work. Every claim traces to `B6-VERIFICATION.md` and `workflow.dev.json`'s `Generate Email` node in the `mycroft` repo — a one-character-class bug (`newItems.length > 1` instead of `> 0`) verified live against the real extracted node code via a Node.js harness, then re-verified against the real patched file on disk.

## Watch

- Landscape (4K 16:9): [Drive link](https://drive.google.com/open?id=1aey3_Igm6LUqh6vHuR6XDtjjCYYG6I2Y)
- Vertical (4K 9:16): [Drive link](https://drive.google.com/open?id=1AAQO67ALY9U6A_XA20ZI2TAfJS0EY9YC)

This video covers a bug found and fixed this week in the alert-email path of the regulatory intelligence pipeline: the `Generate Email` node's `hasData` guard required **strictly more than one** qualifying item before it would build an alert email at all. A run with exactly **one** new high-priority/critical item — the single scenario this alert system exists to catch — fell into the empty-result branch and silently produced no alert, with no error and no log line a person would notice. The fix is a one-character-class change (`> 1` to `> 0`), verified live against the real extracted code before and after the patch, and again against the real patched file on disk.

## What this covers (and what it deliberately leaves out)

Covered: the real verbatim `hasData` guard line, the traced dead-end (the `If` node's true-output connection array is `[]`), the exact one-character-class diff, the real before/after harness table for 0/1/2 items, and two honest limits at full weight: this was caught by code review (not a live incident), and a related but separate `source_feed` compatibility gap was found and flagged, not fixed.

Deliberately left out: no claim that this bug ever caused an actual missed alert on a live run — the pipeline isn't instrumented to log per-run item counts at that granularity, and B06 states this limit explicitly rather than implying it was caught by an incident.

## Production state

- Plan: **approved (Gate P)** — signed 2026-10-15
- Fact-check gate: **resolved** — see `FACTCHECK.md`; both B06 honest limits kept at full weight, no softening
- Narration approval: **approved** — Kokoro `af_bella`, locked 2026-10-15
- Voice: **Bella (`af_bella`)** — persistent for this fellow's whole report series
- Previz: **complete** — 9/9 beats real Manim, no slates, both aspects
- Final render — **16:9 landscape:** `AlertSecondItemGate_SaiPranaviJ.mp4`, 3840x2160, 24fps, h264/aac, **123.5s**. GATE V on the true clean master: **0 BLOCKER, 0 MAJOR**.
- Final render — **9:16 vertical (full-length, native portrait, not a Shorts cut):** `AlertSecondItemGate_SaiPranaviJ.mp4`, 2160x3840, 24fps, h264/aac, **123.5s** (identical duration to the landscape master — every beat kept, nothing dropped). GATE V on the true clean master: **0 BLOCKER, 0 MAJOR**.
- Personally re-verified (not just trusting the build report): extracted and viewed real frames from both final deliverables, including B02's counter (landscape), B04's dead-end chain at both its 50% and 85% sample points (the beat whose closing caption previously landed too late), B05's full before/after table with both captions visible (the beat whose second caption previously bled past the vertical safe-area floor), and B06's honest-limits cards. No text-rendering artifacts, no clipping, no overlap in either aspect.
- Publishing: **not authorized** — masters stay in this folder only, ready for fellow/PM review

## Built under the toolkit's submission spec

This project follows the toolkit's official spec (`brutalist/docs/FELLOWS-SUBMISSION.md`, effective 2026-09-07): `ProjectName_VolunteerName.mp4` naming (no date/aspect suffix), separate `deliverables/landscape/` and `deliverables/vertical/` folders, and a true full-length 4K 2160x3840 vertical companion built via `./art vertical` (not a <=180s Shorts-style cut) — every beat, no cuts, no added endcard.

## Human and AI work

**My decisions, implementation and verification:** the underlying engineering (finding the `hasData` guard's off-by-one-class bug, the one-character-class fix, and the live Node.js verification harness run before and after the patch, then re-run against the real patched file) is my own work on Project 29, done before this video session; the facts and numbers reported here (the verbatim guard line, the diff, the 0/1/2-item before/after table) were measured in that prior session and are carried into this video unchanged.

**AI tools/voices used and what they generated:** Claude Code authored all 9 Manim scenes (both aspects), generated the Kokoro `af_bella` narration audio, ran the full render/compile/QC pipeline, and wrote this paperwork set. Nothing in the pipeline fabricated or altered the underlying code, numbers, or verification results.

**What I rejected or corrected:** none this session — the beat sheet and fact-check were already approved; the build work focused on authoring the visuals accurately against the approved claims and fixing real layout/timing/canvas-fill defects caught by GATE A/B/V (documented in `BUILD-LOG.md`).

**What remains unverified or failed:** nothing — both final masters are GATE V clean (0 BLOCKER, 0 MAJOR) and personally frame-checked.

## Reproduce

- Brutalist version/commit and date checked: this repo's `brutalist/` at the time of this build, 2026-10-15/16
- Source commit used for this export: `mycroft` repo state as documented in `SOURCES.md` (`B6-VERIFICATION.md`, `workflow.dev.json`, commit `f9eed1e`)
- Beat sheet and custom scene files: `beat_sheet.json`, `scenes.py` (landscape), `vertical/beat_sheet.json`, `vertical/scenes.py` (portrait)
- Commands: `python3 brutalist/runtime/scripts/generate_audio_kokoro.py <reel>` (Kokoro TTS), `ffmpeg -f lavfi -i anullsrc ...` (B00 silent track), `./art run <reel>` (landscape review + QC gates), `./art final <reel>` (landscape 4K master), `./art vertical <reel>` + `./art run <reel>/vertical` + `./art final <reel>/vertical --height 3840` (vertical 4K master), `final_frame_check.py --lenient` (standalone GATE V re-check on both true finals)
- Approvals and checks: see `FACTCHECK.md`, `BEAT-SHEET.md` (Gate P sign-off), `BUILD-LOG.md` (build history, bugs found/fixed, GATE V results)

## Watch and review

- Landscape — `deliverables/landscape/AlertSecondItemGate_SaiPranaviJ.mp4` — 3840x2160 — 123.5s — SHA-256 in the adjacent `.verified.json`
- Vertical — `deliverables/vertical/AlertSecondItemGate_SaiPranaviJ.mp4` — 2160x3840 — 123.5s — SHA-256 in the adjacent `.verified.json`
- PM review status: pending
- YouTube 4K processing check: pending upload
- Professors' publication decision: pending

## Useful project files

- `BEAT-SHEET.md` — the narrative beat sheet as drafted and approved
- `beat_sheet.json` / `vertical/beat_sheet.json` — the same plan in the pipeline's structured schema, both aspects
- `FACTCHECK.md` — claim-level review against `B6-VERIFICATION.md`
- `SOURCES.md` — claim -> source mapping
- `SHOTLIST.md` / `PROMPTS.md` (and `vertical/` copies) — beat-by-beat medium/timing table and pantry/asset status
- `scenes.py` / `vertical/scenes.py` — the Manim source for both aspects
- `BUILD-LOG.md` — dated build decisions, bugs found and fixed, and gate history
