# Pedagogy audit -- cli-latency-predictor

## Structure check
- B00 INTRO: brand open, sets register
- B01 PROBLEM: states the stakes before any terminal -- four pipeline stages, one dominates, wasted week framed
- B02 ASK: terminal command, explains what is being asked and why
- B03 CODE: four-stage formula explained; arithmetic intensity as the key variable
- B04 OUTPUT: FP32 Gantt chart with weight load dominant (45ms, CRIMSON), total 100ms
- B05 CHANGE: revision command -- re-run for INT8 model, show which stage shrinks
- B06 OUTPUT (revised): INT8 Gantt; weight load shrinks 4x to 11ms; compute now dominant; total 38ms
- B07 SUMMARY: lesson stated -- memory-bound -> quantize; compute-bound -> prune; wasted-week warning
- B08 NEXT STEPS: concrete actions for the viewer
- B09 OUTRO: brand close

## Voice check
- No "obviously", "clearly", "important to understand", "in this video"
- Problem stated first (B01) before any CLI
- Concrete numbers throughout: 45ms weight load, 12ms compute, 38ms mem move, 5ms overhead, 100ms total, 38ms INT8
- Illustrative data stated as such (per candidate card: this is fine for the video's lesson)
- B02 narration starts "Ask for the experiment. In the terminal: claude -- ..."

## CLI loop check
- At least one revision: YES (B05 CHANGE -> B06 revised output, INT8 stage shift)
- SUMMARY and NEXT STEPS present: YES

VERDICT: PASS
