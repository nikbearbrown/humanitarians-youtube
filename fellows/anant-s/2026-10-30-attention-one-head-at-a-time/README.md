# Attention, One Head at a Time

- **Status:** final — delivered (4K master, gates passed)
- **Series:** STEM AI explainers · ai-explainer format
- **Channel:** @NikBearBrown · **Voice:** Kokoro `am_onyx` · **Greeting:** Hello, Liam
- **Long:** 3840×2160 · 4:21 · 15 beats — `tldr-attention.mp4`
- **Last updated:** 2026-11-24

## Subject

How one attention head lets each word use the words around it. One four-word sentence, "cats chase small dogs", worked by hand with toy numbers: request against offer gives a score, scores ÷ 2 and softmax give a heat map, and each word comes out as a weighted average of the value points. Then the names query, key and value, the one-line equation, and the limit: attention alone can't see word order.

## Notes

- First built in the TL;DR format (greeting "Konnichiwa, Liam"). On 2026-11-24 it was converted to the ai-explainer format: a new B00 cold open and B01 summary replaced the four TL;DR cards; the body (B10–B19), Verdict, Your Turn and outro are unchanged.
- Every number on screen comes from `demo/attention_demo.py` (numpy, seed 290537). Sizes are d_model 4, d_k 4, d_v 2, so values and outputs can be drawn as points; the film says real heads use 64.
- The 4K build failed GATE T twice before the first final (wide terracotta boxes read as text; a spotlight ring read as a text run). Fixed in `scenes.py`; no validator was changed.
