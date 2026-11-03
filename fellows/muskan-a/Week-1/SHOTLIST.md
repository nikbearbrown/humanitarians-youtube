# SHOTLIST — humanitarians-ai-week1-diagnostic-audit
## Total: ~3:44 (223.5s estimated — actual will shift slightly once Kokoro
## measures real narration length) · 14 beats · 0 pantry requests

| Beat | Scene | Source asset | Treatment | Manim class | Est. |
|---|---|---|---|---|---|
| B00 | Intro | none (presenter card) | Typography only | `B00_Intro` | 19.0s |
| B01 | 1 | `01_hero_section.jpg` | Full-bleed, 16:9 cover-crop | `B01_HeroFullBleed` | 14.2s |
| B02 | 1 | none (black card) | Typography only | `B02_GoalCard` | 3.4s |
| B03 | 2 | `01_hero_section.jpg` | Full-bleed + red box (About/Contact) + red arrow (Donate) + 3 sequential chips | `B03_HeroAnnotated` | 19.9s |
| B04 | 3 | `02_tier_framework.jpg` | Full-bleed, 16:9 cover-crop | `B04_TierFramework` | 17.7s |
| B05 | 3 | `03_program_cards.jpg` | Full-bleed + 2 sequential chips | `B05_ProgramCards` | 10.8s |
| B06 | 3 | `06_footer.jpg` | Cropped to Projects column region + 1 chip | `B06_FooterZoom` | 19.5s |
| B07 | 4 | `01_hero_section.jpg` (×2 crops) + `03_program_cards.jpg` (×1 crop) | 3-panel side-by-side comparison + struck-through headline | `B07_TypographyCompare` | 20.8s |
| B08 | 4 | none (diagram) | 4-rung ladder, drawn on cue | `B08_TypeScaleLadder` | 16.9s |
| B09 | 5 | `01_hero_section.jpg` | Full-bleed + red ellipse (video embed) + 2 sequential chips | `B09_HeroReworkAnnotated` | 37.3s |
| B10 | 6 | none (black card) | Typography + strike-through | `B10_PivotPlanA` | 18.6s |
| B11 | 6 | none (black card) | Typography only | `B11_PivotPlanB` | 12.1s |
| B12 | 7 | none (white card) | Typography only | `B12_Close` | 8.2s |
| B13 | Outro | none (black card) | Typography only | `B13_EndCard` | 5.1s |

## Exact crop / annotation coordinates (normalized, 0–1, against the ORIGINAL
## screenshot — all measured directly from pixel data, not eyeballed; see
## BUILD-LOG.md for the measurement method)

| Beat | Region | x0 | y0 | x1 | y1 |
|---|---|---|---|---|---|
| B03 | About Us / Contact Us button box | 0.0725 | 0.762 | 0.261 | 0.812 |
| B03 | Donate button (arrow target) | 0.811 | 0.016 | 0.888 | 0.065 |
| B06 | Footer Projects column (approximate — see note below) | 0.62 | 0.0 | 0.92 | 0.55 |
| B07 | Hero headline crop | 0.06 | 0.19 | 0.40 | 0.45 |
| B07 | Program-card header crop | 0.05 | 0.28 | 0.30 | 0.42 |
| B07 | Hero body-copy crop | 0.06 | 0.30 | 0.36 | 0.58 |
| B09 | Video embed block (ellipse target) | 0.300 | 0.219 | 0.927 | 0.799 |

**Note on B06:** the footer screenshot's Projects-column x-range was
estimated from the column ORDER visible in the footer image (Company,
Programs, Platform, Resources, Projects, Legal & Privacy — Projects is the
5th of 6 columns) rather than pixel-measured like the maroon buttons, since
there's no distinct color to threshold on. **Check this crop on your first
`./art run` previz** — if the column boundary lands wrong, adjust the `box`
tuple in `scenes.py`'s `B06_FooterZoom.construct()` and rerun (only that
beat recompiles).

## Assets used (all six of your uploads; all placed in `assets/`)
- `01_hero_section.jpg` — used in B01, B03, B07 (×2), B09
- `02_tier_framework.jpg` — used in B04
- `03_program_cards.jpg` — used in B05, B07 (×1)
- `06_footer.jpg` — used in B06
- `04_irreducibly_human.jpg`, `05_mission_cta_spotify.jpg` — **not used** in
  this cut (the brief held these in reserve as extra B-roll / an example of
  embed-weight; the 3:44 runtime didn't need them to hit the 3–4 minute
  target). They're still in `assets/` if a future edit wants them.
