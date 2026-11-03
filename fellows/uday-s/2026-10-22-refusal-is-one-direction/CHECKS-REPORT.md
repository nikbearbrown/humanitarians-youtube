# CHECKS-REPORT — Refusal Is One Direction

Written before the first slate compiled, per the PROOF GATE.

**11 SHOW / 0 justified-HOLD / 0 PUNT-flagged**

| Beat | Act | Class | Artifact named |
|---|---|---|---|
| B00 | INTRO | SHOW | Claude composer, topic question answered |
| B01 | BLUF | SHOW | the two corrections to the commissioned phrase (Manim) |
| B02 | FRAMEWORK | SHOW | three question cards (Manim) |
| B03 | EVIDENCE | SHOW | 13 / 72B / one-dimensional, plus the erase-add symmetry, cited (Manim) |
| B04 | EVIDENCE | SHOW | the authors' own conclusion, quoted and attributed (Manim) |
| B05 | FALSIFIABILITY | SHOW | the EMNLP 2026 correction, cited (Manim) |
| B06 | EVIDENCE | SHOW | the non-effects, and the unquantified claim, cited (Manim) |
| B07 | EVIDENCE | SHOW | the security experiment, scoped on screen, cited (Manim) |
| B08 | VERDICT | SHOW | rubric scored, both sides, cited (Manim) |
| B09 | YOUR TURN | SHOW | composer, defensive scaffold + GOOD/BAD |
| B10 | OUTRO | SHOW | title-restate card |

## Scope decision, recorded before anything was built

The topic was commissioned as "Neuron Abliteration to Uncensor an LLM". The
underlying result is a **NeurIPS 2024 interpretability paper** whose own
conclusion is a warning about the brittleness of safety fine-tuning — which
makes it legitimate and useful explainer material.

**This reel is deliberately non-operational.** No frame contains code, a layer
index, a hyperparameter, a model to edit, or a repository. The conceptual
finding is explained because it is published and because understanding it is how
a viewer reasons about alignment robustness; the recipe for applying it is
withheld. All practical guidance runs defensively — how to evaluate someone
else's edited weights before running them.

That line is the same one this series has drawn before: explain the finding,
correct the premise, do not hand over the step.

## Teaching arc

```
PREMISE FIXED ✓    B01 — both halves of the commissioned phrase are wrong. It
                   is a direction, not a neuron; it removes a behaviour, not a
                   lock. Everything after depends on this landing first.
FRAMEWORK ✓        B02 — WHAT CHANGED / WHAT DID IT COST / WHO ELSE TOUCHED THE
                   WEIGHTS, shown AS A STRUCTURE before any figure.
REUSABLE RUBRIC ✓  The three questions work on any "we removed the safety
                   behaviour" claim. B09 turns them on a model the viewer is
                   considering running.
WORKED EXAMPLE ✓   B03 answers question 1; B05 and B06 answer question 2; B07
                   answers question 3. One question per beat, each against a
                   primary source.
FALSIFIABILITY ✓   B05 — and it is a genuine correction rather than a
                   dismissal. The follow-up confirms a shared one-dimensional
                   control exists and denies that the mechanism behind it is
                   one-dimensional. The spark line keeps both halves: "right
                   about the knob, wrong about the mechanism."
HONEST ABSENCE ✓   B06 is built around a missing number: the source says
                   "minimal effect on other capabilities" and attaches no
                   benchmark figure. The beat shows the phrase and flags the
                   absence rather than supplying a number from elsewhere.
SCOPED SOURCE ✓    B07 puts what the experiment was NOT on screen before any
                   figure — not a hub survey, not an abliterated model.
SCAFFOLDED TASK ✓  B09 — base, claimed edit, signature, tool access. Four
                   checkable facts, ending on the one that sets the stakes.
FRICTION ✓         B06 takes away the appealing reading (hidden capability
                   unlocked) and replaces it with a duller true one.
BOOKENDS ✓         B00 cold open with the author's name · B09 "Your turn." ·
                   B10 title restate.
NO-SOURCE-NO-VERDICT ✓  Seven beats carry an on-screen citation. The verdict
                   beat cites all three sources.
```

## The risk, and what answers it

Two risks pull in opposite directions here.

- **Over-claiming the danger.** The security note is the newest and least
  replicated source, and its headline travels further than its evidence. B07's
  scope panel lands first and the citation strip carries the note's own caveats,
  so the beat cannot be read as "abliterated models were found backdoored".
- **Dismissing the technique as mere vandalism.** It is a real interpretability
  result with a real finding behind it, and B03 and B04 give it four beats of
  straight exposition before any complication. The excitement line in B08 is
  specific: interpretability locating a trained behaviour this precisely.

## Notes

- **ILLUSTRATE LAW**: Claude UI only in B00, B09, B10.
- **NEVER THROUGH TEXT**: B01 and B06 both negate phrases, and in both the cross
  sits beside the phrase rather than across it.
- The eight Manim beats were a GATE L library miss (searched: correction rows,
  activation-direction schematic, quotation panel with funnel, claim-row stack,
  two-rate comparison) and are authored as data animations, not slated.
- B07 is the longest beat because the scope has to land before the numbers do.
