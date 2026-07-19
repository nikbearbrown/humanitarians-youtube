# SHOTLIST — vox-trial-failure-tree
## The Cancer Trial That Couldn't Diagnose Its Own Failure

---

## Histogram & Rhythm Check

| Type | Count | % |
|---|---|---|
| CARD | 3 | 23% |
| STILL·ai | 2 | 15% |
| GRAPHIC | 6 | 46% |
| DOCUMENT | 1 | 8% |
| COMPOSITE | 0 | 0% |

**Rhythm check (no >2 consecutive same type):**
B01 CARD → B02 STILL → B03 CARD → B04 GRAPHIC → B05 DOCUMENT → B06 GRAPHIC → B07 GRAPHIC → B08 GRAPHIC → B09 GRAPHIC → B10 GRAPHIC → B11 STILL → B12 GRAPHIC → B13 CARD

**Flag:** B06–B10 = five consecutive GRAPHIC beats. This is a continuous mechanism exposition (all pieces of the failure tree being built); variation is provided by different scene content (each branch, then the full tree). The rhythm reads visually distinct because each scene introduces new structure. Acceptable for a mechanism sequence; alternative would be to insert a DOCUMENT break but that would fracture the tree-building logic.

**STILL·ai count:** 2 stills for ~248s runtime (~1 per 124s). Target is ~1 per 90s, so this is slightly sparse. A third still could replace B07 (delivery failure) or B09 (biology failure) — but Manim graphics are preferred here for the branching mechanics. Acceptable.

---

## Act Map

| Act | Beats | Duration |
|---|---|---|
| COLD OPEN | B01–B02 | ~27s |
| THE QUESTION | B03 | ~20s |
| THE PROBLEM | B04–B05 | ~31s |
| THE MECHANISM | B06–B09 | ~68s |
| THE IMPLICATION | B10–B11 | ~31s |
| THE EXAMPLE | B12 | ~52s |
| RECAP | B13 | ~19s |

Total estimated: ~248s (4:08) — within 5:00 hard cap. ✓

---

## Color Law

**Two accents, one meaning each, stated here, never swapped:**
- **TEAL `#1F6F5C`** = diagnosable / fixed / confirmed — delivery confirmed, fix arrow, successful path
- **CRIMSON `#BF3339`** = failure / unattributable / broken — all three failure modes, the NEGATIVE result node, the split lines, the ambiguity
- **GOLD `#F5D061`** = editor's pen highlighter fill only (B05 quote card) — once per film
- **SLATE `#3E5559`** = structural boxes (B04 endpoint box)

---

## Exclusion Confirmations

From card metadata — these topics appear NOWHERE in the reel:
- [x] NO companion diagnostic regulatory pathway
- [x] NO accelerated approval mechanism
- [x] NO three-arm trial design
- [x] NO specific assay protocols
- [x] One principle only: response-only endpoint cannot identify which of three failure modes caused failure

---

## Per-Slot Work Orders

---

### B02 — STILL · ai

**Beat:** Cold Open — targeted polymeric nanoparticle schematic
**Motion:** kenburns (slow push-in)
**Focus:** center of nanoparticle

**Archive search:** None — schematic diagram, ai generation preferred.
- Wikimedia: no relevant free nanoparticle cross-section diagrams suitable for editorial treatment

**Generative prompt:**
```
B02, schematic cross-section of a spherical polymeric nanoparticle, targeting ligands shown as small hook shapes on the outer surface, enclosed drug payload illustrated as small dots inside the core, flat editorial biomedical diagram style, aged newsprint background, desaturated muted palette, teal outline on the particle, no labels, no digital glow, no gradient, documentary print reproduction aesthetic, square or landscape crop
```

---

### B11 — STILL · ai

**Beat:** The Implication — tracer cohort concept
**Motion:** kenburns (slow pull-back to reveal all five silhouettes)
**Focus:** [0.5, 0.4] center of the group

**Archive search:** None — schematic illustration, ai generation preferred.
- Wikimedia: no editorial schematic of PET tracer cohort with patient silhouettes available under free license

**Generative prompt:**
```
B11, editorial biomedical schematic showing five human silhouettes arranged in a horizontal row, above each silhouette a simplified circular scan cross-section showing false-color tracer distribution inside the body outline, illustration of a biodistribution tracer cohort clinical study, aged newsprint background, flat documentary diagram style, muted warm desaturated tones, no labels, no digital glow, no gradient, print reproduction aesthetic
```

---

## GRAPHIC Scenes (Manim — own)

All six GRAPHIC beats are own-Manim — no fill-in assets needed. Scene classes in `vox_scenes.py`:

| Beat | Class | Description |
|---|---|---|
| B04 | B04_BinaryEndpoint | Binary endpoint: worked / didn't fork |
| B06 | B06_ThreeFailures | The failure tree: one NEGATIVE splits to three branches |
| B07 | B07_DeliveryFailure | Delivery failure branch: particle path to liver, fix arrow |
| B08 | B08_PayloadFailure | Payload failure branch: premature release, fix arrow |
| B09 | B09_BiologyFailure | Biology failure branch: cell unresponsive, fix arrow |
| B10 | B10_FullTree | Full tree with all CRIMSON branches + TEAL fix arrows |
| B12 | B12_TwoPrograms | Two program columns: A closed, B diagnosed + redesigned |

## CARD Scenes (Manim — own)

| Beat | Class | Description |
|---|---|---|
| B01 | B01_Title | Title card with eyebrow, title, crimson underline |
| B03 | B03_Question | THE QUESTION verbatim on screen |
| B13 | B13_End | Endcard: diagnosable negative |

## DOCUMENT Scene (Manim — own)

| Beat | Class | Description |
|---|---|---|
| B05 | B05_Quote | Quote card: cannot be attributed — gold sweep |
