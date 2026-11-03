# ECIS Episode 9: Proving It Works

Weekly update video for the ECIS (Earnings Call Intelligence Signals) series.
Episode 9 extends the system with statistical rigor (bootstrap confidence
intervals, permutation tests, power analysis), end-to-end data quality
tracking (profiling, lineage, completeness monitoring), concept drift detection,
and real-time Grafana monitoring dashboards with threshold alerting.

## Destination and delivery

**Destination:** `anjana-n/2026-10-02-ecis-explained`
**Delivery:** rendered at 4K in both 16:9 (`ecis-ep9.mp4`, 3840×2160) and 9:16
(`short/ecis-ep9-short.mp4`, 2160×3840).

## File structure

```
ecis-ep9/
├── README.md, PEDAGOGY.md   — build notes and sign-off
├── script.md                — the authored body beats (B01–B06)
├── beat_sheet.json, beats.json — beat config
├── narration/, visuals/     — per-beat TTS text and visual briefs
├── mp3/, clips/, media/     — narration audio and rendered per-beat video (16:9)
├── ecis-ep9-slate.mp4       — 16:9 review cut
├── ecis-ep9.mp4             — 16:9 final master (3840×2160)
└── short/                   — 9:16 derivative cut (via runtime/scripts/shorts.py)
    ├── PEDAGOGY.md           — sign-off for the derivative cut
    ├── beat_sheet.json       — aspect_ratio 9:16, beats dropped to fit the Shorts cap
    ├── mp3/, media/          — regenerated outro audio + portrait renders + 4K endcard
    ├── ecis-ep9-short-slate.mp4 — 9:16 review cut
    └── ecis-ep9-short.mp4    — 9:16 final master (2160×3840)
```

## Rebuilding this video

```bash
cd brutalist.art

# 16:9 (4K, 3840×2160)
python3 runtime/scripts/generate_audio_kokoro.py anjana-n/2026-10-02-ecis-explained
python3 runtime/scripts/remotion_scenes.py anjana-n/2026-10-02-ecis-explained
./art final anjana-n/2026-10-02-ecis-explained

# 9:16 derivative (4K vertical, 2160×3840)
python3 runtime/scripts/shorts.py anjana-n/2026-10-02-ecis-explained --drop B01 B05 B08 --handle ""
python3 runtime/scripts/generate_audio_kokoro.py anjana-n/2026-10-02-ecis-explained/short
python3 runtime/scripts/remotion_scenes.py anjana-n/2026-10-02-ecis-explained/short
./art final anjana-n/2026-10-02-ecis-explained/short --height 3840
```

GATE P is signed for both the parent (`PEDAGOGY.md` — `VERDICT: PASS`) and the
short derivative (`short/PEDAGOGY.md` — `VERDICT: PASS`).
