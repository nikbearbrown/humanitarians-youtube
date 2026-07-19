# QC Report — claude-liam-config-guide

**Date:** 2026-07-18  
**Duration:** 4:56 (296.3s compiled)  
**Verdict:** PASS

## Frame audit

| Frame | Beat | Notes |
|---|---|---|
| frame_14s_B00.png | B00 cold open | ClaudeComposerAsk: "Merhaba, Liam", agents/scopes query, 3 output lines, @NikBearBrown |
| frame_59s_B01.png | B01 anatomy | ConfigGuideAnatomy: 4-layer column (left, green) + 5 reference file column (right, terracotta), spark line |
| frame_121s_B02.png | B02 design | ConfigGuideDesign: 3 equal-width cards (Index Pattern · Slack-Only Scope · Debug-Plugins Handoff), Slack card highlighted terracotta, gap items accented in each card |
| frame_184s_B05.png | B05 teardown | ConfigGuideTell: callout + standard 5+5 two-column teardown, spark line with asterisk |
| frame_235s_BVDT.png | BVDT verdict | ClaudeVerdictArtifact: "Config Guide" heading, 6 terracotta-numbered lines |
| frame_274s_BHTF.png | BHTF handoff | ClaudeComposerAsk: "Your Turn", identity-profiles query, expected/red-flag output lines |
| frame_295s_BOUT.png | BOUT outro | ClaudeTitleOutro: "Config Guide" title |

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
| No excessive centering | PASS — two-column B01, three-card B02, two-column B05 |

## Notes

- Greeting: "Merhaba, Liam" (rotation #38)
- New scenes: ConfigGuideAnatomy (B01), ConfigGuideDesign (B02), ConfigGuideTell (B05)
- Index skill pattern correctly visualized: 4-layer model maps to 5 reference file topics
- Slack-only Scope card highlighted in B02 to signal the caveat
- B05 callout targets the silent-failure risk of the index pattern
