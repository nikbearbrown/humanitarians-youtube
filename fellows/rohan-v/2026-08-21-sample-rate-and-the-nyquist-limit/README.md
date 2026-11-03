# Sample Rate and the Nyquist Limit

**Fellow:** Rohan V. (Lyrical Literacy)
**Week ending:** 2026-08-21
**Brand:** `claude-hai` · Kokoro `af_bella` · `@HumanitariansAI`

A teaching explainer: sampling as snapshots, Nyquist as sample-rate/2, and aliasing when a high pitch is stored as a fake low one. Upsampling does not restore missing cycles.

Rebuild from [brutalist.art](https://github.com/nikbearbrown/brutalist.art). Start with `beat_sheet.json` and `scenes.py`. No MP4 or MP3 in this folder.

```bash
python3 runtime/scripts/generate_audio_kokoro.py /absolute/path/to/this/folder --speed 0.95
python3 runtime/scripts/remotion_scenes.py /absolute/path/to/this/folder
# render Manim classes in scenes.py → manim/B0N.mp4
python3 runtime/scripts/compile.py /absolute/path/to/this/folder --height 1080
# 4K: ART_REMOTION_SCALE=2 remotion_scenes.py --force; Manim 3840x2160; compile --height 2160
# 9:16: shorts.py then remotion + compile --height 1920 (or 3840 for 4K)
```

## Renders

The 4K masters are in Google Drive, not in git — renders go to Drive, source and build assets stay here.

[`2026-08-21/` on Drive](https://drive.google.com/drive/folders/1N_7Plt_F1NdyE8JL-xBjWM3IEMM8hH0E) — `2026-08-21_nyquist_stem_4k_16x9.mp4` and `2026-08-21_nyquist_stem_4k_9x16.mp4`.
