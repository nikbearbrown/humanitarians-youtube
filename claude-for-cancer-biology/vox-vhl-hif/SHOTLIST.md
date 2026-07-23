# SHOTLIST — vox-vhl-hif
## Why a Broken Oxygen Sensor Causes a Cancer to Act Permanently Starved

---

## Histogram

| Shot type | Count | % of 15 beats |
|---|---|---|
| CARD | 5 | 33% |
| GRAPHIC (own) | 7 | 47% |
| STILL (ai) | 2 | 13% |
| DOCUMENT | 0 | 0% |
| COMPOSITE | 0 | 0% |
| FOOTAGE | 0 | 0% |

Rhythm check: no run of more than 2 consecutive same-type beats.
- B01 CARD, B02 STILL, B03 GRAPHIC, B04 CARD, B05 GRAPHIC, B06 CARD, B07 GRAPHIC, B08 GRAPHIC, B09 GRAPHIC, B10 GRAPHIC, B11 CARD, B12 STILL, B13 GRAPHIC, B14 GRAPHIC, B15 CARD
- Longest GRAPHIC run: B07–B10 (four consecutive) — flagging this; B06 CARD and B11 CARD break the visual monotony adequately at that arc's boundaries. Within acceptable range given the mechanism requires four graphics to build.

## Act map

| Beat | Act |
|---|---|
| B01 | COLD OPEN — title card, concrete situation stated |
| B02 | COLD OPEN — clear cell RCC key case: the paradox |
| B03 | COLD OPEN — HIF-1alpha as the driver |
| B04 | THE QUESTION — named on screen and in narration |
| B05 | THE PROBLEM — naive expectation (intact sensor should = HIF destroyed) |
| B06 | SECTION CARD — THE MECHANISM |
| B07 | THE MECHANISM — normal VHL degradation pathway |
| B08 | THE MECHANISM — VHL absent, HIF accumulates |
| B09 | THE MECHANISM — constitutive HIF program in normoxia |
| B10 | THE MECHANISM — compare graphic: normal vs VHL-null |
| B11 | SECTION CARD — THE IMPLICATION |
| B12 | THE IMPLICATION — downstream consequences of VHL loss |
| B13 | THE EXAMPLE — normal cell half-life timeline (illustrative) |
| B14 | THE EXAMPLE — VHL-null cell 4-hour accumulation (illustrative) |
| B15 | RECAP — endcard, question answered |

Estimated duration: ~228 seconds (~3:48). Within 3–5 min band. Hard cap 5:00. Pass.

## Color law

TEAL `#1F6F5C` = working degradation pathway / HIF destroyed / normal cell outcome.
CRIMSON `#BF3339` = VHL absent / HIF accumulating / cancer cell outcome.
GOLD `#F5D061` = single editor's highlight on the missing VHL node (B08) and the 40x accumulation label (B14) — one use per scene, never text.
Two accents maximum. Never swapped mid-film.

## Exclusion confirmations

- No full prolyl hydroxylase biochemistry — PHDs named and noted as "hydroxylate HIF-1a," nothing more. CONFIRMED absent.
- No HIF-1alpha vs HIF-2alpha distinction beyond a belzutifan mention — the endcard/recap names HIF but never distinguishes paralogs; belzutifan is excluded from on-screen content entirely (it appeared in the chapter but the card excludes it). CONFIRMED absent.
- No oncogenic pseudohypoxia routes (SDH, KRAS, MYC) — these appear in the chapter but not in any beat. CONFIRMED absent.
- No VEGF/angiogenesis mechanism detail — VEGF named as an output only. CONFIRMED absent.

---

## Slot work orders — fill-in beats

### B02 — STILL · ai (clear cell RCC histology)

**Beat:** COLD OPEN — the key case, the visual paradox of clear lipid-loaded cells expressing hypoxic program.

Public archive search:
- Wikimedia Commons: search "clear cell renal cell carcinoma histology" — several H&E photomicrographs available under CC license.
  - https://commons.wikimedia.org/wiki/Category:Clear_cell_renal_cell_carcinoma
- Armed Forces Institute of Pathology (AFIP) histology collections: no direct API, but open-access images appear on PathologyOutlines.com (check license per image).

Provenance note: real H&E photomicrographs of human tumor tissue require CC-BY or public domain license; if using archive material, verify the specific image license before use.

Generative prompt:

```
B02, editorial histology-style photomicrograph of clear cell renal cell carcinoma tissue, pale vacuolated cytoplasm from lipid and glycogen accumulation, grid of rounded clear cells under microscope, H&E stain, teal annotation label chips reading GLUT1 and VEGF pinned to the image like editorial callouts, desaturated newsprint collage treatment, flat editorial print reproduction, no text overlay on cells themselves, wide field of view showing 20-30 cells, clinical pathology aesthetic
```

---

### B12 — STILL · ai (editorial consequence schematic)

**Beat:** THE IMPLICATION — downstream consequences of VHL loss diagrammed schematically.

Public archive search:
- No obvious archival photograph fits this beat (it is an editorial diagram). Recommend generative.
- Alternatively: a kidney gross specimen or macroscopic clear cell RCC tumor cross-section exists on Wikimedia; could substitute with gross pathology image if an editorial schematic is preferred over a generated graphic.

Generative prompt:

```
B12, editorial diagram on aged newsprint background, central circular node labeled VHL ABSENT in bold crimson serif type, three diverging bold arrows pointing to three labeled rectangular outcome boxes, top arrow to box labeled GLUT1 HIGH parenthetical glucose uptake, middle arrow to box labeled GLYCOLYTIC ENZYMES HIGH parenthetical Warburg metabolism, bottom arrow to box labeled VEGF HIGH parenthetical angiogenesis, all arrows and box borders in teal, flat print reproduction, desaturated newsprint editorial collage, no photographs, schematic diagram only, clean academic infographic aesthetic
```

---
