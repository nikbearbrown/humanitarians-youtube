# CHECKS-REPORT — Unbuilt Is Not Broken

Written before the first slate compiled, per the PROOF GATE.

**12 SHOW / 0 justified-HOLD / 0 PUNT-flagged**

| Beat | Act | Class | Artifact named |
|---|---|---|---|
| B00 | INTRO | SHOW | Claude composer, week's ask answered |
| B01 | PROBLEM | SHOW | 725 split into 554 unbuilt and 171 real (Manim) |
| B02 | FRAMEWORK | SHOW | three question cards, as a structure (Manim) |
| B03 | CLI | SHOW | composer, the ask |
| B04 | OUTPUT | SHOW | 725 → 171 → 80 and the clean count, cited (Manim) |
| B05 | OUTPUT | SHOW | the same question against two lists, cited (Manim) |
| B06 | CODE | SHOW | the eight-line frontmatter block, verbatim |
| B07 | OUTPUT | SHOW | the guard that never fired, cited (Manim) |
| B08 | FALSIFIABILITY | SHOW | my own miscount, with the file named, cited (Manim) |
| B09 | SUMMARY | SHOW | the prepend proved from the diff, cited (Manim) |
| B10 | NEXT STEPS | SHOW | composer, scaffold + GOOD/BAD |
| B11 | OUTRO | SHOW | title-restate card |

## Teaching arc

```
FRAMEWORK ✓        B02 — DOES IT CONTRADICT A CLAIM / WHICH LIST DID YOU MATCH
                   AGAINST / DID THE GUARD EVER FIRE, shown AS A STRUCTURE at
                   57.96s, ahead of the first evidence beat at 80.96s.
REUSABLE RUBRIC ✓  All three questions are about any count of problems from any
                   tool. B10 runs them on the viewer's own backlog.
WORKED EXAMPLE ✓   B04 answers question 1; B05 answers question 2; B07 answers
                   question 3. One question per beat, each against a figure.
FALSIFIABILITY ✓   B08 — and it is the strongest instance this series has had,
                   because the error is mine and it is the SAME error as the
                   subject's. While checking the commit's "42" I ran a grep
                   over a folder instead of a list and got 98 where the truth
                   is 97. Same week, same shape, named file.
HONEST ABSENCE ✓   Three figures from the third commit (531, 73-of-157, 956)
                   could not be reproduced and appear in no frame. That commit
                   is background, not evidence, and FACTCHECK.md says so.
INDEPENDENT PROOF ✓ B09 does not take the commit's "0 bodies altered" on trust.
                   It establishes the same thing from the diff's shape — zero
                   deletions, every hunk inserting 8 lines at line 1 — which a
                   viewer can run themselves.
SCAFFOLDED TASK ✓  B10 — sort findings by whether they contradict a claim.
                   GOOD/BAD included.
FRICTION ✓         B01 tells the viewer that a number they have been quoting is
                   mostly not what they think it is.
BOOKENDS ✓         B00 cold open with the author's name · B10 "Your turn." ·
                   B11 title restate.
NO-SOURCE-NO-VERDICT ✓  Seven beats carry an on-screen citation. B04 cites the
                   exact command, so a viewer can reproduce the headline.
```

## The series arc

Episode 5: gates that could not fail. 6: a status not earned. 7: a checker not
opening the files. 8: a denominator counting things that could never fail. 9: a
record naming no artifacts. **10: a count in which most entries were not
defects at all.**

Every one is the same shape — a signal detached from the thing it claims to
measure — and this is the first where the fix is not a new check but a
*distinction*: a finding is a defect only when it contradicts a claim.

## Why B08 is placed where it is

Two previous episodes ended on an error of mine, and a third would be a format.
This one earns its place for a reason the others did not have: **it is the same
error as the subject's**, made in the same week, while fact-checking the very
commit that describes it. That is not a confession beat — it is the rubric
demonstrating it applies to the person holding it.

It is placed after the three rubric answers and before the summary, so the
episode closes on verified work rather than on the mistake.

## Notes

- **ILLUSTRATE LAW**: Claude UI only in B00, B03, B06, B10, B11.
- **Composition**: built against the failure that cost a beat in three of the
  last four reels — wide, short groups are width-limited and underfill. Every
  beat here is stacked where content allows.
- The seven Manim beats were a GATE L library miss (searched: count splitting
  into categories, query-versus-query comparison, silent guard panel, diff-shape
  proof) and are authored as data animations, not slated.
- B05 and B09 are the longest beats at 29.73s and 30.22s; each carries a
  complete argument plus its caveat.
