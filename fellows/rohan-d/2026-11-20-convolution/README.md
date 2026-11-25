# Convolution, One Window at a Time

- **Status:** built; awaiting the fellow's review of narration and timing. Not published.
- **Series:** ML explainers · film 4
- **Channel:** Brutalist Claude cut · **Voice:** Kokoro `am_onyx` (Liam, in for Bear). The narration is AI-generated. · **Greeting:** Hi, Liam
- **Landscape:** 3840×2160 · 2:43 · 11 beats — `claude-liam-convolution.mp4`
- **Vertical:** 2160×3840 · 2:43 · same beats, re-composed natively for 9:16 — `claude-liam-convolution-vertical.mp4`
- **Last updated:** 2026-11-24
- **Drive:** https://drive.google.com/drive/folders/1KsCa1LWmcUZyzRHbTyZt7uj0LILO8NgO?usp=drive_link (week folder `2026-11-20`)

## Subject
A 3 by 3 kernel with columns -1, 0, 1 slides over a 6 by 6 image whose rows are 0 0 0 9 9 9. The output rows read 0, 27, 27, 0. One kernel of 9 weights replaces 576 in a fully connected layer, and each unpadded layer shrinks the map by 2.

## Notes
- Standard material (cross-correlation as used in deep learning); numpy, experiment.py.
- Rendered MP4s are on Drive, not in this repository. Everything needed to rebuild them is here: the beat sheet, scene code, numbers, checks and the fact-check.
- Vertical sources are in [`vertical/`](vertical/).
- **Required opening line:** "Hi, I am Rohan, and this video is about machine learning." — not yet in this video (the finished masters start with the AI narrator's own greeting). To be added in a later re-record if the supervisor asks.
