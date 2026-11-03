# Process notes — Adversarial Inputs (both cuts)

**Google Drive:** https://drive.google.com/drive/folders/1_bWt6YL_60tla5wehpZKKgOwUW3IJcSc
**Status:** shipped-to-drive · not yet published to YouTube
**Channel:** humanitarians-ai · **Resolution:** 3840x2160 (16:9) / 2160x3840 (9:16)
**Last updated:** 2026-10-02

Build log for `stem-adversarial-inputs` (16:9) and `stem-adversarial-inputs-916` (9:16 Shorts). 

## 2026-10-02 — script → both cuts built at true 4K

**Starting point:** `beat_sheet.json` and markdown script for Adversarial Inputs & System Stability.
**Rendering:** true 4K via `ART_SCALE` default (scale=2). 16:9 at `--height 2160`; 9:16 at `--height 3840`.
**QC pass:** 
- The `DROP TABLE logs;` text injection block was slightly too wide for the portrait mode safe zones and intersected with the UI overlay. Fixed by adding a carriage return in the text component rendering.
**Delivered:** Both masters committed and uploaded to Drive.