# The average that hides the patient

A proprietary bedside sepsis model was deployed across hundreds of hospitals with an aggregate AUC between 0.76 and 0.83 and an apparently pristine Expected Calibration Error of 0.018. But when independent clinicians evaluated it in production, its real-world AUC fell to 0.63, its positive predictive value was just 12%, and it missed 67% of patients who actually developed sepsis.

Standard evaluation treats calibration as a single number. But Expected Calibration Error (ECE) is a sample-weighted sum across bins. When 90% of hospital admissions are low-risk routine cases where the model correctly predicts nothing is happening, that routine majority crushes the aggregate score. A catastrophic miscalibration on the sickest or most vulnerable subgroup—where an 80% risk alert only reflects a 40% true probability—contributes almost nothing to the headline metric.

In this episode of *Computational Skepticism for AI*, Professor Bear and Liam demonstrate how population weighting turns aggregate calibration into an illusion that conceals dangerous local failures.

---

### Key Takeaways & Carry-Out
- **The Core Mechanism**: Expected Calibration Error is mathematically a weighted average: $\\text{ECE} = \\sum \\frac{n_b}{N} |\\text{acc}(b) - \\text{conf}(b)|$. The weights are subgroup sample shares $\\frac{n_b}{N}$.
- **The Masking Effect**: Large routine cohorts dominate the sum. Severe calibration breakdown in high-acuity or rare subgroups disappears into the aggregate rounding error.
- **The Epic Sepsis Case Study**: External validation by Wong et al. (2021) showed aggregate metrics hid severe clinical failure (AUC 0.63, PPV 12%, 67% missed sepsis cases).
- **Carry-Out Law**: An aggregate calibration metric does not measure how well a model serves any specific patient; it measures how well the majority drowns out the margins.
- **Direction A**: A low global ECE does not imply a model is safe for any individual patient or subgroup.
- **Direction B**: Require stratified calibration curves, subgroup ECE audits, and slice-level worst-case bounds before clinical or critical deployment.

---

### Your Turn — Prompt for Claude / AI Assistants
```
Take the calibration curves for your production classifier. Split your evaluation cohort by clinical subgroup, demographic slice, or operational context. Check whether low overall Expected Calibration Error is concealing double-digit error in high-stakes segments.
```

---

### Metadata
- **Series**: Computational Skepticism for AI
- **Channel**: @HumanitariansAI (youtube.com/@HumanitariansAI)
- **Playlist**: Computational Skepticism — Communicating Uncertainty
- **Source**: *Computational Skepticism for AI* by Nik Bear Brown (Chapter 11: Communicating Uncertainty: Calibrating Claims to Evidence)
- **Voice**: Liam (synthesized via open-weights Kokoro `am_onyx`)
- **Visuals**: Manim + Remotion (Cream `#FAF9F5`, Warm Ink `#3D3929`, Terracotta `#D97757`)
- **Code (no media)**: https://github.com/nikbearbrown/humanitarians-youtube/tree/main/computational-skepticism/average-that-hides-patient
