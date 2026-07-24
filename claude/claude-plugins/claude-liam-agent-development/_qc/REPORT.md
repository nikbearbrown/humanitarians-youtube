# QC Report — claude-liam-agent-development

**Date:** 2026-07-18  
**Duration:** 5:17 (317s compiled)  
**Verdict:** PASS

## Frame audit

| Frame | Beat | Notes |
|---|---|---|
| frame_19s.png | B00 cold open | ClaudeComposerAsk: greeting "Konnichiwa, Liam", topic/command/output visible, @NikBearBrown folder label, terracotta asterisk |
| frame_68s.png | B01 anatomy | AgentDevAnatomy: two-column (YAML frontmatter / system prompt body), description row highlighted terracotta, spark line visible |
| frame_127s.png | B02 trigger design | AgentDevTriggerProse: Location 1 (terracotta, description format) + Location 2 (green, When to invoke), system prompt structure row, spark line "Prose in description. Prose in body." |
| frame_195s.png | B05 teardown | AgentDevTell2: 5 gets-right (green) + 5 bites (terracotta), callout box at bottom spanning columns, spark line "Two-location trigger docs readable. Maintenance coupling: consolidate." |
| frame_250s.png | BVDT verdict | ClaudeVerdictArtifact: card centered, 6 artifact lines, terracotta bullet numbers, "Agent Development (Prose Triggers)" heading |
| frame_291s.png | BHTF handoff | ClaudeComposerAsk: "Your Turn" greeting, handoff command, red-flag output lines |
| frame_315s.png | BOUT outro | ClaudeTitleOutro: "Agent Development." centered, @NikBearBrown, subline "agent-development · Plugin Dev" |

## Rubric

| Check | Result |
|---|---|
| Canvas fill >65% | PASS |
| Text readable at all beats | PASS |
| Column alignment correct | PASS |
| Callout / spark line visible (B05) | PASS — callout partially overlaps row 5, both readable (accepted pattern) |
| No Inter font | PASS |
| No purple gradient | PASS — cream PAGE background throughout |
| No uniform rounded corners | PASS — varied border styles |
| No excessive centering | PASS — two-column B05, two-box B02 |

## Notes

- Greeting: "Konnichiwa, Liam" (rotation #27)
- Reused AgentDevAnatomy for B01 (anatomy scene identical to claude-code version)
- New scenes: AgentDevTriggerProse.tsx (B02), AgentDevTell2.tsx (B05)
- B05 callout overlap with row 5 at H*0.40 COL_TOP — cosmetic only, accepted batch-wide
- Pedagogical focus: two-location trigger approach vs single-location `<example>` XML in claude-code version
