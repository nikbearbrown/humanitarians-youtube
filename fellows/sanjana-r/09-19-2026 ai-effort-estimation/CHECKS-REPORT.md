# CHECKS-REPORT — AI Effort Estimation

Written before the first compile, per the cli-explainer PROOF GATE.

## Beat classification
11 SHOW / 1 HOLD / 0 PUNT   (12 beats)

| Beat | Act | Class | On-screen artifact |
|---|---|---|---|
| B00 | INTRO | HOLD (bookend) | Claude composer, ask answered |
| B01 | PROBLEM | SHOW | gut plan (10) vs where similar sprints actually landed (Manim cloud) |
| B02 | FRAMEWORK | SHOW | reference-class forecasting, 4-step pipeline (Manim) — framework BEFORE examples |
| B03 | ASK | SHOW | the naive prompt (Claude composer) |
| B04 | CODE | SHOW | real estimate.py v1 — single-point POINTS (ClaudeCodeBeat) |
| B05 | OUTPUT | SHOW | three point estimates, total 10, no ranges — false precision (Manim) |
| B06 | CHANGE | SHOW | the revision prompt — add HISTORY + velocity (Claude composer) |
| B07 | CODE | SHOW | real estimate.py v2 — percentile*velocity range line (ClaudeCodeBeat) |
| B08 | OUTPUT | SHOW | P50-P80 bands, gut on the optimistic edge, 10->~19, no-class edge flagged (Manim) |
| B09 | SUMMARY | SHOW | 3-question rubric + honest-unknown rule (Manim) |
| B10 | NEXT STEPS | SHOW | scaffolded viewer prompt (Claude composer) |
| B11 | OUTRO | HOLD (bookend) | title restate, @HumanitariansAI |

No CARD-only claim beats. No unresolved PUNTs. Every OUTPUT beat is a moving
visualization (Manim), never a still.

## Teaching-arc checklist
- FRAMEWORK ✓ — B02 shows the 4-step reference-class method before any worked example.
- WORKED EXAMPLE ✓ — B03→B08 build, run, inspect, and revise a real estimator; real
  numbers throughout (gut 10; calibrated P80 ~19; per-task 8-12 / 2-3 / 3-5).
- FALSIFIABILITY ✓ — two levels. (1) The v1→v2 revision is the counter-case: the naive
  single-point model is exposed as systematically optimistic. (2) B08 shows the method's
  OWN limit — a task with no reference class (DB migration) is flagged "spike it, don't
  fake it," the case that stops the framework being applied blindly.
- SCAFFOLDED TASK ✓ — B10 hands a copyable prompt (backlog + last 15 completed tasks
  with ACTUAL durations → grouped classes, matched ranges, no-match flags), plus what a
  good vs bad answer looks like — not "ask Claude".
- BOOKENDS ✓ — cold-open composer (B00), framework (B02), handoff (B10), title outro (B11).
- NO-SOURCE-NO-VERDICT ✓ — every on-screen number is produced by the reel's own
  seed-locked estimator (scenes.py); the generating code is shown (B04 v1, B07 v2), and
  the CLASSES/VELOCITY dataset in scenes.py is identical to the HISTORY/VELOCITY in the
  displayed estimate.py v2.

## Legibility contract (spot-checks pending visual QC)
- Each SHOW beat names its artifact in shot.visual_intent / props.
- ~15–35% negative space targeted in every Manim scene.
- Un-highlighted elements kept ≥ 40% opacity (v1 gut points in full ink; muted labels dark).
- Comparison (B08 gut-10 vs honest-19 totals; per-row gut point on the band) shown
  side-by-side, held ≥ 2s.

Status: authoring PASS. Visual QC (frame-level) runs after compile → see _qc/ and PROOF-REVIEW.md.
