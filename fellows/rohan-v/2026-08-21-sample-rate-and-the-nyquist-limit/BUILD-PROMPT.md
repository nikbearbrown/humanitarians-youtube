# BUILD-PROMPT

From the toolkit root, reel at `../hai-weekly/youtube/claude-hai-nyquist`:

```
python runtime/scripts/generate_audio_kokoro.py ../hai-weekly/youtube/claude-hai-nyquist --speed 0.95
python runtime/scripts/remotion_scenes.py ../hai-weekly/youtube/claude-hai-nyquist --force
python runtime/scripts/compile.py ../hai-weekly/youtube/claude-hai-nyquist --height 1080
python runtime/scripts/shorts.py ../hai-weekly/youtube/claude-hai-nyquist
python runtime/scripts/compile.py ../hai-weekly/youtube/claude-hai-nyquist/short --height 1920
```

Manim: render each `B0N_*` class in `scenes.py` and copy to `manim/B0N.mp4`.

Then visual QC: ffmpeg frames at 2 fps + Read PNGs. Never publish.
