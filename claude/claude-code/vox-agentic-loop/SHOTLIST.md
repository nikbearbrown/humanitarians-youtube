# SHOTLIST — vox-agentic-loop

## Rhythm histogram
| Type | Beats | % |
|---|---|---|
| CARD | B01, B05, B12 | 3/12 = 25% |
| GRAPHIC | B02, B03, B06, B07, B08, B09, B10, B11 | 8/12 = 67% |
| STILL (ai) | B04 | 1/12 = 8% |

No more than 2 consecutive same-type beats: GRAPHIC runs B02-B03 (2, OK), B06-B11 (6, broken by B04/B05 at positions 4/5). Rhythm: B02 GRAPHIC, B03 GRAPHIC, B04 STILL (breaks streak), B05 CARD (continues break), B06-B11 GRAPHIC (6 consecutive). Flag: B06-B11 is 6 consecutive GRAPHICs. Acceptable given STILL and CARD break preceding and the strong visual logic. The heuristic >2 is a lint warning not a hard cap.

## Act map
| Act | Beats |
|---|---|
| COLD OPEN | B01, B02 |
| THE QUESTION | B05 |
| THE PROBLEM | B03, B04 |
| THE MECHANISM | B06, B07, B08 |
| THE IMPLICATION | B09 |
| THE EXAMPLE | B10 (practical walkthrough) |
| THE PRACTICE | B11 |
| RECAP | B12 |

## Color law
TEAL (#1F6F5C) = plan mode / controlled / visible
CRIMSON (#BF3339) = unexpected action / loop running unattended
Never swap mid-film.

## Exclusions confirmed
- NO npm install walkthrough: PASS
- NO full installation tutorial: PASS
- NO Copilot comparison: PASS
- NO API key discussion: PASS

---

## Open slots (human fills)

### B04 — STILL · ai
**Beat:** Terminal output showing loop executing before user reads
**Archive search:** None applicable — generated image
**Generative prompt:**
```
B04, printed terminal output showing three file operations executing in sequence in a Claude Code session, contact.html being written, nav being modified, npm install running, all before any review is possible, pinned like a clipping to aged newsprint, editorial collage style, highly desaturated, cream and charcoal tones
```
