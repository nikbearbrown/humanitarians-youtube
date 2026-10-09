# Process notes — Semantic Normalization (both cuts)

**Google Drive:** https://drive.google.com/drive/folders/1VfQRD7kWi1mjLO2n1G0dck0f-RBlQaNv
**Status:** shipped-to-drive · not yet published to YouTube
**Channel:** humanitarians-ai · **Resolution:** 3840x2160 (16:9) / 2160x3840 (9:16)
**Last updated:** 2026-10-09

Build log for `work-semantic-normalization` (16:9) and `work-semantic-normalization-916` (9:16 Shorts). 

## 2026-10-09 — script → both cuts built at true 4K

**Starting point:** `beat_sheet.json` and markdown script for Semantic Normalization & Regex Parsing.
**Rendering:** true 4K via `ART_SCALE` default (scale=2). 16:9 at `--height 2160`; 9:16 at `--height 3840`.
**QC pass:** 
- The Python regex code block was overflowing the safe zone in the 9:16 portrait render. Fixed by wrapping the regex pattern to a new line and reducing the font weight of the syntax highlighting.
**Delivered:** Both masters committed and uploaded to Drive.