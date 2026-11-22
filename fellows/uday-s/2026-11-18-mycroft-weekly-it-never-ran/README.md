# It Never Ran

**Fellow:** Uday Sonawane
**Date:** 2026-11-18
**Format:** `cli-explainer` spine, applied as a weekly work report (Brutalist)
**Runtime:** ~3:44 (223.86s measured) · 12 beats
**Narrator:** Onyx (`am_onyx`) · Register: Pragmatist
**Channel chip / handle on cut:** `@HumanitariansAI`
**Subject:** `D:/Projects/mycroft` @ commit `08b92d3`, branch `fix/conformance-multidoc-yaml`
**Deliverable (local):** `Mycroft_UdaySonawane_11_18_2026.mp4`

**Episode 13 of the Mycroft weekly — a direct sequel to episode 12**, which
diagnosed the multi-document YAML problem. This episode finds out why the fix
produced no output.

| Episode | Commit | Video |
|---|---|---|
| 1 | `9ef4e7f` | [Build the Defects First](../2026-08-27-weekly-fixtures-before-validators/) |
| 2 | `bdc1bc1` | [Transport, Do Not Repair](../2026-09-03-mycroft-weekly-transport-do-not-repair/) |
| 3 | `253ee74` | [Both Sets Scored 64](../2026-09-10-mycroft-weekly-both-sets-scored-64/) |
| 4 | `aa0c0fe` | [It Never Says Pass](../2026-09-17-mycroft-weekly-it-never-says-pass/) |
| 5 | `4157a8e` | [Passing For The Wrong Reason](../2026-09-25-mycroft-weekly-passing-for-the-wrong-reason/) |
| 6 | `8c13b87` | [The Status Is A Claim](../2026-10-02-mycroft-weekly-the-status-is-a-claim/) |
| 7 | `fbd30b6` | [Green Because It Wasn't Looking](../2026-10-09-mycroft-weekly-green-because-it-wasnt-looking/) |
| 8 | `d85106b` | [Two Hundred Percent](../2026-10-15-mycroft-weekly-two-hundred-percent/) |
| 9 | `93485c4` | [It Looked Complete](../2026-10-22-mycroft-weekly-it-looked-complete/) |
| 10 | `6428457` | [Unbuilt Is Not Broken](../2026-10-30-mycroft-weekly-unbuilt-is-not-broken/) |
| 11 | `0358ab9` | [The Lucky Case](../2026-11-05-mycroft-weekly-the-lucky-case/) |
| 12 | `b425b19` | [Every Row Was True](../2026-11-13-mycroft-weekly-every-row-was-true/) |
| 13 | `08b92d3` | **this one** |

## What this video is about

Episode 12 found that three Kubernetes manifests are multi-document YAML and the
checker was reading only the first document of each. This episode asks why the
fix produced nothing — and the answer is the title.

**The framework (B02) — three questions:**

1. Did the fix change any behaviour?
2. Why did nobody notice?
3. What else has the same shape?

B04 is the single line responsible: it builds a shell command, and the mangling
happens there. B05 reproduces the whole thing standalone, with nothing else in
play. B06 answers why it went unseen — the catch swallowed it. B07 names one
more instance that is the same shape.

B08 is the recount: **the four changed lines are exactly the four**, verified
rather than asserted. B09 lands on eight contributing factors.

## Sourcing

Every figure comes from one of two places, and [`SOURCES.md`](./SOURCES.md)
separates them: the `mycroft` repository at a named commit — including
`scripts/conformance.mjs` at both `08b92d3` and its **parent** `08b92d3^`, so
the before-and-after line is quoted verbatim from each — or a **standalone
interpreter run outside the repository**. No web sources.

## Package contents

| File | Role |
|---|---|
| `beat_sheet.json` | Narrative + visual plan; carries `source_repo` / `source_commit` |
| `README.md` | This file |
| `SOURCES.md` | Every figure, its access method, and whether it was reproduced standalone |
| `FACTCHECK.md` | Claim-level verdicts |
| `CHECKS-REPORT.md` | PROOF gate, with the teaching arc |
| `SHOTLIST.md` | Per-beat shot plan |
| `PROMPTS.md` | Reproducible prompts used to build the video |
| `scenes.py` | Authored Manim scenes |
| `layout_audit.md` / `.json` | Frame-level layout audit |

Not tracked here (gitignored, local only): `clips/`, `media/`, `manim/`,
`pantry/`, `_qc/`, `mp3/`, `qc-sheet.png`, and the masters.

**No `BUILD-LOG.md`**, as with recent episodes. The frictional log for the
underlying engineering is
[`../frictional-logs/2026-11-18-yaml-batch-never-ran.md`](../frictional-logs/2026-11-18-yaml-batch-never-ran.md).

## Provenance warning

This video lives **outside** the repository it documents, so the subject commit
is not implied by folder location. `beat_sheet.json` (`source_repo`,
`source_commit` = `08b92d3`) is the only link. The subject is a **feature
branch** (`fix/conformance-multidoc-yaml`), so that reference could be rebased
or squashed away upstream.

## Toolkit (rebuild)

```bash
git clone https://github.com/nikbearbrown/brutalist.art.git
cd brutalist.art
./setup --install
./setup
```

Audio-first, Kokoro-only, no API keys. Regenerate narration first, then let the
measured durations drive the scenes — timing is never fixed by hand.

## Publishing

Not authorized by this package. The master stays local until a human decides to
share or upload.
