# ECIS Episode 4 — Not Just What. Who, How Clean, and What Came Before.

**Skill:** ai-explainer · **Voice:** af_bella (Anjana) · **Duration:** ~200s (16:9) / ~171s (9:16 short) · **Status:** rendered (both orientations, final cut + slate)
**Series:** Sequel to ECIS Episodes 1–3 (`anjana-s/2026-08-21-ecis-explained`) — extends the system, doesn't re-explain it.
**Destination:** `anjana-s/2026-08-28-ecis-explained`
**Delivery:** rendered at 4K in both 16:9 and 9:16.

## About this video

Episode 3 gave ECIS three independent models, input/output quality gates, and full signal provenance. Episode 4 doesn't add a fourth model — it adds context. Every signal now gets scaled by who said it: a CFO's "we are raising guidance" carries a weight of 1.0, the same words from an analyst asking a question carry 0.3, and an operator's transcript filler carries zero. The same confidence score lands completely differently depending on the speaker's authority.

It also scores how clean the source chunk was — boilerplate ratio, token count, section completeness, and speaker transitions combine into a single quality multiplier, so a chunk cut mid-sentence with three speakers tangled together gets quietly suppressed before it ever reaches the triangulator, rather than treated as equally trustworthy as a clean one.

The third addition is time: a single quarter's guidance means little in isolation, so the system now tags each signal with its trend context — consecutive raises, consecutive lowers, a reversal, or stable maintained guidance — so a sudden reversal after three steady quarters reads as the different, more significant pattern it actually is. The episode closes by showing all three multipliers — reader confidence, speaker authority, chunk quality — combining with trend context into one final signal: not just what was said, but who said it, how clean the source was, and what came before.

## File structure

```
ecis-ep4/
├── README.md, PEDAGOGY.md   — build notes and sign-off
├── script.md, beat_sheet.json, beats.json — narration script and beat config
├── narration/, visuals/     — per-beat TTS text and visual briefs
├── mp3/, clips/, media/     — narration audio and rendered per-beat video (16:9)
├── ecis-ep4-slate.mp4       — 16:9 review cut
├── ecis-ep4.mp4             — 16:9 final master (3840×2160)
└── short/                   — 9:16 derivative cut (via runtime/scripts/shorts.py)
    ├── PEDAGOGY.md           — sign-off for the one rewritten beat (the outro)
    ├── beat_sheet.json       — aspect_ratio 9:16, B08 dropped to fit the Shorts cap
    ├── mp3/, media/          — regenerated outro audio + portrait Remotion renders
    ├── ecis-ep4-short-slate.mp4 — 9:16 review cut
    └── ecis-ep4-short.mp4    — 9:16 final master (2160×3840)
```

Six body-beat illustrations (`Ecis4Recap`, `Ecis4Speaker`, `Ecis4Quality`,
`Ecis4Temporal`, `Ecis4Together`, `Ecis4Close`) plus their portrait `916`
counterparts are registered in `runtime/remotion/src/Root.tsx`, under
`runtime/remotion/src/illustrations/ecis-ep4/`.

## Rebuilding this video

```bash
cd brutalist.art

# 16:9 (4K, 3840×2160)
python3 runtime/scripts/generate_audio_kokoro.py anjana-s/2026-08-28-ecis-explained
python3 runtime/scripts/remotion_scenes.py anjana-s/2026-08-28-ecis-explained
./art final anjana-s/2026-08-28-ecis-explained

# 9:16 derivative (4K vertical, 2160×3840)
python3 runtime/scripts/shorts.py anjana-s/2026-08-28-ecis-explained          # plans cuts, rewires to *916 patterns
python3 runtime/scripts/generate_audio_kokoro.py anjana-s/2026-08-28-ecis-explained/short   # only the rewritten outro
python3 runtime/scripts/remotion_scenes.py anjana-s/2026-08-28-ecis-explained/short
./art final anjana-s/2026-08-28-ecis-explained/short --height 3840
```

GATE P is signed for both the parent (`PEDAGOGY.md` — `VERDICT: PASS`) and
the short derivative (`short/PEDAGOGY.md` — `VERDICT: PASS`, reviewing only
the one new/regenerated beat: the rewritten outro).
