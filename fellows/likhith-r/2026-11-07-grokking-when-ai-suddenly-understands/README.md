# Grokking: When AI Suddenly Understands

**Fellow:** Likhith R. · **Week:** 2026-11-02 to 2026-11-08 · **Builder:** `ai-explainer` on `claude-hai` · **Voice:** Kokoro `am_onyx` (AI narration)

A 60-second explainer on grokking: a small network memorizes its training table almost at once, scores near zero on new problems, and then, many steps later, suddenly generalizes. Every curve on screen comes from my own numpy re-run of the (a + b) mod 97 experiment.

## This week's contribution
- **Question:** Can a model that looks stuck still be learning?
- **Prediction:** I expected a small numpy re-run to be unlikely to grok at all, and I thought the jump would need the 97-number modulus to be made smaller or the run to be much longer.
- **What I built/tried:** 12 beats: the hook, the 2022 OpenAI setup, memorizing first, the late jump on a log-scale axis, why weight decay pushes the model from a lookup table to a rule, Nanda et al.'s finding that it adds with waves, what a flat curve can hide, and where the word comes from. The curves come from `evidence/grok_toy.py`: train 100 % at step 263, test 99 % at step 5,299 (about 20× later), and a control without weight decay that never generalizes. Eight custom dual-aspect scenes in `scenes/Grokking.tsx`, reading numbers only from the generated `scenes/grokkingData.ts`.
- **Observed result:** Both cuts render at native 4K (60.0 s). GATE F, L, T (unmodified checker) and V (0 blocker / 0 major) pass on 16:9 and 9:16.
- **Next experiment:** Change the share of the table the model sees (20 %, 40 %, 60 %) and see how the delay before the jump changes.

## Human and AI work
**My decisions, implementation and verification:**
- Chose the topic and wrote the content brief (the points the beats cover), and set the 12-beat / ~60 s / Kokoro `am_onyx` / native 16:9 + 9:16 constraints.
- Set the branding: @HumanitariansAI channel, "Irreducibly Human" kicker, greetings ("Namaskaram, Likhith" on 16:9, "Hey, Likhith" on 9:16) and the required opening line.
- Watched both the 16:9 and 9:16 cuts, checked each claim in `FACTCHECK.md` against the sources, and approved the final masters.

**AI tools/voices used and what they generated:**
- Claude Code (Anthropic) drafted the beat sheet and narration, wrote the custom scenes in `scenes/`, wrote and ran the evidence code, checked claims against `SOURCES.md`, ran the Brutalist pipeline and gates, and fixed layout defects found in visual QC.
- Narration is an AI voice (Kokoro `am_onyx`, local). **It is not a recording of Likhith.**

**What I rejected or corrected:**
- The run grokked on the first full attempt at mod 97; the hyperparameters were fixed before that run and never tuned against the result.
- "Many times more steps" is shown as "≈ 20× more steps", from our run (5,299 / 263), not the paper's numbers.
- The weight-decay explanation is stated as the field's account (Nanda et al. 2023, Varma et al. 2023), shown next to our own no-decay control.
- The first render's opening beat was too short for the AI-narration disclosure to appear, so beats were re-timed until it shows.
- "Weight decay" slurred to "Wait the K" at the faster voice speed, so that beat stays at 1.2.

**What remains unverified or failed:**
- The required intro "Hi, I am Likhith…" is spoken by the AI narrator; the AI narration is disclosed on screen (opening beat and outro).
- Our model is a small MLP, not the paper's transformer, and the spectrum on screen is from our run (Nanda et al. used mod 113).
- YouTube 4K processing check and the professors' publication decision are pending.

## Reproduce
- **Brutalist version/commit:** nikbearbrown/brutalist.art `a187fab` (Remotion 4.0.535 / React 19).
- **Source commit used for this export:** not committed — `a187fab` plus local changes: `Grokking.tsx`, `grokkingData.ts`, `JevExplainer.tsx`, `HaiOutro.tsx` under `runtime/remotion/src/`, each exported component registered in `Root.tsx` twice: under its own name at 1920×1080, and with a `916` suffix at 1080×1920. `type_check.py` is the unmodified toolkit version.
- **Beat sheet and custom scene files:** `beat_sheet.json` (16:9), `vertical/beat_sheet.json` (9:16), `scenes/Grokking.tsx`, `scenes/grokkingData.ts`, `scenes/JevExplainer.tsx`, `scenes/HaiOutro.tsx`.
- **Commands** (toolkit root, Python 3.12 venv, MacTeX on PATH; reel at `youtube/brutalist/claude-hai-grokking/`):
  ```bash
  python3 runtime/scripts/generate_audio_kokoro.py <reel> --speed <s>          # speeds used: 1.25 (B00, B01, B06 and B10 at 1.2)
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
- **Landscape** — [Watch `landscape/GrokkingWhenAISuddenlyUnderstands_LikhithR.mp4`](https://drive.google.com/file/d/1-aJOER_AViEJDddvJob7kbRyhnTlDTtt/view?usp=share_link) — 3840×2160 — 60.0 s — SHA-256 `eb2cd1fa5e171c95c57831b63146fd5d29095091c0eafd66e081875d59a432d3` (final master, `.verified.json` receipt: ready)
- **Vertical** — [Watch `vertical/GrokkingWhenAISuddenlyUnderstands_LikhithR.mp4`](https://drive.google.com/file/d/1d0hM2gL0w8hH0hkokvc97maLnv3MHTLM/view?usp=share_link) — 2160×3840 — 60.0 s — SHA-256 `2fa3b9d4f29e8262bfca5ea4fd20c0b72206f3dd8f47e69185a4dca257aca890` (final master, `.verified.json` receipt: ready)
- Sources/large assets Drive link: none
- PM review status: pending
- YouTube 4K processing check: pending upload
- Professors' publication decision: pending

## Folder contents
- `README.md` — this report · `FRICTIONAL.md` — process log · `description.txt` — video description
- `beat_sheet.json` / `vertical/beat_sheet.json` — 16:9 / 9:16 production plans · `SCRIPT.md` — narration
- `SOURCES.md`, `FACTCHECK.md`, `SHOTLIST.md`, `PROMPTS.md`, `CHECKS-REPORT.md`, `BUILD-LOG.md`, `TYPECHECK.md` (+ `vertical/TYPECHECK.md`) — sources, claims, shots, prompts, pre-render checks, build record, type-lock gate
- `BUILD-PROMPT.md` — the build prompt
- `scenes/` — custom Remotion scene code (`JevExplainer.tsx` holds the shared stage helpers; `HaiOutro.tsx` is the outro; `grokkingData.ts` is generated from the evidence run)
- `evidence/` — the executed code and its real output shown on screen
