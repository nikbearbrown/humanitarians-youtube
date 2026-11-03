# ECIS Episode 7 — The Bigger Picture

**Skill:** ai-explainer · **Voice:** af_bella (Anjana) · **Duration:** ~203s (16:9) / ~153s (9:16 short) · **Status:** rendered (both orientations, final cut + slate)
**Series:** Sequel to ECIS Episodes 1–6 — the system stops looking at one company at a time.
**Destination:** `anjana-s/2026-09-18-ecis-explained`
**Delivery:** rendered at 4K in both 16:9 (`ecis-ep7.mp4`, 3840×2160) and 9:16 (`short/ecis-ep7-short.mp4`, 2160×3840).

## About this video

Six episodes in, ECIS could read an earnings transcript through four independent readers, triangulate them into a confidence-scored signal, pre-register that signal, predict the next quarter, and grade itself against the market. Every one of those judgments looked at a single company in isolation. Episode 7 is where the system starts looking sideways, and it does so in four places.

First, consensus. A raise means something different depending on what analysts already expected. The system now pulls the consensus estimate for each company and quarter and computes the delta between the extracted guidance and that estimate — and the delta becomes a feature in the Episode 6 prediction model. Second, surprise. The further a signal lands from consensus, the higher its surprise score, and the counter-intuitive consequence is that high-surprise signals are assigned *lower* confidence: the things nobody saw coming are exactly the things the system is worst at predicting, and it now says so rather than pretending otherwise.

Third, correlation. Pairwise correlations across every tracked company surface clusters that move together, and inside a cluster, the company that reliably raises a quarter before its peers — a leading indicator, which is the part of this episode that could actually be traded on. Fourth, the benchmark. Grading moved from a broad-market index to a sector-specific one, and the video shows the same +5% return graded twice: an outperform against a market that rose 2%, a miss against a sector that rose 8%. The company's number never changes. Only the benchmark does.

## File structure

```
ecis-ep7/
├── README.md, PEDAGOGY.md   — build notes and sign-off
├── script.md, beat_sheet.json, beats.json — narration script and beat config
├── narration/, visuals/     — per-beat TTS text and visual briefs
├── mp3/, clips/, media/     — narration audio and rendered per-beat video (16:9)
├── ecis-ep7-slate.mp4       — 16:9 review cut
├── ecis-ep7.mp4             — 16:9 final master (3840×2160)
└── short/                   — 9:16 derivative cut (via runtime/scripts/shorts.py)
    ├── PEDAGOGY.md           — sign-off for the derivative cut
    ├── beat_sheet.json       — aspect_ratio 9:16, B01 and B08 dropped to fit the Shorts cap
    ├── mp3/, media/          — regenerated outro audio + portrait Remotion renders
    ├── ecis-ep7-short-slate.mp4 — 9:16 review cut
    └── ecis-ep7-short.mp4    — 9:16 final master (2160×3840)
```

## Rebuilding this video

```bash
cd brutalist.art

# 16:9 (4K, 3840×2160)
python3 runtime/scripts/generate_audio_kokoro.py anjana-s/2026-09-18-ecis-explained
python3 runtime/scripts/remotion_scenes.py anjana-s/2026-09-18-ecis-explained
./art final anjana-s/2026-09-18-ecis-explained

# 9:16 derivative (4K vertical, 2160×3840)
python3 runtime/scripts/shorts.py anjana-s/2026-09-18-ecis-explained --drop B01 B08 --handle ""
python3 runtime/scripts/generate_audio_kokoro.py anjana-s/2026-09-18-ecis-explained/short
python3 runtime/scripts/remotion_scenes.py anjana-s/2026-09-18-ecis-explained/short
./art final anjana-s/2026-09-18-ecis-explained/short --height 3840
```
