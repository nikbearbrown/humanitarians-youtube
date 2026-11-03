# Why a Perfect Explanation Can Make You More Wrong

An AI tool predicts high malignancy risk at 84% confidence on a screening scan and provides an explanation: the score was driven by texture pattern X and asymmetry Y. The radiologist confirms features X and Y on the scan, concurs, and orders a biopsy. The biopsy comes back completely benign.

The natural assumption is that the AI hallucinated or gave a fake explanation. But the explanation was 100% faithful to the model's math: features X and Y really drove the 84% score. The model did not lie about itself.

In this episode of *Computational Skepticism for AI*, Professor Bear and Liam break down the epistemic mechanism of explainable AI: post-hoc explanations faithfully describe a model's internal accounting, not the world. When a model learns a shortcut, an accurate explanation makes a wrong call feel right.

---

### Key Takeaways & Carry-Out
- **Composite Clinical Illustration**: A deep network learns spurious features X & Y that correlated with cancer in training but belong to a benign condition in the deployment population.
- **Internal Accounting vs The World**: An explanation tells you what the network calculated; it cannot verify whether what the network calculated warrants belief about the physical or biological world.
- **The Two-Path Decision Flow**:
  - *Path A (Prediction Alone)*: Clinician sees an 84% score with no story, maintains healthy skepticism, and keeps confidence balanced at 50%.
  - *Path B (Prediction + Explanation)*: Clinician sees the 84% score paired with a plausible, verifiable story, triggering unearned trust and surging confidence to 90%.
- **The Fluency Trap**: Well-formed outputs are mistaken for evidence of truth. The narrative transfers unearned epistemic trust from the machine's accounting to the human mind.
- **Carry-Out Law**: A faithful explanation describes the model's internal accounting, not the world — so when a model learns a shortcut, an accurate explanation makes a wrong call feel right.
- **The One Flag**: Explanation tools provide transparency into mathematical operations (inspecting weights and feature attributions), but transparency of internal math is not validation of external reality in deployment.
- **Direction A**: A 100% faithful explanation does not prove the model is correct (it may give a high-fidelity view of a broken shortcut).
- **Direction B**: A wrong decision does not mean the explanation tool lied (it faithfully exposed the model's internal logic, leaving skepticism to human supervision).

---

### Your Turn — Prompt for Claude / AI Assistants
```
Take a deployed classifier in your stack that provides feature explanations. Audit five cases where the model made an error. Did the explanation faithfully describe the model's shortcut, and would reading it make a reviewer more likely to approve the mistake?
```

---

### Metadata
- **Series**: Computational Skepticism for AI
- **Channel**: @HumanitariansAI (youtube.com/@HumanitariansAI)
- **Playlist**: Computational Skepticism — Explainability & Interpretability
- **Source**: *Computational Skepticism for AI* by Nik Bear Brown (Chapter 5: Model Explainability: Distinguishing Explanation from the Appearance of Explanation)
- **Voice**: Liam (synthesized via open-weights Kokoro `am_onyx`, in for Bear)
- **Visuals**: Manim + Remotion (Cream `#FAF9F5`, Warm Ink `#3D3929`, Terracotta `#D97757`)
- **Code (no media)**: https://github.com/nikbearbrown/humanitarians-youtube/tree/main/computational-skepticism/why-perfect-explanation-can-make-you-more-wrong
