# CHECKS-REPORT.md — why-agents-fail

Written before the first slate compile, per PROOF GATE (ai-explainer SKILL.md).

## Per-beat classification (SHOW / HOLD / CARD — nopunt SKILL.md)

| Beat | Class | Scene / pattern | Reason |
|------|-------|------------------|--------|
| B00 | SHOW | ClaudeComposerAsk (Remotion) | Cold-open bookend; the UI is the subject |
| B01 | SHOW | B01_FourFailures (Manim) | Names a set of N things — nopunt "panel of N things" row |
| B02 | SHOW | B02_InfiniteLoop (Manim) | Names a cycle that fails to terminate — animated loop diagram |
| B03 | SHOW | B03_ContextDrift (Manim) | Names a container filling and displacing its contents — animated mechanism |
| B04 | SHOW | B04_HallucinatedArgs (Manim) | Names a schema/form mismatch — nopunt "schema validation → show the real artifact" row |
| B05 | SHOW | B05_ConfidentlyWrong (Manim) | Names a comparison held side by side — nopunt "two things compared, two-up aligned" row |
| B06 | SHOW | B06_TwelveAttempts (Manim) | Names an ordered trace with a climbing counter — nopunt "itemized list with running total" row |
| B07 | SHOW | ClaudeVerdictArtifact (Remotion) | Verdict bookend; recaps, asserts nothing new |
| B08 | SHOW | ClaudeComposerAsk (Remotion) | Handoff bookend; prompt typed, read aloud, discussed with rubric |
| B09 | SHOW | ClaudeTitleOutro (Remotion) | Outro bookend; title restate |

**10 SHOW / 0 HOLD / 0 PUNT**

No beat requires an archival photograph — the only legitimate HOLD. Every
claim is a cycle, a mechanism, a schema, a comparison, or an itemized trace,
all of which appear in the nopunt catalog and are therefore animatable.

**Punt costumes explicitly avoided:** the source script's scrolling-terminal
title card and its checkmarked end card were rebuilt into real beats rather
than carried as stills. No gen-AI clip, no archive still, no unfilled
pipeline slate, no FormA card whose narration names a visual.

## Whole-sheet teaching-arc checklist

- [x] **FRAMEWORK beat** — B01 puts all four failure modes on screen as named
  empty panels **before** mode 1 is described. B02–B05 fill them one at a
  time; the legend persists so the viewer always knows which is being filled.
- [x] **WORKED EXAMPLE** — B06 walks the twelve-attempt deploy start to
  finish with the four-mode legend on screen, and lights each mode's tick as
  that mode fires in the trace. The example visibly *uses* the framework
  rather than sitting adjacent to it.
- [x] **FALSIFIABILITY / edge-case beat** — B05 is the dedicated stress test,
  and it stress-tests observation itself: the reel's own subject matter is
  shown to be undetectable by the obvious method (reading what the agent
  reports). This is the beat that forces every B07 guardrail to be an
  *external* check rather than better prompting. A full beat with its own
  two-up comparison and bracketed gap, not a caveat in passing.
- [x] **SCAFFOLDED viewer task** — B08 ships a real prompt ("Take an agent
  workflow I rely on and find where it can fail silently") plus a 3-item
  rubric: names a turn limit / names a verifier checking the real result /
  names a human gate on the irreversible step. It also names a **failing**
  answer to reject ("write a better prompt"), which is a rubric with teeth.
- [x] **Four bookends** — B00 (cold open), B07 (verdict), B08 (Your Turn),
  B09 (title-restate outro).
- [x] **No source, no verdict** — every claim-bearing beat carries its
  artifact on screen: the four panels (B01), the accelerating ring and
  counter (B02), the packed window and displaced goal (B03), the schema card
  with the unmatched field (B04), the ten-line log beside the success card
  (B05), the twelve-step trace (B06). B07 and B08 are exempt (they
  recapitulate).

**Teaching arc: FRAMEWORK ✓ | WORKED EXAMPLE ✓ | FALSIFIABILITY ✓ |
SCAFFOLDED TASK ✓ | BOOKENDS ✓ | NO-SOURCE-NO-VERDICT ✓**

## Slate rules audit (Step 4b, automated)

`runtime/qc/sheet_check.py` — **clean, 10 beats, no findings**, including
under `--strict`. Every non-wrapping field is inside its hard limit and every
wrapping field is inside its *recommended* count.

## Legibility contract (per beat)

Every SHOW beat names its on-screen artifact and every Manim beat carries an
ordered `show` block. Scenes hold ~15–35% negative space; un-highlighted
elements stay at INK/SOFT and are never dropped below GHOST. B05's two
columns hold simultaneously for the full comparison, and B06's four-mode
legend stays on screen for the entire trace so the mapping is always visible.

## PPT test

No beat is a headline over a paragraph. Motion enacts the sentence in every
body beat: the ring accelerating as the counter climbs (B02), blocks packing
in and shoving the goal to the edge (B03), a form filling clean field by
field before one is ringed and dropped to a schema with no match (B04), a log
column stacking while the summary column stays calm (B05), a trace building
step by step then compressing into a block that buries the original
instruction (B06).

## Status

Beat sheet, gate docs, and `scenes.py` are authored and internally
consistent. This pass closes the PROOF GATE for authoring.

**Blocked on:** GATE P signature in `PEDAGOGY.md` (currently `VERDICT:
PENDING`). No audio may be generated until a human signs it.
