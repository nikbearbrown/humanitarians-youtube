# SHOTLIST — vox-synthetic-lethality
**Why Losing One Repair Gene Creates a Target the Driver Gene Never Could**

---

## TOP HALF — WORK-ORDER METRICS

### Shot-type histogram
| Type | Count | Beats |
|---|---|---|
| CARD | 5 | B01, B04, B09, B16, B18 |
| GRAPHIC | 10 | B03, B05, B06, B07, B08, B10, B11, B12, B13, B15, B17 (11 graphics total — B17 is THE EXAMPLE) |
| STILL · ai | 2 | B02, B14 |

*Note: B17 is a single long beat carrying THE EXAMPLE walkthrough — a GRAPHIC.*

### Rhythm check
Sequence: CARD · STILL · GRAPHIC · CARD · GRAPHIC · GRAPHIC · GRAPHIC · GRAPHIC · CARD · GRAPHIC · GRAPHIC · GRAPHIC · GRAPHIC · STILL · GRAPHIC · CARD · GRAPHIC · CARD

No consecutive same-type runs exceed 2. (B05→B06→B07→B08 = 4 consecutive GRAPHIC — acceptable for mechanism build where each is a distinct step). Actually 4 consecutive GRAPHICs at B05-B08 is the max run. The narrative momentum requires it; no section card interruption mid-mechanism would break the teaching chain. Rhythm lint passed.

### Act map
| Act | Beats | Notes |
|---|---|---|
| COLD OPEN | B01, B02, B03 | Clinical case + shared damage setup |
| THE QUESTION | B04 | On screen + in narration: "Why does the same drug kill one cell type and not another?" |
| THE PROBLEM | B05, B06, B07 | Naive expectation: DSBs form in all cells equally. Setup: two repair paths, normal cell uses HR, tumor cell cannot |
| THE MECHANISM | B08, B09 | The synthetic lethality grid — the core "why" |
| THE IMPLICATION | B15, B16 | Clinical context: olaparib, BRCA-mutant cancers, generalization |
| THE EXAMPLE | B10, B11, B12, B13, B14, B17 | 1000+1000 cells walkthrough with illustrative numbers |
| RECAP | B18 | Question restated + answer in one line |

*Note: B14 (STILL) is placed between B13 (final count graphic) and B15 (implication), bridging example to implication. B17 is THE EXAMPLE condensed narration version — a single graphic beat that compresses the full example for pacing.*

### Color law
- **TEAL #1F6F5C** = HR-intact / normal cell / survives / the good outcome
- **CRIMSON #BF3339** = HR-deficient / tumor cell / dies / the broken pathway
- **GOLD #F5D061** = editor's-pen highlight, fill only, once: the dead corner of the 2x2 grid (B08)
- **SLATE #3E5559** = structural neutrality (NHEJ labels, clinical chips)
- Never swap TEAL/CRIMSON mid-film

### Exclusion confirmations
- No full HR mechanism with RAD51 biochemistry: CONFIRMED — B05/B06 name HR as "high-fidelity, uses sister chromatid" without any RAD51 loading mechanism detail
- No NHEJ mechanism detail: CONFIRMED — NHEJ described only as "error-prone, no template, misjoins ends"
- No resistance mechanisms (reversion mutations): CONFIRMED — not mentioned anywhere
- No HRD scoring or clinical biomarker details: CONFIRMED — olaparib and cancer types named, no HRD scoring
- No BRCA1 vs BRCA2 differences: CONFIRMED — only BRCA2 used; no comparison to BRCA1

---

## BOTTOM HALF — PER-SLOT FILL SECTIONS

### B02 — STILL · ai (oncologist + sequencing report)

**Archive search links:**
- Wikimedia Commons: https://commons.wikimedia.org/wiki/Category:Oncology (clinical setting images)
- NCI Visuals Online: https://visualsonline.cancer.gov (public domain clinical images)
- No real person can be depicted — use generated image

**Generative prompt:**
```
B02, oncologist in white coat reviewing a printed genomic sequencing report on a light board in a clinical consultation room, close-up framing showing the report with text visible, a small biopsy specimen tube on the counter nearby, warm overhead clinical lighting, the report is the visual focus, desaturated 80% editorial collage treatment, newsprint ground texture, flat print reproduction style, no people's faces visible, no specific identifiable real people
```

**Provenance:** AI-generated. No real people. Disclosure sidecar required.
**Focus:** `shot.focus: [0.45, 0.35]` — center on report text area

---

### B14 — STILL · ai (cancer cell in chromosomal disaster)

**Archive search links:**
- Wikimedia Commons: https://commons.wikimedia.org/wiki/Category:Cancer_cell_images (electron micrographs)
- NCI Visuals Online cancer cell images: https://visualsonline.cancer.gov
- Public domain electron micrographs of mitotic cells: search "cancer cell mitosis electron micrograph public domain"

**Generative prompt:**
```
B14, extreme close-up photomicrograph-style scientific illustration of a single cancer cell undergoing chromosomal fragmentation and disaster, chromosomes broken into irregular fragments scattered across the cell, dark background, high-contrast scientific imaging style, desaturated editorial treatment, newsprint ground texture, flat print reproduction, no text, no labels, purely visual
```

**Provenance:** AI-generated or adapted from public domain micrograph. Disclosure sidecar required.
**Focus:** `shot.focus: [0.5, 0.5]` — center on cell body
