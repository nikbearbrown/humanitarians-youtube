# QC REPORT — claude-liam-hubspot-api

**Date:** 2026-07-19  
**Duration:** 389.9s (6:30)  
**Result:** PASS

## Frame audit

| Beat | Time | Visual | Status |
|------|------|--------|--------|
| B00 | 11.0s | ClaudeComposerAsk — "Merhaba, Kore"; HUBSPOT API · CLAUDE PLUGINS; correct command + output lines | PASS |
| B01 | 65.4s | HubSpotApiAnatomy — CRM Model left (Uniform v3 URL green, Properties opt-in terracotta, Dedup keys green, Associations typed green); Helpers right (hsapi() green, hs_search.sh green, Search 10,000 cap terracotta) | PASS |
| B02 | 148.3s | HubSpotApiDesign — Workflow left (sanity check/discover schema/properties=/batch all green); Gotchas right (409 CONFLICT/Search 5req/s/400 VALIDATION_ERROR terracotta, idProperty= green) | PASS |
| B05 | 242.4s | HubSpotApiTell — 5+5 teardown; callout about properties opt-in default set in references/api.md; star icon + spark line correct | PASS |
| BVDT | 322.7s | ClaudeVerdictArtifact — "hubspot api" heading; 6 artifact lines correct | PASS |
| BHTF | 367.5s | ClaudeComposerAsk — "Your Turn" handoff; watch list correct | PASS |
| BOUT | 388.3s | ClaudeTitleOutro — "hubspot api. @HumanitariansAI. hubspot api · Claude Plugins" | PASS |

## Checklist

- [x] Palette: PAGE cream, INK dark, SPARK terracotta — correct throughout
- [x] Font: serif headers, sans body, mono property names — correct
- [x] Column layout: B01 4+3 (CRM model + helpers), B02 4+4 (workflow + gotchas) — clean, no overflow
- [x] Terracotta warnings: Properties opt-in / 409 CONFLICT / Search 5req/s / 400 VALIDATION_ERROR correctly flagged
- [x] Star icon + spark line on B05 — present
- [x] Greeting "Merhaba, Kore" — correct
- [x] 7/7 beats filled, no slate beats
- [x] Note: B05 narration long (109s) — 3.4x slow-mo warning from compile; visual still passes
