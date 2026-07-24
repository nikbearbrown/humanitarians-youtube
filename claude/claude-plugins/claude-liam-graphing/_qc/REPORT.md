# QC REPORT — claude-liam-graphing

**Date:** 2026-07-18  
**Duration:** 326.2s (5:26)  
**Result:** PASS

## Frame audit

| Beat | Time | Visual | Status |
|------|------|--------|--------|
| B00 | 9.0s | ClaudeComposerAsk — "Merhaba, Liam", correct topic/output lines | PASS |
| B01 | 53.9s | GraphingAnatomy — 5 chartkit primitives left (all green); 3 data helpers right (zero_fill_days + rolling_mean terracotta, log_floor green); spark line correct | PASS |
| B02 | 114.4s | GraphingDesign — 4 workflow steps left (all green); 5 judgement defaults right (all green); headings correct; spark line correct | PASS |
| B05 | 195.7s | GraphingTell — 5+5 teardown; callout about GRID/ACCENT placeholder present; star icon + spark line correct | PASS |
| BVDT | 274.9s | ClaudeVerdictArtifact — "graphing" heading; 6 artifact lines correct | PASS |
| BHTF | 306.4s | ClaudeComposerAsk — "Your Turn" handoff; watch list correct | PASS |
| BOUT | 325.0s | ClaudeTitleOutro — "graphing. @NikBearBrown. graphing · Claude Plugins" | PASS |

## Checklist

- [x] Palette: PAGE cream, INK dark, SPARK terracotta — correct throughout
- [x] Font: serif headers, sans body, mono function names — correct
- [x] Column layout: asymmetric (5+3 left, 4+5 right) but clean, no overflow
- [x] Terracotta warnings: zero_fill_days (skip if zeros lie), rolling_mean (trailing, don't center) — correctly flagged; log_floor correctly green
- [x] Star icon + spark line on B05 — present
- [x] Greeting "Merhaba, Liam" — correct
- [x] 7/7 beats filled, no slate beats
