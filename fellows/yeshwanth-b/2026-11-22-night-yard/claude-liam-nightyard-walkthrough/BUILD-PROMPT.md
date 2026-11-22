# BUILD-PROMPT — Night Yard, Every Feature, Played

```bash
python3 "$REEL/make_sheet.py" author
python3 runtime/scripts/generate_audio_kokoro.py "$REEL"
python3 "$REEL/make_sheet.py" finish
./art godot-waikthrough --check "$REEL"
python3 runtime/scripts/remotion_scenes.py "$REEL"
python3 ../inside-captures/shotlist.py "$REEL" "Night Yard, Every Feature, Played"
./art final "$REEL" --height 2160 --fps 30 --out "$REEL/exports"
PY=.venv/bin/python bash ../inside-captures/make_vertical_all.sh walkthrough
```
