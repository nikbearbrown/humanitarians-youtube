# Frictional Log — RLHF: How Chatbots Learned to Help

> Append dated entries as you go; never rewrite an earlier one.

## 2026-10-31 — Build a 60-second explainer on RLHF, in 16:9 and 9:16

*Drafted with Claude Code from the build record and reviewed by me.*

- **What I tried, and what I expected:**
  I gave eight points, from the raw model that answers with questions to DPO and AI feedback, and expected the video to say chatbots are given rules for helping. A small seeded numpy toy produced the reward-model agreement, the RL step and the reward-hacking curve.

- **Where it resisted, and what I did next:**
  The fact-check changed a few of my numbers and claims: "100×" became "more than 100×" and the hook is marked illustrative. The draft ran nearly 71 s and was trimmed three times, keeping all eight points. "RLHF" was the hardest word for the voice and needed a letter-by-letter fix. The type check then failed on the bright accent strokes and some small serif text, which were darkened and set on filled cards.

- **What Claude or another person contributed — and what I accepted, changed, or rejected:**
  Claude Code drafted the beat sheet, wrote the toy and the scenes, checked the claims against the InstructGPT, GPT-3, DPO, sycophancy and reward-overoptimization papers, and fixed the layout and type-check issues. I accepted the corrections and the one logged tuning of the toy's people-pleaser cluster.

- **What I understand now, and what I still do not:**
  I understand the three steps and why optimising a learned reward too hard can reward the wrong thing. I still don't know how labs decide how strong the drift penalty should be in practice.

- **Evidence:** [beat sheet](beat_sheet.json) · [vertical beat sheet](vertical/beat_sheet.json) · [build log](BUILD-LOG.md) · [fact-check](FACTCHECK.md) · [evidence](evidence/)
