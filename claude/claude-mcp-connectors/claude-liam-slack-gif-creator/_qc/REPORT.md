# QC REPORT — claude-liam-slack-gif-creator

Date: 2026-07-18  
Reel: `anthropics/skills/youtube/claude-liam-slack-gif-creator/claude-liam-slack-gif-creator.mp4`

## Beat-by-beat assessment

| Beat | Pattern | Layout | Fill | Brand | Text | Result |
|------|---------|--------|------|-------|------|--------|
| B00 | ClaudeComposerAsk | ✓ | ✓ | ✓ | ✓ | PASS |
| B01 | SlackGifAnatomy | ✓ TRIGGER + 2 format cards + 3 utilities + deps | L:69% R:79% | ✓ | ✓ | PASS |
| B02 | SlackGifAnimations | ✓ 4+4 animation concept rows | ~91% | ✓ | ✓ | PASS |
| B05 | SlackGifTell | ✓ callout + 5 gets-right + 5 bites | ~87% | ✓ | ✓ | PASS |
| BVDT | ClaudeVerdictArtifact | ✓ 6 verdict lines | ✓ | ✓ | ✓ | PASS |
| BHTF | ClaudeComposerAsk | ✓ | ✓ | ✓ | ✓ | PASS |
| BOUT | ClaudeTitleOutro | ✓ | ✓ | ✓ | ✓ | PASS |

## Notes
- B01 left column fills to ~69% — natural constraint with only 2 format types; not a major defect
- B05 narration (58.6s) vs clip (32s) → 1.83x slowdown; content visible throughout, spring animations complete early

## 8-point rubric

1. **Layout** ✓ — two-column layout consistent; code labels in MONO on right of card headers
2. **Typography** ✓ — SERIF titles, SANS body, MONO code snippets (math.sin, ease_out, etc.)
3. **Canvas fill** ✓ — B02 fills 91%; B01 right 79%; B05 87%; all within acceptable range
4. **Color** ✓ — PAGE/INK/SPARK tokens; emoji format card terracotta accent correct
5. **Animation** ✓ — spring-in per card, staggered; all items visible by frame 300
6. **Text readability** ✓ — code snippet labels legible at 1280×720
7. **Brand tokens** ✓ — CLAUDE palette and CLAUDE_FONT from claude.ts throughout
8. **SparkLine** ✓ — all three custom sparkLines render correctly

## VERDICT: PASS
