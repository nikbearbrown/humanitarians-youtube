# Process notes — Evaluation Layer (both cuts)

**Google Drive:** https://drive.google.com/drive/folders/1ca944LZn-m0oxm6S7Iq7rM5UrwprYLAK
**Status:** shipped-to-drive · not yet published to YouTube
**Channel:** humanitarians-ai · **Resolution:** 3840x2160 (16:9) / 2160x3840 (9:16)
**Last updated:** 2026-09-21

Build log for `work-evaluation-layer` (16:9) and `work-evaluation-layer-916` (9:16 Shorts). 

## 2026-09-21 — script → both cuts built at true 4K

**Starting point:** `beat_sheet.json` and markdown script for the Evaluation Layer.
**Rendering:** true 4K via `ART_SCALE` default (scale=2).
**QC pass:** 
- `TwoWayCompare` component used in B03 had a FILL-THE-CANVAS violation in 9:16. Modified the bounding boxes to spread the ink across more of the safe area.
**Delivered:** Both masters committed and uploaded to Drive.