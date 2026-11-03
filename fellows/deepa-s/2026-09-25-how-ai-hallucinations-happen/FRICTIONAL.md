# FRICTIONAL.md — How AI Hallucinations Happen

## What I was trying to do
Explain why confident-sounding AI answers can be wrong, using the approved narration and separate native landscape/portrait scenes.

## Friction and response
After resuming the project, the build log says the existing landscape cut was preserved and only portrait B05, B04, B06, and B08 were corrected and rebuilt. The QC report describes the B05 “IF BELIEVED” callout adjustment and spacing/visibility fixes in the other listed beats. It also records remaining automated layout exceptions: landscape bottom-safe-margin and end-card-underfill flags, plus portrait B00 right-safe-margin flags. The QC report calls these nonblocking based on its sampled visual review; it explicitly does not claim the raw automated gate passed. I retain that distinction.

## Human review and status in the records
The approved narration is recorded as unchanged. `STATUS.md` and `QC-REPORT.md` still show the human watch-the-cut gate as pending, so this staged evidence does not claim a later visual approval.

## Evidence used
`BUILD-LOG.md`, `QC-REPORT.md`, `CHECKS-REPORT.md`, `STATUS.md`, `ToDo.md`, `TYPECHECK.md`, `MASTERCHECK.md`, `_qc/REPORT.md`, `vertical/_qc/REPORT.md`, `beat_sheet.json`, `vertical/beat_sheet.json`, `src/DeepaHallucinations.tsx`.

## Status clarification — recorded 2026-09-29

Deepa later watched and approved both complete cuts. The nonblocking automated safe-margin and end-card exceptions described above remain documented qualifications; human approval does not turn them into automated passes. This later approval supersedes the historical pending-review status without altering the earlier QC reports. Its exact watch-through date is not independently recorded here. No manager approval is inferred.
