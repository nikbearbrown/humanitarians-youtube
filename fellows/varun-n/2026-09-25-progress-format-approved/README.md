# Week 8: Format Approved

**Content period:** Week 8 (September 19-25, 2026)  
**Pushed to repository:** 2026-10-22  
**Format:** 4K source, 16:9 (3840x2160) and 9:16 (2160x3840) native, 30fps  
**Voice:** bm_george (Kokoro)  
**Beat sheet:** `beat_sheet.json` (this folder, landscape) / `vertical/beat_sheet.json` (portrait)  
**Video (Google Drive):** [Week 8 folder](https://drive.google.com/drive/folders/1dMw7_uXmNP45qJi-Gg6mowrQaZ55w50T?usp=drive_link)

## What This Video Covers

I fixed captions (18 to 15 pt, and a switch from Open Sans to PT Sans after tracing in-word gaps to Manim and Pango) and upscaled a supplied "4K" outro that was really 478x850. Faculty reviewers assigned me maintenance of the Medhavy AI YouTube channel; I unlisted about ten non-explainer videos. The format was approved on September 25. A GPU test showed NVENC encoding about 2x faster but Manim OpenGL about 23% slower than Cairo, so the renderer was not switched.

**Takeaway:** Check media with ffprobe, not filenames: a file labeled 4K can be 478 pixels wide.
