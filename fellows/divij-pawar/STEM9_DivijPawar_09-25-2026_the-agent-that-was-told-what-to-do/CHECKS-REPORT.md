# CHECKS-REPORT.md — the-agent-that-was-told-what-to-do

Written before the first slate compile, per PROOF GATE (ai-explainer
SKILL.md). This reel is **11 beats (B00-B10)**, one more than the
ai-explainer default of 10 — see "Beat-count rationale" below.

## Per-beat classification (SHOW / HOLD / PUNT — nopunt SKILL.md)

| Beat | Class | Scene / pattern | Reason |
|------|-------|------------------|--------|
| B00 | SHOW | ClaudeComposerAsk (Remotion) | Cold-open bookend; the UI is the subject |
| B01 | SHOW | B01_DataAndInstructions (Manim) | Names the token-level mechanism as a real diagram (a text stream, then a wall drawn and struck) — nopunt "assumed boundary shown not to exist" row |
| B02 | SHOW | B02_WorkedExample (Manim) | Names a hidden-instruction mechanism with a real worked artifact (an email, a zoom into faint text) — nopunt "hidden detail resolved into legibility" row |
| B03 | SHOW | B03_NotTheAutonomyQuestion (Manim) | Names a distinction as a physical diagram (two doors, hand on near vs. far side) — nopunt "two things compared, same shape different origin" row |
| B04 | SHOW | B04_LockTheInstructions (Manim) | Names a mitigation and its limit in one diagram (a locked box, a competing instruction beside it) — nopunt "a boundary drawn, then shown incomplete" row |
| B05 | SHOW | B05_CrossExaminationHole (Manim) | Names a callback mitigation and its hole by reprising STEM6's own nameplate diagram — nopunt "structural blind spot shown, not just asserted" row |
| B06 | SHOW | B06_ApprovalRealLimit (Manim) | Names a mitigation's real limit via two contrasted versions of the same screen — nopunt "two things compared, side by side" row |
| B07 | SHOW | B07_SittingWithIt (Manim) | Names the episode's own honesty beat via a real diagram (the cold-open recipe blog, flickering outlines) rather than a narrated conclusion — nopunt "claim shown, not just stated" row |
| B08 | SHOW | ClaudeVerdictArtifact (Remotion) | Verdict bookend; recaps, preserves "unsolved" framing |
| B09 | SHOW | ClaudeComposerAsk (Remotion) | Handoff bookend; prompt typed, read aloud, discussed with a 2-question scaffold |
| B10 | SHOW | ClaudeTitleOutro (Remotion) | Outro bookend; title restate + series-reflective close |

**11 SHOW / 0 HOLD / 0 PUNT**

No beat requires an archival photograph. Every claim in this script is a
general structural fact about LLM-based agents, all animatable as
diagrams rather than stand-ins.

**Punt costumes explicitly avoided:** the source script's recipe-blog
title card and its "hidden instruction" reveal are rebuilt as real
diagram beats (B02's zoom-in, B07's flickering outlines) rather than
carried as a literal screenshot mockup. No gen-AI clip, no stock icon of
a hacker or a lock, no unfilled pipeline slate.

## Beat-count rationale (11, not 10)

The source script's "Mitigations" section names three distinct
mechanisms (lock instructions, cross-examine, human approval), each with
its own honest limit stated in the same paragraph. Crowding all three
into one beat would either cut two of the three limits or stack three
diagrams into one hold — per `youtube/CLAUDE.md` §4's "one idea per beat"
rule, each got its own beat (B04/B05/B06) instead, the same reasoning
STEM6 applied to its own two-part "Arbitration Step."

## Whole-sheet teaching-arc checklist

- [x] **FRAMEWORK beat** — B01 states the token-level mechanism (no
  channel separation between instructions and data) **before** the
  worked example or any mitigation is introduced.
- [x] **WORKED EXAMPLE** — B02 walks one concrete scenario (hidden
  white-on-white forwarding instruction in an email) live, not just
  referenced.
- [x] **FALSIFIABILITY** — this episode is unusual in stress-testing
  *itself* continuously rather than in one dedicated beat: B04, B05, and
  B06 each state their own mitigation's limit in the same beat that
  introduces it, and B07 states plainly that none of the three closes
  the gap. B05 specifically reprises STEM6's already-verified
  shared-contamination blind spot as a direct callback.
- [x] **SCAFFOLDED viewer task** — B09 ships a real, ordered 2-question
  task: would your own system notice a hidden instruction in content it
  reads, and does your approval screen surface every side-effect.
- [x] **Four bookends** — B00 (cold open), B08 (verdict), B09 (your
  turn), B10 (title-restate outro, series-reflective since this is the
  currently-final episode).
- [x] **No source, no verdict** — every claim-bearing beat carries its
  own on-screen artifact: the struck wall (B01), the resolved hidden text
  (B02), the two doors (B03), the locked box beside a competing
  instruction (B04), the agreeing nameplates and dark arbitration node
  (B05), the two contrasted approval screens (B06), the flickering
  recipe-blog paragraphs (B07).

**Teaching arc: FRAMEWORK ✓ | WORKED EXAMPLE ✓ | FALSIFIABILITY ✓ |
SCAFFOLDED TASK ✓ | BOOKENDS ✓ | NO-SOURCE-NO-VERDICT ✓**

## Slate rules audit (Step 4b, automated)

Not yet run against `runtime/qc/sheet_check.py` — see BUILD-PROMPT.md
Step 1. All `ClaudeComposerAsk` (B00, B09) and `ClaudeVerdictArtifact`
(B08) / `ClaudeTitleOutro` (B10) props were hand-checked against the
hard-limit table in `agents.md` Step 4 during authoring:

| Beat | Field | Length | Limit | OK? |
|---|---|---|---|---|
| B00 | `topic` | 16 chars ("PROMPT INJECTION") | 125 hard | yes |
| B00 | `greeting` | matches `metadata.greeting` ("Olá, Divij") | 55 hard | yes |
| B00/B09 | `command` | single-line, well under 100 chars | wraps, not hard | yes |
| B08 | `artifactLines[]` | each line under 95 chars | wraps, not hard | yes |
| B10 | `title` | "The Agent That Was Told What To Do", 35 chars | wraps, not hard | yes |

## Status

Beat sheet, gate docs, and `scenes.py` are authored and internally
consistent — every `shot.manim.scene_class` in `beat_sheet.json` names
exactly `B01`-`B07` (`B01_DataAndInstructions` through
`B07_SittingWithIt`), matching the seven Manim beats above. `scenes.py`
has been smoke-tested at low quality (`-ql`, per-scene) and visually
QC'd via contact sheets before any 4K render or audio generation — see
"Real defects found" below.

**GATE P: PENDING.** No audio has been generated and no build has been
attempted. `PEDAGOGY.md` must read `VERDICT: PASS`, signed by a human,
before `generate_audio_kokoro.py` runs.

## Post-audio retiming (Step 3)

Not yet run — no real Kokoro audio exists.

## Real defects found in low-quality smoke-test QC

None. All three known defect classes from prior episodes (title collision
with persistent-title captions; same-position crossfade of two different
strings; Montserrat's missing ✓ glyph via `label()`) were designed out
from the start — B05's agreement checkmarks use raw `Text("✓", ...)`
rather than `label("✓", ...)`, every caption swap uses `FadeOut` fully
before `FadeIn`, and nothing sits above ~y=1.6 once a title is on screen.
Contact sheets were pulled for all 7 scenes (4x3 grid per scene, sampled
across each clip's full duration) and read clean on the first pass — no
overlaps, no off-canvas elements, no illegible transitions, no tofu-box
glyphs.

A full mid-scene/frame pass against real 4K renders still happens after
GATE P clears and Step 3 retiming runs — this smoke-test pass is at
360p/15fps pre-audio timing, not a substitute for that.

## 9:16 short — beat selection

Not yet planned — the 16:9 master must be built and QC'd first.

## Final status

Not built. See PEDAGOGY.md for the pending GATE P sign-off required
before `generate_audio_kokoro.py` runs, and BUILD-PROMPT.md for the full
pipeline.
