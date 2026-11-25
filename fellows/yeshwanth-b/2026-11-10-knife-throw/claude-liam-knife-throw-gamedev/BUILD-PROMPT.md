# BUILD-PROMPT — Gino: Knife Throw, Inside the Godot Code

```bash
python3 "$REEL/make_sheet.py" author
python3 runtime/scripts/generate_audio_kokoro.py "$REEL"
python3 "$REEL/make_sheet.py" finish
python3 runtime/scripts/remotion_scenes.py "$REEL"
python3 "$REEL/make_sheet.py" ledger
./art godot-gamedev --check "$REEL" --game ../../knife-throw-platformer-godot-completed
python3 ../knife-throw-captures/shotlist.py "$REEL" "Gino: Knife Throw, Inside the Godot Code"
./art final "$REEL" --height 2160 --fps 30 --out "$REEL/exports"
PY=.venv/bin/python bash ../knife-throw-captures/make_vertical_all.sh gamedev
```
