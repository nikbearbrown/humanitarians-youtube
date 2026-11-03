# CHECKS-REPORT — Levels, Not Layers

Written before the first slate compiled, per the PROOF GATE.

**11 SHOW / 0 justified-HOLD / 0 PUNT-flagged**

| Beat | Act | Class | Artifact named |
|---|---|---|---|
| B00 | INTRO | SHOW | Claude composer, topic question answered |
| B01 | BLUF | SHOW | layers vs levels, drawn (Manim) |
| B02 | FRAMEWORK | SHOW | three question cards (Manim) |
| B03 | EVIDENCE | SHOW | two memory speeds vs four clocks, cited (Manim) |
| B04 | EVIDENCE | SHOW | Table 2's three-way comparison, cited (Manim) |
| B05 | EVIDENCE | SHOW | the CMS ablation, cited (Manim) |
| B06 | FALSIFIABILITY | SHOW | Table 1's baseline row, with the paper's own scoping sentence (Manim) |
| B07 | EVIDENCE | SHOW | the CTNL ordering, labelled not-to-scale (Manim) |
| B08 | VERDICT | SHOW | rubric scored + the authors' limitation (Manim) |
| B09 | YOUR TURN | SHOW | composer, scaffold + GOOD/BAD |
| B10 | OUTRO | SHOW | title-restate card |

## Teaching arc

```
PREMISE FIXED ✓    B01 — the commissioning topic called HOPE a training method.
                   Correcting that is the first substantive beat, not a footnote,
                   because every later beat depends on it being an architecture.
FRAMEWORK ✓        B02 — WHAT UPDATES AND HOW OFTEN / BEATEN AGAINST WHAT / DID
                   THE AUTHORS SAY SOLVED, shown AS A STRUCTURE before the first
                   result. Lands inside the first third of the reel.
REUSABLE RUBRIC ✓  The three questions are about continual-learning claims in
                   general. B09 runs them on the next paper the viewer meets.
WORKED EXAMPLE ✓   B03 answers question 1 with the mechanism; B04 and B05 give
                   it numbers; B06 answers question 2; B08 answers question 3.
FALSIFIABILITY ✓   B06 is the reel's spine: on the paper's hardest retrieval
                   test a plain Transformer (40.8) beats HOPE (24.8), and the
                   paper's own sentence scopes its win to attention-free models.
                   The headline reading does not survive its own source table.
HONEST NEGATIVE ✓  B05 reports the ablation as load-bearing by LESS THAN A POINT
                   of accuracy, rather than as a vindication.
SCAFFOLDED TASK ✓  B09 — find the baseline table, name what is missing from it,
                   read the limitations section. GOOD/BAD included.
BOOKENDS ✓         B00 cold open with the author's name · B09 "Your turn." ·
                   B10 title restate.
NO-SOURCE-NO-VERDICT ✓  Six beats carry an on-screen citation naming the exact
                   table. The verdict beat quotes the authors, not a summary.
```

## The risk in this reel, and what answers it

A reel built around "the headline is wrong" can slide into dismissal, which
would be its own kind of inaccuracy — the paper's results are real and the
mechanism does work. Three things hold it straight:

- **B07 is placed after B06 on purpose.** The falsification lands first, then
  the beat that shows what the architecture is genuinely good at. The reel's
  last evidence beat is a HOPE win, not a HOPE loss.
- **B08 is two-sided by construction.** BE EXCITED ABOUT comes before BE
  SCEPTICAL OF, and the excitement is specific (levels as a design axis), not a
  politeness.
- **FACTCHECK.md records the omission that would have softened B06** —
  Hope-Attention's 42.4 beating the Transformer's 40.8 — so the choice is
  visible rather than hidden.

## Notes

- **ILLUSTRATE LAW**: Claude UI only in B00, B09, B10.
- The eight Manim beats were a GATE L library miss (searched: benchmark
  comparison table, memory levels at different frequencies, needle-in-haystack
  ranking, ablation panel) and are authored as data animations, not slated.
- B07 is the only beat whose geometry is not a measured quantity, and it is
  captioned on screen as such.
