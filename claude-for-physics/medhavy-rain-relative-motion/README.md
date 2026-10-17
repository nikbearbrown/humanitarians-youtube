# Why Does Rain Hit You From The Front?

Vertically falling rain appears slanted toward a walking observer because velocities add across reference frames.

**Source:** Physics Volume 1, Chapter 4: Motion in Two and Three Dimensions, Section 4.5 Relative Motion in One and Two Dimensions
**Working title:** Rain Hits You From the Front (Even When It Falls Straight Down)
**Persona:** MEDHAVY · **Voice:** Kokoro `am_michael` at 0.85x · **Palette:** medhavy (Okabe-Ito, white background)

## Video

Rendered videos are not stored in this repository.

- YouTube Short: https://www.youtube.com/shorts/MBVrHeQRKJE
- Google Drive: https://drive.google.com/file/d/1mbJ6Zaw_sVVHgkHLpmYEkrxsHPKDRytK/view?usp=drive_link

| Cut | File | Resolution | Runtime |
|---|---|---|---:|
| 16:9 long-form | `rain-relative-motion.mp4` | 3840x2160 | 1:02 |
| 9:16 short | `rain-relative-motion-short.mp4` | 2160x3840 | 1:24 |

## Files

- `rain_relative_motion.py` — single Manim scene (`RainRelativeMotion`) that renders both orientations. Portrait adds the opening question card and burned-in captions.
- `beat_sheet.json` — narration, visual intent and measured duration for each beat. `B00Q` is the opening question and is used only in the short.
- `PEDAGOGY.md` — Gate P review (VERDICT: PASS), required before audio generation.

## Rebuild

Requirements: Manim Community, ffmpeg, the PT Sans font, and the [brutalist.art](https://github.com/nikbearbrown/brutalist.art) toolkit for Kokoro narration.

```bash
# 1. Narration (voice comes from the beat sheet; writes mp3/beat-<ID>.mp3)
python <brutalist.art>/runtime/scripts/generate_audio_kokoro.py . --speed 0.85

# 2. Render
manim -qh rain_relative_motion.py RainRelativeMotion                                        # 16:9, no captions
manim -r 1080,1920 --fps 60 --disable_caching rain_relative_motion.py RainRelativeMotion    # 9:16, question card + captions

# 3. Mux narration (long: B00..B04, short: B00Q + B00..B04), then upscale to 4K
ffmpeg -i <render>.mp4 -vf "scale=3840:2160:flags=lanczos" -c:v libx264 -crf 16 -preset slow <slug>.mp4
ffmpeg -i <render>.mp4 -vf "scale=2160:3840:flags=lanczos" -c:v libx264 -crf 16 -preset slow content_4k.mp4

# 4. Short only: crossfade studio intro + content + studio outro (0.6s xfade/acrossfade at each seam)
```

The studio intro and outro clips are brand assets kept on Drive, not in this repository.
