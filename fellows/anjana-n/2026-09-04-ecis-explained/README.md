# ECIS Episode 5 — The System That Learned From Its Own Mistakes

**Skill:** ai-explainer · **Voice:** af_bella (Anjana) · **Duration:** ~258s (16:9) / ~170s (9:16 short) · **Status:** rendered (both orientations, final cut + slate)
**Series:** Sequel to ECIS Episodes 1–4 — the system audits itself, rather than gaining a new capability.
**Destination:** `anjana-s/2026-09-04-ecis-explained`
**Delivery:** rendered at 4K in both 16:9 (`ecis-ep5.mp4`, 3840×2160) and 9:16 (`short/ecis-ep5-short.mp4`, 2160×3840)

## About this video

Episode 4 taught ECIS to weigh who was speaking and how clean the source chunk was. Episode 5 does something different: instead of adding a capability, the system goes back through its own errors and fixes the specific place where it was weakest. The hardest call in the whole pipeline turned out to be the line between "maintained" and "none" — the difference between a company reaffirming guidance and a company saying something that merely sounds like guidance. "We are comfortable with our current outlook" is the first; "We remain focused on execution" is the second, and the model kept confusing them.

The fix is deliberately narrow. Human-reviewed extractions were formatted into training data concentrated on that exact boundary, and a QLoRA adapter — rank 16, four-bit, five epochs — was trained on top of the existing eight-billion-parameter model. The adapter is a small block bolted onto a large model, and the video keeps it visually small on purpose: it sharpens one edge rather than replacing anything.

Three smaller upgrades follow the same self-audit logic. Self-consistency penalties used to be flat — any two-to-one vote cost the same — and now they scale with how far apart the votes actually are, so a 0.80-versus-0.75 disagreement barely dents confidence while a 0.80-versus-0.20 disagreement hits hard. Section weighting scales signals again by where they came from, with prepared remarks at full weight and Q&A at 0.8, because rehearsed language is more reliable than a spontaneous answer. And three new detectors catch problems before the scorecard sees them: negation phrases that force a chunk past the fast-pass shortcut, keyword density that separates real lexical support from sentiment-only guesses, and duplicate detection that drops re-filed transcripts.

The episode closes on signal decay. A prediction can be right at thirty days and wrong at one hundred eighty — that is short-term noise that looked real — while a prediction right at all three horizons is a genuine read. Every signal now carries a decay profile, so the scorecard knows which readers produce predictions that last. The point of the whole episode: the system did not get bigger this week, it got more honest about where it was wrong.

## File structure

```
ecis-ep5/
├── README.md, PEDAGOGY.md   — build notes and sign-off
├── script.md, beat_sheet.json, beats.json — narration script and beat config
├── narration/, visuals/     — per-beat TTS text and visual briefs
├── mp3/, clips/, media/     — narration audio and rendered per-beat video (16:9)
├── ecis-ep5-slate.mp4       — 16:9 review cut
├── ecis-ep5.mp4             — 16:9 final master (3840×2160)
└── short/                   — 9:16 derivative cut (via runtime/scripts/shorts.py)
    ├── PEDAGOGY.md           — sign-off for the derivative cut
    ├── beat_sheet.json       — aspect_ratio 9:16, beats dropped to fit the Shorts cap
    ├── mp3/, media/          — regenerated outro audio + portrait Remotion renders
    ├── ecis-ep5-short-slate.mp4 — 9:16 review cut
    └── ecis-ep5-short.mp4    — 9:16 final master (2160×3840)
```

Six body-beat illustrations (`Ecis5Recap`, `Ecis5Finetune`, `Ecis5Penalties`,
`Ecis5Detectors`, `Ecis5Decay`, `Ecis5Close`) plus their portrait `916`
counterparts are registered in `runtime/remotion/src/Root.tsx`, under
`runtime/remotion/src/illustrations/ecis-ep5/`.

## Rebuilding this video

```bash
cd brutalist.art

# 16:9 (4K, 3840×2160)
python3 runtime/scripts/generate_audio_kokoro.py anjana-s/2026-09-04-ecis-explained
python3 runtime/scripts/remotion_scenes.py anjana-s/2026-09-04-ecis-explained
./art final anjana-s/2026-09-04-ecis-explained

# 9:16 derivative (4K vertical, 2160×3840)
python3 runtime/scripts/shorts.py anjana-s/2026-09-04-ecis-explained
python3 runtime/scripts/generate_audio_kokoro.py anjana-s/2026-09-04-ecis-explained/short
python3 runtime/scripts/remotion_scenes.py anjana-s/2026-09-04-ecis-explained/short
./art final anjana-s/2026-09-04-ecis-explained/short --height 3840
```

GATE P is signed for both the parent (`PEDAGOGY.md` — `VERDICT: PASS`) and
the short derivative (`short/PEDAGOGY.md` — `VERDICT: PASS`).
