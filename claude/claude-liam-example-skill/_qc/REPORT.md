# QC REPORT — claude-liam-example-skill

**Date:** 2026-07-18  
**Duration:** 279.6s (4:40)  
**Result:** PASS

## Frame audit

| Beat | Time | Visual | Status |
|------|------|--------|--------|
| B00 | 10.5s | ClaudeComposerAsk — "Merhaba, Liam" cold open; greeting correct, output lines correct | PASS |
| B01 | 47.3s | ExampleSkillAnatomy — 4 frontmatter fields left (name/desc green, version/license terracotta); 4 file structure rows right (SKILL.md + 3 optional subdirs); spark line correct | PASS |
| B02 | 102.3s | ExampleSkillDesign — trigger patterns left (specific phrases/keywords/topic areas green, avoid-topic-only terracotta); activation modes right (Skill/Command/Agent green, Overlap risk terracotta); spark line correct | PASS |
| B05 | 169.6s | ExampleSkillTell — 5+5 teardown; callout present; star icon + spark line correct | PASS |
| BVDT | 226.4s | ClaudeVerdictArtifact — "example-skill" heading; 6 artifact lines correct | PASS |
| BHTF | 260.9s | ClaudeComposerAsk — "Your Turn" handoff; watch list correct | PASS |
| BOUT | 278.3s | ClaudeTitleOutro — "example-skill. @NikBearBrown. example-skill · Claude Plugins" | PASS |

## Checklist

- [x] Palette: PAGE cream, INK dark, SPARK terracotta — correct throughout
- [x] Font: serif headers, sans body, mono field names — correct
- [x] Column layout: symmetric two-column, no overflow
- [x] Terracotta warnings: version, license, avoid-topic-only, overlap-risk — all correctly flagged
- [x] Spark line with asterisk icon on B05 — present
- [x] Greeting "Merhaba, Liam" — correct for rotation #45
- [x] 7/7 beats filled, no slate beats
