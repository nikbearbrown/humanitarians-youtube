# Pedagogy audit — cli-memory-verdict

## Structure check
- B00 INTRO: brand open
- B01 PROBLEM: stakes before CLI -- flash vs SRAM, out-of-memory hides which; two different bugs, two different fixes
- B02 ASK: terminal command for memory.py
- B03 CODE: weight_kb = params * bpp / 1024; SRAM = largest single activation; typed verdict with margins
- B04 OUTPUT: FP32 waterfall bars; flash 5.6MB over 4MB ceiling (CRIMSON), SRAM 0.5MB under 1MB ceiling (INK); verdict FLASH:FAIL SRAM:OK
- B05 CHANGE: int8 toggle
- B06 OUTPUT (revised): INT8 bars; flash 1.4MB (INK, pass), SRAM 0.25MB (INK, pass); verdict FLASH:PASS SRAM:PASS
- B07 SUMMARY: flash fail -> compress weights; SRAM fail -> tile activations; naming forces right fix
- B08 NEXT STEPS: get param count + activation from loader, flash/SRAM from datasheet, run verdict
- B09 OUTRO: brand close

## Voice check
- No forbidden phrases
- Problem stated first (B01) before CLI
- Concrete numbers: 1.4M params, FP32=5.6MB, INT8=1.4MB, 4MB flash budget, 1MB SRAM budget, 0.5MB activations
- No fabricated numbers (all from candidate 12)

## CLI loop check
- At least one revision: YES (B05 CHANGE -> B06 revised output)
- SUMMARY and NEXT STEPS present: YES

VERDICT: PASS
