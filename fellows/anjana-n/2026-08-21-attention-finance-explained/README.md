# Attention Is All You Need (To Read an Earnings Call)

**Skill:** ai-explainer · **Voice:** af_bella (Anjana) · **Duration:** ~176s · **Status:** rendered (final cut + slate produced)
**Destination:** `anjana-s/2026-08-21-attention-finance-explained`

## About this video

Take one real-sounding CEO sentence: "We expect revenue to remain broadly in line with prior guidance despite near-term headwinds." A human reads it in three seconds and knows it's cautious. An older, left-to-right language model doesn't — by the time it reaches "headwinds" at the end, it's already committed to a positive read of "revenue" at the start, and it can't go back. That's a wrong answer, confidently given.

The fix is self-attention: instead of reading in order, a transformer reads the whole sentence at once — every word asks every other word "how much do you matter to me?" "Revenue" pays attention to "headwinds" clear across the sentence; "despite" reweighs everything that came before it. The video makes this concrete by running the exact same sentence through both readings side by side, then landing the payoff — three rapid-fire financial examples showing the same pattern: a hedge word like "but," "although," or "excluding" can flip the whole sentence's meaning, and only a model that sees the full sentence at once catches it.

It closes on the title as a joke that rewards knowing the reference: "Attention Is All You Need (To Read an Earnings Call)" — a riff on the 2017 transformer paper's actual title.

## File structure

```
attention-finance/
├── README.md, PEDAGOGY.md   — build notes and sign-off
├── script.md, beats.json    — narration script and beat timing
├── narration/, visuals/     — per-beat TTS text and visual briefs
├── mp3/                     — narration audio
├── clips/, media/            — rendered per-beat video
└── _qc/                     — QC frame grabs
```

## Rebuilding this video

```bash
cd brutalist.art
python3 runtime/scripts/generate_audio_kokoro.py anjana-s/2026-08-21-attention-finance-explained
./art run   anjana-s/2026-08-21-attention-finance-explained
./art todo  anjana-s/2026-08-21-attention-finance-explained
./art final anjana-s/2026-08-21-attention-finance-explained
```

GATE P is signed (see `PEDAGOGY.md` — `VERDICT: PASS`).
