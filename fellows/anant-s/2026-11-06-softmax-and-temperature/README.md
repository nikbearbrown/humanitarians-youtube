# Softmax and Temperature, Explained

- **Status:** final — delivered (4K master, gates passed)
- **Series:** STEM AI explainer series · film 2 of 7
- **Channel:** @NikBearBrown (claude-liam brand) · **Voice:** Kokoro `am_onyx` (Liam, in for Bear) · **Greeting:** "Bonjour, Liam"
- **Long:** 3840×2160 · 3:57 · 13 beats — `claude-liam-softmax-temperature.mp4`
- **Last updated:** 2026-11-23

## Subject

Why the same prompt can give a different answer every time. A model scores every next token (logits), softmax turns the scores into probabilities, temperature divides the logits first to sharpen or flatten them, and a sampler rolls weighted dice. The film ends on the limit of the knob: temperature changes the spread, never the ranking.

## Notes

- Built in the ai-explainer format from the start: composer cold open, hesitant-writer summary, eight Manim body scenes (B02–B09), Verdict recap, Your Turn, title outro.
- Every number on screen comes from `demo/softmax_demo.py` (pure Python + numpy, seed 2). The logits are constructed, not from a real model, and are labelled so on screen (B02, B09).
- The 10,000-draw sampling method was changed after a 3.4 σ seed outlier; the change is disclosed in BUILD-LOG and FACTCHECK #18.
- The first 4K run failed GATE V (B01, B06) and GATE T (B02, B03, B05, B06, B08, B09); all were fixed and re-checked before the final on 2026-11-23.
