# It Looked Complete

**Fellow:** Uday Sonawane
**Date:** 2026-10-22
**Format:** `cli-explainer` spine, applied as a weekly work report (Brutalist)
**Runtime:** ~3:17 (196.80s measured) · 12 beats
**Narrator:** Onyx (`am_onyx`) · Register: Pragmatist
**Channel chip / handle on cut:** `@HumanitariansAI`
**Subject:** `D:/Projects/mycroft` @ commit `93485c4`, branch `feat/gate-records`
**Deliverable (local):** `Mycroft_UdaySonawane_10_22_2026.mp4`

**Episode 9 of the Mycroft weekly.**

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
| 9 | `93485c4` | **this one** |

## What this video is about

Episode 8 built the command that runs the steps. This episode makes the record
it writes carry its own evidence — and finds that the record looked complete
while five fields were simply absent.

**The framework (B02) — three questions for any record that claims something
was checked:**

1. Does it name what it looked at?
2. Can it tell *absent* from *checked and fine*?
3. Does it mark what it could not reach?

Question one lands on a derived evidence list. Gate 3's test names two directory
paths; the record's depth-1 stop meant it never saw the **26 JSON files** that
sit two levels down — 14 in one tree, 12 in the other — because each top level
held only 3 and 1 entries.

Question two is the one worth taking slowly: a field that is missing and a field
that was checked and found fine had been indistinguishable. B07 adds the marking
for what a run could not reach, and B08 is the falsifiability beat that makes
the point better than the fix does.

After the change, all six gates pass for reasons the record states.

## Sourcing

Single-source video — everything comes from the `mycroft` repository at
`93485c4`, with no web sources. The commit body is treated as a claim and
confirmed against the diff; file counts come from `git ls-tree` over the two
trees the test names. Commands are recorded in [`SOURCES.md`](./SOURCES.md).

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

**No `BUILD-LOG.md`**, as with recent episodes. The frictional log for the
underlying engineering is
[`../frictional-logs/2026-10-22-gate-records.md`](../frictional-logs/2026-10-22-gate-records.md).

## Provenance warning

This video lives **outside** the repository it documents, so the subject commit
is not implied by folder location. `beat_sheet.json` (`source_repo`,
`source_commit` = `93485c4`) is the only link. The subject is a **feature
branch** (`feat/gate-records`), so that reference could be rebased or squashed
away upstream.

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
