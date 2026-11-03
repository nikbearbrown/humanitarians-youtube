# CHECKS-REPORT.md — grading-the-machine

Written before the first slate compile, per PROOF GATE (ai-explainer
SKILL.md). This reel is **10 beats (B00-B09)**.

## Per-beat classification (SHOW / HOLD / PUNT — nopunt SKILL.md)

| Beat | Class | Scene / pattern | Reason |
|------|-------|------------------|--------|
| B00 | SHOW | ClaudeComposerAsk (Remotion) | Cold-open bookend; the UI is the subject |
| B01 | SHOW | B01_SelfReportedConfidence (Manim) | Names a self-grading mechanism as a real diagram (one box producing both answer and score) — nopunt "one source produces two outputs treated as independent" row |
| B02 | SHOW | B02_LLMAsJudge (Manim) | Names a category error as an on-screen correction (a stamp struck by another stamp) — nopunt "claim visibly corrected" row |
| B03 | SHOW | B03_ComputedNotReported (Manim) | Names an arithmetic mechanism with real itemized deductions — nopunt "itemized ledger, plain subtraction" row |
| B04 | SHOW | B04_NeverSuppress (Manim) | Names a branching design choice — nopunt "one process, two named outcomes" row |
| B05 | SHOW | B05_StillALiveRisk (Manim) | Names the falsifiability turn by re-flagging the same ledger from B03 as uncalibrated — nopunt "claim visibly corrected/annotated" row |
| B06 | SHOW | B06_TheFramework (Manim) | Names a three-way comparison — nopunt "panel/list of N things" row |
| B07 | SHOW | ClaudeVerdictArtifact (Remotion) | Verdict bookend; recaps, asserts nothing new |
| B08 | SHOW | ClaudeComposerAsk (Remotion) | Handoff bookend; prompt typed, read aloud, discussed with a 3-step scaffold |
| B09 | SHOW | ClaudeTitleOutro (Remotion) | Outro bookend; title restate + bridge to STEM9 |

**10 SHOW / 0 HOLD / 0 PUNT**

No beat requires an archival photograph. Every claim in this script is a
general design pattern (self-report, LLM-judge, computed scoring), all
animatable as diagrams rather than stand-ins.

**Punt costumes explicitly avoided:** the source script's report-card
title stamp and end-card panel stack are rebuilt into real diagram beats
rather than carried as a literal report-card illustration. No gen-AI
clip, no stock icon, no unfilled pipeline slate.

## Whole-sheet teaching-arc checklist

- [x] **FRAMEWORK beat** — B00 poses the episode's organizing question
  (who grades the grader, and can they be trusted) before either bad
  idea is examined; B03 states the mechanism that actually holds up
  before B06 collapses everything into a transferable rubric.
- [x] **WORKED EXAMPLE** — the arithmetic ledger (base 1.0, two -0.1
  deductions, final 0.8) is introduced in B03 and revisited in B05 with
  its constants flagged uncalibrated — one continuous worked example
  carrying two beats, not two disconnected illustrations.
- [x] **FALSIFIABILITY / edge-case beat** — B05 is the dedicated stress
  test, and it stress-tests the episode's *own* proposed fix: computed
  scoring is inspectable, but its specific constants are still
  first-principles guesses. B06's framework says "still being
  calibrated," not "solved."
- [x] **SCAFFOLDED viewer task** — B08 ships a real, ordered 3-step task:
  identify which of the three scoring categories your own system's
  confidence score falls into, then sketch a computed alternative.
- [x] **Four bookends** — B00 (cold open), B07 (verdict), B08 (your
  turn), B09 (title-restate outro, bridging to STEM9).
- [x] **No source, no verdict** — every claim-bearing beat carries its
  own on-screen artifact: the self-grading loop (B01), the struck
  "PLAUSIBLE" stamp (B02), the itemized ledger (B03), the branching
  hide/flag paths (B04), the re-flagged ledger (B05), the three-panel
  comparison (B06).

**Teaching arc: FRAMEWORK ✓ | WORKED EXAMPLE ✓ | FALSIFIABILITY ✓ |
SCAFFOLDED TASK ✓ | BOOKENDS ✓ | NO-SOURCE-NO-VERDICT ✓**

## Slate rules audit (Step 4b, automated)

Not yet run against `runtime/qc/sheet_check.py` — see BUILD-PROMPT.md
Step 1. All `ClaudeComposerAsk` (B00, B08) and `ClaudeVerdictArtifact`
(B07) / `ClaudeTitleOutro` (B09) props were hand-checked against the
hard-limit table in `agents.md` Step 4 during authoring:

| Beat | Field | Length | Limit | OK? |
|---|---|---|---|---|
| B00 | `topic` | 21 chars ("GRADING AI CONFIDENCE") | 125 hard | yes |
| B00 | `greeting` | matches `metadata.greeting` ("Olá, Divij") | 55 hard | yes |
| B00/B08 | `command` | single-line, well under 100 chars | wraps, not hard | yes |
| B07 | `artifactLines[]` | each line under 95 chars | wraps, not hard | yes |
| B09 | `title` | "Grading the Machine", 20 chars | wraps, not hard | yes |

## Status

Beat sheet, gate docs, and `scenes.py` are authored and internally
consistent — every `shot.manim.scene_class` in `beat_sheet.json` names
exactly `B01`-`B06` (`B01_SelfReportedConfidence` through
`B06_TheFramework`), matching the six Manim beats above. `scenes.py` has
been smoke-tested at low quality (`-ql`, per-scene) and visually QC'd via
contact sheets before any 4K render or audio generation — see "Real
defects found" below.

**GATE P: PENDING.** No audio has been generated and no build has been
attempted. `PEDAGOGY.md` must read `VERDICT: PASS`, signed by a human,
before `generate_audio_kokoro.py` runs.

## Post-audio retiming (Step 3)

Not yet run — no real Kokoro audio exists. All `self.wait()` calls in
`scenes.py` are currently timed against `estimated_duration_s` only.

## Real defects found in low-quality smoke-test QC

None. Both known defect classes from STEM6/STEM7 (title collision with
persistent-title captions; same-position crossfade of two different
strings) were designed out from the start here — every caption swap uses
`FadeOut` fully before `FadeIn`, and nothing is placed above ~y=1.5 once
a title is on screen. Contact sheets were pulled for all 6 scenes (4x3
grid per scene, sampled across each clip's full duration) and read
clean on the first pass — no overlaps, no off-canvas elements, no
illegible transitions. B02's "CATEGORY ERROR" stamp visibly overlapping
"PLAUSIBLE ✓" is intentional (a held static frame enacting the sentence
"a stamp slams down across it"), not a transitional collision.

A full mid-scene/frame pass against real 4K renders still happens after
GATE P clears and Step 3 retiming runs — this smoke-test pass is at
360p/15fps pre-audio timing, not a substitute for that.

## 9:16 short — beat selection

Not yet planned — the 16:9 master must be built and QC'd first.

## Final status

Not built. See PEDAGOGY.md for the pending GATE P sign-off required
before `generate_audio_kokoro.py` runs, and BUILD-PROMPT.md for the full
pipeline.
