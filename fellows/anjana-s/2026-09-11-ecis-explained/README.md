# ECIS Episode 6 — From Reading to Predicting

**Skill:** ai-explainer · **Voice:** af_bella (Anjana) · **Duration:** ~258s (16:9) / ~170s (9:16 short) · **Status:** rendered (both orientations, final cut + slate)
**Series:** Sequel to ECIS Episodes 1–5.
**Destination:** `anjana-s/2026-09-11-ecis-explained`
**Delivery:** rendered at 4K in both 16:9 and 9:16.

## About this video

For five episodes ECIS only ever looked backward — a transcript came in, a graded signal went out. Episode 6 asks what the accumulated history is worth on its own. The answer is that the signal log the system has been building since Episode 1 already contains everything needed to predict next quarter's guidance direction before the earnings call happens: what direction a company reported last time, how many consecutive quarters it has raised, whether the stock has already moved, what its peers are saying, how long since its last call, and how confident the system was before. Six features, all computed from data the system already had. No new sources, no new APIs. A logistic regression turns them into a prediction — deliberately a simple model, because the sophistication is in the features.

The prediction then inherits the same honesty rule that has governed every extraction: it is logged before the call, with the full feature vector, the model version, and a timestamp, and it cannot be revised, softened, or deleted afterward. The video makes the waiting legible — a locked gold prediction record, a dotted timeline, days ticking past toward the call — and only then does the blue actual-result card land beside it.

That produces two scorecards asking two different questions. Level one grades the prediction against the extraction: did the model correctly forecast what the company would say? Level two grades the extraction against the market: did the guidance predict the stock? The episode's insight is that these are independent — a prediction can be right about the words and wrong about the money, and the video shows exactly that case, green on top and red below. It closes on the dashboard's new forecast view: three companies with upcoming calls, their predicted direction and confidence, the feature that drove each prediction, whether it agrees with the sector, and a track record with one open, unfilled dot still waiting on its call.

## File structure

```
ecis-ep6/
├── README.md, PEDAGOGY.md   — build notes and sign-off
├── script.md, beat_sheet.json, beats.json — narration script and beat config
├── narration/, visuals/     — per-beat TTS text and visual briefs
├── mp3/, clips/, media/     — narration audio and rendered per-beat video (16:9)
├── ecis-ep6-slate.mp4       — 16:9 review cut
├── ecis-ep6.mp4             — 16:9 final master (3840×2160)
└── short/                   — 9:16 derivative cut (via runtime/scripts/shorts.py)
    ├── PEDAGOGY.md           — sign-off for the derivative cut
    ├── beat_sheet.json       — aspect_ratio 9:16, beats dropped to fit the Shorts cap
    ├── mp3/, media/          — regenerated outro audio + portrait Remotion renders
    ├── ecis-ep6-short-slate.mp4 — 9:16 review cut
    └── ecis-ep6-short.mp4    — 9:16 final master (2160×3840)
```

Six body-beat illustrations (`Ecis6Intro`, `Ecis6Features`, `Ecis6Preregistered`,
`Ecis6TwoLevels`, `Ecis6Forecast`, `Ecis6Close`) plus their portrait `916`
counterparts are registered in `runtime/remotion/src/Root.tsx`, under
`runtime/remotion/src/illustrations/ecis-ep6/`. Gold (`#D4A853`) is this
episode's prediction color and appears nowhere on the extraction side.

## Rebuilding this video

```bash
cd brutalist.art

# 16:9 (4K, 3840×2160)
python3 runtime/scripts/generate_audio_kokoro.py anjana-s/2026-09-11-ecis-explained
python3 runtime/scripts/remotion_scenes.py anjana-s/2026-09-11-ecis-explained
./art final anjana-s/2026-09-11-ecis-explained

# 9:16 derivative (4K vertical, 2160×3840)
python3 runtime/scripts/shorts.py anjana-s/2026-09-11-ecis-explained --handle ""
python3 runtime/scripts/generate_audio_kokoro.py anjana-s/2026-09-11-ecis-explained/short
python3 runtime/scripts/remotion_scenes.py anjana-s/2026-09-11-ecis-explained/short
./art final anjana-s/2026-09-11-ecis-explained/short --height 3840
```

GATE P is signed for both the parent (`PEDAGOGY.md` — `VERDICT: PASS`) and
the short derivative (`short/PEDAGOGY.md` — `VERDICT: PASS`).
