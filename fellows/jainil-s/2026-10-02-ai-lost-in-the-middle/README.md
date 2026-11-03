# Lost in the Middle

**Where a fact sits inside a long context changes how reliably it gets used — the middle is the weakest position.**

Built 2026-10-02 · track `ai — educational (STEM / AI)` · channel @HumanitariansAI

## Deliverables

| Cut | Aspect | Resolution | Runtime |
|---|---|---|---|
| Master | 16:9 | 3840×2160 | 2:19.2 |
| Short | 9:16 | 2160×3840 | 2:19.2 |

Video files are **not** in this repo — they are delivered separately.

## Beats

| # | Act | Composition | Duration |
|---|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` | 18.56s |
| B01 | BLUF | `BrutalistHesitantWriter` | 15.77s |
| B02 | SETUP | `FormACard` | 17.28s |
| B03 | HERO | `PositionCurve` | 17.64s |
| B04 | EVIDENCE | `FormACard` | 18.82s |
| B05 | LAND | `WantQuote` | 8.11s |
| B06 | FIX | `FormACard` | 29.65s |
| B07 | HANDOFF | `ClaudeComposerAsk` | 10.5s |
| B08 | OUTRO | `HaiTitleOutro` | 2.86s |

The Short is a derived cut: the same 9 beats re-laid-out portrait via
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
| `qc/` | GATE V evidence. Both cuts: **BLOCKER 0, MAJOR 0**. |

Shared documents are stored once, not duplicated per cut.

## Honesty notes

The central finding is quoted **verbatim** from Liu et al., *Lost in the
Middle: How Language Models Use Long Contexts* (TACL 2024), including the
qualifier that makes it matter: "even for explicitly long-context models".

**No per-model percentage is claimed.** Those figures are specific to the
models and context lengths tested and quoting them as current would
misrepresent them. The U-curve shown on screen carries a caption saying it
is an illustration of the published shape, not measured values.

## Reproducing

```bash
source .tools/env.sh
python3 runtime/scripts/generate_audio_kokoro.py <reel>
./art run   <reel>          # review cut
./art final <reel>          # 4K master
./art shorts <reel>         # derive the 9:16 cut
```
