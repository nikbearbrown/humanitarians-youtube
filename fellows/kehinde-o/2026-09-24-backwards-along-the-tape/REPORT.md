# Explainer — Backwards Along the Tape

**Week:** 21–25 Sep 2026
**Type:** STEM / AI explainer

- **Video:** not yet published
- **Drive:** https://drive.google.com/drive/folders/1V-BZnGQ8a2soQqO7zD2N_atkRd7OYYPp (`Medhavy_Kehinde/STEM Topic/backwards-along-the-tape/`)
- **Frictional log:** [FRICTIONAL.md](FRICTIONAL.md)

## What it covers

What `backward()` actually computes, built on my own tensor autograd engine written
from scratch on raw NumPy and used to train a 624K-parameter GPT.

## Why this topic, this week

It pairs with the Chapter 30 report because both are about proving rather than
asserting. The engine does not claim its gradients are right; it matches PyTorch
to 2.682e-07 over 300 steps with the weights copied bit for bit.

## Limits

- No claim that this engine competes with PyTorch on speed or coverage. The
  measured claim is agreement of gradients and loss curves.
- At initialisation the trained GPT sits slightly worse than uniform guessing
  (4.49 against ln 65 = 4.17). The video states that rather than smoothing it.
- Every figure was read from the repository's committed run logs; see FACTCHECK.md.
