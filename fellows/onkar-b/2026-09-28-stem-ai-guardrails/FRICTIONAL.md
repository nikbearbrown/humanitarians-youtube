# Frictional log — AI Guardrails & Validation

## 2026-09-28 — the STEM explainer, in two aspect ratios

**What I was working on.** A STEM explainer on AI Guardrails—how a deterministic verification layer stops an AI from executing dangerous actions—cut at 16:9 and 9:16.

**What I tried, and what I expected.** 
- I designed the visuals to show a side-by-side comparison of a Python guardrail script blocking a bad JSON payload.
- I expected the 9:16 vertical render to naturally wrap the code text.

**Where it resisted, and what I did next.** 
- The 9:16 compiler suffered from spacing issues, leaving the bottom half of the screen completely empty. 
- I fixed this by converting the code snippet text treatments into full-width bordered cards and repositioning them vertically.

**What Claude contributed, and what I did with it.** 
- Mine: The technical curriculum, the guardrail examples, and the latency tax concept.
- Claude's: Visual QC on the rendered `.mp4` frames, noting the canvas was underutilized. I accepted the feedback and adjusted the components.

**What I understand now, and what I still do not.**
- Understood: Engineering the guardrail is often much harder and more computationally expensive than engineering the original prompt. Latency and false positives are the biggest risks.