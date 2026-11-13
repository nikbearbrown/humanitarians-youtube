# SHOTLIST — agents-use-tools

Typed work order. Every slot is filled by a registered Remotion composition;
there are no open slots and no pantry requests. Durations are measured audio.

| Beat | Composition | Lane | Dur | Status |
|---|---|---|---|---|
| B00 | `ClaudeComposerAsk` | UI bookend | 9.19s | ✅ rendered |
| B01 | `BrutalistHesitantWriter` | UI bookend (BLUF) | 8.58s + 0.8 lead | ✅ rendered |
| B02 | `AgentRuntimeFrame` (phase `wrap`) | illustration — NEW | 9.39s | ✅ rendered, QC passed |
| B03 | `AgentToolLoop` | illustration — NEW | 14.31s | ✅ rendered, QC passed |
| B04 | `ClaudeCodeBeat` | evidence (live output) | 13.21s | ✅ rendered |
| B05 | `AgentRuntimeFrame` (phase `blind`) | illustration — NEW | 9.11s | ✅ rendered, QC passed |
| B06 | `PermissionGate` | illustration — NEW | 11.43s | ✅ rendered, QC passed |
| B07 | `TypesetMath` | structured math | 12.86s | ✅ rendered |
| B08 | `ClaudeComposerAsk` | UI bookend (handoff) | 16.17s | ✅ rendered |
| B09 | `ClaudeTitleOutro` | UI bookend (outro) | 4.31s | ✅ rendered |

**Total 109.4s (1:49.4).**

## Components added to the toolkit by this reel

`AgentRuntimeFrame`, `AgentToolLoop`, `PermissionGate` — all registered in
`Root.tsx` and indexed via `./art scene-index` (687 renderable).

A fourth (`CompoundingReliability`, Manim) was planned and **cancelled**: GATE L
found the existing `TypesetMath` scene already consumes `typeset_math.py` SVG
rows, so B07 needed no new component and no LaTeX.

## Open slots

None. No pantry shopping, no human-supplied media, no slates.
