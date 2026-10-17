# Week 3: Captions That Froze

**Content period:** Week 3 (August 15-21, 2026)  
**Pushed to repository:** 2026-10-14  
**Format:** 4K source, 16:9 (3840x2160) and 9:16 (2160x3840) native, 30fps  
**Voice:** bm_george (Kokoro)  
**Beat sheet:** `beat_sheet.json` (this folder, landscape) / `vertical/beat_sheet.json` (portrait)  
**Video (Google Drive):** [Week 3 folder](https://drive.google.com/drive/folders/1vsn2xoy_peWtEiVNaWghNCMh95rUWOYI?usp=drive_link)

## What This Video Covers

I added a 9:16 Shorts version alongside the 16:9 long-form physics videos, rendered from one script that detects orientation from the pixel dimensions, with a portrait title card and burned-in captions. Captions froze at 0:23 and drifted out of sync because Manim's frozen-frame optimization skips updaters during long waits; the fix was frozen_frame=False plus a precomputed caption schedule.

**Takeaway:** Some bugs only show up in playback; watch the full video, not just sampled frames.
