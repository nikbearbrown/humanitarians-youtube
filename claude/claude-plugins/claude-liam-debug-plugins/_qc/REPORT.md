# QC Report — claude-liam-debug-plugins

**Date:** 2026-07-18  
**Duration:** 4:43 (283.7s compiled)  
**Verdict:** PASS

## Frame audit

| Frame | Beat | Notes |
|---|---|---|
| frame_011s.png | B00 cold open | ClaudeComposerAsk: "Ciao, Kore", plugin-not-loading command, 3 output lines, @HumanitariansAI |
| frame_048s.png | B01 anatomy | DebugPluginsAnatomy: steps 1-3 (Collect Evidence) left + steps 4-6 (Interpret + Report) right; numbered rows with green/terracotta borders |
| frame_103s.png | B02 design | DebugPluginsDesign: 5 failure-ladder rows left + 3 key-constraint cards right; session snapshot + stdout not persisted both terracotta |
| frame_170s.png | B05 teardown | DebugPluginsTell: callout + standard 5+5 two-column teardown, spark line with asterisk |
| frame_224s.png | BVDT verdict | ClaudeVerdictArtifact: "debug-plugins" heading, 6 terracotta-numbered lines |
| frame_260s.png | BHTF handoff | ClaudeComposerAsk: "Your Turn", zip-present-skill-absent prompt, expected/red-flag output |
| frame_282s.png | BOUT outro | ClaudeTitleOutro: "debug-plugins" title |

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
| No excessive centering | PASS — two-column B01 numbered steps, two-column B02, two-column B05 |

## Notes

- Greeting: "Ciao, Kore" (rotation #42)
- New scenes: DebugPluginsAnatomy (B01), DebugPluginsDesign (B02), DebugPluginsTell (B05)
- B01: step 3 (log file) and step 5 (unzip) highlighted terracotta for security/exception tension
- B02: session snapshot and stdout-not-persisted highlighted terracotta as the hardest operational constraints
- B05 callout: unzip Bash exception vs security note — "a reader following the note literally would skip a key diagnostic"
