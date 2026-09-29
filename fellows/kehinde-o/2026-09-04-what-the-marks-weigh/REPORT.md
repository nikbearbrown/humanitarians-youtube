# Explainer — What the Marks Weigh

**Week:** 1–4 Sep 2026
**Type:** STEM / AI explainer

- **Video:** not yet published
- **Drive:** https://drive.google.com/drive/folders/1V-BZnGQ8a2soQqO7zD2N_atkRd7OYYPp (`Medhavy_Kehinde/STEM Topic/what-the-marks-weigh/`)
- **Frictional log:** [FRICTIONAL.md](FRICTIONAL.md)

## What it covers

How much information a Yoruba diacritic actually carries, measured rather than
asserted, and why that number decides whether restoring tone marks needs a model
or a lookup table.

## Why this topic, this week

It is my own work and my own language, and it makes a general point that the rest
of this fellowship keeps running into: you cannot tell whether a problem is hard
until you measure it. Built on my `ami` repo, a 1.29M-parameter BiLSTM.

## Limits

- The model is trained on MENYO-20k; results are specific to that corpus.
- Character accuracy is not the same as word or sentence accuracy, and the video
  says so rather than quoting the friendlier number.
