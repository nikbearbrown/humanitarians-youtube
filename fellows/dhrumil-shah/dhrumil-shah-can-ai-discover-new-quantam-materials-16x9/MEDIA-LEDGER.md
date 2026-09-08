# MEDIA LEDGER — can-ai-discover-new-quantum-materials-16x9

Generated: 2026-09-01
Composition: `src/CanAIDiscoverQuantumMaterials.tsx`
Master: `output/can-ai-discover-new-quantum-materials-4k.mp4`

## Classification

Every beat in this film is a **CLAUDE-GENERATED VISUAL** — produced from code
and structured props inside the Remotion composition. There is no human-supplied
media, no third-party asset, and no captured screenshot anywhere in the reel.

The human-media ownership rules and SHA-256 preservation requirements therefore
do not apply to any beat.

## Beat classification table

| Beat | Scene | Shot type | Generating component | Audio | Notes |
|---|---|---|---|---|---|
| B00 | 01 | CARD | `OpeningScene` | `mp3/beat-B00.mp3` | Title, thesis card, five-token pipeline |
| B01 | 02 | GRAPHIC | `ProblemFrameworkScene` → `TcChart` | `mp3/beat-B01.mp3` | Computed scatter of published measured Tc values |
| B02 | 02 | CARD | `ProblemFrameworkScene` | `mp3/beat-B02.mp3` | Five CLAIM cards, presenter-labelled |
| B03 | 03 | CARD | `DataScene` | `mp3/beat-B03.mp3` | Full bibliographic citation card + 2×2 stats |
| B04 | 03 | CARD | `DataScene` | `mp3/beat-B04.mp3` | Feature chips + NOT-IN-THE-TABLE column |
| B05 | 04 | GRAPHIC | `MethodScene` | `mp3/beat-B05.mp3` | RMSE stat — **carries the VERIFY-flagged figure** |
| B06 | 04 | CARD | `MethodScene` | `mp3/beat-B06.mp3` | Interpolation reframe |
| B07 | 05 | GRAPHIC | `FunnelScene` | `mp3/beat-B07.mp3` | Proportional funnel bars |
| B08 | 05 | CARD | `FunnelScene` | `mp3/beat-B08.mp3` | Illustrative-schematic disclosure |
| B08b | 06 | CARD | `LimitScene` | `mp3/beat-B08b.mp3` | Inside/outside distribution + two dated discoveries |
| B09 | 07 | GRAPHIC | `ChainScene` | `mp3/beat-B09.mp3` | Five-link confirmation chain |
| B10 | 07 | CARD | `ChainScene` | `mp3/beat-B10.mp3` | Human-boundary rule |
| B11 | 08 | CARD | `TestCaseScene` | `mp3/beat-B11.mp3` | LK-99 claimed column |
| B12 | 08 | CARD | `TestCaseScene` | `mp3/beat-B12.mp3` | LK-99 replication column (side-by-side) |
| B12b | 09 | GRAPHIC | `ScoringScene` | `mp3/beat-B12b.mp3` | CLAIM rubric scored against LK-99 |
| B13 | 10 | CARD | `CloseScene` | `mp3/beat-B13.mp3` | Viewer scaffold + title close |

16 beats, 16 unique IDs, 0 slates, 0 pantry slots.

## Beat-ID integrity

Every `beat_id` in this film is unique. This is stated explicitly because the
`claude-for-physics` collection — whose documentation conventions this project
follows — carries a duplicate `B00` in all six of its beat sheets, where a
later greeting beat reused the identifier already held by the cold-open ask.
Because `timings.json`, `todo.json`, and rendered media filenames are all keyed
by `beat_id`, that collision silently overwrites data.

This film's `UNIQUE-ID LAW` (recorded in `beat_sheet.json` metadata) exists to
prevent the same defect. It is verifiable:

```bash
python -c "import json;b=[x['beat_id'] for x in json.load(open('beat_sheet.json'))['beats']];print(len(b),len(set(b)))"
```

Both numbers must be 16.

## Audio

| Property | Value |
|---|---|
| Engine | Kokoro-82M via kokoro-onnx, run locally |
| Voice | `am_onyx` (house default) |
| Generator | `runtime/scripts/generate_audio_kokoro.py` |
| Model files | `runtime/models/kokoro/kokoro-v1.0.onnx`, `voices-v1.0.bin` |
| Cost | $0.00 — no account, no API |
| Measured total | 179.44 s |
| Master duration | 180.011 s (includes a 0.58 s silent title hold) |

Durations in `mp3/timings.json` are ground truth. The composition's
`AUDIO_BEATS` table mirrors them exactly; if audio is regenerated and any
duration changes, that table must be updated to match. Timing is never
corrected by hand.

## Defects found and fixed before the master

| # | Beat | Defect | Resolution |
|---|---|---|---|
| 1 | B01 | The `LaH10` and `H3S` point labels on the Tc chart collided with the 293 K room-temperature line and with each other; one label was clipped at the plot edge. | Point labels removed for the two high-pressure records; their values moved to a dedicated accent callout in the plot's empty upper-left. Re-inspected. |
| 2 | B07 | The two narrowest funnel bars were too small for their labels — "Screened for synthesizability" and "Shortlist for the laboratory" overflowed their cards and collided with the note column. | Layout restructured: the label now lives in a fixed-width column and the bar is a pure proportional block. Text can no longer overflow a bar because text is no longer inside one. Re-inspected. |

Both were caught by rendering and **looking at** stills before the master, per
the workspace rule that renders are verified by frame inspection rather than by
probe output alone.
