# What Really Stops A Sliding Puck?

An object in motion stays in motion unless a net force acts; friction is what stops everyday objects.

**Source:** Physics Volume 1, Chapter 5: Newton's Laws of Motion, Section 5.2 Newton's First Law
**Working title:** Inertia: The Puck That Never Stops
**Persona:** MEDHAVY · **Voice:** Kokoro `am_michael` at 0.85x · **Palette:** medhavy (Okabe-Ito, white background)

## Video

Rendered videos are not stored in this repository.

- YouTube Short: https://www.youtube.com/shorts/nJUA8plGrOQ
- Google Drive: https://drive.google.com/file/d/1tRTu1qvgipst0AY43jzoJPO5m6mir2kG/view?usp=drive_link

| Cut | File | Resolution | Runtime |
|---|---|---|---:|
| 16:9 long-form | `inertia-puck.mp4` | 3840x2160 | 0:53 |
| 9:16 short | `inertia-puck-short.mp4` | 2160x3840 | 1:16 |

## Files

- `inertia_puck.py` — single Manim scene (`InertiaPuck`) that renders both orientations. Portrait adds the opening question card and burned-in captions.
- `beat_sheet.json` — narration, visual intent and measured duration for each beat. `B00Q` is the opening question and is used only in the short.
- `PEDAGOGY.md` — Gate P review (VERDICT: PASS), required before audio generation.

## Rebuild

Requirements: Manim Community, ffmpeg, the PT Sans font, and the [brutalist.art](https://github.com/nikbearbrown/brutalist.art) toolkit for Kokoro narration.

```bash
# 1. Narration (voice comes from the beat sheet; writes mp3/beat-<ID>.mp3)
python <brutalist.art>/runtime/scripts/generate_audio_kokoro.py . --speed 0.85

# 2. Render
manim -qh inertia_puck.py InertiaPuck                                        # 16:9, no captions
manim -r 1080,1920 --fps 60 --disable_caching inertia_puck.py InertiaPuck    # 9:16, question card + captions

# 3. Mux narration (long: B00..B04, short: B00Q + B00..B04), then upscale to 4K
ffmpeg -i <render>.mp4 -vf "scale=3840:2160:flags=lanczos" -c:v libx264 -crf 16 -preset slow <slug>.mp4
ffmpeg -i <render>.mp4 -vf "scale=2160:3840:flags=lanczos" -c:v libx264 -crf 16 -preset slow content_4k.mp4

# 4. Short only: crossfade studio intro + content + studio outro (0.6s xfade/acrossfade at each seam)
```

The studio intro and outro clips are brand assets kept on Drive, not in this repository.
