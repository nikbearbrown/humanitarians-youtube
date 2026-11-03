# Why Your Embeddings Lie About Similarity

An AI/STEM explainer on a hidden failure mode of vector search: **"close in vector
space" is not the same as "actually relevant."** Cosine similarity can rank a
wrong-but-similarly-worded chunk above the chunk that actually answers the question.

## The teach
Similarity is a **measurement, not a truth**. Embeddings measure surface pattern
(which words appear, how often) — not meaning, and not correctness. Negation and
word order barely move the score, so "X approves Y" and "X rejects Y" can sit
almost on top of each other. In a RAG system this fails silently: a high similarity
score on the wrong chunk produces a confident, fluent, wrong answer with no error
and no warning.

## Structure (ai-explainer, 8 beats)
Ask → BLUF → Illustrate → Mechanism → Consequence → Verdict → Your Turn → Outro

## Production notes
- **Voice:** Kokoro `am_onyx` (fellow-documented voice for this report series).
- **Greeting:** "Hello Amruta"
- **Series:** AI/STEM Explainers
- **Channel:** @HumanitariansAI
- **Rebuild:** local, audio-first, via the brutalist.art toolkit. The beat sheet
  drives narration; measured audio is the clock; visual beats compile from the
  beat sheet. Rendered MP3/MP4 are intentionally not committed (root .gitignore).

## Files
- `beat_sheet.json` — the source of truth for this video
- `README.md` — this file
