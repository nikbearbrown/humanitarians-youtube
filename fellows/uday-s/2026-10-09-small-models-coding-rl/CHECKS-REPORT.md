# CHECKS-REPORT — One Model, Three Numbers

Written before the first slate compiled, per the PROOF GATE.

**11 SHOW / 0 justified-HOLD / 0 PUNT-flagged**

| Beat | Act | Class | Artifact named |
|---|---|---|---|
| B00 | INTRO | SHOW | Claude composer, topic question answered |
| B01 | BLUF | SHOW | the three published scores, uncaptioned (Manim) |
| B02 | FRAMEWORK | SHOW | three question cards (Manim) |
| B03 | EVIDENCE | SHOW | the training recipe + decontamination, cited (Manim) |
| B04 | EVIDENCE | SHOW | four settings, each labelled with what it measures (Manim) |
| B05 | EVIDENCE | SHOW | a smaller model scoring higher on a different scaffold (Manim) |
| B06 | FALSIFIABILITY | SHOW | the table's own scaffold and setting columns (Manim) |
| B07 | EVIDENCE | SHOW | RL vs distillation against the selection gain (Manim) |
| B08 | VERDICT | SHOW | rubric scored, both sides, and the cost (Manim) |
| B09 | YOUR TURN | SHOW | composer, scaffold + GOOD/BAD |
| B10 | OUTRO | SHOW | title-restate card |

## Teaching arc

```
BLUF ✓             B01 opens with the three numbers and refuses to explain them
                   yet. The viewer is made to feel the problem before being
                   handed the rubric that resolves it.
FRAMEWORK ✓        B02 — ONE RUN OR BEST OF N / WHICH SCAFFOLD / WHO PICKED THE
                   WINNER, shown AS A STRUCTURE before any evidence beat.
REUSABLE RUBRIC ✓  The three questions apply to any coding-agent score. B09
                   runs them on the next model card the viewer meets.
WORKED EXAMPLE ✓   B04 answers question 1; B05 answers question 2; B08 answers
                   question 3. One question per beat, each against a published
                   figure rather than an argument.
FALSIFIABILITY ✓   B06 — the comparison table that everyone reads as a ranking
                   contains four scaffolds and three test-time settings. The
                   reel's claim is checkable against the authors' own columns,
                   and it is the authors who published them.
HONEST NEGATIVE ✓  B05 shows the subject model LOSING to a smaller one at one
                   attempt. B07 concludes that the training method — the thing
                   the topic was commissioned about — is not where the headline
                   gain came from.
SCAFFOLDED TASK ✓  B09 — name the scaffold, the context window, the N, and the
                   selector. Four checkable asks, no judgment required.
FRICTION ✓         B04 labels 71.0 "upper bound, not shippable" and draws it
                   with a dashed border, which takes the most quotable number
                   in the area away from the viewer.
BOOKENDS ✓         B00 cold open with the author's name · B09 "Your turn." ·
                   B10 title restate.
NO-SOURCE-NO-VERDICT ✓  Eight beats carry an on-screen citation naming the
                   release or the paper. No aggregator page sources any figure.
```

## How the commissioning topic was handled

The brief asked about **optimizing smaller models for coding with agentic
systems and RL** — and the honest finding is that the published evidence cannot
cleanly separate the two levers it names. Rather than pick one and overclaim,
the reel makes the inseparability the subject:

- The RL recipe is given in full (B03), including the decontamination step that
  makes its score meaningful at all.
- The agentic side is shown to be worth more than the gap between the two
  training methods (B05, B07).
- The practical payoff is a rubric for reading any such claim, plus the cost of
  the big number — 16× inference — so a viewer can decide what to actually build.

That is a more useful answer than a ranking, and it is the one the sources
support.

## The risk, and what answers it

A reel arguing "the headline number is inflated" can slide into dismissing real
work. Three things hold it straight:

- **B03 is unreservedly positive** and comes before any criticism: a 32B open
  model, RL-only with no distillation, decontaminated, doing real repository
  work. That is genuinely notable and the reel says so first.
- **B08's excitement line is specific**, not a politeness — it names what is
  impressive and why.
- **The verdict is "budget for it", not "ignore it".** Test-time scaling is
  treated as a real technique with a real price, not as a trick.

## Notes

- **ILLUSTRATE LAW**: Claude UI only in B00, B09, B10.
- The eight Manim beats were a GATE L library miss (searched: benchmark score
  decomposition, scaffold comparison table, pass@k vs best@k bars, two-method
  contrast with a delta bar) and are authored as data animations, not slated.
- B06 shows 6 of the table's 10 rows and says so on the citation strip; the
  selection spans all three settings and three of the four scaffolds, and
  includes both the highest and the lowest rows.
