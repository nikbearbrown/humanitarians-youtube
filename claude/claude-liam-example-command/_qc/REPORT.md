# QC Report — claude-liam-example-command

**Date:** 2026-07-18  
**Duration:** 4:13 (253.3s compiled)  
**Verdict:** PASS

## Frame audit

| Frame | Beat | Notes |
|---|---|---|
| frame_010s.png | B00 cold open | ClaudeComposerAsk: "Olá, Kore", /example-command invocation, 3 output lines, @HumanitariansAI |
| frame_045s.png | B01 anatomy | ExampleCommandAnatomy: 5 frontmatter fields left + 4 skill body pattern rows right; allowed-tools terracotta |
| frame_094s.png | B02 design | ExampleCommandDesign: 2 design cards left (allowed-tools pre-approval terracotta) + 4 practical rules right |
| frame_152s.png | B05 teardown | ExampleCommandTell: callout + standard 5+5 two-column teardown, spark line with asterisk |
| frame_201s.png | BVDT verdict | ClaudeVerdictArtifact: "example-command" heading, 6 terracotta-numbered lines |
| frame_234s.png | BHTF handoff | ClaudeComposerAsk: "Your Turn", build-from-template task, expected/red-flag output |
| frame_252s.png | BOUT outro | ClaudeTitleOutro: "example-command" title |

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
| No excessive centering | PASS — two-column B01 with 5+4 rows, two-column B02 with cards+rules, two-column B05 |

## Notes

- Greeting: "Olá, Kore" (rotation #44)
- New scenes: ExampleCommandAnatomy (B01), ExampleCommandDesign (B02), ExampleCommandTell (B05)
- B01: allowed-tools row terracotta — flags the blast radius concern upfront
- B02: allowed-tools pre-approval card terracotta; name = directory name and Narrow allowed-tools rules terracotta
- B05 callout: self-referential skill — "demonstrates the format by being an example of the format"
