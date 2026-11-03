# SHOTLIST — Seals Pass, Seabirds Wait

Typed work order. Eleven beats, two deliverables (16:9 and the full-length
9:16), **no open slots**. Nine beats are registered Remotion compositions; two
(B04, B06) are photo plates built by `make_plates.py` from freely licensed
Wikimedia Commons photographs. Nothing is generated, purchased or awaiting a key.

| Beat | Act | Lane | Asset | Motion | In 9:16? |
|---|---|---|---|---|---|
| B00 | ASK | remotion | `ClaudeComposerAsk` | illustrate | yes → `ClaudeComposerAsk916` |
| B01 | FOUR QUESTIONS | remotion | `ClaudeScienceChipGrid` | illustrate | yes → `ClaudeScienceChipGrid916` |
| B02 | WHERE NOT TO BUILD | remotion | `BinaryBranch` | illustrate | yes → `BinaryBranch916` |
| B03 | WHAT DEMAND LOOKS LIKE | remotion | `TypesetMath` | illustrate | yes → `TypesetMath916` |
| B04 | MAINE'S SEABIRDS | archival photos | `make_plates.py` · grid2x2 · 4 photos | staged reveal + 2% push | yes → `pantry/B04-916.mp4` (re-composed) |
| B05 | THE DATA QUESTION, MEASURED | remotion | `ExecutedData` | illustrate | yes → `ExecutedData916` |
| B06 | SEALS PASS | archival photos | `make_plates.py` · hero+2 · 3 photos | staged reveal + 2% push | yes → `pantry/B06-916.mp4` (re-composed) |
| B07 | THE RANKING | remotion | `DivergentFates` | illustrate | yes → `DivergentFates916` |
| B08 | VERDICT | remotion | `ClaudeVerdictArtifact` | illustrate | yes → `ClaudeVerdictArtifact916` |
| B09 | HANDOFF | remotion | `ClaudeComposerAsk` | illustrate | yes → `ClaudeComposerAsk916` |
| B10 | OUTRO | remotion | `LogoOutro` | illustrate | yes → `LogoOutro916` |

## The photographs (7)

Fetched by `evidence/commons_fetch.py`, which refuses anything that is not
public domain, CC0, CC BY or CC BY-SA and writes a sidecar
(`images/src/<slug>.json`: title, page, licence, author, sha256, fetch time).

| Beat | File | Caption | Licence | Reveal cue |
|---|---|---|---|---|
| B04 | `counting_dots.jpg` | What observers count — every dot is a bird | Public domain (USFWS) | first, 0s |
| B04 | `herring_gull.jpg` | Herring gull — 53% of Maine's labels | CC BY-SA 4.0 (Rhododendrites) | "herring gulls" |
| B04 | `eider_maine.jpg` | Common eider — 15% of the labels | CC0 (Alan Schmierer) | "eiders" |
| B04 | `cormorant_colony.jpg` | Double-crested cormorant — 13% of the labels | Public domain (USFWS) | "cormorants" |
| B06 | `seal_aerial.jpg` | Harbor seals hauled out on ice, seen from the air | Public domain (NPS) | first, 0s |
| B06 | `ringed_seal.jpg` | Ringed seal — 80% of NOAA's boxed seals | CC0 (Estormiz) | "mostly ringed seals" |
| B06 | `seal_parker.jpg` | Harbor seals hauled out — Massachusetts | Public domain (USFWS) | "hauled out on rocks" |

No photograph is retouched, recoloured, generated or composited; each is
cover-cropped into its cell at a focus point chosen by looking. Colour is kept
(`shot.treatment: "none"`).

**Ordering hazard:** `remotion_scenes.py` writes its start-of-run copy of
`beat_sheet.json` back after every render. Never edit the sheet (or run
`build_beats.py`) while a render is in flight.
