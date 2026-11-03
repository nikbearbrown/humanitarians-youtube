# AI Doesn't Sleep, Markets Don't Wait

**Skill:** ai-explainer · **Voice:** af_bella (Anjana) · **Duration:** ~60s · **Status:** rendered
**Destination:** `anjana-s/2026-08-07-why-ai-dominates-the-crypto-market`

## About this video

Traditional markets had a rhythm: an opening bell, a closing bell, a floor that emptied out at four o'clock and stayed quiet overnight. Crypto broke that. Bitcoin trades at 3am on a Sunday; there is no closing bell anymore, and the clock that used to structure trading just doesn't apply.

A human trader still needs sleep, weekends, a moment to look away — and in a market that never pauses, every second of inattention is a second something can move against you. The video stages exactly that: a flash crash at 2:14am while the trader is asleep, gone before the alarm goes off.

AI's edge in this world isn't that it's smarter than a human trader — it's that it's simply always there. It watches thousands of trading pairs across hundreds of exchanges at once — order books, social sentiment, whale wallets, liquidation maps, news, on-chain data — and reacts in milliseconds. The argument the video makes is a presence argument, not an intelligence argument: the machine's advantage is that it never has to clock out.

## File structure

```
ai-markets/
├── README.md, PEDAGOGY.md   — build notes and sign-off
├── script.md, beats.json    — narration script and beat timing
├── narration/, visuals/     — per-beat TTS text and visual briefs
├── qc-sheet.png              — composite QC contact sheet
├── mp3/                     — narration audio
├── clips/, media/            — rendered per-beat video
├── _qc/                     — QC frame grabs
├── ai-markets-slate.mp4     — rendered title slate
└── ai-markets.mp4           — final assembled video
```

## Rebuilding this video

```bash
cd brutalist.art
python3 runtime/scripts/generate_audio_kokoro.py anjana-s/2026-08-07-why-ai-dominates-the-crypto-market
./art run   anjana-s/2026-08-07-why-ai-dominates-the-crypto-market
./art todo  anjana-s/2026-08-07-why-ai-dominates-the-crypto-market
./art final anjana-s/2026-08-07-why-ai-dominates-the-crypto-market
```

GATE P is already signed in `PEDAGOGY.md` (`VERDICT: PASS`), so
`generate_audio_kokoro.py` runs without needing `--no-gate`.
