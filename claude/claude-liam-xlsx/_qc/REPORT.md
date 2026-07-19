# QC REPORT — claude-liam-xlsx

Date: 2026-07-18
Verdict: **PASS**

## Beat frame checks

| Beat | Frame | Layout | Fill | Notes |
|------|-------|--------|------|-------|
| B01 | 450 | XlsxAnatomy | ~85% | TRIGGER + pandas/openpyxl left col + 6-step workflow right col; recalc.py step highlighted terracotta |
| B02 | 450 | XlsxStandards | ~88% | 5 color swatches left + 5 number formats right + formula mandate callout; clean |
| B05 | 450 | XlsxTell | ~91% | Two 5-item columns; callout mentions formula mandate + data_only trap; spark line visible |

## Duration check

- Compiled: 307.4s (5:07)
- B01 narration 55.91s vs 30.1s clip → 1.86x slowdown
- B02 narration 52.22s vs 30.1s clip → 1.73x slowdown
- B05 narration 65.05s vs 32.0s clip → 2.03x slowdown (borderline; content static but visible throughout)
- All slowdowns accepted: spring animations complete early, static content remains; no blank frames

## ffprobe
- Resolution: 1280×720
- Codec: h264 video + aac audio
- Duration: ~307.4s

## 8-point rubric

1. Canvas fills safe area — PASS (no >35% dead space)
2. Text readable — PASS (11–48px, sufficient contrast)
3. Column alignment — PASS (consistent COL_TOP positioning)
4. Mandate callout visible — PASS (formula mandate box prominent in B02)
5. No Inter font — PASS (CLAUDE_FONT.serif + .ui + .mono only)
6. No purple gradient — PASS (cream page, terracotta + green accents)
7. No uniform rounded corners — PASS (14px trigger, 8px items, 16px callout)
8. No excessive centering — PASS (two-column layout with TRIGGER span dominates)
