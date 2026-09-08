# Visual QC — new components (B01, B02, B03, B04, B06)

Frames sampled at 50%/90% of each component's own duration (not fixed frame
numbers — an earlier pass used fixed frame indices across clips of different
lengths and produced misleading ~25%-progress samples for every beat).

## Findings

| Beat | Component | Verdict | Notes |
|---|---|---|---|
| B01 | CommbankMythMerge | OK | Two source chips, destination window, terracotta settle line. Good use of SAFE area, one accent. |
| B02 | CommbankRecordFork | **BLOCKER → FIXED** | Right-side outcome badges overflowed the canvas edge (END_X=1680 + badge width 280 = 1950, past both the 1920 canvas and the 1824 SAFE.r boundary). Fixed: END_X moved to 1480, notes column narrowed to 400px, connector line shortened to span the gap. Re-rendered and confirmed both badges now land fully inside SAFE with margin. |
| B03 | CommbankDisputesGrade | OK | 2×2 grid, MISSING item correctly muted/undotted, caption cited. |
| B04 | CommbankVoiceBotTimeline | OK | All 5 stage chips visible, arrows connect cleanly, AGM chip correctly accented, banned label struck through. |
| B06 | CommbankNoReconnect | OK | Two verdict cards, broken-X connector, breakLabel lands in terracotta. Clean focal composition. |

No BLOCKER or MAJOR defects remain after the B02 fix. Re-render of B02
confirmed via frame at 90% span (`_qc/frames/B02_fixed.png`).

## Full master QC (all 10 beats, `claude-liam-commbank-untangled.mp4`, 153.8s)

Second defect found and fixed during this pass: `beat_sheet.json` B05 pointed
at Remotion composition id `PredictCard`, which does not exist as a
top-level composition (only `MedhavyPredictCard` and the generic 1280x720
`Illu-PredictCard` preview do — `remotion_scenes.py` passes `pattern`
straight through as a literal composition id, no aliasing). This caused a
hard render failure on B05 and, as a side effect, left Remotion's render
process in a bad state that caused the next render (B07) to hang
indefinitely (confirmed via `ps` — near-zero CPU after 3+ hours; killed
manually). Fix: authored a reel-scoped `CommbankPredictCard` component
(1920×1080, matching the reel's own visual language) registered in
`Root.tsx`, repointed B05 at it. B07 re-rendered cleanly on retry once the
stuck process was killed, confirming the hang was contention from the B05
crash, not a defect in `ClaudeVerdictArtifact` itself.

All 10 beats (B00, B05, B07, B08, B09 — the reused/ready-made compositions —
plus the 5 new ones) sampled at 85% of their span in the final assembled
master. All clean: no edge bleed, no collisions, legible at size, brand chip
present, SAFE margins respected. The two beats that got audio-conformed via
speed change (B01, B03, ~1.07x slow) and the three that got center-cut
(B02, B04, B06, 0.6–1.2s trimmed from head/tail) were re-checked in the
final master specifically — no clipping or misframing introduced by
conform.

Motion-language note (not a defect): compile.py flagged `illustrate` at
60% of beats vs. a ~40% house guideline. Expected here — ILLUSTRATE LAW
restricts the Claude UI to bookends only (B00/B07/B08/B09), so the entire
middle (B01–B06) is concept-illustration by design.

STATUS: zero outstanding BLOCKER/MAJOR defects. First watchable cut is
complete.

## Visual redesign pass (2026-07-28, per author request)

Author feedback: diagrams read as plain (text-in-boxes, lots of empty
canvas); audio had one robotic line (B09 literally said "question mark"
out loud). Scope agreed: richer/more dynamic visuals, kept lightweight
(pure SVG icons, no bitmap assets, same beat durations — no runtime or
file-size bloat).

Changes: added a shared `CommbankIcons.tsx` (11 small inline-SVG glyphs,
no external assets) and enhanced all 6 diagram components — icons per
concept, a converging funnel (B01), traveling pulse dots along drawn paths
(B02/B04), a source-count tally visualizing the sourcing asymmetry (B02),
a bounce-in reveal per function card (B03), a jolt + glow at the break
moment (B06), and two ghost option-cards to fill B05's previously sparse
canvas. B09's narration fixed to a natural `?` instead of spelling out
"question mark" (re-generated audio, re-compiled).

Two real defects caught during re-QC, both fixed and confirmed on
re-render:
- **B04 stray dot**: `IconQuote`'s path mixed absolute (size-scaled)
  coordinates in its `M` command with an additional `transform="scale(40)"`
  wrapping the whole path — double-scaling the origin point and displacing
  the glyph ~20x off-position. Rewrote with consistent absolute coordinates,
  no wrapping transform. Confirmed via a zoomed crop before and after.
- **B05 ghost cards read as invisible**: opacity multiplier (0.5) stacked
  with an already-light token color made them illegible — defeated the
  point of adding them. Raised opacity to 0.9 and switched to `INK_SOFT`
  for border/glyph color; now clearly visible without competing with the
  question.

One false alarm, logged for the record: B06's break line looked washed
out when sampled at 85% of the beat's span in the compiled master, but the
standalone render at the equivalent point showed full solid color —
re-sampling the master at 95% confirmed it reaches full opacity correctly.
The 85% sample simply landed earlier in the reveal window than intended;
not a defect.

Also hit two render-batch timeouts during this pass (B04 first attempt,
mid-batch) with no crash or error — process was gone on inspection, just a
slow render exceeding the batch's timeout window. Retried individually
with a longer bound and it completed normally both times; not a repeat of
the earlier B05/B07 lock-contention hang.

Recompiled master: 152.8s (unchanged runtime, as intended).

## Final fix pass (2026-07-28, per author request)

Author caught B01's first chip text ("~15,000 disputes/day") clipping
"day" at the right edge — the label's foreignObject was 120px wide, too
narrow for "disputes/day" as one unbroken token (no space for the browser
to wrap on). Fixed: widened the chip (220px → 280px) and its label area,
added `overflowWrap: break-word` as a safety net so a future long label
wraps instead of clipping. Confirmed fixed on re-render.

Author also asked to drop any continuously-"floating" motion in favor of
simpler/static visuals, to keep rendering fast — most of this session's
time went to environment setup and one crash-induced 3-hour hang, not the
animation work itself, but two spots genuinely were continuous sine-driven
loops rather than one-time reveals: B01's traveling-dot pulse and B05's
underline pulse (6 oscillation cycles across the beat's back third).
Both removed (constant radius / constant stroke width). Left the
one-time, settle-and-stop motion in B02/B04 (traveling pulse along a
drawn path, once) and B06 (jolt-and-settle) alone, since those aren't
floating loops.

Recompiled once more: 152.8s, unchanged.

## Executive-summary beat + pacing revision (2026-07-29, per reviewer feedback)

Two changes, see `PEDAGOGY.md` for full narration/thesis rationale:

1. **B00B added** (new intro-summary beat, right after B00): reuses
   `ClaudeVerdictArtifact` unchanged. Sampled at ~45% of its span in the
   final master — title card and three summary lines render cleanly, no
   overflow, no collision, brand chip and SAFE margins respected.
2. **Pacing**: applied the same hold-only treatment approved for the
   Klarna reel — 1.0s hold (held last frame + silence) at the end of
   every beat except the last, then a straight hard cut, no crossfade.
   Built as a separate post-pass over `compile.py`'s own per-beat
   conformed clips (video) and per-beat Kokoro narration (audio), same
   as the Klarna reel — **not** part of `compile.py` itself, must be
   re-run manually after any recompile.

Final master: `claude-liam-commbank-untangled-v2.mp4`, 179.7s (~3:00).

## Presenter rebrand (2026-08-04, per reviewer feedback)

Replaced all "Liam, in for Bear" / `@NikBearBrown` references (spoken and
on-screen) with Tanmay Kulkarni — see `PEDAGOGY.md` for the full list of
fields changed. Re-rendered B00/B08/B09 (visual), regenerated audio for
B00/B00B/B09 (narration), recompiled, re-applied the 1.0s hold pacing.
Sampled B00 and B08/B09 in the final master — greeting and folder chip
render correctly ("Habari, Tanmay", "@TanmayKulkarni"). Full-text grep of
the beat sheet confirmed zero remaining Bear/Brown/Liam references.

Final master: 180.3s (~3:00).

## Resolution fix (2026-08-04, per reviewer feedback)

Caught: final output was only 720p, despite every Remotion component being
registered and rendered at 1920x1080 with `--scale=2` (true 4K, 3840x2160)
per beat. Root cause: `compile.py` defaults to `--height 720` (width
computed proportionally) during the conform/concat step, silently
downscaling the already-4K per-beat renders. Fixed by re-running
`compile.py --height 2160 --force`, then re-applying the same 1.0s-hold
pacing script on the new 4K clips. Confirmed via `ffprobe`: final master
is 3840x2160.
