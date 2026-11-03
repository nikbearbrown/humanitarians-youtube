# ECIS Episode 12: How Long Does a Signal Last?

## Series
ECIS Weekly Update — Episode 12

---

## Concept: Earnings Call Intelligence Signals

#### Every quarter, 500 companies tell the market where they're headed. The signal hides in plain sight. ECIS reads what others skim.

---

## What is ECIS?

ECIS (Earnings Call Intelligence Signals) is a financial intelligence system that transforms raw earnings call transcripts into structured, confidence-scored guidance signals, and then holds itself accountable by grading every prediction against real market outcomes.

> Built to extract. Designed to doubt. Engineered to improve.

---

## The Vision:

Earnings calls are the richest public source of corporate intent. Executives disclose revenue targets, margin expectations, and strategic direction. Analysts probe for weakness. The language is deliberate, the stakes are real, and every transcript is public record.

ECIS turns that language into structured intelligence, not by trusting a single model, but by orchestrating multiple readers that challenge each other, catch each other's blind spots, and build trust through validated outcomes.


Phase 17 adds three capabilities: signal quality analysis, linguistic depth (speech act classification, discourse structure, metaphor tracking, sarcasm detection), and feature engineering (automated selection, interaction discovery, embedding drift monitoring). The episode title focuses on signal decay — the most intuitive hook — and expands to cover the full phase.

---

## Voice
Kokoro TTS — am_onyx

---

## Rendering
Remotion (motion graphics) via toolkit

---

## File structure

```
ecis-ep12/
├── README.md, PEDAGOGY.md   — build notes and sign-off
├── script.md                — the authored body beats (B01–B06)
├── beat_sheet.json, beats.json — beat config
├── narration/, visuals/     — per-beat TTS text and visual briefs
├── mp3/, clips/, media/     — narration audio and rendered per-beat video (16:9)
├── ecis-ep12-slate.mp4      — 16:9 review cut
├── ecis-ep12.mp4            — 16:9 final master (3840×2160)
└── short/                   — 9:16 derivative cut (via runtime/scripts/shorts.py)
    ├── PEDAGOGY.md           — sign-off for the derivative cut
    ├── beat_sheet.json       — aspect_ratio 9:16, beats dropped to fit the Shorts cap
    ├── mp3/, media/          — regenerated outro audio + portrait renders + 4K endcard
    ├── ecis-ep12-short-slate.mp4 — 9:16 review cut
    └── ecis-ep12-short.mp4    — 9:16 final master (2160×3840)
## Rebuilding this video

```bash
cd brutalist.art
python3 runtime/scripts/generate_audio_kokoro.py anjana-s/2026-10-23-ecis-explained
./art run   anjana-s/2026-10-23-ecis-explained
./art todo  anjana-s/2026-10-23-ecis-explained
./art final anjana-s/2026-10-23-ecis-explained
```
---
