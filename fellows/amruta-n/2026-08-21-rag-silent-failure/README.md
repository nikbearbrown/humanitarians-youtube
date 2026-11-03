# RAG's Silent Failure

An AI/STEM explainer on the most dangerous failure mode of Retrieval-Augmented
Generation: **when retrieval quietly returns the wrong context, the model answers
confidently and wrongly — with no error and no warning.**

## The teach
RAG feels safe because it "grounds" answers in retrieved documents. But retrieval
can fail silently: it pulls chunks that *look* relevant but aren't, and the language
model dutifully builds a fluent, confident answer on that bad foundation. Nothing
crashes. Nothing flags a problem. The failure is invisible unless you check the
retrieved context yourself. The lesson: trust the *retrieval*, not just the answer —
a confident RAG answer is only as good as the chunks it was given.

## Production notes
- **Voice:** Kokoro `am_onyx` (fellow-documented voice for this report series).
- **Series:** AI/STEM Explainers
- **Channel:** @HumanitariansAI
- **Rebuild:** local, audio-first, via the brutalist.art toolkit. The beat sheet
  drives narration; measured audio is the clock; visual beats compile from the
  beat sheet. Rendered MP3/MP4 are intentionally not committed (root .gitignore).

## Files
- `beat_sheet.json` — the source of truth for this video (copy in from your render folder)
- `README.md` — this file
