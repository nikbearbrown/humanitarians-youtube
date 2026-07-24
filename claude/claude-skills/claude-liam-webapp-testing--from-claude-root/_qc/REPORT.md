# QC REPORT — claude-liam-webapp-testing

Date: 2026-07-18
Verdict: **PASS**

## Beat frame checks

| Beat | Frame | Layout | Fill | Notes |
|------|-------|--------|------|-------|
| B01 | 450 | WebappTestingAnatomy | ~82% | Decision tree: TRIGGER + 2-col (static/dynamic) + 4-card recon loop; spark line at bottom |
| B02 | 450 | WebappTestingPatterns | ~91% | 4+4 items per column; 3 example scripts row; clean fill |
| B05 | 450 | WebappTestingTell | ~92% | Two 5-item columns; callout; spark icon+line; clean |

## Duration check

- Compiled: 284.1s (4:44)
- B01 narration 50.65s vs 30.1s clip → 1.69x slowdown
- B02 narration 59.24s vs 30.1s clip → 1.97x slowdown
- B05 narration 57.43s vs 32.0s clip → 1.79x slowdown
- Slowdowns accepted: spring animations complete early, static content remains; no blank frames

## ffprobe
- Resolution: 1280×720
- Codec: h264 video + aac audio
- Duration: ~284.1s

## 8-point rubric

1. Canvas fills safe area — PASS (no >35% dead space; B01 has small gap between recon loop and spark, acceptable)
2. Text readable — PASS (12–48px, sufficient contrast throughout)
3. Column alignment — PASS (both columns consistent COL_TOP positioning)
4. Spark/callout visible — PASS (spark line and central callout present)
5. No Inter font — PASS (CLAUDE_FONT.serif + .ui + .mono only)
6. No purple gradient — PASS (cream page, terracotta + green accents)
7. No uniform rounded corners — PASS (varied: 14px trigger, 10px items, 8px recon/example cards)
8. No excessive centering — PASS (two-column layout with TRIGGER span dominates)
