# Why Does A Skydiver Stop Speeding Up?

A falling skydiver reaches a steady speed when air drag grows until it balances gravity.

**Source:** Physics Volume 1, Chapter 6: Applications of Newton's Laws, Section 6.4 Drag Force and Terminal Speed
**Working title:** The Fall That Stops Speeding Up
**Persona:** MEDHAVY · **Voice:** Kokoro `am_michael` at 0.85x · **Palette:** medhavy (Okabe-Ito, white background)

## Video

Rendered videos are not stored in this repository.

- YouTube Short: https://www.youtube.com/shorts/4YnvIlrcNJQ
- Google Drive: https://drive.google.com/file/d/14l2piXGjFPDJeq7QRrSI-m6l889NLcgH/view?usp=sharing

| Cut | File | Resolution | Runtime |
|---|---|---|---:|
| 16:9 long-form | `terminal-velocity.mp4` | 3840x2160 | 0:45 |
| 9:16 short | `terminal-velocity-short.mp4` | 2160x3840 | 1:01 |

## Files

- `terminal-velocity.py` — single Manim scene (`TerminalVelocity`) that renders both orientations. Portrait adds the opening question card and burned-in captions.
- `beat_sheet.json` — narration, visual intent and measured duration for each beat. `B00Q` is the opening question and is used only in the short.
- `PEDAGOGY.md` — Gate P review (VERDICT: PASS), required before audio generation.
- `../medhavy_common.py` — shared palette, safe-area helpers, caption schedule and the `MedhavyScene` base class. The script imports it from the parent folder, so keep the two together.

## Rebuild

Requirements: Manim Community, ffmpeg, the PT Sans font, and the [brutalist.art](https://github.com/nikbearbrown/brutalist.art) toolkit for Kokoro narration.

```bash
# 1. Narration (voice comes from the beat sheet; writes mp3/beat-<ID>.mp3)
python <brutalist.art>/runtime/scripts/generate_audio_kokoro.py . --speed 0.85

# 2. Render
manim -qh terminal-velocity.py TerminalVelocity                                        # 16:9, no captions
manim -r 1080,1920 --fps 30 --disable_caching terminal-velocity.py TerminalVelocity    # 9:16, question card + captions

# 3. Mux narration (long: all beats except B00Q, short: B00Q first), then upscale to 4K
ffmpeg -i <render>.mp4 -vf "scale=3840:2160:flags=lanczos" -c:v libx264 -crf 16 -preset slow terminal-velocity.mp4
ffmpeg -i <render>.mp4 -vf "scale=2160:3840:flags=lanczos" -c:v libx264 -crf 16 -preset slow content_4k.mp4

# 4. Short only: studio intro + content + studio outro, joined with 0.8s dissolves through white
#    (white lead-in before the question card, final frame held after the last word)
```

The studio intro and outro clips are brand assets kept on Drive, not in this repository.
