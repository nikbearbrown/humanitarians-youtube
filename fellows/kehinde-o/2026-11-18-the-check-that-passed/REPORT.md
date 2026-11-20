# Explainer — The Check That Passed

**Week:** 12
**Type:** STEM / AI explainer

- **Video:** not yet published
- **Drive:** https://drive.google.com/drive/folders/1YE452Ql5N9XSulackFiN93JbQBVtfToC?usp=drive_link
- **Frictional log:** [FRICTIONAL.md](FRICTIONAL.md)

## What it covers

My two-tower recommender passed its gradient check and still lost to a popularity counter, 3.1 against 5.8 percent recall at ten, because in-batch negatives punish popular films. The logQ correction took it to 8.6.

## Why this topic, this week

Pairs with Chapters 16, 11 and 15: a passing check only answers the question it asks.

## Limits

- One temporal split of MovieLens 25M.
- My README's figure for the uncorrected model (0.018) does not reproduce; the measured 0.031 is used.
