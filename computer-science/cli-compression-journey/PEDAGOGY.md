# Pedagogy audit -- cli-compression-journey

## Structure check
- B00 INTRO: brand open, sets register
- B01 PROBLEM: states the stakes before any terminal -- MobileNetV2-0.5 misses all 3 ceilings on STM32H7; the three-knob problem framed
- B02 ASK: terminal command, explains what is being asked and why
- B03 CODE: key logic shown -- 4-state table with ceiling comparisons
- B04 OUTPUT: compression journey bar chart, all 4 metrics x 4 states, narrates the journey
- B05 CHANGE: revision command -- add order-matters column
- B06 OUTPUT (revised): quantize->prune vs prune->quantize, 2.5 pt spread explained
- B07 SUMMARY: lesson stated -- three-knob sequence and ship state
- B08 NEXT STEPS: concrete actions for the viewer
- B09 OUTRO: brand close

## Voice check
- No "obviously", "clearly", "important to understand", "in this video"
- Problem stated first (B01) before any CLI
- Concrete numbers throughout: 4 MB FP32, 1 MB INT8, 0.75 MB pruned, 240 ms, 90.6%
- No fabricated numbers beyond what the candidate card provides
- B02 narration starts "Ask for the experiment. In the terminal: claude -- ..."

## CLI loop check
- At least one revision: YES (B05 CHANGE -> B06 revised output, order-matters penalty)
- SUMMARY and NEXT STEPS present: YES

VERDICT: PASS
