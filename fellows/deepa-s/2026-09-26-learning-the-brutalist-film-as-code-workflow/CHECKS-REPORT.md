# Checks report — human watch-the-cut gate

## Visual and layout

- 18 native beat layouts audited: PASS.
- 9 portrait compositions were authored with portrait-specific layout rules; the portrait cut is not a landscape crop.
- Typography and safe-area audit: PASS; no text overflow or text outside the 5% frame inset across the 18 scene layouts.
- Contact sheets and compiled-cut frames inspected; earlier overlap findings in the portrait Beat Sheet and QC scenes were corrected before final rendering.
- Branding, title treatment, HAI handle, disclosure, and HAI outro are present.

## Audio

- Approved narration WAV and all 18 landscape/portrait beat audio copies match their SHA-256 integrity record. Narration was not regenerated or changed.
- Both master cuts: loudness QC PASS at −24.23 LUFS integrated and −6.22 dBTP.
- All nine beat audio files decode and pass per-beat silence checks.

## Technical masters and full decode

- Landscape: `LearningBrutalistFilmAsCodeWorkflow_DeepaShenoy-slate.mp4` — 3840×2160, H.264/yuv420p, 24 fps, 84.542 seconds; AAC audio. Master check PASS; complete FFmpeg `-xerror` decode PASS.
- Portrait: `vertical/LearningBrutalistFilmAsCodeWorkflow_DeepaShenoy-slate.mp4` — 2160×3840, H.264/yuv420p, 24 fps, 84.542 seconds; AAC audio. Master check PASS; complete FFmpeg `-xerror` decode PASS.
- Both review cuts are complete and await Deepa’s human watch-the-cut review. No submission packaging, upload, or publication was performed.

Machine-readable layout data: `_qc/dom-layout.json`; contact sheets: `_qc/contact_sheet.png` and `qc-sheet.png` (landscape), plus `vertical/qc-sheet.png`; audio measurements: `audio-review/audio-checks.json`.
