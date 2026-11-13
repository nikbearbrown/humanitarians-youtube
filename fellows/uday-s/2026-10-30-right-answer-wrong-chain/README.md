# Right Answer, Wrong Chain

**Fellow:** Uday Sonawane
**Date:** 2026-10-30
**Format:** `ai-explainer` spine on the `claude-hai` channel key (Brutalist)
**Runtime:** ~4:12 (252.20s measured) · 11 beats
**Narrator:** Onyx (`am_onyx`) · Register: Pragmatist
**Channel chip / handle on cut:** `@HumanitariansAI`
**Topic:** Weekly STEM — process supervision and multi-hop reasoning
**Deliverable (local):** `ProcessSupervisionMultiHop_UdaySonawane_10_30_2026.mp4`

## What this video is about

A model can reach the right answer through a chain that does not support it.
B01 starts by separating the two ideas the commissioned phrase joins together,
because the rest only makes sense once they are apart.

**The framework (B02) — three questions for any claim that grading the reasoning
helps:**

1. What counts as a step?
2. Who labelled the steps?
3. Is the advantage fundamental, or practical?

The measurement that makes this concrete comes from the MuSiQue paper: answer F1
of **68.8 on HotpotQA, 63.4 on 2Wiki, 37.8 on MuSiQue** — lower being harder to
cheat, because the easier sets can be answered while bypassing reasoning steps.
The second tell is in the same paper: one model scores **57.9 / 47.9 / 28.1**
across 2-, 3- and 4-hop questions while another **stays around 42% regardless of
the number of hops** — which is its own kind of evidence.

Process supervision's case rests on grading each step: **78% of a representative
MATH subset**, using **800,000 step-level human labels**.

B06 is the falsifiability beat and keeps the whole thing honest — an earlier
study found parity on grade-school maths, and a theoretical result bears on
whether the advantage is fundamental at all.

## Sourcing

Four sources, every figure read from a primary paper — no aggregator, blog or
summary sourced a number. Several were read directly from the PDF, with the
table and section recorded in [`SOURCES.md`](./SOURCES.md). Quoted phrases are
attributed rather than paraphrased into claims.

## Package contents

| File | Role |
|---|---|
| `beat_sheet.json` | Narrative + visual plan (source of truth) |
| `README.md` | This file |
| `SOURCES.md` | Every figure against its paper, table and section |
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
