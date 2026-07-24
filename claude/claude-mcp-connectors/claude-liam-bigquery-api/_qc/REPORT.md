# QC Report — claude-liam-bigquery-api

**Date:** 2026-07-18  
**Duration:** 5:11 (311.2s compiled)  
**Verdict:** PASS

## Frame audit

| Frame | Beat | Notes |
|---|---|---|
| frame_18s.png | B00 cold open | ClaudeComposerAsk: "Namaste, Kore", command visible, 3 output lines, @HumanitariansAI |
| frame_52s.png | B01 job model | BigQueryApiAnatomy: two-column (Sync green / Async terracotta), 3 critical invariants below, spark line visible |
| frame_110s.png | B02 operations | BigQueryApiOps: 4×2 grid, preview rows (#08) highlighted green, spark line |
| frame_195s.png | B05 teardown | BigQueryApiTell: 5+5 teardown columns, callout with spark icon, spark line |
| frame_272s.png | BVDT verdict | ClaudeVerdictArtifact: "BigQuery API" heading, 6 terracotta-numbered lines including DONE≠success |
| frame_307s.png | BHTF handoff | ClaudeComposerAsk: "Your Turn", Texas query, red flag "DONE assumed success" |
| frame_309s.png | BOUT outro | ClaudeTitleOutro: "BigQuery API." title |

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
| No excessive centering | PASS — two-column B01, 4×2 grid B02, two-column B05 |

## Notes

- Greeting: "Namaste, Kore" (rotation #29)
- New scenes: BigQueryApiAnatomy.tsx (B01), BigQueryApiOps.tsx (B02), BigQueryApiTell.tsx (B05)
- B01 design: sync (green) vs async (terracotta) two modes + 3 critical invariants in a 1×3 row
- Preview op (#08) highlighted green to signal no-cost benefit
