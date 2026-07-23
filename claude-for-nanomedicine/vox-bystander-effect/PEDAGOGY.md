# PEDAGOGY.md — vox-bystander-effect

Audit of beat_sheet.json narration against vox-explainer teaching rules.

---

## 1. Act Structure — Present and In Order

| Act | Beats | Status |
|-----|-------|--------|
| COLD OPEN | B01, B02 | Present — concrete instance (two drugs, same antibody, different outcomes) |
| THE QUESTION | B03 | Present — gap formula on screen and in narration |
| THE PROBLEM | B04, B05 | Present — antibody controls one step; naive expectation stated |
| THE MECHANISM | B06, B07, B08 | Present — T-DM1 confined vs T-DXd spreads |
| THE IMPLICATION | B09 | Present — "the antibody finds the cell; everything else decides" |
| THE EXAMPLE | B10 | Present — 5 entry points, 5 kills vs ~40 kills (illustrative) |
| RECAP | B11 | Present — question restated, answer given, CANCER NANOMEDICINE shown |

Order: COLD OPEN → QUESTION → PROBLEM → MECHANISM → IMPLICATION → EXAMPLE → RECAP. PASS.

---

## 2. Key-Case Cold Open

B01 opens with a concrete patient-level instance: a HER2-low breast cancer diagnosis, two drugs, same antibody, different approval status. No thesis, no verdict stated. The gap (identical antibody, different outcomes) is shown as a concrete situation.

B02 names the two drugs (T-DM1 and T-DXd) and reinforces the observation without explaining it.

No thesis or verdict before B03. PASS.

---

## 3. Gap Formula on THE QUESTION Beat

B03 narration: "Two drugs. Same antibody. One treats HER2-low tumors. The other cannot. The antibody is identical. Why?"

- Gap formula: "X should predict Y; here's the case where it didn't; why?" — present as: identical antibody should predict identical behavior; it does not; why?
- On screen: B03 uses a CARD beat (scene_class B03_Question) — the question is rendered on screen as a card
- In narration: yes, spoken as above

PASS.

---

## 4. Utility-Framing Lint

Scanning all narration texts for banned phrases:

- "is critical for" — NOT PRESENT
- "important to understand" — NOT PRESENT
- "we'll cover" — NOT PRESENT
- "in this video" — NOT PRESENT

PASS.

---

## 5. Vocabulary Law

Every technical term debuts only after its need is established:

- "HER2-low" (B01): Debuts as the patient's diagnosis — the concrete situation. Need established by the film's topic.
- "T-DM1 / T-DXd" (B02): Debut after B01 established that two drugs exist with the same antibody.
- "antibody" (B03): Used as a concept in B01–B02; formally named in the gap formula at B03.
- "HER2-positive / HER2-negative" (B04): Debuts when explaining WHY antibody only controls one step. Need created by B03 (same antibody → what does antibody actually do?).
- "membrane-permeable / membrane-impermeable" (B06–B08): Debuts as the answer to the problem. Need created by B04–B05 (antibody is not the whole story — so what is?).
- "non-cleavable linker" (B06): Debuts as T-DM1's distinguishing property. Need created by B05 (naive guess is wrong — so what is different between the two drugs?).
- "cleavable linker" (B08): Debuts in contrast to B06's non-cleavable. Need established by B06.
- "bystander effect" (B08): Debuts when the mechanism is fully shown. Need created by B06–B07 (confined killing established; B08 names the opposite).

No term debuts before its need. PASS.

---

## 6. Equations

No equations present in any beat. The mechanism is carried visually (cell field graphics) and narratively. PASS.

---

## 7. Recap Endcard

B11 narration: "Same antibody. One payload stays put — confined by charge. One payload spreads — carried by membrane permeability. That is why T-DXd, not T-DM1, treats HER2-low breast cancer."

B11 scene (B11_Endcard):
- Restates Q→A: same antibody, different payload fate, explains clinical difference
- Shows CANCER NANOMEDICINE (the topic kicker, not the book title)
- Does NOT show the book title ("Cancer Nanomedicine" book is NOT named on screen)
- Does NOT show a chapter number

PASS.

---

## 8. THE EXAMPLE Act

B10 is present immediately before B11 (RECAP):
- Concrete scenario: HER2-low tumor patch
- Made-up numbers: 5 HER2-positive entry points, 5 kills (T-DM1), ~40 kills (T-DXd)
- Numbers labeled illustrative in FACTCHECK
- Beat scene (B10_Example) carries the "illustrative" label in the note rectangle

PASS.

---

## 9. Length

Total estimated duration: 108 seconds = 1:48. Well under the 5:00 hard cap.

PASS.

---

VERDICT: PASS
