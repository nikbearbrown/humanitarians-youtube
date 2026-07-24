# QC Report — claude-liam-enterprise-search

**Date:** 2026-07-18  
**Duration:** 5:04 (304.6s compiled)  
**Verdict:** PASS

## Frame audit

| Frame | Beat | Notes |
|---|---|---|
| frame_013s.png | B00 cold open | ClaudeComposerAsk: "Hej, Kore", contractor onboarding query, 3 output lines, @HumanitariansAI |
| frame_057s.png | B01 anatomy | EnterpriseSearchAnatomy: search loop (3 numbered steps) left + bundled scripts right; feedback row terracotta on both sides |
| frame_117s.png | B02 design | EnterpriseSearchDesign: core rules left + gotchas right; base URL -be and permissions gap terracotta |
| frame_189s.png | B05 teardown | EnterpriseSearchTell: callout + standard 5+5 two-column teardown, spark line with asterisk |
| frame_248s.png | BVDT verdict | ClaudeVerdictArtifact: "enterprise-search" heading, 6 terracotta-numbered lines |
| frame_284s.png | BHTF handoff | ClaudeComposerAsk: "Your Turn", contractor onboarding + Jira task, expected/red-flag output |
| frame_303s.png | BOUT outro | ClaudeTitleOutro: "enterprise-search" title |

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
| No excessive centering | PASS — two-column B01 with numbered loop, two-column B02, two-column B05 |

## Notes

- Greeting: "Hej, Kore" (rotation #43)
- New scenes: EnterpriseSearchAnatomy (B01), EnterpriseSearchDesign (B02), EnterpriseSearchTell (B05)
- B01: feedback step (3) and feedback: raw curl both terracotta — mirrors the callout about no bundled script
- B02: base URL -be suffix and permissions gap highlighted terracotta as the silent-failure gotchas
- B05 callout: feedback no-script gap — "the negative label is the first thing skipped when a task is finishing"
