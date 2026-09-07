# Why one agent can't polish seventeen physics chapters

**Fellow:** Charitha Sree Veluru · **Date:** September 7, 2026 · **Folder:** `2026-09-07-why-one-agent-cant-polish-seventeen-physics-chapters`  
**Series:** Humanitarians AI Fellows — Physics Vol. 1 · **Voice:** Kokoro `af_bella` (pending approval)

> Parallel specialist Cursor agents — one chapter each — beat one mega-agent on textbook sim quality.

## Masters (Drive — not in git)

| File | Aspect |
|------|--------|
| `physics_vol_1_bookwide_Charitha_Sree_Veluru_video{N}_16x9.mp4` | 16:9 · 4K |
| `physics_vol_1_bookwide_Charitha_Sree_Veluru_video{N}_9x16.mp4` | 9:16 · 4K |

Replace Drive link after upload: *[▶ Watch on Google Drive](https://drive.google.com/…)*

## Files

| File | What it is |
|------|------------|
| `beat_sheet.json` | Narration + shot plan (brutalist.art) |
| `SOURCES.md` | Provenance |
| `FACTCHECK.md` | Claim audit stub |
| `../video-pipeline/` | Regeneratable Playwright/ffmpeg builder |

## Rebuild

**Beat-sheet / Kokoro path**

```bash
git clone https://github.com/nikbearbrown/brutalist.art.git
cd brutalist.art && ./setup --install && ./setup
# point at this folder's beat_sheet.json
```

**Screen-capture path (same VO structure)**

```bash
cd ../video-pipeline
source .venv/bin/activate   # see pipeline README
VIDEO_TTS=edge python build_videos_bookwide.py
```

Physics Vol. 1 embeds must be live on `http://localhost:3002` (or `VIDEO_BASE_URL`).

## Beat map

| Beat | Act | Lane | Est |
|------|-----|------|-----|
| B00 | COLD OPEN | REMOTION | 8s |
| B01 | HOOK | REMOTION | 8s |
| B02 | CLAIM | REMOTION | 8s |
| B03 | CONTRAST | VOX | 34s |
| B04 | WHY | REMOTION | 24s |
| B05 | SHOW | VOX | 28s |
| B06 | YOUR TURN | VOX | 15s |
| BOUT | OUTRO | REMOTION | 6s |
