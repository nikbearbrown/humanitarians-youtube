# SHOTLIST — kavya-agent-data-overreach

Typed work order: one row per beat, landscape (`beat_sheet.json`) and portrait (`vertical/beat_sheet.json`).
There are no open slots. Every beat is a deterministic Remotion scene, with no pantry media and no stock or AI images.
Portrait beats are native `…916` compositions, never crops.

| Beat | Act | Landscape composition | Portrait composition | Status |
|---|---|---|---|---|
| B00 | ASK (required intro) | `ClaudeComposerAsk` | `ClaudeComposerAsk916` | rendered |
| B01 | BLUF | `BrutalistHesitantWriter` (+ title, name label) | `BrutalistHesitantWriter916` (short lines) | rendered |
| B02 | FRAMEWORK | `HarnessParts` (frame labelled "a scoped credential") | `HarnessParts916` (labels only) | rendered |
| B03 | EXAMPLE-BAD | `HarnessTerminal` (verbatim `overreach_demo.py wide`) | `HarnessTerminal916` | rendered |
| B04 | EXAMPLE-GOOD | `HarnessTerminal` (verbatim `overreach_demo.py scoped`) | `HarnessTerminal916` | rendered |
| B05 | FALSIFIABILITY | `HarnessBoundaryCard` | `HarnessBoundaryCard916` | rendered |
| B06 | VERDICT | `ClaudeVerdictArtifact` (`lectureLayout`) | `ClaudeVerdictArtifact916` (`lectureLayout`) | rendered |
| B07 | HANDOFF | `ClaudeComposerAsk` | `ClaudeComposerAsk916` | rendered |
| B08 | OUTRO (credit + AI-voice disclosure) | `ClaudeVerdictArtifact` (`lectureLayout`) | `ClaudeVerdictArtifact916` (`lectureLayout`) | rendered |

## Notes

- **B04 omits two stdout lines on screen:** the repeated ticket line and the blank spacer. B03 shows the
  ticket. Every line that is shown is verbatim.
- **B05's on-screen items are compressed** ("other customers", "unneeded tables", "unlogged lookups") so
  they fit the card; the narration says them in full.
- **Scenes reused** from the earlier films; no new scenes were needed.
- **The outro is `ClaudeVerdictArtifact`, not `ClaudeTitleOutro`:** `ClaudeTitleOutro` hardcodes `@NikBearBrown`.
