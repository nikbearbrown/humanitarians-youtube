# SHOTLIST — vox-p53-circuit
## Why Cancer Cannot Read Its Own Death Instructions

---

## Header: Rhythm, Color Law, Act Map

### Shot-type histogram (15 beats)
| type | beats | % |
|---|---|---|
| CARD | B01, B03, B15 | 20% |
| STILL · ai | B02, B08 | 13% |
| GRAPHIC · own | B04, B05, B06, B07, B09, B10, B11, B12, B13, B14 | 67% |

Rhythm lint: no run of >2 consecutive same-type beats. STILL at B02 breaks
CARD–CARD; STILL at B08 breaks the GRAPHIC run at B06–B07. Clean.

### Act map
| act | beats | duration (est.) |
|---|---|---|
| COLD OPEN | B01, B02 | ~21s |
| THE QUESTION | B03 | ~12s |
| THE PROBLEM | B04, B05 | ~21s |
| THE MECHANISM | B06, B07, B08, B09, B10 | ~62s |
| THE IMPLICATION | B11, B12 | ~21s |
| THE EXAMPLE | B13, B14 | ~28s |
| RECAP | B15 | ~11s |
| **Total** | **15 beats** | **~176s (~2:56)** |

Well within the 5:00 cap. THE EXAMPLE is present right before RECAP (16:9
law honored). No split needed.

### Color law
- **TEAL #1F6F5C** = p53 wild-type / damage correctly sensed / death executed / good path
- **CRIMSON #BF3339** = p53 mutant / hub absent / damage ignored / lineage drifts
- **GOLD #F5D061** = editor's-pen highlight fill ONLY, once per graphic (B07 fan-out if used)
- **SLATE #3E5559** = structural scaffold only (no data role)
- Two accents max: TEAL and CRIMSON. Never swap mid-film.

### Exclusion confirmations
- [x] No p53 arrest vs. senescence vs. apoptosis choice mechanism
- [x] No extrinsic pathway (FAS, TRAIL, DR4, DR5, FADD, caspase-8)
- [x] No necroptosis, ferroptosis, pyroptosis
- [x] No venetoclax, BH3 mimetics, navitoclax
- [x] No p53 tetramer or dominant-negative detail
- [x] No ATR/ATM biochemistry beyond naming them as sensors
- [x] No BCL-XL or MCL-1 specifics (just "BCL-2 guardians" as a family)

---

## Per-beat work orders

### B01 — CARD · own · hold
**COLD OPEN · Title**
Own-Manim CARD scene. Eyebrow "CANCER BIOLOGY" in TEAL. Title in INK.
No fill slot needed.

### B02 — STILL · ai · kenburns
**COLD OPEN · Keratinocyte apoptosis plate**
One open ai slot. Push-in slow onto the apoptotic cell.

**Archive search (try first — real microscopy, PD or CC):**
- Wikimedia Commons: `keratinocyte apoptosis H&E histology`
  https://commons.wikimedia.org/w/index.php?search=keratinocyte+apoptosis
- NCBI PMC open-access figures: search `keratinocyte UV apoptosis histology`
  https://www.ncbi.nlm.nih.gov/pmc/search/?query=keratinocyte+apoptosis+UV

**Generative prompt:**
```
B02, photomicrograph of human epidermal skin section, stratified squamous
epithelium with keratinocytes in organized layers, one keratinocyte in apoptosis
showing nuclear condensation and membrane blebbing in the center of the frame,
surrounded by healthy neighboring cells, H&E stain or fluorescence, scientific
histology image, newsprint desaturated editorial treatment, flat lighting, no
text overlays, no labels
```

PROMPT LAW: object=keratinocyte monolayer, count=one apoptotic cell central,
geometry=organized layer of cells, material=histological tissue section,
camera=slightly overhead microscopy view, light=flat microscope illumination,
exclusions=no labels, no text, no graphic arrows.

### B03 — CARD · own · hold
**THE QUESTION · Question card**
Own-Manim CARD scene. Question on screen AND in narration (Gap formula: X should predict Y; here it did not; why?).
No fill slot needed.

### B04 — GRAPHIC · own · drawon
**THE PROBLEM · Expected circuit: damage → death**
Manim scene `B04_DamageToDeathExpected`. No fill slot needed.

### B05 — GRAPHIC · own · drawon
**THE PROBLEM · Broken link between sensor and death**
Manim scene `B05_BrokenLink`. No fill slot needed.

### B06 — GRAPHIC · own · drawon
**THE MECHANISM · p53 hub stabilizes**
Manim scene `B06_P53Hub`. No fill slot needed.

### B07 — GRAPHIC · own · drawon
**THE MECHANISM · p53 transcribes PUMA, NOXA, BAX**
Manim scene `B07_P53Transcribes`. Gold highlighter fill may appear once on
the "BCL-2 balance tips" label as the editor's-pen accent.
No fill slot needed.

### B08 — STILL · ai · kenburns
**THE MECHANISM · MOMP diagram plate**
One open ai slot. Push-in on mitochondrial pore complex.

**Archive search (try first):**
- Wikimedia Commons: `mitochondrial outer membrane permeabilization apoptosis`
  https://commons.wikimedia.org/w/index.php?search=MOMP+cytochrome+c+apoptosis
- BioRender-style diagrams in PMC open-access:
  https://www.ncbi.nlm.nih.gov/pmc/search/?query=MOMP+BAX+cytochrome+c+diagram

**Generative prompt:**
```
B08, scientific illustration of mitochondrial outer membrane permeabilization
MOMP, showing a mitochondrion cross-section with BAX oligomers as dark clustered
proteins forming a channel pore in the outer membrane, cytochrome c small orange
molecules releasing through the pore into cytoplasm on the right, apoptosome
wheel-shaped protein complex assembling at lower right, schematic diagram style,
clean scientific illustration, newsprint desaturated editorial treatment, no text
labels in the image, no background clutter
```

PROMPT LAW: object=mitochondrion cross-section with BAX pore complex, count=
multiple cytochrome c molecules streaming out, geometry=outer membrane top
surface with pore cluster center, material=protein complex schematic diagram,
camera=cross-section side view, light=flat scientific illustration lighting,
exclusions=no text, no labels, no caspase cascade shown.

### B09 — GRAPHIC · own · drawon
**THE MECHANISM · Full intact circuit**
Manim scene `B09_FullCircuit`. No fill slot needed.

### B10 — GRAPHIC · own · drawon
**THE MECHANISM · Circuit collapse — p53 removed**
Manim scene `B10_CircuitCollapse`. The COLLAPSE manim move: hub removed,
downstream fades. No fill slot needed.

### B11 — GRAPHIC · own · drawon
**THE IMPLICATION · TP53 frequency grid**
Manim scene `B11_P53FrequencyBar`. IsotypeGrid: 100 squares, ~50 crimson,
~50 teal. No fill slot needed.

### B12 — GRAPHIC · own · drawon
**THE IMPLICATION · Lineage drift fan**
Manim scene `B12_LineageDrift`. No fill slot needed.

### B13 — GRAPHIC · own · drawon
**THE EXAMPLE · Left cell (p53 WT) executes death**
Manim scene `B13_TwoCellsLeft`. No fill slot needed.

### B14 — GRAPHIC · own · drawon
**THE EXAMPLE · Right cell (p53 mutant) divides**
Manim scene `B14_TwoCellsRight`. No fill slot needed.

### B15 — CARD · own · hold
**RECAP · Endcard**
Own-Manim CARD scene. Topic kicker "CANCER BIOLOGY". Question → answer.
No fill slot needed.

---

## Open fill slots summary
| slot | beat | type | motion | notes |
|---|---|---|---|---|
| B02 | B02 | STILL · ai | kenburns | keratinocyte apoptosis plate |
| B08 | B08 | STILL · ai | kenburns | MOMP/cytochrome c diagram |

2 ai-still slots for a ~3-minute film (1 per 90s — within the media economy rule).
