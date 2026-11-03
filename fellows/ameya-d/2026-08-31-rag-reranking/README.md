# RAG: Reranking

*RAG series* · Humanitarians AI Fellows · Ameya Deshmukh · @HumanitariansAI
Persona: Liam, in for Ameya (Kokoro `am_onyx`).

> First-stage search is fast because the query and the document never met — which
> is exactly why the ranking is loose. A cross-encoder reads them together and
> reranks a shortlist, never the whole corpus.

## Master
`RAGReranking_AmeyaDeshmukh_2026-08-31.mp4` — 3840×2160, 11 beats, zero slates.
Review cut with beat labels: `…-slate.mp4`.

## What the episode does
A single-subtopic episode in the RAG series. It shows why a fast first search still
needs a careful second pass, then takes the reranker apart: the bi- vs cross-encoder
distinction, the pair→score→sort mechanism, the two-stage "retrieve wide, rerank narrow"
shape, the real `rerank.py`, the honest latency cost, and when to reach for it (or skip it).

## Files
| File | What it is |
|---|---|
| `beat_sheet.json` | The reel. Everything else derives from it. |
| `scenes.py` | Manim data-viz scenes (B01–B04, B06–B07), audio-conformed via `TARGET`. |
| `PEDAGOGY.md` | GATE P — narration/structure review (VERDICT: PASS). |
| `FACTCHECK.md` | 13 claims audited against the repo. |
| `SOURCES.md` | Every figure traced to `fin-disclosure-rag`. |
| `PROOF.md` | Self-assessment against the weekly requirements. |
| `BUILD-PROMPT.md` | Paste-ready rebuild prompt. |
| `_qc/` | Frame-level visual QC (contact sheet + REPORT). |

Real code shown: `../../rerank.py` (B05, verbatim). Latency figures: `../../benchmark.py`.

## Rebuild (free, local)
```
python3 runtime/scripts/generate_audio_kokoro.py <this dir>   # Kokoro am_onyx
# set scenes.py TARGET{} to measured durations; render Manim 4K -> manim/<BID>.mp4
python3 runtime/scripts/remotion_scenes.py <this dir>          # Claude beats -> media/<BID>.mp4
python3 runtime/scripts/compile.py <this dir> --height 2160
python3 runtime/qc/final_frame_check.py <this dir> --lenient
```
