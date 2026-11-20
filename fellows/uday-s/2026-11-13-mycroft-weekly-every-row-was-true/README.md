# Every Row Was True

**Fellow:** Uday Sonawane
**Date:** 2026-11-13
**Format:** `cli-explainer` spine, applied as a weekly work report (Brutalist)
**Runtime:** ~3:49 (228.93s measured) · 12 beats
**Narrator:** Onyx (`am_onyx`) · Register: Pragmatist
**Channel chip / handle on cut:** `@HumanitariansAI`
**Subject:** `D:/Projects/mycroft` @ commit `b425b19`, branch `chore/map-covers-repo`
**Deliverable (local):** `Mycroft_UdaySonawane_11_13_2026.mp4`

**Episode 12 of the Mycroft weekly.**

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
| 12 | `b425b19` | **this one** |

## What this video is about

The thing worth sitting with: **nothing in the map was false.** Every row was
accurate — and the map was still partial, which is a different failure and a
harder one to notice.

**The framework (B02) — three questions for any index, map or manifest:**

1. Does it say what it covers?
2. What is outside the default path?
3. Would you notice if something were missing?

Ten subsystems, **1,005 files**, and **none of the ten sat inside
`DEFAULT_PATHS`** — so the checker never looked at them. Eight scoped
`CLAUDE.md` files below the root were in the same position.

Pointing the checker at those trees turned up a second problem: three
Kubernetes manifests are multi-document YAML, and `yaml.safe_load` reads only
the first document where `safe_load_all` reads all of them. B08 recounts
everything rather than trusting the new numbers, and B09 closes on one more
thing that was wrong — the file path itself.

## Sourcing

Single-source video from `mycroft` at `b425b19`, no web sources. Each of the ten
subsystem counts comes from its own `git ls-tree -r` invocation, and the 1,005
total is their sum — recorded in [`SOURCES.md`](./SOURCES.md). The multi-document
YAML finding was verified by counting `---` separators (7, 8 and 10), not
inferred.

## Package contents

| File | Role |
|---|---|
| `beat_sheet.json` | Narrative + visual plan; carries `source_repo` / `source_commit` |
| `README.md` | This file |
| `SOURCES.md` | Every figure and the command that produced it |
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
[`../frictional-logs/2026-11-13-map-covers-repo.md`](../frictional-logs/2026-11-13-map-covers-repo.md).

## Provenance warning

This video lives **outside** the repository it documents, so the subject commit
is not implied by folder location. `beat_sheet.json` (`source_repo`,
`source_commit` = `b425b19`) is the only link. The subject is a **feature
branch** (`chore/map-covers-repo`), so that reference could be rebased or
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
