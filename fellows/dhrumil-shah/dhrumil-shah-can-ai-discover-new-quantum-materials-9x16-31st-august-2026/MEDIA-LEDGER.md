# MEDIA LEDGER — Can-AI-discover-new-quantum-materials-9x16

Generated: 2026-09-01
Composition: `src/CanAIDiscoverQuantumMaterials9x16.tsx`
Canvas: 2160 × 3840 (9:16 portrait)
Master: `output/Can-AI-discover-new-quantum-materials-4k(9x16)_Dhrumil_Shah.mp4`

## Classification

Every beat is a **CLAUDE-GENERATED VISUAL** — produced from code and
structured props inside the Remotion composition. There is no human-supplied
media, no third-party asset, and no captured screenshot anywhere in the reel.

The human-media ownership rules and SHA-256 preservation requirements
therefore do not apply to any beat.

## Beat classification table

| Beat | Scene | Shot type | Generating component | Audio | Portrait note |
|---|---|---|---|---|---|
| B00 | 01 | CARD | `OpeningScene` | reused `beat-B00.mp3` | Pipeline restacked vertically with down-arrows |
| B01 | 02 | GRAPHIC | `ProblemFrameworkScene` → `TcChart` | reused `beat-B01.mp3` | Chart 860 px tall; YBCO label left-anchored |
| B02 | 02 | CARD | `ProblemFrameworkScene` | reused `beat-B02.mp3` | CLAIM as a 3+2 grid |
| B03 | 03 | CARD | `DataScene` | reused `beat-B03.mp3` | Citation full width above the stat grid |
| B04 | 03 | CARD | `DataScene` | reused `beat-B04.mp3` | Features and exclusions stacked |
| B05 | 04 | GRAPHIC | `MethodScene` | reused `beat-B05.mp3` | RMSE at 200 px — **carries the VERIFY-flagged figure** |
| B06 | 04 | CARD | `MethodScene` | reused `beat-B06.mp3` | Interpolation reframe |
| B07 | 05 | GRAPHIC | `FunnelScene` | reused `beat-B07.mp3` | Bar max width 880 px; note beneath the label |
| B08 | 05 | CARD | `FunnelScene` | reused `beat-B08.mp3` | Illustrative-schematic disclosure |
| B08b | 06 | CARD | `LimitScene` | reused `beat-B08b.mp3` | Both pairs stacked |
| B09 | 07 | GRAPHIC | `ChainScene` | reused `beat-B09.mp3` | Chain vertical with down-arrows |
| B10 | 07 | CARD | `ChainScene` | reused `beat-B10.mp3` | Boundary labels around a full-width rule |
| B11 | 08 | CARD | `TestCaseScene` | reused `beat-B11.mp3` | Claimed panel, upper half |
| B12 | 08 | CARD | `TestCaseScene` | reused `beat-B12.mp3` | Replication panel, lower half — held with B11 |
| B12b | 09 | GRAPHIC | `ScoringScene` | reused `beat-B12b.mp3` | Justification beneath each axis name |
| B13 | 10 | CARD | `CloseScene` | reused `beat-B13.mp3` | Scaffold + centred title close |

16 beats, 16 unique IDs, 0 slates, 0 pantry slots.

## Beat-ID integrity

Every `beat_id` is unique. Verifiable:

```bash
python -c "import json;b=[x['beat_id'] for x in json.load(open('beat_sheet.json'))['beats']];print(len(b),len(set(b)))"
```

Both numbers must be 16.

## Audio — reused, not duplicated

| Property | Value |
|---|---|
| Engine | Kokoro-82M via kokoro-onnx, run locally |
| Voice | `am_onyx` |
| Source | `../Can-AI-discover-new-quantum-materials-16x9/mp3/` |
| Copies in this folder | **none — deliberately** |
| Measured total | 179.44 s |
| Master duration | 180.011 s (includes a 0.58 s silent title hold) |

There is no `mp3/` directory in this project. Two copies of the same narration
are two things that can drift apart; the sync script reads the approved 16:9
originals directly and fails loudly if they are missing.

If that audio is ever regenerated and any duration changes, the `AUDIO_BEATS`
table in **both** compositions must be updated to match. The audio is the
clock in both cuts.

## Defects found and fixed before this master

| # | Beat | Defect | Resolution |
|---|---|---|---|
| 1 | B01 | Portrait narrows the plot, which pushed the centred `YBCO 92K` label underneath the unlabelled BSCCO point at 110 K. | Added per-point label anchoring to `TC_DATA`; YBCO is now left-anchored clear of the neighbour. Re-inspected in preflight and in the master. |
| 2 | B01/B02 | Scene 02 was bottom-light — roughly 850 px of dead space between the CLAIM grid and the source plate. | Chart height raised 700 → 860 px and the framework block moved down. |
| 3 | all scenes | **Systemic:** every scene was pinned to fixed tops estimated for a shorter canvas, so content occupied roughly the top 40 % of the 3840 px column and the dead band above the source plate read as an unfinished frame rather than as margin. Scene 09 was the worst — its rubric card ended at y≈1520 with the footer line stranded at y≈2580. | Introduced a `ContentColumn` primitive that centres each scene's content between the headline and the source plate. Opacity-gated children still occupy their space, so nothing shifts when a later block fades in. Scene 09's rows were additionally scaled up (circle 86→112 px, name 46→58 px, verdict chip 230→292 px) to suit the portrait column. Verified against the house `mycroft-thesisguard-9x16` framing. |

All three were caught by rendering stills and **looking at them** — the first
two in preflight, the third by inspecting the QC stills of a completed master
and re-rendering. None is visible to a format probe.

## Inherited defects already fixed upstream

The two defects found in the 16:9 cut — colliding high-pressure chart labels
and funnel bars narrower than their own labels — do not recur here. The
portrait composition inherits both fixes by construction: high-pressure values
live in a callout, and the funnel label sits in its own column rather than
inside the bar.
