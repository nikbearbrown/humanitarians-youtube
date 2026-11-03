# BUILD-PROMPT — Fantasy Survival Crafting: The Design Document Came Last

```bash
python3 "$REEL/make_sheet.py" author
python3 runtime/scripts/generate_audio_kokoro.py "$REEL"
python3 "$REEL/make_sheet.py" finish
./art godot-gdd --check "$REEL" --gdd "<game>/submission/GDD.md"
python3 runtime/scripts/remotion_scenes.py "$REEL"
./art final "$REEL" --height 2160 --fps 30 --out "$REEL/exports/landscape"
./art vertical "$REEL" && python3 ../fantasy-captures/make_vertical.py "$REEL"
python3 ../fantasy-captures/make_vertical_cards.py
python3 runtime/scripts/remotion_scenes.py "$REEL/vertical"      # writer, composer, outro only
./art final "$REEL/vertical" --height 3840 --fps 30 --out "$REEL/exports/vertical"
```

The takes come from `../fantasy-captures/record_all.sh` (see `CAPTURE.md`).
