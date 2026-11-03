# Temperature: The Dial Between Prediction and Hallucination

**Skill:** ai-explainer · **Voice:** af_bella (Anjana) · **Duration:** ~168s (16:9) / ~173s (9:16 short) · **Status:** rendered (both orientations, final cut + slate)
**Destination:** `anjana-s/2026-08-28-temperature-llm-finance`
**Delivery:** rendered at 4K in both 16:9 (`temperature-finance.mp4`, 3840×2160) and 9:16 (`short/temperature-finance-short.mp4`, 2160×3840).

## About this video

Run the same LLM, on the same prompt, with the same earnings-call quote, three times — and get three different extracted answers. Nothing about the model or the input changed. One setting did: temperature.

The video walks through what that single number actually controls. At temperature 0, the model always picks the single most likely next token — deterministic, same input in, same output out, every time. Turn it up to 0.5 and the distribution loosens: mostly the same answer, with occasional variation. Push it to 1.0 and the distribution flattens — rare, unlikely tokens get a real shot at being picked, which is exactly what you want for creative writing and exactly what you don't want when you're extracting a financial signal from a transcript.

It makes the stakes concrete by running one earnings quote through three temperatures, three times each: at T=0 the model says "maintained" all three times, locked. At T=0.5 it agrees twice and drifts once. At T=1.0 it gives three different directions on three different runs — unusable. That's the case for why financial extraction systems run at low temperature, and why self-consistency decoding (running the same prompt multiple times and taking a majority vote) exists at all: if a model can't agree with itself, its answer isn't stable enough to trust.

## File structure

```
temperature-finance/
├── README.md, PEDAGOGY.md   — build notes and sign-off
├── script.md, beat_sheet.json, beats.json — narration script and beat config
├── narration/, visuals/     — per-beat TTS text and visual briefs
├── mp3/, clips/, media/     — narration audio and rendered per-beat video (16:9)
├── temperature-finance-slate.mp4 — 16:9 review cut
├── temperature-finance.mp4  — 16:9 final master (3840×2160)
└── short/                   — 9:16 derivative cut (via runtime/scripts/shorts.py)
    ├── PEDAGOGY.md               — sign-off (pure reformat, no new narration)
    ├── beat_sheet.json           — aspect_ratio 9:16, no beats dropped
    ├── mp3/, media/              — symlinked parent audio + portrait Remotion renders
    ├── temperature-finance-short-slate.mp4 — 9:16 review cut
    └── temperature-finance-short.mp4       — 9:16 final master (2160×3840)
```

Four body-beat illustrations (`TemperatureHook`, `TemperatureDial`,
`TemperatureFinance`, `TemperatureClose`) plus their portrait `916`
counterparts share one reusable rotary dial component and are registered in
`runtime/remotion/src/Root.tsx`, under
`runtime/remotion/src/illustrations/temperature-finance/`.

## Rebuilding this video

```bash
cd brutalist.art

# 16:9 (4K, 3840×2160)
python3 runtime/scripts/generate_audio_kokoro.py anjana-s/2026-08-28-temperature-llm-finance
python3 runtime/scripts/remotion_scenes.py anjana-s/2026-08-28-temperature-llm-finance
./art final anjana-s/2026-08-28-temperature-llm-finance

# 9:16 derivative (4K vertical, 2160×3840)
python3 runtime/scripts/shorts.py anjana-s/2026-08-28-temperature-llm-finance   # full reformat, no cuts needed
python3 runtime/scripts/remotion_scenes.py anjana-s/2026-08-28-temperature-llm-finance/short
./art final anjana-s/2026-08-28-temperature-llm-finance/short --height 3840
```

GATE P is signed for both the parent (`PEDAGOGY.md` — `VERDICT: PASS`) and
the short derivative (`short/PEDAGOGY.md` — `VERDICT: PASS`).
