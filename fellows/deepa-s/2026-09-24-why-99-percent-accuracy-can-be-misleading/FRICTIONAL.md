# FRICTIONAL.md — Accuracy 99 Percent

## What I was trying to do
Turn the approved accuracy example into a two-format explainer with beat-level narration and an animated accuracy/recall comparison.

## Friction and response
The build log records that FFmpeg was not initially available on `PATH`; narration generation completed using Remotion's bundled executables after setting their dynamic-library path. The bundled FFmpeg lacked the expected `volumedetect` and raw PCM options, so audio checks used supported decoding and Python PCM measurements instead. The required 0.8-second lead was added once during review-WAV preparation. The scene implementation also records a word-level wording correction (“reveals” to “can hide”) without regenerating the approved narration.

The automated records are not fully aligned: `_qc/REPORT.md` reports sampled visual frames with no blockers or major defects, while `CHECKS-REPORT.md` says visual appearance was not checked and the watch-the-cut gate was pending. `TYPECHECK.md` reports minimum-size failures in B01 and B05, with no overflow or overlap failures. I preserve those qualifications rather than treating all visual checks as passed. The project records do not explain specific reviewer-master corrections, so I do not attribute particular edits to reviewer feedback.

## Human review and status in the records
`CHECKS-REPORT.md` records narration approval, but also leaves the human watch-the-cut gate pending. The staged project records no later cut approval.

## Evidence used
`BUILD-LOG.md`, `BUILD-PROMPT.md`, `AUDIO-REVIEW.md`, `CHECKS-REPORT.md`, `TYPECHECK.md`, `_qc/REPORT.md`, `vertical/_qc/REPORT.md`, `beat_sheet.json`, `vertical/beat_sheet.json`, `src/DeepaAccuracy.tsx`.

## Status clarification — recorded 2026-09-29

Deepa's later review handoff confirms approval of both corrected cuts. The corrections addressed the visible debug/footer text, instructional narration-credit overlay, and portrait opening/title overlap across the two versions. The accepted minimum-text-size lint exception remains an exception; the corrected cuts were reported with zero overlap and zero overflow. Earlier QC reports remain historical and are not rewritten as post-correction results. The date of the later human watch-through is not independently recorded here. No manager approval is inferred.
