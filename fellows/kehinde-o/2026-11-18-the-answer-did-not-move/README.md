# The Answer Did Not Move

**Volunteer:** Kehinde Obidele  
**Week:** 11  
**Type:** STEM / AI explainer  
**Runtime:** 2m04s  
**Source project:** github.com/Kenny0bi/fuse  

My graph compiler rewrites neural networks to run leaner, and every rewrite promises the
answers did not change. I did not want to take the tool's word for it.

On resnet18 the compiler takes 141 operations down to 32, folding all 20 batch-norm layers
into the convolutions before them. I ran the same image through the original and rewritten
networks and compared all 1,000 outputs: the largest difference was about one millionth
on outputs as large as 4.7, with the same top prediction. Because both runs used my own
runtime, I had first checked that runtime against onnxruntime, which I did not write. They
agree to about two millionths.

All figures come from running the repo's code.

Narration is an AI voice (Kokoro). Research and script are mine.

## Video files

The 4K renders are on the shared Google Drive:
[Week 11 - the-answer-did-not-move](https://drive.google.com/drive/folders/1xuJiVtZS1ToZprp0ChjTPXiLxS5OCGc5?usp=drive_link)

- `the-answer-did-not-move.mp4` (16:9, 3840x2160)
- `the-answer-did-not-move-short.mp4` (9:16, 2160x3840)

## Build record

- Brutalist: commit `cbb78906` (upstream `3a6d3979`, pulled 18 Nov 2026)
- SHA-256 `the-answer-did-not-move.mp4`: `6265099123adef18fed2d5ec75c5b3700625bd51c996cf5e72a0a743bb2046a9`
- SHA-256 `the-answer-did-not-move-short.mp4`: `cc07aa438a74d3831ac2ad6458695c3b04ff3cd30b853c81151ce20ebf166b9e`

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
- `export_models.py`: exports the ONNX models the evidence script reads

Media files are not committed.
