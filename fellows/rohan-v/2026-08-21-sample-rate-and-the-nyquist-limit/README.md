# Sample Rate and the Nyquist Limit

**Fellow:** Rohan Vijaykumar (Lyrical Literacy)
**Week ending:** 2026-08-21
**Brand:** `claude-hai` · Kokoro `af_bella` · `@HumanitariansAI`

A teaching explainer: sampling as snapshots, Nyquist as sample-rate/2, and aliasing when a high pitch is stored as a fake low one. Upsampling does not restore missing cycles.

Rebuild from [brutalist.art](https://github.com/nikbearbrown/brutalist.art). Start with `beat_sheet.json` and `scenes.py`. No MP4 or MP3 in this folder.

```bash
python3 runtime/scripts/generate_audio_kokoro.py /absolute/path/to/this/folder --speed 0.95
python3 runtime/scripts/remotion_scenes.py /absolute/path/to/this/folder
# render Manim classes in scenes.py → manim/B0N.mp4
python3 runtime/scripts/compile.py /absolute/path/to/this/folder --height 1080
```
