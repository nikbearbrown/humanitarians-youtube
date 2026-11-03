# It Never Says Pass

**Fellow:** Uday Sonawane
**Date:** 2026-09-17
**Format:** `cli-explainer` spine, applied as a weekly work report (Brutalist)
**Runtime:** ~3:33 (213.29s measured) · 13 beats
**Master:** **3840×2160 @ 24fps, true 4K** (~14 MB), verified by `ffprobe` and a 1:1 crop
**Narrator:** Onyx (`am_onyx`) · Register: Pragmatist
**Channel chip / handle on cut:** `@HumanitariansAI`
**Subject:** `D:/Projects/mycroft` @ `aa0c0fe`, branch `feature/market-sentiment-human-report`
**Deliverable (local):** `Mycroft_UdaySonawane_09_17_2026.mp4`

**Episode 4 — the six-step arc closes.**

| Episode | Commit | Reel |
|---|---|---|
| 1 | `9ef4e7f` | [Build the Defects First](../2026-08-27-weekly-fixtures-before-validators/) |
| 2 | `bdc1bc1` | [Transport, Do Not Repair](../2026-09-03-mycroft-weekly-transport-do-not-repair/) |
| 3 | `253ee74` | [Both Sets Scored 64](../2026-09-10-mycroft-weekly-both-sets-scored-64/) |
| 4 | `aa0c0fe` | **this one — finale** |

Episode 1 opened on six steps marked `[TODO: DEV]` with nothing behind them.
This one closes the ledger: **six of six steps written.**

## What this video is about

Each episode needed a different question. Ep 2's was *"ask what the code refuses
to do"*; ep 3's was *"run it twice and diff the outputs"*. This one needed a
third: **what does this step refuse to *conclude*, and where does it say so?**

That surfaced the line the episode is named for —

> An audit reports what it found; it never says "pass".

— and one level down, the gate-4 note where the report **criticises one of its
own gates in writing.**

Three of the four episode titles came from a docstring. **Read the comments
before the diff.**

**The framework (B02, on screen at 24.08s — ahead of step 6 at 50.26s) — three
questions for any automated report:**

1. **WHAT A RECORD SUPPORTS** — which claims are verified by an artifact?
2. **WHAT YOU INFERRED** — which are the report's own inference?
3. **WHO DECIDES** — who is accountable for acting on it?

Step 6 is scored on all three. The defective set splits **10 verified / 5
inferred** — and episode 3's headline `64` lands under *inferred*, which
demotes the previous episode's centrepiece on camera.

## The falsifiability beat, and the callback

B09 is predicted by question 3 and lands directly on episode 1. **Gate 4 is
satisfiable by doing nothing** — quoted verbatim from the live run:

> This gate as written is satisfiable by doing nothing: it passes if the script
> exists OR if the `[TODO: DEV]` text is still in the recipe. Both are currently
> true.

Episode 1's thesis was that a validator with nothing to catch is not passing.
This is the same defect one level up: **a gate with nothing to fail.**

All six gates report *"evidence recorded; awaiting a named human"* — `cleared_by:
null`, `cleared_at: null`. Nothing self-approves.

## Precision over a better line

`FACTCHECK.md` is **13 rows PASS, 1 PASS-WITH-PRECISION**. Row 10: the commit
says "16/16 log fields", which is correct *for the contract*. A **write** run
reports 17 — the extra is `artifact_hashes`, which only exists once files are
written. The contract requires 16, and the reel says 16.

Every figure was re-derived from a live run; the commit message was treated as a
claim to check, not a source.

## Package contents

| File | Role |
|---|---|
| `beat_sheet.json` | Narrative + visual plan; carries `source_repo` / `source_commit` |
| `README.md` | This file |
| `FACTCHECK.md` | GATE F signed; 15 rows, every figure re-derived from a live run |
| `CHECKS-REPORT.md` | PROOF gate: 13 SHOW / 0 HOLD / 0 PUNT, with the teaching arc |
| `BUILD-LOG.md` | How the episode was found, gate record, the 4K step |
| `SHOTLIST.md` | Per-beat shot plan |
| `PROMPTS.md` | Reproducible prompts, incl. the third question |
| `scenes.py` | Authored Manim scenes for the six data beats |
| `layout_audit.md` / `.json` | Frame-level layout audit |
| `mp3/timings.json` | Measured per-beat narration durations (the clock) |

Not tracked here (gitignored, local only): `clips/`, `media/`, `manim/`,
`pantry/`, `_qc/`, `mp3/*.mp3`, `qc-sheet.png`, and the masters.

**No `SOURCES.md` in this package**, unlike episodes 2 and 3. The derivation of
every on-screen figure lives in `FACTCHECK.md`'s own Derivation column instead.

## Provenance warning

Like the earlier episodes, this reel lives **outside** the repo it documents, so
the subject commit is not implied by folder location. `beat_sheet.json`
(`source_repo`, `source_commit` = `aa0c0fe`) is the only link between this reel
and what it describes — and note the subject is a **feature branch**
(`feature/market-sentiment-human-report`), not a default-branch commit, so it
may be rebased or squashed later. Keep the reference accurate or the chain
breaks.

## Gate record

```
GATE L   searched before authoring; no reusable hit; 6 beats authored as Manim
GATE F   full paperwork set written up front
GATE A   clean on all six, FIRST PASS
GATE W   clean on all six, FIRST PASS
GATE B   pixel-true — 0 errors, 0 warnings, FIRST PASS, no re-renders
GATE V   slate pass 26 BLOCKER (the review burn-in) + 2 MAJOR
```

**Six reels in, the layout helpers have fully converged** — each cost a
re-render to learn on an earlier reel; this reel needed none.

## Known accepted deviations

- The `26 BLOCKER` from GATE V is the `*-slate.mp4` review cut's timecode
  burn-in, outside title-safe by construction. **No clean-cut GATE V frame count
  is recorded** in `BUILD-LOG.md`, unlike the 2026-08-27 and earlier 2026-09
  reels which all logged `BLOCKER 0` against the clean cut explicitly.
- **No `PROOF-REVIEW.md`.** The PROOF self-assessment lives as a table inside
  `BUILD-LOG.md`.
- `BUILD-LOG.md` records that the 4K step was interrupted repeatedly by a
  session-level classifier blocking shell execution; the compile itself
  succeeded and verification was completed afterwards.

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
