# The Fourth Gate

**Fellow:** Uday Sonawane
**Date:** 2026-11-27
**Format:** `cli-explainer` spine, applied as a weekly work report (Brutalist)
**Runtime:** ~3:46 (226.25s measured) · 12 beats
**Narrator:** Onyx (`am_onyx`) · Register: Pragmatist
**Channel chip / handle on cut:** `@HumanitariansAI`
**Subject:** `D:/Projects/mycroft` @ commit `20795b2`, branch `chore/promote-scenariostresstestingagent`
**Deliverable (local):** `Mycroft_UdaySonawane_11_27_2026.mp4`

**Episode 14 of the Mycroft weekly.**

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
| 13 | `08b92d3` | [It Never Ran](../2026-11-18-mycroft-weekly-it-never-ran/) |
| 14 | `20795b2` | **this one** |

## What this video is about

One recipe was promoted, and the ask was to take that sign-off apart — my own.

**The framework (B02) — three questions for any check that guards a promotion:**

1. Can it fail?
2. What happens to a failure it cannot judge?
3. What was written down?

B04 quotes the three gates verbatim. B05 re-runs all three **outside the
repository**, against planted defects, so each one's failure path is shown
rather than assumed. B06 is the gate nobody named — **gate four**, which is the
title.

## The recount corrects the author

B07 is the falsifiability beat, and this week it does not vindicate the work:
the recount **corrects a claim in the commit message**. B08 is what survived it.
B09 answers why sign the promotion at all.

That is the pattern worth noting — the commit message is treated as a claim to
check, and here the check went against it.

## Sourcing

Two places only: the `mycroft` repository at `20795b2`, read-only, and a scratch
folder outside it where every gate test was re-run against planted defects.
[`SOURCES.md`](./SOURCES.md) keeps those separate, and marks which rows come
from the commit message — including the one the recount corrects.

## Package contents

| File | Role |
|---|---|
| `beat_sheet.json` | Narrative + visual plan; carries `source_repo` / `source_commit` |
| `README.md` | This file |
| `SOURCES.md` | Every figure, its access method, and which rows were re-run outside the repo |
| `FACTCHECK.md` | Claim-level verdicts |
| `CHECKS-REPORT.md` | PROOF gate, with the teaching arc |
| `SHOTLIST.md` | Per-beat shot plan |
| `PROMPTS.md` | Reproducible prompts used to build the video |
| `scenes.py` | Authored Manim scenes |
| `layout_audit.md` / `.json` | Frame-level layout audit |
| `layout_audit_frames/*.png` | Sampled audit stills |

Not tracked here (gitignored, local only): `clips/`, `media/`, `manim/`,
`pantry/`, `_qc/`, `mp3/`, `qc-sheet.png`, and the masters.

**No `BUILD-LOG.md`**, as with recent episodes. The frictional log for the
underlying engineering is
[`../frictional-logs/2026-11-27-promote-scenario-agent.md`](../frictional-logs/2026-11-27-promote-scenario-agent.md).

## Provenance warning

This video lives **outside** the repository it documents, so the subject commit
is not implied by folder location. `beat_sheet.json` (`source_repo`,
`source_commit` = `20795b2`) is the only link. The subject is a **feature
branch** (`chore/promote-scenariostresstestingagent`), so that reference could
be rebased or squashed away upstream.

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
