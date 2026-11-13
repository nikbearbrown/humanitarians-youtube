# Explainer — Causal Memory and Prevention Layers (Pi Memory)

- **Week:** 28 Sep – 4 Oct 2026
- **Type:** Topic explainer
- **Explainer video:** https://drive.google.com/file/d/1cgrPLyHPYWT5n3w6fxOis5dKi2yYOx8j/view?usp=drive_link
- **Frictional log:** [FRICTIONAL.md](FRICTIONAL.md)
- **Beat sheet:** [beatsheet.md](beatsheet.md) · [beat_sheet.json](beat_sheet.json) · **Narration:** [script.md](script.md)

## What it covers

This report details the production of explainer video (16:9 widescreen and 9:16 portrait) designed to demonstrate that Pi’s causal memory functions as a bounded reactive safety gate inside beforeToolCall (agent-loop.ts) rather than an open-ended intelligence layer. Developed collaboratively through human architectural direction and AI-assisted Remotion video generation with Kokoro voice synthesis, the project formalizes a five-slot causal tuple (condition, action, outcome, mechanism, mitigation) and illustrates a full block-and-explain recovery cycle using an uncommitted git reset failure.

## Evidence — Open Directly

- [Adapted beat sheet (12 beats)](beat_sheet.json).
- [Frictional log](FRICTIONAL.md).
- [Explainer video](https://drive.google.com/file/d/1cgrPLyHPYWT5n3w6fxOis5dKi2yYOx8j/view?usp=drive_link).
- [Progress video](https://drive.google.com/file/d/1SgdIIJpmpgKTf5gCDyWiZwosWo2TYzNb/view?usp=drive_link).

## Attribution and Contribution

Work by Kriti S.: technical mechanism structured into a 12-beat explainer, custom Remotion scene components created (`UpdRule`, `UpdMatch`, `UpdBlock` in `WeekUpdate.tsx`), worked example grounded in common git recovery scenarios, and narration script written, then voiced via Kokoro am_onyx (Liam in for Kriti). Research and review by Kriti S.: designing the 5-slot causal rule schema, defining the `beforeToolCall` hook interception point, and verifying factual claims against sources.
