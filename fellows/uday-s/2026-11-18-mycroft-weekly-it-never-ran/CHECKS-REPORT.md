# CHECKS-REPORT — It Never Ran

Written before the first slate compiled, per the PROOF GATE.

**12 SHOW / 0 justified-HOLD / 0 PUNT-flagged**

| Beat | Act | Class | Artifact named |
|---|---|---|---|
| B00 | INTRO | SHOW | Claude composer, the week's ask answered |
| B01 | PROBLEM | SHOW | the two loader calls and the identical output (Manim) |
| B02 | FRAMEWORK | SHOW | three question cards (Manim) |
| B03 | CLI | SHOW | composer, the instrumentation ask |
| B04 | CODE | SHOW | the runner construction, verbatim from `08b92d3^` |
| B05 | OUTPUT | SHOW | three mechanisms with their real output (Manim) |
| B06 | OUTPUT | SHOW | the throw/catch/fallback flow and the introducing date (Manim) |
| B07 | OUTPUT | SHOW | 4 lines, one author; what was left alone (Manim) |
| B08 | FALSIFIABILITY | SHOW | what reproduced, and the totals that did not (Manim) |
| B09 | SUMMARY | SHOW | 8 added, 2 excluded with reasons, the untested version (Manim) |
| B10 | NEXT STEPS | SHOW | composer, scaffold + GOOD/BAD |
| B11 | OUTRO | SHOW | title-restate card |

## GATE L — library-first

Searched before authoring: `./art scenes` for a before/after code-call pair, a
vertical failure-cascade flow, a verified/unverified recount comparison, and a
stacked three-panel interpreter-output card. Genuine miss on all four; the seven
Manim beats are authored as data animations and the miss is logged.

Reused from the library without change: `ClaudeComposerAsk`, `ClaudeCodeBeat`,
`ClaudeTitleOutro`.

## Teaching arc

```
PREMISE ✓          B01 — the fix changed nothing, and that is the finding, not
                   a disappointment. Continues episode 12 directly.
FRAMEWORK ✓        B02 — DID THE FIX CHANGE ANYTHING / WHAT DOES THE FALLBACK
                   HIDE / WOULD IT PASS ON NOTHING, shown AS A STRUCTURE
                   before any evidence.
REUSABLE RUBRIC ✓  All three work on any check in any project. B10 turns them
                   on the viewer's own as a one-run experiment.
WORKED EXAMPLE ✓   B04 shows the actual line; B05 reproduces all three
                   mechanisms it causes; B06 answers question 2 concretely.
FALSIFIABILITY ✓   B08 — three things reproduced, one pair of figures that did
                   not, shown side by side with the discrepancy named and the
                   likely cause stated. The totals are attributed, not claimed.
SELF-IMPLICATION ✓ B06 and B07 — the broken line is the author's own, from the
                   commit this series already made an episode about.
SCAFFOLDED TASK ✓  B10 — break the fast path, see if anything says so.
                   GOOD/BAD discriminator included.
FRICTION ✓         B05 panel 3 tells a viewer that the obvious fix for this
                   class of bug has a silent-pass trap in it.
HONEST LIMIT ✓     B09 closes on what was NOT tested — the Python version CI
                   uses — because the commit itself records it.
NO-SOURCE-NO-VERDICT ✓  Six Manim beats carry an on-screen citation strip.
BOOKENDS ✓         B00 cold open with the author's name · B10 "Your turn." ·
                   B11 title restate.
```

## The risk, and what answers it

- **Sounding like a confession.** B07 is the counterweight: the discipline shown
  there — fix your own four lines, leave the other contributor's correct code
  alone — is the transferable part, and it is a positive practice, not an
  apology.
- **Overclaiming the file counts.** B08 exists precisely to prevent it. Both
  pairs are on screen with a label saying which is which.

## Read-only discipline

Nothing in this build wrote to `D:\Projects\mycroft`. `snickerdoodle gate` and
`conformance.mjs` were both left unrun for that reason, and FACTCHECK.md records
what that cost: one pair of figures that had to be attributed rather than
reproduced.

## Notes

- **ILLUSTRATE LAW**: Claude UI only in B00, B03, B04, B10, B11.
- **Composition**: every Manim beat stacked except B02, whose cards are tall.
- **B04 motion is `reveal`**, not `fade` — accurate, and keeps the reel under
  the fade cap.

## GATE V, as measured on the clean master

`BLOCKER: 0 · MAJOR: 2`, both on B11 — the library `ClaudeTitleOutro` card,
sparse by design, the same accepted bookend state as episode 12.

One defect the gate did **not** catch was found by looking at the frames, which
is why that step exists: B05 and B06 were being scaled to ~46% by `fit_src()`,
because each stacked group was about 9 units tall against the 4.2-unit body band
the citation strip leaves. They passed the gate only because its `cover` metric
is a bounding box, and the kicker rule spans the full width regardless.

B05 is now a row of three panels, and B06's four cascade steps are single-line
chips. Both fill the frame and both are legible at size. The rule — keep the
group inside the band so `fit_src()` scales it **up** — is written into the
scenes.py header.
