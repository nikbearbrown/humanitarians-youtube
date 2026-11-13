# How GPS Knows Where You Are — Tanishaa

## This week's contribution
- **Question:** how does a phone that never transmits anything work out where it is?
- **Prediction:** three satellites should be enough.
- **What I built:** a 3-minute explainer. The worked example (`demo/gps_demo.py`) is a real position solver for four satellites above Boston Common.
- **Observed result:** with the phone clock off by one microsecond, solving with three unknowns (position only) landed 390 m away; adding the clock as a fourth unknown landed on the spot and recovered the 1.000000 µs error. Three satellites aren't enough with a cheap clock.
- **Next experiment:** add realistic noise (atmosphere, multipath) and see how satellite geometry spreads the error.

## Human and AI work
- **My decisions, implementation and verification:** topic choice (GPS, from four non-music options), script approval, the on-screen-text rule (key points cued to the narration). _[Tanishaa: add what you reviewed or changed.]_
- **AI tools/voices used and what they generated:** Claude (Claude Code) drafted the script, wrote the demo, the beat sheet and GpsScenes.tsx, and ran the build. Kokoro `af_bella` (a local AI voice) speaks all narration, which is disclosed in the opening.
- **What I rejected or corrected:** _[Tanishaa: add anything you changed.]_
- **What remains unverified or failed:** the demo's satellite positions are illustrative (not a live almanac); B02 and B04/B05 are schematic diagrams, labeled that way.

## Reproduce
- Brutalist commit `a99b5323fe346786c3e5991b09a5cc784a6b0da2` (2026-10-23), checked 2026-11-08.
- Steps: `python demo/gps_demo.py` → `python3 build_sheet.py` → `generate_audio_kokoro.py` → `python word_times.py` → `python3 build_sheet.py` → `remotion_scenes.py` → `python add_bug.py B00 B10` → `./art final`; vertical: `./art vertical`, edit B09/B10, render, `add_bug.py --dir vertical B00 B10`, `./art final vertical --height 3840`.
- Media (MP4/MP3) goes to Drive, not GitHub.

## Watch and review
| Version | Drive link | Resolution | Duration | SHA-256 |
|---|---|---|---|---|
| Landscape | _[Tanishaa: add Drive week folder link]_ (`landscape/`) | 3840×2160 | 2:55.8 | `c4fd3fca2a68b98228500ba914fe51077a7d9395ef820662d656939302d26d03` |
| Vertical | _[Tanishaa: add Drive week folder link]_ (`vertical/`) | 2160×3840 | 2:55.8 | `761e388b874de6d7dce9e5f89005832479bd40e46295a27cdc8c8805e07a921c` |

- Review status: pending
- YouTube 4K check: pending
- Publication decision: pending
