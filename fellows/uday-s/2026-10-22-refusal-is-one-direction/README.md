# Refusal Is One Direction

**Fellow:** Uday Sonawane
**Date:** 2026-10-22
**Format:** `ai-explainer` spine on the `claude-hai` channel key (Brutalist)
**Runtime:** ~4:22 (262.36s measured) · 11 beats
**Narrator:** Onyx (`am_onyx`) · Register: Pragmatist
**Channel chip / handle on cut:** `@HumanitariansAI`
**Topic:** Weekly STEM — what "abliteration" actually is
**Deliverable (local):** `Abliteration_UdaySonawane_10_22_2026.mp4`

## Non-operational and defensive by design

`FACTCHECK.md` carries an explicit scope section: **this video is deliberately
non-operational.** No frame contains code, a layer index, or a procedure. All
practical guidance runs defensively — how to evaluate a third-party edited model
*before* running it. There are also sections for **"Attribution deliberately
omitted"**, **"Claims deliberately NOT made"** and, in `SOURCES.md`, **"What was
deliberately not sought."**

The actionable beat (B09) is a scaffold for anyone considering a third-party
model, not a method.

## The title was corrected

Commissioned as *"Neuron Abliteration to Uncensor an LLM"*, with permission to
retitle. Both halves of that phrase are wrong, and B01 says so before anything
else:

| The phrase says | Verdict | What the video says |
|---|---|---|
| **"Neuron"** | Wrong | The intervention targets a **one-dimensional subspace — a direction** — in activation space, not a neuron |
| **"Uncensor"** | Misleading | Uncensoring implies withheld knowledge being released. What changes is a **behaviour**: the model stops declining |

`FACTCHECK.md` is signed **GATE F — 2026-10-22: 12 rows PASS, 1 title CORRECTED,
1 source SCOPED DOWN on screen.**

## The framework (B02) — three questions

1. What was actually changed?
2. What did it cost?
3. Who else touched the weights?

The source finding (arXiv 2406.11717) is that across **13 open chat models, up
to 72B**, refusal is mediated by a one-dimensional subspace — one direction per
model. The paper's own conclusion is quoted and attributed: it underscores the
brittleness of current safety fine-tuning methods.

B05 is the falsifiability beat and it undercuts the simple story: a later result
(arXiv 2602.02132) finds refusal maps to **geometrically distinct directions per
category**, so the single-knob framing does not hold up.

B06 states the limit plainly — **it adds no capability.** B07 is the practical
question about weight provenance, which is where the video lands.

## Sourcing

Three sources, each read directly — no aggregator, forum post, wiki or blog
sourced any figure. Listed in [`SOURCES.md`](./SOURCES.md), along with what was
deliberately not sought.

## Package contents

| File | Role |
|---|---|
| `beat_sheet.json` | Narrative + visual plan (source of truth) |
| `README.md` | This file |
| `SOURCES.md` | Every figure against its paper, plus what was not sought |
| `FACTCHECK.md` | GATE F signed; scope, title correction, omissions |
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
