# The RAG System I Built

*Weekly work report* · Humanitarians AI Fellows · Ameya Deshmukh · @HumanitariansAI
Persona: Liam, in for Ameya (Kokoro `am_onyx`).

> Bigger is not better; hit rate saturates while MRR keeps discriminating; and
> vector search is a rounding error in your latency budget. Measure before you optimise.

## Master
`Mycroft_AmeyaDeshmukh_2026-08-31.mp4` — 3840×2160, 12 beats, zero slates.
Review cut with beat labels: `…-slate.mp4`.

## What the episode does
A walkthrough of the production RAG system I built over a synthetic corpus of 600
financial disclosures, measured end to end. It covers the task and golden set, the
pipeline, and three levers with real numbers — chunking (MRR 0.833 → 1.000),
embedding-model choice (a 384-dim model beat a 768-dim one), and hybrid search
(MRR 0.655 → 0.810). Then the latency reality (vector search is ~0.2%), the real
`hybrid.py` fusion code, and the three surprises worth keeping.

## Files
| File | What it is |
|---|---|
| `beat_sheet.json` | The reel. Everything else derives from it. |
| `scenes.py` | Manim data-viz scenes (B01–B06, B08), audio-conformed via `TARGET`. |
| `PEDAGOGY.md` | GATE P — narration/structure review (VERDICT: PASS). |
| `FACTCHECK.md` | 14 claims audited against the repo. |
| `SOURCES.md` | Every figure traced to a script in `fin-disclosure-rag`. |
| `PROOF.md` | Self-assessment against the weekly requirements. |
| `BUILD-PROMPT.md` | Paste-ready rebuild prompt. |
| `_qc/` | Frame-level visual QC (contact sheet + REPORT). |

Real code shown: `../../hybrid.py` (B07, verbatim RRF fusion). Numbers:
`../../run_eval.py`, `../../compare_embeddings.py`, `../../weight_sweep.py`, `../../benchmark.py`.

## Rebuild (free, local)
```
python3 runtime/scripts/generate_audio_kokoro.py <this dir>   # Kokoro am_onyx
# set scenes.py TARGET{} to measured durations; render Manim 4K -> manim/<BID>.mp4
python3 runtime/scripts/remotion_scenes.py <this dir>          # Claude beats -> media/<BID>.mp4
python3 runtime/scripts/compile.py <this dir> --height 2160
python3 runtime/qc/final_frame_check.py <this dir> --lenient
```
