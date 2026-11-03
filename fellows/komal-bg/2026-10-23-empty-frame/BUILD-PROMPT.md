# BUILD-PROMPT.md — The Empty Frame.

Paste-ready rebuild. Never publishes.

```bash
export ART_HOME=/Users/komalganapathy/Desktop/brutalist.art
REEL="/Users/komalganapathy/Desktop/humanitarians-youtube/fellows/komal-bg/2026-10-23-empty-frame"
cd "$ART_HOME"

.venv/bin/python runtime/scripts/generate_audio_kokoro.py "$REEL"
.venv/bin/python runtime/scripts/remotion_scenes.py "$REEL" --force
.venv/bin/python runtime/scripts/compile.py "$REEL" --height 2160 --out "$REEL"
.venv/bin/python runtime/scripts/shorts.py "$REEL" --vertical
# shorts.py copies landscape output_height (2160); portrait master is 3840
python3 -c 'import json,pathlib,sys; p=pathlib.Path(sys.argv[1]); s=json.loads(p.read_text()); s["metadata"]["output_height"]=3840; p.write_text(json.dumps(s, indent=2, ensure_ascii=False)+"\n")' "$REEL/vertical/beat_sheet.json"
# portrait stills already in pantry/B02-916.png B03-916.png B05-916.png
.venv/bin/python runtime/scripts/remotion_scenes.py "$REEL/vertical" --force
.venv/bin/python runtime/scripts/compile.py "$REEL/vertical" --height 3840 --out "$REEL/vertical"
cp "$REEL/vertical/claude-liam-empty-frame-vertical.mp4" "$REEL/claude-liam-empty-frame-vertical.mp4"
```

Locks: Liam in for Komal · Kokoro `am_onyx` · `keep_review_labels: false` · greeting `Vanakkam, Liam` · Liam spoken LEE-um.
Portrait Remotion: `*916` twins. Stills: `pantry/B0X-916.png`. Outro `OwnedFaceOutro`.
Composer beats B00 / B07: `qc.full_bleed: true`.
