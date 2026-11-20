# Every Look Was Right

**Volunteer:** Kehinde Obidele  
**Week:** 10  
**Type:** STEM / AI explainer  
**Runtime:** 2m28s  
**Source project:** github.com/Kenny0bi/product-analytics-engine  

Checking a running experiment again and again, and stopping at the first significant
result, raises the false alarm rate even though every single check is a valid test.

I ran 1,000 A/A experiments (no real difference, 2,000 users per arm, 10 looks) through my
analytics engine. Reading the z-test once at the end gave 4.0 percent false alarms.
Stopping at the first significant look gave 18.7 percent. My engine's own sequential test
gave 12.9 percent, because it re-estimated the control rate from the same data at every
look. I fixed it the same day: the engine now compares users in pairs, and on the same 1,000
experiments it raised 1.7 percent false alarms.

Narration is an AI voice (Kokoro). Research and script are mine.

## Video files

The 4K renders are on the shared Google Drive:
[Week 10 - every-look-was-right](https://drive.google.com/drive/folders/1uzsEqyuOdUHjgOWCFHAsc-94NnuNb2bm?usp=drive_link)

- `every-look-was-right.mp4` (16:9, 3840x2160)
- `every-look-was-right-short.mp4` (9:16, 2160x3840)

## Build record

- Brutalist: commit `2efd40ad` (upstream `3a6d3979`, pulled 18 Nov 2026)
- SHA-256 `every-look-was-right.mp4`: `b1a0a907b951564e38e8ffadf7a507e4ba14105ab2170a60ba75042f363dca30`
- SHA-256 `every-look-was-right-short.mp4`: `eeaf8b832c5cc6c00f7c597556afb988ae086655c43dd592ed5c7de395a87400`

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
