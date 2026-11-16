# Quantization: Big AI on a Laptop

**Fellow:** Likhith R. · **Week:** 2026-10-26 to 2026-11-01 · **Builder:** `ai-explainer` on `claude-hai` · **Voice:** Kokoro `am_onyx` (AI narration)

A 60-second explainer on quantization: how a 70-billion-weight model that needs 140 GB at 16 bits can still run on a laptop, by rounding each weight onto a small grid and storing it in 8 or 4 bits.

## This week's contribution
- **Question:** How does a model that needs 140 GB of memory run on a 16 GB laptop?
- **Prediction:** I expected quantization to be mostly about throwing precision away and accepting worse answers, and I thought GPTQ and AWQ were two versions of the same trick for protecting outlier weights.
- **What I built/tried:** 12 beats: the 140 GB problem, weights as 2-byte numbers, rounding onto a grid, 256 vs. 16 levels with per-group scales, 14 → 7 → 3.5 GB, why rounding errors mostly cancel, where quality drops below 4 bits, and llama.cpp / Ollama making 4-bit the local default. Every number on screen comes from a seeded numpy run (`evidence/quant_toy.py`). Eight custom dual-aspect scenes in `scenes/Quantization.tsx`.
- **Observed result:** Both cuts render at native 4K (60.0 s). GATE F, L, T (unmodified checker) and V (0 blocker / 0 major) pass on 16:9 and 9:16.
- **Next experiment:** Quantize one small open model myself at 8, 4 and 3 bits with llama.cpp and measure the memory, speed and answer quality on my own laptop.

## Human and AI work
**My decisions, implementation and verification:**
- Chose the topic and wrote the content brief (the points the beats cover), and set the 12-beat / ~60 s / Kokoro `am_onyx` / native 16:9 + 9:16 constraints.
- Set the branding: @HumanitariansAI channel, "Irreducibly Human" kicker, greetings ("Namaskaram, Likhith" on 16:9, "Hey, Likhith" on 9:16) and the required opening line.
- Watched both the 16:9 and 9:16 cuts, checked each claim in `FACTCHECK.md` against the sources, and approved the final masters.

**AI tools/voices used and what they generated:**
- Claude Code (Anthropic) drafted the beat sheet and narration, wrote the custom scenes in `scenes/`, wrote and ran the evidence code, checked claims against `SOURCES.md`, ran the Brutalist pipeline and gates, and fixed layout defects found in visual QC.
- Narration is an AI voice (Kokoro `am_onyx`, local). **It is not a recording of Likhith.**

**What I rejected or corrected:**
- My brief said GPTQ and AWQ both protect outliers. Corrected: GPTQ compensates the rounding error of each weight using the ones not yet quantized, and AWQ protects the small share of weights that matter most for the activations.
- "3.5 GB" is stated as "about": real 4-bit files also store the scales (about 3.94 GB for 7B).
- The quality-vs-bits curve is from a toy layer, so it is captioned as a proxy, not a benchmark.
- Kokoro read "3.5" as "three. five", so it is spoken "three and a half"; "Your turn" and "llama.cpp" got pronunciation fixes after I flagged them.

**What remains unverified or failed:**
- The required intro "Hi, I am Likhith…" is spoken by the AI narrator; the AI narration is disclosed on screen (opening beat and outro).
- The toy quantizes one synthetic layer; it doesn't measure a real model's answer quality.
- YouTube 4K processing check and the professors' publication decision are pending.

## Reproduce
- **Brutalist version/commit:** nikbearbrown/brutalist.art `a187fab` (Remotion 4.0.535 / React 19).
- **Source commit used for this export:** not committed — `a187fab` plus local changes: `Quantization.tsx`, `JevExplainer.tsx`, `HaiOutro.tsx` under `runtime/remotion/src/`, each exported component registered in `Root.tsx` twice: under its own name at 1920×1080, and with a `916` suffix at 1080×1920. `type_check.py` is the unmodified toolkit version.
- **Beat sheet and custom scene files:** `beat_sheet.json` (16:9), `vertical/beat_sheet.json` (9:16), `scenes/Quantization.tsx`, `scenes/JevExplainer.tsx`, `scenes/HaiOutro.tsx`.
- **Commands** (toolkit root, Python 3.12 venv, MacTeX on PATH; reel at `youtube/brutalist/claude-hai-quantization/`):
  ```bash
  python3 runtime/scripts/generate_audio_kokoro.py <reel> --speed <s>          # speeds used: 1.2
  python3 runtime/scripts/remotion_scenes.py <reel>
  ./art run <reel>                                              # 16:9 review
  ./art vertical <reel>                                         # then restore vertical/beat_sheet.json from this folder
  python3 runtime/scripts/remotion_scenes.py <reel>/vertical
  ./art final <reel>                                            # 16:9 master (GATE T first)
  ./art final <reel>/vertical --height 3840                     # 9:16 master
  ```
- **Input/source links:** [SOURCES.md](SOURCES.md) · executable evidence in [`evidence/`](evidence/)
- **Approvals and checks:** [FACTCHECK.md](FACTCHECK.md) (signed off by Likhith), [TYPECHECK.md](TYPECHECK.md) and [vertical/TYPECHECK.md](vertical/TYPECHECK.md) (GATE T PASS), [CHECKS-REPORT.md](CHECKS-REPORT.md), [BUILD-LOG.md](BUILD-LOG.md).

## Watch and review
- **Landscape** — [Watch `landscape/QuantizationBigAIOnALaptop_LikhithR.mp4`](https://drive.google.com/file/d/1gz_G1vxSHPHhb5byQDPp-lIFATdTrIkK/view?usp=sharing) — 3840×2160 — 60.0 s — SHA-256 `8c9cd808826ca4bbe7bea894985cd4bec488b66368f5eed0efac305cb121be72` (final master, `.verified.json` receipt: ready)
- **Vertical** — [Watch `vertical/QuantizationBigAIOnALaptop_LikhithR.mp4`](https://drive.google.com/file/d/19YVC5UiqeGUAIsy9Ut-muXOzJk-exz1e/view?usp=share_link) — 2160×3840 — 60.0 s — SHA-256 `48194f0f1da6d901f493cd98b0aad40b86767d4b1d12aee62753a40ab8acb2fb` (final master, `.verified.json` receipt: ready)
- Sources/large assets Drive link: none
- PM review status: pending
- YouTube 4K processing check: pending upload
- Professors' publication decision: pending

## Folder contents
- `README.md` — this report · `FRICTIONAL.md` — process log · `description.txt` — video description
- `beat_sheet.json` / `vertical/beat_sheet.json` — 16:9 / 9:16 production plans · `SCRIPT.md` — narration
- `SOURCES.md`, `FACTCHECK.md`, `SHOTLIST.md`, `PROMPTS.md`, `CHECKS-REPORT.md`, `BUILD-LOG.md`, `TYPECHECK.md` (+ `vertical/TYPECHECK.md`) — sources, claims, shots, prompts, pre-render checks, build record, type-lock gate
- `BUILD-PROMPT.md` — the build prompt
- `scenes/` — custom Remotion scene code (`JevExplainer.tsx` holds the shared stage helpers; `HaiOutro.tsx` is the outro)
- `evidence/` — the executed code and its real output shown on screen
