# Twenty Percent, Or Five

**Fellow:** Uday Sonawane
**Date:** 2026-11-18
**Format:** `ai-explainer` spine (Brutalist)
**Runtime:** ~4:07 (246.55s measured) · 11 beats
**Narrator:** Onyx (`am_onyx`) · Register: Pragmatist
**Channel chip / handle on cut:** `@HumanitariansAI`
**Topic:** AI · music practice — what a practice tool can and cannot claim
**Deliverable (local):** `AIMusicPractice_UdaySonawane_11_18_2026.mp4`

## What this video is about

If you practise an instrument, the question is what an AI practice tool can
honestly claim. B01 narrows it: such a tool is not a performance intervention,
and the distinction decides which evidence applies.

**The framework (B02) — three questions for any claim about practice:**

1. How was practice measured?
2. Which domain, and does it transfer?
3. What is the comparison group?

The headline is a meta-analysis across domains, and the title is its range:
deliberate practice explains **twenty percent** of performance variance in some
domains and about **five** in others — depending heavily on the domain and on
how practice was measured.

B04 and B05 are the measurement problem on each axis in turn. B06 applies the
framework to an AI practice app specifically. B07 is the falsifiability beat and
the first limit **cuts against the video's own argument** rather than for it.

## Sourcing

**One primary source**, and every number on screen was read out of the paper
itself — a locally saved PDF extracted with `pdftotext -layout`, not from a
summary, press release, blog post or book about it. That provenance is stated
explicitly at the top of [`SOURCES.md`](./SOURCES.md), which matters here
because this particular finding is more often quoted secondhand than read.

Source: Macnamara, Hambrick & Oswald (2014), *"Deliberate Practice and
Performance in Music, Games, Sports, Education, and Professions: A
Meta-Analysis"*, **Psychological Science**.

## Package contents

| File | Role |
|---|---|
| `beat_sheet.json` | Narrative + visual plan (source of truth) |
| `README.md` | This file |
| `SOURCES.md` | The single source, how it was accessed, and what each figure supports |
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
