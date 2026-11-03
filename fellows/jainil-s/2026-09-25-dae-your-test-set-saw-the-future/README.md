# Your Test Set Saw the Future

**A random train/test split on time-ordered data lets the model train on the future and be tested on the past — the score is inflated and nothing warns you.**

Built 2026-09-25 · track `dae — independent research (ML evaluation)` · channel @HumanitariansAI

## Deliverables

| Cut | Aspect | Resolution | Runtime |
|---|---|---|---|
| Master | 16:9 | 3840×2160 | 2:18.2 |
| Short | 9:16 | 2160×3840 | 2:18.2 |

Video files are **not** in this repo — they are delivered separately.
Everything here is the source of record for how they were built.

## Beats

| # | Act | Composition | Duration |
|---|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` | 11.88s |
| B01 | BLUF | `BrutalistHesitantWriter` | 15.79s |
| B02 | HERO | `TimelineSplit` | 15.55s |
| B03 | EVIDENCE | `FormACard` | 18.52s |
| B04 | FIX | `TimelineSplit` | 14.59s |
| B05 | LAND | `WantQuote` | 12.16s |
| B06 | BODY | `FormACard` | 31.27s |
| B07 | HANDOFF | `ClaudeComposerAsk` | 14.81s |
| B08 | OUTRO | `HaiTitleOutro` | 3.63s |

The Short is a derived cut: the same 9 beats re-laid-out portrait via
`<Pattern>916` compositions — never a centre-crop. No beats were dropped, so the
narration is identical and a single `SCRIPT.md` covers both.

## Files

| File | What it is |
|---|---|
| `beat_sheet.json` | The master (16:9). Source of truth: narration, scenes, props, measured durations. |
| `beat_sheet.short.json` | The Short (9:16). Differs only in the `916` composition names. |
| `SCRIPT.md` | Narration as delivered, with measured durations. Covers both cuts. |
| `FACTCHECK.md` | One row per claim: verdict + derivation or source. |
| `SOURCES.md` | Every source used, and what was deliberately **not** used. |
| `SHOTLIST.md` | Typed work order — what must be on screen in each beat. |
| `PROMPTS.md` | Beat-prefixed prompts for open slots (none here). |
| `STATUS.md` / `ToDo.md` | Build ledger. |
| `qc/` | GATE V evidence — reports and frames. Both cuts: **BLOCKER 0, MAJOR 0**. |

`FACTCHECK.md`, `SOURCES.md`, `SHOTLIST.md` and `PROMPTS.md` apply to both cuts
and are stored once rather than duplicated per cut.

## Honesty notes

Every claim traces to scikit-learn’s own `TimeSeriesSplit` documentation,
quoted verbatim in `SOURCES.md`. The strongest evidence that the standard tool
is wrong for this data is the standard library saying so itself.

**No magnitude of accuracy inflation is claimed.** Blog posts quote dramatic
figures; they are dataset-specific and untraceable, so the reel argues
direction and mechanism only.

## Reproducing

Requires the `brutalist.art` toolkit. Narration is generated first and its
measured durations are the master clock; visuals conform to audio, never the
reverse.

```bash
source .tools/env.sh
python3 runtime/scripts/generate_audio_kokoro.py <reel>
./art run   <reel>          # review cut
./art final <reel>          # 4K master
./art shorts <reel>         # derive the 9:16 cut
```
