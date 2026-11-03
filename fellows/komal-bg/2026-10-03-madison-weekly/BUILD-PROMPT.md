# BUILD-PROMPT — Madison Weekly — Oct 3.

```bash
export ART_HOME=/Users/komalganapathy/Desktop/brutalist.art
REEL="/Users/komalganapathy/Desktop/humanitarians-youtube/fellows/komal-bg/2026-10-03-madison-weekly"
cd "$ART_HOME"
.venv/bin/python runtime/scripts/generate_audio_kokoro.py "$REEL"
.venv/bin/python runtime/scripts/remotion_scenes.py "$REEL" --force
.venv/bin/python runtime/scripts/compile.py "$REEL" --height 2160 --out "$REEL"
.venv/bin/python runtime/scripts/shorts.py "$REEL" --vertical
.venv/bin/python runtime/scripts/remotion_scenes.py "$REEL/vertical" --force
.venv/bin/python runtime/scripts/compile.py "$REEL/vertical" --height 3840 --out "$REEL/vertical"
cp "$REEL/vertical/madison-weekly-oct-3-vertical.mp4" "$REEL/madison-weekly-oct-3-vertical.mp4"
```

Never publish. 4K 16:9 and 9:16. No beat labels. Liam in for Komal.
Locks: Kokoro `am_onyx` · `keep_review_labels: false` · greeting `Vanakkam, Liam` · Liam spoken LEE-um.
Outro is `OwnedFaceOutro` (Komal handle), not `@NikBearBrown`.
Composer beats B00 / B07: `qc.full_bleed: true` for 9:16 Gate V.
