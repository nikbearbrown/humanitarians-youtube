# QC Report — claude-liam-build-mcpb

**Date:** 2026-07-18  
**Duration:** 5:32 (331.6s compiled)  
**Verdict:** PASS

## Frame audit

| Frame | Beat | Notes |
|---|---|---|
| frame_17_4s.png | B00 cold open | ClaudeComposerAsk: "Merhaba, Kore", command visible, 3 output lines, @HumanitariansAI |
| frame_66_7s.png | B01 anatomy | BuildMcpbAnatomy: bundle tree (left, green border) + 4 manifest sections (right, color-coded), no-auto-prefix warning callout visible, spark line |
| frame_132_7s.png | B02 pipeline | BuildMcpbPipeline: USE MCPB (green) / USE REMOTE HTTP (terracotta) two-column + 3-step Node pipeline + 3 security invariants rows, spark line |
| frame_207_0s.png | B05 teardown | BuildMcpbTell: 5+5 teardown columns, callout overlaps row 5 (accepted batch pattern), spark line |
| frame_266_1s.png | BVDT verdict | ClaudeVerdictArtifact: "Build MCPB" heading, 6 terracotta-numbered lines |
| frame_306_8s.png | BHTF handoff | ClaudeComposerAsk: "Your Turn", file reader MCPB prompt, red flags |
| frame_330_2s.png | BOUT outro | ClaudeTitleOutro: "Build MCPB" title |

## Rubric

| Check | Result |
|---|---|
| Canvas fill >65% | PASS |
| Text readable at all beats | PASS |
| Column alignment correct | PASS |
| Callout / spark line visible (B05) | PASS — callout overlaps row 5 (accepted batch pattern) |
| No Inter font | PASS |
| No purple gradient | PASS |
| No uniform rounded corners | PASS |
| No excessive centering | PASS — two-column B01, two-column B02, two-column B05 |

## Notes

- Greeting: "Merhaba, Kore" (rotation #32)
- New scenes: BuildMcpbAnatomy.tsx (B01), BuildMcpbPipeline.tsx (B02), BuildMcpbTell.tsx (B05)
- B01 design: bundle tree structure (left, green) + 4 manifest key sections (right, color-coded) + no-auto-prefix warning
- B02 design: USE MCPB / USE REMOTE HTTP gate + 3-step Node build pipeline + 3 security invariants
- Two silent failures unified in B05 callout: no auto-prefix on env vars + no sandbox
