# Process notes — Tracking & Alerting (both cuts)

**Google Drive:** https://drive.google.com/drive/folders/1v0LFVRNdma-HeUjIoWLViYzKnBw5ecIq
**Status:** shipped-to-drive · not yet published to YouTube
**Channel:** humanitarians-ai · **Resolution:** 3840x2160 (16:9) / 2160x3840 (9:16)
**Last updated:** 2026-09-28

Build log for `work-tracking-alerting` (16:9) and `work-tracking-alerting-916` (9:16 Shorts). 

## 2026-09-28 — script → both cuts built at true 4K

**Starting point:** `beat_sheet.json` and markdown script for Tracking & Alerting.
**Rendering:** true 4K via `ART_SCALE` default (scale=2). 16:9 at `--height 2160`; 9:16 at `--height 3840`.
**QC pass:** 
- `ResultsTable` component had a text-overflow bug. The display flex logic caused the SQLite table visual to cramp in portrait mode. Fixed by removing flexbox and using block `div`s with explicit widths.
**Delivered:** Both masters committed and uploaded to Drive.