# ECIS Episode 13

**Series:** ECIS — Weekly Implementation Video


**Project:** [Mycroft — ECIS](https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis)


**Week:** Week 18 (Phase 18), October 25 – 31, 2026


**Status:** Complete
 
---
 
## About the Video
 
ECIS reads earnings calls and predicts how companies will revise their financial guidance. Every prediction comes with a confidence score. But a confidence score is only useful if it is accurate.
 
This episode covers the Phase 18 work, which teaches the system when to be careful with its own answers. It adds four new abilities:
 
- **Accurate confidence:** when the system says it is 80% sure, it should be right about 80% of the time.
- **Mixed-signal detection:** the system notices when signals from the same call point in different directions.
- **Plain-English explanations:** every prediction comes with a sentence explaining what drove it.
- **Unfamiliar-call detection:** the system lowers its confidence when a call looks unlike anything it has seen before.
## Key Takeaways
 
- **A confidence score should mean what it says.** Two standard methods, Platt scaling and isotonic regression, adjust the scores. Both are tested on data the system has not seen.
- **Mixed signals are useful information, not just noise.** They can point to real uncertainty or a mixed outlook.
- **Every prediction now comes with a reason.** The system shows which factors pushed it up or down, and writes that out as a sentence.
- **The system knows its limits.** The more unusual a call is, the more its confidence is reduced.
## Video Outline
 
| # | Section | What it covers |
|---|---|---|
| 1 | Opening | Why a confidence score needs to be checked |
| 2 | Recap | A short overview of what the system already does |
| 3 | Calibration | Making confidence scores match real outcomes |
| 4 | Contradictions | Finding and rating mixed signals within one call |
| 5 | Explanations | Breaking each prediction into the factors behind it |
| 6 | Unfamiliar Calls | Lowering confidence for calls unlike the training data |
| 7 | Closing | The four new abilities, summed up |
| 8 | Summary | The main ideas in one place |
| 9 | Your Turn | A prompt for viewers to check their own model's confidence |
| 10 | Outro | Closing title |
 
## Project Structure
 
```
README.md               — this file
beats.json              — summary of each scene
beat_sheet.json         — full scene-by-scene plan, with narration and timings
narration/              — narration audio for each scene
visuals/                — visuals for each scene
short/beat_sheet.json   — scene plan for the short version
FRICTIONAL.md           — friction log
REPORT.md               — video report
```
 
