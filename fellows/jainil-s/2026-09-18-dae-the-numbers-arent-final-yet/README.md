# The Numbers Aren't Final Yet

**A metric is a draft that keeps being revised; comparing a fresh number to a settled one measures the settling, not performance.**

Built 2026-09-18 · track `dae — independent research (data analytics engineering)` · channel @HumanitariansAI

## Deliverables

| Cut | Aspect | Resolution | Runtime |
|---|---|---|---|
| Master | 16:9 | 3840×2160 | 2:06.8 |
| Short | 9:16 | 2160×3840 | 2:06.8 |

Video files are **not** in this repo — they are delivered separately.
Everything here is the source of record for how they were built.

## Beats

| # | Act | Composition | Duration |
|---|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` | 11.58s |
| B01 | BLUF | `BrutalistHesitantWriter` | 13.4s |
| B02 | EVIDENCE | `FormACard` | 16.85s |
| B03 | HERO | `SettlingBar` | 16.9s |
| B04 | TURN | `BarChart` | 19.14s |
| B05 | LAND | `WantQuote` | 12.52s |
| B06 | FIX | `FormACard` | 20.18s |
| B07 | HANDOFF | `ClaudeComposerAsk` | 12.84s |
| B08 | OUTRO | `HaiTitleOutro` | 3.35s |

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
| `PROMPTS.md` | Beat-prefixed prompts for open slots (none here; all beats render from registered compositions). |
| `STATUS.md` / `ToDo.md` | Build ledger. |
| `qc/` | GATE V evidence — see below. |

`FACTCHECK.md`, `SOURCES.md`, `SHOTLIST.md` and `PROMPTS.md` apply to both cuts
and are stored once rather than duplicated per cut.

## QC evidence

| File | What it is |
|---|---|
| `qc/gate-v-report.md` · `.short.md` | GATE V results. Both: **BLOCKER 0, MAJOR 0**. |
| `qc/contact-sheet.png` · `.short.png` | Frames sampled from the finished mp4 — what GATE V actually graded. |
| `qc/qc-sheet.png` · `.short.png` | One frame per beat from the clips before assembly — the storyboard view. |

## Honesty notes

Every platform-behaviour claim traces to a verbatim quote from YouTube Help
(8 rows in `SOURCES.md`). The four-reading settling chart is labelled on screen as an
illustration — direction is documented, magnitude is not claimed. Per-metric delay
tables circulating on SEO blogs are deliberately excluded as unsourceable.

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
