# Three Things Called Recycling

**Fellow:** Uday Sonawane
**Date:** 2026-10-15
**Format:** `ai-explainer` spine on the `claude-hai` channel key (Brutalist)
**Runtime:** ~3:39 (218.52s measured) · 11 beats
**Narrator:** Onyx (`am_onyx`) · Register: Pragmatist
**Channel chip / handle on cut:** `@HumanitariansAI`
**Topic:** Weekly STEM — energy-recycling photonics
**Deliverable (local):** `EnergyRecyclingPhotonics_UdaySonawane_10_15_2026.mp4`

## What this video is about

The commissioned phrase does not name a single research programme. Rather than
pretending there is one canonical result, **B01 separates the three distinct
things the phrase is used for** — and says so on screen.

**The framework (B02) — three questions for any photonic recycling claim:**

1. What is actually being reused?
2. What did reusing it buy?
3. What does the headline leave out?

The strongest published example is an optical parametric amplifier on thin-film
lithium niobate, where the pump is generated in a resonator and recirculated —
**more than 17 dB of gain at under 200 mW input power** (arXiv 2509.26425;
published in *Nature* 649, 1159–1164, 28 January 2026).

B06 is the falsifiability beat: the part that does not survive the headline.
B07 covers the other two layers the phrase gets attached to, including energy
recovery in particle accelerators.

## Sourcing

The video states how the category itself was established — two independent
searches, recorded under *"How the category was established"* in
[`SOURCES.md`](./SOURCES.md) — because the phrase has no single owner and the
scope of the claim is part of what needed checking. Every number is attributed
to the paper's abstract or the journal listing.

## Package contents

| File | Role |
|---|---|
| `beat_sheet.json` | Narrative + visual plan (source of truth) |
| `README.md` | This file |
| `SOURCES.md` | Every figure against its source, plus how the category was established |
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
