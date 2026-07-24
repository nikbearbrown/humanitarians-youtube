# QC REPORT — claude-liam-web-artifacts-builder

Date: 2026-07-18
Verdict: **PASS**

## Beat frame checks

| Beat | Frame | Layout | Fill | Notes |
|------|-------|--------|------|-------|
| B01 | 450 | WebArtifactsAnatomy | ~88% | TRIGGER box + 4 step cards + 4 stack cards; clean |
| B02 | 450 | WebArtifactsDesign | ~90% | 4 anti-slop rules (terracotta) + 4 bundle facts (white); clean |
| B05 | 450 | WebArtifactsTell | ~92% | Two 5-item columns; callout; spark line; clean |

## Duration check

- Compiled: 296.5s (4:56)
- B01 narration 60.05s vs 30.1s clip → 2.00x slowdown (all content visible throughout)
- B05 narration 61.4s vs 32s clip → 1.92x slowdown (all content visible throughout)
- Slowdowns accepted: spring animations complete early, static content remains; no blank frames

## ffprobe
- Resolution: 1280×720
- Codec: h264 video + aac audio
- Duration: ~296.5s

## 8-point rubric

1. Canvas fills safe area — PASS (no >35% dead space)
2. Text readable — PASS (13–50px, sufficient contrast)
3. Column alignment — PASS (both columns top-aligned at H*0.40)
4. Spark/callout visible — PASS (callout at H*0.26, spark line at bottom)
5. No Inter font — PASS (CLAUDE_FONT.serif + .ui + .mono only)
6. No purple gradient — PASS (cream page, terracotta + green accents)
7. No uniform rounded corners — PASS (varied: 16px callout, 10px cards)
8. No excessive centering — PASS (two-column layout dominates)
