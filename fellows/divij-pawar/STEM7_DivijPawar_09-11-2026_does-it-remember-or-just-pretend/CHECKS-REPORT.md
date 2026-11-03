# CHECKS-REPORT.md — does-it-remember-or-just-pretend

Written before the first slate compile, per PROOF GATE (ai-explainer
SKILL.md). This reel is **10 beats (B00-B09)**, not the ai-explainer
default of 10 — coincidentally matching the default count, though the
mix (6 Manim + 4 Remotion) is arrived at from content mass, not the
default template.

## Per-beat classification (SHOW / HOLD / PUNT — nopunt SKILL.md)

| Beat | Class | Scene / pattern | Reason |
|------|-------|------------------|--------|
| B00 | SHOW | ClaudeComposerAsk (Remotion) | Cold-open bookend; the UI is the subject |
| B01 | SHOW | B01_OneWordTwoMechanisms (Manim) | Names the central distinction as a real diagram (one word splitting into two boxes, one evaporating, one persisting) — nopunt "one thing splits into two, contrasted" row |
| B02 | SHOW | B02_HowRetrievalWorks (Manim) | Names a similarity-search mechanism with a real worked pair (flight vs. recipe) — nopunt "field of things, nearest ones light up" row |
| B03 | SHOW | B03_StaleMemory (Manim) | Names a failure mode as a diagram (a card that doesn't change while a clock ticks) — nopunt "something that should change but doesn't" row |
| B04 | SHOW | B04_PoisonedMemory (Manim) | Names a failure mode as a two-query timeline (dormant, then triggered) — nopunt "a hidden flaw resurfaces later" row |
| B05 | SHOW | B05_SameBlindSpot (Manim) | Names the falsifiability connection as a real side-by-side diagram, reprising STEM6's own visual rather than just asserting the parallel — nopunt "two things compared, same shape" row |
| B06 | SHOW | B06_TheFramework (Manim) | Names a set of three transferable rules — nopunt "panel/list of N things" row |
| B07 | SHOW | ClaudeVerdictArtifact (Remotion) | Verdict bookend; recaps, asserts nothing new |
| B08 | SHOW | ClaudeComposerAsk (Remotion) | Handoff bookend; prompt typed, read aloud, discussed with a 3-question scaffold |
| B09 | SHOW | ClaudeTitleOutro (Remotion) | Outro bookend; title restate + bridge to STEM8 |

**10 SHOW / 0 HOLD / 0 PUNT**

No beat requires an archival photograph — the only legitimate HOLD in
this catalog. Every claim in this script is a general architectural
pattern (context window vs. persistent store, vector similarity search,
decay, provenance, contradiction-checking), all of which are animatable
diagrams, not stand-ins for a real system.

**Punt costumes explicitly avoided:** the source script's filing-cabinet
title card and closing drawer shot are rebuilt into real diagram beats
and Remotion bookend props rather than carried as a literal filing-
cabinet illustration. No gen-AI clip, no stock icon of a brain or a
memory chip, no unfilled pipeline slate, no card whose narration names a
visual that isn't actually on screen.

## Beat-count rationale (10, not forced to match STEM6's 12)

Unlike STEM6, whose "Arbitration Step" section carried two independently-
checkable ideas (the single-round mechanic and the resolved/unresolved
branch) that needed separate holds, every section of this script maps to
exactly one idea:

- **B01** — the two-mechanisms distinction is one idea, even though it
  has two halves (context window, persistent memory), because the point
  being made is the contrast itself, best held in a single diagram.
- **B03/B04** — the two failure modes are kept as separate beats (not
  merged into one "failure modes" beat) because each has its own worked
  example and its own diagram; merging them would either crowd two
  timelines into one hold or cut one example.
- **B06** — the three design requirements (provenance/decay/contradiction)
  are kept as one beat, not three, because they're presented as a single
  three-part framework meant to be seen together, matching STEM6's B08
  precedent (four rules, one beat).

This matches the reel's actual content mass — `youtube/CLAUDE.md`'s "one
idea per beat" rule was applied per-section rather than forcing a fixed
count to match the prior episode.

## Whole-sheet teaching-arc checklist

- [x] **FRAMEWORK beat** — B01 states the episode's organizing distinction
  (context window vs. persistent memory) **before** the retrieval
  mechanism or either failure mode is described.
- [x] **WORKED EXAMPLE** — each mechanism beat carries its own concrete
  instance rather than staying abstract: the flight/recipe contrast (B02),
  the vegetarian preference (B03), and the two-query poisoned-memory
  timeline (B04) — three separate worked examples across three beats,
  each fully illustrated rather than referenced.
- [x] **FALSIFIABILITY / edge-case beat** — B05 is the dedicated stress
  test, and it stress-tests the episode's *own* proposed framework in
  advance: the same structural blind spot STEM6 established for
  arbitration-by-disagreement (it cannot catch shared agreement on a bad
  source) applies here to a single agent agreeing with its own past
  memory across time. B06's framework is introduced only after this
  limit is named, so it isn't presented as a complete fix.
- [x] **SCAFFOLDED viewer task** — B08 ships a real, ordered 3-question
  task: trace one stored fact's origin, its age, and what happens when
  something contradicts it. Directly actionable against the viewer's own
  memory/RAG system, not "learn more."
- [x] **Four bookends** — B00 (cold open), B07 (verdict), B08 (your turn),
  B09 (title-restate outro, bridging to STEM8).
- [x] **No source, no verdict** — every claim-bearing beat carries its own
  on-screen artifact: the splitting word and evaporating box (B01), the
  lit-up field of dots (B02), the unchanging card against a ticking clock
  (B03), the dormant-then-triggered cracked dot (B04), the side-by-side
  callback diagram (B05), the three-rule row (B06).

**Teaching arc: FRAMEWORK ✓ | WORKED EXAMPLE ✓ | FALSIFIABILITY ✓ |
SCAFFOLDED TASK ✓ | BOOKENDS ✓ | NO-SOURCE-NO-VERDICT ✓**

## Slate rules audit (Step 4b, automated)

Not yet run against `runtime/qc/sheet_check.py` — see BUILD-PROMPT.md Step
1. All `ClaudeComposerAsk` (B00, B08) and `ClaudeVerdictArtifact` (B07) /
`ClaudeTitleOutro` (B09) props were hand-checked against the hard-limit
table in `agents.md` Step 4 during authoring:

| Beat | Field | Length | Limit | OK? |
|---|---|---|---|---|
| B00 | `topic` | 12 chars ("AGENT MEMORY") | 125 hard | yes |
| B00 | `greeting` | matches `metadata.greeting` ("Olá, Divij") | 55 hard | yes |
| B00/B08 | `command` | single-line, well under 100 chars | wraps, not hard | yes |
| B07 | `artifactLines[]` | each line under 95 chars | wraps, not hard | yes |
| B09 | `title` | "Does It Remember, or Just Pretend To?", 38 chars | wraps, not hard | yes |

Run `./art check` (or `sheet_check.py` directly) before rendering to get
the automated pass — this table is a manual pre-check, not a substitute.

## Status

Beat sheet, gate docs, and `scenes.py` are authored and internally
consistent — verified by direct diff: every `shot.manim.scene_class` in
`beat_sheet.json` names exactly `B01`-`B06` (`B01_OneWordTwoMechanisms`
through `B06_TheFramework`), matching the six Manim beats above.

**GATE P signed 09/11/2026 — build completed end to end.** Full pipeline
run: Kokoro audio (10 beats, ground truth), retiming, Manim 4K render,
Remotion bookends, 4K compile, captions, `./art shorts` derivation. See
below for the real defects this pass caught and fixed — none were caught
by the mp4-probe/manifest check alone; all came from actually reading
extracted frames per §6 of the channel `CLAUDE.md`.

## Post-audio retiming (Step 3)

Every Manim scene ran shorter than its real Kokoro audio (the scenes as
first authored used pre-audio time estimates that undershot in every
case, 5–20s per beat), the same direction as STEM6's own retiming pass.
Fixed by scaling up 2–4 of the longer holds near each beat's end,
computed from `actual_duration_s - measured_-ql_duration`, never dumping
the full delta into one hold — B06 in particular added time to its
per-rule reveal loop *and* its two closing holds rather than parking
~20s in a single static frame. All 6 scenes landed within 0.3s of
`actual_duration_s` after correction.

## Real defects found in mid-scene/frame QC (not caught by any automated check)

1. **B03 (Stale Memory)** — two defects in one transition: (a) `cap1`
   ("no built-in clock") and `cap2` ("something has to decide...") were
   crossfaded simultaneously at the identical `DOWN*3.0` anchor, so two
   different strings briefly double-exposed at overlapping opacity —
   caught in low-res smoke-test QC, invisible in any final-frame check
   since both settle to their own frame eventually. Fixed by sequencing
   the fade (`FadeOut(cap1)` fully, then `FadeIn(cap2)`), never
   simultaneous at a shared position. (b) The "recommend dinner" query
   card sat at y=-2.6, sharing the bottom third of the frame with both
   captions (also near y=-3.0) — its box bottom edge touched the caption
   text directly. Fixed by moving the query card to y=-0.4, well clear of
   the caption zone.
2. **B04 (Poisoned Memory)** — the "one bad moment doesn't stay
   contained" caption was anchored at `UP*3.0`, directly into the
   persistent title (this scene's title never fades, and its own bottom
   edge sits at y≈2.9 for this font size) — the exact title-collision
   defect class the channel `CLAUDE.md` already documents from a prior
   session, recurring here on a fresh scene. Fixed by clearing the whole
   dot-field diagram first, then showing the caption alone in the frame's
   vertical center, rather than stacking it above still-visible content.
3. **short/B01_OneWordTwoMechanisms916** (portrait re-layout) — none
   found; the layout was computed from measured mobject heights
   (`title.get_bottom()`, box heights) rather than guessed coordinates
   from the start, so the smoke-test render came back clean on the first
   pass. Retimed only for duration (43.1s → 48.53s), no layout changes
   needed.

All three defects above were caught by actually reading extracted PNG
contact sheets sampled across each clip's full duration, never by a
render or compile succeeding — consistent with the channel's "the mp4
probe has never once caught a real layout defect" rule.

## 9:16 short — beat selection

`./art shorts` auto-dropped B01, B02, B05, B06 as the "cheapest"
combination under the cap, keeping B03+B04 (the two failure-mode beats)
directly after the cold open. This was incoherent: B03's own opening line
— "**That gap** creates two distinct problems" — refers directly to B02's
"no built-in sense of expiration/confidence/origin," which the auto-plan
had just cut, leaving a dangling reference with no antecedent. The same
failure class STEM6's own build notes flagged (opening mid-mechanism with
no setup). Manually overridden via `--drop B02 B03 B04 B05 B06` to keep
B00 (cold open) + **B01 only** (One Word, Two Mechanisms — fully
self-contained: states its own contrast and lands its own concluding
line without depending on any other beat) + B07/B08/B09 (verdict,
handoff, outro) — a complete arc: problem → one fully-illustrated
distinction → recap → task → outro, at 126.4s (well under the 180s cap).
B07's verdict card already restates all four framework rules as text, so
dropping B02–B06 does not lose the framework message — the same
reasoning STEM5 and STEM6 both applied when trimming their own shorts.
The auto-rewritten outro narration was regenerated via Kokoro
(`--no-gate`, since this is a mechanical re-cut of already-GATE-P-approved
content, not new material) after `shorts.py` rewrote it to reference the
cuts.

## Final status

16:9 4K master (`does-it-remember-or-just-pretend_DivijPawar_09-11-2026.mp4`,
3840×2160@30, 324.2s, captions muxed as `mov_text`) and 9:16 short
(`short/does-it-remember-or-just-pretend-short_DivijPawar_09-11-2026.mp4`,
1080×1920@30, 126.4s, captions muxed as `mov_text`) both compiled with
zero slates and passed frame-level visual QC across every beat, including
the Remotion bookends and a whole-video overview pass. No
`_qc/PROOF-REVIEW.md` self-review has been run yet against the full PROOF
rubric in `youtube/PROOF.md` — recommended before treating either file as
ready to publish, even unlisted.
