# SOURCES — humanitarians-ai-week1-diagnostic-audit

## Primary source
- **"Week 1 Video Brief: Diagnostic Audit and Typography Foundations"** —
  the presenter's own scene-by-scene script, working title "Before You
  Rebuild, You Read the Room." Supplied directly in this build session.
  First-party source: the presenter is narrating her own project work, so
  there's no independent-source verification needed for the narration
  itself (unlike, say, a claim about a third party's product). FACTCHECK.md
  covers the on-screen claims that CAN be checked against something —
  the screenshots.

## Screenshots (all six supplied, all placed in `assets/`)
1. `01_hero_section.jpg` — humanitarians.ai homepage hero section
2. `02_tier_framework.jpg` — the Tier 1 / Tiers 3–6 / Tier 7 comparison block
3. `03_program_cards.jpg` — the four program cards (Fellows Program,
   Botspeak: AI Fluency, Lyrical Literacy, AI for Good)
4. `04_irreducibly_human.jpg` — the Irreducibly Human framework section
   (held in reserve, not used in this cut — see SHOTLIST.md)
5. `05_mission_cta_spotify.jpg` — the closing mission CTA with the Spotify
   embed (held in reserve, not used in this cut)
6. `06_footer.jpg` — the full footer navigation

All six are direct screenshots of the presenter's own organization's live
website (humanitarians.ai), supplied by the presenter for this build — not
third-party or archival material, so no license/credit sidecar is needed
(compare to the toolkit's `archive` source-axis rule, which doesn't apply
here since these are `source: own` screenshots of the presenter's own site).

## Color/coordinate measurements (derivation, not opinion)
The maroon accent (`#64140E`) and every annotation bounding box in
`scenes.py` were measured programmatically from the actual pixel data of
`01_hero_section.jpg` and `01_hero_section.jpg`'s video-embed region — not
eyeballed or guessed. Full method: color-threshold on the button's known
maroon RGB value, then take the bounding box of matching pixels. See
BUILD-LOG.md for the exact commands run.

## What has NOT been independently sourced
Claims about the project's internal history — "the original brief was a
full rebuild," "the direction shifted" — describe the presenter's own
project decisions, not facts about the live site. These are flagged
UNVERIFIABLE FROM SCREENSHOTS in FACTCHECK.md, not because they're doubted,
but because a screenshot of a website can't confirm what a project brief
said. Confirm those against your own project records before this ships.
