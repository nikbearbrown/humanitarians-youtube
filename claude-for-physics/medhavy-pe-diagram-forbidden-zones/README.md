# Why Can't A Particle Pass Certain Points?

A particle sliding in a potential-energy valley is confined to the region where its total energy is at least its potential energy.

**Source:** Physics Volume 1, Chapter 8: Potential Energy and Conservation of Energy, Section 8.4 Potential Energy Diagrams and Stability
**Working title:** A Potential Energy Diagram Shows Where a Particle Cannot Go
**Persona:** MEDHAVY · **Voice:** Kokoro `am_michael` at 0.85x · **Palette:** medhavy (Okabe-Ito, white background)

## Video

Rendered videos are not stored in this repository.

- YouTube Short: https://www.youtube.com/shorts/zS_nQV0kLv0
- Google Drive: https://drive.google.com/file/d/1LoR2KoBPgZWL7cFoJ7i7s02reeERnm6j/view?usp=drive_link

| Cut | File | Resolution | Runtime |
|---|---|---|---:|
| 16:9 long-form | `pe-diagram-forbidden-zones.mp4` | 3840x2160 | 1:30 |
| 9:16 short | `pe-diagram-forbidden-zones-short.mp4` | 2160x3840 | 1:45 |

## Files

- `pe-diagram-forbidden-zones.py` — single Manim scene (`PEDiagramForbiddenZones`) that renders both orientations. Portrait adds the opening question card and burned-in captions.
- `beat_sheet.json` — narration, visual intent and measured duration for each beat. `B00Q` is the opening question and is used only in the short.
- `PEDAGOGY.md` — Gate P review (VERDICT: PASS), required before audio generation.
- `../medhavy_common.py` — shared palette, safe-area helpers, caption schedule and the `MedhavyScene` base class. The script imports it from the parent folder, so keep the two together.

## Rebuild

Requirements: Manim Community, ffmpeg, the PT Sans font, and the [brutalist.art](https://github.com/nikbearbrown/brutalist.art) toolkit for Kokoro narration.

```bash
# 1. Narration (voice comes from the beat sheet; writes mp3/beat-<ID>.mp3)
python <brutalist.art>/runtime/scripts/generate_audio_kokoro.py . --speed 0.85

# 2. Render
manim -qh pe-diagram-forbidden-zones.py PEDiagramForbiddenZones                                        # 16:9, no captions
manim -r 1080,1920 --fps 30 --disable_caching pe-diagram-forbidden-zones.py PEDiagramForbiddenZones    # 9:16, question card + captions

# 3. Mux narration (long: all beats except B00Q, short: B00Q first), then upscale to 4K
ffmpeg -i <render>.mp4 -vf "scale=3840:2160:flags=lanczos" -c:v libx264 -crf 16 -preset slow pe-diagram-forbidden-zones.mp4
ffmpeg -i <render>.mp4 -vf "scale=2160:3840:flags=lanczos" -c:v libx264 -crf 16 -preset slow content_4k.mp4

# 4. Short only: studio intro + content + studio outro, joined with 0.8s dissolves through white
#    (white lead-in before the question card, final frame held after the last word)
```

The studio intro and outro clips are brand assets kept on Drive, not in this repository.
