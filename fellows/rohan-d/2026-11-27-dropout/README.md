# Dropout, One Silenced Unit at a Time

- **Status:** built; awaiting the fellow's review of narration and timing. Not published.
- **Series:** ML explainers · extra film
- **Channel:** Brutalist Claude cut · **Voice:** Kokoro `am_onyx` (Liam, in for Bear). The narration is AI-generated. · **Greeting:** Hi, Liam
- **Landscape:** 3840×2160 · 2:46 · 11 beats — `claude-liam-dropout.mp4`
- **Vertical:** 2160×3840 · 2:46 · same beats, re-composed natively for 9:16 — `claude-liam-dropout-vertical.mp4`
- **Last updated:** 2026-11-24
- **Drive:** https://drive.google.com/drive/folders/1KsCa1LWmcUZyzRHbTyZt7uj0LILO8NgO?usp=drive_link (week folder `2026-11-27`)

## Subject
Eight activations 1 to 8 sum to 36. A random mask keeps 1, 5, 6, 7 (sum 19, scaled 38). Ten thousand masks average 35.98, unscaled they average 18; 256 masks average exactly 36 for a plain sum; noise grows with p (4.8, 14.3, 42.9).

## Notes
- Srivastava et al. (2014) for the method; the numbers are my own computations (seeds 6, 11, 3).
- Rendered MP4s are on Drive, not in this repository. Everything needed to rebuild them is here: the beat sheet, scene code, numbers, checks and the fact-check.
- Vertical sources are in [`vertical/`](vertical/).
- **Required opening line:** "Hi, I am Rohan, and this video is about machine learning." — not yet in this video (the finished masters start with the AI narrator's own greeting). To be added in a later re-record if the supervisor asks.
