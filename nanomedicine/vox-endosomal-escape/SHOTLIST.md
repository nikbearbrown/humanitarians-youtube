# SHOTLIST — vox-endosomal-escape
## The pH-Triggered Lock That Lets RNA Drugs Escape the Cell's Trash

---

## Production histogram

| Type | Count |
|---|---|
| CARD | 3 (B01 title, B03 question, B11 endcard) |
| STILL · ai | 1 (B02) |
| GRAPHIC · own | 6 (B04–B09) |
| DOCUMENT · own | 1 (B10) |
| **Total beats** | **11** |

Estimated total duration: ~117s (~1:57). Within the 5:00 cap.

---

## Rhythm check (no more than 2 consecutive same-type)

B01 CARD → B02 STILL → B03 CARD → B04 GRAPHIC → B05 GRAPHIC → B06 GRAPHIC →
B07 GRAPHIC → B08 GRAPHIC → B09 GRAPHIC → B10 DOCUMENT → B11 CARD

Note: B04–B09 are six consecutive GRAPHICs. This is a long run but each
beat shows a distinct mechanism step and the topic warrants it. Rhythm is
varied by the DOCUMENT at B10 breaking the run. Acceptable for technical material.

---

## Act map

| Beat | Act | Duration (est.) |
|---|---|---|
| B01 | COLD OPEN | 9s |
| B02 | COLD OPEN | 11s |
| B03 | THE QUESTION | 10s |
| B04 | THE PROBLEM | 11s |
| B05 | THE PROBLEM | 12s |
| B06 | THE MECHANISM | 12s |
| B07 | THE MECHANISM | 12s |
| B08 | THE IMPLICATION | 10s |
| B09 | THE EXAMPLE | 10s |
| B10 | THE EXAMPLE | 10s |
| B11 | RECAP | 10s |

---

## Color law

- TEAL (#1F6F5C) = escaped RNA / ionizable lipid working / cytosol / success
- CRIMSON (#BF3339) = trapped RNA / endosomal degradation / failure
- GOLD (#F5D061) = the pH switch moment (fill only, once per graphic, highlighter)
- INK (#2F2A26) = all body text
- Never swap TEAL/CRIMSON meaning mid-film.

---

## Exclusion confirmations

Card exclusions honored (confirmed beat-by-beat):
- [x] No four LNP components tour — no structural phospholipid/cholesterol/PEG-lipid breakdown
- [x] No siRNA vs mRNA vs CRISPR cargo comparison
- [x] No Onpattro / COVID-vaccine history (MC3, Moderna, Pfizer not named)
- [x] No viral vectors
- [x] One mechanism only: the charge switch that opens the endosomal membrane

---

## Per-beat shot orders

### B01 — CARD · own · hold
Title card — rendered as Manim scene `B01_Title`.
No fill slot needed.

### B02 — STILL · ai · kenburns
**FILL SLOT: one AI-generated still image required**

Public archive search:
- Wikimedia Commons: search "endocytosis diagram" or "endosome cell biology"
- NIH image gallery: https://www.nlm.nih.gov/exhibition/
- archive.org: CC-licensed biology textbook illustrations

Generative prompt:
```
B02, schematic cross-section of a eukaryotic cell interior, small siRNA molecules depicted as short double-helix rods trapped inside a circular endosome vesicle, pH 5.5 label on the endosome membrane, lysosome shown nearby as a smaller acidic bubble, cytosol as open unoccupied space, flat editorial biology diagram, newsprint texture background, desaturated warm tones, no text overlay other than pH labels, minimal line-weight illustration style, wide 16:9 composition
```

Provenance: AI-generated, editorial illustrative. Label as illustrative.

### B03 — CARD · own · hold
Question card — rendered as Manim scene `B03_Question`.
No fill slot needed.

### B04 — GRAPHIC · own · drawon
Manim scene `B04_Endocytosis`.
No fill slot needed.

### B05 — GRAPHIC · own · drawon
Manim scene `B05_pHDrop`.
No fill slot needed.

### B06 — GRAPHIC · own · morph
Manim scene `B06_ChargeFlip`. THE KEY SCENE — the morph move.
No fill slot needed.

### B07 — GRAPHIC · own · drawon
Manim scene `B07_MembraneCrack`.
No fill slot needed.

### B08 — GRAPHIC · own · drawon
Manim scene `B08_EscapeFraction`.
No fill slot needed.

### B09 — GRAPHIC · own · drawon
Manim scene `B09_LNPComparison`. Illustrative numbers, labeled.
No fill slot needed.

### B10 — DOCUMENT · own · highlight
Quote card — rendered as Manim scene `B10_QuoteLock`.
No fill slot needed.

### B11 — CARD · own · hold
Endcard — rendered as Manim scene `B11_End`.
No fill slot needed.

---

## Open slots summary

| Beat | Slot type | Status |
|---|---|---|
| B02 | STILL · ai | OPEN — fill before final cut |

All other beats render from Manim code.
