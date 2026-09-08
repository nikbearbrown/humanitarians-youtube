# CHECKS-REPORT.md — what-makes-ai-agentic

Written before the first slate compile, per PROOF GATE (ai-explainer SKILL.md).

## Per-beat classification (SHOW / HOLD / CARD — nopunt SKILL.md)

| Beat | Class | Scene / pattern | Reason |
|------|-------|------------------|--------|
| B00 | SHOW | ClaudeComposerAsk (Remotion) | Cold-open bookend; the UI is the subject |
| B01 | SHOW | B01_TierSpectrum (Manim) | Names a structure (four-tier spectrum) — nopunt "ladder / tiers / hierarchy" row |
| B02 | SHOW | B02_TierZero (Manim) | Names a mechanism (next-token prediction, no tools bound) — animated diagram |
| B03 | SHOW | B03_TierOne (Manim) | Names a flow (user → model → tool API → back) — nopunt "animated flow / call chain" row |
| B04 | SHOW | B04_TierTwo (Manim) | Names a plan built step by step with a branch — nopunt "static flow → node-and-arrow drawn on cue" row |
| B05 | SHOW | B05_TierThree (Manim) | Names a cycle carrying state (Monitor→Decide→Act→Remember) — animated loop |
| B06 | SHOW | B06_TheChecklist (Manim) | Names three diagnostic questions + a claim about where the market sits — progressive disclosure + bracketed span |
| B07 | SHOW | ClaudeVerdictArtifact (Remotion) | Verdict bookend; recaps, asserts nothing new |
| B08 | SHOW | ClaudeComposerAsk (Remotion) | Handoff bookend; prompt typed, read aloud, discussed with rubric |
| B09 | SHOW | ClaudeTitleOutro (Remotion) | Outro bookend; title restate |

**10 SHOW / 0 HOLD / 0 PUNT**

No beat requires an archival photograph — the only legitimate HOLD. Every
claim is a structure, a mechanism, a flow, or a comparison, all of which
appear in the nopunt catalog and are therefore animatable.

**Punt costumes explicitly avoided:** the source script's title card
("swirling tech-blue background"), its end card ("subscribe prompt, two
thumbnail cards"), and its corner cross-promo thumbnail were all cut or
rebuilt rather than carried in as stills. No gen-AI clip, no archive still,
no FormA card whose narration names a visual.

## Whole-sheet teaching-arc checklist

- [x] **FRAMEWORK beat** — B01 presents the four-tier spectrum and fixes the
  running example ("book me a flight") **before** tier 0 is described. The
  B06 checklist is a recap of this framework, not its first statement.
- [x] **WORKED EXAMPLE** — the same task is walked through all four tiers in
  B02–B05, with the spectrum bar on screen throughout and the active tier lit.
  The example visibly *uses* the framework rather than sitting adjacent to it.
- [x] **FALSIFIABILITY / edge-case beat** — B06 turns the framework on the
  products the reel is about and finds the label mostly fails: what is sold
  as agentic lands in tier 1–2, and true tier 3 is rare and unsolved. A full
  beat with its own visual (the terracotta bracket over tiers 1–2), not a
  caveat in passing.
- [x] **SCAFFOLDED viewer task** — B08 ships a real prompt ("Audit an AI
  product I use. Which tier is it really…") plus a 3-item rubric the viewer
  checks the output against: names specific tools / shows a multi-step plan /
  proves cross-session memory. Not "ask Claude about X."
- [x] **Four bookends** — B00 (cold open), B07 (verdict), B08 (Your Turn),
  B09 (title-restate outro).
- [x] **No source, no verdict** — every claim-bearing beat carries its
  artifact on screen: the spectrum bar (B01), the locked tool row (B02), the
  call chain (B03), the flowchart and conflict (B04), the memory ring (B05),
  the bracketed span (B06). B07 and B08 are exempt (they recapitulate).

**Teaching arc: FRAMEWORK ✓ | WORKED EXAMPLE ✓ | FALSIFIABILITY ✓ |
SCAFFOLDED TASK ✓ | BOOKENDS ✓ | NO-SOURCE-NO-VERDICT ✓**

## Slate rules audit (Step 4b, automated)

`runtime/qc/sheet_check.py` — **clean, 10 beats, no findings**, including
under `--strict`. Every non-wrapping field (`topic`, `segment`, `greeting`,
`handle`) is inside its hard limit, and every wrapping field is inside its
*recommended* count, not merely its wrap width.

## Legibility contract (per beat)

Every SHOW beat names its on-screen artifact in `shot.manim.scene_class` or
`shot.remotion.pattern`, and every Manim beat carries an ordered `show` block
of visual events. Scenes hold ~15–35% negative space (title at top, single
diagram centered); un-highlighted elements stay at INK/SOFT and are never
dropped below GHOST. B04's two flight options and B06's three questions each
hold their full set on screen simultaneously for comparison.

## PPT test

No beat is a headline over a paragraph. Each body beat has motion that enacts
its sentence: tokens assembling one at a time (B02), a pulse making the round
trip to the tool and back (B03), boxes drawing on the spoken step and the
chain visibly halting (B04), the ring circling unattended while a day counter
climbs and memory chips persist (B05), a bracket sweeping the span where the
market actually sits (B06).

## Status

Beat sheet, gate docs, and `scenes.py` are authored and internally
consistent. This pass closes the PROOF GATE for authoring.

**Blocked on:** GATE P signature in `PEDAGOGY.md` (currently `VERDICT:
PENDING`). No audio may be generated until a human signs it.
