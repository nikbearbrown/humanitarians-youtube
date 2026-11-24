# Cross-Entropy, One Surprise at a Time

- **Status:** built; awaiting the fellow's review of narration and timing. Not published.
- **Series:** ML explainers · film 1 (format of the reference films)
- **Channel:** Brutalist Claude cut · **Voice:** Kokoro `am_onyx` (Liam, in for Bear). The narration is AI-generated. · **Greeting:** Hi, Liam
- **Landscape:** 3840×2160 · 3:06 · 11 beats — `claude-liam-cross-entropy.mp4`
- **Vertical:** 2160×3840 · 3:06 · same beats, re-composed natively for 9:16 — `claude-liam-cross-entropy-vertical.mp4`
- **Last updated:** 2026-11-24
- **Drive:** https://drive.google.com/drive/folders/1KsCa1LWmcUZyzRHbTyZt7uj0LILO8NgO?usp=drive_link (week folder `2026-11-13`)

## Subject
How a classifier turns scores into a loss: softmax shares 66/24/10, loss minus-log of the right answer's share (0.417), why a confident mistake costs 4.6 while a hedge costs 0.7, the slope share-minus-answer, and the clipping floor (27.63).

## Notes
- Standard textbook definition; every number recomputed in experiment.py.
- Rendered MP4s are on Drive, not in this repository. Everything needed to rebuild them is here: the beat sheet, scene code, numbers, checks and the fact-check.
- Vertical sources are in [`vertical/`](vertical/).
- **Required opening line:** "Hi, I am Rohan, and this video is about machine learning." — not yet in this video (the finished masters start with the AI narrator's own greeting). To be added in a later re-record if the supervisor asks.
