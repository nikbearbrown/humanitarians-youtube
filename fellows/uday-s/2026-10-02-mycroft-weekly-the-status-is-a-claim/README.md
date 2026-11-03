# The Status Is A Claim

**Fellow:** Uday Sonawane
**Date:** 2026-10-02
**Format:** `cli-explainer` spine, applied as a weekly work report (Brutalist)
**Runtime:** ~3:15 (195.37s measured) · 12 beats
**Narrator:** Onyx (`am_onyx`) · Register: Pragmatist
**Channel chip / handle on cut:** `@HumanitariansAI`
**Subject:** `D:/Projects/mycroft` @ commit `8c13b87`, branch `feature/market-sentiment-human-report`
**Deliverable (local):** `Mycroft_UdaySonawane_10_02_2026.mp4`

**Episode 6 of the Mycroft weekly.**

| Episode | Commit | Video |
|---|---|---|
| 1 | `9ef4e7f` | [Build the Defects First](../2026-08-27-weekly-fixtures-before-validators/) |
| 2 | `bdc1bc1` | [Transport, Do Not Repair](../2026-09-03-mycroft-weekly-transport-do-not-repair/) |
| 3 | `253ee74` | [Both Sets Scored 64](../2026-09-10-mycroft-weekly-both-sets-scored-64/) |
| 4 | `aa0c0fe` | [It Never Says Pass](../2026-09-17-mycroft-weekly-it-never-says-pass/) |
| 5 | `4157a8e` | [Passing For The Wrong Reason](../2026-09-25-mycroft-weekly-passing-for-the-wrong-reason/) |
| 6 | `8c13b87` | **this one** |

## What this video is about

Episode 5 gave two gates real failure paths. This episode asks what a status
field is actually worth once you try to write down the evidence behind it.

**The framework (B02) — three questions for any status field:**

1. What did you run?
2. What did it cover?
3. What would make the status wrong?

Question three is the expensive one. The attestation records **17 rows, 7 of
them break tests**, 18/18 defects at their expected locations split 8 in step 3
and 10 in step 4, and **0 leaks between steps**.

The falsifiability beat (B08) is the honest part: nine things broke while the
attestation was being written. The status was a claim before it was a record.

## Package contents

| File | Role |
|---|---|
| `beat_sheet.json` | Narrative + visual plan; carries `source_repo` / `source_commit` |
| `README.md` | This file |
| `SOURCES.md` | Every on-screen figure against the file in the repo it came from |
| `FACTCHECK.md` | Claim-level verdicts |
| `CHECKS-REPORT.md` | PROOF gate, with the teaching arc |
| `SHOTLIST.md` | Per-beat shot plan |
| `PROMPTS.md` | Reproducible prompts used to build the video |
| `scenes.py` | Authored Manim scenes |
| `layout_audit.md` / `.json` | Frame-level layout audit |

Not tracked here (gitignored, local only): `clips/`, `media/`, `manim/`,
`pantry/`, `_qc/`, `mp3/`, `qc-sheet.png`, and the masters.

**No `BUILD-LOG.md`**, as with episode 5. The frictional log for the underlying
engineering work is at
[`../frictional-logs/2026-10-02-closing-the-two-todos.md`](../frictional-logs/2026-10-02-closing-the-two-todos.md).

## Provenance warning

This video lives **outside** the repository it documents, so the subject commit
is not implied by folder location. `beat_sheet.json` (`source_repo`,
`source_commit` = `8c13b87`) is the only link. The subject is a **feature
branch** (`feature/market-sentiment-human-report`), so that reference could be
rebased or squashed away upstream.

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
