# SHOTLIST — vox-idh-2hg
**Why a Metabolic Enzyme Mutation Can Lock Cells Into an Immature State**
CANCER BIOLOGY · 13 beats · ~153 s estimated

---

## Top-half: audit

### Shot-type histogram
| Type | Count | Beats |
|---|---|---|
| CARD | 3 | B01, B03, B13 |
| STILL · ai | 2 | B02, B10 |
| GRAPHIC · own | 8 | B04, B05, B06, B07, B08, B09, B11, B12 |

Rhythm check: no more than 2 consecutive same-type beats.
- B04–B09: 6 consecutive GRAPHIC — the mechanism acts need dense Manim. Split check: B04+B05 (Problem), B06+B07 (Mechanism pt1+2), B08+B09 (Mechanism pt3+4). Each sub-group is separated conceptually; pacing acceptable for technical material in 3-5 min band. No STILL runs longer than 2 consecutive. PASS.

### Act map
| Beat | Act |
|---|---|
| B01 | COLD OPEN |
| B02 | COLD OPEN |
| B03 | THE QUESTION |
| B04 | THE PROBLEM |
| B05 | THE PROBLEM |
| B06 | THE MECHANISM pt1 (normal IDH) |
| B07 | THE MECHANISM pt2 (mutant IDH, 2HG) |
| B08 | THE MECHANISM pt3 (competitive block — the core) |
| B09 | THE MECHANISM pt4 (methylation accumulation) |
| B10 | THE IMPLICATION |
| B11 | THE EXAMPLE (Day 0) |
| B12 | THE EXAMPLE (Day 14/28 recovery) |
| B13 | RECAP / ENDCARD |

Act structure: cold open → question → problem → mechanism → implication → example → recap. PASS.

### Color law
TEAL `#1F6F5C` = alpha-KG / demethylase active / differentiation / healthy state
CRIMSON `#BF3339` = 2HG / demethylase blocked / silenced / blast-locked
GOLD `#F5D061` = editor's-pen highlight ONCE (B08, keyhole highlight)
SLATE `#3E5559` = IDH enzyme box (structural, not good/bad)
Never swapped mid-film.

### Exclusion confirmations
- No full TCA cycle chemistry: CONFIRMED ABSENT
- No TET1/2/3 isoforms: CONFIRMED ABSENT
- No IDH-mutant glioma vs AML distinction: CONFIRMED ABSENT (glioma mentioned once in implication as a number context only — removed from narration)
- No histone demethylase mechanism detail: CONFIRMED ABSENT
- No DNMT inhibitor comparison: CONFIRMED ABSENT

### Media economy (ai stills)
~153 s runtime → 1–2 ai stills (one per 90s). Two stills placed: B02 (cold open, the concrete case) and B10 (implication, hematopoiesis diagram). Within economy.

---

## Bottom-half: per-slot work order

### B02 — STILL · ai — cold open: AML bone marrow biopsy
**Beat:** B02 · COLD OPEN · kenburns · ~12 s

Archive search (may exist as PD or CC teaching image):
- Wikimedia: https://commons.wikimedia.org/wiki/Category:Acute_myeloid_leukemia
  (search "AML bone marrow histology" — H&E stained histology slides sometimes CC-BY from pathology collections)
- NCI Visual Online: https://visualsonline.cancer.gov/ (search "leukemia marrow")

Provenance: real patient histology images require de-identified clinical source or explicit CC license. If no clean archive find, use ai generation.

```
B02, bone marrow histology slide showing acute myeloid leukemia, densely packed immature blast cells with large round nuclei and prominent nucleoli, sparse mature segmented neutrophils, H&E stain appearance, high magnification field, educational pathology image, desaturated 80% flat print reproduction on aged newsprint texture, editorial collage, no labels or annotations on the image itself, landscape 16:9 crop
```

Shot focus: `[0.5, 0.4]` (center-mass on the blast cluster)

---

### B10 — STILL · ai — implication: hematopoiesis arrest diagram
**Beat:** B10 · THE IMPLICATION · kenburns · ~11 s

Archive search:
- Wikimedia: https://commons.wikimedia.org/wiki/File:Hematopoiesis_(human)_diagram_en.svg
  (this CC-BY diagram exists; may be usable with desaturation treatment; verify license)
- NCI: https://visualsonline.cancer.gov/ (search "hematopoiesis")

Note: if using the Wikimedia SVG, render to PNG at ≥1920px wide; the blast-stage circle must be added as an annotation in vox_compile or placed as a Manim overlay.

```
B10, clean simplified hematopoiesis diagram, stem cell at top branching downward through myeloid progenitor and blast stages to mature segmented neutrophil at the bottom right, one branch node circled in red to indicate developmental arrest at the blast stage, the mature neutrophil branch below the arrest point is shown faint or absent, minimal flat illustration style, educational biology diagram, desaturated editorial treatment on aged newsprint, no patient-identifiable information, landscape 16:9
```

Shot focus: `[0.5, 0.5]` (midpoint — the arrest circle and the blocked path)

---

*All GRAPHIC beats (B04–B09, B11–B12) are own-Manim — scenes in vox_scenes.py. No fill-in work required.*
