# Overfitting, When a Perfect Score Lies

- **Status:** final — delivered (4K master, gates passed)
- **Series:** STEM AI explainer series · ai-explainer format
- **Channel:** @NikBearBrown (claude-liam) · **Voice:** Kokoro `am_onyx` (Liam, in for Bear) · **Greeting:** "Namaste, Liam"
- **Long:** 3840×2160 · 3:19 · 11 beats — `claude-liam-overfitting.mp4`
- **Last updated:** 2026-11-23

## Subject

Why a zero training error is not proof of a good model. Sixteen noisy points from sin(πx), graded by mean squared error: degree 15 scores 0 in training and 9,882.6 on 1,000 test points, while degree 3 scores 0.0586 and 0.0471. The film then tests two simple stories: more data tames the same degree-15 model, and a held-out score used to choose the model comes in optimistic 69.6% of the time.

## Notes

- Built in the ai-explainer format from the start: cold open in the Claude composer, hesitant-writer summary, six Manim scenes, verdict recap, Your Turn, title outro.
- Every on-screen number comes from `demo/overfit_demo.py` (pure Python + numpy, about 7 s; dataset seed 15). The demo was extended before audio for the B06 refits and B07 grids, with existing values unchanged.
- GATE T fix on B03: the hat on f̂ measured 38 px, under the 41 px floor. The prediction is now written f(xᵢ), with the tag "model's guess"; the narration is unchanged.
- Terracotta appears only on non-text shapes, because GATE T reads terracotta text and arrow tips as 2.74:1 on cream.
