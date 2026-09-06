# FACTCHECK — humanitarians-ai-week1-diagnostic-audit

Status: **DRAFT — needs your sign-off before this ships.** Every row below
was checked against the six screenshots you supplied (pixel-measured where
possible, per BUILD-LOG.md); rows marked UNVERIFIABLE need your own project
records, not the screenshots, to confirm.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix if needed |
|---|---|---|---|---|---|
| 1 | B03 | "The original brief was a full rebuild" | ⚠ UNVERIFIABLE FROM SCREENSHOTS | This is a claim about your project's kickoff brief, not about the live site. Confirm against your own scope doc / kickoff notes before publishing. | If the original ask wasn't literally "full rebuild," soften the narration |
| 2 | B03 | About Us / Contact Us buttons sit directly below the hero copy; a Donate button sits in the top nav | ✓ PASS | Measured directly from `01_hero_section.jpg` pixel data (maroon-color bounding boxes): About/Contact at x∈[0.073,0.261] y∈[0.762,0.812]; Donate at x∈[0.811,0.888] y∈[0.016,0.065] (normalized, full image) | — |
| 3 | B04 | Homepage carries "tiers, a framework, four separate program blocks, a documentation system, a curriculum series" before a plain next-step ask | ✓ PASS (4 of 5 sub-claims directly confirmed) | Tier framework: `02_tier_framework.jpg` shows Tier 1 / Tiers 3–6 / Tier 7. Four program blocks: `03_program_cards.jpg` shows exactly four cards (Fellows Program, Botspeak: AI Fluency, Lyrical Literacy, AI for Good). Curriculum series: `04_irreducibly_human.jpg`'s own copy says "A curriculum series, production pipeline, and measurement infrastructure." | "Documentation system" isn't independently visible in the six supplied screenshots — if you're not confident this is accurate, drop that one phrase from B04's narration |
| 4 | B05 | "Six concepts before one ask" | ⚠ APPROXIMATE | Count depends on what you're bundling as a "concept" (tiers + framework + 4 program cards ≈ 6, depending on whether the framework itself counts separately). The four program cards and the tier framework are both confirmed real; the number "six" is an editorial count, not a labeled fact on the page | If you want this bulletproof, recount on the live page and adjust the chip text to match exactly |
| 5 | B06 | Footer Projects column lists exactly 8 unlabeled project names: Dewey, Madison, Medhavy, Mycroft, Popper (+3 more) | ✓ PASS | `06_footer.jpg`'s Projects column: Dewey, Irreducibly Human, Lyrical Literacy, Madison, Medhavy, Musinique, Mycroft, Popper = 8 items, confirmed by direct count | — |
| 6 | B07 | "The site currently relies on one bold display face at nearly every level" | ⚠ DESIGN JUDGMENT, NOT A VERIFIABLE FACT | Visually plausible across `01_hero_section.jpg` and `03_program_cards.jpg` (both use the same bold sans at multiple sizes) but "one weight" is your own design assessment, not a measurable claim (font-weight isn't legible from a JPEG at this resolution) | Keep as stated opinion/assessment; don't present as a measured fact if asked |
| 7 | B09 | "Primary visual real estate goes to a video embed" spanning most of the hero's right half | ✓ PASS | Measured: dark video block bounding box x∈[0.300,0.927] y∈[0.219,0.799] of `01_hero_section.jpg` — occupies roughly 46% of total hero area vs. the text column's ~30% | — |
| 8 | B10–B11 | "The original scope was a full rebuild... the direction shifted to fix structural problems first" | ⚠ UNVERIFIABLE FROM SCREENSHOTS | Same as row 1 — a claim about the project's internal decision history, not the live site. Confirm against your own scope/pivot documentation. | — |

## What this file does NOT check
Narration wording, pacing, and pedagogical structure are PEDAGOGY.md's job.
This file only checks: did the video state something as fact that the
underlying screenshot doesn't actually show?

## Sign-off
- [ ] Rows 1 and 8 confirmed against your own project brief/scope documents
- [ ] Row 4's "documentation system" phrase either confirmed or removed
- [ ] Row 5's "six concepts" recounted against the live page if you want an
      exact, defensible number rather than an editorial estimate

Until those three boxes are checked, treat this as **GATE F: NOT YET
SIGNED.**
