# CHECKS-REPORT — madison-archetype-progress-week2

Written before the first compile, per the ai-explainer PROOF GATE.

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
| B00 | SHOW | composer; three status output lines |
| B01 | SHOW | the overview being written and corrected |
| B02 | SHOW | predict card + the three Ruler copy phrases |
| B03 | SHOW | the three design parts as a stack |
| B04 | SHOW | four published-text sources flowing into the detector |
| B05 | SHOW | composer with the generation prompt |
| B06 | SHOW | the planned scored output with evidence quotes |
| B07 | SHOW | two evaluation branches and the hand-labelled resolver |
| B08 | SHOW | the three open sample-data questions |
| B09 | SHOW | the four-rung route, rung one accented |
| B10 | SHOW | the five-chip status board |
| BVDT | SHOW | verdict artifact page, four numbered lines |
| BHTF | SHOW | composer prompt + three-point rubric |
| BOUT | SHOW | title-restate card |

## Teaching arc

- **FRAMEWORK ✓** — B03 presents all three design parts as a beat, before any of
  them is explained, and stays the reel's reference figure.
- **WORKED EXAMPLE ✓** — B06 and B07 walk the Ruler archetype through that
  framework: scoring produces cited evidence, evaluation tests it against labels.
- **FALSIFIABILITY ✓** — B07 states both directions (agreement only on obvious
  words = keywords; agreement on the hard case = voice), and B10 names what does
  not exist yet.
- **SCAFFOLDED TASK ✓** — BHTF carries a real prompt plus a three-point rubric,
  which is the same auditability standard the design is built on.
- **BOOKENDS ✓** — cold open (B00), verdict (BVDT), your turn (BHTF), outro (BOUT).
- **NO-SOURCE-NO-VERDICT ✓** — every claim beat carries on-screen evidence.

## Honesty audit (the governing constraint)

- No beat shows detector output. Nothing is built.
- B06: tab "design target, not produced"; scores are `0.0` placeholders; closing
  comment `// NOT OUTPUT.`
- B07: `slideMeta` "illustrative — the test design, not a produced result".
- B02's Ruler phrases are constructed; no real brand named or quoted.
- B10 carries three deliberately negative chips.
- BVDT closes "Status: design drafted. Not built. Waiting on sample data."
- B01's correction (`built` → `designed`) puts the honesty on screen first.

## Regression guards (verified programmatically before rendering)

| Prior bug | Result |
|---|---|
| `@NikBearBrown` chip | `folderLabel` per-beat on B00/B05/BHTF — 0 missing |
| Multi-word trigger never fires | single token `built`, 1 occurrence |
| Animation truncated at ~50% | `durationInSeconds` on all 14 beats — 0 missing |
| Orphan verdict number | 0 empty `artifactLines` |
| Chip grid / caption collision | B08, B10 at `cols=3`, 5 items, two rows |
| Names that should stay generic | no personal or tool names in the sheet |

## Laws verified at authoring time

- **ILLUSTRATE LAW** — UI only at B00, B05, BVDT, BHTF, BOUT. No two adjacent beats
  share a scheme (`LayerStack` B03/B09, `ChipGrid` B08/B10, both separated).
- **ASK→RESULT LAW** — one pair: B05 → B06.
- **SPARK-LINE LAW** — every inner beat carries a `sparkLine` ≤4 words.
- **ONE ACCENT** — one terracotta moment per beat, audited in SHOTLIST.
- **SHOW-DON'T-TELL** — shows authored before narration. Body beats 45–60 words.
- **EXECUTIVE-SUMMARY LAW** — B01 is `BrutalistHesitantWriter`, `lead_silence_s: 0.8`,
  34 words, measured **11.58s** (clears the ≥9s window).
- **REUSE ONLY** — no components built or modified.

## Measured runtime (audio is the clock)

Kokoro `am_onyx`, 14 beats, **194.3s total** — inside the requested 180–200s on the
first pass, so no resizing was needed.

B00 14.08 · B01 11.58 · B02 14.12 · B03 15.87 · B04 18.56 · B05 5.70 · B06 16.23 ·
B07 16.51 · B08 14.83 · B09 15.13 · B10 13.99 · BVDT 15.42 · BHTF 19.39 · BOUT 2.86
