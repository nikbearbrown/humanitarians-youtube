# SHOTLIST — The Model Didn't Change. The World Did.

Typed work order. Nine beats, two deliverables (16:9 and the full-length 9:16),
**no open slots**: every beat is a registered Remotion composition rendered from
props in `beat_sheet.json`, which `build_beats.py` generates. No user media, no
photos, nothing waiting on generation, purchase or approval.

| Beat | Act | Lane | Asset | Motion | In 9:16? |
|---|---|---|---|---|---|
| B00 | ASK | remotion | `ClaudeComposerAsk` | illustrate | yes → `ClaudeComposerAsk916` |
| B01 | THE WORD | remotion | `ClaudeScienceChipGrid` | illustrate | yes → `ClaudeScienceChipGrid916` |
| B02 | THE DECAY | remotion | `ExecutedData` | illustrate | yes → `ExecutedData916` |
| B03 | THE NAMES | remotion | `TypesetMath` | illustrate | yes → `TypesetMath916` |
| B04 | THE ALARM | remotion | `BinaryBranch` | illustrate | yes → `BinaryBranch916` |
| B05 | THE FIX? | remotion | `DivergentFates` | illustrate | yes → `DivergentFates916` |
| B06 | VERDICT | remotion | `ClaudeVerdictArtifact` | illustrate | yes → `ClaudeVerdictArtifact916` |
| B07 | HANDOFF | remotion | `ClaudeComposerAsk` | illustrate | yes → `ClaudeComposerAsk916` |
| B08 | OUTRO | remotion | `LogoOutro` | illustrate | yes → `LogoOutro916` |

All `*916` siblings are real `<Composition id=…>` registrations in `Root.tsx`
(checked with grep).

## B02 — the evidence beat

`ExecutedData`, four rows from `evidence/drift_run.csv`. The composition is
450 frames (15 s) on a 17.7 s beat, so every reveal is cued to land by 14.3 s
(the generator asserts ≤ 14.5 s).

## B03 — the equation beat

`TypesetMath`: covariate shift, concept drift (after Huyen, 2022), and the KS
statistic as computed in the run. Algebra and figures asserted by
`build_beats.py --check`.
