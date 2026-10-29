# SHOTLIST — kavya-data-agents-harness

Typed work order: one row per beat, landscape (`beat_sheet.json`) and portrait (`vertical/beat_sheet.json`).
There are no open slots. Every beat is a deterministic Remotion scene, with no pantry media and no stock or AI images.
Portrait beats are native `…916` compositions, never crops of the landscape render.

| Beat | Act | Landscape composition | Portrait composition | Status |
|---|---|---|---|---|
| B00 | ASK (required intro) | `ClaudeComposerAsk` | `ClaudeComposerAsk916` | rendered |
| B01 | BLUF | `BrutalistHesitantWriter` (+ title, 3 context cards) | `BrutalistHesitantWriter916` (4 short lines, title, name label) | rendered |
| B02 | FRAMEWORK | `HarnessParts` (new) | `HarnessParts916` (new) | rendered |
| B03 | EXAMPLE-BAD | `HarnessTerminal` (new; verbatim demo stdout) | `HarnessTerminal916` (new) | rendered |
| B04 | EXAMPLE-GOOD | `HarnessTerminal` (new; verbatim demo stdout) | `HarnessTerminal916` (new) | rendered |
| B05 | FALSIFIABILITY | `HarnessBoundaryCard` (new) | `HarnessBoundaryCard916` (new) | rendered |
| B06 | VERDICT | `ClaudeVerdictArtifact` (`lectureLayout`) | `ClaudeVerdictArtifact916` (`lectureLayout`) | rendered |
| B07 | HANDOFF | `ClaudeComposerAsk` | `ClaudeComposerAsk916` | rendered |
| B08 | OUTRO (credit + AI-voice disclosure) | `ClaudeVerdictArtifact` (`lectureLayout`) | `ClaudeVerdictArtifact916` (`lectureLayout`) | rendered |

## Toolkit changes this film needed

- **New dual-aspect scenes:** `runtime/remotion/src/scenes/HarnessParts.tsx`, `HarnessTerminal.tsx` and
  `HarnessBoundaryCard.tsx`, each registered as `<Name>` (1920×1080) and `<Name>916` (1080×1920) in
  `Root.tsx`. They render at 3840×2160 and 2160×3840 via the pipeline's `--scale=2`.
- **`ClaudeVerdictArtifact916` now honours `lectureLayout`.** It already shared the landscape schema but
  ignored that prop. The change is opt-in, so reels that don't pass the prop are unchanged.
- **Why the new scenes:** library search found nothing renderable that fills a 4K frame for these beats.
  - `SkillTeardownPipeline` and `MedhavyTwoColumnCard` use fixed pixel sizes, and the former reveals
    every box at once instead of in narration order.
  - `ShellSession` draws a fixed-size window on a black stage, which the final-frame gate failed as
    underfill and low contrast.
  - `ClaudeScienceLayerStack` is a 1280×720 composition that would be upscaled.
- **The outro is `ClaudeVerdictArtifact`, not `ClaudeTitleOutro`:** `ClaudeTitleOutro` hardcodes `@NikBearBrown`.
