# Explainer — Every Look Was Right

**Week:** 10
**Type:** STEM / AI explainer

- **Video:** not yet published
- **Drive:** https://drive.google.com/drive/folders/1uzsEqyuOdUHjgOWCFHAsc-94NnuNb2bm?usp=drive_link
- **Frictional log:** [FRICTIONAL.md](FRICTIONAL.md)

## What it covers

Peeking at A/B tests on 1,000 experiments with no real effect: 4.0 percent false alarms checking once, 18.7 checking ten times. My engine's sequential test gave 12.9 because it re-estimates the control rate each look; fixed in advance, 3.2. I then rebuilt the engine's test to work on pairs of users, which needs no estimate under the null: 1.7 percent on the same experiments.

## Why this topic, this week

Pairs with Chapters 31 and 32: the trusted number hid the error.

## Limits

- The textbook-style test was fixed at the true rate, which a real analyst would estimate from history.
- The paired test's 1.7 percent is at the same ten looks; checked after every pair it stays between 3.3 and 3.9 percent.
