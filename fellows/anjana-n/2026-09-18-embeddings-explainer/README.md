# What Embeddings Actually Store

**Skill:** ai-explainer · **Voice:** af_bella (Anjana) · **Duration:** ~150s (16:9) / ~154s (9:16) · **Status:** rendered (both orientations, final cut + slate)
**Standalone:** not part of the ECIS series. Adjacent to `transformer-layer` (what a layer does) and `attention-finance` (how tokens look at each other) — this one is about what a token *is* before either of those happens.
**Destination:** `anjana-s/2026-09-18-embeddings-explainer`
**Delivery:** rendered at 4K in both 16:9 (`embeddings-explainer.mp4`, 3840×2160) and 9:16 (`short/embeddings-explainer-short.mp4`, 2160×3840).

## About this video

Everyone says a language model turns words into numbers. Almost nobody says
which numbers, where they come from, or why they end up where they do. This
video opens the table.

It starts with the lookup: before a model does anything else, every token in
its vocabulary is exchanged for a row in an embedding matrix. Those values are
not written by anyone — they are initialized randomly and shaped by training,
and the video shows exactly that, with a sweep that leaves structure where
there was noise.

Then the part that makes embeddings worth caring about: position carries
meaning. Words that mean similar things end up as near neighbours, not because
a dictionary said so but because they turned up in similar company across
billions of sentences. The video measures it twice in the same frame — a short
gold line inside a cluster marked "similar", a long one across the whole space
marked "distant".

And then the twist that separates a static embedding from what a transformer
actually does: the same token does not keep the same vector. "Bank" beside
"river" and "bank" beside "earnings" take two visibly different routes through
the layers and land in two different neighbourhoods. By the final layer the
vector no longer represents a word — it represents that word in that sentence.

## File structure

```
embeddings-explainer/
├── README.md, PEDAGOGY.md   — build notes and sign-off
├── script.md, beat_sheet.json, beats.json — narration script and beat config
├── narration/, visuals/     — per-beat TTS text and visual briefs
├── mp3/, clips/, media/     — narration audio and rendered per-beat video (16:9)
├── embeddings-explainer-slate.mp4 — 16:9 review cut
├── embeddings-explainer.mp4       — 16:9 final master (3840×2160)
└── short/                   — 9:16 version (via runtime/scripts/shorts.py)
    ├── PEDAGOGY.md           — sign-off for the derivative cut
    ├── beat_sheet.json       — aspect_ratio 9:16; NO beats dropped (under the cap)
    ├── media/                — portrait Remotion renders + the 4K endcard
    ├── embeddings-explainer-short-slate.mp4 — 9:16 review cut
    └── embeddings-explainer-short.mp4       — 9:16 final master (2160×3840)
```

## Rebuilding this video

```bash
cd brutalist.art

# 16:9 (4K, 3840×2160)
python3 runtime/scripts/generate_audio_kokoro.py anjana-s/2026-09-18-embeddings-explainer
python3 runtime/scripts/remotion_scenes.py anjana-s/2026-09-18-embeddings-explainer
./art final anjana-s/2026-09-18-embeddings-explainer

# 9:16 (4K vertical, 2160×3840) — full reformat, nothing cut
python3 runtime/scripts/shorts.py anjana-s/2026-09-18-embeddings-explainer --handle "" --no-outro-rewrite
python3 runtime/scripts/remotion_scenes.py anjana-s/2026-09-18-embeddings-explainer/short
./art final anjana-s/2026-09-18-embeddings-explainer/short --height 3840
```
