# RLHF: How Chatbots Learned to Help

**Fellow:** Likhith R. · **Week:** 2026-10-26 to 2026-11-01 · **Builder:** `ai-explainer` on `claude-hai` · **Voice:** Kokoro `am_onyx` (AI narration)

A 60-second explainer on reinforcement learning from human feedback: how a raw model that only continues text becomes an assistant, through example answers, a reward model trained on people's rankings, and RL with a penalty for drifting.

## This week's contribution
- **Question:** How did a model that only predicts the next word learn to be a helpful assistant?
- **Prediction:** I expected RLHF to work like giving the model rules for good behaviour, and I didn't expect a much smaller model to beat GPT-3 just from people's preferences.
- **What I built/tried:** 12 beats: the raw-model problem, pretraining, the three steps (imitate examples, learn a reward model from rankings, RL with a KL penalty), the InstructGPT result, sycophancy and reward hacking, and DPO / Constitutional AI as cheaper follow-ups. A seeded numpy toy (`evidence/rlhf_toy.py`) produces the reward-model agreement, the RL step and the reward-hacking curve on screen. Eight custom dual-aspect scenes in `scenes/RLHF.tsx`.
- **Observed result:** Both cuts render at native 4K (60.0 s). GATE F, L, T (unmodified checker) and V (0 blocker / 0 major) pass on 16:9 and 9:16.
- **Next experiment:** Train a tiny reward model on my own ranked answers and watch where pushing harder on it starts rewarding the wrong thing.

## Human and AI work
**My decisions, implementation and verification:**
- Chose the topic and wrote the content brief (the points the beats cover), and set the 12-beat / ~60 s / Kokoro `am_onyx` / native 16:9 + 9:16 constraints.
- Set the branding: @HumanitariansAI channel, "Irreducibly Human" kicker, greetings ("Namaskaram, Likhith" on 16:9, "Hey, Likhith" on 9:16) and the required opening line.
- Watched both the 16:9 and 9:16 cuts, checked each claim in `FACTCHECK.md` against the sources, and approved the final masters.

**AI tools/voices used and what they generated:**
- Claude Code (Anthropic) drafted the beat sheet and narration, wrote the custom scenes in `scenes/`, wrote and ran the evidence code, checked claims against `SOURCES.md`, ran the Brutalist pipeline and gates, and fixed layout defects found in visual QC.
- Narration is an AI voice (Kokoro `am_onyx`, local). **It is not a recording of Likhith.**

**What I rejected or corrected:**
- The bread-baking hook is labelled illustrative; the InstructGPT paper's own example is a different prompt.
- "A hundred times smaller": 175B / 1.3B is 134.6×, so the screen says "more than 100×".
- "In 2026" was dropped from the closing claim; the voice says preferences still train every major chatbot.
- The people-pleaser cluster in the toy was tuned once so the reward-hacking curve peaks and then falls cleanly; that tuning is logged in the build log.
- Kokoro ran "RLHF" together (Whisper heard "RLE Chef"), so it is now spoken as separate letters.

**What remains unverified or failed:**
- The required intro "Hi, I am Likhith…" is spoken by the AI narrator; the AI narration is disclosed on screen (opening beat and outro).
- The reward-hacking curve is a toy; it shows the shape reported by Gao et al. 2022, not a measurement of a real chatbot.
- YouTube 4K processing check and the professors' publication decision are pending.

## Reproduce
- **Brutalist version/commit:** nikbearbrown/brutalist.art `a187fab` (Remotion 4.0.535 / React 19).
- **Source commit used for this export:** not committed — `a187fab` plus local changes: `RLHF.tsx`, `JevExplainer.tsx`, `HaiOutro.tsx` under `runtime/remotion/src/`, each exported component registered in `Root.tsx` twice: under its own name at 1920×1080, and with a `916` suffix at 1080×1920. `type_check.py` is the unmodified toolkit version.
- **Beat sheet and custom scene files:** `beat_sheet.json` (16:9), `vertical/beat_sheet.json` (9:16), `scenes/RLHF.tsx`, `scenes/JevExplainer.tsx`, `scenes/HaiOutro.tsx`.
- **Commands** (toolkit root, Python 3.12 venv, MacTeX on PATH; reel at `youtube/brutalist/claude-hai-rlhf/`):
  ```bash
  python3 runtime/scripts/generate_audio_kokoro.py <reel> --speed <s>          # speeds used: 1.25 (B00 and B10 at 1.2)
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
- **Landscape** — [Watch `landscape/RLHFHowChatbotsLearnedToHelp_LikhithR.mp4`](https://drive.google.com/file/d/1lXLXzY4oQ50z0bAMgx537mw72Y9boz3D/view?usp=share_link) — 3840×2160 — 60.0 s — SHA-256 `5fdd8ba002c82707a6998d1cd387074bd89ba3b788193f561b5c6de04503828b` (final master, `.verified.json` receipt: ready)
- **Vertical** — [Watch `vertical/RLHFHowChatbotsLearnedToHelp_LikhithR.mp4`](https://drive.google.com/file/d/1DEehENGIIhRoajutDbnKw9GKTeabat_3/view?usp=share_link) — 2160×3840 — 60.0 s — SHA-256 `1accfe397a5e86d14af67d201bb5b7b4ca9e1272f6d6224c06dbf7d1ac78ec63` (final master, `.verified.json` receipt: ready)
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
