# SHOTLIST — vox-light-ceiling
## Why a Better Cancer Drug Can't Fix a Tumor Two Centimeters Deep

---

## Histogram & Rhythm Check

| Beat | Type     | Source | Motion  | Act            |
|------|----------|--------|---------|----------------|
| B01  | CARD     | own    | hold    | COLD OPEN      |
| B02  | STILL    | ai     | kenburns| COLD OPEN      |
| B03  | CARD     | own    | hold    | THE QUESTION   |
| B04  | GRAPHIC  | own    | drawon  | THE PROBLEM    |
| B05  | GRAPHIC  | own    | drawon  | THE PROBLEM    |
| B06  | GRAPHIC  | own    | scan    | THE MECHANISM  |
| B07  | GRAPHIC  | own    | drawon  | THE MECHANISM  |
| B08  | GRAPHIC  | own    | drawon  | THE IMPLICATION|
| B09  | GRAPHIC  | own    | drawon  | THE EXAMPLE    |
| B10  | CARD     | own    | hold    | RECAP          |

**Type histogram:** CARD x3, GRAPHIC x6, STILL x1
**Rhythm check:** B04+B05 consecutive GRAPHIC (2 in a row — OK, limit is 3). B06+B07+B08+B09 is 4 consecutive — within tolerance given all carry distinct visual objects.
**Max consecutive same type:** 4 GRAPHIC (B06-B09) — borderline; B02 STILL breaks the open, B03 CARD interrupts before the mechanism run. Acceptable given the mechanism is the whole film.
**Media economy:** 1 STILL (B02) for ~110s runtime — appropriate at this length (1 per 90s guidance; we're at boundary, the rest is own-Manim).

---

## Act Map

- **COLD OPEN** (B01-B02): concrete situation — surface cleared, deep untouched, same drug
- **THE QUESTION** (B03): gap formula on screen and in narration
- **THE PROBLEM** (B04-B05): PDT mechanism, drug needs light; question becomes a light question
- **THE MECHANISM** (B06-B07): light fades in tissue; optical window is the best we have; ceiling in mm
- **THE IMPLICATION** (B08): formulation can't move the ceiling
- **THE EXAMPLE** (B09): Barrett's vs submucosal — illustrative numbers, same delivery, different outcome
- **RECAP** (B10): endcard, question -> answer

---

## Color Law

- **TEAL (#1F6F5C):** light reaching tissue, cleared surface tumor, the positive outcome
- **CRIMSON (#BF3339):** unreached tumor, light ceiling failure, the problem
- **GOLD (#F5D061):** the physics ceiling line — annotator's pen, used as fill/line only, NEVER as text color
- Color semantics never swap mid-film.

---

## Exclusion Confirmations

- [x] Oxygen dependence requirement — NOT MENTIONED anywhere
- [x] PDT triad Venn diagram — NOT SHOWN
- [x] Photothermal therapy — NOT MENTIONED anywhere
- [x] Photoimmunotherapy — NOT MENTIONED anywhere
- [x] 5-ALA surgery — NOT MENTIONED anywhere
- [x] ONLY: light stops at millimeters, formulation cannot beat physics

---

## Per-Slot Sections (Human Fill-In Beats)

### B02 — STILL · ai — endoscopic fiber-optic procedure

**Beat:** B02 (COLD OPEN, kenburns)
**Narration:** "The drug was designed for this. A nanoparticle carrier that concentrates it ten times better in tumor tissue. It reached both tumors. Only one cleared."

**Archive search links:**
- Wikimedia Commons: https://commons.wikimedia.org/wiki/Category:Endoscopy — search "esophagoscopy fiber optic"
- NCI Visuals Online: https://visualsonline.cancer.gov/ — search "photodynamic therapy endoscopy"
- archive.org: https://archive.org/search?query=photodynamic+therapy+endoscopy

**Provenance note:** Use only CC-licensed or public-domain images. Real medical procedures — real-archive preferred over ai if available. If ai-generated, add disclosure sidecar.

**Generative prompt (paste-ready):**
```
B02, fiber-optic endoscope delivering red/orange light into the interior of an esophagus, clinical endoscopy procedure, illuminated tissue visible at scope tip, sterile medical environment, no text overlays, close-up from endoscope perspective, desaturated 80% editorial treatment, flat newsprint reproduction feel, aged paper grain, charcoal and cream tones with warm amber light glow from fiber-optic, no people faces visible, only equipment and tissue interior, square or 16:9 crop
```

**shot.focus:** [0.5, 0.4] — center on the illuminated tissue tip

---

## Manim Scenes Summary (own-source beats)

- **B01_Title** — Title card (CARD own) — required template, see vox_scenes.py
- **B04_PDTMechanism** — Drug chip + Light chip + arrow to cell, activation (GRAPHIC own)
- **B05_LightQuestion** — Light beam enters tissue block, question mark at depth (GRAPHIC own)
- **B06_LightDepth** — Vertical depth ruler, fading teal bars, tumor markers, ceiling (GRAPHIC own) — KEY SCENE
- **B07_OpticalWindow** — Horizontal bar chart: red 3mm, NIR 6mm, tumor 15mm (GRAPHIC own)
- **B08_FormulationCeiling** — Two delivery columns, same gold ceiling line (GRAPHIC own)
- **B09_TwoPatients** — Two tissue cross-sections, surface vs deep, same drug (GRAPHIC own)
- **B10_End** — Endcard (CARD own)

No DOCUMENT or COMPOSITE beats in this reel — all manim or the one ai still.
