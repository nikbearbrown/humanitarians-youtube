# BUILD-PROMPT — Stage Runner: The Design Document Came Last

```bash
python3 "$REEL/make_sheet.py" author
python3 runtime/scripts/generate_audio_kokoro.py "$REEL"
python3 "$REEL/make_sheet.py" finish
./art godot-gdd --check "$REEL" --gdd "$REEL/GDD.md"
python3 runtime/scripts/remotion_scenes.py "$REEL"
python3 ../stage-runner-captures/shotlist.py "$REEL" "Stage Runner: The Design Document Came Last"
./art final "$REEL" --height 2160 --fps 30 --out "$REEL/exports"
PY=.venv/bin/python bash ../stage-runner-captures/make_vertical_all.sh gdd
```
