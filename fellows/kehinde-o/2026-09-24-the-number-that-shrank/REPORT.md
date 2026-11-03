# Explainer — The Number That Shrank

**Week:** 21–25 Sep 2026
**Type:** STEM / AI explainer

- **Video:** not yet published
- **Drive:** https://drive.google.com/drive/folders/1V-BZnGQ8a2soQqO7zD2N_atkRd7OYYPp (`Medhavy_Kehinde/STEM Topic/the-number-that-shrank/`)
- **Frictional log:** [FRICTIONAL.md](FRICTIONAL.md)

## What it covers

Drug safety signal detection on 1,214,808 deduplicated FDA adverse event cases:
why a disproportionality ratio is only as good as the evidence behind it.

## Why this topic, this week

It is the same subject as the Chapter 25 report approached from the data side, and
it corrects an assumption I made when I built the pipeline. Warfarin with
gastrointestinal bleeding keeps 99 percent of its crude ratio after empirical-Bayes
shrinkage; esculin with heart sounds keeps 4 percent.

## Limits

- Disproportionality is not causality. FAERS reporting is voluntary and the counts
  are counts of reports, not patients. The video states this on screen.
- Esculin appears as an example of thin evidence, not as a safety claim.
- Every figure was recomputed from the repository's committed run outputs; see
  FACTCHECK.md for the file-by-file trace.
