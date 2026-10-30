# Unbuilt Is Not Broken

**Fellow:** Uday Sonawane
**Date:** 2026-10-30
**Format:** `cli-explainer` spine, applied as a weekly work report (Brutalist)
**Runtime:** ~3:24 (203.72s measured) · 12 beats
**Narrator:** Onyx (`am_onyx`) · Register: Pragmatist
**Channel chip / handle on cut:** `@HumanitariansAI`
**Subject:** `D:/Projects/mycroft` @ commit `6428457`, branch `chore/recipe-lifecycle-frontmatter`
**Deliverable (local):** `Mycroft_UdaySonawane_10_30_2026.mp4`

**Episode 10 of the Mycroft weekly.**

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
| 10 | `6428457` | **this one** |

## What this video is about

Episode 8 built the thing that counts problems. This episode stops it counting
honest states as problems — a step that was never built is not a step that is
broken.

**The framework (B02) — three questions for any count of problems:**

1. Does it contradict a claim?
2. Who decided the severity?
3. Does the thing that generates these know the rule?

The arithmetic is the story. **725 findings** became **171 defects** once
severity was applied, then **80** once lifecycle frontmatter was read — because
**554 of them were unbuilt steps across 94 recipes**, which were never defects
at all. Of 97 recipes, **90 now have no defects.**

B06 shows the change itself is **eight lines**. B07 asks whether the generator
that writes these records knows the rule, and B08 is unplanned — something found
while checking the rest.

## Sourcing

Single-source video — everything comes from `mycroft` at `6428457`, with
companions `83793ff` and `0536907`, no web sources. [`SOURCES.md`](./SOURCES.md)
marks which figures are **author-reported from a commit body** rather than
re-run, and says plainly that the pre-change state cannot be reproduced — the
725 figure is one of those.

## Package contents

| File | Role |
|---|---|
| `beat_sheet.json` | Narrative + visual plan; carries `source_repo` / `source_commit` |
| `README.md` | This file |
| `SOURCES.md` | Every figure, its command, and which ones cannot be re-run |
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
[lifecycle frontmatter](../frictional-logs/2026-10-30-lifecycle-frontmatter.md),
[check status awareness](../frictional-logs/2026-10-30-check-status-awareness.md)
and [conformance data/Python](../frictional-logs/2026-10-30-conformance-data-python.md).

## Provenance warning

This video lives **outside** the repository it documents, so the subject commit
is not implied by folder location. `beat_sheet.json` (`source_repo`,
`source_commit` = `6428457`) is the only link. The subject is a **feature
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
