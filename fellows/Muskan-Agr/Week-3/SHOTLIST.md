# SHOTLIST — humanitarians-ai-week3-stakeholder-strategy-hierarchy
## Estimated 3:54 (233.7s) · 19 beats · 0 pantry requests · 0 new assets
##
## Runtime uses 3.00 words/sec, the midpoint of two MEASURED builds:
## Week 1 = 2.89 wps (475 w / 164.57s), Week 2 = 3.01 wps (655 w / 217.61s).
## Week 2 landed 4% under its estimate, so expect roughly 3:40-3:53 here.

| Beat | Act | Source asset | Treatment | Manim class | Est. |
|---|---|---|---|---|---|
| B00 | Intro | none | Presenter card | `B00_Intro` | 13.7s |
| B01 | Limits | none | Three ticked rows | `B01_WhatNumbersGave` | 12.3s |
| B02 | Limits | none (black card) | Typography + mark | `B02_LimitCard` | 10.0s |
| B03 | Only-the-org | none (diagram) | 8 audience rows, built | `B03_Audiences` | 13.7s |
| B04 | Only-the-org | `02_tier_framework.jpg` | Full-bleed + 3 measured card boxes + 2 fitted chips | `B04_Terminology` | 14.0s |
| B05 | Only-the-org | none (diagram) | 3 stat blocks | `B05_Exits` | 9.3s |
| B06 | Only-the-org | `05_mission_cta_spotify.jpg` | Full-bleed + 3 button boxes + group box + fitted chip | `B06_ThreeAsks` | 11.0s |
| B07 | Trust | none (diagram) | Two-column ledger | `B07_TrustLedger` | 12.7s |
| B08 | Trust | none (quotes) | Two quoted claims + verdict | `B08_DonationConflict` | 18.3s |
| B09 | Trust | none (diagram) | Number inventory + 0 OUTCOMES | `B09_NoOutcomes` | 12.7s |
| B10 | Questions | none (black card) | Typography + mark | `B10_NotDesignDecisions` | 10.3s |
| B11 | Questions | none (diagram) | 8 themes, two columns | `B11_EightThemes` | 12.0s |
| B12 | Questions | none | 3 questions typeset | `B12_QuestionsAudience` | 13.3s |
| B13 | Questions | none | 3 questions typeset | `B13_QuestionsAction` | 15.0s |
| B14 | Questions | none | 3 questions typeset | `B14_QuestionsTrust` | 15.7s |
| B15 | Hierarchy | none (diagram) | 4-step content order | `B15_HierarchyOrder` | 12.3s |
| B16 | Hierarchy | none (card) | Statement — no layout drawn | `B16_HeroHeld` | 12.0s |
| B17 | Close | none (card) | The four-week arc — Week 4 named as nav cleanup + handoff | `B17_Close` | 13.3s |
| B18 | Outro | none (black card) | End card | `B18_EndCard` | 3.0s |

## Measured coordinates (normalized 0–1 against the ORIGINAL 1503×812 screenshots)

Derived by connected-component labelling on a maroon mask with holes closed
(so a white button label doesn't split its own button), and light-panel
thresholding for the tier cards. Nothing eyeballed. Constants sit together in
`scenes.py` under "Measured annotation boxes".

| Constant | Element | Asset | x0 | y0 | x1 | y1 |
|---|---|---|---|---|---|---|
| `TIER_CARD_1` | "Tier 1" card | 02 | 0.5163 | 0.2660 | 0.9308 | 0.4323 |
| `TIER_CARD_2` | "Tiers 3–6" card | 02 | 0.5163 | 0.4433 | 0.9308 | 0.6195 |
| `TIER_CARD_3` | "Tier 7" card | 02 | 0.5163 | 0.6305 | 0.9308 | 0.7968 |
| `CTA_DONATE_NOW` | DONATE NOW button | 05 | 0.3360 | 0.0825 | 0.4471 | 0.1133 |
| `CTA_VOLUNTEER` | VOLUNTEER button | 05 | 0.4591 | 0.0825 | 0.5609 | 0.1133 |
| `CTA_YOUTUBE` | YOUTUBE button | 05 | 0.5729 | 0.0837 | 0.6633 | 0.1133 |
| `CTA_GROUP` | all three, as one | 05 | 0.3360 | 0.0825 | 0.6633 | 0.1133 |

**Note on the CTA boxes.** Those three buttons are partially clipped at the top
by the sticky header in this capture, so the boxes hug the *visible* extent
(≈25 px tall rather than the full ≈40 px). That is deliberate: the annotation
should sit on what the viewer can see, not on geometry inferred from elsewhere.

## Geometry pre-check (done before any render)

All seven boxes mapped through `rect_in_image()` at 16:9 and confirmed
on-frame. The third tier card reaches y = −2.37, leaving only 0.16 units of
clearance for a chip pinned at y_frac 0.87 — so B04 and B06 use `chip_below()`,
which measures the band and fits the chip into it instead. Cannot collide by
construction.

## Assets — reused from Week 1, none new
- `02_tier_framework.jpg` — B04. **First use in the series.** Week 1 held it
  in reserve; it is the clearest on-site evidence of internal shorthand.
- `05_mission_cta_spotify.jpg` — B06. **First use in the series.** Week 1 held
  it in reserve; it is the only asset showing the three simultaneous asks.
- `01_hero_section.jpg`, `03_program_cards.jpg`, `06_footer.jpg`,
  `04_irreducibly_human.jpg` — copied in, not used in this cut.

Both previously-unused reserve screenshots now earn their place, which closes
the note Week 1 left open about them.

## Standing rule: no proposed layouts

Nothing in this reel shows the site altered. B15 draws an abstract content
order (what a visitor came for → why it is credible → the one next action →
everything else), which is a principle, not a mockup of their page. B16 states
the hero direction in words. Carried forward from the Week 2 correction.
