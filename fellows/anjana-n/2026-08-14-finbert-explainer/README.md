# What Happens When You Teach BERT to Read Financial Statements

**Skill:** ai-explainer · **Voice:** af_bella (Anjana) · **Duration:** ~60s · **Status:** slate rendered, full cut pending
**Destination:** `anjana-s/2026-08-14-finbert-explainer`

## About this video

BERT is a language model that reads everyday English just fine — but hand it an earnings call and it breaks. A general model reads "beat estimates by a narrow margin" as positive; but, in finance, that phrasing is not. "Headwinds" isn't about weather. "Adjusted results" usually means numbers got reshaped to look better. The same words carry different weight when money is on the line, and BERT doesn't know that — yet.

FinBERT is the fix, and the video's whole point is how small that fix actually is: it's the *same* BERT architecture, just fine-tuned on ~50,000 sentences of financial text. Nothing structural changes — only the training data — and that's enough to teach the model that "revenue decline" is bad news while "expense decline" is good news.

The video walks through it in order: where a general model gets financial language wrong, how fine-tuning reshapes the model's weights without touching its architecture, what's actually happening inside FinBERT when it reads a sentence (tokenize → embed → attend → classify, in about 10ms), and the payoff — same architecture, retrained, now reading money instead of just words.

## File structure

```
finbert-explainer/
├── README.md, PEDAGOGY.md       — build notes and sign-off
├── script.md, beats.json        — narration script and beat timing
├── narration/, visuals/         — per-beat TTS text and visual briefs
├── qc-sheet.png                 — composite QC contact sheet
├── mp3/                         — narration audio
├── clips/, media/                — rendered per-beat video
├── _qc/                         — QC frame grabs
└── finbert-explainer-slate.mp4  — rendered title slate
```

## Rebuilding this video

```bash
cd brutalist.art
python3 runtime/scripts/generate_audio_kokoro.py anjana-s/2026-08-14-finbert-explainer
./art run   anjana-s/2026-08-14-finbert-explainer
./art todo  anjana-s/2026-08-14-finbert-explainer
./art final anjana-s/2026-08-14-finbert-explainer
```

GATE P is already signed in `PEDAGOGY.md` (`VERDICT: PASS`), so
`generate_audio_kokoro.py` runs without needing `--no-gate`.
