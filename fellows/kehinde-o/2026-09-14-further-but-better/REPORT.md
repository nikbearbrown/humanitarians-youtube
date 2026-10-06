# Explainer — Further, But Better

**Week:** 14–18 Sep 2026
**Type:** STEM / AI explainer

- **Video:** not yet published
- **Drive:** https://drive.google.com/drive/folders/1V-BZnGQ8a2soQqO7zD2N_atkRd7OYYPp (`Medhavy_Kehinde/STEM Topic/further-but-better/`)
- **Frictional log:** [FRICTIONAL.md](FRICTIONAL.md)

## What it covers

Post-training quantization, measured across 34 configurations on GPT-2: why the
method that ends further from the original weights produces better outputs.

## Why this topic, this week

It is a result that sounds like a mistake until you separate the two things being
measured. Distance in weight space is not damage in loss space, and that
distinction is the whole reason the better method wins.

## Limits

- GPT-2 only. Whether the ordering holds at larger scale is not shown here.
- The animation is my own Manim scene, re-rendered at 4K rather than upscaled.
