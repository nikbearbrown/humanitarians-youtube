# How RAG Works

- **Status:** final — delivered (4K master, gates passed)
- **Series:** STEM AI explainer series · film 7
- **Channel:** @NikBearBrown (claude-liam brand) · **Voice:** Kokoro `am_onyx` (Liam, in for Bear) · **Greeting:** "Hello, Liam"
- **Long:** 3840×2160 · 3:36 · 18 beats — `show-tell-how-rag-works.mp4`
- **Last updated:** 2026-11-24

## Subject

How a chatbot can answer from documents it has never read. One question ("How long do I have to return a laptop?") is carried through every step of a toy RAG pipeline: chunk, embed, store, retrieve, paste into the prompt, answer. Then a stale FAQ page wins the search and the answer goes wrong, and the fix is in the store, not the model.

## Notes

- First built in the show-tell format (2026-11-22/23); converted to ai-explainer on 2026-11-24 at my request: new B00 cold open, B01 summary and BVDT recap; body renumbered B00–B12 → B10–B22 with no content change.
- Every score comes from `demo/rag_demo.py` (deterministic TF-IDF cosine in numpy, no models). The answer step is illustrated, not executed, and tagged "illustrated" on screen.
- In the show-tell build, the B06 search card failed GATE T and became a Manim ranking scene (now `B16_Ranking`); dark answer-card squiggles were softened to grey.
- The 21 million passages figure is attributed to Lewis et al. 2020, the paper that named RAG.
