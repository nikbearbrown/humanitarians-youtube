# Frictional log — Deterministic Parsing

## 2026-10-09 — the project update, in two aspect ratios

**What I was working on.** A STEM AI explainer outlining the architectural divide between probabilistic LLM tokens and strict deterministic database requirements.

**What I tried, and what I expected.** 
- I attempted to explain the formatting failures purely as an LLM "hallucination" issue.
- I expected the audience to easily grasp why a dollar sign causes a C++ crash.

**Where it resisted, and what I did next.** 
- The term "hallucination" was inaccurate for formatting errors. The model isn't hallucinating; it's statistically predicting valid linguistic variations of numbers, which software systems cannot handle.
- I shifted the script to focus on "Tokenization" and introduced the "Deterministic Shield" concept, visualizing regex as a physical barrier between the AI and the database.

**What Claude contributed, and what I did with it.** 
- Mine: The structural framework of the video and the downstream database crash scenario.
- Claude's: Defining the "Token Fragmentation" issue and contrasting probabilistic guessing with deterministic parsing. I used this juxtaposition as the core narrative hook.

**What I understand now, and what I still do not.**
- Understood: AI systems fail not because the model is broken, but because software engineers treat statistical text generators like traditional API endpoints.