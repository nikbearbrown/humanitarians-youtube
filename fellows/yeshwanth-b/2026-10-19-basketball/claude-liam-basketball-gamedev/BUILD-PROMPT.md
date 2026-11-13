# BUILD-PROMPT — Basketball Blaster: Inside the Godot Code

```bash
python3 "$REEL/make_sheet.py" author
python3 runtime/scripts/generate_audio_kokoro.py "$REEL"
python3 "$REEL/make_sheet.py" finish
python3 runtime/scripts/remotion_scenes.py "$REEL"
python3 "$REEL/make_sheet.py" ledger
./art godot-gamedev --check "$REEL" --game ../../basketball-game-godot-completed
./art final "$REEL" --height 2160 --fps 30 --out "$REEL/exports/landscape"
./art vertical "$REEL" && python3 ../basketball-captures/make_vertical.py "$REEL"
python3 runtime/scripts/remotion_scenes.py "$REEL/vertical"
python3 ../basketball-captures/make_vertical_cards.py
./art final "$REEL/vertical" --height 3840 --fps 30 --out "$REEL/exports/vertical"
```
