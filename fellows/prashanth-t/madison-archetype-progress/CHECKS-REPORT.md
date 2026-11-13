# CHECKS-REPORT — madison-archetype-progress

Written before the first slate compiled, per the ai-explainer PROOF GATE.

```
14 SHOW / 0 justified-HOLD / 0 PUNT-flagged
Teaching arc: FRAMEWORK ✓ | WORKED EXAMPLE ✓ | FALSIFIABILITY ✓
              SCAFFOLDED TASK ✓ | BOOKENDS ✓ | NO-SOURCE-NO-VERDICT ✓
```

## Per-beat classification

Every beat carries a `shot.show` block with ordered visual events and names its
on-screen artifact, so all 14 classify SHOW. No bare CARDs, no PUNTs.

| Beat | Class | On-screen artifact it names |
|---|---|---|
| B00 | SHOW | composer; output lines naming what it is and the status |
| B01 | SHOW | the overview being written and corrected |
| B02 | SHOW | twelve-archetype chip grid |
| B03 | SHOW | the shallow pipeline as three stacked cards |
| B04 | SHOW | predict card + commit line |
| B05 | SHOW | brand artefacts flowing into the analyzer |
| B06 | SHOW | composer with the generation prompt |
| B07 | SHOW | two archetype readings resolving on the cost of the gap |
| B08 | SHOW | the planned output schema as code |
| B09 | SHOW | the scope ladder, Ruler accented |
| B10 | SHOW | the five-chip status board |
| BVDT | SHOW | verdict artifact page with the status line |
| BHTF | SHOW | composer prompt + three-point rubric |
| BOUT | SHOW | title-restate card |

## Teaching arc

- **FRAMEWORK ✓** — B02 puts all twelve archetypes on screen as a beat, before
  any example, and before the method is described.
- **WORKED EXAMPLE ✓** — B07 runs the B04 handbag through the framework and
  returns a primary/secondary pair plus the tension, which is exactly what the
  method claims to produce. It uses the framework rather than sitting beside it.
- **FALSIFIABILITY ✓** — B10 is a full beat, not a passing caveat, and it names
  what does *not* exist: build not started, no results yet. B07 adds the both-
  directions move: neither single reading is wrong, the gap is the finding.
- **SCAFFOLDED TASK ✓** — BHTF carries a real prompt plus a three-point rubric.
  It has the viewer run the method by hand, which is the honest offer while the
  tool does not exist.
- **BOOKENDS ✓** — cold open (B00), verdict (BVDT), your turn (BHTF),
  title-restate outro (BOUT).
- **NO-SOURCE-NO-VERDICT ✓** — every claim beat carries on-screen evidence. B02's
  grid carries the vocabulary, B03's stack carries the status-quo shape, B07's
  branches carry the tension, B08's code carries the target schema, B10's chips
  carry the status. BVDT and BHTF recapitulate and are exempt.

## Honesty audit (the governing constraint for this reel)

This is a planning-stage update, so the risk is overclaiming, not sourcing.

- No beat shows tool output. There is no tool.
- B07 `slideMeta`: *"illustrative example — not a produced result."*
- B08 file tab: *"planned output schema — a design target, not produced"*, and the
  code block's last line is `// NOT OUTPUT. This is the shape I am building toward.`
- B10 carries two deliberately negative chips so the board cannot read as a brag.
- BVDT's artifact page ends *"Status: scoped with the team. Not built. No results
  yet."* so the summary cannot be excerpted as capability.
- B01's narration states "Today it is a plan and a scope document, not a working
  tool" in the same breath as the design intent.

## Legibility contract

- B02 runs `cols=3` with **no caption**: at `cols=4` the grid is 1338px on a
  1280 stage (`x0=-29`, edge bleed); at `cols=3` row four (582–678) collides with
  the caption slot (~598). Clarifier moved to the spark line.
- Non-focal elements keep full-opacity ink rails; only the accent changes. B03
  accents nothing on purpose — none of those three steps is the answer.
- Comparison beat holds ≥2s: B07's two branches are both on screen from p≈0.50
  through the end of a 16.3s beat.

## Laws verified at authoring time

- **ILLUSTRATE LAW** — UI only at B00, B06, BVDT, BHTF, BOUT. B02–B05 and
  B07–B10 all illustrate. **No two adjacent beats share a scheme** (verified
  programmatically); `ChipGrid` recurs at B02/B10 and `LayerStack` at B03/B09,
  both widely separated.
- **ASK→RESULT LAW** — one pair: B06 (the actual generation prompt) → B07 (the
  figure it produced). B00 is itself an ask that lands answered.
- **SPARK-LINE LAW** — every inner beat passes a `sparkLine` ≤4 words; B06 uses
  `"Map the tension."` rather than an empty greeting.
- **ONE ACCENT** — one terracotta moment per beat; audited per beat in SHOTLIST.
- **SHOW-DON'T-TELL** — shows authored before narration. Body beats run 44–58
  words, inside the 45–70 budget (B04 at 44 is a hook, not a claim beat);
  bookends exempt.
- **EXECUTIVE-SUMMARY LAW** — B01 is `BrutalistHesitantWriter` with
  `lead_silence_s: 0.8`, 31 words, measured **10.47s** (≥8s floor), and its
  trigger is a **single token** (`quiz`) so the correction actually fires.
- **DOODLE-BANNED** — no DoodleScene / DoodleChart.
- **REUSE ONLY** — no new components; nothing added to `Root.tsx`, no
  `scene-index` rebuild.

## Measured runtime (audio is the clock)

Kokoro `am_onyx`, 14 beats, **193.5s total** — inside the requested 180–200s.

B00 12.35 · B01 10.47 · B02 17.64 · B03 14.72 · B04 13.65 · B05 17.90 ·
B06 5.21 · B07 16.34 · B08 16.98 · B09 14.38 · B10 14.93 · BVDT 14.81 ·
BHTF 20.67 · BOUT 3.43

The first pass measured 200.3s, 0.3s outside the window. Reached 193.5s by
**script-sizing** — trimming a redundant parallelism in B00, tightening B08, and
compacting BHTF's spoken rubric (which is also rendered on screen) — never by
stretching or clipping narration.
