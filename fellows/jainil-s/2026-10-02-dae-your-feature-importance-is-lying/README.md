# Your Feature Importance Is Lying

**Importance scores measure what a model would miss, not what matters — so duplicating a signal hides it, and enough copies invert the ranking.**

Built 2026-10-02 · track `dae — independent research (ML interpretability)` · channel @HumanitariansAI

## Deliverables

| Cut | Aspect | Resolution | Runtime |
|---|---|---|---|
| Master | 16:9 | 3840×2160 | 2:25.9 |
| Short | 9:16 | 2160×3840 | 2:25.9 |

Video files are **not** in this repo — they are delivered separately.

## Beats

| # | Act | Composition | Duration |
|---|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` | 15.62s |
| B01 | BLUF | `BrutalistHesitantWriter` | 15.17s |
| B02 | SETUP | `BarChart` | 13.29s |
| B03 | TURN | `BarChart` | 20.46s |
| B04 | HERO | `BarChart` | 16.85s |
| B05 | EVIDENCE | `FormACard` | 17.92s |
| B06 | LAND | `WantQuote` | 11.43s |
| B07 | FIX | `FormACard` | 19.14s |
| B08 | HANDOFF | `ClaudeComposerAsk` | 12.27s |
| B09 | OUTRO | `HaiTitleOutro` | 3.8s |

The Short is a derived cut: the same 10 beats re-laid-out portrait via
`<Pattern>916` compositions, never a centre-crop. No beats were dropped, so one
`SCRIPT.md` covers both.

## Files

| File | What it is |
|---|---|
| `beat_sheet.json` | The master (16:9). Narration, scenes, props, measured durations. |
| `beat_sheet.short.json` | The Short (9:16). Differs only in the `916` composition names. |
| `SCRIPT.md` | Narration as delivered. Covers both cuts. |
| `FACTCHECK.md` | One row per claim: verdict + derivation or source. |
| `SOURCES.md` | Every source used, and what was deliberately **not** used. |
| `SHOTLIST.md` · `PROMPTS.md` | The typed work order. |
| `STATUS.md` · `ToDo.md` | Build ledger. |
| `FRICTIONAL.md` | Dated record of the process — what was tried, where it resisted, what was accepted or rejected. |
| `importance_evidence.py` | Reproduces every figure in the reel. Primary evidence, not a citation. |
| `qc/` | GATE V evidence. Both cuts: **BLOCKER 0, MAJOR 0**. |

Shared documents are stored once, not duplicated per cut.

## Honesty notes

Two independent sources. scikit-learn documents the failure in its own
`permutation_importance` page, quoted verbatim. And `importance_evidence.py`
in this folder reproduces every number on screen from scratch, in numpy,
with a fixed seed.

**A correction is on the record in `FACTCHECK.md`.** The reel was first
pitched on the claim that both copies report ~zero importance. The
experiment does not show that: two copies each score 0.58 against a true
1.68, and the correct feature still ranks first. It takes **three** copies
to invert a ranking, and three is what the reel says.

## Reproducing

```bash
source .tools/env.sh
python3 runtime/scripts/generate_audio_kokoro.py <reel>
./art run   <reel>          # review cut
./art final <reel>          # 4K master
./art shorts <reel>         # derive the 9:16 cut
```
