# You Can't Escape the Fairness Impossibility — You Can Only Choose Where to Sign

When group fairness metrics hit an arithmetic impossibility theorem — where demographic parity, equalized odds, and calibration cannot simultaneously hold across different base rates — engineers naturally look for an escape hatch. Three famous exits beckon: drop down to individual fairness, climb to causal models, or quantify total unfairness on a continuous inequality scoreboard.

Every single one hands you back the exact same bill.

In this episode of *Computational Skepticism for AI*, Liam (in for Professor Bear) traces where the values choice relocates across all three frameworks:
1. **Individual Fairness** dodges group aggregates but forces you to sign the similarity metric $d$ — where ignoring access barriers bakes structural inequity directly into the definition of "similar."
2. **Causal Fairness** moves beyond observational correlations but bills you for a complete structural causal graph — where deciding which paths are illegitimate discrimination is a values choice data alone cannot make.
3. **The Inequality Index (Generalized Entropy)** replaces binary pass/fail with a continuous scoreboard decomposed into within-group and between-group unfairness — but forces you to define a cardinal "benefit" and tune the sensitivity slider $\alpha$.

The mathematical impossibility is never solved. It is only re-addressed to whoever must sign off on the object.

---

### Key Takeaways & Carry-Out
- **The Three Famous Exits**:
  - *Individual Fairness*: Treat similar individuals similarly ($x \approx y \implies \hat{Y}(x) \approx \hat{Y}(y)$).
  - *Causal Fairness*: Climb Pearl's ladder to isolate direct discrimination from legitimate mediators via Structural Causal Models.
  - *Continuous Inequality*: Treat prediction benefits like income distribution, decomposing total unfairness into within-group and between-group components.
- **The Three Relocations**:
  - Individual fairness moves the price into the **Similarity Metric ($d$)**.
  - Causal fairness moves the price into the **Causal Graph**.
  - The inequality index moves the price into the **Benefit Definition** and **Sensitivity Parameter ($\alpha$)**.
- **The Upstream Construct Gap (The One Flag)**: No downstream fairness metric — group, individual, causal, or continuous — can validate whether the prediction task itself was fair to pose. Optimizing re-arrest or credit score proxies does not guarantee public safety or creditworthiness.
- **Both Directions**:
  - *Direction A (Smuggling via Elegance)*: A mathematically rigorous framework can satisfy its proof cleanly while smuggling biased assumptions into the similarity metric or causal graph.
  - *Direction B (Coarse Blindspots)*: Refusing advanced frameworks leaves you trapped in coarse group averages that cannot distinguish legitimate credentials from systemic discrimination.
- **Carry-Out Law**: "You cannot escape the fairness impossibility — every advanced framework simply relocates the values choice to a new object you have to sign."

---

### Your Turn — Prompt for Claude / AI Assistants
```
Take an algorithmic decision system in your organization that claims to satisfy individual, causal, or continuous fairness. Identify the specific object that encodes its core assumptions — the similarity metric, the causal graph, or the benefit function. Who defined that object, what values trade-off does it embed, and who signed off on it?
```

---

### Metadata
- **Series**: Computational Skepticism for AI
- **Channel**: @HumanitariansAI (youtube.com/@HumanitariansAI)
- **Playlist**: Computational Skepticism — Bias & Fairness
- **Source**: *Computational Skepticism for AI* by Nik Bear Brown (Chapter 7: Fairness Metrics: Choosing a Definition and Defending It)
- **Voice**: Liam (synthesized via open-weights Kokoro `am_onyx`, in for Bear)
- **Visuals**: Manim + Remotion (Cream `#FAF9F5`, Warm Ink `#3D3929`, Terracotta `#D97757`)
- **AI Disclosure**: Synthetic narration generated locally via Kokoro `am_onyx`. Visuals algorithmically rendered via Manim and Remotion. Zero generative video, zero paid APIs.
- **Code (no media)**: https://github.com/nikbearbrown/humanitarians-youtube/tree/main/computational-skepticism/you-cant-escape-fairness-impossibility-you-can-only
