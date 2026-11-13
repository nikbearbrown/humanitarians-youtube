# SHOTLIST — Inside the Black Box, Part 2

Typed work order. Eight beats, two deliverables (16:9 and the full-length 9:16),
**no open slots**. Six are registered Remotion compositions; two (B01, B04) are
figure plates built by `make_plates.py` from Stephen Wolfram's figures
(CC BY-NC-SA 4.0).

| Beat | Act | Lane | Asset | Motion | In 9:16? |
|---|---|---|---|---|---|
| B00 | ASK | remotion | `ClaudeComposerAsk` | illustrate | yes → `ClaudeComposerAsk916` |
| B01 | LOOKING INSIDE | figures | `make_plates.py` · pair · 2 figures | staged reveal + 2% push | yes → `pantry/B01-916.mp4` |
| B02 | GPT-2, OPENED | remotion | `ExecutedData` | illustrate | yes → `ExecutedData916` |
| B03 | EVERY WEIGHT, COUNTED | remotion | `TypesetMath` | illustrate | yes → `TypesetMath916` |
| B04 | INSIDE GPT-2 | figures | `make_plates.py` · quad · 4 figures | staged reveal + 2% push | yes → `pantry/B04-916.mp4` |
| B05 | VERDICT | remotion | `ClaudeVerdictArtifact` | illustrate | yes → `ClaudeVerdictArtifact916` |
| B06 | HANDOFF | remotion | `ClaudeComposerAsk` | illustrate | yes → `ClaudeComposerAsk916` |
| B07 | OUTRO | remotion | `LogoOutro` | illustrate | yes → `LogoOutro916` |

## The figures (6)

| Beat | File | On-screen caption | Cue |
|---|---|---|---|
| B01 | `cat_layer1.png` | Layer 1: the cat without its background, its outline | first, 0s |
| B01 | `cat_layer10.png` | Layer 10: features with no names | "By the tenth layer" |
| B04 | `word_map.png` | Words laid out by meaning (projected to 2D) | first, 0s |
| B04 | `attention.png` | 12 attention heads, first block: where each looks back | "In the first block" |
| B04 | `weights_raw.png` | One 768 × 768 weight matrix | "Here's one of" |
| B04 | `weights_smooth.png` | Smoothed: structure, meaning unknown | "Smooth it" |

**Ordering hazard:** never edit the sheet (or run `build_beats.py`) while
`remotion_scenes.py` is rendering.
