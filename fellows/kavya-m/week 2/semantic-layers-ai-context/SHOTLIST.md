# SHOTLIST — kavya-semantic-layers-ai-context

Typed work order: one row per beat, landscape (`beat_sheet.json`) and portrait (`vertical/beat_sheet.json`).
There are no open slots. Every beat is a deterministic Remotion scene, with no pantry media and no stock or AI images.
Portrait beats are native `…916` compositions, never crops.

| Beat | Act | Landscape composition | Portrait composition | Status |
|---|---|---|---|---|
| B00 | ASK (required intro) | `ClaudeComposerAsk` | `ClaudeComposerAsk916` | rendered |
| B01 | BLUF | `BrutalistHesitantWriter` (+ title, 3 context cards) | `BrutalistHesitantWriter916` (short lines, title, name label) | rendered |
| B02 | FRAMEWORK | `HarnessParts` (frame labelled "the semantic layer") | `HarnessParts916` | rendered |
| B03 | EXAMPLE-BAD | `HarnessTerminal` (verbatim `semantic_demo.py raw`) | `HarnessTerminal916` | rendered |
| B04 | EXAMPLE-GOOD | `HarnessTerminal` (verbatim `semantic_demo.py layer`) | `HarnessTerminal916` | rendered |
| B05 | FALSIFIABILITY | `HarnessBoundaryCard` | `HarnessBoundaryCard916` | rendered |
| B06 | VERDICT | `ClaudeVerdictArtifact` (`lectureLayout`) | `ClaudeVerdictArtifact916` (`lectureLayout`) | rendered |
| B07 | HANDOFF | `ClaudeComposerAsk` | `ClaudeComposerAsk916` | rendered |
| B08 | OUTRO (credit + AI-voice disclosure) | `ClaudeVerdictArtifact` (`lectureLayout`) | `ClaudeVerdictArtifact916` (`lectureLayout`) | rendered |

## Notes

- **Scenes reused** from `kavya-data-agents-harness`: `HarnessParts`, `HarnessTerminal` and `HarnessBoundaryCard`.
  Their names are historical; all labels are props.
- **Toolkit change this film needed:** those three scenes now accept `durationSeconds`, and `Root.tsx`
  sizes the composition to it with `calculateMetadata`, so reveals map to the real narration length.
  Without the prop the old fixed lengths apply.
- **The outro is `ClaudeVerdictArtifact`, not `ClaudeTitleOutro`:** `ClaudeTitleOutro` hardcodes `@NikBearBrown`.
