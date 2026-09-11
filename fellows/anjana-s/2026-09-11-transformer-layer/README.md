# What Happens Inside a Transformer Layer

**Skill:** ai-explainer · **Voice:** af_bella (Anjana) · **Duration:** ~224s (16:9) / ~170s (9:16 short) · **Status:** rendered (both orientations, final cut + slate)
**Companion to:** `examples/attention-finance` — that video covers *why* attention beats left-to-right reading; this one is the level below: what one layer does to one token, with attention as one of four steps.
**Destination:** `anjana-s/2026-09-11-inside-a-transformer-layer`
**Delivery:** rendered at 4K in both 16:9 and 9:16.

## About this video

A transformer model can have dozens of layers, but every layer does the same four things in the same order — and the video's whole method is to open one of them like a cross-section and follow a single token through. The token is "revenue," from the sentence "We expect revenue growth to moderate."

Self-attention comes first. The token creates three vectors from itself — a query, a key, and a value — and its query asks every other token in the sentence how much it matters. The scores come back as a distribution that sums to one: "growth" and "moderate" score high because they directly shape what "revenue" means here; "we" and "to" score near zero. The weighted sum of everyone's values flows back into "revenue," and the word has not changed, but it now knows what surrounds it. The feed-forward network comes second and never looks sideways: it expands the vector to four times its width, passes it through an activation that switches some features on and others off, and compresses it back. Attention gathers context; feed-forward processes it.

The other two operations are the unglamorous ones, and they are the reason the first two can be stacked. Residual connections save the original input before each block and add it back afterward, so a layer that learns nothing useful does no damage — the token passes through unchanged. Layer norm rescales the values after each addition so they stay in a stable range instead of drifting higher with every layer until the model breaks. The video ends by closing the cross-section and rejoining the stack: twelve of these is BERT, ninety-six is GPT, and it is the same four steps every time.

## File structure

```
transformer-layer/
├── README.md, PEDAGOGY.md   — build notes and sign-off
├── script.md, beat_sheet.json, beats.json — narration script and beat config
├── narration/, visuals/     — per-beat TTS text and visual briefs
├── mp3/, clips/, media/     — narration audio and rendered per-beat video (16:9)
├── transformer-layer-slate.mp4 — 16:9 review cut
├── transformer-layer.mp4    — 16:9 final master (3840×2160)
└── short/                   — 9:16 derivative cut (via runtime/scripts/shorts.py)
    ├── PEDAGOGY.md           — sign-off for the derivative cut
    ├── beat_sheet.json       — aspect_ratio 9:16, beats dropped to fit the Shorts cap
    ├── mp3/, media/          — regenerated outro audio + portrait Remotion renders
    ├── transformer-layer-short-slate.mp4 — 9:16 review cut
    └── transformer-layer-short.mp4       — 9:16 final master (2160×3840)
```

Five body-beat illustrations (`TransformerHook`, `TransformerAttention`,
`TransformerFeedForward`, `TransformerGlue`, `TransformerClose`) plus their
portrait `916` counterparts are registered in `runtime/remotion/src/Root.tsx`,
under `runtime/remotion/src/illustrations/transformer-layer/`. Q is gold, K is
blue, V is green, the token is terracotta, and the feed-forward strip is purple
— none of those are reused for anything else.

Two simplifications are deliberate and logged in `PEDAGOGY.md`: attention is
shown single-head, and layer norm is placed after the add (the original
Vaswani arrangement) rather than before each block as most modern models do.

## Rebuilding this video

```bash
cd brutalist.art

# 16:9 (4K, 3840×2160)
python3 runtime/scripts/generate_audio_kokoro.py anjana-s/2026-09-11-inside-a-transformer-layer
python3 runtime/scripts/remotion_scenes.py anjana-s/2026-09-11-inside-a-transformer-layer
./art final anjana-s/2026-09-11-inside-a-transformer-layer

# 9:16 derivative (4K vertical, 2160×3840)
python3 runtime/scripts/shorts.py anjana-s/2026-09-11-inside-a-transformer-layer --handle ""
python3 runtime/scripts/generate_audio_kokoro.py anjana-s/2026-09-11-inside-a-transformer-layer/short
python3 runtime/scripts/remotion_scenes.py anjana-s/2026-09-11-inside-a-transformer-layer/short
./art final anjana-s/2026-09-11-inside-a-transformer-layer/short --height 3840
```

GATE P is signed for both the parent (`PEDAGOGY.md` — `VERDICT: PASS`) and
the short derivative (`short/PEDAGOGY.md` — `VERDICT: PASS`).
