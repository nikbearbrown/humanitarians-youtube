# QC Report — claude-liam-command-development

**Date:** 2026-07-18  
**Duration:** 5:33 (332.5s compiled)  
**Verdict:** PASS

## Frame audit

| Frame | Beat | Notes |
|---|---|---|
| frame_13_9s.png | B00 cold open | ClaudeComposerAsk: "Hej, Kore", create slash command, 3 output lines, @HumanitariansAI |
| frame_60_4s.png | B01 anatomy | CommandDevAnatomy: 3-location column (left) + 5-field column (right) + 4-argument row (bottom), spark line |
| frame_130_6s.png | B02 content | CommandDevContent: instructions-rule framing + 4 pattern cards |
| frame_207_8s.png | B05 teardown | CommandDevTell: standard teardown layout with gets-right/bites columns + callout, spark line |
| frame_268_5s.png | BVDT verdict | ClaudeVerdictArtifact: "Command Development" heading, 6 terracotta-numbered lines |
| frame_309_4s.png | BHTF handoff | ClaudeComposerAsk: "Your Turn", review-pr command task, red flags |
| frame_330_9s.png | BOUT outro | ClaudeTitleOutro: "Command Development" title |

## Rubric

| Check | Result |
|---|---|
| Canvas fill >65% | PASS |
| Text readable at all beats | PASS |
| Column alignment correct | PASS |
| Callout / spark line visible (B05) | PASS |
| No Inter font | PASS |
| No purple gradient | PASS |
| No uniform rounded corners | PASS |
| No excessive centering | PASS — two-column B01, card grid B02, two-column B05 |

## Notes

- Greeting: "Hej, Kore" (rotation #37)
- Reused existing scenes: CommandDevAnatomy (B01), CommandDevContent (B02), CommandDevTell (B05) — same skill content as claude-code #19
- Different narration and greeting from the claude-code version; same visual frames
