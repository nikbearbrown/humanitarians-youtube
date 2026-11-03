# ECIS Episode 8 — Reading Between the Lines

**Skill:** ai-explainer · **Voice:** af_bella (Anjana) · **Duration:** ~212s (16:9) / ~150s (9:16 short) · **Status:** rendered (both orientations, final cut + slate)
**Series:** Sequel to ECIS Episodes 1–7 — the system turns back to the transcript and reads the delivery.
**Destination:** `anjana-s/2026-09-25-ecis-explained`
**Delivery:** rendered at 4K in both 16:9 (`ecis-ep8.mp4`, 3840×2160) and 9:16 (`short/ecis-ep8-short.mp4`, 2160×3840).

## About this video

For seven episodes ECIS read what management *said* — four readers, a triangulator, a pre-registered signal, graded against the market, weighed against consensus and the sector. Episode 8 turns back to the same transcript and reads how they said it.

Three instruments do that. A readability scorer tracks whether language complexity spikes before guidance changes. A hedging index measures cautious phrases against definitive ones. A tone shift detector compares sentiment distributions across consecutive quarters. All three become features in the prediction model, alongside the numbers — because when the way a company talks changes, something usually changes in the numbers too.

Then the episode makes outcomes stop being binary. A correct signal is not always a useful one: the system now measures how far the stock actually moved after the call, when that move accumulated, and whether volume spiked enough to say traders treated the guidance as material news. A signal followed by twelve percent counts for more than one followed by half a percent.

And then the uncomfortable question. If the stock already climbed five percent in the same direction in the ten trading days *before* the call, the market may have already known. The system measures that pre-signal drift, and the video shows the case plainly — the price line already rising inside the shaded pre-call window, the verdict sitting underneath: correct, but already priced in. The beat stops there, at the diagnosis, because that is where the source stops.

The last body beat is the one about plumbing: the data layer outgrew SQLite and moved to PostgreSQL, with a TimescaleDB hypertable for market series and materialized views for the dashboard. A system quietly outgrowing its database is a real thing that happens to real projects, and the episode is more honest for showing it.

## File structure

```
ecis-ep8/
├── README.md, PEDAGOGY.md   — build notes and sign-off
├── script.md, beat_sheet.json, beats.json — narration script and beat config
├── narration/, visuals/     — per-beat TTS text and visual briefs
├── mp3/, clips/, media/     — narration audio and rendered per-beat video (16:9)
├── ecis-ep8-slate.mp4       — 16:9 review cut
├── ecis-ep8.mp4             — 16:9 final master (3840×2160)
└── short/                   — 9:16 derivative cut (via runtime/scripts/shorts.py)
    ├── PEDAGOGY.md           — sign-off for the derivative cut
    ├── beat_sheet.json       — aspect_ratio 9:16; B01, B05 and B08 dropped for the cap
    ├── mp3/, media/          — regenerated outro audio + portrait renders + 4K endcard
    ├── ecis-ep8-short-slate.mp4 — 9:16 review cut
    └── ecis-ep8-short.mp4    — 9:16 final master (2160×3840)
```

## Rebuilding this video

```bash
cd brutalist.art

# 16:9 (4K, 3840×2160)
python3 runtime/scripts/generate_audio_kokoro.py anjana-s/2026-09-25-ecis-explained
python3 runtime/scripts/remotion_scenes.py anjana-s/2026-09-25-ecis-explained
./art final anjana-s/2026-09-25-ecis-explained

# 9:16 derivative (4K vertical, 2160×3840)
python3 runtime/scripts/shorts.py anjana-s/2026-09-25-ecis-explained --drop B01 B05 B08 --handle ""
python3 runtime/scripts/generate_audio_kokoro.py anjana-s/2026-09-25-ecis-explained/short
python3 runtime/scripts/remotion_scenes.py anjana-s/2026-09-25-ecis-explained/short
./art final anjana-s/2026-09-25-ecis-explained/short --height 3840
```

GATE P is signed for both the parent (`PEDAGOGY.md` — `VERDICT: PASS`) and
the short derivative (`short/PEDAGOGY.md` — `VERDICT: PASS`).
