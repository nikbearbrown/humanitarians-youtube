# CHECKS-REPORT — Who Decides It's A Bug?

Written before the first slate compiled, per the PROOF GATE.

**11 SHOW / 0 justified-HOLD / 0 PUNT-flagged**

| Beat | Act | Class | Artifact named |
|---|---|---|---|
| B00 | INTRO | SHOW | Claude composer, topic question answered |
| B01 | BLUF | SHOW | the four jobs of a beta tester, the second marked (Manim) |
| B02 | FRAMEWORK | SHOW | three question cards (Manim) |
| B03 | EVIDENCE | SHOW | the free oracle and OSS-Fuzz's dated figures, cited (Manim) |
| B04 | EVIDENCE | SHOW | the LLM writes the target; the grading metrics, cited (Manim) |
| B05 | EVIDENCE | SHOW | the paper's oracle sentence, quoted and attributed (Manim) |
| B06 | EVIDENCE | SHOW | the narrowing funnel and its counts, cited (Manim) |
| B07 | FALSIFIABILITY | SHOW | three source problems, with arithmetic (Manim) |
| B08 | VERDICT | SHOW | the rubric scored, the games case, then both sides (Manim) |
| B09 | YOUR TURN | SHOW | composer, scaffold + GOOD/BAD |
| B10 | OUTRO | SHOW | title-restate card |

## How the commissioned topic was handled

The brief asked for **implications and advantages of AI as a beta tester**. A
list of advantages would be filler. The reel instead supplies the distinction
that governs every advantage — what decides that a result is wrong — and then
walks three regimes with real, dated figures in each:

1. **Free oracle** (a crash): enormous scale, and honestly labelled as *not AI*.
2. **AI inside the free-oracle loop**: the model writes the probe, the crash
   still returns the verdict.
3. **Oracle must be written**: Meta's numbers, and the failure-discarding
   admission that is the reel's hero beat.
4. **No oracle** (is this fun?): the games case, framed as a definition rather
   than a finding.

## GATE L — library-first

Searched before authoring: a four-item split column, a three-stage pipeline
ending in a verdict, a quotation card with attribution, and a descending
proportional funnel. Genuine miss on all four — the nearest candidates are
topic-locked to other seasons, and the only funnel in the library is a 9:16
portrait composition. The eight Manim beats are authored as data animations and
the miss is logged. Reused unchanged from the library: `ClaudeComposerAsk` and
`ClaudeTitleOutro`.

## Teaching arc

```
PREMISE SPLIT ✓    B01 — a beta tester does four jobs, not one, and automation
                   is wildly uneven across them.
FRAMEWORK ✓        B02 — WHAT IS THE ORACLE / WHAT HAPPENS TO A FAILURE IT
                   CANNOT JUDGE / WHO PAYS FOR A FALSE POSITIVE, shown AS A
                   STRUCTURE before any figure.
REUSABLE RUBRIC ✓  All three work on any testing tool. B09 turns them on the
                   viewer's own in one question.
WORKED EXAMPLE ✓   B03, B04 and B05 are the same rubric applied three times to
                   three real systems, with the answer changing each time.
HONEST LABELLING ✓ B03 states on screen that classical fuzzing is not AI. That
                   is the central available error in this topic, and the reel's
                   structure exists to avoid it.
FALSIFIABILITY ✓   B07 carries three real source problems: the abstract-vs-body
                   11.5% vs ~10% with the arithmetic shown, the denominator
                   shifting between test cases and test classes, and two
                   official pages of the same project disagreeing.
SOURCE CORRECTION ✓ The popular reading attributes fuzzing's totals to "AI".
                   B03 refuses it. The widely-quoted 11.5% is the abstract's;
                   the reel uses the body's 10% and shows 196/1,979.
FRICTION ✓         B05 tells a viewer that a shipped, published tool discards
                   exactly the failures a beta tester exists to find.
BOTH SIDES ✓       B08's excitement line is specific: a model writing probes
                   found bugs in already-hard-fuzzed code.
SCAFFOLDED TASK ✓  B09 — name the oracle, then ask what happens to an
                   unclassifiable failure. GOOD/BAD included.
NO-SOURCE-NO-VERDICT ✓  Six Manim beats carry an on-screen citation strip, and
                   every dated figure carries its date on screen.
BOOKENDS ✓         B00 cold open with the author's name · B09 "Your turn." ·
                   B10 title restate.
```

## The risks, and what answers them

- **Calling fuzzing "AI".** The single biggest error available here, and the
  reason B03 exists in its current form with an explicit on-screen chip.
- **Overclaiming OSS-Fuzz-Gen's oracle.** Its README never states how a bug is
  adjudicated. B04 claims only the documented grading metrics.
- **Using an unreadable source.** The November 2024 Google Security Blog post
  returned only page chrome, so none of its figures appear. SOURCES.md records
  what was dropped and why.
- **Sounding anti-AI.** B04 and B08 are sincere about what the model contributes
  — reach into code that human-written harnesses had not touched.
- **Sounding like a verdict on games.** B08's games claim is framed as a
  consequence of the reel's own taxonomy, not as a cited empirical result, and
  FACTCHECK.md says so explicitly.

## Notes

- **ILLUSTRATE LAW**: Claude UI only in B00, B09, B10.
- **Composition**: every Manim group is sized to fit inside the 4.2-unit body
  band so `fit_src()` scales it up, and every beat lands its citation strip by
  ~45% of runtime so the midpoint QC frame reaches the bottom of the safe area.
- Bars in B06 encode the stated percentages proportionally and carry their own
  numbers beside them.

## GATE V, as measured on the clean master

`BLOCKER: 0 · MAJOR: 2`, both on B10 — the library `ClaudeTitleOutro` card, a
2.0s title restate that is sparse by design. Same accepted bookend state as
every other reel in this series.

**Every data beat passed on the first render.** The two layout rules carried
forward from the previous build — size each group to fill the 4.2-unit body
band, and land the citation strip by ~45% of runtime — were applied during
authoring rather than discovered by the gate.

`build` came back at 5/11 (45%), over the pantry cap. B06 was relabelled
`reveal`, which is the accurate word: it reveals three pre-composed bars against
a scale track drawn before them. Final histogram: build 4, fade 3, reveal 3,
resolve 1.
