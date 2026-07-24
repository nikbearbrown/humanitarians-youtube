# QC Report — claude-liam-claude-opus-4-5-migration

**Date:** 2026-07-18  
**Duration:** 5:24 (324.4s compiled)  
**Verdict:** PASS

## Frame audit

| Frame | Beat | Notes |
|---|---|---|
| frame_18_2s.png | B00 cold open | ClaudeComposerAsk: "Ciao, Kore", migrate Sonnet 4.5 → Opus 4.5 command, 3 output lines, @HumanitariansAI |
| frame_72_7s.png | B01 matrix | Opus45MigrationMatrix: 4-row target platform table + source/exclusion side panel + 6-step workflow, spark line |
| frame_140_4s.png | B02 triggers | Opus45MigrationTriggers: green opt-in banner + 5 behavioral trigger rows (when/fix columns), integration note, spark line |
| frame_206_6s.png | B05 teardown | Opus45MigrationTell: 5+5 two-column teardown, callout overlaps row 5 (accepted batch pattern), spark line |
| frame_260_4s.png | BVDT verdict | ClaudeVerdictArtifact: "Opus 4.5 Migration" heading, 6 terracotta-numbered lines |
| frame_300_0s.png | BHTF handoff | ClaudeComposerAsk: "Your Turn", migrate from Sonnet 4.5 prompt, red flags |
| frame_322_5s.png | BOUT outro | ClaudeTitleOutro: "Opus 4.5 Migration" title |

## Rubric

| Check | Result |
|---|---|
| Canvas fill >65% | PASS |
| Text readable at all beats | PASS |
| Column alignment correct | PASS |
| Callout / spark line visible (B05) | PASS — callout overlaps row 5 (accepted batch pattern) |
| No Inter font | PASS |
| No purple gradient | PASS |
| No uniform rounded corners | PASS |
| No excessive centering | PASS — two-column matrix B01, 5-row triggers B02, two-column B05 |

## Notes

- Greeting: "Ciao, Kore" (rotation #36)
- New scenes: Opus45MigrationMatrix.tsx (B01), Opus45MigrationTriggers.tsx (B02), Opus45MigrationTell.tsx (B05)
- B01 design: 4-row target platform table (left, 60% wide) + source/exclusion/beta-header panel (right) + 6-step workflow below
- B02 design: green opt-in rule banner above 5 trigger rows; each row has when (terracotta) and fix (green) sub-labels
- Step 3 "Remove Beta Header" highlighted terracotta in B01 workflow (the only non-default step)
