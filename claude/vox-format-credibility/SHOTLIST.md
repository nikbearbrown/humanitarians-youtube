# SHOTLIST — vox-format-credibility

**Title:** Why a Perfect-Looking Spreadsheet Can Be Off by a Factor of Ten  
**Topic:** CLAUDE COWORK  
**Source chapter:** claude-cowork/chapters/06-extracting-data-from-documents.md  
**Slug:** vox-format-credibility  
**Derived duration:** ~2:08 (128s)

---

## Rhythm check

| Beat | Type | Source | Motion | Act |
|------|------|--------|--------|-----|
| B01 | CARD | own | hold | COLD OPEN |
| B02 | STILL | ai | kenburns | COLD OPEN |
| B03 | DOCUMENT | own | highlight | THE QUESTION |
| B04 | GRAPHIC | own | drawon | THE PROBLEM |
| B05 | GRAPHIC | own | drawon | THE PROBLEM |
| B06 | GRAPHIC | own | drawon | THE MECHANISM |
| B07 | GRAPHIC | own | drawon | THE MECHANISM |
| B08 | DOCUMENT | own | highlight | THE MECHANISM |
| B09 | STILL | ai | kenburns | THE IMPLICATION |
| B10 | GRAPHIC | own | drawon | THE EXAMPLE |
| B11 | GRAPHIC | own | drawon | THE EXAMPLE |
| B12 | CARD | own | hold | RECAP |

**Type histogram:** CARD×2, STILL×2, DOCUMENT×2, GRAPHIC×6  
**Consecutive same-type check:** B04–B07 are 4 consecutive GRAPHIC beats — FAIL lint. Fix: insert DOCUMENT B08 between B07 and B09 (already planned), breaking the chain at B04-B05 (2 GRAPHIC) and B06-B07 (2 GRAPHIC) with DOCUMENT B08 between — OK.

Wait — B04, B05, B06, B07 are 4 consecutive GRAPHIC. Rule: no more than 2 consecutive same type. Insert a CARD section break between B05 and B06.

**REVISED plan:**

| Beat | Type | Source | Motion | Act |
|------|------|--------|--------|-----|
| B01 | CARD | own | hold | COLD OPEN |
| B02 | STILL | ai | kenburns | COLD OPEN |
| B03 | DOCUMENT | own | highlight | THE QUESTION |
| B04 | GRAPHIC | own | drawon | THE PROBLEM |
| B05 | GRAPHIC | own | drawon | THE PROBLEM |
| B06 | CARD | own | hold | SECTION — THE MECHANISM |
| B07 | GRAPHIC | own | drawon | THE MECHANISM |
| B08 | GRAPHIC | own | drawon | THE MECHANISM |
| B09 | DOCUMENT | own | highlight | THE MECHANISM (key claim) |
| B10 | STILL | ai | kenburns | THE IMPLICATION |
| B11 | GRAPHIC | own | drawon | THE EXAMPLE |
| B12 | GRAPHIC | own | drawon | THE EXAMPLE |
| B13 | CARD | own | hold | RECAP |

**New histogram:** CARD×3, STILL×2, DOCUMENT×2, GRAPHIC×6 — 13 beats total  
**Consecutive check:** B01(CARD) B02(STILL) B03(DOC) B04-B05(GRAPHIC×2) B06(CARD) B07-B08(GRAPHIC×2) B09(DOC) B10(STILL) B11-B12(GRAPHIC×2) B13(CARD) ✓ max 2 consecutive

---

## Color law

TEAL #1F6F5C = correctly read / verified value (the good)  
CRIMSON #BF3339 = wrong extraction / silent error (the bad)  
GOLD #F5D061 = editor's-pen highlight fill, once in B08 (the Unknown Merchant clone sweep) — never text  
Never swapped mid-film.

---

## Act map

| Act | Beats | Purpose |
|-----|-------|---------|
| COLD OPEN | B01–B02 | Concrete situation: 47 receipts, clean table, hidden error |
| THE QUESTION | B03 | Gap formula on screen and in narration |
| THE PROBLEM | B04–B05 | Two identical cells with different values; the two-step model |
| THE MECHANISM | B06–B09 | Section break + read fails → format runs → error propagates → key claim |
| THE IMPLICATION | B10 | Trusting the format means inferring what it cannot tell you |
| THE EXAMPLE | B11–B12 | Illustrative 47-row scenario, spot-check reveals 2 errors |
| RECAP | B13 | Endcard: question → answer |

---

## Exclusions confirmed

- NO OCR/vision-model architecture explainer ✓
- NO schema-design template walkthrough ✓
- NO full verification-checklist enumeration ✓
- NO second example with invoices ✓
- NO hallucination-vs-granularity error taxonomy ✓

---

## Human fill-in slots

### B02 — STILL · ai (aligned-cells / professional spreadsheet)

Search: Wikimedia Commons "spreadsheet table printed" — likely no usable archival match.

Generative prompt:
```
B02, top-down view of a clean professionally printed spreadsheet on a desk, neatly aligned column headers in bold, every cell filled with numbers and short text entries, no visible errors, all decimal places consistent, flat editorial newsprint treatment, cream and charcoal tones, desaturated, no people in frame, close crop showing 8-10 rows and 5-6 columns
```

### B10 — STILL · ai (person trusting spreadsheet / marking cell with red pen)

Search: Wikimedia Commons "desk paperwork reviewing" — unlikely archival match for this specific scenario.

Generative prompt:
```
B10, close-up of two hands at a desk holding a red pen and marking a single cell in a clean printed spreadsheet, confident reviewing posture, the document looks official and well-formatted, editorial collage style, desaturated newsprint treatment, warm cream tones, no face visible, shallow depth
```

---

## Own-Manim scenes (beat_sheet.json field `graphic.manim`)

| Beat | Class | Description |
|------|-------|-------------|
| B01 | B01_Title | Title CARD with CLAUDE COWORK eyebrow |
| B03 | B03_TheQuestion | DOCUMENT quote — gap formula |
| B04 | B04_TwoCells | Two identically formatted cells: $34.20 (TEAL) vs $342.00 (CRIMSON) |
| B05 | B05_TwoSteps | Two-box pipeline: READ → FORMAT, FORMAT always checks |
| B06 | B06_SectionMechanism | Section CARD: TWO SEPARATE STEPS |
| B07 | B07_StepFails | Same pipeline, READ X'd in CRIMSON, FORMAT still ticks TEAL |
| B08 | B08_MerchantClone | 4 rows of "Unknown Merchant" in CRIMSON, GOLD sweep |
| B09 | B09_KeyClaim | DOCUMENT quote — structure confers credibility |
| B11 | B11_Example | Mini spreadsheet, row 23 in CRIMSON $342.00, arrow to $34.20 |
| B12 | B12_SpotCheck | 47 row-marks, 5 ticked, 2 error in CRIMSON, 42 neutral |
| B13 | B13_Endcard | Endcard CARD: "Clean format ≠ correct data." / CLAUDE COWORK |
