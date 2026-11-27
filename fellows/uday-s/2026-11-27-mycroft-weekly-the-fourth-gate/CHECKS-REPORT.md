# CHECKS-REPORT — The Fourth Gate

Written before the first slate compiled, per the PROOF GATE.

**12 SHOW / 0 justified-HOLD / 0 PUNT-flagged**

| Beat | Act | Class | Artifact named |
|---|---|---|---|
| B00 | INTRO | SHOW | Claude composer, the week's ask answered |
| B01 | PROBLEM | SHOW | the two-line promotion and its self-reported weaknesses (Manim) |
| B02 | FRAMEWORK | SHOW | three question cards (Manim) |
| B03 | CLI | SHOW | composer, the audit ask |
| B04 | CODE | SHOW | the three gate tests, verbatim from `20795b2` |
| B05 | OUTPUT | SHOW | three gates run against planted defects, with exit codes (Manim) |
| B06 | OUTPUT | SHOW | gate 4 matching its own test line (Manim) |
| B07 | FALSIFIABILITY | SHOW | the correction to the commit message, plus two caveats (Manim) |
| B08 | OUTPUT | SHOW | five recounted figures and the file-count note (Manim) |
| B09 | SUMMARY | SHOW | three things the sign-off got right (Manim) |
| B10 | NEXT STEPS | SHOW | composer, scaffold + GOOD/BAD |
| B11 | OUTRO | SHOW | title-restate card |

## GATE L — library-first

Searched before authoring: a claim-versus-measured comparison card, an
exit-code result matrix, a self-referential-match diagram, and a recounted-
figures tick list. Genuine miss on all four; the seven Manim beats are authored
as data animations and the miss is logged. Reused unchanged from the library:
`ClaudeComposerAsk`, `ClaudeCodeBeat`, `ClaudeTitleOutro`.

## Teaching arc

```
PREMISE ✓          B01 — a promotion whose sign-off lists its own weaknesses.
                   That is the thing worth copying, before any defect is named.
FRAMEWORK ✓        B02 — CAN IT FAIL / WHAT HAPPENS TO A FAILURE IT CANNOT
                   JUDGE / WHAT WAS WRITTEN DOWN UNASKED, shown AS A STRUCTURE
                   before any evidence.
REUSABLE RUBRIC ✓  All three work on any check in any project. B10 turns them
                   on the viewer's own in a single command.
WORKED EXAMPLE ✓   B04 shows the three tests; B05 runs them against planted
                   defects and reports measured exit codes.
ORIGINAL FINDING ✓ B06 — gate 4 greps for a string that lives inside its own
                   test command. Not in the commit. Reproduced standalone.
FALSIFIABILITY ✓   B07 — the recount CORRECTS THE AUTHOR'S OWN COMMIT MESSAGE:
                   gate 6 is "cannot pass", not "cannot fail", and the two have
                   opposite consequences. Two further caveats carried.
SELF-IMPLICATION ✓ The commit being audited is the author's own sign-off, and
                   the episode's headline finding is a defect he missed.
WHAT HELD UP ✓     B08 — most figures reproduce exactly, including a lifecycle
                   count that lands on the nose. A reel that only reported
                   failures would be as unbalanced as one that reported none.
SCAFFOLDED TASK ✓  B10 — plant the defect the check exists to catch, run it,
                   read the exit code. GOOD/BAD discriminator included.
NO-SOURCE-NO-VERDICT ✓  Six Manim beats carry an on-screen citation strip.
BOOKENDS ✓         B00 cold open with the author's name · B10 "Your turn." ·
                   B11 title restate.
```

## The risk, and what answers it

- **Sounding like a takedown of a colleague's recipe.** The recipe is another
  contributor's; the *sign-off* is the author's. Every defect named here is in
  the author's own review, not in the contributor's code, and B09 makes the
  positive case explicitly. The handoff's new line — "make its gate tests real"
  — is recorded as a request to the recipe's author, not an edit.
- **Sounding like the promotion was wrong.** B09 is the counterweight: live
  stays blocked, the version is frozen so the evidence binds to the reviewed
  text, and the promotion replaced its own open item with a sharper one.
- **Overclaiming the fourth gate.** B06 is reproduced standalone with the
  script deleted and every real TODO removed, and FACTCHECK.md records the
  exact occurrence counts (9 total, 6 marked Closed, 1 the gate itself).

## Read-only discipline

Nothing in this build wrote to `D:\Projects\mycroft`. `snickerdoodle gate`,
`snickerdoodle run` and the conformance pass were all left unrun — which is why
every gate was reproduced by shape in a scratch folder rather than executed in
place. SOURCES.md records that trade.

## Notes

- **ILLUSTRATE LAW**: Claude UI only in B00, B03, B04, B10, B11.
- **B05's panel lines are capped at ~20 characters** so the three-across row
  stays near 11.5 units wide and `fit_src()` scales it up rather than down.
- **Every Manim beat lands its citation strip by ~45%** of its runtime, so the
  midpoint QC frame has content down to the bottom of the safe area.

## GATE V, as measured on the clean master

`BLOCKER: 0 · MAJOR: 2`, both on B11 — the library `ClaudeTitleOutro` card,
sparse by design, the same accepted bookend state as episodes 12 and 13.

**GATE B caught one real defect before any frame was slotted.** B09's closing
line was positioned with `to_edge(DOWN, buff=2.30)` instead of being composed
into the fitted group, which put it inside the body band and on top of the third
panel — a 100% text-on-text overlap. That is a rule this series already had
written down ("compose every label INTO the fitted group before fitting"), and
the gate caught the author breaking it. Fixed by adding the line to the `VGroup`
before `fit_src()`; the other six Manim beats were untouched and stayed slotted.

Motion histogram on the master: fade 4, build 3, reveal 3, resolve 2 — `fade` at
33%, under the cap.
