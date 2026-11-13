# BUILD-PROMPT.md — The Agent's Cart.

Paste-ready rebuild. Never publishes.

```bash
export ART_HOME=/Users/komalganapathy/Desktop/brutalist.art
REEL="/Users/komalganapathy/Desktop/humanitarians-youtube/fellows/komal-bg/2026-10-03-agentic-commerce"
cd "$ART_HOME"
./setup --install   # first time only

.venv/bin/python runtime/scripts/generate_audio_kokoro.py "$REEL"
.venv/bin/python runtime/scripts/remotion_scenes.py "$REEL" --force
.venv/bin/python runtime/scripts/compile.py "$REEL" --height 2160 --out "$REEL"
.venv/bin/python runtime/scripts/shorts.py "$REEL" --vertical
.venv/bin/python runtime/scripts/remotion_scenes.py "$REEL/vertical" --force
.venv/bin/python runtime/scripts/compile.py "$REEL/vertical" --height 3840 --out "$REEL/vertical"
cp "$REEL/vertical/claude-liam-agentic-commerce-vertical.mp4" "$REEL/claude-liam-agentic-commerce-vertical.mp4"
```

Locks: Liam in for Komal · Kokoro `am_onyx` · `keep_review_labels: false` · greeting `Ciao, Liam` · Liam spoken LEE-um.
Portrait compositions: `*916` twins. Outro is `OwnedFaceOutro` (Komal handle), not `@NikBearBrown`.
Composer beats B00 / B07: `qc.full_bleed: true` for 9:16 Gate V.
