# The Critical Path — AI + Critical Path Method (Humanitarians AI Fellows)

A Claude-styled (cream + terracotta) brutalist **concept explainer** with voiceover, teaching
what the critical path is, why the longest chain of dependent tasks sets your deadline, and how
to use AI to find it without being misled. Customized for Sanjana · @HumanitariansAI.

## The masters (both true 4K, 24 fps, with audio)

| File | Aspect | Resolution | Length | Use |
|---|---|---|---|---|
| `The-Critical-Path__16x9_4K_YouTube.mp4` | 16:9 landscape | 3840×2160 | ~4:30 | Main YouTube video |
| `critical-path-short/The-Critical-Path__9x16_Short.mp4` | 9:16 vertical | 2160×3840 | ~0:48 | YouTube Shorts |

Intro & outro use the Claude scenes (ClaudeComposerAsk, EB Garamond serif); the intro opens
with Sanjana's spoken hello. The outro is a **custom @HumanitariansAI title card**. The body
uses a **new visual language**: an activity-on-node **network diagram** with task durations,
the critical path highlighted in terracotta, a slack bar, and a path-SHIFT animation.

**Audio:** Kokoro `af_bella` (local, free). Narration is the master clock. Cross-dissolve-
through-cream transitions. **Native 4K flat-vector render** — do not upscale.

## What it teaches (MAP / FIND / PROTECT)
The rule: **the longest path sets the deadline** — speeding up anything else saves nothing.
1. **MAP** — give the AI real tasks, durations, and dependencies.
2. **FIND** — the AI computes the critical path (longest chain) + slack on every other task.
3. **PROTECT** — guard that chain, treat slack as a buffer, and re-check — the path can move.
4. **Worked example** — A-B-D-E = 14 days (critical) vs A-C-D-E = 11 days (3 days slack on the UI branch).
5. **The trap** — crash a non-critical task → deadline unchanged; let a "safe" task overrun its slack → the critical path shifts. You don't find it once; you watch it.
6. **Your turn** — get the critical path, each task's slack, and a slip simulation (copyable prompt in the video).

Concept explainer — the task network is an illustrative teaching example; the arithmetic is
exact (see `FACTCHECK.md`). No people are named.

## Companion files
- `beat_sheet.json` · `build_sheet.py` · `scenes.py` (16:9) · `…-short/scenes_short.py` (9:16)
- `add_transitions.py` · `SHOTLIST.md` · `SOURCES.md` · `FACTCHECK.md` · `PROMPTS.md` · `CHECKS-REPORT.md` · `BUILD-LOG.md`
- `PROOF-REVIEW.md` — self-assessment against the PROOF rubric
- `description.txt` — ready-to-paste YouTube description

## Delivery
- Delivered to this folder (**not pushed to GitHub**, per the user's instruction).
- Rendered with the **brutalist.art** Remotion + Manim toolkit · Kokoro `af_bella` voice.
