# MiniRAG: The Index Does the Thinking

A Brutalist research explainer on **MiniRAG** (Fan, Wang, Ren & Huang,
University of Hong Kong — arXiv:2501.06713v3, 26 Jan 2025).

**16 beats · 4:37 · 3840×2160 · Kokoro `am_onyx` (Liam, in for Bear) · $0.00**

## The claim the film argues

Retrieval-augmented generation was built on an unstated assumption: a large
language model sits behind every stage — indexing, retrieval, generation. Swap in
a small model and LightRAG falls from 56.90% to 35.42% accuracy, while GraphRAG
stops producing usable output entirely.

MiniRAG moves the reasoning out of the model and into a heterogeneous graph
index, so a 1.5–4B model on a phone only has to do the two things small models
are good at: extract entities, and write the final sentence.

**The ablation carries the claim.** Replace that index with ordinary
description-based indexing and accuracy collapses from 53.29% to 26.02% — roughly
half the system's performance lives in the index, not the model.

The reel also states a cost the paper does not discuss: on multi-hop questions
MiniRAG's error rate is 28.44% against LightRAG's 11.78%. It answers far more
questions correctly, and is confidently wrong more often too. That trade-off is
beat B11; both figures are the paper's own (Table 1).

## Versions

Rendered media is not committed here, per the repo convention. Both cuts live in
the shared Drive folder:

**→ [Brutalist_Neelabh_Bhardwaj (Google Drive)](https://drive.google.com/drive/folders/13ruU7k_DWiiXbQcCb_ks7h-g5P3VDTBi)**

| Version | File | Notes |
|---|---|---|
| **v2 — final** | `claude-liam-minirag.mp4` | 3840×2160, 4:37. Clean master, no review burn-in. Channel handle `@NeelabhBhardwaj`. **This is the upload master.** |
| v1 — first review cut | `claude-liam-minirag-slate.mp4` | Superseded. Carries the `B0x GRAPHIC VIDEO` review burn-in and the earlier `@NikBearBrown` handle. |

The Drive folder also holds the YouTube title and description document.

## What's in this folder

| File | What it is |
|---|---|
| `beat_sheet.json` | **The authoritative source.** All 16 beats: narration, `show` blocks, scene + props, measured audio durations. |
| `FACTCHECK.md` | 25 claims, each traced to a specific table or section of the paper. |
| `SOURCES.md` | Citation, plus three claims from the paper's own abstract dropped as unsupported by its own Table 1. |
| `PROMPTS.md` | Every prompt that appears on screen, verbatim, plus the generation prompts behind each custom scene. |
| `SHOTLIST.md` | Beat → component mapping, and the GATE L library-search findings. |
| `PEDAGOGY.md` | Why the beats are ordered this way; what was deliberately left out. |
| `CHECKS-REPORT.md` | Pre-build gate record — 16 SHOW / 0 PUNT, teaching-arc checklist. |
| `BUILD-PROMPT.md` | How to rebuild end to end, including the per-beat edit loop. |
| `MiniRag.tsx` | Build asset: the six reel-local Remotion scenes. No component hardcodes a statistic — every figure arrives as a prop from the beat sheet, so a wrong number is a beat-sheet fix. |
| `FRICTIONAL.md` | Process log. |

## Rebuilding

Full instructions in `BUILD-PROMPT.md`. In short, from a `brutalist.art` checkout
with its venv active:

```bash
python3 runtime/scripts/generate_audio_kokoro.py <reel>   # audio is the master clock
./art run   <reel>                                        # review cut
./art final <reel> --out <reel>                           # clean 4K master
```

`MiniRag.tsx` must be placed at `runtime/remotion/src/` and registered in
`Root.tsx` under a `MiniRag` folder, then `./art scene-index` re-run.

To change one beat without rebuilding the film:

```bash
python3 runtime/scripts/generate_audio_kokoro.py <reel> --only B05
rm <reel>/media/B05.mp4 && ./art run <reel>
```

Never hand-time anything — if a beat runs long, cut words and regenerate. The
measured MP3 is the only clock.

## Source

Fan, T., Wang, J., Ren, X., & Huang, C. (2025). *MiniRAG: Towards Extremely
Simple Retrieval-Augmented Generation.* University of Hong Kong.
arXiv:2501.06713v3 — <https://arxiv.org/abs/2501.06713>
Code: <https://github.com/HKUDS/MiniRAG>

Every figure on screen is redrawn from the paper's own tables. No screenshots
were lifted.
