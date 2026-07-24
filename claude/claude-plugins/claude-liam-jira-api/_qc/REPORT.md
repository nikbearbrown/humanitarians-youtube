# QC REPORT — claude-liam-jira-api

**Date:** 2026-07-19  
**Duration:** 423.9s (7:04)  
**Result:** PASS

## Frame audit

| Beat | Time | Visual | Status |
|------|------|--------|--------|
| B00 | 14.5s | ClaudeComposerAsk — "Merhaba, Kore"; JIRA API · CLAUDE PLUGINS; correct command + output lines | PASS |
| B01 | 80.9s | JiraApiAnatomy — API Families left (Platform REST v3 green, Agile REST v1 green, ADF body terracotta, Transitions terracotta); Helpers right (jira_api() green, jql_search.sh green, Search no total terracotta) | PASS |
| B02 | 177.2s | JiraApiDesign — Workflow left (sanity check/createmeta/bounded JQL/accountId all green); Status Codes right (204=success green, 404 masks access/410 retired/Watcher bare string terracotta) | PASS |
| B05 | 275.2s | JiraApiTell — 5+5 teardown; callout about ADF body requirement; star icon + spark line correct | PASS |
| BVDT | 353.7s | ClaudeVerdictArtifact — "jira api" heading; 6 artifact lines correct | PASS |
| BHTF | 399.7s | ClaudeComposerAsk — "Your Turn" handoff; watch list correct | PASS |
| BOUT | 422.3s | ClaudeTitleOutro — "jira api. @HumanitariansAI. jira api · Claude Plugins" | PASS |

## Checklist

- [x] Palette: PAGE cream, INK dark, SPARK terracotta — correct throughout
- [x] Font: serif headers, sans body, mono API names — correct
- [x] Column layout: B01 4+3 (families + helpers), B02 4+4 (workflow + status codes) — clean, no overflow
- [x] Terracotta warnings: ADF body / Transitions / Search no-total / 404 masks / 410 / Watcher bare string correctly flagged
- [x] Star icon + spark line on B05 — present
- [x] Greeting "Merhaba, Kore" — correct
- [x] 7/7 beats filled, no slate beats
- [x] Note: B01 (3.2x) + B05 (3.3x) slow-mo warnings from compile; all slots VIDEO, visual passes
