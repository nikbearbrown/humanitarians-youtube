# K-Means, One Reassignment at a Time

- **Status:** built; awaiting the fellow's review of narration and timing. Not published.
- **Series:** ML explainers · film 7
- **Channel:** Brutalist Claude cut · **Voice:** Kokoro `am_onyx` (Liam, in for Bear). The narration is AI-generated. · **Greeting:** Hi, Liam
- **Landscape:** 3840×2160 · 2:59 · 11 beats — `claude-liam-kmeans.mp4`
- **Vertical:** 2160×3840 · 2:59 · same beats, re-composed natively for 9:16 — `claude-liam-kmeans-vertical.mp4`
- **Last updated:** 2026-11-24
- **Drive:** https://drive.google.com/drive/folders/1KsCa1LWmcUZyzRHbTyZt7uj0LILO8NgO?usp=drive_link (week folder `2026-11-27`)

## Subject
Seven points, two centers starting at (1,1) and (5,6) settle at (1.25,1.5) and (3.9,5.1) in two rounds; inertia falls from 19.25 to 8.53 and never rises. Four rectangle corners show two stable answers, inertia 4 and 16, depending on the start.

## Notes
- Lloyd's algorithm; numpy, deterministic, experiment.py.
- Rendered MP4s are on Drive, not in this repository. Everything needed to rebuild them is here: the beat sheet, scene code, numbers, checks and the fact-check.
- Vertical sources are in [`vertical/`](vertical/).
- **Required opening line:** "Hi, I am Rohan, and this video is about machine learning." — not yet in this video (the finished masters start with the AI narrator's own greeting). To be added in a later re-record if the supervisor asks.
