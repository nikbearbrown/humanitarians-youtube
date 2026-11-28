# BUILD-PROMPT — Madison Weekly — Nov 27.

```bash
export ART_HOME=/Users/komalganapathy/Desktop/brutalist.art
export ART_CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
REEL="/Users/komalganapathy/Desktop/humanitarians-youtube/fellows/komal-bg/2026-11-27-madison-weekly"
cd "$ART_HOME"
"$ART_HOME/.venv/bin/python" "$REEL/assets/render_plates.py"
.venv/bin/python runtime/scripts/generate_audio_kokoro.py "$REEL"
.venv/bin/python runtime/scripts/remotion_scenes.py "$REEL" --force
.venv/bin/python runtime/scripts/compile.py "$REEL" --height 2160 --out "$REEL"
.venv/bin/python runtime/scripts/shorts.py "$REEL" --vertical
python3 -c 'import json,pathlib,sys; p=pathlib.Path(sys.argv[1]); s=json.loads(p.read_text()); s["metadata"]["output_height"]=3840; p.write_text(json.dumps(s, indent=2, ensure_ascii=False)+"\n")' "$REEL/vertical/beat_sheet.json"
.venv/bin/python runtime/scripts/remotion_scenes.py "$REEL/vertical" --force
.venv/bin/python runtime/scripts/compile.py "$REEL/vertical" --height 3840 --out "$REEL/vertical"
cp "$REEL/vertical/madison-weekly-nov-27-vertical.mp4" "$REEL/madison-weekly-nov-27-vertical.mp4"
```

Never publish. 4K 16:9 and 9:16. No beat labels. Liam in for Komal.
Locks: Kokoro `am_onyx` · `keep_review_labels: false` · greeting `Namaste, Liam` · Liam spoken as one word (`liam.json` Liam-after-stop + IPA `lˈiəm`; never Lay-um; no `metadata.pronounce`).
TTS: nah mah stay; Hype Auditor; Modash; Creator I Q; Twai bot twenty. Outro is `OwnedFaceOutro`.
Composer beats B00 / B07: `qc.full_bleed: true`. Chart beats B02 / B03 / B04 also `qc.full_bleed`.
No teammate names.
