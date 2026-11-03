# Why a sepsis alarm in hundreds of hospitals learned to wait for the doctor

A proprietary sepsis early-warning model cleared internal validation and was deployed across hundreds of hospitals — yet independent evaluation showed it missed most sepsis cases while flooding clinicians with false alerts.

The reason was not a mathematical coding error. The model partly learned to trigger on clinical workflow traces: specifically, doctors ordering blood cultures. Because the alert was downstream of the clinician's own diagnostic suspicion, the "early warning" was simply echoing the human judgment it claimed to precede — a circular signal that internal validation metrics scored as high accuracy, and that no algorithm can detect from inside its own data frame.

In this episode of *Computational Skepticism for AI*, Professor Bear and Liam unpack the suspicion loop and explain why in-distribution validation metrics fail to detect circular premise flaws.

---

### Key Takeaways & Carry-Out
- **The Suspicion Loop**: Clinician suspects sepsis -> Clinician orders diagnostic blood culture -> Model reads culture order as a high-weight feature -> Model fires sepsis alert -> Alert lands back on the clinician who already suspected sepsis.
- **The Validation Blind Spot**: Internal automated scripts scored the model as highly accurate because the alert and the sepsis diagnosis co-occurred — masking the fact that the alert arrived after human intervention had already begun.
- **The Data-World Gap**: The training data contains the timestamped order code, but not the clinical intent that placed it. No machine learning model can detect from inside its feature frame that its strongest signal is a reaction to the outcome.
- **Carry-Out Law**: An early-warning model cannot warn you about an event if its strongest feature is the trace of you already reacting to it.
- **Direction A**: High predictive accuracy in training logs is NOT proof of early forecasting lead time.
- **Direction B**: The statistical optimizer did not fail its math — it found the strongest pattern in the data. The failure was an epistemic mistake: treating an echo of clinician behavior as an independent forecasting discovery.

---

### Your Turn — Prompt for Claude / AI Assistants
```
Audit a predictive model or early-warning system in your workflow. Which of its top input features are actually traces of human decisions responding to the outcome it claims to predict? Check whether your model's accuracy is partly an echo of human suspicion before your next deployment review.
```

---

### Metadata
- **Series**: Computational Skepticism for AI
- **Channel**: @HumanitariansAI (youtube.com/@HumanitariansAI)
- **Playlist**: Computational Skepticism — Limits of AI
- **Source**: *Computational Skepticism for AI* by Nik Bear Brown (Chapter 13: The Limits of AI — What the Tools Cannot Do)
- **Voice**: Liam (synthesized via open-weights Kokoro `am_onyx`)
- **Visuals**: Manim + Remotion (Cream `#FAF9F5`, Warm Ink `#3D3929`, Terracotta `#D97757`)
- **AI Disclosure**: Voice narration synthesized with open-weights Kokoro TTS (`am_onyx`). Visual animations generated programmatically with Manim and Remotion.
- **Code (no media)**: https://github.com/nikbearbrown/humanitarians-youtube/tree/main/computational-skepticism/why-sepsis-alarm-in-hundreds-hospitals-learned-wait
