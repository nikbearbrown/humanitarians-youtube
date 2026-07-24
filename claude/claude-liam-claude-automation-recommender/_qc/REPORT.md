# QC Report — claude-liam-claude-automation-recommender

**Date:** 2026-07-18  
**Duration:** 5:06 (306.1s compiled)  
**Verdict:** PASS

## Frame audit

| Frame | Beat | Notes |
|---|---|---|
| frame_16_2s.png | B00 cold open | ClaudeComposerAsk: "Bonjour, Kore", command visible, 3 output lines, @HumanitariansAI |
| frame_60_9s.png | B01 five types | AutomationRecommenderTypes: 5-type rows (Hooks/Subagents/Skills/Plugins/MCP Servers), invocation control 3 rows, spark line |
| frame_118_3s.png | B02 workflow | AutomationRecommenderSignals: 3-phase cards (Analyze/Generate/Output) + 5 signal→rec examples, spark line |
| frame_187_4s.png | B05 teardown | AutomationRecommenderTell: 5+5 two-column teardown, callout overlaps row 5 (accepted batch pattern), spark line |
| frame_245_2s.png | BVDT verdict | ClaudeVerdictArtifact: "Claude Automation Recommender" heading, 6 terracotta-numbered lines |
| frame_282_6s.png | BHTF handoff | ClaudeComposerAsk: "Your Turn", React TypeScript prompt, red flags |
| frame_304_2s.png | BOUT outro | ClaudeTitleOutro: "Claude Automation Recommender" title |

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
| No excessive centering | PASS — full-width rows B01/B02, two-column B05 |

## Notes

- Greeting: "Bonjour, Kore" (rotation #34)
- New scenes: AutomationRecommenderTypes.tsx (B01), AutomationRecommenderSignals.tsx (B02), AutomationRecommenderTell.tsx (B05)
- B01 design: 5-type rows with name/trigger/use columns + invocation control table (3 rows)
- B02 design: 3-phase workflow cards + 5 signal→recommendation example rows
- B05 standard 5+5 teardown; callout overlapping row 5 is established batch pattern (same as build-mcp-app, build-mcp-server, build-mcpb)
