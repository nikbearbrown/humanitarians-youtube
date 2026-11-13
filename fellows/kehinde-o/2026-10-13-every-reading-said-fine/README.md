# Every Reading Said Fine

**Volunteer:** Kehinde Obidele
**Week:** 13 Oct 2026
**Type:** STEM / AI explainer
**Runtime:** 2m36s
**Source project:** github.com/Kenny0bi/real-time-vitals-pipeline

A threshold that is correct on every individual reading can still miss a patient who
is deteriorating, because deterioration lives in the trend and a threshold only ever
sees the instant.

Worked on my own streaming pipeline: twelve synthetic patients, one reading a second,
each scored with the Modified Early Warning Score. For a patient whose oxygen
saturation fell from 98 to 80, 1,117 of 1,800 readings (62.1 percent) still scored two
or below, and only 24 (1.3 percent) crossed the immediate-review threshold. The score
was not broken. It fired correctly, 24 times, on someone who had been sliding for most
of an hour.

Every figure was computed by running the repo's simulator and scorer at seed 42, not
read off a README.

## Video files

The 4K renders are on the shared Google Drive:
[Medhavy_Kehinde/STEM Topic/every-reading-said-fine/](https://drive.google.com/drive/folders/1YZ3bLjWZ74sSdhdx4vC9X8MTLOykNk_6?usp=drive_link)

- `every-reading-said-fine.mp4` (16:9, 3840x2160)
- `every-reading-said-fine-short.mp4` (9:16, 2160x3840, native render)

## Files in this repo

- `beat_sheet.json` — the script and beat structure
- `PEDAGOGY.md` — pedagogy review, VERDICT: PASS
- `FACTCHECK.md` — all 12 on-screen claims and how each was measured
- `SHOTLIST.md` — the typed work order
- `PROMPTS.md` — the on-screen prompts
- `REPORT.md` — what the week produced
- `FRICTIONAL.md` — the frictional log

Media files are not committed.
