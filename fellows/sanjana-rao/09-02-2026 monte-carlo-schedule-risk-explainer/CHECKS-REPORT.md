# CHECKS-REPORT — Monte Carlo Schedule Risk

Written before the first compile, per the cli-explainer PROOF GATE.

## Beat classification
11 SHOW / 1 HOLD / 0 PUNT   (12 beats)

| Beat | Act | Class | On-screen artifact |
|---|---|---|---|
| B00 | INTRO | HOLD (bookend) | Claude composer, ask answered |
| B01 | PROBLEM | SHOW | plan-19 line vs the real finish histogram (Manim) |
| B02 | FRAMEWORK | SHOW | 4-step method pipeline (Manim) — framework BEFORE examples |
| B03 | ASK | SHOW | the actual prompt (Claude composer) |
| B04 | CODE | SHOW | real schedule_sim.py v1 (ClaudeCodeBeat) |
| B05 | OUTPUT | SHOW | simulated distribution: plan / P50 / P80 / risk (Manim) |
| B06 | CHANGE | SHOW | the revision prompt (Claude composer) |
| B07 | CODE | SHOW | real schedule_sim.py v2 — the merge line (ClaudeCodeBeat) |
| B08 | OUTPUT | SHOW | v1 vs v2 distributions overlaid, P80 shift (Manim) |
| B09 | SUMMARY | SHOW | P50/P80/P90 reference card (Manim) |
| B10 | NEXT STEPS | SHOW | scaffolded viewer prompt (Claude composer) |
| B11 | OUTRO | HOLD (bookend) | title restate, @HumanitariansAI |

No CARD-only claim beats. No unresolved PUNTs. Every OUTPUT beat is a moving
visualization (Manim), never a still.

## Teaching-arc checklist
- FRAMEWORK ✓ — B02 shows the 4-step method before any worked example.
- WORKED EXAMPLE ✓ — B03→B08 build, run, inspect, and revise a real simulator.
- FALSIFIABILITY ✓ — B06–B08 stress-test the naive single-chain model; the
  parallel-merge revision is the counter-case that proves the method (the finish
  is the MAX of parallel paths, so v2 lands later than v1).
- SCAFFOLDED TASK ✓ — B10 hands the viewer a copyable prompt (tasks + three
  estimates + dependencies), not "ask Claude".
- BOOKENDS ✓ — cold-open composer (B00), framework (B02), handoff (B10),
  title outro (B11).
- NO-SOURCE-NO-VERDICT ✓ — every on-screen number is produced by the reel's own
  runnable simulator (scenes.py, seed-locked); the code that generates the
  output is shown on screen (B04, B07).

## Legibility contract (spot-checks pending visual QC)
- Each SHOW beat names its artifact in shot.visual_intent / props.
- ~15–35% negative space targeted in every Manim scene.
- Un-highlighted elements kept ≥ 40% opacity (v1 bars at 0.55, muted labels dark).
- Comparison (B08) shown side-by-side, held ≥ 2s.

Status: authoring PASS. Visual QC (frame-level) runs after compile → see _qc/ and PROOF-REVIEW.md.
