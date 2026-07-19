# Pedagogy audit -- cli-battery-life

## Structure check
- B00 INTRO: brand open, sets register
- B01 PROBLEM: states the stakes before any terminal -- product died at 33 days instead of 333; duty cycle formula framed
- B02 ASK: terminal command, explains what is being asked and why
- B03 CODE: three-multiplication formula explained
- B04 OUTPUT: current strip at 3 frequencies showing duty cycle and days ticking down
- B05 CHANGE: revision command -- add race-to-sleep optimization
- B06 OUTPUT (revised): two traces, run slow vs race-to-sleep; RACE-TO-SLEEP WINS chip
- B07 SUMMARY: lesson stated -- the three-multiplication formula; compute before prototype
- B08 NEXT STEPS: concrete actions for the viewer
- B09 OUTRO: brand close

## Voice check
- No "obviously", "clearly", "important to understand", "in this video"
- Problem stated first (B01) before any CLI
- Concrete numbers throughout: 10Hz vs 1Hz, duty cycle 1.0, 30mA vs 3mA, 333 days vs 33 days
- No fabricated numbers beyond what the candidate card provides
- B02 narration starts "Ask for the experiment. In the terminal: claude -- ..."

## CLI loop check
- At least one revision: YES (B05 CHANGE -> B06 revised output, race-to-sleep)
- SUMMARY and NEXT STEPS present: YES

VERDICT: PASS
