# CHECKS-REPORT — llm-function-calling

Written before the first slate compiled, per the ai-explainer PROOF GATE.

```
14 SHOW / 0 justified-HOLD / 0 PUNT-flagged
Teaching arc: FRAMEWORK ✓ | WORKED EXAMPLE ✓ | FALSIFIABILITY ✓
              SCAFFOLDED TASK ✓ | BOOKENDS ✓ | NO-SOURCE-NO-VERDICT ✓
```

## Per-beat classification

Every beat carries a `shot.show` block with ordered visual events and names its
on-screen artifact, so all 14 classify SHOW. No beat is a bare CARD and none is
a PUNT.

| Beat | Class | On-screen artifact it names |
|---|---|---|
| B00 | SHOW | composer, tool request/result output lines |
| B01 | SHOW | the overview being written and corrected |
| B02 | SHOW | predict card + commit line |
| B03 | SHOW | five-chip grid of what the model lacks |
| B04 | SHOW | the four-stage loop figure (framework) |
| B05 | SHOW | tool definitions flowing into context, one matching |
| B06 | SHOW | composer with the generation prompt |
| B07 | SHOW | the same loop figure carrying real payloads |
| B08 | SHOW | the four-message conversation as code |
| B08B | SHOW | the conversation stack growing one round per tool call |
| B09 | SHOW | binary branch, two failure directions, one resolver |
| BVDT | SHOW | verdict artifact page |
| BHTF | SHOW | composer prompt + three-point rubric |
| BOUT | SHOW | title-restate card |

## Teaching arc

- **FRAMEWORK ✓** — B04 presents the whole four-step loop before any example.
  It is a beat, not a phrase in narration, and it precedes B07.
- **WORKED EXAMPLE ✓** — B07 re-renders the *same* `FnCallLoop` figure with
  payloads on each stage, so the example visibly uses the framework rather than
  sitting beside it.
- **REPEAT/AGENT BRIDGE ✓** — B08B extends the return leg into repetition and
  lands the function-calling-to-agents bridge without adding a mechanism. Added
  as a beat rather than by padding existing narration, per duration-planner
  ("a complex mechanism becomes more beats, not longer ones").
- **FALSIFIABILITY ✓** — B09 is a full beat, not a passing caveat, and it states
  both directions: a successful call does not prove understanding, and an
  un-called tool does not prove the tool is wrong.
- **SCAFFOLDED TASK ✓** — BHTF carries a real prompt plus a three-point rubric
  the viewer can judge the output against, not "ask Claude about X".
- **BOOKENDS ✓** — cold open (B00), verdict (BVDT), your turn (BHTF),
  title-restate outro (BOUT).
- **NO-SOURCE-NO-VERDICT ✓** — every claim beat carries on-screen evidence.
  B03's chips carry the falsifying case, B07's payloads carry the trace, B08
  shows the literal message list. BVDT and BHTF recapitulate and are exempt.

## Legibility contract

- Negative space: all illustration beats sit on the cream stage with the
  structural family's built-in margins; `FnCallLoop` uses a 2×2 slot layout on
  the 1280×720 stage with ~18% of the frame left as ground.
- No un-highlighted element drops below 40% opacity — non-focal stage cards keep
  full-opacity ink left rails; only the *accent* changes.
- Comparison beats hold ≥2s: B09's two branches are both on screen from p≈0.48
  through the end of a 21s beat.

## Laws verified at authoring time

- **ILLUSTRATE LAW** — the Claude UI appears only at B00, B06, BVDT, BHTF, BOUT.
  B02–B05 and B07–B09 (including B08B) all illustrate. No two adjacent beats share a scheme;
  `FnCallLoop` recurs at B04 and B07 but they are separated by B05 and B06, and
  the recurrence is the deliberate framework callback the arc requires.
- **ASK→RESULT LAW** — one pair: B06 (the actual generation prompt) → B07 (the
  figure it produced). B00 is itself an ask that lands answered.
- **SPARK-LINE LAW** — every inner beat passes a `sparkLine` (≤4 words).
- **ONE ACCENT** — exactly one terracotta element per beat; audited per beat in
  the `show` blocks.
- **SHOW-DON'T-TELL** — shows were authored before narration. Body beats run
  47–63 words, inside the 45–70 budget; bookends are exempt.
- **DOODLE-BANNED** — no DoodleScene / DoodleChart.
- **EXECUTIVE-SUMMARY LAW** — B01 is `BrutalistHesitantWriter` with
  `lead_silence_s: 0.8` and a 33-word narration (≥9s window), and its correction
  is the reel's actual misconception.

## Register note

Register is **Plain**, not Teardown. Plain explains how a thing works and stops;
it does not judge the design. No beat in this sheet rates function calling as a
design choice. The six Plain moves are sequenced: stake first (B00/B01), wrong
guess built then falsified (B02/B03), mechanism once with exactly one inference
flag (B05), one running example planted early and paid off late (Boston, B00 →
B07/B08), failure modes both directions (B09), one compressible sentence (BVDT).

## Measured runtime (audio is the clock)

Kokoro `am_onyx`, 14 beats, **201.0s total**. Per-beat: B00 16.00 · B01 10.05 ·
B02 15.04 · B03 14.34 · B04 15.45 · B05 18.24 · B06 5.03 · B07 17.34 · B08 15.45 ·
B08B 16.32 · B09 16.90 · BVDT 16.62 · BHTF 21.29 · BOUT 2.94.

B01 measured 10.05s, clearing the ≥8s floor the EXECUTIVE-SUMMARY LAW sets so the
hesitant-writer correction lands on screen before the cut.

Duration was reached by script-sizing, not by stretching narration: the first pass
measured 168s because `am_onyx` runs ~3.35 words/sec (the 2.75 estimate came from an
`af_bella` sample). One beat was added (B08B) and three were lengthened (B00, B02,
BVDT) to land at 201s.
