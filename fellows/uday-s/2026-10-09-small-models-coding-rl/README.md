# One Model, Three Numbers

**Fellow:** Uday Sonawane
**Date:** 2026-10-09
**Format:** `ai-explainer` spine on the `claude-hai` channel key (Brutalist)
**Runtime:** ~3:31 (210.82s measured) · 11 beats
**Narrator:** Onyx (`am_onyx`) · Register: Pragmatist
**Channel chip / handle on cut:** `@HumanitariansAI`
**Topic:** Weekly STEM — small models, coding agents and reinforcement learning
**Deliverable (local):** `SmallModelsCodingRL_UdaySonawane_10_09_2026.mp4`

## What this video is about

One model posts several different numbers on the same benchmark, and which one
gets quoted decides whether it looks state of the art. DeepSWE-Preview on
SWE-bench Verified reports **42.2 pass@1**, **57.9 Best@8**, **59.0 Best@16**
with a verifier picking the winner, and **71.0 Pass@16** as an oracle upper
bound. Same model, same benchmark.

**The framework (B02) — three questions for any coding-agent score:**

1. One run, or best of N?
2. Which scaffold, and how much context?
3. Who picked the winner?

The falsifiability beat (B06) is where the usual reading breaks: the comparison
table mixes numbers produced under different conditions, so the ranking it
implies is not a like-for-like one.

The setup is in B03 — a Qwen3-32B base, RL only with a modified GRPO, trained on
4,500 tasks from an R2E-Gym subset, with benchmark repositories filtered out of
training.

## Sourcing

Every figure is attributed to the DeepSWE-Preview release (Agentica / Together
AI) and listed in [`SOURCES.md`](./SOURCES.md), with each number tied to the
beats that use it. Where a number is an oracle bound rather than an achievable
score, the video says so rather than quoting it bare.

## Package contents

| File | Role |
|---|---|
| `beat_sheet.json` | Narrative + visual plan (source of truth) |
| `README.md` | This file |
| `SOURCES.md` | Every on-screen figure against its published source |
| `FACTCHECK.md` | Claim-level verdicts |
| `CHECKS-REPORT.md` | PROOF gate, with the teaching arc |
| `SHOTLIST.md` | Per-beat shot plan |
| `PROMPTS.md` | Reproducible prompts used to build the video |
| `scenes.py` | Authored Manim scenes |
| `layout_audit.md` / `.json` | Frame-level layout audit |

Not tracked here (gitignored, local only): `clips/`, `media/`, `manim/`,
`pantry/`, `_qc/`, `mp3/`, `qc-sheet.png`, and the masters.

**No `BUILD-LOG.md` in this package**, as with the other recent videos.

## Toolkit (rebuild)

```bash
git clone https://github.com/nikbearbrown/brutalist.art.git
cd brutalist.art
./setup --install
./setup
```

Audio-first, Kokoro-only, no API keys. Full prompt path is in `PROMPTS.md`.

## Publishing

Not authorized by this package. The master stays local until a human decides to
share or upload.
