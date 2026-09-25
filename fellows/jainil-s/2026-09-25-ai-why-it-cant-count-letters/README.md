# Why It Can't Count Letters

**A model cannot count the letters in a word because it never receives letters — text is split into tokens first, and tokens are not letters.**

Built 2026-09-25 · track `ai — educational (STEM / AI)` · channel @HumanitariansAI

## Deliverables

| Cut | Aspect | Resolution | Runtime |
|---|---|---|---|
| Master | 16:9 | 3840×2160 | 2:20.0 |
| Short | 9:16 | 2160×3840 | 2:20.0 |

Video files are **not** in this repo — they are delivered separately.
Everything here is the source of record for how they were built.

## Beats

| # | Act | Composition | Duration |
|---|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` | 12.69s |
| B01 | BLUF | `BrutalistHesitantWriter` | 16.47s |
| B02 | HERO | `TokenSplit` | 17.62s |
| B03 | TURN | `TokenSplit` | 13.53s |
| B04 | EVIDENCE | `FormACard` | 31.33s |
| B05 | LAND | `WantQuote` | 11.29s |
| B06 | FIX | `FormACard` | 21.06s |
| B07 | HANDOFF | `ClaudeComposerAsk` | 12.67s |
| B08 | OUTRO | `HaiTitleOutro` | 3.33s |

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
| `tokenize_evidence.py` | Reproduces every tokenisation figure in the reel. Primary evidence, not a citation. |
| `qc/` | GATE V evidence — reports and frames. Both cuts: **BLOCKER 0, MAJOR 0**. |

`FACTCHECK.md`, `SOURCES.md`, `SHOTLIST.md` and `PROMPTS.md` apply to both cuts
and are stored once rather than duplicated per cut.

## Honesty notes

Central evidence is **primary and reproducible**, not cited. Every token split
shown on screen is real GPT-2 BPE output, produced by `tokenize_evidence.py`
in this folder. Run it and you get the same numbers.

The reel states on screen that the tokenizer is GPT-2 and that every model has
its own vocabulary — the mechanism is general, the specific splits are not.

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
