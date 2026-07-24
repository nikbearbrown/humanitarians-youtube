# QC REPORT — claude-liam-linear-api

**Date:** 2026-07-19  
**Duration:** 373.9s (6:14)  
**Result:** PASS

## Frame audit

| Beat | Time | Visual | Status |
|------|------|--------|--------|
| B00 | 12.3s | ClaudeComposerAsk — "Merhaba, Kore"; LINEAR API · CLAUDE PLUGINS; ENG team command + 3 output lines | PASS |
| B01 | 67.9s | LinearApiAnatomy — GraphQL MODEL left (Single endpoint green, Two ID systems green, No Bearer prefix terracotta, HTTP 200 on errors terracotta); HELPERS right (linear_gql() green, linear_issues.sh green, Rate limit: HTTP 400 terracotta) | PASS |
| B02 | 148.3s | LinearApiDesign — WORKFLOW left (Sanity check/UUID before mutate/Markdown body/Check success boolean all green); GOTCHAS right (Rate limit=HTTP 400/No totalCount/Epoch milliseconds/UUID not identifier all terracotta) | PASS |
| B05 | 237.0s | LinearApiTell — callout with rate-limit HTTP 400 explanation; 5 GETS RIGHT green left + 5 WHERE IT BITES terracotta right; star spark line correct | PASS |
| BVDT | 309.9s | ClaudeVerdictArtifact — "linear api" heading; 6 artifact lines correct | PASS |
| BHTF | 351.1s | ClaudeComposerAsk — "Your Turn" handoff; 5-point watch list correct | PASS |
| BOUT | 372.4s | ClaudeTitleOutro — "linear api. @HumanitariansAI. linear api · Claude Plugins" | PASS |

## Checklist

- [x] Palette: PAGE cream, INK dark, SPARK terracotta — correct throughout
- [x] Font: serif headers, sans body, mono API names — correct
- [x] Column layout: B01 4+3 (GraphQL model + helpers), B02 4+4 (workflow + gotchas) — clean, no overflow
- [x] Terracotta warnings: No Bearer prefix / HTTP 200 on errors / Rate limit HTTP 400 / No totalCount / Epoch ms / UUID not identifier correctly flagged
- [x] Star icon + spark line on B05 — present
- [x] Greeting "Merhaba, Kore" — correct
- [x] 7/7 beats filled, no slate beats
- [x] Note: B05 (3.2x) slow-mo warning from compile; all slots VIDEO, visual passes
