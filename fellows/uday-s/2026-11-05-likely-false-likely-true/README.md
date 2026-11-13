# Likely False, Likely True

**Fellow:** Uday Sonawane
**Date:** 2026-11-05
**Format:** `ai-explainer` spine on the `claude-hai` channel key (Brutalist)
**Runtime:** ~4:01 (241.49s measured) · 11 beats
**Narrator:** Onyx (`am_onyx`) · Register: Pragmatist
**Channel chip / handle on cut:** `@HumanitariansAI`
**Topic:** Weekly STEM — algorithmic trading and the statistics of claimed edges
**Deliverable (local):** `AlgorithmicTrading_UdaySonawane_11_05_2026.mp4`

## What this video is about

Two papers reach opposite conclusions about the same literature, and the title
is both of their claims side by side. Algorithmic trading is a field rather than
a claim, so B01 narrows it to something that can actually be tested.

**The framework (B02) — three questions for any claimed edge:**

1. How many were tried?
2. What does "false" mean here?
3. Whose bar, and why that one?

Question one is the scale of the problem: **316 factors** across **313
articles**, 250 of them published, with discovery rates rising from about one a
year to roughly eighteen — **164 in nine years against 84 in all prior years
combined**. If hundreds of candidates are tested, the usual **t > 2.0** bar
stops meaning what it is taken to mean, which is why **t > 3.0** was proposed.

B05 is the falsifiability beat, and deliberately not a blog post: a Federal
Reserve Board paper arguing close to the opposite, with bounds. B06 is the
striking part — where the two sides actually agree — and B07 is what survives
that neither contests.

## Sourcing

Two primary sources carry every figure; no aggregator, blog, vendor page or
summary sourced a number. Figures were extracted from the papers' own text, and
the two headline phrases are quoted verbatim and attributed rather than
paraphrased. Full ledger in [`SOURCES.md`](./SOURCES.md).

## Package contents

| File | Role |
|---|---|
| `beat_sheet.json` | Narrative + visual plan (source of truth) |
| `README.md` | This file |
| `SOURCES.md` | Every figure against its paper, with quoted phrases attributed |
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
