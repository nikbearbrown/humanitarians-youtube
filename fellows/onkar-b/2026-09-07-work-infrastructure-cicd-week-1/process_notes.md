# Process notes — Infrastructure & CI/CD (both cuts)

**Google Drive:** https://drive.google.com/drive/folders/1WVcJvvy4fNrPXxgYmsOFLT2A5cCjKg-c
**Status:** shipped-to-drive · not yet published to YouTube
**Channel:** humanitarians-ai · **Resolution:** 3840x2160 (16:9) / 2160x3840 (9:16)
**Last updated:** 2026-09-07

Build log for `work-infrastructure` (16:9) and `work-infrastructure-916` (9:16 Shorts). Chronological; append-only going forward.

## 2026-09-07 — script → both cuts built at true 4K

**Starting point:** `beat_sheet.json` and markdown script for the Infrastructure video.
**9:16 Shorts cut designed:** B00 (cold open) → B01 (the point) → B02 (results) → B03 (verdict) → B04 (outro).
**Audio:** Generated once at full length straight into true-4K rendering. `actual_duration_s` in the beat sheet is ground truth.
**Rendering:** true 4K via `ART_SCALE` default (scale=2). 16:9 compiled at `--height 2160`; 9:16 at `--height 3840`.
**QC pass — Defect caught and fixed:** 
- `metadata.aspect` was used instead of `metadata.aspect_ratio`. Left alone this would have framed the 9:16 cut as 16:9 with no error at all. Fixed in both the master sheets and the working copies.
**Delivered:** Both masters committed and uploaded to Drive.