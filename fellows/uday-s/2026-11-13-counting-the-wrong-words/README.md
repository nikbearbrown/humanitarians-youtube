# Counting The Wrong Words

**Fellow:** Uday Sonawane
**Date:** 2026-11-13
**Format:** `ai-explainer` spine on the `claude-hai` channel key (Brutalist)
**Runtime:** ~3:43 (223.44s measured) · 11 beats
**Narrator:** Onyx (`am_onyx`) · Register: Pragmatist
**Channel chip / handle on cut:** `@HumanitariansAI`
**Topic:** Weekly STEM — market sentiment analysis and what a word list actually counts
**Deliverable (local):** `MarketSentimentAnalysis_UdaySonawane_11_13_2026.mp4`

## What this video is about

If you want to measure market sentiment, the first question is what your word
list is actually counting. B01 narrows the job: a sentiment score is a counting
exercise, and the counting can be wrong while the arithmetic is right.

**The framework (B02) — three questions before you trust a sentiment number:**

1. What counts as negative, and who decided?
2. How much of the score is a few common words?
3. Has anyone checked it predicts anything?

The measurement comes from Loughran & McDonald (2011), across **121,217 filings
from 1994 to 2008**: using a general-purpose word list, **73.8% of negative word
counts** are words that are not negative in a financial setting. Seven words
alone account for **more than a quarter**, and *costs* by itself is **4.61% of
the total**.

B05 is the second failure mode in the same list — *foreign* catching
international operations, *vice* catching vice-presidents, and *mine*, *cancer*,
*crude* and *tire* simply identifying an industry segment. B06 is the fix, B07
the limits the original authors themselves set, and B08 brings question three
back to the repository.

## Sourcing

One primary paper carries every figure, plus one quotation from the `mycroft`
repository — no aggregator, blog or summary sourced a number. Figures were read
directly out of the *Journal of Finance* PDF with `pdftotext` rather than from
any secondary description. Full ledger in [`SOURCES.md`](./SOURCES.md).

## Package contents

| File | Role |
|---|---|
| `beat_sheet.json` | Narrative + visual plan (source of truth) |
| `README.md` | This file |
| `SOURCES.md` | Every figure against the paper's body, table or abstract |
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
