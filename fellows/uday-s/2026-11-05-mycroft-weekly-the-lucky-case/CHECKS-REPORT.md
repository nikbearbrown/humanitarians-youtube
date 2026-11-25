# CHECKS-REPORT — The Lucky Case

Written before the first slate compiled, per the PROOF GATE.

**12 SHOW / 0 justified-HOLD / 0 PUNT-flagged**

| Beat | Act | Class | Artifact named |
|---|---|---|---|
| B00 | INTRO | SHOW | Claude composer, week's ask answered |
| B01 | PROBLEM | SHOW | the Flags cell feeding the runner's command (Manim) |
| B02 | FRAMEWORK | SHOW | three question cards, as a structure (Manim) |
| B03 | CLI | SHOW | composer, the ask |
| B04 | CODE | SHOW | the failing command and its error, verbatim |
| B05 | OUTPUT | SHOW | both argparse cases, real standalone output (Manim) |
| B06 | OUTPUT | SHOW | the identical boilerplate and the 1:1 fix, cited (Manim) |
| B07 | OUTPUT | SHOW | 0-of-70 against a repo-wide 9, cited (Manim) |
| B08 | FALSIFIABILITY | SHOW | episode 6's rule firing on schedule, cited (Manim) |
| B09 | SUMMARY | SHOW | 85 → 5, all in one recipe, cited (Manim) |
| B10 | NEXT STEPS | SHOW | composer, scaffold + GOOD/BAD |
| B11 | OUTRO | SHOW | title-restate card |

## Teaching arc

```
FRAMEWORK ✓        B02 — IS IT READ BY A MACHINE / CRASH OR SOMETHING WORSE /
                   WHAT DOES THE FIX INVALIDATE, shown AS A STRUCTURE at
                   47.27s, ahead of the hero beat at 71.76s.
REUSABLE RUBRIC ✓  All three apply to any field a human writes and software
                   parses. B10 runs them on the viewer's own project.
WORKED EXAMPLE ✓   B04 shows the failure; B05 explains it; B06 answers question
                   1; B08 answers question 3.
REPRODUCED, NOT QUOTED ✓  B05 is the strongest evidence in the reel because it
                   is not the commit's word for anything. The argparse claim is
                   about Python, not about this repository, so it was checked in
                   a standalone interpreter. Case A's error text matches the
                   commit exactly; Case B demonstrates the silent absorption the
                   commit warns about.
SELF-CORRECTION DURING BUILD ✓  The first attempt at Case B used another flag as
                   the following token and still crashed — argparse will not
                   take a "-" token as a value. The example was corrected to a
                   path, which is the realistic shape. SOURCES.md records that.
POPULATION DISCIPLINE ✓  B07 is episode 10's lesson applied before the mistake
                   rather than after: the repo-wide answer (9) and the
                   right-list answer (0) are both shown, with which question
                   each one settles.
SERIES CALLBACK ✓  B08 closes a loop opened in episode 6. The attestation's own
                   point 5 said any edit voids it; this week's edit voided it,
                   and the old record was kept with the voiding appended rather
                   than deleted.
SCAFFOLDED TASK ✓  B10 — list the human-written, machine-parsed fields and name
                   the failure mode of each. GOOD/BAD included.
FRICTION ✓         B05 tells the viewer that the failure they would notice is
                   the good one, which reframes every silent config they have.
BOOKENDS ✓         B00 cold open with the author's name · B10 "Your turn." ·
                   B11 title restate.
NO-SOURCE-NO-VERDICT ✓  Seven beats carry an on-screen citation. B05's strip
                   says the output was produced standalone.
```

## The series arc

5: gates that could not fail. 6: a status not earned. 7: a checker not opening
the files. 8: a denominator counting what could never fail. 9: a record naming
no artifacts. 10: a count mostly not of defects. **11: a documentation field
that was being executed.**

Every one is a signal detached from what it claims to measure. This is the first
where the detachment ran the other way — the field was not describing the
system, the system was *reading the field* — and the first where a rule the
series documented earlier fired on its own schedule.

## The risk, and what answers it

An episode built on "the crash was lucky" can slide into alarmism about a small
bug. Two things hold it straight:

- **The severity is demonstrated, not asserted.** B05 shows both outcomes with
  real output, including that Case B needs a particular shape of next token.
  FACTCHECK records that the first version of that example was wrong.
- **B07 shows the fix was checked before it was made.** Dropping a `--sample`
  flag could in principle promote a sample run to a live one; the 0-of-70 result
  is why it could not, and it was established before the edit.

## Notes

- **ILLUSTRATE LAW**: Claude UI only in B00, B03, B04, B10, B11.
- **Composition**: every beat stacked where content allows, per the rule these
  reels converged on after repeated width-limited underfills.
- The seven Manim beats were a GATE L library miss (searched: table-cell to
  command flow, two-outcome parser comparison, population-versus-population
  stat pair, rule-and-consequence pairing) and are authored as data animations.
- B08 is the longest beat at 32.02s because it asks the viewer to connect this
  week to an episode five weeks old, and that needs both halves on screen
  together.
