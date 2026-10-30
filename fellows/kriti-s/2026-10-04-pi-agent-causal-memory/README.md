# Week 2: Causal Memory and Prevention Layers (Pi Memory)

**Group:** RL Environment · **Reporting week:** 2026-09-26 through 2026-10-03

## Executive Summary

This report details the production of explainer video (16:9 widescreen and 9:16 portrait) designed to demonstrate that Pi’s causal memory functions as a bounded reactive safety gate inside beforeToolCall (agent-loop.ts) rather than an open-ended intelligence layer. Developed collaboratively through human architectural direction and AI-assisted Remotion video generation with Kokoro voice synthesis, the project formalizes a five-slot causal tuple (condition, action, outcome, mechanism, mitigation) and illustrates a full block-and-explain recovery cycle using an uncommitted git reset failure. The film is credited to original production. The film is credited to original production. 


## Evidence — Open Directly

- [Adapted beat sheet (12 beats)](beat_sheet.json).
- [Frictional log](Frictional.md).
- [Explainer video](https://drive.google.com/file/d/1cgrPLyHPYWT5n3w6fxOis5dKi2yYOx8j/view?usp=drive_link)
- [Progress video](https://drive.google.com/file/d/1SgdIIJpmpgKTf5gCDyWiZwosWo2TYzNb/view?usp=drive_link)

## Attribution and Contribution

 Work by Kriti S.: technical mechanism structured into a 12-beat explainer, custom Remotion scene components created (`UpdRule`, `UpdMatch`, `UpdBlock` in `WeekUpdate.tsx`), worked example grounded in common git recovery scenarios, and narration script written, then voiced via Kokoro am_onyx (Liam in for Kriti). Research and review by Kriti S.: designing the 5-slot causal rule schema, defining the `beforeToolCall` hook interception point, and verifying factual claims against sources.

## Folder Contents

- README.md: result, evidence status, and attribution.
- beat_sheet.json: 12-beat causal memory production plan and cues.
- Frictional.md: process reflection and build friction log.
