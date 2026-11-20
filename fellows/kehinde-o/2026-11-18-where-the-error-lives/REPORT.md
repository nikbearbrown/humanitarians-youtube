# Explainer — Where the Error Lives

**Week:** 8
**Type:** STEM / AI explainer

- **Video:** not yet published
- **Drive:** https://drive.google.com/drive/folders/1f8Z0WM-Y6Q0zLh6vhZEnR6skycg4RNB3?usp=drive_link
- **Frictional log:** [FRICTIONAL.md](FRICTIONAL.md)

## What it covers

My IVF-PQ vector index plateaus near 46 percent recall however many cells it searches, because the error is in the 8-byte codes, not the search. Coverage of true neighbours reaches 100 percent while recall stays at 46. Re-checking the top hundred against the real vectors reaches 93.

## Why this topic, this week

Pairs with Chapters 10 and 13: re-checking against the original is what fixes a compressed summary.

## Limits

- One dataset (100,000 SIFT vectors) and one configuration.
- The re-check needs the original vectors stored.
