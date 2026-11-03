# PROMPTS.md — one-run-still-open (GATE F)

The command sequence used to build this revision. `python3` is shimmed to the real interpreter
(this machine's `python3` is a Microsoft Store alias).

```bash
export PATH="/c/ffmpeg:$PATH" PYTHONUTF8=1
TOOLKIT=/c/Users/divij/Desktop/mycroft/brutalist.art
REEL="D:/Code/humanitarians-youtube/fellows/divij-pawar/Mycroft9_DivijPawar_09-25-2026_one-run-still-open"
python assets/evidence/m9_evidence.py                      # evidence JSON (read-only against verification-layer)
python ../Mycroft8_DivijPawar_09-18-2026_the-rule-that-lost/build_sheets.py   # beat sheet from narration_v4 + visual_v4
python3 "$TOOLKIT/runtime/scripts/generate_audio_kokoro.py" "$REEL"           # am_onyx, durations = ground truth
# scenes.py reads each TARGET from beat_sheet.json actual_duration_s: no manual retiming step
while read bid cls; do python3 -m manim render -qk --fps 30 scenes.py "$cls" -o "$bid.mp4" < /dev/null \
  && cp "media/videos/scenes/2160p30/$bid.mp4" "manim/$bid.mp4"; done < _qc/scene_map_lf.txt
python3 "$TOOLKIT/runtime/scripts/remotion_scenes.py" "$REEL" --only B00 --force
python3 "$TOOLKIT/runtime/scripts/remotion_scenes.py" "$REEL" --only B20 --force
python3 "$TOOLKIT/runtime/scripts/compile.py" "$REEL" --height 2160 --fps 30
python3 "$TOOLKIT/runtime/scripts/shorts.py" "$REEL" --vertical --output-dir "$REEL/short"
```
