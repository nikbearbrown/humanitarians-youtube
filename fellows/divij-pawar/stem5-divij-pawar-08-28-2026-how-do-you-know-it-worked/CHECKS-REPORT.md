# CHECKS-REPORT.md — how-do-you-know-it-worked

Written before the first slate compile, per PROOF GATE (ai-explainer
SKILL.md). This reel is **13 beats (B00-B12)**, not the ai-explainer
default of 10 — see "Beat-count deviation" below.

## Per-beat classification (SHOW / HOLD / PUNT — nopunt SKILL.md)

| Beat | Class | Scene / pattern | Reason |
|------|-------|------------------|--------|
| B00 | SHOW | ClaudeComposerAsk (Remotion) | Cold-open bookend; the UI is the subject |
| B01 | SHOW | B01_TheTrustProblem (Manim) | Names the reasoning-vs-narration gap as a real diagram (two boxes, a dotted assumption, a struck thesis) — nopunt "two things compared" row |
| B02 | SHOW | B02_ClaimExtraction (Manim) | Names a parsing mechanism with a named taxonomy — nopunt "wall of text mechanically sorted into N labeled categories" row |
| B03 | SHOW | B03_VerifyAgainstReality (Manim) | Names a fetch-and-check mechanism with a real tri-state outcome — nopunt "external fetch resolves to a named state" row |
| B04 | SHOW | B04_VerificationRollup (Manim) | Names an aggregation (many outcomes to one rate) plus a real, previously-unstated precision gap — nopunt "itemized outcomes roll up to one number" row |
| B05 | SHOW | B05_AskTwice (Manim) | Names a duplication-and-compare mechanism — nopunt "one input forks into two parallel processes" row |
| B06 | SHOW | B06_ConsistencyFlag (Manim) | Names a scoring/classification mechanism with a concrete pass/fail pair — nopunt "two worked instances, one passes one fails" row |
| B07 | SHOW | B07_ProofToEvidence (Manim) | Names the falsifiability turn as an on-screen correction (word struck, replaced) — nopunt "claim visibly corrected" row |
| B08 | SHOW | B08_GoodAtCatching (Manim) | Names a two-column boundary (strong direction vs. hard limit) — nopunt "two things compared, two-up aligned" row |
| B09 | SHOW | B09_TheFramework (Manim) | Names a set of N transferable rules — nopunt "panel/list of N things" row |
| B10 | SHOW | ClaudeVerdictArtifact (Remotion) | Verdict bookend; recaps, asserts nothing new |
| B11 | SHOW | ClaudeComposerAsk (Remotion) | Handoff bookend; prompt typed, read aloud, discussed with a 3-step scaffold |
| B12 | SHOW | ClaudeTitleOutro (Remotion) | Outro bookend; title restate + bridge to STEM6 |

**13 SHOW / 0 HOLD / 0 PUNT**

No beat requires an archival photograph — the only legitimate HOLD in this
catalog. Every claim in this script is a real mechanism in this project's
own code (a parser, a fetch-and-compare, a duplicate-and-score), all of
which are animatable diagrams, not stand-ins.

**Punt costumes explicitly avoided:** the source script's magnifying-glass
title card and its green-checkmark end card are rebuilt into real
diagram beats rather than carried as stills or a literal color scheme that
would violate the house palette. No gen-AI clip, no stock icon, no
unfilled pipeline slate, no card whose narration names a visual that isn't
actually on screen.

## Beat-count deviation (13, not 10)

`agents.md`'s Quick Start default is a fixed 10-beat B00-B09 structure.
This reel authored 13 (B00-B12) because the source script's three
mechanism sections and its "what this doesn't prove" section each carry
enough independent content to need their own on-screen artifact:

- **Mechanism 2 (verification)** splits into B03 (the fetch + tri-state
  outcome) and B04 (the rollup rate + the honest pooling caveat) — forcing
  both into one beat would either cut the caveat (the reel's most
  evidence-driven addition) or crowd two distinct diagrams into one hold.
- **Mechanism 3 (consistency probing)** splits into B05 (the setup: fork,
  weighting) and B06 (the resolution: two worked outcomes, one flagged) —
  same reasoning; the "ask twice" setup and the "classify and flag" payoff
  are each their own idea.
- **"What this doesn't prove"** splits into B07 (PROOF struck to EVIDENCE)
  and B08 (the two-column good-at/cannot-prove card) — this is the reel's
  designated falsifiability beat and it gets two full holds rather than
  one crowded one, per `youtube/CLAUDE.md` §4 ("give the falsifiability
  beat its own moment").
- **B09 and B10 both carry "the framework"** deliberately, in two
  registers: B09 is the Manim beat that states the three rules live (with
  icons); B10 is the Remotion verdict-card recap. This mirrors STEM2,
  which also carried its guardrails on both a body beat's content and a
  dedicated `ClaudeVerdictArtifact` recap.

This matches the reel's actual content mass rather than forcing a fixed
count — `youtube/CLAUDE.md`'s "one idea per beat" rule was prioritized over
matching STEM1-4's beat count exactly.

## Whole-sheet teaching-arc checklist

- [x] **FRAMEWORK beat** — B01 states the whole episode's thesis (the
  reasoning-vs-narration gap, "the log is evidence of output, not evidence
  of process") and previews all three mechanisms as named, empty panels
  **before** mechanism 1 is described. The three-mechanism legend then
  persists (ghosted/lit/active) across every mechanism beat through B09, so
  the viewer always knows which mechanism is being filled.
- [x] **WORKED EXAMPLE** — one real worked line ("Revenue grew 34% YoY,
  driven by international expansion — source: 10-K") is introduced in B02
  and walked live through B03/B04 (verified, rolled up with its own
  caveat) and B05/B06 (probed twice, then deliberately diverged against a
  fabricated "41%"). The example is used, not just referenced, across five
  consecutive beats — the framework is demonstrated on one continuous
  thread rather than three disconnected illustrations.
- [x] **FALSIFIABILITY / edge-case beat** — B07+B08 are the dedicated
  stress test, and they stress-test the reel's *own tools*: PROOF is
  visibly struck and replaced with EVIDENCE, then a two-column card states
  plainly what these mechanisms can never claim (correct causal reasoning,
  sound judgment) alongside what they're actually strong at (fabrication,
  drift, absent evidence). B04's mid-mechanism caveat (the pooling gap) is
  a second, code-level falsifiability moment inside the body itself, not
  just in the dedicated stress-test beats.
- [x] **SCAFFOLDED viewer task** — B11 ships a real, ordered 3-step task:
  tag a real reasoning trace by hand (citation / number / hedge / causal),
  pick one citation and actually check it against its real source, and —
  if there's no external source — run the same prompt twice and watch the
  numbers for drift. This is directly actionable against the viewer's own
  work, not "learn more."
- [x] **Four bookends** — B00 (cold open), B10 (verdict), B11 (your turn),
  B12 (title-restate outro, bridging to STEM6).
- [x] **No source, no verdict** — every claim-bearing beat carries its own
  on-screen artifact: the split-screen gap and struck thesis (B01), the
  shredder and tagged worked line (B02), the real `_close_enough` code and
  tri-state chips (B03), the pooled-numbers diagram and caveat (B04), the
  parallel-run setup (B05), the worked agreement/divergence pair (B06),
  the struck PROOF (B07), the two-column limits card (B08), the three
  numbered rules (B09).

**Teaching arc: FRAMEWORK ✓ | WORKED EXAMPLE ✓ | FALSIFIABILITY ✓ |
SCAFFOLDED TASK ✓ | BOOKENDS ✓ | NO-SOURCE-NO-VERDICT ✓**

## Slate rules audit (Step 4b, automated)

Not yet run against `runtime/qc/sheet_check.py` — see BUILD-PROMPT.md Step
1. All `ClaudeComposerAsk` (B00, B11) and `ClaudeVerdictArtifact` (B10) /
`ClaudeTitleOutro` (B12) props were hand-checked against the hard-limit
table in `agents.md` Step 4 during authoring:

| Beat | Field | Length | Limit | OK? |
|---|---|---|---|---|
| B00 | `topic` | 19 chars ("AGENT VERIFICATION"... — see beat_sheet.json for exact current value) | 125 hard | yes |
| B00 | `greeting` | matches `metadata.greeting` | 55 hard | yes |
| B00/B11 | `command` | single-line, well under 100 chars | wraps, not hard | yes |
| B10 | `artifactLines[]` | each line under 90 chars | wraps, not hard | yes |
| B12 | `title` | under 48 chars, clean 2-line wrap | wraps, not hard | yes |

Run `./art check` (or `sheet_check.py` directly) before rendering to get
the automated pass — this table is a manual pre-check, not a substitute.

## Legibility contract (per beat)

Every SHOW beat names its on-screen artifact and every Manim beat carries
an ordered `show` block in `beat_sheet.json`. Scenes hold ~15-35% negative
space; un-highlighted elements stay at INK/SOFT and are never dropped
below GHOST. B03's three outcome chips hold simultaneously for the full
comparison; B06's two worked examples (agree/diverge) are shown in
sequence, each held long enough to read before the next replaces it; B08's
two columns hold side by side for the full comparison.

## PPT test

No beat is a headline over a paragraph. Motion enacts the sentence in
every body beat: prose literally shredded into labeled cards (B02), a
citation card physically leaving the frame toward an external source
(B03), a pool of unrelated numbers converging on one citation to expose
the caveat (B04), one input forking into two parallel boxes (B05), two
conclusion pairs resolving in sequence — one calm, one ringed and flagged
(B06), a word struck through and replaced (B07), a divider splitting two
honestly-opposed columns (B08), three icons collecting a rule each (B09).

## Status

Beat sheet, gate docs, and `scenes.py` are authored and internally
consistent — verified by direct diff: every `shot.manim.scene_class` in
`beat_sheet.json` has exactly one matching `class` in `scenes.py`, no
extras, no gaps (`B01_TheTrustProblem` through `B09_TheFramework`). This
pass closes the PROOF GATE for authoring.

**GATE P signed 08/29/2026 — build completed end to end.** Full pipeline
run: Kokoro audio (13 beats, ground truth), retiming, Manim 4K render,
Remotion bookends, 4K compile, captions, `./art shorts` derivation. See
below for the real defects this pass caught and fixed — none were caught
by the mp4-probe/manifest check alone; all came from actually reading
extracted frames per §6 of the channel `CLAUDE.md`.

## Post-audio retiming (Step 3)

Every beat came in shorter than its pre-audio `estimated_duration_s`
(Kokoro reads faster than the ~2.5 words/sec planning assumption — same
direction of error as prior reels, opposite magnitude to STEM4's note that
scenes ran long). `self.wait()` calls were scaled per scene by
`(actual_duration_s - play_sum) / wait_sum`, computed from the beat's real
`play`/`wait` calls **including for-loop multiplicity** — the first
scaling pass under-counted loop bodies (a `self.wait()` inside a 3-4×
loop only appears once in source text), which put B01/B02/B03 several
seconds over their targets on the first re-render; corrected with a second
pass using the real measured `-ql` duration as ground truth. All 9 scenes
landed within 0.3s of `actual_duration_s` after correction.

## Real defects found in mid-scene/frame QC (not caught by any automated check)

1. **B01** — the dotted "assumed to be the same thing" connector was drawn
   between `box_l.get_right()`/`box_r.get_left()`, which sit at the boxes'
   vertical center — directly through the right box's confident-narration
   text. Same defect class as the channel `CLAUDE.md`'s documented
   `next_to()`-midpoint gotcha, different call. Fixed by anchoring the
   connector at a fixed y below both boxes' bottom edge.
2. **B02** — the shredder graphic was never faded out after use; it sat
   behind/through the four claim-type cards for the rest of the scene.
   Invisible in a final-frame check (the cards visually dominate by then),
   caught only by sampling mid-scene frames per §6. Fixed with an explicit
   `FadeOut(shredder)`.
3. **B03** — the `_close_enough(...)` code line was left on screen and
   collided with the `redflag`/`nojudge` captions once those landed near
   the same height below the three-outcome chip row. Fixed by including it
   in the chip-row transition's `FadeOut`.
4. **B09** — the scene never rendered a title at all (a real content gap
   against its own `beat_sheet.json` `show[]` plan), and the retiming pass
   dumped nearly all its slack into a single final `self.wait(18.33)` —
   the exact "single 15-20s static frame reads as dead air" failure mode
   the channel `CLAUDE.md` names explicitly. Fixed by adding the missing
   `title()` call and redistributing time across the three rule reveals
   (~4s each) instead of one dump.
5. **short/B02_ClaimExtraction916** (portrait re-layout) — the title never
   fades out for the scene's duration, but the four-card vertical stack's
   real height (~2.7 units, 4 cards + 3 gaps) was underestimated against a
   too-high initial center position, so the top card collided with the
   title's bottom edge for the entire scene. Fixed by lowering the stack's
   anchor point with the real stack height accounted for.
6. **short/END card** — `shorts.py --handle` defaults to `@nikbearbrown`
   (a toolkit placeholder, not this channel's handle) and was not
   overridden on the initial run, so the silent branded end-card read
   `@nikbearbrown` instead of `@DivijPawar`. Regenerated via
   `shorts.endcard_png()` with the correct handle and recompiled.

All six were caught by actually reading extracted PNG frames at multiple
points per beat (15/35/50/65/85%), never by a render or compile succeeding
— consistent with the channel's "the mp4 probe has never once caught a
real layout defect" rule.

## 9:16 short — beat selection

`./art shorts` auto-dropped B06/B08/B09 as the "cheapest" combination
under the cap, which would have opened the short mid-`Consistency Probe`
with no claim-extraction or verification context — an incoherent stand-
alone narrative. Manually overridden via `--drop` to keep B00 (cold open)
+ **B02 only** (Claim Extraction, fully self-contained with the worked
example) + B10/B11/B12 (verdict, handoff, outro) — a complete arc: problem
→ one fully-illustrated mechanism → recap → task → outro, at 128.5s
(well under the 180s cap, no need to trim further). B10's verdict card
already restates all three framework rules as text, so dropping B09
specifically does not lose the framework message. The auto-rewritten
outro narration (which literally quoted the first sentence fragments of
dropped beats as topic names) was hand-edited to real prose before its
audio was regenerated.

## Final status

16:9 4K master (`how-do-you-know-it-worked_DivijPawar_08-29-2026.mp4`,
3840×2160@30, captions muxed as `mov_text`) and 9:16 short
(`short/how-do-you-know-it-worked-short_DivijPawar_08-29-2026.mp4`,
1080×1920@30) both compiled with zero slates and passed frame-level visual
QC. See `_qc/PROOF-REVIEW.md` for the pre-submission self-review and ship
verdict.
