# What Vector Databases Do That SQL Cannot

**Skill:** ai-explainer · **Voice:** af_bella (Anjana) · **Duration:** ~171s (16:9) / ~175s (9:16) · **Status:** rendered (both orientations, final cut + slate)
**Standalone:** sibling to `embeddings-explainer`. That one is about what a vector *is*; this one is about what you do with a few million of them.
**Destination:** `anjana-s/2026-09-25-vector-db-explainer`
**Delivery:** rendered at 4K in both 16:9 (`vector-db-explainer.mp4`, 3840×2160) and 9:16 (`short/vector-db-explainer-short.mp4`, 2160×3840).

## About this video

A SQL database answers exact questions: which rows match this condition. The
video opens by trying to write the other kind of question and failing — a
second query types itself out and stops dead where the operator should be,
`WHERE ??? similar to this`. There isn't one. That's the hook, and it's
animated rather than asserted.

What follows is the three things a vector database does instead. It stores
records as embeddings, so meaning becomes *position* — similar records land near
each other, and the video draws that as two clusters with a measured distance
between them. It answers a query by taking a point rather than a predicate, and
returns everything ranked by proximity; the losing cluster stays visible and dim
on screen, because nothing was excluded, it just ranked low. And it stays fast
by refusing to be exact: instead of a million distance calculations it walks a
graph of near neighbours, entering anywhere and hopping closer until nothing
improves.

That last part is worth knowing about the build: the graph and the walk are
real. The neighbour graph is generated from a deterministic point cloud, the
hops are an actual greedy search over it, and the comparison count on screen is
summed from the walk itself rather than typed in. If the path takes a slightly
awkward route, that's the algorithm.

## File structure

```
vector-db-explainer/
├── README.md, PEDAGOGY.md   — build notes and sign-off
├── script.md, beat_sheet.json, beats.json — narration script and beat config
├── narration/, visuals/     — per-beat TTS text and visual briefs
├── mp3/, clips/, media/     — narration audio and rendered per-beat video (16:9)
├── vector-db-explainer-slate.mp4 — 16:9 review cut
├── vector-db-explainer.mp4       — 16:9 final master (3840×2160)
└── short/                   — 9:16 version (via runtime/scripts/shorts.py)
    ├── PEDAGOGY.md           — sign-off for the derivative cut
    ├── beat_sheet.json       — aspect_ratio 9:16; NO beats dropped (under the cap)
    ├── media/                — portrait renders + the 4K endcard
    ├── vector-db-explainer-short-slate.mp4 — 9:16 review cut
    └── vector-db-explainer-short.mp4       — 9:16 final master (2160×3840)
```

## Rebuilding this video

```bash
cd brutalist.art

# 16:9 (4K, 3840×2160)
python3 runtime/scripts/generate_audio_kokoro.py anjana-s/2026-09-25-vector-db-explainer
python3 runtime/scripts/remotion_scenes.py anjana-s/2026-09-25-vector-db-explainer
./art final anjana-s/2026-09-25-vector-db-explainer

# 9:16 (4K vertical, 2160×3840) — full reformat, nothing cut
python3 runtime/scripts/shorts.py anjana-s/2026-09-25-vector-db-explainer --handle "" --no-outro-rewrite
python3 runtime/scripts/remotion_scenes.py anjana-s/2026-09-25-vector-db-explainer/short
./art final anjana-s/2026-09-25-vector-db-explainer/short --height 3840
```

GATE P is signed for both the parent (`PEDAGOGY.md` — `VERDICT: PASS`) and the
9:16 cut (`short/PEDAGOGY.md` — `VERDICT: PASS`).
