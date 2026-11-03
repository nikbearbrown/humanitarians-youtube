# SHOTLIST — humanitarians-ai-week2-typography-hero-concepting
## Estimated 3:47 (226.6s) · 17 beats · 0 pantry requests · 0 new assets
##
## Runtime estimate uses 2.89 words/sec — MEASURED from Week 1's real Kokoro
## output (475 words / 164.57s), not the 2.3 wps planning figure Week 1 used.
## Week 1 estimated 3:44 and actually ran 2:44; this sheet should not repeat
## that error. Actual durations still come from ffprobe after the audio step.

| Beat | Act | Source asset | Treatment | Manim class | Est. |
|---|---|---|---|---|---|
| B00 | Intro | none (presenter card) | Typography only | `B00_Intro` | 15.2s |
| B01 | Scope | none (black card) | Typography only | `B01_ScopeCard` | 12.8s |
| B02 | Scope | none (white card) | Typography only | `B02_MethodCard` | 9.7s |
| B03 | Nav audit | `01_hero_section.jpg` | Full-bleed + 2 measured red boxes + 2 sequential chips | `B03_NavAnnotated` | 17.3s |
| B04 | Nav audit | none (diagram) | 7-slot nav map + 2 absent-link ghosts, drawn on cue | `B04_NavMap` | 14.5s |
| B05 | Footer audit | `06_footer.jpg` | Full-bleed + red box on Projects column + 2 chips | `B05_FooterFull` | 12.8s |
| B06 | Footer audit | none (typeset list) | 6 project names, built row by row | `B06_ProjectNames` | 14.9s |
| B07 | Footer audit | none (black card) | Duplicate-link table, 2 rows | `B07_FooterDupes` | 10.7s |
| B08 | Typography | none (diagram) | 4 stat blocks | `B08_TypeCount` | 13.8s |
| B09 | Typography | none (diagram) | 5-rung type scale with px values, rung by rung | `B09_TypeScaleSpec` | 15.6s |
| B10 | Typography | none (diagram) | Measure bar, 84 chars vs the 45–75 band | `B10_LineLength` | 14.9s |
| B11 | Accessibility | none (diagram) | 2 contrast swatch rows, FAIL vs PASS | `B11_ContrastCard` | 20.4s |
| B12 | Accessibility | `01_hero_section.jpg` | Full-bleed + 4 measured red boxes + fitted chip | `B12_MaroonCTAs` | 13.1s |
| B13 | Hero | `01_hero_section.jpg` | Full-bleed + 2 measured area boxes + 2 chips | `B13_HeroRatio` | 15.2s |
| B14 | Hero | none (statement card) | The hero principle, typeset — no layout shown | `B14_HeroDirection` | 12.1s |
| B15 | Close | none (white card) | Typography only | `B15_Close` | 12.1s |
| B16 | Outro | none (black card) | Typography only | `B16_EndCard` | 3.1s |

## Measured coordinates (normalized 0–1 against the ORIGINAL 1503×812 screenshot)

Every box below came out of PIL/numpy analysis of the actual asset pixels —
connected-component labelling on a maroon colour mask for the buttons, a
brightness threshold for the video block, and ink-column profiling for the
footer. Nothing here was eyeballed. Method is in SOURCES.md; the scene
constants sit at the top of the B03 block in `scenes.py`.

| Constant | Element | x0 | y0 | x1 | y1 |
|---|---|---|---|---|---|
| `NAV_SECTION_LINKS` | AI+1 / Fellows / Projects / Videos | 0.2043 | 0.0148 | 0.3779 | 0.0653 |
| `NAV_CTA_BUTTONS` | Youtube + Donate pair | 0.7172 | 0.0148 | 0.8882 | 0.0653 |
| `BTN_YOUTUBE` | Youtube button | 0.7172 | 0.0160 | 0.7991 | 0.0653 |
| `BTN_DONATE` | Donate button | 0.8110 | 0.0160 | 0.8882 | 0.0653 |
| `BTN_ABOUT` | About Us button | 0.0725 | 0.7623 | 0.1590 | 0.8116 |
| `BTN_CONTACT` | Contact Us button | 0.1657 | 0.7623 | 0.2608 | 0.8116 |
| `HERO_VIDEO` | Video embed block | 0.3686 | 0.2192 | 0.9275 | 0.7993 |
| `HERO_MESSAGE` | Hero message column | 0.0725 | 0.2167 | 0.3320 | 0.8128 |
| `FOOTER_PROJECTS_COL` | Footer Projects column | 0.7319 | 0.0973 | 0.8071 | 0.5012 |

**Cross-validation against Week 1.** `BTN_DONATE` reproduces Week 1's measured
Donate box (0.811, 0.016, 0.888, 0.065) to four decimals, and the union of
`BTN_ABOUT` + `BTN_CONTACT` reproduces Week 1's combined About/Contact box
(0.0725, 0.762, 0.261, 0.812). Two independent measurement passes, same
numbers — that is the confidence check for every other box on this list.

**Correction carried over from Week 1.** Week 1's `B06_FooterZoom` used an
estimated crop of (0.62, 0.0, 0.92, 0.55) and flagged it as the one box to
verify. Measured now: that range spans px 931–1382, which covers **three**
footer columns (Resources 935–1048, Projects 1100–1213, Legal & Privacy
1264–1354), not the Projects column alone. The corrected Projects-only range
is 0.7319–0.8071. Week 1's cut is already published; this is recorded so the
number is right from here on.

## Geometry pre-check (run before any render)

All nine boxes were mapped through `rect_in_image()` at 16:9 and confirmed
on-frame. The two hero beats leave a clear band of **0.62 Manim units
(~168 px at 4K)** between the lowest annotation edge and the bottom safe-area
line; `chip_below()` fits the overlay chip into that band rather than clamping
it back through the box. See BUILD-LOG.md.

## Assets — all six reused from Week 1, none new
- `01_hero_section.jpg` — B03, B12, B13
- `06_footer.jpg` — B05
- `02_tier_framework.jpg`, `03_program_cards.jpg`, `04_irreducibly_human.jpg`,
  `05_mission_cta_spotify.jpg` — copied in, **not used** in this cut. Available
  if the real Kokoro runtime lands short and the piece needs another beat.

Re-verified against the live site on 2026-09-04: the hero layout, the nav
items, and the footer column structure all still match these captures. One
drift worth knowing — the live page has shifted about 22 px vertically since
these screenshots were taken, so live DOM coordinates are **not**
interchangeable with screenshot coordinates. Every annotation box in this reel
was measured from the screenshot, which is what actually appears on screen.

## B14 — deliberately shows no proposed layout

An earlier draft of B14 drew a "current vs direction" wireframe pair. That was
removed at the presenter's instruction: the hero is not shown altered, because
no redesign has been settled. Inventing a layout for the screen would claim
work that has not been done. B14 now states the intent — order the hero around
what a first-time visitor expects to find first — and nothing more. The only
hero imagery in this reel is the unmodified screenshot, in B03, B12 and B13.
