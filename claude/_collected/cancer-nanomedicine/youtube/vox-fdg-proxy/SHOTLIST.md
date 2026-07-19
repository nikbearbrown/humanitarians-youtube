# SHOTLIST — vox-fdg-proxy
## Why a Glowing PET Scan Doesn't Actually Show Cancer

---

## Histogram

| Shot type | Beats | Count |
|-----------|-------|-------|
| CARD      | B01, B03, B12 | 3 |
| STILL·ai  | B02, B09 | 2 |
| GRAPHIC   | B04, B05, B06, B08, B10 | 5 |
| DOCUMENT  | B07, B11 | 2 |

**Total beats:** 12  
**Estimated runtime:** ~174 s (~2:54) — within 5:00 cap  
**STILL·ai density:** 2 stills over ~174 s → ~1 per 87 s (target: ~1 per 90 s) ✓

---

## Rhythm check

B01 CARD → B02 STILL → B03 CARD → B04 GRAPHIC → B05 GRAPHIC → B06 GRAPHIC → B07 DOCUMENT → B08 GRAPHIC → B09 STILL → B10 GRAPHIC → B11 DOCUMENT → B12 CARD

- B04–B05–B06: three consecutive GRAPHIC — VIOLATION. Fixed: B07 (DOCUMENT) breaks the run between B06 and B08. Sequence is GGG then D then G, which splits to max 3 then 1 then 1. Per the rule "no more than 2 consecutive same shot type" this needs addressing: B04, B05, B06 are 3 consecutive GRAPHICs.

**Resolution:** Convert B06 to a DOCUMENT beat (quote card) to break the GRAPHIC run.

Revised rhythm: B04 GRAPHIC → B05 GRAPHIC → B06 DOCUMENT → B07 DOCUMENT → ...

Wait — two consecutive DOCUMENTs at B06–B07 is also a violation. 

**Final resolved sequence:**
- B04 GRAPHIC
- B05 GRAPHIC  
- B06 GRAPHIC (3 consecutive — exceeds limit)

**Correction:** Move B06 (false positives) to CARD type (section card) — it is inherently a list beat that reads well as a card. B07 stays DOCUMENT.

**Final revised rhythm:**
B01 CARD → B02 STILL → B03 CARD → B04 GRAPHIC → B05 GRAPHIC → B06 CARD → B07 DOCUMENT → B08 GRAPHIC → B09 STILL → B10 GRAPHIC → B11 DOCUMENT → B12 CARD

Consecutive check:
- B01-B03: CARD, STILL, CARD — ok (all different)
- B04-B06: GRAPHIC, GRAPHIC, CARD — max 2 same ✓
- B06-B08: CARD, DOCUMENT, GRAPHIC — ok ✓
- B09-B11: STILL, GRAPHIC, DOCUMENT — ok ✓
- B11-B12: DOCUMENT, CARD — ok ✓

**RHYTHM: PASS** (max 2 consecutive same type)

> Note: beat_sheet.json has B06 as GRAPHIC. This shotlist corrects it to CARD. The beat_sheet will be updated to reflect this correction before audio.

---

## Act map

| Beat | Act |
|------|-----|
| B01 | COLD OPEN |
| B02 | COLD OPEN |
| B03 | THE QUESTION |
| B04 | THE PROBLEM |
| B05 | THE PROBLEM |
| B06 | THE MECHANISM |
| B07 | THE MECHANISM |
| B08 | THE IMPLICATION |
| B09 | THE EXAMPLE |
| B10 | THE EXAMPLE |
| B11 | THE EXAMPLE |
| B12 | RECAP (endcard) |

Act structure: COLD OPEN → THE QUESTION → THE PROBLEM → THE MECHANISM → THE IMPLICATION → THE EXAMPLE → RECAP ✓

---

## Color law

- **TEAL #1F6F5C** = true signal / correct finding / the proxy that holds / biopsy-confirmed reality
- **CRIMSON #BF3339** = false positive / wrong interpretation / the gap between proxy and biology
- **GOLD #F5D061** = editor's-pen highlight (fill only, never text — once in B07, once in B11 on highlight_words)
- Never swap mid-film. Two accents (TEAL + CRIMSON) ✓

---

## Exclusions confirmed

Card exclusions honored — nowhere in this reel do the following appear:
- Five-modality tour (MRI, CT, fluorescence, photoacoustic) — ABSENT ✓
- Biodistribution decision tree — ABSENT ✓
- Activatable probes — ABSENT ✓
- Anatomical/molecular hierarchy (the hierarchy section of the chapter) — ABSENT ✓

---

## Per-slot fill-in sections

### B02 — STILL·ai

**Beat:** B02, COLD OPEN, ~14 s  
**Subject:** FDG-PET scan coronal image showing bright lymph node uptake  
**Archive search:** Wikimedia Commons → "FDG-PET scan" (most PET scan images are from institutional reports, not free archive); NCI Visuals Online (https://visualsonline.cancer.gov/) — search "PET scan" for PD images  
**Provenance note:** Real PET scan images of named patients are PHI; use a schematic/generic or AI-generated image only.

```
B02, schematic FDG-PET coronal scan image printed on paper and pinned to aged newsprint background, warm amber-gold hotspots of radiotracer uptake concentrated in the chest and neck lymph node regions against a dark near-black background, three distinct bright foci clearly visible, editorial desaturated treatment, printed like a journal figure clipping, flat light, no frame, no labels, isolated on cream newsprint texture, overhead view
```

---

### B09 — STILL·ai

**Beat:** B09, THE EXAMPLE, ~16 s  
**Subject:** Oncology case summary note with annotated lymph node locations  
**Archive search:** No real patient notes available; AI-generated only.  
**Provenance note:** Illustrative case — invented patient. All numbers are labeled illustrative.

```
B09, a printed oncology referral or case summary note on white paper pinned to aged newsprint, handwritten annotations marking three circled lymph node locations in the chest diagram, words "high FDG uptake" written beside each circle, a small thumbnail PET scan image in the corner showing three bright spots, desaturated editorial reproduction, flat print, no identifiable patient information, overhead flat light
```

---
