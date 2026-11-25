# The Lucky Case

**Fellow:** Uday Sonawane
**Date:** 2026-11-05
**Format:** `cli-explainer` spine, applied as a weekly work report (Brutalist)
**Runtime:** ~3:25 (204.71s measured) · 12 beats
**Narrator:** Onyx (`am_onyx`) · Register: Pragmatist
**Channel chip / handle on cut:** `@HumanitariansAI`
**Subject:** `D:/Projects/mycroft` @ commit `0358ab9`, branch `chore/recipe-lifecycle-frontmatter`
**Deliverable (local):** `Mycroft_UdaySonawane_11_05_2026.mp4`

**Episode 11 of the Mycroft weekly.**

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
| 11 | `0358ab9` | **this one** |

## What this video is about

Every recipe carries a Step Commands table with a Flags column, and that column
feeds the runner's command. The ask was narrow: find out whether it is actually
read.

**The framework (B02) — three questions:**

1. Is this field read by a machine?
2. Does it crash, or do something worse?
3. What else carries the same shape?

The answer to question two is the title. Reproduced standalone in a fresh
interpreter, the mechanism has two cases: the flag prefix on its own produces a
**clean crash**; the prefix followed by a word is **silently absorbed**. The
crash is the lucky one — it tells you.

Question one is answered by looking at all of them: **six built recipes carried
identical boilerplate**, with 24 rows removed and 24 added in the fix. B07 is
the check made before dropping a sample flag from recipes that might need it,
and B08 closes the loop back on the earlier episodes.

**85 defects down to 5.**

## Sourcing

Single-source video from `mycroft` at `0358ab9`, with one standalone
reproduction and no web sources. [`SOURCES.md`](./SOURCES.md) marks which rows
are **reproduced** (Cases A and B, re-run in a fresh `python3` interpreter)
versus taken from the commit body, so the two kinds of evidence stay distinct.

## Package contents

| File | Role |
|---|---|
| `beat_sheet.json` | Narrative + visual plan; carries `source_repo` / `source_commit` |
| `README.md` | This file |
| `SOURCES.md` | Every figure, its command, and which rows were reproduced |
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
[the flag contract](../frictional-logs/2026-11-05-flag-contract.md) and
[rebase and TODO drift](../frictional-logs/2026-11-05-rebase-todos-drift.md).

## Provenance warning

This video lives **outside** the repository it documents, so the subject commit
is not implied by folder location. `beat_sheet.json` (`source_repo`,
`source_commit` = `0358ab9`) is the only link. The subject is a **feature
branch** (`chore/recipe-lifecycle-frontmatter`), so that reference could be
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
