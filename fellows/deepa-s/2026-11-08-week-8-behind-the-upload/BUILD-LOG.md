# Build log

## 2026-11-08

Prepared original script and planned scenes. Reusing the series am_onyx voice, Montserrat OFL fonts, HAI branding and measured sentence-cue workflow. All figures/illustrations will be original code graphics. No new human review or publication is claimed.

## 2026-11-08 — Production execution

- Generated per-sentence cached Kokoro WAVs, per-scene WAVs, full narration and measured sentence captions.
- Compiled both Remotion compositions and rendered scene/final-frame previews.
- Corrected title-safe positioning; archived pre-correction exports locally and started corrected H.264/AAC exports.
- TypeScript compiler, JSON parsing, timing checks, toolkit Beat Sheet lint and project schema validation passed. Final measured export results are maintained in QC.md.

## 2026-11-09 — Final technical validation reconciliation

Both corrected exports completed and passed full decode, measured duration/frame rate/dimensions, scene-wise audio correlation, loudness/peak, caption-layout and motion checks. Final-frame Gate V passed in both orientations. Exact measured values and SHA-256 hashes are in QC.md. Human review remains pending. No commit, push, upload or publication was performed.

## 2026-11-09 — Packaging reconciliation

Resumed from existing files: both render/QC queues had exited successfully. SHA-256 verification and fresh ffprobe checks confirmed all final files match the earlier passing QC evidence; no renders or narration were regenerated. Project-local .gitignore rules now exclude node_modules/ and generated media/QC caches without deleting them. Narration scripts and caption text were checked against the Beat Sheets.

## Approved redesign continuation — Approved redesign render

Original active MP4s, source and QC documents were copied to _qc/pre-redesign/ before changes. All 31 scenes were implemented with the approved warm editorial environments. TypeScript and all scene previews in both layouts passed checks before starting eight candidate renders under _qc/redesigned-final/. Narration was reused, not regenerated.

## 2026-11-10 — Redesign continuation and closure

The interrupted render/QC jobs had completed successfully. Existing files were reused, not rerendered. Hash checks tied the eight-video set to completed technical QC; encoded scene samples and endings were inspected. Validated copies were promoted to the documented final paths. Original exports remain intact in _qc/pre-redesign/ until Deepa approves all eight redesigned videos. Narration, captions, citations and scene clocks are unchanged. Final human review remains pending; no remote Git operation or upload was performed.
