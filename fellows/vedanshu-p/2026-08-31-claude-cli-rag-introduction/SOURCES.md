# SOURCES — Watch Retrieval Fix A Stale Answer.

## Book source

- Book: *RAG Foundations* (author: Vedanshu Daxesh Patel)
- Chapter: `chapters/01-introduction.md` — "Introduction: What RAG Is and Why It Exists"
- Same source as the sibling ai-explainer reel `claude-liam-rag-introduction`;
  full citation list (Lewis et al. 2020, Ovadia et al. 2024, Soudani et al.
  2024, Petroni et al. 2019) carries over unchanged — see that reel's
  `SOURCES.md` for the complete bibliography.

## Code (THE ACTUAL-CODE LAW — real, run, not fabricated)

- `code/naive_answer.py` — toy parametric-only model; written for this reel,
  run for real via `python code/naive_answer.py`. Output captured verbatim
  into beat B04.
- `code/rag_answer.py` — same toy model with a `retrieve()` step added; run
  for real via `python code/rag_answer.py`. Output captured verbatim into
  beat B07.
- Both scripts are free, local, dependency-free (Python stdlib only) — no
  API calls, no cost, consistent with Fellow-tier "no money, ever."

## Anecdote used as the running example (B00–B08)

- The help-desk / stale sick-leave-policy scenario, sourced from the
  chapter's "Opening" and "Worked example" sections — same anecdote as the
  sibling reel, now demonstrated as a literal running program instead of an
  illustrated diagram. The specific numbers (10 → 15 days, "8 months ago")
  are invented FOR THE DEMO CODE (the chapter doesn't give exact day counts),
  used consistently between both scripts and both reels' narration.
