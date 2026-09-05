# Same CSV, Two Dashboards, Opposite Beliefs

Take one byte-for-byte fixed validation CSV and hand it to two builders: one told to reassure a nervous deployment partner, the other told to provoke hard questions. Without altering a single row, number, or metric, both dashboards query identical data — but lead to completely opposite beliefs about whether the system is safe to ship.

In this episode of *Computational Skepticism for AI*, Professor Bear and Liam explain how dashboards argue through structure rather than raw numbers. About five routine visual choices — headline dominance, compressed subgroup axes, grayed-out disparities, buried calibration curves, and reassuring framing banners — accumulate into an entirely different narrative from identical data.

---

### Key Takeaways & Carry-Out
- **The Core Mechanism**: A dashboard is not a neutral window into data; it is an argument constructed through layout, visual hierarchy, axis scales, color salience, and grouping.
- **The Structural Accumulation**: Five 30-second choices accumulate to transform perception: lead with an aggregate metric, compress failing subgroup axes, gray out disparities, bury broken calibration curves in sub-tabs, and stamp reassuring green banners.
- **Carry-Out Law**: A dashboard argues by structure before any number is read — the design choices are the argument.
- **Direction A**: Verifying the numbers does not verify the dashboard. You can audit every cell in the underlying CSV, confirm zero calculation errors, and still present a deceptive visual argument.
- **Direction B**: An honest layout does not make the decision for you. It does not prove the model is ready or broken; it simply preserves the evidence so human judgment operates on reality rather than reassurance.

---

### Your Turn — Prompt for Claude / AI Assistants
```
Take the primary dashboard your team uses to evaluate model performance. Identify five layout choices: the headline metric, the axis baselines, the color salience, the tab placement, and the card framing. For each choice, write down the argument the visual structure makes before anyone reads the numbers.
```

---

### Metadata
- **Series**: Computational Skepticism for AI
- **Channel**: @HumanitariansAI (youtube.com/@HumanitariansAI)
- **Playlist**: Computational Skepticism — Visualization & Deception
- **Source**: *Computational Skepticism for AI* by Nik Bear Brown (Chapter 10: Visualization Under Validation: Honest, Misleading, and the Choices Between)
- **Voice**: Liam (synthesized via open-weights Kokoro `am_onyx`)
- **Visuals**: Manim + Remotion (Cream `#FAF9F5`, Warm Ink `#3D3929`, Terracotta `#D97757`)
- **Code (no media)**: https://github.com/nikbearbrown/humanitarians-youtube/tree/main/computational-skepticism/same-csv-two-dashboards-opposite-beliefs
