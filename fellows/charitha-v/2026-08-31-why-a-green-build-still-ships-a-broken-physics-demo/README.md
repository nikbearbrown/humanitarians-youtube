# Why a green build still ships a broken physics demo

**Fellow:** Charitha Sree Veluru · **Date:** August 31, 2026 · **Folder:** `2026-08-31-why-a-green-build-still-ships-a-broken-physics-demo`  
**Series:** Humanitarians AI Fellows — Physics Vol. 1 · **Voice:** Kokoro `af_bella` (pending approval)

> Canvas embeds with Play + drag beat green builds that still ship unusable physics demos.

## Masters (Drive — not in git)

| File | Aspect |
|------|--------|
| `physics_vol_1_ch4_Charitha_Sree_Veluru_video1_16x9.mp4` | 16:9 · 4K |
| `physics_vol_1_ch4_Charitha_Sree_Veluru_video1_9x16.mp4` | 9:16 · 4K |

Replace Drive link after upload: *[▶ Watch on Google Drive](https://drive.google.com/…)*

## Files

| File | What it is |
|------|------------|
| `beat_sheet.json` | Narration + shot plan (brutalist.art) |
| `SOURCES.md` | Provenance |
| `FACTCHECK.md` | Claim audit stub |
| `../video-pipeline/` | Regeneratable Playwright/ffmpeg builder (`build_videos.py`) |

## Rebuild

**Beat-sheet / Kokoro path**

```bash
git clone https://github.com/nikbearbrown/brutalist.art.git
cd brutalist.art && ./setup --install && ./setup
```

**Screen-capture path**

```bash
cd ../video-pipeline
source .venv/bin/activate
VIDEO_TTS=edge python build_videos.py
```

Physics Vol. 1 embeds must be live on `http://localhost:3002` (or `VIDEO_BASE_URL`).

## Beat map

| Beat | Act | Lane | Est |
|------|-----|------|-----|
| B00 | COLD OPEN | REMOTION | 8s |
| B01 | CLAIM | REMOTION | 16s |
| B02 | CONTRAST | VOX | 34s |
| B03 | WHY | REMOTION | 24s |
| B04 | SHOW | VOX | 30s |
| B05 | YOUR TURN | VOX | 16s |
| BOUT | OUTRO | REMOTION | 6s |

