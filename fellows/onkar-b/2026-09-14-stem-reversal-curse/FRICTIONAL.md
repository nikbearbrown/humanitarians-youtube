# Frictional log — The Reversal Curse

## 2026-09-14 — the STEM explainer, in two aspect ratios

**What I was working on.** A STEM explainer on the Reversal Curse in Large Language Models, cut at 16:9 and 9:16.

**What I tried, and what I expected.**
- I prompted an LLM with obscure biographical facts and expected it to answer in both directions correctly, assuming it built a knowledge graph.

**Where it resisted, and what I did next.**
- The model confidently hallucinated answers when tested in reverse. 
- I used this exact failure state (the Tom Cruise mother example) as the primary visual for the video to prove the architectural limitation on screen.

**What Claude contributed, and what I did with it.**
- Mine: The prompt testing and deductive logic research.
- Claude's: Structural script formatting. Claude also flagged that the `metadata.aspect` compiler bug was still present in the boilerplate. I corrected it to `aspect_ratio`.

**What I understand now, and what I still do not.**
- Understood: You cannot fix the Reversal Curse simply by making the model bigger; it is a flaw in left-to-right training data.