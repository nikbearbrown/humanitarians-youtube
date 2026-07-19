# QC Report — claude-liam-asana-api

**Date:** 2026-07-18  
**Duration:** 4:39 (279.5s compiled)  
**Verdict:** PASS

## Frame audit

| Frame | Beat | Notes |
|---|---|---|
| frame_16s.png | B00 cold open | ClaudeComposerAsk: "Hola, Liam" greeting, command/output visible, @NikBearBrown, terracotta asterisk |
| frame_51s.png | B01 hierarchy | AsanaApiAnatomy: two-column (hierarchy / three rules), task row highlighted terracotta, three numbered rules (gid/data/opt_fields) green/terracotta/INK_SOFT, spark line visible |
| frame_97s.png | B02 operations | AsanaApiOps: 5×2 grid of 10 operations, search (#06) terracotta premium-highlighted, spark line visible |
| frame_162s.png | B05 teardown | AsanaApiTell: 5 gets-right (green) + 5 bites (terracotta), callout with spark SVG icon, spark line at bottom |
| frame_221s.png | BVDT verdict | ClaudeVerdictArtifact: card with "Asana API" heading, 6 terracotta-numbered artifact lines |
| frame_259s.png | BHTF handoff | ClaudeComposerAsk: "Your Turn", cross-workspace task query, red-flag output lines |
| frame_278s.png | BOUT outro | ClaudeTitleOutro: "Asana API." title, @NikBearBrown, subline |

## Rubric

| Check | Result |
|---|---|
| Canvas fill >65% | PASS |
| Text readable at all beats | PASS |
| Column alignment correct | PASS |
| Callout / spark line visible (B05) | PASS — callout overlaps row 5 (accepted batch pattern), both readable |
| No Inter font | PASS |
| No purple gradient | PASS — cream PAGE throughout |
| No uniform rounded corners | PASS — varied border-left styles |
| No excessive centering | PASS — two-column B01, 5×2 grid B02, two-column B05 |

## Notes

- Greeting: "Hola, Liam" (rotation #28)
- New scenes: AsanaApiAnatomy.tsx (B01), AsanaApiOps.tsx (B02), AsanaApiTell.tsx (B05)
- Op #06 search highlighted with terracotta background to signal premium/limitation
- B05 callout overlap with row 5 — cosmetic only, accepted batch-wide
