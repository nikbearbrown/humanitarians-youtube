# Frictional log — Evaluation Layer Engineering

## 2026-09-21 — the project update, in two aspect ratios

**What I was working on.** A project update explainer on building the core mathematical grading logic for the AI outputs, cut at 16:9 and 9:16.

**What I tried, and what I expected.**
- I wrote a strict programmatic comparison to subtract the AI's numeric claim from the database truth.
- Expected Python to handle the math flawlessly.

**Where it resisted, and what I did next.**
- The numeric parsing logic initially crashed because it couldn't handle commas and currency symbols in the AI's output (e.g., "$4.5M" vs 4500000). 
- Fixed by writing a deterministic normalizer function to strip conversational noise before running the mathematical variance.

**What Claude contributed, and what I did with it.**
- Mine: The parsing normalizer, grading logic, and API endpoint integration.
- Claude's: QC on the visual spacing in the `TwoWayCompare` component. I accepted the edits to convert thin text into full-width bordered cards for better mobile legibility.

**What I understand now, and what I still do not.**
- Understood: An overly rigid evaluation script will trigger massive false positives if it does not normalize the input data first.