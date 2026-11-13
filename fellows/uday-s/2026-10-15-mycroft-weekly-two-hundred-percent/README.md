# Two Hundred Percent

**Fellow:** Uday Sonawane
**Date:** 2026-10-15
**Format:** `cli-explainer` spine, applied as a weekly work report (Brutalist)
**Runtime:** ~3:29 (209.28s measured) · 12 beats
**Narrator:** Onyx (`am_onyx`) · Register: Pragmatist
**Channel chip / handle on cut:** `@HumanitariansAI`
**Subject:** `D:/Projects/mycroft` @ commit `d85106b`, branch `feat/snickerdoodle-cli`
**Deliverable (local):** `Mycroft_UdaySonawane_10_15_2026.mp4`

**Episode 8 of the Mycroft weekly.**

| Episode | Commit | Video |
|---|---|---|
| 1 | `9ef4e7f` | [Build the Defects First](../2026-08-27-weekly-fixtures-before-validators/) |
| 2 | `bdc1bc1` | [Transport, Do Not Repair](../2026-09-03-mycroft-weekly-transport-do-not-repair/) |
| 3 | `253ee74` | [Both Sets Scored 64](../2026-09-10-mycroft-weekly-both-sets-scored-64/) |
| 4 | `aa0c0fe` | [It Never Says Pass](../2026-09-17-mycroft-weekly-it-never-says-pass/) |
| 5 | `4157a8e` | [Passing For The Wrong Reason](../2026-09-25-mycroft-weekly-passing-for-the-wrong-reason/) |
| 6 | `8c13b87` | [The Status Is A Claim](../2026-10-02-mycroft-weekly-the-status-is-a-claim/) |
| 7 | `fbd30b6` | [Green Because It Wasn't Looking](../2026-10-09-mycroft-weekly-green-because-it-wasnt-looking/) |
| 8 | `d85106b` | **this one** |

## What this video is about

Episode 7 made the conformance checker actually read the code. This episode
builds the `snickerdoodle` command the recipes have always documented, and then
asks what its first results actually mean.

**The framework (B02) — three questions for any percentage in a repository:**

1. What is the denominator?
2. Does the checker say so itself?
3. What does the number change about what you do on Monday?

The headline is the denominator problem. The recipes reference the documented
commands **1,444 times across 97 recipes** — a command that had never existed.
Running the new checker across all 97 produced **616 findings**, with **94 of 97**
flagged and **zero clean**. But the figure the episode is named for comes from a
denominator so small the percentage stops meaning anything: 4 of 97 recipes
advertise a comparison, and **93 have nothing to compare at all**.

B06 shows the checker saying this in its own source — the denominator comment is
in the code, not just the narration. B08 applies the series' own rule: recount
rather than trust the number you were handed.

## Sourcing

Every figure is re-derived with the exact command recorded in
[`SOURCES.md`](./SOURCES.md) — `git grep -c` for the occurrence counts, a
read-only `snickerdoodle check --all` run for the findings, and `git show` for
the source quotations. The commit body is treated as a claim to check, not a
source.

## Package contents

| File | Role |
|---|---|
| `beat_sheet.json` | Narrative + visual plan; carries `source_repo` / `source_commit` |
| `README.md` | This file |
| `SOURCES.md` | Every on-screen figure and the command that produced it |
| `FACTCHECK.md` | Claim-level verdicts |
| `CHECKS-REPORT.md` | PROOF gate, with the teaching arc |
| `SHOTLIST.md` | Per-beat shot plan |
| `PROMPTS.md` | Reproducible prompts used to build the video |
| `scenes.py` | Authored Manim scenes |
| `layout_audit.md` / `.json` | Frame-level layout audit |

Not tracked here (gitignored, local only): `clips/`, `media/`, `manim/`,
`pantry/`, `_qc/`, `mp3/`, `qc-sheet.png`, and the masters.

**No `BUILD-LOG.md`**, as with recent episodes. The frictional logs for the
underlying engineering are
[`../frictional-logs/2026-10-15-snickerdoodle-cli.md`](../frictional-logs/2026-10-15-snickerdoodle-cli.md)
and
[`../frictional-logs/2026-10-15-check-verb.md`](../frictional-logs/2026-10-15-check-verb.md).

## Provenance warning

This video lives **outside** the repository it documents, so the subject commit
is not implied by folder location. `beat_sheet.json` (`source_repo`,
`source_commit` = `d85106b`) is the only link. The subject is a **feature
branch** (`feat/snickerdoodle-cli`), so that reference could be rebased or
squashed away upstream.

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
