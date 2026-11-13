# BUILD-PROMPT — Basketball Blaster: The Design Document Came Last

Run from the brutalist.art toolkit root. `REEL` is this folder; `GDD` is `basketball-game-godot/GDD.md`.

```bash
python3 "$REEL/make_sheet.py" author
python3 runtime/scripts/generate_audio_kokoro.py "$REEL"
python3 "$REEL/make_sheet.py" finish            # exact-frame clips, padded audio, cues, gdd-evidence.json
./art godot-gdd --check "$REEL" --gdd "$GDD"
python3 runtime/scripts/remotion_scenes.py "$REEL"
./art final "$REEL" --height 2160 --fps 30 --out "$REEL/exports/landscape"

# vertical (9:16)
./art vertical "$REEL"
python3 ../basketball-captures/make_vertical.py "$REEL"
python3 runtime/scripts/remotion_scenes.py "$REEL/vertical"
python3 ../basketball-captures/make_vertical_cards.py
./art final "$REEL/vertical" --height 3840 --fps 30 --out "$REEL/exports/vertical"
```

The takes come from `../basketball-captures/run_take.sh` (see `CAPTURE.md`).
