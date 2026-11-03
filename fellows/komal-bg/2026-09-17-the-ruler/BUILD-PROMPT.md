# BUILD-PROMPT.md — The Ruler.

Paste-ready rebuild. Never publishes.

```bash
export ART_HOME=/Users/komalganapathy/Desktop/brutalist.art
REEL="/Users/komalganapathy/Desktop/humanitarians-youtube/fellows/komal-bg/2026-09-17-the-ruler"
cd "$ART_HOME"
./setup --install   # first time only

# 1. Narration is the clock
.venv/bin/python runtime/scripts/generate_audio_kokoro.py "$REEL"

# 2. Fill Remotion slots (4K via --scale=2)
.venv/bin/python runtime/scripts/remotion_scenes.py "$REEL" --force

# 3. Clean 16:9 4K master (no beat chips)
./art final "$REEL" --height 2160 --out "$REEL"

# 4. Full-length 9:16 companion (not a crop)
.venv/bin/python runtime/scripts/shorts.py "$REEL" --vertical
.venv/bin/python runtime/scripts/remotion_scenes.py "$REEL/vertical" --force
.venv/bin/python runtime/scripts/compile.py "$REEL/vertical" --height 3840
```

Locks: Liam in for Komal · Kokoro `am_onyx` · `keep_review_labels: false` · greeting `Olá, Liam`.
Portrait compositions: `*916` twins. Outro is `TheRulerOutro` (Komal handle), not `@NikBearBrown`.
