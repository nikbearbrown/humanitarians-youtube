# SHOTLIST — vox-warburg-carbon
## Why Cancer Cells Run an Inefficient Engine on Purpose

---

## Shot-type histogram
| Type | Count | Beats |
|---|---|---|
| CARD | 4 | B01, B03, B08, B14 |
| GRAPHIC (own) | 8 | B02, B04, B06, B07, B09, B11, B12, B13 |
| STILL (ai) | 2 | B05, B10 |
**Total: 14 beats**

Rhythm check: max consecutive same type = 4 GRAPHIC (B06–B07–B09–B11, with CARD B08 between B07 and B09 — so no consecutive run exceeds 2 between fills). Actual: B06–B07 GRAPHIC/GRAPHIC (2), then B08 CARD breaks it, then B09 GRAPHIC alone, then B10 STILL breaks it. No violation.

---

## Act map
| Beat | Act | Type |
|---|---|---|
| B01–B02 | COLD OPEN | CARD, GRAPHIC |
| B03 | THE QUESTION | CARD |
| B04–B05 | THE PROBLEM | GRAPHIC, STILL |
| B06–B09 | THE MECHANISM | GRAPHIC×3, CARD |
| B10–B11 | THE IMPLICATION | STILL, GRAPHIC |
| B12–B13 | THE EXAMPLE | GRAPHIC×2 |
| B14 | RECAP | CARD |

---

## Color law
- **TEAL `#1F6F5C`** = efficient/kept/built — carbon that becomes structure (nucleotides, lipids, serine), the TEAL bars and branches
- **CRIMSON `#BF3339`** = wasted/excreted/lost — lactate, CO2, the naive expectation of pure oxidation
- **GOLD `#F5D061`** = editor's-pen highlighter only, never text (available once per graphic, used in B03 question card if desired)
- Two accents max: TEAL + CRIMSON. Never swap mid-film.

---

## Exclusion confirmations
- NO HIF-1alpha or VHL mechanism (separate cards 11 and 12 in video-ideas.md)
- NO specific enzyme kinetics (PDK1, LDHA, HK2 not named as enzymes — HK2 mentioned only as "same enzyme" in B10 narration at the conceptual level)
- NO detailed TCA cycle chemistry
- NO isotope-tracing experiments mentioned
- NO Otto Warburg history beyond the one sentence in B08 narration
- NO oncogenic signaling pathways driving HIF

---

## Estimated total duration
14 beats × avg ~12s = ~168s estimated. Actual will be set after audio lock. Well under 5:00 cap.

---

## Per-beat work order

### B01 — Title card
**Type:** CARD · source: own · motion: hold
Own Manim scene: `B01_Title`. TEAL eyebrow "CANCER BIOLOGY". No fill-in slot.

---

### B02 — 2 vs 30 ATP bar chart
**Type:** GRAPHIC · source: own · motion: drawon
Own Manim scene: `B02_TwoBar`. No fill-in slot.

---

### B03 — The Question card
**Type:** CARD · source: own · motion: hold
Own Manim scene: `B03_Question`. No fill-in slot.

---

### B04 — Quiescent cell: glucose to CO2
**Type:** GRAPHIC · source: own · motion: drawon
Own Manim scene: `B04_QuiescentCell`. No fill-in slot.

---

### B05 — Dividing cell (STILL · ai)
**Type:** STILL · source: ai · motion: kenburns
**FILL-IN SLOT — human provides image.**

**Archive search:**
- Wikimedia Commons: `cell division mitosis diagram` https://commons.wikimedia.org/wiki/Category:Mitosis
- Wikimedia: `cytokinesis diagram` https://commons.wikimedia.org/w/index.php?search=cytokinesis
- NCI Visuals Online: https://visualsonline.cancer.gov/ (search: "cell division")
- BioRender exports (if licensed): animal cell division schematic

**Generative prompt:**
```
B05, editorial illustration of an animal cell mid-division, two daughter cells beginning to separate at cytokinesis, simplified flat cross-section diagram, charcoal-ink line art on aged cream newsprint, desaturated palette no bright colors, no text labels, no gradients, biological diagram aesthetic, flat print reproduction style, top-down or slight three-quarter view, white space around the cell pair
```

---

### B06 — Complete oxidation: all carbon lost as CO2
**Type:** GRAPHIC · source: own · motion: drawon
Own Manim scene: `B06_CarbonLoss`. No fill-in slot.

---

### B07 — Carbon fate split (THE SPLIT manim move)
**Type:** GRAPHIC · source: own · motion: drawon
Own Manim scene: `B07_CarbonSplit`. No fill-in slot.

---

### B08 — Pivot section card
**Type:** CARD · source: own · motion: hold
Own Manim scene: `B08_Pivot`. No fill-in slot.

---

### B09 — Two parallel metabolic streams
**Type:** GRAPHIC · source: own · motion: drawon
Own Manim scene: `B09_TwoStreams`. No fill-in slot.

---

### B10 — PET scan image (STILL · ai)
**Type:** STILL · source: ai · motion: kenburns
**FILL-IN SLOT — human provides image.**

**Archive search:**
- Wikimedia Commons: `PET scan lymphoma` https://commons.wikimedia.org/w/index.php?search=PET+scan
- NCI Visuals Online: https://visualsonline.cancer.gov/ (search: "PET scan")
- NIH image gallery: https://www.nih.gov/news-events/images (PET, lymphoma)
- Radiology open-access archives — check license before use

**Generative prompt:**
```
B10, editorial flat graphic of a PET scan cross-section, two small lymph nodes glowing bright white-gold against a dark anatomical background rendered in muted charcoal-gray, simplified medical illustration style, no photorealism, no text labels, two circular hotspots circled with thin lines, newsprint collage treatment, flat print, cream and charcoal palette with two bright focal areas, no gradients, no color photography
```

---

### B11 — FDG trap mechanism
**Type:** GRAPHIC · source: own · motion: drawon
Own Manim scene: `B11_PETSignal`. No fill-in slot.

---

### B12 — One glucose traced (THE EXAMPLE)
**Type:** GRAPHIC · source: own · motion: drawon
Own Manim scene: `B12_ExampleTrace`. No fill-in slot.

---

### B13 — Compare outcomes (THE EXAMPLE continued)
**Type:** GRAPHIC · source: own · motion: drawon
Own Manim scene: `B13_CompareOutcomes`. No fill-in slot.

---

### B14 — Endcard / RECAP
**Type:** CARD · source: own · motion: hold
Own Manim scene: `B14_End`. No fill-in slot.

---

## Open slots (human fills)
1. **B05** — STILL · ai — dividing cell
2. **B10** — STILL · ai — PET scan image
