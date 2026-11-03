# The Arrow Points The Other Way

**Fellow:** Uday Sonawane
**Date:** 2026-09-25
**Format:** `ai-explainer` chassis on the `claude-hai` channel key (Brutalist)
**Runtime:** ~3:49 (229.23s measured) · 11 beats
**Narrator:** Onyx (`am_onyx`) · Register: Pragmatist
**Channel chip / handle on cut:** `@HumanitariansAI`
**Audience:** students — smart people getting started
**Deliverable (local):** `QuantumAI_UdaySonawane_09_25_2026.mp4`

## What this video is about

The commissioning brief's central claim was that qubits find patterns in large
classical data sets faster than ordinary computers. That turns out to be the
**least supported part of the field**, so the video reports what has actually
been demonstrated instead — and the demonstrated wins point the other way.

**The framework (B02) — three questions for any quantum AI claim:**

1. Which direction is the help flowing — quantum helping AI, or AI helping quantum?
2. What does the data have to do before a quantum algorithm can touch it?
3. Has a classical algorithm since matched the result?

Question three is where the field gets uncomfortable. **Ewin Tang's 2018 result**
produced a classical algorithm matching quantum recommendation systems — the
advantage had come from input assumptions rather than from quantum mechanics —
and a wider class of QML algorithms was subsequently dequantized.

Where quantum genuinely wins is the reverse direction: **AlphaQubit**, a neural
decoder for quantum error correction (Google DeepMind / Google Quantum AI,
*Nature* 2024), beating tensor-network decoding by 6% and correlated matching by
30%, holding from 17 qubits to 241. That is machine learning helping quantum
computing, not the other way round.

## Sourcing

The field is unusually prone to headline figures that are true in a narrow
technical sense and misleading in plain reading. The standard applied: every
number names a published result, and the one famous benchmark that is routinely
misread is shown **with its caveat attached** rather than quoted bare.

`FACTCHECK.md` is signed **GATE F — 2026-09-25, 12 rows PASS**, and records that
**two of the brief's claims did not survive checking and were rewritten**; one
survived and is used. Primary sources include the AlphaQubit paper, Tang (2018)
and Tang et al. (2019), and Google's below-threshold error-correction result
(Willow, 105 qubits, 2024).

## Package contents

| File | Role |
|---|---|
| `beat_sheet.json` | Narrative + visual plan (source of truth) |
| `README.md` | This file |
| `SOURCES.md` | Every on-screen figure against its published result |
| `FACTCHECK.md` | GATE F signed; includes the brief's claims that failed checking |
| `CHECKS-REPORT.md` | PROOF gate, with the teaching arc |
| `SHOTLIST.md` | Per-beat shot plan |
| `PROMPTS.md` | Reproducible prompts used to build the video |
| `scenes.py` | Authored Manim scenes |
| `layout_audit.md` / `.json` | Frame-level layout audit |
| `layout_audit_frames/*.png` | Sampled audit stills |

Not tracked here (gitignored, local only): `clips/`, `media/`, `manim/`,
`pantry/`, `_qc/`, `mp3/` (now excluded repo-wide), `qc-sheet.png`, and the masters.

**No `BUILD-LOG.md` in this package**, unlike the earlier eight videos. The
build record that usually doubles as this work's frictional log was not written
for this cut.

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
