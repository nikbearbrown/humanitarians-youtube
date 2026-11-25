# Word2Vec: King − Man + Woman ≈ Queen

**Fellow:** Likhith R. · **Week:** 2026-11-09 to 2026-11-15 · **Builder:** `ai-explainer` on `claude-hai` · **Voice:** Kokoro `am_onyx` (AI narration)

A 60-second explainer on Word2Vec: how predicting a word's neighbours turns every word into 300 numbers, so that similar words land close together and relationships like man → woman and king → queen become directions, including the catch in the famous analogy and the bias the vectors learn from us.

## This week's contribution
- **Question:** How did a computer work out that king − man + woman is close to queen, without being told what any word means?
- **Prediction:** I expected a small skip-gram on a toy corpus to reproduce king − man + woman = queen cleanly, and I didn't know the famous result depends on excluding the input words.
- **What I built/tried:** 12 beats: the analogy hook, words as ID numbers, Firth's "company it keeps", Mikolov's 2013 skip-gram, meaning as geometry, the catch (inputs excluded) and the 2016 bias finding, embeddings in today's models, and the close. Every toy number comes from `evidence/w2v_toy.py`, a numpy skip-gram with negative sampling on a built-in 30,000-sentence corpus. Eight custom dual-aspect scenes in `scenes/Word2Vec.tsx`, reading numbers only from `scenes/word2vecData.ts`.
- **Observed result:** Both cuts render at native 4K (60.0 s). GATE F, L, T (unmodified checker) and V (0 blocker / 0 major) pass on 16:9 and 9:16.
- **Next experiment:** Train the same toy on real text from one field and look for words that share company but mean different things.

## Human and AI work
**My decisions, implementation and verification:**
- Chose the topic and wrote the content brief (the points the beats cover), and set the 12-beat / ~60 s / Kokoro `am_onyx` / native 16:9 + 9:16 constraints.
- Set the branding: @HumanitariansAI channel, "Irreducibly Human" kicker, greetings ("Namaskaram, Likhith" on 16:9, "Hey, Likhith" on 9:16) and the required opening line.
- Watched both the 16:9 and 9:16 cuts, checked each claim in `FACTCHECK.md` against the sources, and approved the final masters.

**AI tools/voices used and what they generated:**
- Claude Code (Anthropic) drafted the beat sheet and narration, wrote the custom scenes in `scenes/`, wrote and ran the evidence code, checked claims against `SOURCES.md`, ran the Brutalist pipeline and gates, and fixed layout defects found in visual QC.
- Narration is an AI voice (Kokoro `am_onyx`, local). **It is not a recording of Likhith.**

**What I rejected or corrected:**
- The toy corpus was revised twice (v1 made king and prince identical; v2 still failed the place analogy). Every version's output is kept in `evidence/`, and a sweep (`evidence/sweep/SWEEP.md`) shows how the result depends on one corpus setting. Training settings never changed.
- In our toy, "king" edges out "queen" (0.710 vs 0.709) when the input words are included; the video says so instead of hiding it.
- "Man to woman roughly matches king to queen": "roughly" is deliberate, because the two steps line up at only 0.406 in the toy.
- Modern models learn their own vectors for word pieces; a small on-screen note says so, instead of implying Word2Vec is inside ChatGPT or Claude.
- "Programmer as" kept being heard as "program her as", so the line uses the paper's own "computer programmer".
- Firth's line is quoted word for word; the printed original ends with "!", and the screen uses a period.

**What remains unverified or failed:**
- The required intro "Hi, I am Likhith…" is spoken by the AI narrator; the AI narration is disclosed on screen (opening beat and outro).
- The toy is a template corpus with 173 words, not Google News; it shows the mechanism, not the published vectors' exact similarities.
- YouTube 4K processing check and the professors' publication decision are pending.

## Reproduce
- **Brutalist version/commit:** nikbearbrown/brutalist.art `a187fab` (Remotion 4.0.535 / React 19).
- **Source commit used for this export:** not committed — `a187fab` plus local changes: `Word2Vec.tsx`, `word2vecData.ts`, `JevExplainer.tsx`, `HaiOutro.tsx` under `runtime/remotion/src/`, each exported component registered in `Root.tsx` twice: under its own name at 1920×1080, and with a `916` suffix at 1080×1920. `type_check.py` is the unmodified toolkit version.
- **Beat sheet and custom scene files:** `beat_sheet.json` (16:9), `vertical/beat_sheet.json` (9:16), `scenes/Word2Vec.tsx`, `scenes/word2vecData.ts`, `scenes/JevExplainer.tsx`, `scenes/HaiOutro.tsx`.
- **Commands** (toolkit root, Python 3.12 venv, MacTeX on PATH; reel at `youtube/brutalist/claude-hai-word2vec/`):
  ```bash
  python3 runtime/scripts/generate_audio_kokoro.py <reel> --sheet <reel>/beat_sheet.tts.json --speed <s>   # tts sheet = spoken_as applied (evidence/tts_sheet.py in the toolkit reel); speeds used: 1.25 (B00, B01, B10 and B11 at 1.2)
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
- **Landscape** — [Watch `landscape/Word2VecKingManWomanQueen_LikhithR.mp4`](https://drive.google.com/file/d/1I6bNxCQ-uZnvLlhDFPVvGHEwdcp-xK5W/view?usp=share_link) — 3840×2160 — 60.0 s — SHA-256 `cbbdf3e0c6165e131eaac8a599fab2cf7bcc82898be63e42824d697c53ea9aec` (final master, `.verified.json` receipt: ready)
- **Vertical** — [Watch `vertical/Word2VecKingManWomanQueen_LikhithR.mp4`](https://drive.google.com/file/d/11cYFzWoyqtX5pDjEwDdjXSvFuDhDdnEe/view?usp=share_link) — 2160×3840 — 60.0 s — SHA-256 `6729e09776d715fefd42e01b664f6696a5a13665081a86de97cdfbf21fab1caa` (final master, `.verified.json` receipt: ready)
- Sources/large assets Drive link: none
- PM review status: pending
- YouTube 4K processing check: pending upload
- Professors' publication decision: pending

## Folder contents
- `README.md` — this report · `FRICTIONAL.md` — process log · `description.txt` — video description
- `beat_sheet.json` / `vertical/beat_sheet.json` — 16:9 / 9:16 production plans · `SCRIPT.md` — narration
- `SOURCES.md`, `FACTCHECK.md`, `SHOTLIST.md`, `PROMPTS.md`, `CHECKS-REPORT.md`, `BUILD-LOG.md`, `TYPECHECK.md` (+ `vertical/TYPECHECK.md`) — sources, claims, shots, prompts, pre-render checks, build record, type-lock gate
- `BUILD-PROMPT.md` — the build prompt
- `scenes/` — custom Remotion scene code (`JevExplainer.tsx` holds the shared stage helpers; `HaiOutro.tsx` is the outro; `word2vecData.ts` is generated from the evidence run)
- `evidence/` — the executed code and its real output shown on screen
