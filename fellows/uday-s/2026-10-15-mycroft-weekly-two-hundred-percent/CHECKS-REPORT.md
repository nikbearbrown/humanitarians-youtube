# CHECKS-REPORT — Two Hundred Percent

Written before the first slate compiled, per the PROOF GATE.

**12 SHOW / 0 justified-HOLD / 0 PUNT-flagged**

| Beat | Act | Class | Artifact named |
|---|---|---|---|
| B00 | INTRO | SHOW | Claude composer, week's ask answered |
| B01 | PROBLEM | SHOW | the documented command, 1444 times, never built (Manim) |
| B02 | FRAMEWORK | SHOW | three question cards, as a structure (Manim) |
| B03 | CLI | SHOW | composer, the ask |
| B04 | OUTPUT | SHOW | 97 / 616 / 94-of-97 / 0 clean, cited (Manim) |
| B05 | OUTPUT | SHOW | one numerator over three denominators, cited (Manim) |
| B06 | CODE | SHOW | the denominator comment, verbatim from the committed file |
| B07 | OUTPUT | SHOW | 94 squares read two ways, cited (Manim) |
| B08 | FALSIFIABILITY | SHOW | four figures reproduced, 99-vs-97 reconciled, cited (Manim) |
| B09 | SUMMARY | SHOW | the gate's refusals and the false-failure bug, cited (Manim) |
| B10 | NEXT STEPS | SHOW | composer, scaffold + GOOD/BAD |
| B11 | OUTRO | SHOW | title-restate card |

## Teaching arc

```
FRAMEWORK ✓        B02 — WHAT IS THE DENOMINATOR / COULD EVERY ITEM HAVE BEEN
                   FOUND / ONE DEFECT OR MANY, shown AS A STRUCTURE at 50.92s,
                   ahead of the first number at 71.65s.
REUSABLE RUBRIC ✓  The three questions are about any percentage in any report,
                   not about this repository. B10 runs them on the viewer's own
                   dashboard.
WORKED EXAMPLE ✓   B04 gives the raw result; B05 answers question 1 and 2 with
                   three denominators for one numerator; B07 answers question 3.
FALSIFIABILITY ✓   Two layers. B05 is the subject falsifying itself: a plausible
                   denominator gave 4% and would have shipped, and only an
                   impossible 200% forced a third look. B08 is the reel
                   falsifying its own series: episode 7 said 99 recipes, this
                   one says 97, and the reconciliation is shown rather than the
                   number quietly changed.
HONEST SCOPE ✓     The 4/2 = 200% denominator belongs to an uncommitted
                   intermediate version and cannot be re-run. It is attributed
                   to the commit in narration, and FACTCHECK.md records that
                   the arithmetic reconciliation is mine.
SCAFFOLDED TASK ✓  B10 — name the denominator, then count how many of those
                   items could actually have produced the finding. GOOD/BAD
                   included.
FRICTION ✓         B07 tells the viewer their 94-item bug list is probably one
                   bug, which is good news that costs them a number they may
                   have been reporting.
BOOKENDS ✓         B00 cold open with the author's name · B10 "Your turn." ·
                   B11 title restate.
NO-SOURCE-NO-VERDICT ✓  Six beats carry an on-screen citation. B04 cites the
                   exact command that was run, so a viewer can reproduce it.
```

## The series arc

Episode 5 found gates that could not fail. Episode 6 found a status that had not
been earned. Episode 7 found a checker that was not opening the files. Episode 8
finds a **measurement that was counting things that could never have failed** —
the same shape one level further out: the signal is now real, and the *summary
of it* is what misleads.

This is the first episode where the defect is in the author's own reasoning
rather than in inherited code, and B05 is built so that lands without
self-flagellation: the wrong answer is shown as plausible, because it was.

## The risk, and what answers it

A reel whose hero beat is "I nearly shipped a wrong number" can read as either
humblebrag or hand-wringing. Three things hold it straight:

- **The first denominator is presented as reasonable.** 4/97 is what most people
  would compute. The beat does not treat it as careless.
- **The save is credited to the absurdity, not to diligence.** The commit says
  it plainly — the impossible number "was the only reason it got a third look" —
  and the reel keeps that attribution rather than claiming vigilance.
- **B08 immediately turns the same discipline on the reel itself**, reconciling
  97 against episode 7's 99, so the standard is applied in both directions.

## Notes

- **ILLUSTRATE LAW**: Claude UI only in B00, B03, B06, B10, B11.
- The seven Manim beats were a GATE L library miss (searched: denominator
  comparison, fraction-to-percentage rows, grid of repeated defects, claim
  reconciliation ledger) and are authored as data animations, not slated.
- B05 and B09 are the longest beats at 31.33s and 30.22s. B05 carries three
  complete arguments; B09 carries both commits' remaining substance.
- **GATE F caught this reel rendering before its paperwork existed.** The first
  `./art run` exited on a missing FACTCHECK.md, which is the gate working.
