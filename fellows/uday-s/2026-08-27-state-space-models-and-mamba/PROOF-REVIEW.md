# PROOF self-review — "State Space Models and Mamba Architecture"

Scored against `brutalist.art/PROOF.md` before asking anyone else to watch.
Frames were inspected at the moment of each claim; nothing is scored from the
beat sheet alone.

**Verdict:** meets the teaching bar and passes the production gate.
Publication remains a human decision — this toolkit ships nothing.

## Rubric

| Criterion | What it means | This cut | Score |
|---|---|---|---|
| **Explicit framework** | Organizing idea shown as a structure *before* the examples | B02 — three axis cards (STATE / UPDATE / COST) on screen at 22.98s, before any architecture is scored | **2** |
| **Reusable rubric** | A viewer could apply the axes to a new case without guessing | The axes are stated as questions about *any* sequence model, and B10 has the viewer run them on an architecture the reel never mentions | **2** |
| **Worked example** | A case walked through the framework live — the reasoning, not the conclusion | B03 — RNN and Transformer scored cell by cell, with the reasoning spoken ("it forgets nothing, and pays for that on every token") | **2** |
| **Falsifiability / edge case** | Framework stress-tested against a case that breaks it | B08 — and it is *predicted* by axis 1 rather than bolted on: fixed state ⇒ cannot copy unless state grows with the sequence (Jelassi et al. 2024). Sourced on screen | **2** |
| **Active task** | CTA requires structured doing — never "ask Claude" | B10 — score a named architecture on the three axes, then name a task it should fail and which axis predicts it. GOOD/BAD answers stated | **2** |
| **Friction** | Viewer must resolve a tension, not just receive facts | The reel sets up a genuine turn — the axis that makes Mamba cheap is the axis that limits it — and B10 forces the viewer to find a failure rather than recite a feature. Still largely delivery, though: the viewer is told the tension, not made to sit in it before the reveal | **1** |

**Teaching: 11 / 12.** Ship bar is ≥ 8.

## Production gate (binary — vetoes publish regardless of teaching score)

| Check | Verdict | Evidence |
|---|---|---|
| **Evidence legible at the moment of assertion** | PASS | GATE B pixel-true audit: **0 errors, 0 warnings** across all nine Manim scenes. GATE W clean on contrast/margins/overlap. Frames inspected at 38s, 78s, 118s, 160s |
| **Sources on screen, not just voiced** | PASS | Four beats carry a visible arXiv citation at the moment of the claim: B05 (2111.00396), B06 (2312.00752), B07 (2312.00752), B08 (2402.01032). Every numeric or attributed claim sits under one |
| **Side-by-side at the moment of comparison** | PASS | B03 holds the RNN and Transformer columns together for the rest of the beat. B08 holds the fixed state box and the growing store together, with the verdict beneath both |

## What the gates caught, and what was done about it

Three defects were found by the pipeline and fixed at source — none suppressed:

1. **B07 — text crossing its own card border** (GATE B: "label on a curve/line", 3
   errors). A fixed card width narrower than its body text. Fixed by sizing every
   box to its content and moving the four claims to a 2×2 grid; the same guard was
   added to the shared `card()` helper so other beats cannot repeat it.
2. **B07 / B08 — the citation line colliding with the body.** Fixed with a
   `fit_src()` band that reserves the citation strip, and by composing B08's
   verdict *into* the fitted group rather than positioning it afterwards.
3. **B06 — "forget" labelled but not shown.** The word sat above a block that
   looked identical to its neighbours, so the visual did not demonstrate the
   claim. The forgotten block is now struck through — a strikethrough rather
   than a fade, so it stays above the ~40% opacity floor and leaves terracotta
   reserved for "propagate". This one is a SHOW-DON'T-TELL fix, not a layout fix,
   and it is the one that mattered most.

## Honest limitations

- **Friction scored 1**, and that is the real ceiling on this cut. Raising it
  would mean withholding the copying result and asking the viewer to predict
  what a fixed-size state must fail at — a structural change, logged for next
  week rather than claimed as done.
- **`underfill` findings remain** (59 frames of 431, ~14%), all at beat openings
  during staggered reveals, plus the sparse outro card. The 4 `low-contrast`
  flags co-occur with 10–11% fill — they are near-blank opening frames with too
  little ink to measure, not content that is hard to read.
- **The B01 cost curves carry no axis numbers**, deliberately. They show the
  *shape* of quadratic versus linear growth; no measured data backs a specific
  curve, and REBUILD LAW permits shape without inventing figures.
- **No benchmark table.** Only the four claims the Mamba abstract states in its
  own words appear. Anything richer would require re-reading the results tables,
  which was not done for this cut.
