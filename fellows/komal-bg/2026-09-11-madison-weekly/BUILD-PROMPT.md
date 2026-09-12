# BUILD-PROMPT — Madison Weekly — Sep 11.

```bash
export ART_HOME=/Users/komalganapathy/Desktop/brutalist.art
REEL="$ART_HOME/renders/madison-weekly-0911"
.venv/bin/python runtime/scripts/generate_audio_kokoro.py "$REEL"
.venv/bin/python runtime/scripts/remotion_scenes.py "$REEL" --force
.venv/bin/python runtime/scripts/compile.py "$REEL" --height 2160
./art vertical "$REEL"
.venv/bin/python runtime/scripts/remotion_scenes.py "$REEL/vertical" --force
.venv/bin/python runtime/scripts/compile.py "$REEL/vertical" --height 3840
```

Never publish. 4K 16:9 and 9:16. No beat labels.
