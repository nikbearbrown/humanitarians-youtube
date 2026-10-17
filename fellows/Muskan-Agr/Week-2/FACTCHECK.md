# FACTCHECK — humanitarians-ai-week2-typography-hero-concepting

Scope: this gate checks the ON-SCREEN CLAIMS against evidence. The narration is
the presenter's own account of her own work; what needs verifying is every
number and label that appears as a graphic.

Method and per-claim evidence: see SOURCES.md. Status legend:
✅ measured · ⚠️ convention/judgement · ⬜ needs Muskan's sign-off

| # | On-screen claim | Beat | Status | Evidence |
|---|---|---|---|---|
| 1 | "4 SECTION LINKS. 2 BUTTONS." | B03 | ✅ | DOM header walk: AI+1, Fellows, Projects, Videos + Youtube, Donate |
| 2 | "NO ABOUT. NO CONTACT." | B03 | ✅ | Neither string occurs in `<header>`; both occur in hero + footer |
| 3 | Nav map shows 7 slots | B04 | ✅ | logo + 4 sections + 2 CTAs (theme toggle excluded: not a destination) |
| 4 | "ORIENTATION MISSING. PROMOTION DUPLICATED." | B04 | ✅ | YouTube ×4 and Donate ×3 page-wide; About/Contact absent from nav |
| 5 | "6 COLUMNS. 33 LINKS." | B05 | ✅ | 5+3+4+6+11+4 = 33 |
| 6 | "39 ANCHORS IN TOTAL." | B05 | ✅ | 33 column links + logo + 5 inline |
| 7 | Red box = the Projects column | B05 | ✅ | ink-column profiling, x 0.7319–0.8071 (corrects Week 1's 3-column box) |
| 8 | "PROJECTS COLUMN — 11 LINKS." | B06 | ✅ | DOM list of 11 |
| 9 | The six names listed | B06 | ✅ | Dewey, Madison, Medhavy, Musinique, Mycroft, Popper |
| 10 | "6 BARE PROPER NOUNS. 0 CONTEXT." | B06 | ⚠️ | The count is measured; "undecodable" is a UX judgement, stated as such |
| 11 | "ALL PROJECTS — COMPANY + PROJECTS" | B07 | ✅ | DOM |
| 12 | "MUSINIQUE — RESOURCES + PROJECTS" | B07 | ✅ | DOM |
| 13 | 19 styles / 8 sizes / 1 family / 6 of 8 bold | B08 | ✅ | computed-style tuple survey |
| 14 | Proposed scale 60/36/20/16 + 14 caption | B09 | ⬜ | This is the proposal on the table — needs Muskan to confirm these are the numbers she actually settled on |
| 15 | "BOLD STOPS AT HEADLINE." | B09 | ⬜ | Same — a design decision, not a measurement |
| 16 | "84 ACTUAL" characters per line | B10 | ✅ | canvas measureText ÷ box width, longest body paragraph |
| 17 | "45-75 COMFORTABLE" | B10 | ⚠️ | Typographic convention, not a site measurement |
| 18 | "#7D7D7D — 4.12 : 1 — FAILS AA" | B11 | ✅ | WCAG relative-luminance formula; AA normal text needs 4.5:1 |
| 19 | "#767676 — 4.54 : 1 — PASSES AA" | B11 | ✅ | Computed; lightest neutral grey clearing 4.5:1 on white |
| 20 | "64 ELEMENTS USE IT. 52 AT BODY SIZE." | B11 | ✅ | DOM leaf-element colour survey: 64 total, 16px×52 |
| 21 | Four maroon CTAs above the fold | B12 | ✅ | pixel components: all rgb(122,0,0), all 40px tall, all within y<812 |
| 22 | "VIDEO: 2.10x THE AREA." | B13 | ✅ | 395,640 px² vs 188,760 px² (DOM cross-check: 1.91× on the bare iframe) |
| 23 | "MESSAGE: 26% OF THE FRAME." | B13 | ✅ | 390 / 1503 = 25.9% |
| 24 | B14 states a principle, shows no layout | B14 | ✅ | Resolved: the proposed-layout wireframe was removed at the presenter's instruction. Nothing on screen depicts an altered hero. |
| 25 | "WEEK 3 IS THE BUILD." | B15 | ⬜ | Assumed from Week 2's shape; Muskan has not stated Week 3's scope |

## Open items — Muskan to confirm before publication

- [ ] Row 14/15 — is the four-step scale really 60 / 36 / 20 / 16 (+14 caption),
      and does bold really stop at headline?
- [ ] Row 25 — what is Week 3 actually? B15 and B16 change if it isn't "the build".

## Deliberately NOT claimed on screen

- The site's true accent token is #7A0000, not the #64140E this series uses.
  Recorded in SOURCES.md; not stated on screen, because the series palette is
  locked to Week 1 and the difference would confuse more than it informs.
- Week 1 said the footer holds "8 unlabeled project names". That was the count
  visible in the Week 1 screenshot crop. Week 2 states the measured column
  total (11) and the bare-proper-noun count (6) rather than relitigating it.
