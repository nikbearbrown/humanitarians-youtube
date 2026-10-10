# ECIS Episode 10 — The Business Layer

## Series
ECIS Weekly Update (Episode 10)

## Summary
Episode 10 covers Phase 15 (Week 15): the business analytics layer that transforms raw NLP signals into actionable sector-level intelligence. New capabilities include sector sentiment aggregation with a mood index, cross-sector heatmap benchmarking, management confidence scoring, CEO-vs-CFO tone divergence detection, guidance language tracking, signal-to-price correlation ranking, surprise score analytics (NLP vs consensus vs actual), and multi-horizon reaction window curves. The system now answers "which sectors are shifting," "which executives are hedging," and "which signals actually move prices."

## Destination and delivery

**Destination:** `anjana-n/2026-10-09-ecis-explained`
**Delivery:** rendered at 4K in both 16:9 (`ecis-ep10.mp4`, 3840×2160) and 9:16
(`short/ecis-ep10-short.mp4`, 2160×3840).

## File structure

```
ecis-ep10/
├── README.md, PEDAGOGY.md   — build notes and sign-off
├── script.md                — the authored body beats (B01–B06)
├── beat_sheet.json, beats.json — beat config
├── narration/, visuals/     — per-beat TTS text and visual briefs
├── mp3/, clips/, media/     — narration audio and rendered per-beat video (16:9)
├── ecis-ep10-slate.mp4      — 16:9 review cut
├── ecis-ep10.mp4            — 16:9 final master (3840×2160)
└── short/                   — 9:16 derivative cut (via runtime/scripts/shorts.py)
    ├── PEDAGOGY.md          — sign-off for the derivative cut
    ├── beat_sheet.json      — aspect_ratio 9:16, beats dropped to fit the Shorts cap
    ├── mp3/, media/         — regenerated outro audio + portrait renders + 4K endcard
    ├── ecis-ep10-short-slate.mp4 — 9:16 review cut
    └── ecis-ep10-short.mp4    — 9:16 final master (2160×3840)
```

## Rebuilding this video

```bash
cd brutalist.art

# 16:9 (4K, 3840×2160)
python3 runtime/scripts/generate_audio_kokoro.py anjana-n/2026-10-09-ecis-explained
python3 runtime/scripts/remotion_scenes.py anjana-n/2026-10-09-ecis-explained
./art final anjana-n/2026-10-09-ecis-explained

# 9:16 derivative (4K vertical, 2160×3840)
python3 runtime/scripts/shorts.py anjana-n/2026-10-09-ecis-explained --drop B01 B05 B08 --handle ""
python3 runtime/scripts/generate_audio_kokoro.py anjana-n/2026-10-09-ecis-explained/short
python3 runtime/scripts/remotion_scenes.py anjana-n/2026-10-09-ecis-explained/short
./art final anjana-n/2026-10-09-ecis-explained/short --height 3840
```
