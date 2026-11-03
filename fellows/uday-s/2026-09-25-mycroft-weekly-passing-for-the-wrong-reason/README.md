# Passing For The Wrong Reason

**Fellow:** Uday Sonawane
**Date:** 2026-09-25
**Format:** `cli-explainer` spine, applied as a weekly work report (Brutalist)
**Runtime:** ~3:10 (190.22s measured) · 13 beats
**Narrator:** Onyx (`am_onyx`) · Register: Pragmatist
**Channel chip / handle on cut:** `@HumanitariansAI`
**Subject:** `D:/Projects/mycroft` @ commit `4157a8e`
**Deliverable (local):** `Mycroft_UdaySonawane_09_25_2026.mp4`

**Episode 5 of the Mycroft weekly.**

| Episode | Commit | Video |
|---|---|---|
| 1 | `9ef4e7f` | [Build the Defects First](../2026-08-27-weekly-fixtures-before-validators/) |
| 2 | `bdc1bc1` | [Transport, Do Not Repair](../2026-09-03-mycroft-weekly-transport-do-not-repair/) |
| 3 | `253ee74` | [Both Sets Scored 64](../2026-09-10-mycroft-weekly-both-sets-scored-64/) |
| 4 | `aa0c0fe` | [It Never Says Pass](../2026-09-17-mycroft-weekly-it-never-says-pass/) |
| 5 | `4157a8e` | **this one** |

## What this video is about

Episode 4 closed by asking the viewer what makes their own green indicators go
red. This episode runs that question **on the repository itself**.

Two gates could be satisfied by doing nothing — each passed if its artifact
existed **or** if a `[TODO: DEV]` marker was still present. Both conditions were
true, so both gates were green for the wrong reason.

**The framework (B02) — three questions for any automated check:**

1. What does it actually read?
2. What would make it fail?
3. Has that failure ever been demonstrated?

Both gates are scored on those three. The new gate 5 is **break-tested across
three cases**, so its failure path is shown rather than asserted.

The falsifiability beat (B09) is the part the commit is honest about: gate 5 is
deliberately **not** cleared, because no live or model call has run and writing
that clearance would be a false one.

## Package contents

| File | Role |
|---|---|
| `beat_sheet.json` | Narrative + visual plan; carries `source_repo` / `source_commit` |
| `README.md` | This file |
| `FACTCHECK.md` | Claim-level verdicts |
| `CHECKS-REPORT.md` | PROOF gate, with the teaching arc |
| `SHOTLIST.md` | Per-beat shot plan |
| `PROMPTS.md` | Reproducible prompts used to build the video |
| `scenes.py` | Authored Manim scenes |
| `layout_audit.md` / `.json` | Frame-level layout audit |

Not tracked here (gitignored, local only): `clips/`, `media/`, `manim/`,
`pantry/`, `_qc/`, `mp3/` (now excluded repo-wide), `qc-sheet.png`, and the masters.

**Two files are absent** that earlier episodes in this series carry:

- **No `SOURCES.md`.** Derivations live in `FACTCHECK.md` instead, as with episode 4.
- **No `BUILD-LOG.md`.** For the earlier episodes this doubled as the video's own
  frictional log. The frictional log for the underlying engineering work is at
  [`../frictional-logs/2026-09-25-recipe-promotion-and-gate-fixes.md`](../frictional-logs/2026-09-25-recipe-promotion-and-gate-fixes.md).

## Provenance warning

Like the earlier episodes, this video lives **outside** the repository it
documents, so the subject commit is not implied by folder location.
`beat_sheet.json` (`source_repo`, `source_commit` = `4157a8e`) is the only link.

**As of this writing, `4157a8e` has not been merged into `nikbearbrown/mycroft`** —
the most recent merged pull request is [#48](https://github.com/nikbearbrown/mycroft/pull/48)
(2026-09-18, episode 4). This episode's subject work is not yet upstream.

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
