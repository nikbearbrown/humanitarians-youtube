# Mixture of Experts

**Fellow:** Likhith R. · **Week:** 2026-09-14 to 2026-09-20 · **Builder:** `ai-explainer` on `claude-hai` · **Voice:** Kokoro `am_onyx` (AI narration)

A 60-second explainer on Mixture of Experts: a router sends each token to a few small expert blocks, so a model can hold far more parameters than it runs per token, at the cost of keeping every expert in memory.

## This week's contribution
- **Question:** How do Mixture of Experts models stay fast with so many parameters?
- **Prediction:** I expected "experts" to be separate specialist sub-models inside one big model.
- **What I built/tried:** 12 beats covering the points I set: the parameter-count hook; dense models; experts inside each layer; the router picking two of eight; only chosen experts running; Mixtral's published 47B total vs ~13B active; the memory catch. Seven custom dual-aspect scenes in `scenes/MoeExplainer.tsx`.
- **Observed result:** Both cuts render at native 4K (62.7 s). GATE F, L, T (unmodified checker) and V (0/0) pass on 16:9 and 9:16.
- **Next experiment:** Look into how routers are trained to balance load across experts, as a possible follow-up video.

## Human and AI work
**My decisions, implementation and verification:**
- Chose the topic and wrote the content brief (the points the beats cover), and set the 12-beat / ~60 s / Kokoro `am_onyx` / native 16:9 + 9:16 constraints.
- Set the branding: @HumanitariansAI channel, "Irreducibly Human" kicker, and the required opening line.
- Watched both cuts and signed off every claim in `FACTCHECK.md`.

**AI tools/voices used and what they generated:**
- Claude Code (Anthropic) drafted the beat sheet and narration, wrote the custom scenes in `scenes/`, ran the evidence code, checked claims against `SOURCES.md`, ran the Brutalist pipeline and gates, and fixed layout defects found in visual QC.
- Narration is an AI voice (Kokoro `am_onyx`, local). **It is not a recording of Likhith.**

**What I rejected or corrected:**
- "Experts" are the feed-forward blocks inside each layer, not separate topic-specialist models; the video never claims an expert "knows" a subject.
- Active parameters aren't simply 2/8 of the model, because shared weights always run; the video uses Mixtral's published ~13B instead of a derived ratio.
- "Double the size, double the cost" is shown qualitatively; router scores and token words are illustrative.
- Bar fills darkened for contrast; the verdict gained a sixth, fact-checked line (DeepSeek-V3) so the portrait card fills properly.

**What remains unverified or failed:**
- The required intro "Hi, I am Likhith…" is spoken by the AI narrator; the AI narration is disclosed on screen (opening beat and outro).
- YouTube 4K processing check and the professors' publication decision are pending.

## Reproduce
- **Brutalist version/commit:** nikbearbrown/brutalist.art `6a8380a`.
- **Source commit used for this export:** not committed — `6a8380a` plus local changes: `scenes/MoeExplainer.tsx`, `scenes/JevExplainer.tsx`, `scenes/HaiOutro.tsx` added under `runtime/remotion/src/`, each exported component registered in `Root.tsx` twice: under its own name at 1920×1080, and with a `916` suffix at 1080×1920, and `durationSeconds` hooks added to `ClaudeComposerAsk916`, `BrutalistHesitantWriter916`, `ClaudeVerdictArtifact916`. `type_check.py` is the unmodified toolkit version.
- **Beat sheet and custom scene files:** `beat_sheet.json` (16:9), `vertical/beat_sheet.json` (9:16), `scenes/MoeExplainer.tsx`, `scenes/JevExplainer.tsx`, `scenes/HaiOutro.tsx`.
- **Commands** (toolkit root, Python 3.12 venv, MacTeX on PATH; reel at `youtube/brutalist/claude-hai-mixture-of-experts/`):
  ```bash
  python3 runtime/scripts/generate_audio_kokoro.py <reel>
  python3 runtime/scripts/remotion_scenes.py <reel>
  ./art run <reel>                                              # 16:9 review
  ./art vertical <reel>                                         # then restore vertical/beat_sheet.json from this folder
  python3 runtime/scripts/remotion_scenes.py <reel>/vertical
  ./art final <reel>                                            # 16:9 master (GATE T first)
  ./art final <reel>/vertical --height 3840                     # 9:16 master
  ```
- **Input/source links:** [SOURCES.md](SOURCES.md)
- **Approvals and checks:** [FACTCHECK.md](FACTCHECK.md) (signed off by Likhith), [TYPECHECK.md](TYPECHECK.md) and [vertical/TYPECHECK.md](vertical/TYPECHECK.md) (GATE T PASS), [CHECKS-REPORT.md](CHECKS-REPORT.md), [BUILD-LOG.md](BUILD-LOG.md).

## Watch and review
- **Landscape** — [Watch `landscape/MixtureOfExperts_LikhithR.mp4`](https://drive.google.com/file/d/146cSoc_6OaWLajMeMQ5mjK7P8hXikI7_/view?usp=sharing) — 3840×2160 — 62.7 s — SHA-256 `c70f3c93b54d767c5911d26777dff586bf04b29c1600f194ab8058182f346e52` (final master, `.verified.json` receipt: ready)
- **Vertical** — [Watch `vertical/MixtureOfExperts_LikhithR.mp4`](https://drive.google.com/file/d/120-Qra8qRX85nIsqNY9kqXlF1TjkWODs/view?usp=sharing) — 2160×3840 — 62.7 s — SHA-256 `41bdb836ee1388bde55138853a89184c3ddb68c24764b5ef2a013e91d0638460` (final master, `.verified.json` receipt: ready)
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
