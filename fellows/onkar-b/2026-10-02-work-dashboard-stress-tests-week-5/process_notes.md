# Process notes — Dashboard & Stress Tests (both cuts)

**Google Drive:** https://drive.google.com/drive/folders/1HKZ84Fa_kqDGmpcqE_M-YdSjtxPqEOhi
**Status:** shipped-to-drive · not yet published to YouTube
**Channel:** humanitarians-ai · **Resolution:** 3840x2160 (16:9) / 2160x3840 (9:16)
**Last updated:** 2026-10-02

Build log for `work-dashboard-stress-tests` (16:9) and `work-dashboard-stress-tests-916` (9:16 Shorts). 

## 2026-10-02 — script → both cuts built at true 4K

**Starting point:** `beat_sheet.json` and markdown script for Dashboard & Stress Tests.
**Rendering:** true 4K via `ART_SCALE` default (scale=2). 16:9 at `--height 2160`; 9:16 at `--height 3840`.
**QC pass:** 
- The raw HTML table rendered in `dashboard.py` was breaking out of the viewport in the 9:16 portrait render. Fixed by ensuring CSS `table { width: 100%; border-collapse: collapse; }` was tightly scoped and adding horizontal scroll properties to the UI wrapper.
**Delivered:** Both masters committed and uploaded to Drive.