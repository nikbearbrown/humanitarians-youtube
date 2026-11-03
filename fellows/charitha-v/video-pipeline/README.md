# Video pipeline — Physics Vol. 1 explainers

Regeneratable **screen capture + voiceover** builders for Charitha’s fellows videos.

Masters are **not** stored here. Run locally; upload MP4s to Google Drive; link from episode READMEs.

## Builders

| Script | Videos | Cards |
|--------|--------|-------|
| `build_videos.py` | Ch. 4 pair (Aug 31) | `brutalist-title-cards.html` |
| `build_videos_bookwide.py` | Agents + book-wide (Sep 7) | `brutalist-title-cards-bookwide.html` |

### Chapter 4 outputs

- `physics_vol_1_ch4_Charitha_Sree_Veluru_video{1,2}_{16x9\|9x16}.mp4`

Titles: *Why a green build still ships a broken physics demo* · *Why putting the simulation at the bottom breaks the lesson*

### Book-wide outputs

- `physics_vol_1_bookwide_Charitha_Sree_Veluru_video{1,2}_{16x9\|9x16}.mp4`

Titles: *Why one agent can't polish seventeen physics chapters* · *What shipped when Chapter 4's sim contract went book-wide*

## Supporting files

| File | Role |
|------|------|
| `bottom-gallery-demo.html` | Bottom-gallery contrast (Ch. 4 video 2) |
| `figure-with-sim-demo.html` / `-portrait.html` | Side-by-side layout demos |
| `agent-parallel-demo.html` | Parallel specialist agents board |
| `title-cards.html` | Legacy HAI palette (superseded for PM gate) |
| `VIDEO_SCRIPTS.md` / `STORYBOARD.md` / `VISUAL_THEME.md` | Ch. 4 scripts |
| `VIDEO_SCRIPTS_BOOKWIDE.md` / `STORYBOARD_BOOKWIDE.md` | Book-wide scripts |

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium
cp .env.example .env   # optional ELEVENLABS_API_KEY; else VIDEO_TTS=edge
```

Requires `ffmpeg` / `ffprobe` and Physics Vol. 1 serving embeds:

```bash
cd /path/to/physics-vol-1 && npm start   # default http://localhost:3002
```

## Build

```bash
VIDEO_TTS=edge python build_videos.py
VIDEO_TTS=edge python build_videos_bookwide.py
```

Outputs land in `./output/` (gitignored).

## Naming / PM gate

- Intro line: *This is Charitha Sree Veluru in for Sanjana about …*
- Template: brutalist 4K (ink / red / ochre)
- Both **16:9** and **9:16** at 4K
