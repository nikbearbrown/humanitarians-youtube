# Why Attention Divides By The Square Root

- **Status:** built; awaiting the fellow's review of narration and timing. Not published.
- **Series:** TL;DR · Attention Is All You Need (section S2)
- **Channel:** Brutalist Claude cut · **Voice:** Kokoro `am_onyx` (Liam, in for Bear). The narration is AI-generated. · **Greeting:** Hola, Liam
- **Landscape:** 3840×2160 · 3:41 · 16 beats — `tldr-attention-scaling.mp4`
- **Vertical:** 2160×3840 · 3:41 · same beats, re-composed natively for 9:16 — `tldr-attention-scaling-vertical.mp4`
- **Last updated:** 2026-11-23
- **Drive:** https://drive.google.com/drive/folders/1KsCa1LWmcUZyzRHbTyZt7uj0LILO8NgO?usp=drive_link (week folder `2026-11-13`)

## Subject
The Transformer's scaled dot-product attention divides scores by the square root of the key length. The film shows why: longer vectors give wider scores, wide scores make softmax pick one winner and starve the gradient, a fixed divisor fits one length only, and dividing by the square root keeps the spread constant.

## Notes
- Source: Vaswani et al., 'Attention Is All You Need' (2017), section 3.2.1. Numbers recomputed in experiment.py, naive_fixed_divisor.py and bhtf_check.py (seed 7).
- Rendered MP4s are on Drive, not in this repository. Everything needed to rebuild them is here: the beat sheet, scene code, numbers, checks and the fact-check.
- Vertical sources are in [`vertical/`](vertical/).
- **Required opening line:** "Hi, I am Rohan, and this video is about machine learning." — not yet in this video (the finished masters start with the AI narrator's own greeting). To be added in a later re-record if the supervisor asks.
