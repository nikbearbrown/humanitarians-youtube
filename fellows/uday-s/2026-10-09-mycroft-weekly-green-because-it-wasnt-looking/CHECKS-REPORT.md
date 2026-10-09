# CHECKS-REPORT — Green Because It Wasn't Looking

Written before the first slate compiled, per the PROOF GATE.

**12 SHOW / 0 justified-HOLD / 0 PUNT-flagged**

| Beat | Act | Class | Artifact named |
|---|---|---|---|
| B00 | INTRO | SHOW | Claude composer, week's ask answered |
| B01 | PROBLEM | SHOW | episode 6's entry and the unasked follow-up (Manim) |
| B02 | FRAMEWORK | SHOW | three question cards, as a structure (Manim) |
| B03 | CLI | SHOW | composer, the ask |
| B04 | OUTPUT | SHOW | 187 → 743, and the 476 / 99 recipes, cited (Manim) |
| B05 | CODE | SHOW | the skip list split, verbatim from the committed file |
| B06 | OUTPUT | SHOW | three timings and the 8191 cliff, cited (Manim) |
| B07 | OUTPUT | SHOW | five break tests, cited (Manim) |
| B08 | FALSIFIABILITY | SHOW | four ticks and one cross on my own message, cited (Manim) |
| B09 | SUMMARY | SHOW | one file, two hashes, and the pin, cited (Manim) |
| B10 | NEXT STEPS | SHOW | composer, scaffold + GOOD/BAD |
| B11 | OUTRO | SHOW | title-restate card |

## Teaching arc

```
FRAMEWORK ✓        B02 — WHAT DID IT OPEN / WHY IS EACH EXCLUSION THERE / HOW
                   WOULD YOU KNOW IF IT STOPPED, shown AS A STRUCTURE at
                   46.16s, ahead of the first evidence beat at 68.93s.
REUSABLE RUBRIC ✓  The three questions are about any passing automated check,
                   not about this repository. B10 runs them on the viewer's CI.
WORKED EXAMPLE ✓   B04 answers question 1 with a recount; B05 answers question
                   2 with the code; B07 answers question 3 with break tests.
FALSIFIABILITY ✓   B08 is the strongest form available: the reel checks its own
                   subject's commit message and finds a figure wrong. Four
                   claims reproduce exactly, one does not, and the one that
                   does not is the author's. It is shown as a cross on screen,
                   not conceded in narration.
HONEST SCOPE ✓     B06's timings and B09's 250-file sample are measurements the
                   repository cannot reproduce. They are attributed to the
                   commit in narration and recorded as author-reported in
                   FACTCHECK.md rather than presented as verification.
SCAFFOLDED TASK ✓  B10 — make the check print what it opened, by type, then
                   compute the gap. GOOD/BAD included.
FRICTION ✓         B08 is uncomfortable by design: the episode's sharpest
                   finding is against its own author.
BOOKENDS ✓         B00 cold open with the author's name · B10 "Your turn." ·
                   B11 title restate.
NO-SOURCE-NO-VERDICT ✓  Six beats carry an on-screen citation. The verdict beat
                   cites the replay method, not the commit that is being judged.
```

## The series arc this episode closes

Episode 5 found gates that could not fail. Episode 6 found a status that had not
been earned. Episode 7 finds a checker that was green because it was not
opening the files. The three share one shape — **a signal that was never
connected to the thing it claimed to measure** — and this episode says so
without restating the previous two.

## The risk, and what answers it

A reel whose climax is "I found my own mistake" can read as performance. Two
things hold it straight:

- **The correction is small and the reel says so.** 39 files out of a 187-file
  surface, all in one subsystem, and the claim that carries the argument is
  unaffected. B08 states both halves — the headline is wrong, the argument
  stands — rather than inflating the error for drama.
- **The recount is shown as a method, not a result.** SOURCES.md records the
  first attempt that produced 352 instead of 187, so the method is visible as
  something that can be got wrong.

## Notes

- **ILLUSTRATE LAW**: Claude UI only in B00, B03, B05, B10, B11.
- The seven Manim beats were a GATE L library miss (searched: file-count
  comparison, skip-list diagram, timing bars with a threshold, claim-vs-recount
  ledger, hash fork) and are authored as data animations, not slated.
- B06 and B08 are the longest beats at 31.95s and 31.35s, because each carries a
  two-part finding — a fix and the trap inside it, a count and its correction.
