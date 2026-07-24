# QC REPORT — claude-liam-m5-onboard

**Date:** 2026-07-19  
**Duration:** 387.5s (6:28)  
**Result:** PASS

## Frame audit

| Beat | Time | Visual | Status |
|------|------|--------|--------|
| B00 | 14.8s | ClaudeComposerAsk — "Merhaba, Kore"; M5-ONBOARD · CLAUDE PLUGINS; Cardputer-Adv command + 3 output lines | PASS |
| B01 | 56.2s | M5OnboardAnatomy — STAGES left (Detect+Identify green, Fetch firmware green, Flash terracotta, Install apps green); RUN PATTERN right (onboard.py green, Run in background terracotta, smoke_test.py green) | PASS |
| B02 | 140.3s | M5OnboardDesign — WORKFLOW left (Confirm variant/Background+tee/Relay button dance/Install-only mode all green); GOTCHAS right (Baud rate/NVS boot_option=2/Cardputer vs Cardputer-Adv/Never unplug all terracotta) | PASS |
| B05 | 227.2s | M5OnboardTell — callout about BtnG0+BtnRST no-software-path; 5 GETS RIGHT green left + 5 WHERE IT BITES terracotta right; star spark line correct | PASS |
| BVDT | 329.7s | ClaudeVerdictArtifact — "m5-onboard" heading; 6 artifact lines correct | PASS |
| BHTF | 379.9s | ClaudeComposerAsk — "Your Turn" handoff; 5-point watch list correct | PASS |
| BOUT | 386.0s | ClaudeTitleOutro — "m5-onboard. @HumanitariansAI. m5-onboard · Claude Plugins" | PASS |

## Checklist

- [x] Palette: PAGE cream, INK dark, SPARK terracotta — correct throughout
- [x] Font: serif headers, sans body, mono stage names — correct
- [x] Column layout: B01 4+3 (stages + run pattern), B02 4+4 (workflow + gotchas) — clean, no overflow
- [x] Terracotta warnings: Flash stage / Run in background / Baud rate / NVS boot_option=2 / Cardputer vs Cardputer-Adv / Never unplug correctly flagged
- [x] Star icon + spark line on B05 — present
- [x] Greeting "Merhaba, Kore" — correct
- [x] 7/7 beats filled, no slate beats
- [x] Note: B05 (3.2x) slow-mo warning from compile; all slots VIDEO, visual passes
