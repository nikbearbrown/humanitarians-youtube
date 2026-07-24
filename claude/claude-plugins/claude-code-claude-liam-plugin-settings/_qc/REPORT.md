# QC Report — claude-liam-plugin-settings

**Date:** 2026-07-18  
**Duration:** 316.9s (5:17)  
**Result:** PASS

## Frame checks

| Beat | Timestamp | Check |
|------|-----------|-------|
| B00 | 17s | ClaudeComposerAsk — "Shalom, Kore" greeting, settings command, 3 output lines. Clean. |
| B01 | 66s | PluginSettingsAnatomy — file location tree + YAML/body structure boxes + 3 consumer cards (HOOKS green, COMMANDS/AGENTS gray). All elements present. |
| B02 | 125s | PluginSettingsPatterns — parsing box with sed/awk code + CAVEAT callout (terracotta) + 3 pattern cards. Readable. |
| B05 | 191s | PluginSettingsTell — standard teardown, 5+5 cards, callout box, spark line. Canvas fill good. |
| BVDT | 248s | ClaudeVerdictArtifact — 6 lines, all content present. |
| BHTF | 291s | ClaudeComposerAsk "Your Turn" — handoff with 4 watch items. |

## Rubric

- [x] Canvas fill >65% across all beats
- [x] Text readable at 1920×1080
- [x] Structure hierarchy clear (B01 file location + structure boxes)
- [x] Callout and spark visible (B05)
- [x] No Inter font (CLAUDE_FONT tokens used)
- [x] No purple gradient (cream PAGE background)
- [x] Border-left accents correct (green HOOKS, gray COMMANDS/AGENTS)
- [x] Caveat box terracotta-bordered in B02

## Slowdown notes

B01: 1.98x · B02: 2.01x · B05: 2.30x  
Slowdowns acceptable: animations complete early, content static and fully visible.
