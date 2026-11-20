# Where the Error Lives

**Volunteer:** Kehinde Obidele  
**Week:** 8  
**Type:** STEM / AI explainer  
**Runtime:** 2m37s  
**Source project:** github.com/Kenny0bi/hive-index  

My compressed vector index (IVF-PQ, from Jégou, Douze and Schmid, 2011) missed more
than half of the true nearest neighbours, and searching more cells did not help: recall
climbed from 30 percent at one cell to 46 at sixteen, then stayed at 46 all the way to 128
cells while running seven times slower.

To find out why, I counted how many true neighbours were inside the cells being searched.
At 128 cells it was all of them. The search had every answer; the 8-byte codes ranked most
of them out. Re-checking the top hundred candidates against the original vectors took
recall from 46 to 93 percent.

All figures come from running the repo on 100,000 SIFT descriptors.

Narration is an AI voice (Kokoro). Research and script are mine.

## Video files

The 4K renders are on the shared Google Drive:
[Week 8 - where-the-error-lives](https://drive.google.com/drive/folders/1f8Z0WM-Y6Q0zLh6vhZEnR6skycg4RNB3?usp=drive_link)

- `where-the-error-lives.mp4` (16:9, 3840x2160)
- `where-the-error-lives-short.mp4` (9:16, 2160x3840)

## Build record

- Brutalist: commit `2efd40ad` (upstream `3a6d3979`, pulled 18 Nov 2026)
- SHA-256 `where-the-error-lives.mp4`: `a0837681ef1552f32a28d8be2dc94f5fb83a0daa58a898fb26e253a274cc0a9f`
- SHA-256 `where-the-error-lives-short.mp4`: `2eeb62ef7242efc5c9450d19071bf68807241b09e1539b52c97bf7c318cf499f`

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
