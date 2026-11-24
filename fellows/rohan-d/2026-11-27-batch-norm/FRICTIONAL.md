# Frictional log — ML explainer: batch normalization and the condition number of the loss

> DRAFT written from the real build record. Edit it into your own words and add what you understand now; the guide says entries are written as the work happens and never rewritten afterwards.

## 2026-11-24 — Batch Normalization, One Rescale at a Time

- **Drive:** https://drive.google.com/drive/folders/1KsCa1LWmcUZyzRHbTyZt7uj0LILO8NgO?usp=drive_link (week folder `2026-11-27`)
- **Evidence of commit:** [add the commit link once this folder is committed]

**What I was working on.** Two features, [2,4,6,8] and [200,400,600,800], normalize to the same four numbers. On a small regression the raw loss has condition number 3,182,113 and has not converged in 100,000 steps; normalized it is 1.4 and converges in 4 steps. Gamma and beta restore scale, and small batches make noisy statistics.

**What I tried, and what I expected.**
- I expected to match the format of the reference films: composer ask, a corrected overview, numbers-first Manim beats, a recap, a your-turn prompt and the locked outro.
- I expected each beat to pass the toolkit's checks (layout audit, frame QC, type size) on the first or second render.

**Where it resisted, and what was done next.**
- I accidentally added row rules to the wrong beat with a global text replace, which put lines through the numbers. Claude found it by looking at the audit frame, and removed them.
- The portrait build was blocked by the type check: the typeset equations render too small in the tall frame. Claude wrote the portrait formulas as large text instead and kept the typeset ones in the landscape cut.
- My own build script wrongly marked the vertical master as done when the type gate had blocked it. I caught it from the log and corrected the table.
- Frames were underfilled until the two features were put on wide cards.

**What Claude contributed, and what I did with it.**
- Claude designed the example, computed the numbers and wrote everything; the batch-norm-versus-covariate-shift debate is noted in FACTCHECK as an editorial choice.
- Accepted: the film structure, the computed numbers (each recomputed in code), and the fixes above.
- Rejected / changed: [add what you rejected or changed in your own words]

**What I understand now, and what I still do not.**
- Understood: [write in your own words what you now understand about the topic]
- Not understood / not verified:
- The portrait film shows formulas as text, not typeset.
- Delivery not judged by ear.
