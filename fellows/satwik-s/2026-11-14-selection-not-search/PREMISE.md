# PREMISE — Week 16: Selection, Not Search (Stage 4b Matching)

**Central question.** If you ranked every section by similarity to the project and took the top ones, would you get the same reading set the matcher chooses — or is selection doing something a similarity search cannot?

**Answer (the spine).** 60–85% of the most similar sections share no specific project vocabulary, so similarity alone would fill the roadmap with topically-near but project-irrelevant reading. The matcher instead selects on shared vocabulary, labels each section by role, and logs every high-similarity rejection (109 / 63). Measured, swept over K, reproducible; isolates Stage 4b (no sequencing).

**Why it matters.** The headline design claim of the whole project is that building a roadmap is a *selection* problem, not a *retrieval* problem. This week measures that claim directly at the matcher.

**Register.** Pragmatist / skeptical-explainer (PROOF): framework first (two arms, two signals), then the number, robustness, structure, then the honest boundary.

**Reusable framework.** (1) To prove selection beats search, remove the selection signal and measure what changes. (2) Measure the right thing — how much of a pure ranker's output shares no task-specific signal. (3) Sweep the free parameter (K). (4) Treat the reject log as a result.
