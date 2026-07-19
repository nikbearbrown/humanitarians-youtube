# Pedagogy audit — cli-roofline

## Structure check
- B00 INTRO: brand open, sets register
- B01 PROBLEM: states the stakes before any terminal — two identical FLOPs, wildly different speed, memory bus as hidden variable
- B02 ASK: terminal command, explains what is being asked and why
- B03 CODE: key function shown, what to verify
- B04 OUTPUT: roofline plot with FP32 operating point, narrates what it shows
- B05 CHANGE: revision command, explains the change
- B06 OUTPUT (revised): INT8 point added, shift explained
- B07 SUMMARY: lesson stated — which knob to turn for each region
- B08 NEXT STEPS: concrete actions for the viewer
- B09 OUTRO: brand close

## Voice check
- No "obviously", "clearly", "important to understand", "in this video", "fascinating", "powerful"
- Problem stated first (B01) before any CLI
- Concrete numbers throughout: 0.5 FLOP/byte ridge, AI=0.2 FP32, AI=0.8 INT8
- No fabricated numbers beyond what the candidate card provides

## CLI loop check
- At least one revision: YES (B05 CHANGE -> B06 revised output)
- SUMMARY and NEXT STEPS present: YES

VERDICT: PASS
