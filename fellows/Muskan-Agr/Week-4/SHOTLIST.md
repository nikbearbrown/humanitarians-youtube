# SHOTLIST — humanitarians-ai-week4-navigation-cleanup-handoff
## Estimated 3:51 (230.7s) · 20 beats · 0 pantry requests · 0 new assets
##
## Runtime uses 3.03 words/sec — Week 3's own measured Kokoro pace
## (698 words / 230.55s). Week 2 measured 3.01, Week 1 measured 2.89.

| Beat | Act | Source asset | Treatment | Manim class | Est. |
|---|---|---|---|---|---|
| B00 | Intro | none | Presenter card | `B00_Intro` | 13.9s |
| B01 | Blocked | none (diagram) | Four pending rows, built | `B01_MeetingPending` | 13.2s |
| B02 | Blocked | none (black card) | Typography + mark | `B02_MoveWhatIsntBlocked` | 9.9s |
| B03 | Cleanup | none (card) | The one question, with rule | `B03_AuditBecomesWorkingDoc` | 13.2s |
| B04 | Cleanup | `06_footer.jpg` | Full-bleed + measured Projects box + 2 chips | `B04_FooterToday` | 13.2s |
| B05 | Cleanup | none (typeset) | The five names, row by row | `B05_FiveNames` | 13.2s |
| B06 | Cleanup | none (diagram) | Three before→after counters | `B06_Arithmetic` | 13.5s |
| B07 | Cleanup | none (white card) | Typography + mark | `B07_CheapestImprovement` | 11.6s |
| B08 | Cleanup | none (black card) | Status: decided / specified / not deployed | `B08_StatusNotDeployed` | 11.9s |
| B09 | Process | none (white card) | PROCESS BEFORE PIXELS | `B09_TurnToProcess` | 10.6s |
| B10 | Process | none (black card) | Where handoff friction comes from | `B10_HandoffFriction` | 7.6s |
| B11 | Process | none (diagram) | Two-option comparison, A vs B | `B11_TheQuestion` | 13.9s |
| B12 | Framework | none (diagram) | Parts 01 and 02, with rules | `B12_FrameworkOneTwo` | 14.5s |
| B13 | Framework | none (card) | Why the library compounds | `B13_LibraryCompounds` | 12.5s |
| B14 | Framework | none (diagram) | Parts 03 and 04, with rules | `B14_FrameworkThreeFour` | 12.5s |
| B15 | Framework | none (diagram) | Four state chips | `B15_InteractionStates` | 10.9s |
| B16 | Close | none (diagram) | Staged rollout rows | `B16_Rollout` | 10.6s |
| B17 | Close | none (diagram) | The four-week arc, complete | `B17_FourWeekArc` | 12.9s |
| B18 | Close | none (black card) | What remains open | `B18_StillOpen` | 8.3s |
| B19 | Outro | none (black card) | End card | `B19_EndCard` | 3.0s |

## Measured coordinates

| Constant | Element | Asset | x0 | y0 | x1 | y1 |
|---|---|---|---|---|---|---|
| `FOOTER_PROJECTS_COL` | Footer Projects column | 06 | 0.7319 | 0.0973 | 0.8071 | 0.5012 |

Reused from Week 2, where it was derived by ink-column profiling of
`06_footer.jpg` — and where it corrected Week 1's estimate, which spanned three
footer columns rather than one.

## Geometry pre-check (before any render)

B04 is the only annotated beat. Box maps to left 3.43 / bottom −0.01 / right
4.55 / top 3.22 — on-frame. The chip at y_frac 0.86 sits at y −2.88, top −2.45,
clear of the box bottom by 2.44 units, bottom edge −3.31 inside the −3.40 safe
line.

## Counts on screen — all re-measured on the live site 2026-09-06

| metric | today | after the agreed cleanup |
|---|---|---|
| Projects-column links | 11 | 6 |
| Footer column links | 33 | 28 |
| Footer anchors | 39 | 34 |
| Bare proper nouns (Week 3's count) | 6 | 1 |

**These are current-vs-agreed, not current-vs-live.** See B08 and SOURCES.md.

## Assets
- `06_footer.jpg` — B04. The only screenshot in this cut.
- The other five Week 1 assets are copied in and unused. If the cut lands short,
  the cheapest addition is a hero beat showing the nav bar with the four section
  links boxed (`NAV_SECTION_LINKS` from Week 2's SHOTLIST).

## Standing rules honoured
- No proposed layout is drawn anywhere; the site is never shown altered.
- No `Line()` anywhere — "scoped for removal" in B05 is a maroon block plus a
  label, never a strikethrough.
