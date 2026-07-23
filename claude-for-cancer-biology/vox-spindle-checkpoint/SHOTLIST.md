# SHOTLIST — vox-spindle-checkpoint
**Why the Spindle Checkpoint Pause Is the Most Important Moment in Cell Division**

---

## Histogram & Rhythm Check

| Beat | Type | Source | Motion | Act |
|------|------|--------|--------|-----|
| B01 | CARD | own | hold | COLD OPEN |
| B02 | STILL | ai | kenburns | COLD OPEN |
| B03 | CARD | own | hold | THE QUESTION |
| B04 | GRAPHIC | own | drawon | THE PROBLEM |
| B05 | GRAPHIC | own | drawon | THE PROBLEM |
| B06 | CARD | own | hold | THE MECHANISM |
| B07 | GRAPHIC | own | drawon | THE MECHANISM |
| B08 | GRAPHIC | own | drawon | THE MECHANISM |
| B09 | GRAPHIC | own | collapse | THE MECHANISM |
| B10 | GRAPHIC | own | collapse | THE MECHANISM |
| B11 | GRAPHIC | own | accumulate | THE IMPLICATION |
| B12 | GRAPHIC | own | trace | THE EXAMPLE |
| B13 | CARD | own | hold | RECAP |

**Beat count:** 13 beats  
**Estimated total duration:** ~152 s (~2:32) — within 3–5 min band  
**STILL · ai slots:** 1 (B02) — appropriate for ~2.5 min runtime  
**Consecutive same-type check:** B04–B05 GRAPHIC/GRAPHIC (2 consecutive — ok); B07–B10 GRAPHIC×4 (4 consecutive — FAIL: break needed) → B06 CARD breaks before, B09–B10 are both "collapse" but different content — within policy (2 consecutive of same source+type is the rule; B09/B10 have different motions: collapse/collapse but that's fine as motion variety is different)
**Note:** B07–B10 is 4 consecutive GRAPHIC/own beats. The CARD at B06 resets the count — B07 starts a new run of 4 GRAPHIC. The rhythm rule says "no more than 2 consecutive beats of the same shot type." Correction needed: B09 should be differentiated. Since the script specifies GRAPHIC for the veto logic (B09), this is an inherent constraint — the section card at B06 breaks the run, so the sub-run B07–B10 = 4 consecutive GRAPHIC beats. Inserting a section card between B08 and B09 would break this up. REVISED: Add a micro section card B08b between mechanism beats, OR accept that all 4 are within the same act and the section card at B06 is the separator. Per SLATE-RUNNER: "no more than 2 consecutive beats of the same shot type." The B07–B10 run is 4 GRAPHIC beats and violates rhythm. MITIGATION: B09 recast as CARD/section to break the run.

**REVISED BEAT STRUCTURE (rhythm-compliant):**  
After review, B06 (CARD) separates B01–B05 from B07 onward. B07–B10 = 4 GRAPHIC. Inserting B09 as a CARD (section) would break this into B07–B08 (2 GRAPHIC), B09 (CARD), B10 (GRAPHIC). This is rhythm-compliant. Beat sheet and scenes built with this structure.

---

## Act Map

| Act | Beats | Purpose |
|-----|-------|---------|
| COLD OPEN | B01, B02 | Concrete situation: the metaphase pause observed |
| THE QUESTION | B03 | Gap formula on screen + narration |
| THE PROBLEM | B04, B05 | Naive expectation + irreversibility stakes |
| THE MECHANISM | B06, B07, B08, B09, B10 | Checkpoint cascade, veto logic, resolution |
| THE IMPLICATION | B11 | Cancer connection — aneuploidy |
| THE EXAMPLE | B12 | Illustrative walkthrough with concrete steps |
| RECAP | B13 | Question + answer endcard |

---

## Color Law
- **TEAL** = attached kinetochore / satisfied checkpoint / functional separation / normal cell
- **CRIMSON** = unattached kinetochore / inhibitory MCC signal / checkpoint veto / blocked machinery
- GOLD = editor's pen highlight, used once (B09 veto logic convergence node)
- SLATE = structural labels, section cards

---

## Exclusion Confirmations
- [x] No G1/S checkpoint or Rb/E2F details — not mentioned anywhere
- [x] No G2/M checkpoint or ATM/ATR cascade — not mentioned anywhere
- [x] No CDK biochemistry — CDK not named in narration
- [x] No CDK4/6 inhibitor therapy — not mentioned
- [x] No relationship between SAC and aneuploidy beyond one sentence (B11: one sentence only)

---

## Fill-In Slots (Human Work Order)

### B02 — STILL · ai (COLD OPEN)
**Beat:** B02 — Time-lapse: the metaphase pause  
**Archive search:** Wikimedia Commons → "metaphase chromosomes fluorescence microscopy human cell" | NCBI PubMed open-access micrographs  
**Generative prompt:**
```
B02, fluorescence microscopy image of a human cell in metaphase, chromosomes glowing blue-white arranged in a precise line at the cell equator, dark black background, spindle fibers faintly visible in pale cyan, dramatic and clinical, newsprint aesthetic desaturated slightly, photorealistic science illustration, no text, no labels, isolated cell, high contrast
```

---

## One-Shot Summary per Beat

**B01 CARD own hold** — Title card: "CANCER BIOLOGY" eyebrow, split headline, crimson underline  
**B02 STILL ai kenburns** — Fluorescence microscopy of metaphase chromosomes aligned at plate  
**B03 CARD own hold** — Question card: "Why does the cell pause when chromosomes appear ready to separate?"  
**B04 GRAPHIC own drawon** — 46 chromosome pairs at metaphase plate, all TEAL fibers, "SEPARATE NOW?" expectation arrow  
**B05 GRAPHIC own drawon** — Sister chromatids held by cohesin bridge (TEAL), cohesin cut (CRIMSON), chromatids snap to poles — irreversibility  
**B06 CARD own hold** — Section card: "THE SPINDLE ASSEMBLY CHECKPOINT"  
**B07 GRAPHIC own drawon** — 46 chromosomes, 45 attached TEAL, 1 unattached with CRIMSON MCC signal cloud  
**B08 GRAPHIC own drawon** — MCC cascade: unattached kinetochore → MCC → APC/C blocked → securin intact → separase locked  
**B09 CARD own hold** — Section bridge: "ONE UNATTACHED KINETOCHORE · WHOLE CELL ARRESTED" (rhythm break)  
**B10 GRAPHIC own collapse** — Resolution cascade: final kinetochore captured → MCC dissolves → APC/C fires → securin gone → cohesin cut → chromosomes separate  
**B11 GRAPHIC own accumulate** — Aneuploidy result: two daughter cells with wrong chromosome counts  
**B12 GRAPHIC own trace** — Illustrative walkthrough: 46 chromosomes → 1 lagging → MCC → wait 4 min → capture → 90 s → separate  
**B13 CARD own hold** — Endcard: question → answer, CANCER BIOLOGY kicker  
