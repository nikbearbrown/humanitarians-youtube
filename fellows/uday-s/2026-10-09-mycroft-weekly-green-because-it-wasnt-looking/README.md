# Green Because It Wasn't Looking

**Fellow:** Uday Sonawane
**Date:** 2026-10-09
**Format:** `cli-explainer` spine, applied as a weekly work report (Brutalist)
**Runtime:** ~3:38 (217.74s measured) · 12 beats
**Narrator:** Onyx (`am_onyx`) · Register: Pragmatist
**Channel chip / handle on cut:** `@HumanitariansAI`
**Subject:** `D:/Projects/mycroft` @ commit `fbd30b6`, branch `fix/conformance-skip-list`
**Deliverable (local):** `Mycroft_UdaySonawane_10_09_2026.mp4`

**Episode 7 of the Mycroft weekly.**

| Episode | Commit | Video |
|---|---|---|
| 1 | `9ef4e7f` | [Build the Defects First](../2026-08-27-weekly-fixtures-before-validators/) |
| 2 | `bdc1bc1` | [Transport, Do Not Repair](../2026-09-03-mycroft-weekly-transport-do-not-repair/) |
| 3 | `253ee74` | [Both Sets Scored 64](../2026-09-10-mycroft-weekly-both-sets-scored-64/) |
| 4 | `aa0c0fe` | [It Never Says Pass](../2026-09-17-mycroft-weekly-it-never-says-pass/) |
| 5 | `4157a8e` | [Passing For The Wrong Reason](../2026-09-25-mycroft-weekly-passing-for-the-wrong-reason/) |
| 6 | `8c13b87` | [The Status Is A Claim](../2026-10-02-mycroft-weekly-the-status-is-a-claim/) |
| 7 | `fbd30b6` | **this one** |

## What this video is about

Episode 6 listed ten things the attestation had not tested. This episode takes
the first of them: a conformance checker that was passing because of what it
never opened.

**The framework (B02) — three questions for any automated check that is green:**

1. What did it actually open?
2. Why was anything excluded?
3. Has it ever been shown to fail?

The numbers are the argument. The old skip rule meant the checker opened **187
files**. The corrected rule opens **743** — revealing **476 Python files** and
99 recipes that had never been inspected.

The fix was not simply deleting the skip entries. B05 shows the `SKIP` /
`SKIP_PREFIXES` split that was needed, and B06 records what deleting them alone
would have cost: the run became eleven times slower.

B07 answers question three — five things were broken on purpose to confirm the
checker now fails when it should. B08 turns episode 6's own rule back on this
work.

## Sourcing

Every figure is re-derived rather than quoted from a commit message — the before
and after file counts come from replaying each skip rule against the repository
at the relevant commit, and `SOURCES.md` records the exact command for each.

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
| `layout_audit_frames/*.png` | Sampled audit stills |

Not tracked here (gitignored, local only): `clips/`, `media/`, `manim/`,
`pantry/`, `_qc/`, `mp3/`, `qc-sheet.png`, and the masters.

**No `BUILD-LOG.md`**, as with recent episodes. The frictional logs for the
underlying engineering work are
[`../frictional-logs/2026-10-09-conformance-skip-list.md`](../frictional-logs/2026-10-09-conformance-skip-list.md)
and
[`../frictional-logs/2026-10-09-gitattributes-and-manifest-drift.md`](../frictional-logs/2026-10-09-gitattributes-and-manifest-drift.md).

## Provenance warning

This video lives **outside** the repository it documents, so the subject commit
is not implied by folder location. `beat_sheet.json` (`source_repo`,
`source_commit` = `fbd30b6`) is the only link. The subject is a **feature
branch** (`fix/conformance-skip-list`), so that reference could be rebased or
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
