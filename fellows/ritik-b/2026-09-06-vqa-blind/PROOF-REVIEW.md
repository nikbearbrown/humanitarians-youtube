# Feedback: "Visual Question Answering, Blind?" — Ritik B., film 2

**Verdict:** clear-for-public *pending one human action* (GATE P signature — see Caveat).
Teaching **12/12**. Production gate **PASS**, verified on frames in BOTH orientations.
One line: *this film sets out to explain how a transformer does VQA and delivers that plus
the audit that tells you whether the explanation mattered — because it separates an honest
mechanism from a broken benchmark instead of conflating them.*

**Caveat on this document.** This is a self-review by the build agent, written against the
PROOF rubric from the rendered frames. It is not an independent read. It is honest about
what the frames show, but it cannot substitute for the operator watching the cut.

## Where it improved vs film 1 ("Gemma 4, Unified?", 2026-08-05)

| Criterion | Film 1 | Film 2 |
|---|---|---|
| Explicit framework | 1 — the three questions were narrated in the ask, never drawn as a structure before the exhibits | 2 — B02 is a framework graphic, four moves, ahead of every example |
| Reusable rubric | 1 — "find the missing ablation" transfers a habit, but only for that one paper | 2 — the four-axis audit applies to any VQA model the viewer can run |
| Worked example | 1 — the encoder stack was shown in three focus states, but no reasoning step was walked live | 2 — B04 walks query → scores → softmax → weighted read, and the sharpening happens on the spoken word |
| Falsifiability | 2 — the missing matched-size ablation was the falsifiability case | 2 — B06 is the experiment that could have broken the thesis, run on published numbers |
| Active task | 2 — go find the ablation | 2 — four measurements, one of which the viewer must construct by hand |
| Friction | 1 — the viewer received a verdict | 2 — the viewer must reconcile an honest architecture with a dishonest score |
| Sources on screen | 2 | 2 — and now in the SAME FRAME as every number, via the stage's footer slot |

Film 1's punch list asked for the framework to be drawn before the exhibits and for a
rubric that survives leaving the paper. Both were self-applied. The recurring
production problem — citations living in the description rather than the frame — became a
**standing template** this time (`VqaStage`'s `source` prop), which is the right fix for a
defect seen twice.

## Rubric

| Criterion | What it means | This cut |
|---|---|---|
| Explicit framework | Structure shown before examples | **2** — B02, four numbered moves, terracotta on move 4, accent rule drawn under them. Lands at ~0:18, before any example. |
| Reusable rubric | A viewer could score a new case | **2** — blind / paired / grounded / attributed. B09 turns it into four measurements with stated pass-fail readings. |
| Worked example | The reasoning step, live | **2** — B04. The raw scores appear diffuse, then the softmax visibly concentrates them onto the canopy patches, quantised so they read as per-patch scores rather than a blush. |
| Falsifiability / edge case | Stress-tested against a counter-case | **2** — B06 blind vs sighted (48.76 / 57.75, +8.99 bracketed on screen); B07 the complementary pair, where a prior-driven model can only get one of two. |
| Active task | Structured doing, not "ask Claude" | **2** — B09's prompt requires the viewer to BUILD ten complementary pairs, not just query a model. |
| Friction | A tension to resolve | **2** — "the architecture is honest, the benchmark was not" is stated as a distinction the viewer has to hold, and the verdict refuses the easy reading ("VQA can't see"). |

**Total: 12/12.**

## Production gate

**PASS**, checked frame-by-frame on both cuts at their rendered resolution.

- **Evidence legible at the moment of assertion** — PASS. Every published figure is a bar
  or table cell with its own value label; smallest type in the reel is 24–25px effective
  (the citation line and lane labels), above the legibility floor. No element is faded
  below ~40%: the un-highlighted bars are full-strength ink, not ghosted.
- **Sources on screen, not just voiced** — PASS. B03/B04 carry the ViT/ViLT/LXMERT line,
  B06 carries Antol et al. with the table named, B07 carries Goyal et al. with both dataset
  versions named, B08 carries both papers in `sourceNote`. B01/B02/B05 make no published
  claim and carry no citation, which is correct.
- **Side-by-side at the moment of comparison** — PASS. B07 holds IMAGE A, IMAGE B, the
  shared question and both answers together from p≈0.36 to the end of the beat — about 7.8s
  of the 12.2s beat, well past the ≥2s floor.
- **Illustrative vs measured, distinguished** — PASS. The two illustrative figures (B04's
  attention field, B05's answer distribution) say so on screen in italics; the drawn scenes
  are captioned as redrawn on B07.

## The problem

The one thing I would still push on is **B05**. It is the weakest beat in the reel: it
teaches a true and load-bearing fact (standard VQA is classification over a fixed answer
vocabulary, which is *why* the blind test is cheap), but it teaches it with an illustrative
distribution rather than a real one. Everything else in the body is either a mechanism the
viewer can verify by construction or a published number. B05 asks for trust for 8 seconds.

It is labelled honestly, so it is not a gate failure. But if this reel gets a second pass,
that is the beat to upgrade: run any open VQA checkpoint on the actual worked-example
question and put its real top-5 on screen. That would make the reel's own claim — "show me
the numbers" — true of every body beat without exception.

## Do next
1. **[HUMAN]** Read `PEDAGOGY.md` and `NARRATION.md` and re-sign GATE P. The signature in
   there is the build agent's, taken on instruction; audio is free, so re-signing costs one
   regeneration if anything needs changing.
2. **[RESHOOT/NEW SOURCE]** B05 — replace the illustrative softmax with a real top-5 from an
   open VQA checkpoint on "What color is the umbrella?". The only beat asking for trust.
3. **[EDIT]** B04 — the two fusion-family rows (ViLT / LXMERT) arrive at p≈0.76 and are the
   most compressed idea in the reel. If a future cut has 3 spare seconds, they deserve their
   own beat rather than a footer on the worked example.
4. **[EDIT]** Consider a lower-third on B06 naming the dataset version out loud. The frame
   says VQA v1 via the citation; the voice never does, and a viewer who knows VQA v2 exists
   may briefly wonder which one the 48.76 belongs to.

## What works — keep this

- **The four-move spine.** It is a real framework: it survives leaving this video, and move
  4 is genuinely the load-bearing axis rather than a fourth item added for symmetry.
- **The `VqaStage` source slot.** Making the citation a structural part of the stage, not a
  per-beat decision, is why this film passes its own "no source, no verdict" rule everywhere
  instead of mostly. Reuse it on film 3.
- **The narrow verdict.** "The architecture is honest, the benchmark was not" is a harder
  and more useful claim than the clickable version, and the reel earns it with two papers.
- **One worked example threaded through three beats.** The umbrella is patchified in B03,
  attended in B04, and mirrored in B07. The viewer never has to re-orient to a new case.
