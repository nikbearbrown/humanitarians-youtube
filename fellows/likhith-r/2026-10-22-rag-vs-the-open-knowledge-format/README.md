# RAG vs. the Open Knowledge Format

**Fellow:** Likhith R. · **Week:** 2026-10-19 to 2026-10-25 · **Builder:** `ai-explainer` on `claude-hai` · **Voice:** Kokoro `am_onyx` (AI narration)

A 60-second explainer comparing RAG with Google's Open Knowledge Format: RAG searches a pile of documents as vectors on every question, while OKF is a curated folder of linked Markdown that an agent reads directly and that lives in git.

## This week's contribution
- **Question:** How should an AI agent get the knowledge it needs: search it, or read it?
- **Prediction:** I expected OKF to be a RAG replacement that has to be curated entirely by hand.
- **What I built/tried:** 12 beats on RAG as the default, how RAG chunks and searches, what OKF is, search-every-time versus one curated base, reading through index files and links, the curation cost, where RAG still wins, and OKF as maintained knowledge. The similarity scores, the agent's walk through the files and the git history on screen come from a real 5-file OKF bundle and two scripts in `evidence/`. Seven custom dual-aspect scenes in `scenes/RagOkf.tsx`.
- **Observed result:** Both cuts render at native 4K (60.0 s). GATE F, L, T (unmodified checker) and V (0 blocker / 0 major) pass on 16:9 and 9:16.
- **Next experiment:** Convert a small set of my own project docs into an OKF bundle and compare an agent's answers against a RAG index over the same docs.

## Human and AI work
**My decisions, implementation and verification:**
- Chose the topic and wrote the content brief (the points the beats cover), and set the 12-beat / ~60 s / Kokoro `am_onyx` / native 16:9 + 9:16 constraints.
- Set the branding: @HumanitariansAI channel, "Irreducibly Human" kicker, greetings ("Namaskaram, Likhith" on 16:9, "Hey, Likhith" on 9:16) and the required opening line.
- Watched both the 16:9 and 9:16 cuts, checked each claim in `FACTCHECK.md` against the sources, and approved the final masters.

**AI tools/voices used and what they generated:**
- Claude Code (Anthropic) drafted the beat sheet and narration, wrote the custom scenes in `scenes/`, ran the evidence code, checked claims against `SOURCES.md`, ran the Brutalist pipeline and gates, and fixed layout defects found in visual QC.
- Narration is an AI voice (Kokoro `am_onyx`, local). **It is not a recording of Likhith.**

**What I rejected or corrected:**
- "OKF can't auto-generate; someone curates it by hand" corrected: Google's post and the spec say agents can draft and update OKF pages; the real cost is curation and review.
- Google didn't frame OKF as a RAG replacement; the comparison is the video's own, and the verdict calls them different approaches, not a winner.
- "No retrieval step" shown as the agent choosing files through indexes and links, not reading everything; "no embeddings" kept as "not required".
- Versioning stated precisely (v0.1 announced June 2026, v0.2 now); the 2,000,000-document count is labelled illustrative.

**What remains unverified or failed:**
- The required intro "Hi, I am Likhith…" is spoken by the AI narrator; the AI narration is disclosed on screen (opening beat and outro).
- YouTube 4K processing check and the professors' publication decision are pending.

## Reproduce
- **Brutalist version/commit:** nikbearbrown/brutalist.art `a187fab` (Remotion 4.0.535 / React 19).
- **Source commit used for this export:** not committed — `a187fab` plus local changes: `scenes/RagOkf.tsx`, `scenes/JevExplainer.tsx`, `scenes/HaiOutro.tsx` under `runtime/remotion/src/`, each exported component registered in `Root.tsx` twice: under its own name at 1920×1080, and with a `916` suffix at 1080×1920. `type_check.py` is the unmodified toolkit version.
- **Beat sheet and custom scene files:** `beat_sheet.json` (16:9), `vertical/beat_sheet.json` (9:16), `scenes/RagOkf.tsx`, `scenes/JevExplainer.tsx`, `scenes/HaiOutro.tsx`.
- **Commands** (toolkit root, Python 3.12 venv, MacTeX on PATH; reel at `youtube/brutalist/claude-hai-rag-vs-okf/`):
  ```bash
  python3 runtime/scripts/generate_audio_kokoro.py <reel>
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
- **Landscape** — [Watch `landscape/RAGVsOpenKnowledgeFormat_LikhithR.mp4`](https://drive.google.com/file/d/1mPzopR99vEbYIjNYXwZI1j3-6LEjlm0n/view?usp=sharing) — 3840×2160 — 60.0 s — SHA-256 `8cabe7db2d9a3855e4fd2729294fae8893e3e83de6dddb35e7afafc9183a49b6` (final master, `.verified.json` receipt: ready)
- **Vertical** — [Watch `vertical/RAGVsOpenKnowledgeFormat_LikhithR.mp4`](https://drive.google.com/file/d/1QBE2r9ztoK9QI67XpLZQWH8hIIqLN27o/view?usp=sharing) — 2160×3840 — 60.0 s — SHA-256 `0cb32c8356e86b37958240509cc2fd4d900473bc78cc78c38541e0504a43ec61` (final master, `.verified.json` receipt: ready)
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
