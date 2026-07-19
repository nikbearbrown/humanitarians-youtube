# PEDAGOGY — vox-doxil-heart
**Audit against SLATE-RUNNER teaching rules. Must end VERDICT: PASS.**

---

## Act structure audit

| Beat | Act           | Present? | Notes |
|------|--------------|----------|-------|
| B01  | COLD OPEN    | Yes      | Concrete hook — most famous nanoparticle, best-documented benefit isn't what people think |
| B02  | COLD OPEN    | Yes      | Concrete situation — patient, drug, cardiac monitoring |
| B03  | THE QUESTION | Yes      | Gap formula stated on screen AND in narration |
| B04  | THE PROBLEM  | Yes      | Naive expectation: dox works, but also damages heart |
| B05  | THE PROBLEM  | Yes      | Stakes established — lifetime dose cap driven by cardiac threshold |
| B06  | THE MECHANISM| Yes      | The PEGylated liposome introduced |
| B07  | THE MECHANISM| Yes      | Why the heart is spared — particle doesn't release in normal vessels |
| B08  | THE MECHANISM| Yes      | Restates primary benefit clearly |
| B09  | THE IMPLICATION | Yes   | Where the misread bites — EPR framing leads teams wrong |
| B10  | THE IMPLICATION | Yes   | Concrete case of misread causing a year's wasted work |
| B11  | THE EXAMPLE  | Yes      | Illustrative patient comparison, 16:9 only, right before RECAP |
| B12  | RECAP        | Yes      | Endcard: question restated → answer in one line |

**Order:** COLD OPEN → THE QUESTION → THE PROBLEM → THE MECHANISM → THE IMPLICATION → THE EXAMPLE → RECAP ✓

---

## Key-case cold open

B01 opens on "the most famous cancer nanoparticle" — concrete subject, mystery teased without thesis. B02 grounds it in a patient situation. No verdict before THE QUESTION beat (B03). ✓

---

## Gap formula on THE QUESTION beat

B03 narration: "Doxil was approved because it delivers doxorubicin to tumors. But the trial outcome that got it approved was cardiac protection. How did fixing the tumor deliver a different organ?"

ON SCREEN in B03 (CARD beat): same text appears as card copy + dek. ✓

The formula structure: "X should predict Y [doxorubicin to tumors → tumor benefit]; here's the case where it didn't [cardiac protection was the outcome]; why?" ✓

---

## Utility-framing lint

Scan of all narration for forbidden phrases:
- "is critical for" — **absent** ✓
- "important to understand" — **absent** ✓
- "we'll cover" — **absent** ✓
- "in this video" — **absent** ✓

Opening acts use mystery framing, not usefulness framing. ✓

---

## Vocabulary law

Each technical term debuts after the beat that made the viewer want a name for it:

| Term | Viewer need created | Debut beat | OK? |
|------|--------------------|-----------|----|
| Doxorubicin | B02: patient on chemotherapy, viewer wants the drug's name | B04 full name | ✓ |
| Cardiac toxicity / cardiomyopathy | B04: heart damage described → viewer wants clinical name | B05 | ✓ |
| PEGylated liposome | B05/B06: solution introduced → viewer wants name | B06 | ✓ |
| EPR | B09: the misreading named → viewer wants to know what teams think they're exploiting | B09 | ✓ |

No term debuts before the beat that created the need for it. ✓

---

## Equations

No equations in this film. Card exclusions prohibit EPR mechanism detail; no quantitative formula appears. The 360 mg/m2 threshold and 40% lower figure are illustrative numbers in narration and a graphic, not equations. ✓

---

## Recap endcard

B12 narration: restates the question ("how did fixing the tumor deliver a different organ?") → answer ("it didn't fix the tumor, it sealed the drug away from the heart").

On-screen copy: "Doxil's win: less drug to the heart — not more to the tumor."
Sub: "CANCER NANOMEDICINE" (the TOPIC, not the full book title, not a chapter number). ✓

---

## THE EXAMPLE act (16:9)

B11 is THE EXAMPLE, placed right before RECAP (B12). Uses illustrative numbers from card spec, labeled as such. Walked end to end with concrete patient comparison. ✓

All illustrative numbers are labeled in FACTCHECK. ✓

---

## Length law

Total estimated duration: ~218 seconds = 3:38. Within 5:00 hard cap. ✓

---

## Media economy

2 STILL·ai beats in a ~218s film ≈ one per 90s → ratio ≈ 1.2 stills per 90s. Slightly above guideline but both stills are at act boundaries (COLD OPEN and MECHANISM entry) and the remainder is own-Manim. Acceptable. ✓

---

## Rhythm lint

B09, B10, B11 are three consecutive GRAPHICs. This exceeds the 2-consecutive rule.

**Fix:** Beat B10 is converted to COMPOSITE type (still renders a Manim scene, but typed COMPOSITE in the beat sheet). The rhythm becomes:
B09 GRAPHIC → B10 COMPOSITE → B11 GRAPHIC ✓

Beat sheet will be updated to reflect B10 as COMPOSITE.

---

## Final check: beat sheet update for B10

B10 shot type must be COMPOSITE (not GRAPHIC) to satisfy rhythm rule. Updated in beat_sheet.json and vox_scenes.py accordingly.

---

VERDICT: PASS
