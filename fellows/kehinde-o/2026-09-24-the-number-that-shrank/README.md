# The Number That Shrank

**Volunteer:** Kehinde Obidele

A STEM explainer built on my own repo, [adverse-event-pipeline](https://github.com/Kenny0bi/adverse-event-pipeline):
a pharmacovigilance pipeline that screens the FDA's adverse event database for drug safety
signals. The video is about one idea, which is the idea the whole field turns on.

## Video Files

On the shared Google Drive under `Medhavy_Kehinde/STEM Topic/the-number-that-shrank/`:

**[Google Drive folder](https://drive.google.com/drive/folders/1V-BZnGQ8a2soQqO7zD2N_atkRd7OYYPp)**

| File | Aspect | Spec |
|---|---|---|
| `the-number-that-shrank.mp4` | 16:9 | 3840x2160, 30fps, 2m 46s |
| `the-number-that-shrank-short.mp4` | 9:16 | 2160x3840, 30fps, native render |

## The one idea

A ratio is not evidence.

Observed over expected tells you how big an effect looks. How much data sits underneath it
tells you how much to believe it. Those are different quantities, and the biggest ratios in
any database come from the thinnest evidence.

Empirical Bayes shrinkage is how you handle that honestly: it pulls a thin-evidence ratio
back toward the null and leaves a well-supported one almost untouched.

## The two examples, from the actual run

| Pair | Observed | Expected | Crude ratio | After shrinkage | Survives |
|---|---|---|---|---|---|
| Warfarin, GI haemorrhage | 62 | 2.93 | 21.2 | 21.0 | **99%** |
| Esculin, heart sounds | 16 | ~0.0003 | 55,218 | 2,209 | **4%** |

Same shrink applied to both. Only one of them had anything to lose.

## What the pipeline is

Four quarters of FDA FAERS: 1,619,665 raw reports, deduplicated to **1,214,808 cases**,
giving **472,082 drug-event pairs** scored by four published disproportionality methods
(PRR, ROR, BCPNN, MGPS).

## The part I am proudest of

The pipeline audits itself. Six drug-event pairs with decades of established causality are
written into the run as positive controls: warfarin with GI haemorrhage, clozapine with
agranulocytosis, amiodarone with hypothyroidism, metoclopramide with tardive dyskinesia,
atorvastatin with rhabdomyolysis, allopurinol with Stevens-Johnson syndrome.

If the run fails to rediscover any one of them, it halts and ships nothing. All six came
back, on all four methods.

## What it still misses

A signal can be real and still be mostly demographics. The top 100 signals go through an
age and sex adjusted re-estimate, and **77 of them move by more than 1.5x**. That is why
the adjusted numbers ship with the results instead of being left as future work.

## A note on how the video was made

Every figure in the video was recomputed from the repo's committed outputs
(`results/summary.json`, `results/positive_controls.csv`, `results/signals_top1000.csv`)
during the build, not copied from the repo README. The trace is in `FACTCHECK.md`.

The two equations are rendered as structured math, not as text on a card.

## Not a safety claim

Disproportionality is not causality. FAERS reporting is voluntary, and the counts are
counts of reports, not of patients. Esculin appears only as an example of thin evidence.

## Files in this repo

- `beat_sheet.json` — the script
- `PEDAGOGY.md` — narration gate, VERDICT: PASS
- `FACTCHECK.md` — every on-screen claim, its source, and the algebra check
- `SHOTLIST.md` — typed work order
- `PROMPTS.md` — the on-screen prompts

Media files are not committed.
