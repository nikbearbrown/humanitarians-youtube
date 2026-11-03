# Medhavy — Logo Reel (brand sting)

A ~20s animated logo reel. Base = Manim (silent); voiceover muxed by `assemble.py`
using the Medhavy brand voice (`1sgY6Voq1aexKOB1IJ2D`).

## Voice (3 lines)
1. **"Medhavy."** — lands as the wordmark writes in.
2. **"Intelligent Textbooks."** — lands as the tagline appears.
3. **"www.Medhavy.com"** (spoken "W W W dot Medhavy dot com.") — lands as the URL writes in.

## Visual arc
- **Open** — white field, one accent circuit-node blinks.
- **Construct** — the hero mark (an "M" of circuit traces rising from an open book)
  draws on stroke-by-stroke; accent nodes pulse in. This is the "constructed" centerpiece.
- **Wordmark** — **MEDHAVY** writes in below, Montserrat **Bold**, all caps,
  letter-spacing ~0.28em (tracked per-letter to match the CSS spec).
- **Montage** — the mark above the wordmark cycles through alternate Medhavy marks,
  each with a different animation (grow, spiral, draw-on, border-then-fill, fade-rotate).
  This is the "try many animations" showcase.
- **Lockup** — hero returns, tagline **INTELLIGENT TEXTBOOKS** appears, then the URL.
- **Outro** — final lockup holds with one last accent pulse.

## Knobs
- `HERO` (scene constant) — the hero mark. Currently `medhavy-08`. Swap to any file in
  `assets/svg/` (see the contact sheet `medhavy/_contact_sheet.png` for all 58).
- `MONTAGE` — the list of alternate marks shown in the showcase.
- `ACCENT` `#2A6FB0`, `INK` `#15151c` — palette. No brand color was specified; these are
  a tasteful default (ink mark, tech-blue circuit nodes). Easy to change.
- Wordmark tracking: `tracked_text(..., track=0.28)` = the 0.28em letter-spacing.

## Notes
- Pronunciation: if ElevenLabs mis-says "Medhavy", set `tts_normalized_text` on `B02_NAME`
  to a phonetic spelling (e.g. "Med-hah-vee") and re-run audio for that beat only.
- Silent construction/montage/hold beats use the new `generate_audio` `"silent": true`
  feature so the three spoken lines stay synced to their sections.
- 16:9 only (brand sting). Say the word and I'll add a 9:16 cut for Shorts/Reels.
