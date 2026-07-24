# QC Report — claude-liam-datadog-api

**Date:** 2026-07-18  
**Duration:** 6:04 (364.1s compiled)  
**Verdict:** PASS

## Frame audit

| Frame | Beat | Notes |
|---|---|---|
| frame_018s.png | B00 cold open | ClaudeComposerAsk: "Bonjour, Liam", Datadog search query, 3 output lines, @NikBearBrown |
| frame_074s.png | B01 anatomy | DatadogApiAnatomy: v1 + v2 resource cards (green) + 4 setup requirement rows (DD-API-KEY, DD-APPLICATION-KEY, DD_SITE, curl -g) |
| frame_155s.png | B02 design | DatadogApiDesign: 3 pagination rows left + 3 JSON:API gotcha rows right (all terracotta) |
| frame_238s.png | B05 teardown | DatadogApiTell: callout + standard 5+5 two-column teardown, spark line with asterisk |
| frame_299s.png | BVDT verdict | ClaudeVerdictArtifact: "Datadog API" heading, 6 terracotta-numbered lines |
| frame_340s.png | BHTF handoff | ClaudeComposerAsk: "Your Turn", service:web prompt, expected/red-flag output |
| frame_362s.png | BOUT outro | ClaudeTitleOutro: "Datadog API" title |

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
| No excessive centering | PASS — two-column B01 with setup rows, two-column B02, two-column B05 |

## Notes

- Greeting: "Bonjour, Liam" (rotation #41)
- New scenes: DatadogApiAnatomy (B01), DatadogApiDesign (B02), DatadogApiTell (B05)
- B01: v1/v2 both green (neither is "legacy"); setup rows warn terracotta for DD-API-KEY, DD_SITE, curl -g
- B02: all JSON:API gotcha rows terracotta; offset/bracketed pagination row also terracotta for globoff
- B05 callout: spans vs logs JSON:API envelope asymmetry — "malformed body" 400 without naming the missing field
