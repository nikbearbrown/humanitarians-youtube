# SHOTLIST — Small Enough to Stay Offline

Typed work order. Eleven beats, two deliverables (16:9 and the full-length 9:16),
**no open slots**: every beat is a registered Remotion composition rendered from props
in `beat_sheet.json`, which `build_beats.py` generates. No user media, no photos,
nothing waiting on generation, purchase or approval.

| Beat | Act | Lane | Asset | Motion | In 9:16? |
|---|---|---|---|---|---|
| B00 | ASK | remotion | `ClaudeComposerAsk` | illustrate | yes → `ClaudeComposerAsk916` |
| B01 | THE MACHINES | remotion | `ClaudeScienceChipGrid` | illustrate | yes → `ClaudeScienceChipGrid916` |
| B02 | THE ARITHMETIC | remotion | `TypesetMath` | illustrate | yes → `TypesetMath916` |
| B03 | THE BITS | remotion | `BinaryBranch` | illustrate | yes → `BinaryBranch916` |
| B04 | THE RUN | remotion | `ExecutedData` | illustrate | yes → `ExecutedData916` |
| B05 | THE ENGINE | remotion | `DivergentFates` | illustrate | yes → `DivergentFates916` |
| B06 | THE BUTTONS | remotion | `BinaryBranch` | illustrate | yes → `BinaryBranch916` |
| B07 | HELP AND IT | remotion | `DivergentFates` | illustrate | yes → `DivergentFates916` |
| B08 | VERDICT | remotion | `ClaudeVerdictArtifact` | illustrate | yes → `ClaudeVerdictArtifact916` |
| B09 | HANDOFF | remotion | `ClaudeComposerAsk` | illustrate | yes → `ClaudeComposerAsk916` |
| B10 | OUTRO | remotion | `LogoOutro` | illustrate | yes → `LogoOutro916` |

All `*916` siblings are real `<Composition id=…>` registrations in `Root.tsx`
(checked with grep, 2026-10-09).

## B02 — the equation beat

`TypesetMath`: M = N·b/8, r ≤ B/M, and 200 GB/s ÷ 2.65 GB ≈ 75.5 tokens/s, worked on
the Qwen3.5 4B file's own parameter count and size (`evidence/model_facts.out`). The
composition is 450 frames (15 s) on a 21.2 s beat; reveals at 2.15 / 5.84 / 11.05 s
(the generator asserts ≤ 14.5 s).

## B04 — the evidence beat

`ExecutedData`, four rows from `evidence/local_bench.json`; reveals at 5.16 / 7.36 /
8.31 / 9.89 s on a 19.5 s beat.
