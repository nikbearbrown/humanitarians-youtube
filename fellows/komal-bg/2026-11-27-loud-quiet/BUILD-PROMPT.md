# BUILD-PROMPT — The Loud Quiet.

```bash
export ART_HOME=/Users/komalganapathy/Desktop/brutalist.art
export ART_CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
REEL="/Users/komalganapathy/Desktop/humanitarians-youtube/fellows/komal-bg/2026-11-27-loud-quiet"
cd "$ART_HOME"
"$ART_HOME/.venv/bin/python" "$REEL/assets/render_charts.py"
.venv/bin/python runtime/scripts/generate_audio_kokoro.py "$REEL"
.venv/bin/python runtime/scripts/remotion_scenes.py "$REEL" --force
.venv/bin/python runtime/scripts/compile.py "$REEL" --height 2160 --out "$REEL"
.venv/bin/python runtime/scripts/shorts.py "$REEL" --vertical
python3 -c 'import json,pathlib,sys; p=pathlib.Path(sys.argv[1]); s=json.loads(p.read_text()); s["metadata"]["output_height"]=3840; p.write_text(json.dumps(s, indent=2, ensure_ascii=False)+"\n")' "$REEL/vertical/beat_sheet.json"
.venv/bin/python runtime/scripts/remotion_scenes.py "$REEL/vertical" --force
.venv/bin/python runtime/scripts/compile.py "$REEL/vertical" --height 3840 --out "$REEL/vertical"
cp "$REEL/vertical/claude-liam-loud-quiet-vertical.mp4" "$REEL/claude-liam-loud-quiet-vertical.mp4"
```

Never publish. 4K 16:9 and 9:16. No beat labels. Liam in for Komal.
Locks: Kokoro `am_onyx` · `keep_review_labels: false` · greeting `Salut, Liam` · Liam spoken as one word via `Leeyum` in `liam.json` (no `metadata.pronounce`).
TTS: sah-loo. Outro is `OwnedFaceOutro`.
Composer beats B00 / B07: `qc.full_bleed: true`. Chart beats B02 / B03 / B04 also `qc.full_bleed`.
