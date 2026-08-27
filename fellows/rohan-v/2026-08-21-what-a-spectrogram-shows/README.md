# What a Spectrogram Shows

**Fellow:** Rohan Vijaykumar (Lyrical Literacy)
**Week ending:** 2026-08-21
**Brand:** `claude-hai` · Kokoro `af_bella` · `@HumanitariansAI`

A teaching explainer: a spectrogram is a map of energy over time and frequency — what it shows, the STFT window trade, and what it hides (phase, overlap, the floor).

Rebuild from [brutalist.art](https://github.com/nikbearbrown/brutalist.art). Start with `beat_sheet.json` and `scenes.py`. No MP4 or MP3 in this folder.

```bash
python3 runtime/scripts/generate_audio_kokoro.py /absolute/path/to/this/folder --speed 0.95
python3 runtime/scripts/remotion_scenes.py /absolute/path/to/this/folder
# render Manim classes in scenes.py → manim/B0N.mp4
python3 runtime/scripts/compile.py /absolute/path/to/this/folder --height 1080
# 4K: ART_REMOTION_SCALE=2 remotion_scenes.py --force; Manim 3840x2160; compile --height 2160
# 9:16: shorts.py then remotion + compile --height 1920 (or 3840 for 4K)
```
