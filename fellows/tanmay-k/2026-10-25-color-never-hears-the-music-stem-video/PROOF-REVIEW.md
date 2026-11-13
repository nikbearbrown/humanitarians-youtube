# Feedback: "Color Never Hears the Music" — long film (16:9), script review 2

**Rubric:** `PROOF.md` teaching rubric (six criteria, 0–2 each, /12) plus the binary production gate.
**Reviewed:** `BEATS-DRAFT.md` draft 2, after Palmer et al. 2013 was read in full (`FACTCHECK.md` v2). Plan level: no frames exist yet, so legibility is *specified*, not measured.
**Prior review:** `PROOF-REVIEW-1.md` (11/12).
**Verdict:** **clear-for-public at script level.** Teaching **12/12**. Production gate **PASS at plan level**; it must be re-measured on the render, and public still requires that.
One line: this film attempts to teach a two-scale method for predicting colour–music matches and delivers it, with a prediction the paper's own figure can refute.

## Where it improved vs review 1

| Criterion | Review 1 | Review 2 | What changed |
|---|---|---|---|
| Explicit framework | 1 | 2 | The strip (happy–sad, strong–weak) is on screen **from frame one** and named in B01, about 20 s in; it is explained in B04, before any worked example. |
| Reusable rubric | 2 | 2 | Now the paper's own two dimensions, not our simplification. |
| Worked example | 2 | 2 | B05 now uses the paper's own two examples (Bach's F-major dance, Brahms's C-minor Adagio) and says they are the paper's illustration of its hypothesis, not a measured pick. |
| Falsifiability | 2 | 2 | Stronger: B10 makes a prediction that Figure 2 can refute, and B11 reads the answer off it. |
| Active task | 2 | 2 | B10 asks for two pushes placed on the strip, a prediction, and two written answers. |
| Friction | 2 | 2 | Two forces pull opposite ways (fast → yellow-ward, minor → blue-ward); the answer is withheld across a 6 s hold. |

## Rubric (this cut)

| Criterion | Score | Reason |
|---|---|---|
| Explicit framework | 2 | Strip visible frame one; method stated B04 ahead of B05–B11. |
| Reusable rubric | 2 | "Rate the sound, rate each color on the same two scales, do they agree": a three-step card (B05) and a four-step card (B10). Runs on any new tune and swatch. |
| Worked example | 2 | B05 walks two cases through the strip with the reasoning step on screen. |
| Falsifiability / edge case | 2 | B07: two countries only, Western classical only, nonwestern untested. B10–B11: a case where the method could miss, checked against Fig. 2. B04: correlation, not proof of mechanism, direct links not ruled out. |
| Active task | 2 | Structured, with answer slots and a rubric card; not "ask Claude". |
| Friction | 2 | B01 pick-before-told; B10 opposing pulls. |
| **Total** | **12/12** | |

**Reverse-engineered-framework check:** the two scales are the paper's own, fitted to *its* data before this film existed (separate scalings of the 18 pieces and the 37 colors both yielded happy/sad and strong/weak). The categories do not map one-per-example. B10 is a case the scales do not settle in advance. Passes.

## Production gate (plan level)

| Check | Result |
|---|---|
| Evidence legible at the moment of assertion | PASS as specified: every beat names its artifact. **Re-measure at full 4K size on the render** (BEATS.md: a thumbnail passes everything). |
| Sources on screen, not just voiced | PASS: every beat has a source line. Claims drawn from the essay we read (B06, B07's symbolism, B08) are attributed on screen as "from an essay we read", neutrally, with no name and no comment on the essay; their separate-source status is tracked here and in `FACTCHECK.md`, not on screen. B03's grid and swatches are labelled as an illustration, not the paper's figures. B11's three-axis redraw is labelled "approximate, read from chart". |
| Side-by-side at the moment of comparison | PASS as specified: B01 skies together; B04 four correlation rows with the "correlation" card; B07 two contexts and the US↔Mexico row; B08 two strips; B09 three columns; B11 slow-minor, fast-minor, fast-major on shared axes plus the viewer's answers; each held ≥ 3 s. |

## The problem

None that blocks. The largest remaining risk is **not in the script**: B11's three values per axis are read from a chart, and the redraw must be checked against Figure 2 at pixel level when it is built.

## Findings from this pass (applied to `BEATS-DRAFT.md`)

1. **[EDIT, applied] Scales changed to the paper's** (happy–sad, strong–weak). Draft 1's "calm–agitated" is not a single bipolar dimension in the paper's data and was its weakest correlation.
2. **[EDIT, applied] B10–B11 rebuilt.** Draft 1 told the viewer fast-minor was "a case the study doesn't hand you"; the study crossed tempo and mode fully, so it is in the data. The task now asks the viewer to predict a result the paper's chart can confirm or contradict.
3. **[EDIT, applied] B04 states the correlational limit** and the paper's own caveat that direct color–sound links are not ruled out.
4. **[EDIT, applied] B03 numbers and design** (97 listeners: 48 US + 49 Mexican; 18 × 50 s; 37 colors, five best and five worst) now come from the paper's methods.
5. **[EDIT, applied] B07** now carries the paper's US↔Mexico correlations and its "unclear for non-Western scales".
6. **Not changed, still open:** B06 (infants), B07's symbolism line, and B08's scene lengths stay attributed to the essay and visibly labelled. A primary would upgrade them from "the essay says" to findings.

## What works

- The strip on screen from the first frame carries the framework before the argument needs it.
- The pick-before-told opening, and its swapped return, carry the claim in the film's own form.
- B11 gives a way for the film to be wrong, and shows the answer.

## Do next

1. [EDIT] Gate P: read every line aloud once; sign `PEDAGOGY.md`.
2. [EDIT] Generate audio only after Gate P; measure durations (they set the clock, replacing the 3.3 words/s plan).
3. [RESHOOT/NEW SOURCE] Optional: primaries for B06, B07 symbolism, B08, to upgrade the essay attributions.
4. At build: re-run this review on frames, with the production gate measured at full size.
