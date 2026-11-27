# Who Decides It's A Bug?

**Fellow:** Uday Sonawane
**Date:** 2026-11-27
**Format:** `ai-explainer` spine (Brutalist)
**Runtime:** ~4:31 (270.47s measured) · 11 beats
**Narrator:** Onyx (`am_onyx`) · Register: Pragmatist
**Channel chip / handle on cut:** `@HumanitariansAI`
**Topic:** AI · software testing
**Deliverable (local):** `AIBetaTesting_UdaySonawane_11_27_2026.mp4`

## The title was changed, and the change is the point

Commissioned as *"Implications/Advantages of using AI as a Beta Tester for games
and other kinds of software"*, retitled under the standing permission to make a
title professional and correct.

The retitle is the argument: the hard part of testing is not generating inputs,
it is deciding what counts as a failure. **That is the oracle problem**, and the
question in the title is the one the whole video turns on.

## What this video is about

B01 splits the job, because "beta tester" bundles several different things.

**The framework (B02) — three questions you can ask of any testing tool:**

1. What is the oracle?
2. Who decides it is a bug?
3. What does it actually deliver?

The three evidence beats are three cases, ordered by how much the oracle costs:

- **B03 — the oracle is free.** If the program crashes, nobody has to judge it.
- **B04 — where AI enters**, and it enters at a specific point rather than everywhere.
- **B05 — the oracle has to be written**, which is the expensive case.

B06 is what it delivers when it works. B07 is the falsifiability beat, and this
one is **the author checking his own sources** rather than checking the field.

## Sourcing

Three primary sources, each read directly — no figure from secondary coverage,
a vendor page or a summary. Figures from the OSS-Fuzz README are **dated (May
2025)** on screen rather than quoted as current, since that README changes; the
OSS-Fuzz-Gen README supplies the reported-bug count and grading metrics; and
Meta's TestGen-LLM paper (arXiv:2402.09171) was extracted verbatim.

Full ledger in [`SOURCES.md`](./SOURCES.md).

## Package contents

| File | Role |
|---|---|
| `beat_sheet.json` | Narrative + visual plan (source of truth) |
| `README.md` | This file |
| `SOURCES.md` | The three sources, how each was accessed, and what each figure supports |
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
