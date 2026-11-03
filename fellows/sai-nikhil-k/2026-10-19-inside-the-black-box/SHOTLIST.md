# SHOTLIST — Inside the Black Box, Part 1

Typed work order. Nine beats, two deliverables (16:9 and the full-length 9:16),
**no open slots**. Seven are registered Remotion compositions; two (B01, B03)
are figure plates built by `make_plates.py` from Stephen Wolfram's figures
(CC BY-NC-SA 4.0).

| Beat | Act | Lane | Asset | Motion | In 9:16? |
|---|---|---|---|---|---|
| B00 | ASK | remotion | `ClaudeComposerAsk` | illustrate | yes → `ClaudeComposerAsk916` |
| B01 | SIMPLE PARTS | figures | `make_plates.py` · left+2 · 3 figures | staged reveal + 2% push | yes → `pantry/B01-916.mp4` |
| B02 | ONE NEURON | remotion | `TypesetMath` | illustrate | yes → `TypesetMath916` |
| B03 | LEARNED, NOT WRITTEN | figures | `make_plates.py` · hero+strip · 3 figures | staged reveal + 2% push | yes → `pantry/B03-916.mp4` |
| B04 | WHICH NET IS RIGHT? | remotion | `BinaryBranch` | illustrate | yes → `BinaryBranch916` |
| B05 | TEN NETS, TRAINED HERE | remotion | `ExecutedData` | illustrate | yes → `ExecutedData916` |
| B06 | VERDICT | remotion | `ClaudeVerdictArtifact` | illustrate | yes → `ClaudeVerdictArtifact916` |
| B07 | HANDOFF | remotion | `ClaudeComposerAsk` | illustrate | yes → `ClaudeComposerAsk916` |
| B08 | OUTRO | remotion | `LogoOutro` | illustrate | yes → `LogoOutro916` |

## The figures (6)

| Beat | File | On-screen caption | Cue |
|---|---|---|---|
| B01 | `neuron_net.png` | A small net: every neuron weighs its inputs | first, 0s |
| B01 | `activations.png` | The simple function each neuron applies | "through a simple function" |
| B01 | `net_formula.png` | The whole tiny net, written out as one formula | "Write out everything" |
| B03 | `descent.png` | Downhill on the error: two starts, two different lakes | first, 0s |
| B03 | `examples.png` | 10,000 to 10,000,000 examples for one shape | "Even this toy net" |
| B03 | `extrapolate.png` | Four nets, same examples (white): different guesses beyond them | "And train it twice" |

Each figure is scaled whole (≤ 2.2×) and multiplied onto the cream; the credit
line is at the foot of every plate.

**Ordering hazard:** never edit the sheet (or run `build_beats.py`) while
`remotion_scenes.py` is rendering.
