# Batch Normalization, One Rescale at a Time

- **Status:** built; awaiting the fellow's review of narration and timing. Not published.
- **Series:** ML explainers · film 6
- **Channel:** Brutalist Claude cut · **Voice:** Kokoro `am_onyx` (Liam, in for Bear). The narration is AI-generated. · **Greeting:** Hi, Liam
- **Landscape:** 3840×2160 · 3:00 · 11 beats — `claude-liam-batch-norm.mp4`
- **Vertical:** 2160×3840 · 3:00 · same beats, re-composed natively for 9:16 — `claude-liam-batch-norm-vertical.mp4`
- **Last updated:** 2026-11-24
- **Drive:** https://drive.google.com/drive/folders/1KsCa1LWmcUZyzRHbTyZt7uj0LILO8NgO?usp=drive_link (week folder `2026-11-27`)

## Subject
Two features, [2,4,6,8] and [200,400,600,800], normalize to the same four numbers. On a small regression the raw loss has condition number 3,182,113 and has not converged in 100,000 steps; normalized it is 1.4 and converges in 4 steps. Gamma and beta restore scale, and small batches make noisy statistics.

## Notes
- Ioffe and Szegedy (2015) for the method; the conditioning numbers are my own computations (seed 4).
- Rendered MP4s are on Drive, not in this repository. Everything needed to rebuild them is here: the beat sheet, scene code, numbers, checks and the fact-check.
- Vertical sources are in [`vertical/`](vertical/).
- **Required opening line:** "Hi, I am Rohan, and this video is about machine learning." — not yet in this video (the finished masters start with the AI narrator's own greeting). To be added in a later re-record if the supervisor asks.
