# Levels, Not Layers

**Fellow:** Uday Sonawane
**Date:** 2026-10-02
**Format:** `ai-explainer` spine on the `claude-hai` channel key (Brutalist)
**Runtime:** ~3:27 (207.15s measured) · 11 beats
**Narrator:** Onyx (`am_onyx`) · Register: Pragmatist
**Channel chip / handle on cut:** `@HumanitariansAI`
**Topic:** Weekly STEM — HOPE and nested learning
**Deliverable (local):** `HopeTraining_UdaySonawane_10_02_2026.mp4`

## What this video is about

The topic was requested as *"HOPE training by Google"*. **B01 corrects that
premise on screen:** HOPE is not a training method — it is a self-modifying
architecture, a Titans variant. Depth is the illusion; levels are the axis.
That correction is the title.

**The framework (B02) — three questions for any claim that a model learns
continually:**

1. What are its memory systems, and on what schedule does each update?
2. Does the headline number survive a fair comparison?
3. What do the authors themselves say it cannot do?

A transformer has two memory systems — weights that never update after training
and attention that holds one context. HOPE's continuous memory system is a
spectrum of blocks, each on its own update frequency, worked through the
paper's own four-level example.

Question two is where the headline softens, and question three goes to the
authors' own limitations section.

## Sourcing

Every figure is cited to a table or section of the paper, listed in
[`SOURCES.md`](./SOURCES.md) — including the 1.3B-parameter / 100B-token
comparisons from Table 2 and the ablation in Table 6 that tests whether the
memory spectrum is doing the work.

## Package contents

| File | Role |
|---|---|
| `beat_sheet.json` | Narrative + visual plan (source of truth) |
| `README.md` | This file |
| `SOURCES.md` | Every on-screen figure against its table or section in the paper |
| `FACTCHECK.md` | Claim-level verdicts, including the corrected premise |
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
