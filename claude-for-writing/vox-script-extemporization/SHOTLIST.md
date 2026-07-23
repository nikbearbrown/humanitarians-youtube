# SHOTLIST — vox-script-extemporization
## Why the Script Made the Extemporization Possible

---

## Histogram

| Shot type | Count | % |
|---|---|---|
| STILL (archive) | 1 | 7% |
| STILL (ai) | 1 | 7% |
| CARD (own) | 2 | 14% |
| GRAPHIC (own) | 10 | 71% |

No more than 2 consecutive same-type beats. Rhythm check: B01 STILL → B02 CARD → B03 GRAPHIC → B04 GRAPHIC → B05 GRAPHIC → B06 GRAPHIC → B07 GRAPHIC → B08 GRAPHIC → B09 STILL → B10 GRAPHIC → B11 GRAPHIC → B12 GRAPHIC → B13 GRAPHIC → B14 CARD. Three consecutive GRAPHIC beats (B03–B08 and B10–B13) — acceptable as mechanism beats; split by STILL at B09 and bookended by CARD.

---

## Act map

| Beat | Act | Duration est. |
|---|---|---|
| B01 | COLD OPEN | 12s |
| B02 | COLD OPEN | 10s |
| B03 | THE QUESTION | 13s |
| B04 | THE PROBLEM | 11s |
| B05 | THE PROBLEM | 11s |
| B06 | THE MECHANISM | 12s |
| B07 | THE MECHANISM | 12s |
| B08 | THE MECHANISM | 13s |
| B09 | THE IMPLICATION | 12s |
| B10 | THE IMPLICATION | 13s |
| B11 | THE EXAMPLE | 14s |
| B12 | THE EXAMPLE | 13s |
| B13 | THE PRACTICE | 13s |
| B14 | RECAP | 12s |

**Total estimated: ~171s (~2:51). Within 3–5 min band. Hard cap 5:00 — CLEAR.**

---

## Color law

TEAL (#2A1A0E = plain INK in teardown palette) = the spoken / ear-adapted technique — what survives the ear.
CRIMSON (#C8102E) = the page-prose form that fails the ear — long sentences, repetition-as-padding, abstraction.
Never swapped mid-film.

---

## Exclusions confirmed

- NO delivery coaching beyond naming pace/pause/pitch as tools (no demonstration, no full coaching section)
- NO full speech content beyond the Gettysburg and "I Have a Dream" excerpts used as worked examples
- NO broader civil rights context — King and Lincoln appear only as demonstration of the three techniques
- NO civil rights history, no debate over speech versions, no political context of 1963

---

## Per-slot fill-in sections

### B01 — STILL · archive

**Beat:** B01 — COLD OPEN (12s)
**Required:** Archival photograph of Martin Luther King Jr. at the Lincoln Memorial podium, August 28, 1963, crowd visible along the reflecting pool.

**Archive search:**
- Wikimedia Commons: https://commons.wikimedia.org/wiki/File:March_on_Washington_edit.jpg (Warren K. Leffler, US News & World Report, LOC — public domain via LOC)
- Library of Congress: https://www.loc.gov/pictures/collection/ppmsca/ (search "March on Washington 1963")
- Getty/AP archive for licensed use: search "King Lincoln Memorial 1963 podium"

**Provenance note:** Warren K. Leffler / U.S. News & World Report photos are in the public domain (LOC). Use the highest-resolution scan available. Verify attribution against the LOC catalog record before ship.

Ken Burns direction: slow push toward King at the lectern. `shot.focus: [0.5, 0.35]` — motivates the zoom toward King's face and the prepared text on the podium.

```
B01, archival photograph, Martin Luther King Jr. standing at a wooden podium
at the Lincoln Memorial, August 28 1963, crowd stretching back along the
reflecting pool visible in distance, desaturated editorial newsprint treatment,
flat documentary reproduction, no overlay text, 16:9 landscape format
```

---

### B09 — STILL · ai

**Beat:** B09 — THE IMPLICATION (12s)
**Required:** Lincoln at Gettysburg, period illustration — a rendering of the Gettysburg Address scene, November 1863.

**Archive search (period illustrations, PD):**
- Wikimedia Commons: https://commons.wikimedia.org/wiki/Battle_of_Gettysburg (search "Gettysburg Address crowd" or "Lincoln at Gettysburg 1863")
- LOC prints: https://www.loc.gov/pictures/ (search "Gettysburg Address ceremony 1863")
- Harper's Weekly 1863 reproductions on Wikimedia

If no suitable archive image found, generate via ai:

```
B09, Lincoln at Gettysburg Address, November 1863, period illustration style,
engraving or lithograph reproduction aesthetic, crowd gathered before a speaker's
platform, tall figure at podium center, overcast Pennsylvania November sky,
desaturated editorial newsprint treatment, 16:9 landscape, no text overlay,
realistic historical scene, muted period palette, flat reproduction lighting
```

Ken Burns direction: slow push across the crowd toward the platform. `shot.focus: [0.5, 0.4]`.

---
