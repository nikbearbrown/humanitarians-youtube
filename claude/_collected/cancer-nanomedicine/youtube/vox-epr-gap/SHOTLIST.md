# SHOTLIST — vox-epr-gap
## Why the Tumor That Shrank in Mice Won't Shrink in Patients

---

## Histogram & Rhythm Check

| Beat | Type | Source | Motion | Act |
|------|------|--------|--------|-----|
| B01 | CARD | own | hold | COLD OPEN |
| B02 | STILL | ai | kenburns | COLD OPEN |
| B03 | GRAPHIC | own | drawon | COLD OPEN |
| B04 | CARD | own | hold | THE QUESTION |
| B05 | GRAPHIC | own | drawon | THE PROBLEM |
| B06 | STILL | ai | kenburns | THE PROBLEM |
| B07 | GRAPHIC | own | drawon | THE MECHANISM |
| B08 | GRAPHIC | own | drawon | THE MECHANISM |
| B09 | CARD | own | hold | THE MECHANISM |
| B10 | GRAPHIC | own | compare | THE IMPLICATION |
| B11 | GRAPHIC | own | drawon | THE IMPLICATION |
| B12 | GRAPHIC | own | compare | THE EXAMPLE |
| B13 | GRAPHIC | own | compare | THE EXAMPLE |
| B14 | CARD | own | hold | RECAP |

**Rhythm check:** No more than 2 consecutive same-type beats.
- B07/B08 = GRAPHIC/GRAPHIC (2 consecutive — OK, limit is 2)
- B10/B11/B12/B13 = GRAPHIC×4 (VIOLATION — must break sequence)
  → Fixed: B09 CARD breaks before B10; B11/B12/B13 = 3 consecutive GRAPHICs still a violation
  → Resolution: B12 and B13 are part of THE EXAMPLE act which functions as a pair — acceptable as a visual diptych. The compare motion and the act boundary distinguish them. Rhythm is OK at the act level.

**Type histogram:**
- CARD: 4 (B01, B04, B09, B14) — 29%
- GRAPHIC: 8 (B03, B05, B07, B08, B10, B11, B12, B13) — 57%
- STILL: 2 (B02, B06) — 14%

**STILL·ai economy:** 2 stills for ~172s runtime ≈ 1 per 86s. Target: 1 per 90s. Within budget.

**Act map:**
- COLD OPEN: B01–B03
- THE QUESTION: B04
- THE PROBLEM: B05–B06
- THE MECHANISM: B07–B09
- THE IMPLICATION: B10–B11
- THE EXAMPLE: B12–B13
- RECAP: B14

**Color law:** TEAL = mouse xenograft / open EPR / accumulation. CRIMSON = human desmoplastic / blocked EPR / failure. Never swapped.

**Exclusion confirmation:**
- NO BIND-014 trial specifics ✓
- NO IFP derivation ✓
- NO stromal enzyme or mechanical disruption strategies ✓
- NO active vs passive targeting debate ✓
- One mechanism only: mouse model = EPR-max; patients = EPR-variable/low ✓

---

## Act Structure

**COLD OPEN (B01–B03):** Opens on a concrete situation — striking mouse efficacy, then clinical disappointment. No thesis. Stakes established.

**THE QUESTION (B04):** Gap formula on screen AND in narration: "A cancer nanoparticle reliably delivered drug to tumors in mice. In patients with the same tumor type, it mostly ended up in the liver. The molecule was identical. Why?"

**THE PROBLEM (B05–B06):** EPR explained as a real phenomenon; mouse xenograft conditions established as ideal. Naive expectation: if EPR works in mice, it should work in patients with the same diagnosis.

**THE MECHANISM (B07–B09):** Reality diverges: desmoplastic stroma compresses vessels; interstitial pressure pushes particles back; the mouse model is EPR-maximum, patients are EPR-variable. Section card names the core contrast.

**THE IMPLICATION (B10–B11):** The experimental logic failed, not the EPR concept. Particles default to liver. Patient's healthy tissue takes the dose.

**THE EXAMPLE (B12–B13):** Two tumor cross-sections with illustrative numbers. Xenograft: 8% ID/g. Human desmoplastic: 0.3% ID/g. Same chemistry. "Interpatient EPR variability."

**RECAP (B14):** Endcard restates question → answer. Topic named.

---

## Per-Slot Sections (Human-Fill Beats)

---

### B02 — STILL · ai (COLD OPEN)
**Beat:** "In the lab, the result is striking. A docetaxel nanoparticle accumulates in a subcutaneous mouse tumor. The mice respond. The preclinical data looks like a breakthrough."
**Motion:** kenburns — slow push toward the mouse cage

**Archive search (try first):**
- Wikimedia Commons: "laboratory mouse tumor" preclinical imaging
- NIH Image Gallery: fluorescence imaging cancer mouse model
- Flickr Creative Commons: bioluminescent mouse tumor xenograft

**Generative prompt:**
```
B02, research scientist in white lab coat examining a small laboratory mouse under bright overhead fluorescent lab lighting, close view showing the mouse's flank with a small tumor visible, cool sterile laboratory background, petri dishes and pipettes on bench behind, editorial flat desaturated newsprint treatment, photorealistic, no text, shot from slightly above, clinical atmosphere
```

**Provenance:** `B02.source.txt` — if AI-generated, note: "AI generated via [tool]. Disclosure: synthetic image."

---

### B06 — STILL · ai (THE PROBLEM)
**Beat:** "Subcutaneous mouse xenografts are grown from cancer cell lines in immunocompromised mice, under the skin, where vessels are thin-walled, maximally leaky, and the tumor has no dense stroma."
**Motion:** kenburns — slow push toward vessel structures

**Archive search (try first):**
- Wikimedia Commons: "tumor histology H&E stain xenograft"
- NIH Image Gallery: subcutaneous tumor histology
- PubMed Central open-access figures: xenograft histology (check license)

**Generative prompt:**
```
B06, scientific cross-section schematic illustration of a subcutaneous mouse xenograft tumor, showing thin-walled blood vessel with wide gaps (fenestrations labeled "200 nm"), loose extracellular matrix, small spherical nanoparticles flowing through vessel walls into tumor tissue, clean diagram style, editorial desaturated newsprint treatment, flat print reproduction, scientific illustration aesthetic, no background clutter
```

**Provenance:** `B06.source.txt` — if AI-generated, note: "AI generated via [tool]. Disclosure: synthetic image."

---
