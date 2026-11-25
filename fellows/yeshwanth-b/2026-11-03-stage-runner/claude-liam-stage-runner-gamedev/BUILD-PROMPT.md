# BUILD-PROMPT — Stage Runner: Inside the Godot Code

```bash
python3 "$REEL/make_sheet.py" author
python3 runtime/scripts/generate_audio_kokoro.py "$REEL"
python3 "$REEL/make_sheet.py" finish
python3 runtime/scripts/remotion_scenes.py "$REEL"
python3 "$REEL/make_sheet.py" ledger
./art godot-gamedev --check "$REEL" --game ../../stage-runner-godot-completed
python3 ../stage-runner-captures/shotlist.py "$REEL" "Stage Runner: Inside the Godot Code"
./art final "$REEL" --height 2160 --fps 30 --out "$REEL/exports"
PY=.venv/bin/python bash ../stage-runner-captures/make_vertical_all.sh gamedev
```
