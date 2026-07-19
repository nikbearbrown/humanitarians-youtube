# SHOTLIST — vox-isotope-swap
## One Molecule, Two Isotopes: See the Tumor, Then Treat It

---

## Beat histogram
| Type | Count | Beats |
|------|-------|-------|
| CARD | 3 | B01, B04, B12 |
| STILL·ai | 2 | B02, B09 |
| GRAPHIC | 6 | B03, B05, B07, B08, B10, B11 |
| DOCUMENT | 1 | B06 |
**Total: 12 beats**

## Rhythm check (no more than 2 consecutive same-type)
B01 CARD → B02 STILL → B03 GRAPHIC → B04 CARD → B05 GRAPHIC → B06 DOCUMENT → B07 GRAPHIC → B08 GRAPHIC → B09 STILL → B10 GRAPHIC → B11 GRAPHIC → B12 CARD
No run of 3+ same-type: PASS

## Act map
| Beat | Act | Duration (est.) |
|------|-----|-----------------|
| B01 | COLD OPEN | 8s |
| B02 | COLD OPEN | 10s |
| B03 | COLD OPEN | 14s |
| B04 | THE QUESTION | 12s |
| B05 | THE PROBLEM | 14s |
| B06 | THE PROBLEM | 10s |
| B07 | THE MECHANISM | 18s |
| B08 | THE MECHANISM | 16s |
| B09 | THE IMPLICATION | 12s |
| B10 | THE IMPLICATION | 16s |
| B11 | THE EXAMPLE | 28s |
| B12 | RECAP | 10s |
**Total estimated: ~168s (~2:48) — under 5:00 hard cap**

## Color law
- TEAL `#1F6F5C` = target-expressed / imaging-lit / responds to drug
- CRIMSON `#BF3339` = PSMA-negative / dark on scan / drug cannot reach
- GOLD `#F5D061` = editor's-pen fill highlight (B06 only), never text
- Never swapped mid-film

## Exclusions confirmed
- NO beta-vs-alpha physics (emitter comparison belongs to separate card)
- NO off-target salivary/kidney dosing mechanism detail
- NO DOTATATE second pair
- NO VISION trial statistics or efficacy numbers (other than the illustrative example)
- Isotope-swap loop and "scan selects the patient" only

---

## Per-beat work order

### B01 — CARD (own Manim)
Title card. Scene class: B01_Title. No fill-in slot.

### B02 — STILL·ai (open slot)
**Beat:** Cold open — PET scan showing mixed bright/dark lesions

**Archive search:**
- Wikimedia Commons: search "PSMA PET scan prostate cancer" — likely none usable (clinical data)
- ClinicalTrials.gov imagery: check for public-domain clinical images
- NCI Visuals Online: https://visualsonline.cancer.gov/ — search "PET scan prostate"

**Generative prompt:**
```
B02, editorial medical illustration of a whole-body PET scan showing a human torso in sagittal/coronal view, scattered glowing fluorescent foci indicating tumor lesions against a dark anatomical background, clinical nuclear medicine imaging aesthetic, photorealistic but desaturated approximately 80%, high contrast, mounted on aged newsprint texture, flat editorial print treatment, no text overlays, no labels, centered composition
```

### B03 — GRAPHIC (own Manim)
Scene class: B03_LesionMap. No fill-in slot.

### B04 — CARD (own Manim)
Question card. Scene class: B04_Question. No fill-in slot.

### B05 — GRAPHIC (own Manim)
Scene class: B05_NaiveLoop. No fill-in slot.

### B06 — DOCUMENT (own Manim)
Quote scene using _quote_scene. Scene class: B06_CompanionDx. No fill-in slot.

### B07 — GRAPHIC (own Manim)
Scene class: B07_IsotopeSwap. Key morph animation. No fill-in slot.

### B08 — GRAPHIC (own Manim)
Scene class: B08_BindingLogic. No fill-in slot.

### B09 — STILL·ai (open slot)
**Beat:** Implication — physician reviewing PET scan, patient selection moment

**Archive search:**
- NCI Visuals Online: https://visualsonline.cancer.gov/ — search "physician reading scan" "nuclear medicine"
- Wikimedia Commons: search "doctor PET scan reading room" — public domain clinical settings
- Unsplash (license check needed): "radiologist reading scan"

**Generative prompt:**
```
B09, a physician in white coat standing in a dim clinical nuclear medicine reading room, reviewing a glowing whole-body PET scan displayed on a large light-box wall monitor, patient silhouette visible through glass in background, documentary photojournalism style, desaturated ~80% warm newsprint treatment, harsh overhead fluorescent clinical light, editorial flat print reproduction, no text overlays
```

### B10 — GRAPHIC (own Manim)
Scene class: B10_ScanPredicts. No fill-in slot.

### B11 — GRAPHIC (own Manim)
Scene class: B11_Example. No fill-in slot.

### B12 — CARD (own Manim)
Endcard. Scene class: B12_End. No fill-in slot.

---

## Metadata
```json
{
  "source": "cancer-nanomedicine/chapters/07-radioligand-theranostics.md",
  "topic": "CANCER NANOMEDICINE",
  "manim_move": "morph",
  "open_slots": ["B02", "B09"],
  "color_semantics": "TEAL=target-expressed, CRIMSON=target-negative"
}
```
