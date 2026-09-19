# SOURCES — humanitarians-ai-week3-stakeholder-strategy-hierarchy

Every on-screen number, with how it was obtained. Nothing here is an estimate
presented as a measurement.

## Primary source

**https://humanitarians.ai** — homepage plus `/about`, `/donate`, `/clients`
and `/fellows`, inspected live on **2026-09-05** at an emulated 1503×812
viewport (matching the Week 1 screenshot dimensions exactly).

Method: JavaScript executed in the page — `innerText` scans with counted
regular expressions, `getComputedStyle` and `getBoundingClientRect` for
geometry, and anchor walks of `<header>` and `<footer>`. Screenshot annotation
boxes came from PIL + numpy + scipy against the Week 1 assets.

## Claim-by-claim

| Beat | On-screen claim | Source | Value |
|---|---|---|---|
| B03 | Eight audiences | counted mentions in homepage copy | fellows/OPT 15, donors 10, mentors 5, educators 5, organizations/clients 5, kids/families 2, volunteers 1, the public 1 |
| B03 | "No stated order of priority" | absence check — no ranking, no primary-audience statement anywhere in the copy | — |
| B04 | 24 named concepts | matched against the homepage text | Tier 1, Tiers 3–6, Tier 7, Irreducibly Human, Botspeak, Addams, AI+1, AIMagineering, Lyrical Literacy, Conducting AI, Ethical Play, Causal Reasoning, Embodied Teaching, The AI Sherpa, AI Skunkworks, Dewey, Madison, Medhavy, Musinique, Mycroft, Popper, 80 Days to Stay, cognitive forklift, OPT |
| B04 | "One every 50 words" | 1,201 homepage words ÷ 24 terms | 50.0 |
| B05 | 13 onward links | anchors matching learn more / explore / more on | 13 (10 distinct labels) |
| B05 | 69 clickable labels, 54 distinct | all `<a>` and `<button>` with non-empty text | 69 / 54 |
| B06 | Three asks, identically weighted | pixel measurement of `05_mission_cta_spotify.jpg` | DONATE NOW, VOLUNTEER, YOUTUBE — same fill, same height, same row |
| B07 | 501(c)(3), EIN, state registration present | footer text | "A 501(c)(3) nonprofit organization · State ID: 001846362 · EIN: 33-1984805" |
| B07 | Annual report, Form 990, named board, charity rating absent | absence checks across homepage, /about, /donate, /clients, /fellows | none found |
| B08 | Mid-page donation claim | verbatim quote | "100% of donations fund the programs, mentorship, and project support that make this happen." |
| B08 | Footer donation claim | verbatim quote, same page | "100% of all donations support our direct operational costs, including program expenses, legal fees, and staff salaries to advance our mission." |
| B09 | Every number is a label, an identifier, a count, a claim or a year | exhaustive scan of every numeric token in the homepage copy | 23 numeric tokens, 0 outcomes |

## The donation conflict — stated precisely

Both sentences appear on the homepage. Both begin "100%". They are not
compatible readings of the same policy: one promises donations fund programs,
mentorship and project support; the other says they support operational costs
*including legal fees and staff salaries*. A donor comparing them cannot tell
which applies.

This is quoted, not paraphrased, in B08. It is the clearest example in the
whole series of a finding a designer must surface and must not resolve alone —
which is the argument the video is making.

## Not verifiable from public sources

Carried on the presenter's authority, and flagged in FACTCHECK.md:

- that the stakeholder meeting and question set are prepared and pending
- that the structural hierarchy strategy is the one described in B15
- that hero refinement continued this week without a layout being settled
