# What a Context Window Really Is

## Summary
Demystifies the context window — the fixed-size memory every LLM reads from on each generation step. Covers tokenization's role in sizing, the KV cache that makes it work, why quadratic attention cost matters, and why a 128K-token window doesn't mean 128K tokens of perfect recall. Ends with practical strategies: chunking, summarization, and RAG as workarounds.

## Destination and delivery

**Destination:** `anjana-n/2026-10-02-context-window-explainer`
**Delivery:** rendered at 4K in both 16:9 and 9:16(`context-window-explainer.mp4`).

## File structure

```
context-window-explainer/
├── README.md, PEDAGOGY.md   — build notes and sign-off
├── script.md                — the authored body beats (B01–B05)
├── beat_sheet.json, beats.json — beat config
├── narration/, visuals/     — per-beat TTS text and visual briefs
├── mp3/, clips/, media/     — narration audio and rendered per-beat video (16:9)
├── context-window-explainer-slate.mp4 — 16:9 review cut
├── context-window-explainer.mp4       — 16:9 final master (3840×2160)
└── short/                   — 9:16 cut (via runtime/scripts/shorts.py)
    ├── PEDAGOGY.md, beat_sheet.json — sign-off and 9:16 beat config
    ├── mp3/, media/          — regenerated outro audio + portrait renders + 4K endcard
    ├── context-window-explainer-short-slate.mp4 — 9:16 review cut
    └── context-window-explainer-short.mp4       — 9:16 final master (2160×3840)
```

## Rebuilding this video

```bash
cd brutalist.art

# 16:9 (4K, 3840×2160)
python3 runtime/scripts/generate_audio_kokoro.py anjana-s/2026-10-02-context-window-explainer
python3 runtime/scripts/remotion_scenes.py anjana-s/2026-10-02-context-window-explainer
./art final anjana-s/2026-10-02-context-window-explainer

# 9:16 (4K vertical, 2160×3840)
python3 runtime/scripts/shorts.py anjana-s/2026-10-02-context-window-explainer --drop B07 --handle ""
python3 runtime/scripts/generate_audio_kokoro.py anjana-s/2026-10-02-context-window-explainer/short
python3 runtime/scripts/remotion_scenes.py anjana-s/2026-10-02-context-window-explainer/short
./art final anjana-s/2026-10-02-context-window-explainer/short --height 3840
```

GATE P is signed for both the parent (`PEDAGOGY.md` — `VERDICT: PASS`) and the
9:16 cut (`short/PEDAGOGY.md` — `VERDICT: PASS`).
