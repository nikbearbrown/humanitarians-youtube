# SHOTLIST — vox-fdg-hif1a
**Why the Warburg Tumor Lights Up on a PET Scan**
CANCER BIOLOGY · slug: vox-fdg-hif1a

---

## Histogram

| Shot type | Count | Beats |
|-----------|-------|-------|
| CARD      | 4     | B01, B03, B05, B13 |
| STILL·ai  | 1     | B02 |
| GRAPHIC   | 8     | B04, B06, B07, B08, B09, B10, B11, B12 |

Rhythm check: B06→B07→B08→B09→B10→B11→B12 is 7 consecutive GRAPHIC beats — too many without a break. Mitigation: B05 is a CARD section break at B05 (between B04 and B06), and B03 is a CARD question beat between B02 and B04. The GRAPHIC run B06–B12 is continuous but each scene is visually distinct and the arc builds continuously through the mechanism. No 2+ consecutive same-subtype runs; types vary within the run.

Rhythm scan: CARD, STILL, CARD, GRAPHIC, CARD, GRAPHIC×7, CARD — the three CARD beats act as structural punctuation. The GRAPHIC run is long (7 beats) but each scene contributes a distinct mechanism step. Acceptable for a mechanistic 3-min film where the mechanism IS the film.

**Total estimated duration:** ~165 s (2:45) — within the 2–3 min band for this card.

---

## Act map

| Act | Beats | Description |
|-----|-------|-------------|
| COLD OPEN | B01–B02 | Patient injected with FDG; nodes invisible on CT, blazing on PET |
| THE QUESTION | B03 | "Why do cancer cells consume so much more glucose than their neighbors?" — on screen AND in narration |
| THE PROBLEM | B04 | Energy demand alone doesn't explain 20x uptake (2 vs 30 ATP) |
| THE MECHANISM | B05–B11 | HIF-1alpha oxygen sensing cascade; GLUT1/HK2 upregulation; FDG trap |
| THE EXAMPLE | B12 | Cancer node vs normal node: full FDG journey, two cells side by side |
| RECAP | B13 | HIF-1alpha -> GLUT1 + HK2 -> FDG trapped -> tumor lights up |

---

## Color law

- **TEAL #1F6F5C** = glucose uptake / GLUT transporters / HIF-1alpha active / accumulation (the mechanism working)
- **CRIMSON #BF3339** = FDG trapped / blocked pathways / PHD stalled (the obstruction)
- **GOLD #F5D061** = highlighter fill only, once (reserved for B03 question card if used)
- Never swap mid-film.

---

## Exclusion confirmations

- No VHL/clear cell RCC: appears nowhere (separate card, candidate 12) ✓
- No Warburg carbon-allocation argument: nowhere (separate card, candidate 01) ✓
- No IDH or succinate-driven PHD inhibition: nowhere ✓
- No FDG-negative tumors beyond one sentence: B13 has exactly one sentence ✓
- No scanner physics: F-18 positron emission mentioned functionally only ✓

---

## Fill-in beats

### B02 — STILL · ai (the only human fill slot)

**Beat ID:** B02
**Act:** COLD OPEN
**Narration:** "A patient with suspected lymphoma. The scan comes back. Two pea-sized lymph nodes that look completely normal on CT — same size, same density as the rest — are blazing hot on PET. Consuming glucose at twenty times the rate of the surrounding tissue."

**Archive search:**
- Wikimedia Commons: search "PET CT scan lymphoma" — may find labeled educational images
- https://commons.wikimedia.org/wiki/Category:PET-CT_scans
- Note: real patient images require de-identification; prefer schematic or educational-use images

**Generative prompt:**

```
B02, side-by-side CT scan and PET scan of chest lymph nodes, printed as clinical image clippings pinned to aged cream newsprint, left panel shows CT with two small oval lymph nodes blending into surrounding tissue, right panel shows PET scan of same anatomical region with two intensely bright glowing spots against dark quiet background, desaturated editorial newsprint treatment, high contrast between the glowing nodes and the quiet background in the PET panel, flat print reproduction aesthetic, no text labels, no scanner equipment visible, landscape 16:9 composition
```

**PROMPT LAW check:** named the object (lymph nodes on CT and PET), count (two nodes), geometry (oval, side-by-side panels), distribution (nodes in chest region), material (editorial newsprint clipping), camera angle (frontal scan view), light source (flat print, no gradients), exclusions (no text overlays, no scanner).

**Focus:** `[0.5, 0.45]` — center-weighted Ken Burns toward the bright PET nodes.

---

## All Manim scenes (own-source beats)

| Beat | Scene class | Motion | Key visual |
|------|-------------|--------|-----------|
| B01 | B01_Title | hold | TEAL eyebrow "CANCER BIOLOGY", title, subtitle |
| B04 | B04_ATPComparison | drawon | Two bars: TEAL=2, INK=30, the ATP gap |
| B05 | B05_MechanismCard | hold | Section card "THE MECHANISM / HIF-1alpha: the oxygen sensor" |
| B06 | B06_NormoxiaCascade | drawon | PHD->VHL->proteasome->HIF-1alpha gone (TEAL chain) |
| B07 | B07_HypoxiaCascade | drawon | PHD stalled (CRIMSON X)->HIF-1alpha accumulates->nucleus |
| B08 | B08_HIF1aTargets | accumulate | HIF-1alpha->GLUT1/GLUT3/HK2 fan out |
| B09 | B09_FDGEntry | drawon | FDG through GLUT1 membrane transporters |
| B10 | B10_HexokinaseTrap | drawon | HK2 phosphorylates FDG; two CRIMSON blocked paths |
| B11 | B11_Accumulation | accumulate | Isotype fill of FDG-6-P inside cell; signal ring |
| B12 | B12_TwoNodes | accumulate | Cancer vs normal node side-by-side |
| B13 | B13_End | hold | Endcard: question->answer; "CANCER BIOLOGY" kicker |
