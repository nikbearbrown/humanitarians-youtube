# How Can A Small Push Lift A Car?

A hydraulic jack trades a long, gentle push on a small piston for a short, powerful lift on a large one.

**Source:** Physics Volume 1, Chapter 14: Fluid Mechanics, Section 14.3 Pascal's Principle and Hydraulics
**Working title:** A Small Push Lifts a Car: Pascal's Principle and Hydraulics
**Persona:** MEDHAVY · **Voice:** Kokoro `am_michael` at 0.85x · **Palette:** medhavy (Okabe-Ito, white background)

## Video

Rendered videos are not stored in this repository.

- YouTube Short: https://www.youtube.com/shorts/zERIfq1IIEI
- Google Drive: https://drive.google.com/file/d/1bvKKn3cc6acC9_KJBax4MDu6L-PBD8ur/view?usp=drive_link

| Cut | File | Resolution | Runtime |
|---|---|---|---:|
| 16:9 long-form | `hydraulics.mp4` | 3840x2160 | 1:46 |
| 9:16 short | `hydraulics-short.mp4` | 2160x3840 | 2:00 |

## Files

- `hydraulics.py` — single Manim scene (`Hydraulics`) that renders both orientations. Portrait adds the opening question card and burned-in captions.
- `beat_sheet.json` — narration, visual intent and measured duration for each beat. `B00Q` is the opening question and is used only in the short.
- `PEDAGOGY.md` — Gate P review (VERDICT: PASS), required before audio generation.
- `../medhavy_common.py` — shared palette, safe-area helpers, caption schedule and the `MedhavyScene` base class. The script imports it from the parent folder, so keep the two together.

## Rebuild

Requirements: Manim Community, ffmpeg, the PT Sans font, and the [brutalist.art](https://github.com/nikbearbrown/brutalist.art) toolkit for Kokoro narration.

```bash
# 1. Narration (voice comes from the beat sheet; writes mp3/beat-<ID>.mp3)
python <brutalist.art>/runtime/scripts/generate_audio_kokoro.py . --speed 0.85

# 2. Render
manim -qh hydraulics.py Hydraulics                                        # 16:9, no captions
manim -r 1080,1920 --fps 30 --disable_caching hydraulics.py Hydraulics    # 9:16, question card + captions

# 3. Mux narration (long: all beats except B00Q, short: B00Q first), then upscale to 4K
ffmpeg -i <render>.mp4 -vf "scale=3840:2160:flags=lanczos" -c:v libx264 -crf 16 -preset slow hydraulics.mp4
ffmpeg -i <render>.mp4 -vf "scale=2160:3840:flags=lanczos" -c:v libx264 -crf 16 -preset slow content_4k.mp4

# 4. Short only: studio intro + content + studio outro, joined with 0.8s dissolves through white
#    (white lead-in before the question card, final frame held after the last word)
```

The studio intro and outro clips are brand assets kept on Drive, not in this repository.
