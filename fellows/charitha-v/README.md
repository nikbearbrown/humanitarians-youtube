# Charitha Sree Veluru — Fellow

Humanitarians AI fellow · Physics Vol. 1 (OpenStax interactive textbook) · @HumanitariansAI

## Voice

| Field | Value |
|-------|--------|
| Engine | Kokoro (brutalist.art) / edge-tts fallback in local Playwright builder |
| Selected voice | `af_bella` |
| Policy | Persistent fellow-selected voice across weekly reports |
| Approval | **PENDING FELLOW APPROVAL** before first Kokoro audio lock |

Suggestion basis: female-coded first name → `af_*`. Stated preference overrides this.

Required PM intro pattern (spoken): *"This is Charitha Sree Veluru in for Sanjana about [topic]."*

## Folder layout

```text
fellows/charitha-v/
  README.md
  video-pipeline/          ← regeneratable builders (no MP4s)
  2026-08-31-why-a-green-build-still-ships-a-broken-physics-demo/
  2026-08-31-why-putting-the-simulation-at-the-bottom-breaks-the-lesson/
  2026-09-07-why-one-agent-cant-polish-seventeen-physics-chapters/
  2026-09-07-what-shipped-when-chapter-4s-sim-contract-went-book-wide/
```

Weekly episodes use `YYYY-MM-DD-kebab-title/`. Final masters live on **Google Drive** (not GitHub). This repo holds beat sheets + code only.

## Episodes

### Chapter 4 (Aug 31)

- [Why a green build still ships a broken physics demo](./2026-08-31-why-a-green-build-still-ships-a-broken-physics-demo/)
- [Why putting the simulation at the bottom breaks the lesson](./2026-08-31-why-putting-the-simulation-at-the-bottom-breaks-the-lesson/)

### Book-wide + agents (Sep 7)

- [Why one agent can't polish seventeen physics chapters](./2026-09-07-why-one-agent-cant-polish-seventeen-physics-chapters/)
- [What shipped when Chapter 4's sim contract went book-wide](./2026-09-07-what-shipped-when-chapter-4s-sim-contract-went-book-wide/)

## Rebuild toolkit (brutalist.art)

```bash
git clone https://github.com/nikbearbrown/brutalist.art.git
cd brutalist.art
./setup --install
./setup
```

## Local screen-capture builder

```bash
cd fellows/charitha-v/video-pipeline
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium
# physics-vol-1 on VIDEO_BASE_URL (default http://localhost:3002)

VIDEO_TTS=edge python build_videos.py            # Ch. 4 pair
VIDEO_TTS=edge python build_videos_bookwide.py   # agents + book-wide pair
```

Do not commit `.env`, `.venv/`, or `output/*.mp4`.


<!-- BEGIN BRUTALIST REBUILD GUIDE -->

# Charitha V

This folder organizes **4 video projects** built around beat sheets. Each project README explains the subject, supplies research and fact-check prompts, and documents the free local rebuild workflow.

## Rebuild toolkit

```bash
git clone https://github.com/nikbearbrown/brutalist.art.git
cd brutalist.art
./setup --install
./setup
```

Brutalist is audio-first and local: the beat sheet drives narration, measured audio becomes the clock, generated visual beats compile immediately, and unavailable media remains as labeled slates until a human fills the pantry. The human conducts, watches, fact-checks, refines, and decides whether anything is published.

## Projects in this folder

- [2026 08 31 Why A Green Build Still Ships A Broken Physics Demo](./2026-08-31-why-a-green-build-still-ships-a-broken-physics-demo/)
- [2026 08 31 Why Putting The Simulation At The Bottom Breaks The Lesson](./2026-08-31-why-putting-the-simulation-at-the-bottom-breaks-the-lesson/)
- [2026 09 07 Why One Agent Cant Polish Seventeen Physics Chapters](./2026-09-07-why-one-agent-cant-polish-seventeen-physics-chapters/)
- [2026 09 07 What Shipped When Chapter 4s Sim Contract Went Book Wide](./2026-09-07-what-shipped-when-chapter-4s-sim-contract-went-book-wide/)

<!-- END BRUTALIST REBUILD GUIDE -->
