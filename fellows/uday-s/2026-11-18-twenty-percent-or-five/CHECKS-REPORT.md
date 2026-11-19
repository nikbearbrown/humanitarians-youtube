# CHECKS-REPORT — Twenty Percent, Or Five

Written before the first slate compiled, per the PROOF GATE.

**11 SHOW / 0 justified-HOLD / 0 PUNT-flagged**

| Beat | Act | Class | Artifact named |
|---|---|---|---|
| B00 | INTRO | SHOW | Claude composer, topic question answered |
| B01 | BLUF | SHOW | the three things the tool gives you, the log marked (Manim) |
| B02 | FRAMEWORK | SHOW | three question cards (Manim) |
| B03 | EVIDENCE | SHOW | 21% with its denominator, and the study's scale, cited (Manim) |
| B04 | EVIDENCE | SHOW | the practice-measurement moderator, 20/12/5, cited (Manim) |
| B05 | EVIDENCE | SHOW | the performance-measurement moderator, 26/14/9/8, cited (Manim) |
| B06 | EVIDENCE | SHOW | the app classified as the log method, with the paper's conclusion quoted (Manim) |
| B07 | FALSIFIABILITY | SHOW | four limits, the first one against the reel's own case (Manim) |
| B08 | VERDICT | SHOW | the rubric scored, then both sides (Manim) |
| B09 | YOUR TURN | SHOW | composer, scaffold + GOOD/BAD |
| B10 | OUTRO | SHOW | title-restate card |

## How the commissioned topic was handled

The brief was **"AI for learning Music"**, with permission to retitle. A tutorial
on practice apps would be filler. The reel answers the question underneath the
brief — what does the evidence actually say about the quantity these tools
measure — and lands on the result that applies to them most directly.

## Teaching arc

```
PREMISE ✓          B01 — name what the tool really changes: reps, instant
                   feedback, and a log. The log is an instrument, and
                   instruments can be compared.
FRAMEWORK ✓        B02 — HOW WAS PRACTICE MEASURED / HOW WAS PERFORMANCE
                   MEASURED / WHAT ABOUT THE REST, shown AS A STRUCTURE
                   before any figure.
REUSABLE RUBRIC ✓  All three work on any claim about practice and skill, in
                   any domain. B09 turns them on the viewer's own tool.
WORKED EXAMPLE ✓   B03 gives the headline with its denominator; B04 answers
                   question 1 and is the hero; B05 answers question 2 and
                   independently confirms the shape; B06 applies it.
REPLICATION-WITHIN ✓ B05 is not decoration. It is a second, independent
                   moderator in the same paper pointing the same way, which is
                   what turns B04 from a curiosity into a pattern.
FALSIFIABILITY ✓   B07 carries four limits and leads with the one that cuts
                   against the reel's own framing — between-person variance is
                   not a within-person promise.
SOURCE CORRECTION ✓ The circulating reading is "21% practice, so 79% talent".
                   The paper says unexplained. B07 puts the word "talent"
                   under a cross and leaves "unexplained" standing.
SCAFFOLDED TASK ✓  B09 — find your app's proudest number, ask what it is a
                   percentage of and what it was validated against.
                   GOOD/BAD included.
FRICTION ✓         B04 and B06 tell a viewer that the most accurate practice
                   data anyone has ever collected is also the data that gives
                   the smallest effect — which is uncomfortable and checkable.
BOTH SIDES ✓       B08 is genuinely two-sided: the excitement line is specific
                   about what these tools make newly possible for research.
NO-SOURCE-NO-VERDICT ✓  Six Manim beats carry an on-screen citation strip.
BOOKENDS ✓         B00 cold open with the author's name · B09 "Your turn." ·
                   B10 title restate.
```

## The risks, and what answers them

- **Sounding like "practice doesn't matter."** B06 quotes the paper's actual
  conclusion verbatim — important, but not as important as has been argued —
  and B08's excitement line is sincere. The reel's claim is about measurement
  fidelity, not about whether to practise.
- **Over-reading a between-person result as personal advice.** B07 leads with
  exactly this and says the design cannot answer the within-person question.
- **Implicating a product.** No product is named or tested. B01 and B06 describe
  the category by its measurement method, which is the only bridge the source
  supports.
- **Confusing measurement with mechanism.** The moderator is about how practice
  was *recorded*, not about how it was *done*. FACTCHECK.md records this and the
  narration never implies logging practice makes it less effective.

## Notes

- **ILLUSTRATE LAW**: Claude UI only in B00, B09, B10.
- **Composition**: every beat stacked where content allows, per the rule these
  reels converged on after repeated width-limited underfills.
- The eight Manim beats were a GATE L library miss (searched: proportional
  moderator bar set, figure-with-denominator card, method-fidelity ladder,
  limits-with-unticked-boxes rows) and are authored as data animations.
- **Bars encode the stated percentages proportionally** and nothing else; every
  bar carries its own r alongside, so the bar is never the only evidence.

## GATE V, as measured on the clean master

`BLOCKER: 0 · MAJOR: 2`, both on B10 — the library `ClaudeTitleOutro` card,
which is a 2.0s title restate and is sparse by design. That is the same accepted
bookend state as the previous two reels in this series.

Three real defects were found by the gate and fixed before this cut:

| Defect | Beats | Cause | Fix |
|---|---|---|---|
| `low-contrast` 0.23 | B03, B05 | bar fills at 0.16 opacity sat too close to CREAM; the gate averages the luminance of **all** ink pixels, so large pale areas drag the frame down | fill raised to 0.34, strokes to 2.8, and the nine non-accent bar rows moved from `INK_SOFT` to full `INK` |
| `underfill` 51–54% | B04, B07 | the gate's `cover` is the ink **bounding box** over the safe area. The citation strip is the lowest element on the frame and arrived in the last third, so at the midpoint sample the box was 95% wide but only 56% tall | the citation now lands right after the figures it supports — which is where it belongs anyway — and B07's limit rows finish building by ~47% |
| `underfill` (B04, second pass) | B04 | an earlier safe-area fix had narrowed the bar track | labels shortened instead, so the track stays wide |

The empty **scale track** drawn before each bar set came out of this pass. It
was added to stop the midpoint frame reading as half-empty without rushing the
bars ahead of the narration that names them — and it is the better chart, since
every bar is now read against a visible common reference rather than against
whichever bar happens to be longest.
