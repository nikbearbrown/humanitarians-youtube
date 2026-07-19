# SHOTLIST — vox-rb-convergence
*Why the Rb Gate Has Six Different Keys — and Losing Any One Opens It*

---

## Histogram

| Shot type | Count | % |
|-----------|-------|---|
| CARD | 6 | 40% |
| GRAPHIC·own | 7 | 47% |
| STILL·ai | 2 | 13% |

No type exceeds 47%. No run of 3+ consecutive same-type beats. ✓

---

## Rhythm Check

B01 CARD · B02 STILL · B03 CARD · B04 CARD · B05 GRAPHIC · B06 GRAPHIC · B07 CARD · B08 GRAPHIC · B09 CARD · B10 GRAPHIC · B11 GRAPHIC · B12 STILL · B13 GRAPHIC · B14 GRAPHIC · B15 CARD

Longest consecutive run: 2 (B03-B04 CARD/CARD; B05-B06 GRAPHIC/GRAPHIC; B10-B11 GRAPHIC/GRAPHIC; B13-B14 GRAPHIC/GRAPHIC). All ≤ 2. ✓

---

## Act Map

| Act | Beats | Type |
|-----|-------|------|
| COLD OPEN | B01-B02 | CARD, STILL |
| THE QUESTION | B03 | CARD |
| THE PROBLEM | B04-B06 | CARD, GRAPHIC, GRAPHIC |
| THE MECHANISM | B07-B10 | CARD, GRAPHIC, CARD, GRAPHIC |
| THE IMPLICATION | B11-B12 | GRAPHIC, STILL |
| THE EXAMPLE (16:9 only) | B13 | GRAPHIC |
| THE IMPLICATION (coda) | B14 | GRAPHIC |
| RECAP | B15 | CARD |

---

## Color Law

TEAL #1F6F5C = gate held / brake applied / cell in check (the good/true/intact state)
CRIMSON #BF3339 = gate forced open / lost brake / S-phase uncontrolled (the bad/lost/broken state)
GOLD #F5D061 = editor's-pen highlight fill (B14 only — "convergence point" sweep; fill, never text)
Semantics: never swapped mid-film. ✓

---

## Exclusion Confirmations

- NO BRAF inhibitor resistance mechanisms (NRAS amplification, BRAF amplification, parallel RAF isoforms): ✓ absent
- NO full MAPK pathway details beyond "BRAF → MAPK → cyclin D1": ✓ absent
- NO PI3K beyond cyclin D1 stabilization via AKT: ✓ absent
- NO cyclin E amplification as resistance route: ✓ absent
- NO breast cancer CDK4/6 inhibitor trial data: ✓ absent

---

## Beat-by-Beat Shot Specifications

### B01 — CARD · own · hold
Type: title card
Copy: "Why the Rb gate has six different keys — and losing any one opens it"
Eyebrow: "CANCER BIOLOGY" in TEAL
Sub: "the convergence problem"
Font: title in DISPLAY (Montserrat) / eyebrow DISPLAY caps
Duration: ~11s

---

### B02 — STILL · ai · kenburns [OPEN SLOT]
Narration: "BRAF V600E is the mutation driving half of all cutaneous melanomas. Vemurafenib produces dramatic tumor shrinkage within weeks."
Focus: [0.5, 0.4] — push toward lesions

**Archive search:**
- Wikimedia Commons: "PET scan melanoma" — https://commons.wikimedia.org/w/index.php?search=PET+scan+melanoma
- NIH Image Gallery: https://imagebank.nih.gov/ (search: melanoma PET)
- NCI Visuals Online: https://visualsonline.cancer.gov/

**Generative prompt:**
```
B02, axial PET scan image of a human torso showing bright metabolically active metastatic melanoma lesions scattered through lymph nodes and soft tissue, warm golden-orange hotspots against dark background, printed reproduction on aged cream newsprint, desaturated editorial collage treatment, charcoal tone flattening, no text overlay, no annotations, medical imaging aesthetic
```

---

### B03 — CARD · own · hold
Type: question card
Copy: "BRAF inhibition should shut down the proliferative signal in a BRAF-mutant melanoma. Here BRAF is blocked, yet the cancer continues dividing. Why?"
Font: SERIF (EB Garamond) for the question body
Duration: ~13s

---

### B04 — CARD · own · hold
Type: section card
Copy: "The Gate" / Sub: "one switch, many inputs"
Font: DISPLAY
Duration: ~13s

---

### B05 — GRAPHIC · own · drawon [Manim: B05_RbGate]
Narration: Rb grips E2F — the gate in its closed, healthy state
Visual: Gate symbol — teal Rb rectangle gripping an E2F circle; "G1" label left, "S phase" label right with a barrier; each component labeled in SERIF italic as it appears
Colors: TEAL throughout
Motion: drawon — gate posts draw, then Rb chip fades in gripping E2F circle
Duration: ~14s

---

### B06 — GRAPHIC · own · drawon [Manim: B06_NormalSignal]
Narration: growth signal → cyclin D-CDK4/6 → Rb phosphorylated → E2F freed → S phase
Visual: Single input arrow "growth signal" from above; LabelChip "cyclin D-CDK4/6" appears; phosphorylation dot tags Rb; Rb releases E2F; E2F moves to S phase; gate swings open
Colors: TEAL (normal, conditioned opening)
Motion: drawon — each step draws on sequentially
Duration: ~13s

---

### B07 — CARD · own · hold
Type: section card
Copy: "Six Keys" / Sub: "different lesions, one gate"
Font: DISPLAY
Duration: ~13s

---

### B08 — GRAPHIC · own · accumulate [Manim: B08_SixInputs]
Narration: six lesions each named, all pointing to E2F free
Visual: Six crimson LabelChips accumulate one at a time in a left column; labels: "Rb loss", "p16 loss", "Cyclin D amplified", "CDK4/6 amplified", "CDK4 activating mutation", "Hyperactive upstream signaling"; each chip gets a short crimson arrow pointing right; a single crimson LabelChip "E2F free" sits at right; arrows point into it
Colors: CRIMSON throughout (all six lesions are the bad state)
Motion: accumulate — one chip + arrow per narration phrase
Duration: ~16s

---

### B09 — CARD · own · hold
Type: section card
Copy: "Three Inputs, One Melanoma" / Sub: "BRAF V600E — the convergence case"
Font: DISPLAY
Duration: ~13s

---

### B10 — GRAPHIC · own · accumulate [Manim: B10_ThreeInputs]
Narration: three melanoma alterations named, each plugging into the CDK4/6 junction
Visual: Central junction box "CDK4/6 → Rb" at center-right. Three input cables appear left to right, one at a time:
  - Cable 1: "BRAF V600E → MAPK → cyclin D1" (long; three chip nodes connected)
  - Cable 2: "p16 loss → CDK4/6 uninhibited" (short direct)
  - Cable 3: "PTEN loss → AKT → cyclin D1 stable" (three nodes)
Each cable draws on and "plugs" into junction box. After all three: arrow from junction to "E2F free → S phase" endpoint at far right
Colors: All crimson; junction box outlined in CRIMSON fill
Motion: accumulate — one cable per narration clause
Duration: ~15s

---

### B11 — GRAPHIC · own · drawon [Manim: B11_BrafBlock]
Narration: BRAF blocked — cable 1 goes gray; cables 2 and 3 stay crimson; junction stays on
Visual: Start from B10 end state (three cables, junction, endpoint). A block mark labeled "BRAFi" crosses cable 1; cable 1 fades to gray. Cables 2 and 3 remain CRIMSON. Junction box stays outlined CRIMSON. Endpoint "E2F free → S phase" stays. A SerifLabel "gate stays open" appears below junction in CRIMSON.
Colors: CRIMSON (active) / gray (blocked)
Motion: drawon — BRAFi label draws, then cable 1 fades
Duration: ~14s

---

### B12 — STILL · ai · kenburns [OPEN SLOT]
Narration: "Blocking one input in a convergent pathway does not close a gate that has two other active inputs."
Focus: [0.5, 0.5] — push toward the junction indicator light

**Archive search:**
- Unsplash (CC0): https://unsplash.com/s/photos/electrical-junction-box
- Wikimedia Commons: https://commons.wikimedia.org/w/index.php?search=electrical+junction+box

**Generative prompt:**
```
B12, close-up photograph of a weathered industrial electrical junction box mounted on a concrete wall, three thick insulated wires entering from below, one wire clamped with a red padlock clasp but the small green LED indicator light on the face of the box still glows, shallow depth of field, editorial newsprint desaturation treatment, charcoal tones on cream aged paper reproduction, no text, no labels
```

---

### B13 — GRAPHIC · own · accumulate [Manim: B13_CdkBlock]
Narration: full illustrative example — BRAF blocked + CDK4/6i added → junction dark → gate restored
Visual: Start from B11 end state (cable 1 gray, cables 2+3 crimson, junction crimson, endpoint lit). "CDK4/6i" block label appears at the junction box. Sequentially: cables 2 and 3 fade to gray, junction dims (fill fades), endpoint changes from "E2F free → S phase" (crimson) to "E2F bound → G1 arrest" (teal). SerifLabel "junction dark" below junction in TEAL.
Colors: TEAL (restored gate) / gray (both blocked cables)
Motion: accumulate — each resolution step accumulates sequentially
Duration: ~15s

---

### B14 — GRAPHIC · own · drawon [Manim: B14_RationalCombination]
Narration: rational combination strategy — map inputs, find convergence, block there
Visual: Three stacked text boxes appear in sequence on the left: "Map active inputs", "Find convergence point", "Block at convergence". A teal bracket and arrow connects all three to a label "rational combination" on the right. On the word "convergence point" in narration: a GOLD highlight bar (Rectangle, fill GOLD opacity 0.4) sweeps behind "Find convergence point" text.
Colors: TEAL (the strategy is the solution), GOLD (the single editor's-pen highlight for this film)
Motion: drawon — boxes draw on; GOLD sweep on keyword
Duration: ~13s

---

### B15 — CARD · own · hold
Type: endcard
Eyebrow: "CANCER BIOLOGY" in TEAL
Copy: "Blocking one input cannot close a gate with two others active."
Sub: "the convergence point is where the combination must act"
Font: DISPLAY for eyebrow, SERIF bold for copy, SERIF for sub
Duration: ~14s (outro law owns tail)

---

## Open Slots Summary (for PROMPTS.md)

| Beat | Type | Status |
|------|------|--------|
| B02 | STILL·ai | OPEN — PET scan / melanoma metastases |
| B12 | STILL·ai | OPEN — electrical junction box, one wire blocked but LED still on |
