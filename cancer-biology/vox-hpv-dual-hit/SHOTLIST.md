# SHOTLIST — vox-hpv-dual-hit
## Why Two Checkpoints Fail When One Virus Infects

---

## Histogram

| Shot type | Beat count | % |
|---|---|---|
| CARD | 4 (B01, B03, B07, B14) | 29% |
| STILL | 1 (B02) | 7% |
| GRAPHIC | 9 (B04–B06, B08–B13) | 64% |

Rhythm check: No >2 consecutive same-type beats. B01 (CARD) -> B02 (STILL) -> B03 (CARD) -> B04-B13 (GRAPHIC, broken by B07 CARD at beat 7) -> B14 (CARD). Clean.

## Act map

| Beat | Act |
|---|---|
| B01 | COLD OPEN |
| B02 | COLD OPEN |
| B03 | THE QUESTION |
| B04–B06 | THE PROBLEM |
| B07 | Section CARD |
| B08–B10 | THE MECHANISM |
| B11–B12 | THE IMPLICATION |
| B13 | THE EXAMPLE |
| B14 | RECAP |

## Color law

TEAL (#1F6F5C) = intact / functional / normal cell circuits, healthy checkpoints.
CRIMSON (#BF3339) = disabled / hijacked / lost — E6, E7, destroyed p53, freed E2F.
GOLD = editor's pen highlight, used once (B10, the dual-arm split convergence node).
Two accents only.

## Exclusion confirmations

- No HPV type taxonomy beyond naming HPV-16 (and HPV-18 noted only in parenthetical context from chapter). CONFIRMED absent.
- No CIN grading system detail. CONFIRMED absent.
- No other viral carcinogens (EBV, KSHV, HBV, HCV, HTLV). CONFIRMED absent.
- No HPV vaccine mechanism. CONFIRMED absent.
- No integration vs episomal HPV distinction. CONFIRMED absent.
- All illustrative numbers (B13 example) labeled illustrative in FACTCHECK.

---

## Per-beat work orders

### B01 — CARD (own) — Title card
Type: CARD · Source: own · Motion: hold
Manim scene: `B01_Title`
Eyebrow chip: "CANCER BIOLOGY" in TEAL. Headline: "Why Two Checkpoints Fail When One Virus Infects" in INK. No fill slots.

---

### B02 — STILL (ai) — Cervical cell under HPV assault
Type: STILL · Source: ai · Motion: kenburns · Focus: [0.5, 0.4]

**Archive search links:**
- Wikimedia Commons: https://commons.wikimedia.org/w/index.php?search=cervical+epithelial+cell+HPV+microscopy
- NIH Image Gallery: https://www.nih.gov/news-events/images
- NCI Visuals Online: https://visualsonline.cancer.gov/

**Generative prompt:**
```
B02, cross-section diagram of a human cervical epithelial cell being contacted by HPV-16 virus particles, schematic illustration style, newsprint treatment desaturated 80% contrast 1.15, cream ground, small icosahedral virus particles shown at cell surface, cell nucleus visible, clinical scientific illustration, no text, no labels, cool muted palette, bird's-eye angle, diffuse overhead light, no people, no background clutter
```

---

### B03 — CARD (own) — The question card
Type: CARD · Source: own · Motion: hold
Manim scene: `B03_Question`
No fill slots.

---

### B04 — GRAPHIC (own) — Two-hit mutation expectation
Type: GRAPHIC · Source: own · Motion: drawon
Manim scene: `B04_TwoHitExpectation`
No fill slots.

---

### B05 — GRAPHIC (own) — p53 circuit (intact)
Type: GRAPHIC · Source: own · Motion: drawon
Manim scene: `B05_P53Circuit`
No fill slots.

---

### B06 — GRAPHIC (own) — Rb/E2F gate (intact)
Type: GRAPHIC · Source: own · Motion: drawon
Manim scene: `B06_RbGate`
No fill slots.

---

### B07 — CARD (own) — Section card: THE MECHANISM
Type: CARD · Source: own · Motion: hold
Manim scene: `B07_SectionMechanism`
No fill slots.

---

### B08 — GRAPHIC (own) — E6 degrades p53
Type: GRAPHIC · Source: own · Motion: drawon
Manim scene: `B08_E6Degrades`
No fill slots.

---

### B09 — GRAPHIC (own) — E7 displaces E2F from Rb
Type: GRAPHIC · Source: own · Motion: drawon
Manim scene: `B09_E7Displaces`
No fill slots.

---

### B10 — GRAPHIC (own) — Dual-arm split: both circuits dark
Type: GRAPHIC · Source: own · Motion: split
Manim scene: `B10_DualArmSplit`
No fill slots.

---

### B11 — GRAPHIC (own) — Gene intact, protein gone
Type: GRAPHIC · Source: own · Motion: hold
Manim scene: `B11_GenVsProtein`
No fill slots.

---

### B12 — GRAPHIC (own) — Damage accumulation timeline
Type: GRAPHIC · Source: own · Motion: accumulate
Manim scene: `B12_DamageAccumulation`
No fill slots.

---

### B13 — GRAPHIC (own) — THE EXAMPLE: UV in normal vs HPV cell
Type: GRAPHIC · Source: own · Motion: compare
Manim scene: `B13_UVExample`
No fill slots.

---

### B14 — CARD (own) — Endcard / RECAP
Type: CARD · Source: own · Motion: hold
Manim scene: `B14_End`
No fill slots.

---

## Media economy note

1 STILL (ai) across ~255s runtime (~4:15) = 1 still per ~255s. Card says "3-5 min"; one still is appropriate for the length (one per ~90s would be 2-3; one is lean but the heavy graphic density in THE MECHANISM justifies the single still at the cold-open boundary). Placement: B02 at the COLD OPEN / QUESTION boundary.
