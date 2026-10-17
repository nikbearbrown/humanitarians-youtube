# Explainer — The Target That Moved

**Week:** 7–11 Sep 2026
**Type:** STEM / AI explainer

- **Video:** not yet published
- **Drive:** https://drive.google.com/drive/folders/1V-BZnGQ8a2soQqO7zD2N_atkRd7OYYPp (`Medhavy_Kehinde/STEM Topic/the-target-that-moved/`)
- **Frictional log:** [FRICTIONAL.md](FRICTIONAL.md)

## What it covers

Why my deep Q-learning agent for LunarLander scored worse than random, and why
the cause was a moving target rather than insufficient training.

## Why this topic, this week

Measured over 100 greedy episodes the trained model scored -391; a random policy
scores -213 on the same environment. The agent computes its learning target with
the same network it is updating, so the target moves every time it learns.

## Limits

- The video reports the diagnosis, not a repaired result. I did not retrain to
  convergence with the target network in place.
- One environment, one seed regime.
