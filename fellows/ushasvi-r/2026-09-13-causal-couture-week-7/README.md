# Causal Couture — Week 7: Causal Reliability and Uncertainty Refinement

- **Presenter:** Ushasvi Rachel
- **Organization:** Humanitarians.ai
- **Type:** Causal Couture project progress
- **Formats:** 16:9 master source and portrait-native 9:16 source

Week 7 adds SKU-level cluster-bootstrap uncertainty alongside the existing row-level bootstrap, making dependence among repeated product observations more visible.

The root `beat_sheet.json` is the horizontal master. `remotion/horizontal/` and `remotion/vertical/` contain the format-specific compositions; the vertical beat sheet is preserved beside its composition. `remotion/shared/` contains the shared visual tokens used by both.

**Boundary:** Improved uncertainty diagnostics do not establish causality, remove unobserved confounding, prove the causal graph, or guarantee treatment overlap.
