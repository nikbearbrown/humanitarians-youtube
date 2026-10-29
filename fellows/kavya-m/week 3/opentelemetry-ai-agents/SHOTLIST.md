# SHOTLIST — kavya-opentelemetry-ai-agents

Typed work order: one row per beat, landscape (`beat_sheet.json`) and portrait (`vertical/beat_sheet.json`).
There are no open slots. Every beat is a deterministic Remotion scene, with no pantry media and no stock or AI images.
Portrait beats are native `…916` compositions, never crops.

| Beat | Act | Landscape composition | Portrait composition | Status |
|---|---|---|---|---|
| B00 | ASK (required intro) | `ClaudeComposerAsk` | `ClaudeComposerAsk916` | rendered |
| B01 | BLUF | `BrutalistHesitantWriter` (+ title, name label) | `BrutalistHesitantWriter916` (short lines) | rendered |
| B02 | FRAMEWORK | `HarnessParts` (frame labelled "a trace") | `HarnessParts916` (labels only) | rendered |
| B03 | EXAMPLE-BAD | `HarnessTerminal` (verbatim `otel_demo.py log`) | `HarnessTerminal916` | rendered |
| B04 | EXAMPLE-GOOD | `HarnessTerminal` (verbatim `otel_demo.py trace`, span tree) | `HarnessTerminal916` | rendered |
| B05 | FALSIFIABILITY | `HarnessBoundaryCard` | `HarnessBoundaryCard916` | rendered |
| B06 | VERDICT | `ClaudeVerdictArtifact` (`lectureLayout`) | `ClaudeVerdictArtifact916` (`lectureLayout`) | rendered |
| B07 | HANDOFF | `ClaudeComposerAsk` | `ClaudeComposerAsk916` | rendered |
| B08 | OUTRO (credit + AI-voice disclosure) | `ClaudeVerdictArtifact` (`lectureLayout`) | `ClaudeVerdictArtifact916` (`lectureLayout`) | rendered |

## Notes

- **B04 omits two stdout lines on screen:** the repeated `question:` line and the blank spacer, so the
  span tree fits the window. Every line that is shown is verbatim. The full output is in
  `demo/otel_demo_output.txt`, and B03 shows the question.
- **Scenes reused** from the earlier films: `HarnessParts`, `HarnessTerminal` and `HarnessBoundaryCard`. No new scenes were needed.
- **The outro is `ClaudeVerdictArtifact`, not `ClaudeTitleOutro`:** `ClaudeTitleOutro` hardcodes `@NikBearBrown`.
