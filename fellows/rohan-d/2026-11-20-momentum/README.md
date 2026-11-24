# Momentum, One Remembered Step at a Time

- **Status:** built; awaiting the fellow's review of narration and timing. Not published.
- **Series:** ML explainers · film 3
- **Channel:** Brutalist Claude cut · **Voice:** Kokoro `am_onyx` (Liam, in for Bear). The narration is AI-generated. · **Greeting:** Hi, Liam
- **Landscape:** 3840×2160 · 3:00 · 11 beats — `claude-liam-momentum.mp4`
- **Vertical:** 2160×3840 · 3:00 · same beats, re-composed natively for 9:16 — `claude-liam-momentum-vertical.mp4`
- **Last updated:** 2026-11-24
- **Drive:** https://drive.google.com/drive/folders/1KsCa1LWmcUZyzRHbTyZt7uj0LILO8NgO?usp=drive_link (week folder `2026-11-20`)

## Subject
On the loss 0.5(x^2 + 25y^2) from (4, 1), plain descent bounces across the valley and needs 47 steps to reach loss 0.01; momentum with beta 0.5 needs 20; beta 0.9 needs 53; beta 0.99 does not settle in 200 steps. The film shows why: swings across the valley cancel in the velocity while steady slopes along it add up.

## Notes
- Heavy-ball (Polyak) momentum; numpy, deterministic, experiment.py.
- Rendered MP4s are on Drive, not in this repository. Everything needed to rebuild them is here: the beat sheet, scene code, numbers, checks and the fact-check.
- Vertical sources are in [`vertical/`](vertical/).
- **Required opening line:** "Hi, I am Rohan, and this video is about machine learning." — not yet in this video (the finished masters start with the AI narrator's own greeting). To be added in a later re-record if the supervisor asks.
