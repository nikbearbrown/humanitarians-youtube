# The Check That Passed

**Volunteer:** Kehinde Obidele  
**Week:** 12  
**Type:** STEM / AI explainer  
**Runtime:** 2m18s  
**Source project:** github.com/Kenny0bi/pulse-recsys  

My two-tower recommender passed its gradient check and still lost to a popularity counter.
On 6,198 test users, the counter's recall@10 was 5.8 percent and my model's was 3.1.

A gradient check only confirms that the code computes the slope of its objective
correctly. My objective was wrong: in-batch softmax treats popular films as wrong answers
in proportion to how often they appear, so the model learned to avoid them. The logQ
correction (Yi et al., 2019) subtracts each film's log sampling frequency during training.
Same model, same data: 3.1 percent became 8.6.

All figures come from running the repo's training and evaluation code.

Narration is an AI voice (Kokoro). Research and script are mine.

## Video files

The 4K renders are on the shared Google Drive:
[Week 12 - the-check-that-passed](https://drive.google.com/drive/folders/1YE452Ql5N9XSulackFiN93JbQBVtfToC?usp=drive_link)

- `the-check-that-passed.mp4` (16:9, 3840x2160)
- `the-check-that-passed-short.mp4` (9:16, 2160x3840)

## Build record

- Brutalist: commit `cbb78906` (upstream `3a6d3979`, pulled 18 Nov 2026)
- SHA-256 `the-check-that-passed.mp4`: `56eb09dae7cdc3c1f3d4aa0d9fb6e28b9c817064d560e778e2b2cd9446195617`
- SHA-256 `the-check-that-passed-short.mp4`: `44fa105c4f7c29e6aa160efa76366ef90781859c6202e4ee8c3774a384090bf9`

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
