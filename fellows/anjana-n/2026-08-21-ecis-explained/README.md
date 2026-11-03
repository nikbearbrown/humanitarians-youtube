# ECIS Episode 3 — Three Models, Zero Shortcuts

**Skill:** ai-explainer · **Voice:** af_bella (Anjana) · **Duration:** ~194s · **Status:** rendered (final cut + slate produced)
**Series:** Sequel to ECIS Episode 2 (`examples/ecis-ep2`, "Two Brains, 25 Companies, One Scorecard") — extends the system, doesn't re-explain it.
**Destination:** `anjana-s/2026-08-21-ecis-explained`

## About this video

Episode 2 gave ECIS two independent LLM readers, Llama and Mistral, cross-checking each other across 25 companies. Episode 3 picks up from there and adds a third: Qwen2.5, at 14B parameters roughly twice the size of the other two, running the same pipeline and prompts but landing more reliable structured output. The bigger change isn't the extra model — it's that the architecture was reworked so multi-model support is native to the pipeline state rather than bolted on, and the triangulator now weighs all three readers independently.

More readers means more signals, and more signals means more noise if nothing checks it. So this episode's real subject is discipline: an input gate that rejects empty, boilerplate, or too-short chunks before any reader sees them, and an output gate that logs low-confidence signals for audit instead of letting them quietly drag down the scorecard. Every signal ECIS produces now also carries its own provenance — the exact system prompt, few-shot examples, temporal context, and source chunk that produced it — so any signal can be reproduced and re-run months later instead of trusted blindly.

It closes on the dashboard, now showing all three models' calibration curves and Brier scores side by side, filterable by ticker, model, or confidence, with every signal drillable down to its full provenance trail.

## File structure

```
ecis-ep3/
├── README.md, PEDAGOGY.md   — build notes and sign-off
├── script.md, beats.json    — narration script and beat timing
├── narration/, visuals/     — per-beat TTS text and visual briefs
├── mp3/                     — narration audio (generated after GATE P)
├── clips/, media/            — rendered per-beat video
└── _qc/                     — QC frame grabs
```

`beat_sheet.json` is the full Remotion scene config `generate_audio_kokoro.py`
and `./art run` read; `beats.json` is the lighter per-beat timing/status
ledger the script was originally planned against. The six body-beat
illustrations (`Ecis3Recap`, `Ecis3ThirdModel`, `Ecis3QualityGates`,
`Ecis3Provenance`, `Ecis3Dashboard`, `Ecis3Close`) are written and registered
in `runtime/remotion/src/Root.tsx` under `runtime/remotion/src/illustrations/ecis-ep3/`.

## Rebuilding this video

```bash
cd brutalist.art
python3 runtime/scripts/generate_audio_kokoro.py anjana-s/2026-08-21-ecis-explained
./art run   anjana-s/2026-08-21-ecis-explained
./art todo  anjana-s/2026-08-21-ecis-explained
./art final anjana-s/2026-08-21-ecis-explained
```

GATE P is signed (see `PEDAGOGY.md` — `VERDICT: PASS`).
