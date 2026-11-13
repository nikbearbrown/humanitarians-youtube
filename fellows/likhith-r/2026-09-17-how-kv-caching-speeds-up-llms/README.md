# How KV Caching Speeds Up LLMs

**Fellow:** Likhith R. · **Week:** 2026-09-14 to 2026-09-20 · **Builder:** `ai-explainer` on `claude-hai` · **Voice:** Kokoro `am_onyx` (AI narration)

A 60-second explainer on the KV cache: each new token reuses the stored keys and values of earlier tokens instead of recomputing them, which is why text streams quickly after the first word, and why long contexts cost memory.

## This week's contribution
- **Question:** Why does a chatbot pause before its first word and then stream the rest so fast?
- **Prediction:** I expected LLMs to get faster per token as a response goes on; the fact-check corrected that to roughly steady cost after the first token.
- **What I built/tried:** 12 beats covering seven points I set: the pause-then-stream hook; recomputation without a cache; queries, keys and values; storing K and V; decoding against the cache; quadratic to roughly linear work per token; the memory trade-off. The counts and memory figures come from a real script (`evidence/kv_cache_toy.py`) that checks cached and uncached decoding give the same result. Seven custom dual-aspect scenes in `scenes/KvCache.tsx`.
- **Observed result:** Both cuts render at native 4K (65.4 s). GATE F, L, T (unmodified checker) and V (0/0) pass on 16:9 and 9:16.
- **Next experiment:** Work out how batch size and grouped-query attention change KV-cache memory for a real model shape.

## Human and AI work
**My decisions, implementation and verification:**
- Chose the topic and wrote the content brief (the points the beats cover), and set the 12-beat / ~60 s / Kokoro `am_onyx` / native 16:9 + 9:16 constraints.
- Set the branding: @HumanitariansAI channel, "Irreducibly Human" kicker, and the required opening line.
- Watched both cuts and signed off every claim in `FACTCHECK.md`.

**AI tools/voices used and what they generated:**
- Claude Code (Anthropic) drafted the beat sheet and narration, wrote the custom scenes in `scenes/`, ran the evidence code, checked claims against `SOURCES.md`, ran the Brutalist pipeline and gates, and fixed layout defects found in visual QC.
- Narration is an AI voice (Kokoro `am_onyx`, local). **It is not a recording of Likhith.**

**What I rejected or corrected:**
- My brief said LLMs get faster per token as a response goes on; corrected to roughly steady cost per token after the first — the cache is why it's fast, not accelerating.
- The initial pause is attributed to prefill (reading the prompt and filling the cache), with no latency numbers shown.
- The memory figure uses one published model shape (Llama 2 7B) and is captioned; batch size and grouped-query attention change it.
- The equation was simplified for legibility, and portrait labels merged to clear the 9:16 type floor.

**What remains unverified or failed:**
- The required intro "Hi, I am Likhith…" is spoken by the AI narrator; the AI narration is disclosed on screen (opening beat and outro).
- YouTube 4K processing check and the professors' publication decision are pending.

## Reproduce
- **Brutalist version/commit:** nikbearbrown/brutalist.art `6a8380a`.
- **Source commit used for this export:** not committed — `6a8380a` plus local changes: `scenes/KvCache.tsx`, `scenes/JevExplainer.tsx`, `scenes/HaiOutro.tsx` added under `runtime/remotion/src/`, each exported component registered in `Root.tsx` twice: under its own name at 1920×1080, and with a `916` suffix at 1080×1920, and `durationSeconds` hooks added to `ClaudeComposerAsk916`, `BrutalistHesitantWriter916`, `ClaudeVerdictArtifact916`. `type_check.py` is the unmodified toolkit version.
- **Beat sheet and custom scene files:** `beat_sheet.json` (16:9), `vertical/beat_sheet.json` (9:16), `scenes/KvCache.tsx`, `scenes/JevExplainer.tsx`, `scenes/HaiOutro.tsx`.
- **Commands** (toolkit root, Python 3.12 venv, MacTeX on PATH; reel at `youtube/brutalist/claude-hai-kv-caching/`):
  ```bash
  python3 runtime/scripts/generate_audio_kokoro.py <reel>
  python3 runtime/scripts/remotion_scenes.py <reel>
  ./art run <reel>                                              # 16:9 review
  ./art vertical <reel>                                         # then restore vertical/beat_sheet.json from this folder
  python3 runtime/scripts/remotion_scenes.py <reel>/vertical
  ./art final <reel>                                            # 16:9 master (GATE T first)
  ./art final <reel>/vertical --height 3840                     # 9:16 master
  ```
  ```bash
  # executable evidence (see SOURCES.md for the exact environment)
  ls evidence/
  ```
- **Input/source links:** [SOURCES.md](SOURCES.md)
- **Approvals and checks:** [FACTCHECK.md](FACTCHECK.md) (signed off by Likhith), [TYPECHECK.md](TYPECHECK.md) and [vertical/TYPECHECK.md](vertical/TYPECHECK.md) (GATE T PASS), [CHECKS-REPORT.md](CHECKS-REPORT.md), [BUILD-LOG.md](BUILD-LOG.md).

## Watch and review
- **Landscape** — [Watch `landscape/KVCaching_LikhithR.mp4`](https://drive.google.com/file/d/1Xy6othbPhBSzyHP9TeK2ntNN0AoTNo9M/view?usp=sharing) — 3840×2160 — 65.4 s — SHA-256 `b58d5a7668b6245adde5e0d570615ddd171a54990472f0a2aa96cebcf6124302` (final master, `.verified.json` receipt: ready)
- **Vertical** — [Watch `vertical/KVCaching_LikhithR.mp4`](https://drive.google.com/file/d/1_I2KVjicjc6NRAZ-hIXaMgNZOM3OIAPM/view?usp=sharing) — 2160×3840 — 65.4 s — SHA-256 `a80e8afd13df580a0e37037f5d0e5213b460c975a3bf327b00aea1fd0f87c094` (final master, `.verified.json` receipt: ready)
- Sources/large assets Drive link: none
- PM review status: pending
- YouTube 4K processing check: pending upload
- Professors' publication decision: pending

## Folder contents
- `README.md` — this report · `FRICTIONAL.md` — process log · `description.txt` — video description
- `beat_sheet.json` / `vertical/beat_sheet.json` — 16:9 / 9:16 production plans · `SCRIPT.md` — narration
- `SOURCES.md`, `FACTCHECK.md`, `SHOTLIST.md`, `PROMPTS.md`, `CHECKS-REPORT.md`, `BUILD-LOG.md`, `TYPECHECK.md` (+ `vertical/TYPECHECK.md`) — sources, claims, shots, prompts, pre-render checks, build record, type-lock gate
- `scenes/` — custom Remotion scene code (`JevExplainer.tsx` holds the shared stage helpers; `HaiOutro.tsx` is the outro)
- `evidence/` — the executed code and its real output shown on screen
