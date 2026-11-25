# BUILD-PROMPT — Background AI Agents: How AI Works While You Don't

Run from the brutalist.art toolkit, with `.venv/bin` on PATH.

```bash
REEL=~/Documents/AI_Content_submission/youtube/claude-hai-background-agents
python "$REEL/make_sheet.py" author
python runtime/scripts/generate_audio_kokoro.py "$REEL"
python "$REEL/make_sheet.py" finish                  # pad audio, durations
python runtime/scripts/align.py "$REEL"              # word clock → mp3/words.json
python "$REEL/make_sheet.py" finish                  # place cues on the spoken words
python runtime/scripts/remotion_scenes.py "$REEL"
./art final "$REEL" --height 2160 --fps 30 --out "$REEL/exports"
./art vertical "$REEL"                               # 9:16 sheet: every beat → its *916 composition
python runtime/scripts/remotion_scenes.py "$REEL/vertical"
./art final "$REEL/vertical" --height 3840 --fps 30 --out "$REEL/exports/vertical"
```

Then look at the frames (`_qc/`) and log what you found. Never publish.
