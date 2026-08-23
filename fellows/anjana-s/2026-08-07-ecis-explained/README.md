# ECIS — The Honest Scorecard

**Skill:** ai-explainer · **Voice:** af_bella (Anjana) · **Duration:** ~2 min · **Status:** rendered
**Destination:** `anjana-s/2026-08-07-ecis-explained`

## About this video

Every earnings call has a CEO saying something like "we remain optimistic about our forward outlook" — and that sentence could mean raised guidance, lowered guidance, or nothing at all. ECIS (Earnings Call Intelligence Signals) reads the transcript and tells you which, with a confidence score you can actually trust.

Four independent readers run on every chunk of every transcript — a keyword matcher, FinBERT for sentiment, a named-entity recognizer for hard numbers, and an LLM that reasons through the passage with chain-of-thought and self-consistency checks. A triangulator fuses all four, weighting the readers that have historically been right more heavily. Smart routing skips the expensive LLM pass entirely for chunks where the fast readers already agree there's nothing there, cutting inference calls by 60–80%.

The part that gives the system its name: every signal gets logged before anyone knows if it was right, then checked against the actual market 30 days later. Brier score, calibration error, skill score — ECIS tracks its own honesty the same way it tracks the companies it's watching, and three separate feedback loops let it self-correct. Anything structural — a routing threshold shifting by more than 25%, a reader getting swapped out — pauses the system and waits for a human to approve it.

## File structure

```
ecis/
├── README.md, PEDAGOGY.md   — build notes and sign-off
├── script.md, beats.json    — narration script and beat timing
├── scenes.py                — Manim source for the B03/B04 diagrams
├── narration/, visuals/     — per-beat TTS text and visual briefs
├── qc-sheet.png              — composite QC contact sheet
├── mp3/                     — narration audio
├── clips/, media/            — rendered per-beat video (Remotion)
├── manim/                   — B03/B04 architecture + routing renders
└── _qc/                     — QC frame grabs
```

## Rebuilding this video

```bash
cd brutalist.art
python3 runtime/scripts/generate_audio_kokoro.py anjana-s/2026-08-07-ecis-explained
./art run   anjana-s/2026-08-07-ecis-explained
./art todo  anjana-s/2026-08-07-ecis-explained
./art final anjana-s/2026-08-07-ecis-explained
```

GATE P is already signed in `PEDAGOGY.md` (`VERDICT: PASS`). `./art run`
finds `scenes.py` in this folder and renders B03/B04 via Manim automatically.
