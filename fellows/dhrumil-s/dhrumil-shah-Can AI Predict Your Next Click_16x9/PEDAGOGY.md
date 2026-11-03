# PEDAGOGY — narration gate and teaching audit

**Gate P status: DRAFT — awaiting human sign-off.** Claude drafted this audit; a human
must read the narration aloud against the animatic before the film is approved for
publishing. Record the verdict at the bottom.

Target viewer: a university student or marketer who has never trained a classifier.

**Intro edition note (B00).** The presenter greeting states the topic and the core answer
("probabilities, not certainties") before the cold open. This front-loads the thesis, so the
B01 hook now works as a demonstration rather than a pure curiosity gap. Reviewer should confirm
the 11-second intro does not cost too much retention on Shorts/Reels, where the first 3 seconds
matter most.

## Checklist

| Question | Verdict | Where it is taught | Notes |
|---|---|---|---|
| Does a beginner understand what a **feature** is? | ✅ | B04 | Raw events visibly become four named numbers with plain-English labels and code names; the window bars show "last 30 / 90 days". |
| Is **prediction clearly different from certainty**? | ✅ | B02, B08, B16 | Stated in B02; *proved* in B08 with a real outcome (61% buy → did not buy); repeated as the last line and end card. |
| Is **classification distinguished from causal inference**? | ✅ | B13 | ≠ equation plus a holdout schematic; "A high scorer might have bought anyway." Schematic labelled ILLUSTRATIVE. |
| Are **targets defined properly**? | ✅ | B05 | Each model has an event, a window, and a 0/1 label. |
| Does the audience understand the **prediction window**? | ✅ | B04, B05, B08 | Prediction date line in B04; 7/30-cell window bars in B05; ring labels repeat the window ("CLICK · 7 DAYS"). |
| Is **churn** defined, not implied? | ✅ | B05 | Demo definition spoken and plated; "Real businesses define it differently." |
| Are **probabilities explained correctly**? | ✅ | B02, B12 | Uncertainty band on the bar; calibration explained with one concrete group (55% → 56%). |
| Is **leakage** addressed? | ✅ | B04, B06 | "counted only before the prediction date"; "a later month it never saw … so the future can't leak in." |
| Are **privacy concerns** acknowledged? | ✅ | B11, B14, end card | Consent + privacy rules guardrail; synthetic data disclosed; opens caveat. |
| Does **Claude's role remain distinct** from the predictive model? | ✅ | B15 | "Claude isn't the predictor here." Architecture stack separates scikit-learn model → scores → Claude → human. |
| Are **marketing actions decisions rather than automatic truth**? | ✅ | B10, B11 | "business choices, not laws of nature"; actions phrased as *tests*; guardrail plate. |
| Does **every animation teach** something? | ✅ with one note | all | B03 particles are the most decorative element; they carry the events-into-dataset idea. Node grid in B01 establishes population scale for the later segmentation. |

## Register audit (Pragmatist)

- Verbs used: *estimates, scores, ranks, sets cutoffs, test* — no "knows", "reads minds", "guarantees".
- One deliberate rhetorical question per bookend (B01 "But how does it know?", B16 "can AI predict your next click?").
- No product promotion: Salesforce appears once as "one commercial implementation — not the only way"; Claude is explicitly *not* the predictor.

## Cognitive load

- ≤ 6 primary elements per beat (tracker counts as one).
- Every number spoken is on screen at the same moment (cue-synced reveals).
- Burned-in captions ≤ 2 lines, ≤ 25 characters per line, keyword highlights only for pipeline terms.

## Risks for a nontechnical viewer

| Risk | Mitigation in film |
|---|---|
| "ROC-AUC" and "PR-AUC" are jargon | Not spoken; shown only as small chips with "0.5 = chance" and "base rate" hints. Narration explains calibration in words instead. |
| "Holdout" unfamiliar | Visualised as a group that gets "no email". |
| Synthetic data mistaken for real | "fictional coffee shop" on B01, SOURCE tags on every scene, disclaimer on end card. |

## Human Gate P verdict

- [ ] Narration read aloud — no stumbles, no ambiguous claims
- [ ] Watched full review cut with captions
- [ ] FACTCHECK open items S01 and G05 resolved
- [ ] At least one refinement pass requested and applied

Reviewer: ______________________ Date: ____________ Verdict: PASS / REVISE
