# GATE P — "Visual Question Answering, Blind?"

Narration review before audio generation. Reel: `youtube/vqa-blind` (16:9) and its 9:16
twin `youtube/vqa-blind-916` — same beat sheet content, same measured audio, different
canvas. 11 beats.

## The teach, in one line

A transformer answers questions about images in four moves, and the fourth move — hide the
image and re-score — is the only one that tells you whether the first three mattered.

## The rubric a viewer walks away able to apply

Not "VQA is interesting." The viewer leaves with a four-axis audit they can run on a model
they did not build, on a question they wrote themselves:

1. **Blind** — replace the image with noise. Does accuracy collapse, or barely move?
2. **Paired** — build a second image where the honest answer flips. Does the model get
   BOTH, or exactly one? Exactly one is the prior's signature.
3. **Grounded** — how much attention mass lands inside the region the question names?
4. **Attributed** — which of the four moves is actually carrying the answer?

That is scoreable on a new case without guessing, which is the test for whether a
framework is real or decorative.

## The falsifiability case

B06 is the beat that could break the reel's own thesis, and it is built from the numbers
that would break it. If the blind model had scored near chance, "the mechanism is the
whole story" would have been the honest verdict. It scored 48.76 against a sighted 57.75 —
so the reel says the mechanism is honest and the *benchmark* was broken, which is a
narrower claim than "VQA doesn't see." B07 then shows the fix working, which is the
falsification of the pessimistic reading: balanced data costs every model 5–7 points, so
the gap was measurable and fixable, not permanent.

## Where the framework sits relative to the examples

B02 shows the four moves as a structure **before** any example appears. B03/B04/B05 walk
moves 1–3 on one worked case ("What color is the umbrella?"). B04 is the reasoning step,
not the conclusion: the raw scores appear diffuse, then the softmax visibly sharpens them
onto the umbrella patches. B06 runs move 4. Nothing is narrated after the fact.

## Narration budget

352 words across 11 beats; body beats run 24–38 words, under the 45–70 ceiling because
the evidence is on screen rather than in the voice. The two bookends that are exempt
(B00's ask, B09's read-and-discuss handoff) are the longest at 24 and 46.

Every published figure is spoken loosely ("within nine points", "clears seventy-eight
percent") and shown exactly (48.76 / 57.75 / +8.99 / 78.20). That split is deliberate:
the voice carries the judgment, the screen carries the digits.

## PROOF rubric — self-assessment

| Criterion | This cut | Score |
|---|---|---|
| Explicit framework | B02 shows the four moves as a graphic before any example | 2 |
| Reusable rubric | The four-axis audit; B09 hands it over as a runnable protocol with pass/fail readings | 2 |
| Worked example | B04 walks "color" → query → scores → softmax → weighted read, live | 2 |
| Falsifiability / edge case | B06 is the experiment that could have broken the thesis; B07 is the fix, with its cost measured | 2 |
| Active task | B09 requires four measurements the viewer produces, including 10 pairs they build by hand | 2 |
| Friction | The viewer must resolve why an honest architecture produced a dishonest score — the mechanism and the benchmark are separated, not conflated | 2 |

**Teaching: 12/12 by self-assessment.** Self-assessment is not a review; a second pass
lives in `PROOF-REVIEW.md`.

## Production gate — what must hold at render

- **Evidence legible at the moment of assertion.** Every published number is a bar or a
  table cell with its own value label, minimum 24px effective type, on cream at warm-ink
  contrast. No opacity floor below ~40% on un-highlighted elements.
- **Sources on screen, not just voiced.** `VqaStage` renders the citation under the
  artwork on B03, B04, B06, B07; B08 carries `sourceNote`. B01/B02/B05 make no published
  claim and carry no citation, which is correct rather than an omission.
- **Side-by-side at the moment of comparison.** B07 holds both images, the shared
  question, and both answers on screen together from p≈0.36 to the end of the beat
  (≈8s at the planned length), well past the ≥2s floor.
- **Both orientations verified independently.** GATE V runs on each compiled cut; the
  9:16 twin is a separate render, not a crop.

## VERDICT: PASS

Signed by the build agent on 2026-09-06 at the operator's explicit instruction to author
and sign the gate in-session ("ask questions if any, do yourself, do fast"). This is a
delegated signature, not a human review: **the operator should read this file and the
narration before the cut is shown to anyone.** GATE P exists to catch a bad teach before
audio is spent; audio here is free (Kokoro, local), so the cost of re-signing after a real
read is one regeneration.
