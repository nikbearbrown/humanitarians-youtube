# Explainer — The Answer Did Not Move

**Week:** 11
**Type:** STEM / AI explainer

- **Video:** not yet published
- **Drive:** https://drive.google.com/drive/folders/1xuJiVtZS1ToZprp0ChjTPXiLxS5OCGc5?usp=drive_link
- **Frictional log:** [FRICTIONAL.md](FRICTIONAL.md)

## What it covers

My graph compiler takes resnet18 from 141 operations to 32. Original and rewritten outputs differ by about one millionth; my runtime agrees with onnxruntime to about two millionths; the normalization fold is exact algebra.

## Why this topic, this week

Pairs with Chapters 5, 7 and 12: check the checker, not only its verdict.

## Limits

- The network is untrained, as the repo exports it; this is about preserving the function, not accuracy.
