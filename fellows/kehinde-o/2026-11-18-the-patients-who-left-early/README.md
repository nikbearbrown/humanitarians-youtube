# The Patients Who Left Early

**Volunteer:** Kehinde Obidele  
**Week:** 9  
**Type:** STEM / AI explainer  
**Runtime:** 2m21s  
**Source project:** github.com/Kenny0bi/cancer-survival-prediction  

Patients who leave a study early are not missing data. Each one tells you they survived
at least that long.

My survival project generates synthetic patients, so I know every patient's true survival
time, including the 1,458 of 5,000 (29 percent) the study never sees finish. Against a
true median survival of 51.4 months, dropping the patients who left gives 32.8, counting
them as deaths gives 43.4, and Kaplan-Meier gives 51.1. Of the 425 who left before five
years, 286 were still alive at five years, which is why dropping them throws away
survivors.

All figures come from running the repo's generator and estimator.

Narration is an AI voice (Kokoro). Research and script are mine.

## Video files

The 4K renders are on the shared Google Drive:
[Week 9 - the-patients-who-left-early](https://drive.google.com/drive/folders/1DqXc0ULgsH540xdVlhw8euQVDLcl4Jzs?usp=drive_link)

- `the-patients-who-left-early.mp4` (16:9, 3840x2160)
- `the-patients-who-left-early-short.mp4` (9:16, 2160x3840)

## Build record

- Brutalist: commit `2efd40ad` (upstream `3a6d3979`, pulled 18 Nov 2026)
- SHA-256 `the-patients-who-left-early.mp4`: `be95bc683ed636d2831d8e2075a4a3cdda267b9ffbf3c8cbed2a047c3efa4d78`
- SHA-256 `the-patients-who-left-early-short.mp4`: `6b7301c0672da81f3a9e0080aa7850c2c0297ab17c26dc8c2a34cb4fe6208526`

## Files in this repo

- `beat_sheet.json`: the script and beat structure
- `PEDAGOGY.md`: pedagogy review, VERDICT: PASS
- `FACTCHECK.md`: every on-screen claim and how it was measured
- `SHOTLIST.md`: the typed work order
- `PROMPTS.md`: the on-screen prompts
- `REPORT.md`: what the week produced
- `FRICTIONAL.md`: the frictional log
- `evidence_run.py`: the script that produced every number on screen
- `evidence.json`: its output

Media files are not committed.
