# ECIS Episode 2 — Two Brains, 25 Companies, One Scorecard

**Skill:** ai-explainer · **Voice:** af_bella (Anjana) · **Duration:** ~60s · **Status:** rendered
**Series:** Sequel to ECIS Episode 1 (`anjana-s/2026-08-07-ecis-explained`, "The Honest Scorecard") — extends the system, doesn't re-explain it.
**Destination:** `anjana-s/2026-08-14-ecis-explained`

## About this video

Episode 1 introduced ECIS's four-reader system for reading earnings-call guidance. Episode 2 picks up assuming you already know that, and shows how the system grew.

The single LLM reader becomes two independent models — Llama and Mistral — that process every chunk through the same pipeline without sharing answers. When they agree, confidence goes up; when they disagree, the system knows exactly where the language got ambiguous. The pipeline itself scales from two hand-checked tickers in Episode 1 to a full sector of 20–25 companies, hundreds of transcripts and thousands of chunks running through the same readers and routing.

At that scale, the video zeroes in on the hardest judgment call in the system: the line between "guidance maintained" and "no guidance given at all." A CEO saying "we're reaffirming our outlook" and one saying "we remain focused on executing our strategy" sound similar to a human ear but score completely differently — and getting that boundary right is what makes the system trustworthy at scale. It closes on the dashboard where every signal, every reader's vote, and every feedback-loop decision lands in one live, queryable place.

## File structure

```
ecis-ep2/
├── README.md, PEDAGOGY.md   — build notes and sign-off
├── script.md, beats.json    — narration script and beat timing
├── narration/, visuals/     — per-beat TTS text and visual briefs
├── qc-sheet.png              — composite QC contact sheet
├── mp3/                     — narration audio
├── clips/, media/            — rendered per-beat video
└── _qc/                     — QC frame grabs
```

## Rebuilding this video

```bash
cd brutalist.art
python3 runtime/scripts/generate_audio_kokoro.py anjana-s/2026-08-14-ecis-explained
./art run   anjana-s/2026-08-14-ecis-explained
./art todo  anjana-s/2026-08-14-ecis-explained
./art final anjana-s/2026-08-14-ecis-explained
```

GATE P is already signed in `PEDAGOGY.md` (`VERDICT: PASS`), so
`generate_audio_kokoro.py` runs without needing `--no-gate`.
