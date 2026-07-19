# QC REPORT — claude-liam-command-development

**Date:** 2026-07-18
**Duration:** 334.1s (5:34)
**Status:** PASS

## Beat-by-beat

| Beat | Pattern | Duration | Slowdown | QC |
|------|---------|----------|----------|----|
| B00 | ClaudeComposerAsk | 41.5s | 1.38x | PASS |
| B01 | CommandDevAnatomy | 70.0s | 2.33x | PASS |
| B02 | CommandDevContent | 65.7s | 2.19x | PASS |
| B05 | CommandDevTell | 69.1s | 2.16x | PASS |
| BVDT | ClaudeVerdictArtifact | 43.8s | 1.28x | PASS |
| BHTF | ClaudeComposerAsk | 41.0s | 1.36x | PASS |
| BOUT | ClaudeTitleOutro | 3.0s | center-cut | PASS |

## 8-point rubric

1. Canvas fill >65%: PASS — B01 fills with 3 locations + 5 fields + 4 arg cards; B02 fills with wrong/right pair + 4 pattern cards; B05 fills with standard teardown columns
2. Text readable at 1280×720: PASS
3. Column alignment correct: PASS — both columns aligned in B01 and B05
4. Callout and spark lines visible: PASS — B05 has callout box + spark icon + spark line
5. No Inter font: PASS — Claude palette fonts throughout
6. No purple gradient: PASS — cream #FAF9F5 background throughout
7. No uniform excessive rounded corners: PASS — distinct card treatments
8. No excessive centering: PASS — data beats left-aligned, title beats centered

## Notes

- B01/B02/B05 slowdowns (2.16x–2.33x): animations complete in first ~15s, content stays static and fully readable throughout. Established PASS pattern.
- allowed-tools field highlighted in terracotta in B01 — correct visual emphasis.
- Wrong/right comparison in B02 clear with distinct border colors (terracotta wrong, green right).
- Greeting "Ciao, Liam" displays correctly in B00.
