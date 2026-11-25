# Overfitting, One Memorized Point at a Time

- **Status:** built; awaiting the fellow's review of narration and timing. Not published.
- **Series:** ML explainers · film 2
- **Channel:** Brutalist Claude cut · **Voice:** Kokoro `am_onyx` (Liam, in for Bear). The narration is AI-generated. · **Greeting:** Hi, Liam
- **Landscape:** 3840×2160 · 2:48 · 11 beats — `claude-liam-overfitting.mp4`
- **Vertical:** 2160×3840 · 2:48 · same beats, re-composed natively for 9:16 — `claude-liam-overfitting-vertical.mp4`
- **Last updated:** 2026-11-24
- **Drive:** https://drive.google.com/drive/folders/1KsCa1LWmcUZyzRHbTyZt7uj0LILO8NgO?usp=drive_link (week folder `2026-11-13`)

## Subject
Eight noisy points around y = 2x. A straight line has train error 0.099 and test error 0.074. A degree-7 curve passes through every point (train 0.000) but its test error is 0.221. Test error turns around while training error keeps falling; more data (8 to 40 points) closes the gap; noise sets a floor of about 0.0625.

## Notes
- Standard material; numpy polyfit, seeds 3, 99 and 5 in experiment.py.
- Rendered MP4s are on Drive, not in this repository. Everything needed to rebuild them is here: the beat sheet, scene code, numbers, checks and the fact-check.
- Vertical sources are in [`vertical/`](vertical/).
- **Required opening line:** "Hi, I am Rohan, and this video is about machine learning." — not yet in this video (the finished masters start with the AI narrator's own greeting). To be added in a later re-record if the supervisor asks.
