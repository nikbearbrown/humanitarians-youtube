# Frictional log — RAG Architecture

## 2026-09-21 — the STEM explainer, in two aspect ratios

**What I was working on.** A STEM explainer breaking down the RAG Triangle (Query, Retrieval, Generation), cut at 16:9 and 9:16.

**What I tried, and what I expected.**
- I wanted to visually explain how RAG overrides base training data.
- Expected a simple prompt vs. answer visual to be enough.

**Where it resisted, and what I did next.**
- Explaining "Context Poisoning" visually was difficult using just text boxes. 
- Fixed by using a split-screen visual (the `TwoWayCompare` component) showing how a flawed search retrieval (e.g., pulling Q2 data instead of Q3) immediately dooms the AI's generation.

**What Claude contributed, and what I did with it.**
- Mine: The technical explanation of context poisoning and the RAG limits.
- Claude's: Caught the fact that `--height 2160` was still being used on the portrait render in my local script, which would have output 1216x2160. I updated the script to explicitly use `--height 3840`.

**What I understand now, and what I still do not.**
- Understood: In a RAG system, the AI surrenders entirely to the retrieved text. The vulnerability lies in the search, not the LLM.