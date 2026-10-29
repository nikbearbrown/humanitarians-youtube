# SHOTLIST — kavya-ai-junk-data-gate

Typed work order: one row per beat, landscape (`beat_sheet.json`) and portrait (`vertical/beat_sheet.json`).
There are no open slots. Every beat is a deterministic Remotion scene, with no stock or AI images.
Portrait beats are native `…916` compositions, never crops.

| Beat | Act | Landscape composition | Portrait composition | Status |
|---|---|---|---|---|
| B00 | ASK (required intro) | `ClaudeComposerAsk` | `ClaudeComposerAsk916` | rendered |
| B01 | BLUF | `BrutalistHesitantWriter` (title, name label) | `BrutalistHesitantWriter916` (short lines) | rendered |
| B02 | FRAMEWORK | `HarnessParts` (frame labelled "a validation gate") | `HarnessParts916` (labels only) | rendered |
| B03 | EXAMPLE-BAD | `HarnessTerminal` (verbatim `junk_gate_demo.py ungated`) | `HarnessTerminal916` | rendered |
| B04 | EXAMPLE-GOOD | `HarnessTerminal` (verbatim `junk_gate_demo.py gated`) | `HarnessTerminal916` | rendered |
| B05 | FALSIFIABILITY | `HarnessBoundaryCard` | `HarnessBoundaryCard916` | rendered |
| B06 | VERDICT | `ClaudeVerdictArtifact` (`lectureLayout`) | `ClaudeVerdictArtifact916` (`lectureLayout`) | rendered |
| B07 | HANDOFF | `ClaudeComposerAsk` | `ClaudeComposerAsk916` | rendered |
| B08 | OUTRO (credit + AI-voice disclosure) | `ClaudeVerdictArtifact` (`lectureLayout`) | `ClaudeVerdictArtifact916` (`lectureLayout`) | rendered |

B04 omits one stdout line on screen: the repeated "gate checks data properties" line, which B03 already
shows. Every line that is shown is verbatim.
