# Twenty Dots Beat Twenty Percent

When physicians are given a mammography screening problem framed in standard percentages — an eighty percent sensitivity and a nine point six percent false-positive rate — over eighty percent of them conclude that a positive test means an eighty to ninety percent chance of cancer. The true probability is under eight percent. When Gerd Gigerenzer presented the exact same problem using natural frequencies of real people — eight out of one hundred and seven who test positive — the vast majority of physicians reasoned correctly immediately.

In this episode of *Computational Skepticism for AI*, Professor Bear and Liam unpack why twenty discrete dots beat "twenty percent" when communicating uncertainty. Abstract percentages force Bayesian mental arithmetic that human cognitive architecture notoriously bungles. By translating probabilities into discrete quantile dotplots and natural frequencies, we replace fragile symbolic multiplication with direct human perception: position and count.

---

### Key Takeaways & Carry-Out
- **The Core Problem**: Percentages detach probability from concrete population baselines. A 90% sensitivity sounds overwhelming, hiding the fact that false positives outnumber true positives by more than ten to one.
- **The Mechanism (Gigerenzer's Natural Frequencies)**: Natural frequencies anchor probability in real, countable people. Translating percentages into "8 out of 107 positive tests" resolves the base-rate fallacy without doing Bayes' theorem in your head.
- **The Perception Hierarchy (Cleveland & McGill)**: Human vision perceives position along a common scale and discrete counts with near-zero error. It evaluates area, volume, and color saturation with massive perceptual variance.
- **The 20-Dot Solution (Kay & Hullman)**: A 20-dot quantile dotplot (each dot represents a 5% quantile) maps abstract probabilities directly into position and count. Four filled circles make "20% risk of failure" directly tangible.
- **Carry-Out Law**: Position and count replace mental arithmetic with direct perception.
- **Direction A (The Tool)**: A dotplot will not calculate the probability for you; your calibration, priors, and sampling pipeline must still be rigorous.
- **Direction B (The Interface)**: A mathematically flawless probability remains epistemic malpractice if presented in a format that guarantees human misinterpretation.

---

### Your Turn — Prompt for Claude / AI Assistants
```
Take the primary probability your system reports to users or partners — a risk score, a failure rate, or a calibration band. Rewrite it as twenty discrete dots. Show four filled circles for a twenty percent risk. How does the perception of the decision change when mental arithmetic is replaced by direct counting?
```

---

### Metadata
- **Series**: Computational Skepticism for AI
- **Channel**: @HumanitariansAI (youtube.com/@HumanitariansAI)
- **Playlist**: Computational Skepticism — Visualization & Deception
- **Source**: *Computational Skepticism for AI* by Nik Bear Brown (Chapter 10: Visualization Under Validation: Honest, Misleading, and the Choices Between)
- **Voice**: Liam (synthesized via open-weights Kokoro `am_onyx`)
- **Visuals**: Manim + Remotion (Cream `#FAF9F5`, Warm Ink `#3D3929`, Terracotta `#D97757`)
- **Code (no media)**: https://github.com/nikbearbrown/humanitarians-youtube/tree/main/computational-skepticism/twenty-dots-beat-twenty-percent
