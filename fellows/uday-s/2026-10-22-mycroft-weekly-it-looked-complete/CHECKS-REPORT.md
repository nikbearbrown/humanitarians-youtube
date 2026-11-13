# CHECKS-REPORT — It Looked Complete

Written before the first slate compiled, per the PROOF GATE.

**12 SHOW / 0 justified-HOLD / 0 PUNT-flagged**

| Beat | Act | Class | Artifact named |
|---|---|---|---|
| B00 | INTRO | SHOW | Claude composer, week's ask answered |
| B01 | PROBLEM | SHOW | the two records and the five absent fields (Manim) |
| B02 | FRAMEWORK | SHOW | three question cards, as a structure (Manim) |
| B03 | CLI | SHOW | composer, the ask |
| B04 | OUTPUT | SHOW | the depth-1 stop and the 26 files, cited (Manim) |
| B05 | CODE | SHOW | gate 3's test, verbatim from the committed recipe |
| B06 | OUTPUT | SHOW | exists:false against resolved:false, cited (Manim) |
| B07 | OUTPUT | SHOW | three fields that became observations, cited (Manim) |
| B08 | FALSIFIABILITY | SHOW | the UTC date bug, cited (Manim) |
| B09 | SUMMARY | SHOW | six distinct sets, four refusals, nothing else moved (Manim) |
| B10 | NEXT STEPS | SHOW | composer, scaffold + GOOD/BAD |
| B11 | OUTRO | SHOW | title-restate card |

## Teaching arc

```
FRAMEWORK ✓        B02 — DOES IT NAME WHAT IT LOOKED AT / ABSENT OR UNKNOWABLE /
                   IS A DEFAULT VISIBLY A DEFAULT, shown AS A STRUCTURE at
                   59.03s, ahead of the first evidence beat at 76.91s.
REUSABLE RUBRIC ✓  The three questions are about any audit record anywhere, not
                   about this repository. B10 runs them on the viewer's own.
WORKED EXAMPLE ✓   B04 answers question 1 with a recount; B05 shows the test the
                   answer is derived from; B06 answers question 2; B07 answers
                   question 3.
FALSIFIABILITY ✓   B08, the date bug — and it is reconstructed rather than
                   quoted. The commit's own author timestamp is 22:28 at UTC-4,
                   which is 02:28 on the 23rd in UTC, so a UTC-formatted field
                   would have printed the wrong day exactly as described. The
                   viewer can check it from the commit alone.
HONEST ABSENCE ✓   The commit's "2 to 32 evidence files" does not reproduce — I
                   count 31 — and resolving it would require running the command
                   that WRITES records. It appears in no frame. B04 uses 26
                   instead, which reproduces exactly and is the figure that
                   carries the argument.
SCAFFOLDED TASK ✓  B10 — list what the record names, and which fields are
                   defaults rather than observations. GOOD/BAD included.
FRICTION ✓         B06 is the uncomfortable one: it argues that writing "not
                   found" when you mean "cannot tell" is a false statement, not
                   a rounding error — which indicts a lot of ordinary tooling.
BOOKENDS ✓         B00 cold open with the author's name · B10 "Your turn." ·
                   B11 title restate.
NO-SOURCE-NO-VERDICT ✓  Seven beats carry an on-screen citation. B09's strip
                   says plainly that the gate writer was not run here.
```

## The series arc

Episode 5: gates that could not fail. Episode 6: a status that was not earned.
Episode 7: a checker that was not opening the files. Episode 8: a denominator
that counted things which could never have failed. Episode 9: **a record that
named no artifacts** — the same shape at the last remaining layer. The signal
was real, the summary was real, and the *receipt* was thin.

This is the episode where the series' own method gets applied to the series'
own output: last week's command produced these records, and this week reads
them against a human's.

## A restriction worth naming

Last episode's strongest evidence was **running** the committed checker, because
`check` only reads. This week the equivalent command **writes a decision record
into the repository**, so it was not run — confirming a count is not worth
leaving a file in someone's repo. That decision costs the reel one figure, and
the reel says so rather than quietly substituting a number.

## The risk, and what answers it

Two episodes running have ended on "I found an error in my own work", and a
third would start to look like a format rather than a finding. Three things keep
B08 honest:

- **It is a different kind of error.** Episodes 7 and 8 were counting mistakes.
  This is a correctness bug in a field, caught by reading, and it is small,
  specific and completely verifiable from the commit.
- **It is reconstructed, not asserted.** The viewer is given the arithmetic.
- **It is placed last among the substance**, after three beats of real
  improvement, so the episode is not organised around the confession.

## Notes

- **ILLUSTRATE LAW**: Claude UI only in B00, B03, B05, B10, B11.
- The seven Manim beats were a GATE L library miss (searched: record diff with
  absent fields, directory walk depth, two-kinds-of-false comparison, date
  offset) and are authored as data animations, not slated.
- B06 is the longest beat at 28.03s because the absent/unknowable distinction
  needs both the principle and the two real cases to land.
