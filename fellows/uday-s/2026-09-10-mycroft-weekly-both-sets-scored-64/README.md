# Both Sets Scored 64

**Fellow:** Uday Sonawane
**Date:** 2026-09-10
**Format:** `cli-explainer` spine, applied as a weekly work report (Brutalist)
**Runtime:** ~3:34 (214.28s measured) · 13 beats
**Master:** 1920×1080; assets are 4K (Manim 2160p24, Remotion `--scale=2`), so `./art final` yields a true 4K master with no re-render
**Narrator:** Onyx (`am_onyx`) · Register: Pragmatist
**Channel chip / handle on cut:** `@HumanitariansAI`
**Subject:** `D:/Projects/mycroft` @ commit `253ee74`
**Deliverable (local):** `BothSetsScored64_UdaySonawane_2026-09-10.mp4`

**Episode 3 of the Mycroft weekly.** Previous: `bdc1bc1` (ep 2) · `9ef4e7f` (ep 1).

| Episode | Commit | Reel |
|---|---|---|
| 1 | `9ef4e7f` | [Build the Defects First](../2026-08-27-weekly-fixtures-before-validators/) |
| 2 | `bdc1bc1` | [Transport, Do Not Repair](../2026-09-03-mycroft-weekly-transport-do-not-repair/) |
| 3 | `253ee74` | **this one** |

## What this video is about

Episode 2's lesson was *"ask what the code refuses to do."* That would not have
found this one. The centrepiece came from running steps 4 and 5 on **both**
fixture sets and diffing the outputs rather than the logs:

```
clean set      overall_score 64      3 flags
defective set  overall_score 64      8 flags
```

The corrupted set — 5 duplicates removed, 6 rows rejected, 6 quality flags —
**reports the same headline number as the clean one.** The arithmetic cannot
tell them apart; only the flag list can. That is the entire argument for step
5's "loud substitutions" rule, demonstrated rather than asserted.

**The framework (B02, on screen at 21.85s — ahead of step 4 at 49.18s) — three
questions to ask of any number a pipeline hands you:**

1. **MEASURED OR SUBSTITUTED** — is this a real measurement, or a default?
2. **DOES THE OUTPUT SAY** — does the artifact itself tell you which?
3. **CAN YOU WALK IT BACK** — can you trace the number to its inputs?

Steps 4 and 5 are both scored on those three (B05, B08).

The falsifiability beat (B09) is predicted by question 1 and lands **right back
on episode 1**: the frozen corpus reaches only **5 of the 10** catalogue flags —
and the 5 it misses are exactly the substitution paths. The series' own earlier
work is the limiting case.

## Precision over a better line

The two scores are **not identical** — the unrounded values are **63.75 and
64.0**. "Identical" would have been the stronger sentence and a small
fabrication. The narration says *"the same headline number"*, never "identical",
and the on-screen figure is the reported `overall_score`, which is what both
runs emit.

The distinction matters because the beat's whole point is that the *reported*
number cannot distinguish clean data from corrupted data. See
[`FACTCHECK.md`](./FACTCHECK.md) row 10, graded `PASS-WITH-PRECISION`.

## Package contents

| File | Role |
|---|---|
| `beat_sheet.json` | Narrative + visual plan; carries `source_repo` / `source_commit` |
| `README.md` | This file |
| `SOURCES.md` | Every on-screen figure, re-derived from a live run, plus "Not claimed" |
| `FACTCHECK.md` | Claim-level verdicts, incl. the 63.75/64.0 precision note |
| `CHECKS-REPORT.md` | PROOF gate: 13 SHOW / 0 HOLD / 0 PUNT, with the teaching arc |
| `BUILD-LOG.md` | How the episode was found, the precision decision, gate record |
| `SHOTLIST.md` | Per-beat shot plan |
| `PROMPTS.md` | Reproducible prompts, incl. the reusable "run it twice and diff" move |
| `scenes.py` | Authored Manim scenes for the six data beats |
| `layout_audit.md` / `.json` | Frame-level layout audit |
| `mp3/timings.json` | Measured per-beat narration durations (the clock) |

Not tracked here (gitignored, local only): `clips/`, `media/`, `manim/`,
`pantry/`, `_qc/`, `mp3/*.mp3`, `qc-sheet.png`, and the masters.

## Provenance warning

Like episodes 1 and 2, this reel lives **outside** the repo it documents, so the
subject commit is not implied by folder location. `beat_sheet.json`
(`source_repo`, `source_commit` = `253ee74`) and `SOURCES.md` are the only link
between this reel and what it describes. Keep them accurate or the chain breaks.

## Gate record

```
GATE L   searched before authoring; no reusable hit; 6 beats authored as Manim
GATE F   full paperwork set written up front (learned from the last reel, where
         it failed on a missing SHOTLIST)
GATE A   clean on all six, first pass
GATE W   clean on all six, first pass
GATE B   pixel-true — 0 errors, 0 warnings, FIRST PASS, no re-renders
GATE V   clean cut: 429 frames, BLOCKER 0, MAJOR 63 (58 underfill · 5 low-contrast)
```

**Four reels in, the layout helpers have converged** — kicker at `buff=0.72`,
content-adaptive box widths, `fit_src()` reserving the citation strip, every
label composed *into* the fitted group, `_fit()` scaling up as well as down, and
never a line drawn through text. Each cost a re-render to learn on an earlier
reel and cost nothing here.

## Known accepted deviations

- **63 MAJOR** on the clean cut (58 underfill · 5 low-contrast) — underfill is
  13.5% of sampled frames, build-in ramps plus the sparse outro card. The
  low-contrast flags all co-occur with 10–11% fill readings: near-blank frames
  at beat openings, not unreadable content. Documented, not silenced with
  `ART_STRICT=0`.
- The `26 BLOCKER` headline from `./art run` is GATE V reading `*-slate.mp4`,
  the review cut, whose timecode burn-in sits outside title-safe by construction.
- **No `PROOF-REVIEW.md`.** The PROOF self-assessment lives as a table inside
  `BUILD-LOG.md`, as with the 2026-09-03 packages.

## Toolkit (rebuild)

```bash
git clone https://github.com/nikbearbrown/brutalist.art.git
cd brutalist.art
./setup --install
./setup
```

Repo: https://github.com/nikbearbrown/brutalist.art

Audio-first, Kokoro-only, no API keys. Regenerate narration first, then let the
measured durations drive the scenes — timing is never fixed by hand.

## Publishing

Not authorized by this package. The master stays local until a human decides to
share or upload.
