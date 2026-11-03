# Transport, Do Not Repair

**Fellow:** Uday Sonawane
**Date:** 2026-09-03
**Format:** `cli-explainer` spine, applied as a weekly work report (Brutalist)
**Runtime:** ~3:22 (202.16s measured) · 13 beats
**Master:** 1920×1080; assets are 4K (Manim 2160p24, Remotion `--scale=2`), so `./art final` yields a true 4K master with no re-render
**Narrator:** Onyx (`am_onyx`) · Register: Pragmatist
**Channel chip / handle on cut:** `@HumanitariansAI`
**Subject:** `D:/Projects/mycroft` @ commit `bdc1bc1`
**Deliverable (local):** `TransportDoNotRepair_UdaySonawane_2026-09-03.mp4`

**Episode 2 of the Mycroft weekly.** Built deliberately as a sequel to
[2026-08-27 — Build the Defects First](../2026-08-27-weekly-fixtures-before-validators/),
whose ledger closed on *"run-envelope absent · gate 2 cannot clear"*. B01 opens
on that same list and resolves two rows of it, and B10 restates the ledger in
the same shape. The ledger is the series' through-line.

## What this video is about

The commit message describes *what changed*. The strongest material was what it
did not summarise — the ingest script's own load-bearing rule:

> An ingest script that cleans data destroys the evidence that cleaning was needed.

That line gave the episode its title, its thesis, and axis 2 of the framework.

**The framework (B02, on screen at 20.16s — ahead of the first example at 47.10s)
— three questions for any pipeline stage:**

1. **DECIDES** — what does this stage judge?
2. **REFUSES** — what does it deliberately *not* do?
3. **EVIDENCE** — what does it leave behind that a later run can check?

Both steps are then scored on the same three axes (B05, B08) — **opposite jobs,
one rubric.** Step 2 (ingest) decides nothing about content and refuses to
repair anything. Step 3 does judge: clean set → nothing found, exit zero;
defective set → the defects surface.

The falsifiability beat (B09) is axis 3 broken in practice: **evidence that
moves with the platform is not evidence.**

## The honesty correction, recorded not quietly fixed

The first draft of B09 put **invented hash prefixes** on screen as stand-ins for
"two different digests". That is an invented figure, which the REBUILD LAW
forbids outright. It was replaced with the real ones — the actual file's bytes
hashed under each line ending:

```
sample/clean/news-finnhub.json
  LF    3,180 bytes   sha256 441291ec…
  CRLF  3,261 bytes   sha256 42fdf8fc…
```

Both honest and a better beat, because a viewer can reproduce it.

Also corrected: the commit message says step 3 catches "3 parse errors". That is
a rollup — the manifest's taxonomy for those three is 2 `malformed_row` plus 1
`unparseable_file`. The script's `parse_errors` field does return 3, so the
on-screen label is the script's own term and correct; the narration avoids
restating it as a defect count. See [`BUILD-LOG.md`](./BUILD-LOG.md).

## Package contents

| File | Role |
|---|---|
| `beat_sheet.json` | Narrative + visual plan; carries `source_repo` / `source_commit` |
| `README.md` | This file |
| `SOURCES.md` | Every on-screen figure and how it was re-derived |
| `FACTCHECK.md` | Claim-level verdicts |
| `CHECKS-REPORT.md` | PROOF gate: 13 SHOW / 0 HOLD / 0 PUNT, with the teaching arc |
| `BUILD-LOG.md` | Where the episode came from, continuity, the honesty correction, gate record |
| `SHOTLIST.md` | Per-beat shot plan |
| `PROMPTS.md` | Reproducible prompts, plus next week's lesson |
| `scenes.py` | Authored Manim scenes for the six data beats |
| `layout_audit.md` / `.json` | Frame-level layout audit |
| `mp3/timings.json` | Measured per-beat narration durations (the clock) |

Not tracked here (gitignored, local only): `clips/`, `media/`, `manim/`,
`pantry/`, `_qc/`, `mp3/*.mp3`, `qc-sheet.png`, and the masters.

## Provenance warning

Like episode 1, this reel lives **outside** the repo it documents, so the
subject commit is not implied by folder location. `beat_sheet.json`
(`source_repo`, `source_commit` = `bdc1bc1`) and `SOURCES.md` are the only link
between this reel and what it describes. Keep them accurate or the chain breaks.

## Gate record

```
GATE L   library-first searched; no reusable hit; six beats authored as Manim
GATE F   paperwork set written before render
GATE A   one fix: B05 was pure typography with no shape to change. Given the
         geometry its content implies (bordered scorecard cells per row)
GATE W   clean on all six, first pass
GATE B   pixel-true — 0 errors, 0 warnings, FIRST PASS
GATE V   clean cut: 404 frames, BLOCKER 0, MAJOR 39 (35 underfill · 4 low-contrast)
```

**GATE B passed first pass**, which is the payoff from the previous two reels:
the layout helpers carried over (kicker `buff=0.72`, content-adaptive box
widths, `fit_src()` reserving the citation strip, never a line drawn through
text) cost three re-renders to learn and zero here.

Underfill is down to **8.7%** of sampled frames, from ~14% on episode 1.

## Known accepted deviations

- **39 MAJOR** on the clean cut (35 underfill · 4 low-contrast) — build-in ramps
  plus the sparse outro card; the low-contrast flags all co-occur with 10–11%
  fill readings, i.e. near-blank beat openings with too little ink to measure a
  luminance separation. Accepted and documented, not silenced with `ART_STRICT=0`.
- The `26 BLOCKER` headline from `./art run` is GATE V reading `*-slate.mp4`, the
  review cut, whose timecode burn-in sits outside title-safe by construction.
  Against the clean cut there are none.
- **Friction scored weakest again** — a work report mostly delivers. `BUILD-LOG.md`
  points at `PROOF-REVIEW.md` for the detail, but **that file is not in this
  package**; the PROOF table in `BUILD-LOG.md` is what exists.

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
