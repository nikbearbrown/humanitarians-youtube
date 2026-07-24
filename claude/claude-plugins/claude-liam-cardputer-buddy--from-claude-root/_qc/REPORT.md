# QC Report — claude-liam-cardputer-buddy

**Date:** 2026-07-18  
**Duration:** 4:02 (242.1s compiled)  
**Verdict:** PASS

## Frame audit

| Frame | Beat | Notes |
|---|---|---|
| frame_11_4s.png | B00 cold open | ClaudeComposerAsk: "Hola, Kore", command visible, 3 output lines, @HumanitariansAI |
| frame_42_1s.png | B01 layout | CardputerBuddyLayout: /flash/ tree (left, green) + LAUNCHER AUTO-DISCOVERY + CANONICAL APP TEMPLATE + push command (right), spark line |
| frame_84_6s.png | B02 scripts | CardputerBuddyScripts: 4-script list (install_apps terracotta / push green / tail / repl), PORT row, install_apps vs push callout, spark line |
| frame_140_8s.png | B05 teardown | CardputerBuddyTell: 4+4 teardown columns (4 items per side), callout visible, spark line |
| frame_189_3s.png | BVDT verdict | ClaudeVerdictArtifact: "Cardputer Buddy" heading, 6 terracotta-numbered lines |
| frame_222_0s.png | BHTF handoff | ClaudeComposerAsk: "Your Turn", timer app prompt, red flags |
| frame_240_6s.png | BOUT outro | ClaudeTitleOutro: "Cardputer Buddy" title |

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
| No excessive centering | PASS — two-column B01, stacked list B02, two-column B05 |

## Notes

- Greeting: "Hola, Kore" (rotation #33)
- New scenes: CardputerBuddyLayout.tsx (B01), CardputerBuddyScripts.tsx (B02), CardputerBuddyTell.tsx (B05)
- B01 design: /flash/ device tree (left, green) + launcher auto-discovery + template card + push command (right column)
- B02 design: 4-row script list (install_apps terracotta / push green / tail / repl) + PORT row + push distinction callout
- This skill has 4 gets-right/4 bites (not 5+5) — adjusted ITEM_H accordingly, no callout row overlap
