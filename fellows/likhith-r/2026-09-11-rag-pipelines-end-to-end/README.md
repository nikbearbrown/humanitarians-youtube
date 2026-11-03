# RAG Pipelines, End to End

**Fellow:** Likhith R. · **Week:** 2026-09-09 to 2026-09-13 · **Builder:** `ai-explainer` on `claude-hai` · **Voice:** Kokoro `am_onyx` (AI narration)

A 60-second explainer on retrieval-augmented generation: instead of retraining a model on your documents, embed and store them as vectors, retrieve the closest chunks for each question, and ground the answer in them.

## This week's contribution
- **Question:** How can an LLM answer questions about documents it was never trained on?
- **Prediction:** I expected the five-step pipeline to map neatly onto the beats, with retrieval as the easy part.
- **What I built/tried:** 12 beats covering eight points I set, as five steps: embed, store, retrieve, augment, generate. The cosine-similarity formula is typeset properly and the similarity scores on screen come from a real script (`evidence/cosine_toy.py`). Seven custom dual-aspect scenes in `scenes/RagPipeline.tsx`.
- **Observed result:** Both cuts render at native 4K (65.9 s). GATE F, L, T (unmodified checker) and V (0/0) pass on 16:9 and 9:16.
- **Next experiment:** Build a small RAG pipeline over a real document set and measure how often retrieval misses the right chunk.

## Human and AI work
**My decisions, implementation and verification:**
- Chose the topic and wrote the content brief (the points the beats cover), and set the 12-beat / ~60 s / Kokoro `am_onyx` / native 16:9 + 9:16 constraints.
- Set the branding: @HumanitariansAI channel, "Irreducibly Human" kicker, and the required opening line.
- Watched both cuts and signed off every claim in `FACTCHECK.md`.

**AI tools/voices used and what they generated:**
- Claude Code (Anthropic) drafted the beat sheet and narration, wrote the custom scenes in `scenes/`, ran the evidence code, checked claims against `SOURCES.md`, ran the Brutalist pipeline and gates, and fixed layout defects found in visual QC.
- Narration is an AI voice (Kokoro `am_onyx`, local). **It is not a recording of Likhith.**

**What I rejected or corrected:**
- "Answer accurately" softened: RAG improves grounding, it doesn't guarantee accuracy. The verdict adds that it is only as good as its retrieval.
- Cosine similarity is named as the common metric, not the only one; the 2-D vectors are labelled as toys (real embeddings have hundreds of dimensions).
- Retraining cost kept qualitative, with no invented figures; documents, chunks and answers on screen are illustrative.
- Portrait layouts redesigned for the 9:16 type floor; greeting changed to "Hey, Likhith".

**What remains unverified or failed:**
- The required intro "Hi, I am Likhith…" is spoken by the AI narrator; the AI narration is disclosed on screen (opening beat and outro).
- YouTube 4K processing check and the professors' publication decision are pending.

## Reproduce
- **Brutalist version/commit:** nikbearbrown/brutalist.art `6a8380a`.
- **Source commit used for this export:** not committed — `6a8380a` plus local changes: `scenes/RagPipeline.tsx`, `scenes/JevExplainer.tsx`, `scenes/HaiOutro.tsx` added under `runtime/remotion/src/`, each exported component registered in `Root.tsx` twice: under its own name at 1920×1080, and with a `916` suffix at 1080×1920, and `durationSeconds` hooks added to `ClaudeComposerAsk916`, `BrutalistHesitantWriter916`, `ClaudeVerdictArtifact916`. `type_check.py` is the unmodified toolkit version.
- **Beat sheet and custom scene files:** `beat_sheet.json` (16:9), `vertical/beat_sheet.json` (9:16), `scenes/RagPipeline.tsx`, `scenes/JevExplainer.tsx`, `scenes/HaiOutro.tsx`.
- **Commands** (toolkit root, Python 3.12 venv, MacTeX on PATH; reel at `youtube/brutalist/claude-hai-rag-pipelines/`):
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
- **Landscape** — [Watch `landscape/RagPipelines_LikhithR.mp4`](https://drive.google.com/file/d/1bmhecBOWpSr87jRvU2nZN--9O2v5EQKK/view?usp=sharing) — 3840×2160 — 65.9 s — SHA-256 `b7bf79be9b005e5ddc6ad1f856fc5f161068f167a84c8d2141cfed59e18bbe1b` (final master, `.verified.json` receipt: ready)
- **Vertical** — [Watch `vertical/RagPipelines_LikhithR.mp4`](https://drive.google.com/file/d/1SYug4iIR2UrcBJieQnkAVLnLj4YSeNYU/view?usp=sharing) — 2160×3840 — 65.9 s — SHA-256 `2823768afc21806c72fe5df1d812b81e9c65c212fc4ab9a1a63e64702ea50845` (final master, `.verified.json` receipt: ready)
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
