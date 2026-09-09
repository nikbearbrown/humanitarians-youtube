# GATE P — "BLIP: Noisier Data, Better Model?"

**VERDICT: PASS** — see the signature block at the bottom. Read it before you trust this line.

Reel: `blip-bootstrap` (16:9) + `blip-bootstrap-916` (9:16) · 11 beats · Kokoro `am_onyx`
Source: Li, Li, Xiong & Hoi, *BLIP: Bootstrapping Language-Image Pre-training for Unified
Vision-Language Understanding and Generation*, ICML 2022 — arXiv:2201.12086v2.

## The teach, in one sentence

BLIP's contribution is not an architecture — it is that BLIP treats **its own training data
as a hypothesis to be tested**, and publishes the run with the test switched off.

## The reusable rubric the viewer leaves with

**THE BOOTSTRAP AUDIT** — four questions for anything trained on data it generated itself.
They are not reverse-engineered from BLIP's examples: each axis is a design decision any
self-training pipeline must make, and BLIP happens to have run an ablation on every one.

| # | Axis | The question | BLIP's receipt |
|---|---|---|---|
| 1 | GENERATE | Who writes the new labels, and with what decoder? | §3.3 — captioner = image-grounded text decoder, nucleus sampling |
| 2 | JUDGE | Is the filter a separate copy, or the writer's twin? | **Table 4** — sharing weights drops rejection 25% → 8% and every downstream number |
| 3 | DIVERSITY | Does the writer sample, or play it safe? | **Table 2** — nucleus 25% noise / 80.6 TR@1 beats beam 19% / 79.6 |
| 4 | ABLATE | Is there a run with the bootstrap off, same data, same backbone? | **Table 1** — 78.4 → 79.1 (F) → 79.7 (C) → 80.6 (C+F) |

A viewer can score Self-Instruct, STaR, RLAIF, or any distillation paper on these four
without knowing anything about vision-language models. That is the test of a real rubric:
it survives leaving its home domain. B09 hands it over as a runnable prompt.

## Why axis 2 carries the accent

Because it is the one that is usually skipped, and BLIP is the paper that measured the cost.
A filter finetuned from the same weights as the captioner rejects 8% of its twin's output
instead of 25% — it stops recognising the mistakes it would have made itself. Every
downstream number falls with it. That is confirmation bias with a measurement beside it,
and it is the single most transferable finding in the paper.

## The friction the viewer has to resolve

Nucleus sampling produces captions the filter throws out **more** often — 25% against beam
search's 19% — and the model trained on them is **better**, 80.6 against 79.6 TR@1. The
viewer has to sit with "noisier data, better model" before the resolution lands: diversity
is what the captioner contributes, and the filter is what makes the extra noise affordable.
The video does not resolve this in the narration ahead of the graphic — the butterfly chart
shows both wings growing together first, and the sentence comes after.

## PROOF rubric — self-assessment

| Criterion | Score | Where, and why |
|---|---|---|
| Explicit framework | **2** | B02 is the four-axis audit as a graphic, before any BLIP specific. Each axis carries the table that proves it, so the framework is not four assertions. |
| Reusable rubric | **2** | The axes are decisions every self-training pipeline makes, not categories fitted to BLIP. B09 is the rubric as a runnable prompt with PASS/FAIL readings. |
| Worked example | **2** | B04 walks CapFilt live on one image — alt-text in, synthetic caption written, both judged — then shows the published rejection rate as twenty tiles with five struck. B03 shows the mechanism that makes one model able to do both jobs. |
| Falsifiability / edge case | **2** | Two, not one. B05 runs the paper's own stress test on axis 2. B07 names where the thesis **fails**: on COCO captioning the raw 129M edges the bootstrapped 14M, 130.1 to 129.7. |
| Active task | **2** | B09: quote and grade all four axes on a paper of the viewer's choosing, then name the axis it leaves unproven. A scaffold with a named failure mode, not "ask Claude". |
| Friction | **2** | B06, above. The viewer resolves a contradiction rather than receiving a fact. |
| **Total** | **12 / 12** | |

## Production gate (binary — vetoes publish regardless of score)

| Requirement | How this reel meets it |
|---|---|
| Evidence legible at the moment of assertion | Every number is a counter or a bar that moves to its value as the figure is spoken, sized from the safe box. GATE V samples each beat at ~15/50/85% of its span and reads the frames — 0 BLOCKER, 0 MAJOR required to ship. |
| Sources on screen, not just voiced | `ReelKit.Stage` renders a `source` slot under every illustration, so the citation is in the **same frame** as the number. B04's two caption strings are illustrative and labelled as such on screen; its 25% rate is published and cited separately. |
| Side-by-side at the moment of comparison | B05 holds shared and decoupled columns together for the whole beat. B06's two wings share one spine. B07 holds all five bars plus the dashed reference line, and the exception renders beside the claim, not after it. |

## Honesty notes (DOUBLE-CHECK LAW)

- **Truncated axes are declared.** B06 and B07 both plot spreads of ~2 points, invisible on
  0–100. Both state their floor on screen; B07 draws a real axis strip with a break glyph
  and both tick values. A chart that hides its own floor is the exact failure this series
  is about, so hiding one here would be self-refuting.
- **The abstract's headline gains are not attributed to CapFilt.** +2.7 recall@1, +2.8
  CIDEr and +1.6 VQA score in the abstract are improvements over prior state of the art,
  not the bootstrap's contribution. The reel never uses them; it uses the ablations, where
  the bootstrap is the only variable.
- **"Nine times the data" is arithmetic on published sizes** (129M / 14M ≈ 9.2), not a
  quoted claim.
- **No claim about BLIP-2, or about modern VLMs.** The reel's verdict is scoped to what
  Tables 1, 2 and 4 support, and says "here, not everywhere" out loud.
- **The deltas in B05 are computed from the two columns at render time**, so they cannot
  drift from the numbers printed beside them.

## Signature

**Signed by the build agent (Claude), 2026-09-08, at the operator's instruction to work
without check-ins.** This is NOT a human review, and GATE P is a human gate by design.

What a human still owes this reel: read the eleven narration lines in `NARRATION.md`
against the animated beats, and confirm the register and the claim calibration. Audio is
Kokoro — free and local — so a change costs one regeneration and a re-conform, not money.
Until that read happens, treat this PASS as provisional and the reel as unlisted.
