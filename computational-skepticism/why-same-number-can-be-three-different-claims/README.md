# Why the Same Number Can Be Three Different Claims

A model scores 87% once — and three engineers write it up as "we observe," "we find," and "we conclude." Only one of them is telling the truth.

In this episode of *Computational Skepticism for AI*, Professor Bear and Liam explain the epistemic price tags attached to scientific and machine learning claim-verbs. Accuracy is an outcome, not an evidentiary warrant. Every claim-verb sits on a frozen eight-rung ladder — hypothesize, suggest, observe, find, show, demonstrate, conclude, prove — and a verb upgrades only when the requisite evidence (replication across seeds, subgroup breakdowns, external validation, and adversarial stress testing) is actually paid.

---

### Key Takeaways & Carry-Out
- **The Core Mechanism**: Claims operate under *warranted assertibility* — you are entitled to assert only what your evidence pays for. A single benchmark run on a held-out split pays for "observe." It does not pay for "find" (which requires replication), and it nowhere near pays for "conclude" (which requires ruling out alternative explanations and surviving sensitivity analysis).
- **The Frozen Ladder**: The editorial canon runs strictly from weakest to strongest:
  `hypothesize → suggest → observe → find → show → demonstrate → conclude → prove`
- **Carry-Out Law**: Every claim-verb has an evidence price — you can only spend the verb your validation actually paid for.
- **Direction A**: A stellar 99% accuracy on a single benchmark does not buy you "conclude." High accuracy is an outcome, not an evidentiary warrant. Without replication, distribution shifts, and sensitivity analysis, your evidence only warrants "observe."
- **Direction B**: Writing "observe" or "find" does not diminish your engineering. Modest, calibrated verbs survive peer scrutiny, while inflated claims collapse the moment an auditor checks your test setup.

---

### Your Turn — Prompt for Claude / AI Assistants
```
Take the last validation report or model card your team drafted. Highlight every occurrence of observe, find, show, and conclude. For each one, list the exact evidence backing that sentence: was it a single run, replicated seeds, subgroup checks, or a stress test? If the evidence doesn't pay the verb's price, downgrade it to the rung it earned.
```

---

### Metadata
- **Series**: Computational Skepticism for AI
- **Channel**: @HumanitariansAI (youtube.com/@HumanitariansAI)
- **Playlist**: Computational Skepticism — Communicating Uncertainty
- **Source**: *Computational Skepticism for AI* by Nik Bear Brown (Chapter 11: Communicating Uncertainty: Calibrating Claims to Evidence)
- **Voice**: Liam (synthesized via open-weights Kokoro `am_onyx`)
- **Visuals**: Manim + Remotion (Cream `#FAF9F5`, Warm Ink `#3D3929`, Terracotta `#D97757`)
- **Code (no media)**: https://github.com/nikbearbrown/humanitarians-youtube/tree/main/computational-skepticism/why-same-number-can-be-three-different-claims
