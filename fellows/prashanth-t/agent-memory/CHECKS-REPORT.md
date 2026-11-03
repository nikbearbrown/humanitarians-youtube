# CHECKS-REPORT — agent-memory

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
| B00 | SHOW | composer; output lines showing empty context and no stored history |
| B01 | SHOW | the overview being written and corrected |
| B02 | SHOW | predict card + commit line |
| B03 | SHOW | two requests, the second re-sending the whole transcript |
| B04 | SHOW | the three memory tiers as a stack |
| B05 | SHOW | turn chips filling the context window to its ceiling |
| B06 | SHOW | composer with the generation prompt |
| B07 | SHOW | the store feeding one retrieved fact into the next request |
| B08 | SHOW | save and retrieve as two literal calls around the model call |
| B09 | SHOW | one new session splitting on whether a store exists |
| B10 | SHOW | the five things a remembered/forgotten fact does and does not prove |
| BVDT | SHOW | verdict artifact page, four numbered lines |
| BHTF | SHOW | composer prompt + three-point rubric |
| BOUT | SHOW | title-restate card |

## Teaching arc

- **FRAMEWORK ✓** — B04 presents all three tiers as a beat, before any example and
  before the mechanism of either layer is explained.
- **WORKED EXAMPLE ✓** — B09 runs the B02 coffee order through the B04 framework and
  resolves on the thesis. It uses the framework rather than sitting beside it.
- **FALSIFIABILITY ✓** — B10 is a full beat and states **both** directions: a
  remembered fact proves retrieval worked (not understanding); a forgotten one does
  not prove the store broke (the search missed, or nothing was saved).
- **SCAFFOLDED TASK ✓** — BHTF carries a real prompt plus a three-point rubric,
  including a consent check on what gets written down about a person.
- **BOOKENDS ✓** — cold open (B00), verdict (BVDT), your turn (BHTF), outro (BOUT).
- **NO-SOURCE-NO-VERDICT ✓** — every claim beat carries on-screen evidence: B03's
  payload, B04's stack, B05's filling window, B07's retrieval arc, B08's two calls,
  B09's branches, B10's chips. BVDT and BHTF recapitulate and are exempt.

## Regression guards (all verified programmatically before rendering)

| Prior bug | Guard | Result |
|---|---|---|
| `@NikBearBrown` in the composer chip | `folderLabel` as a **per-beat prop** on every ClaudeComposerAsk beat | 0 beats missing |
| Multi-word trigger silently never fires | B01 trigger is a single token | `remembers`, 1 occurrence |
| Typing truncated mid-sentence | `charMs: 22`, tuned to fit; final frame to be sampled after render | pending visual check |
| Animation truncated at ~50% of the beat | `durationInSeconds` on **every** beat | 0 beats missing |
| Orphan number on the verdict page | no empty strings in `artifactLines` | 0 empties |
| Review footer burned in | `metadata.review_labels: false` | set |

## Legibility contract

- B05 and B10 run `ChipGrid` at `cols=3` with 6 and 5 items — two rows each, so no
  collision with the caption slot (unlike a 12-chip four-row grid).
- Non-focal elements keep full-opacity ink rails; only the accent changes.
- Comparison beat holds ≥2s: B09's two branches are both on screen from p≈0.50
  through the end of a 17.6s beat.

## Laws verified at authoring time

- **ILLUSTRATE LAW** — UI only at B00, B06, BVDT, BHTF, BOUT. B02–B05 and B07–B10
  all illustrate. **No two adjacent beats share a scheme** (verified
  programmatically); `ChipGrid` recurs at B05/B10 and `ClaudeCodeBeat` at B03/B08,
  both widely separated.
- **ASK→RESULT LAW** — one pair: B06 (the actual generation prompt) → B07 (the
  figure it produced). B00 is itself an ask that lands answered.
- **SPARK-LINE LAW** — every inner beat passes a `sparkLine` ≤4 words; B06 uses
  `"Somewhere else."` rather than an empty greeting.
- **ONE ACCENT** — one terracotta moment per beat; audited per beat in SHOTLIST.
- **SHOW-DON'T-TELL** — shows authored before narration. Body beats run 47–64 words,
  inside the 45–70 budget; bookends exempt.
- **EXECUTIVE-SUMMARY LAW** — B01 is `BrutalistHesitantWriter`, `lead_silence_s: 0.8`,
  31 words, measured **9.79s** (clears the ≥9s window, not just the ≥8s floor).
- **DOODLE-BANNED** — no DoodleScene / DoodleChart.
- **REUSE ONLY** — no new components. One shared composition (`ClaudeCodeBeat`) gained
  optional `durationInSeconds` + `calculateMetadata` per the build instruction, default
  unchanged at 10s so no other reel renders differently.

## Measured runtime (audio is the clock)

Kokoro `am_onyx`, 14 beats, **197.4s total**.

B00 14.46 · B01 9.79 · B02 13.97 · B03 15.00 · B04 16.98 · B05 15.25 · B06 5.03 ·
B07 18.56 · B08 15.55 · B09 17.56 · B10 16.58 · BVDT 14.34 · BHTF 21.03 · BOUT 3.33

The first pass measured 190.1s with B01 at 8.53s. Reached 197.4s by **script-sizing**
four beats — giving B02's wrong guess more plausible detail, naming the store key in
B08, landing B10's both-directions point, and lengthening B01 to clear the 9s window —
never by stretching or clipping narration.
