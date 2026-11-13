# Microduck and Sim-to-Real Training

**Fellow:** Likhith R. · **Week:** 2026-10-19 to 2026-10-25 · **Builder:** `ai-explainer` on `claude-hai` · **Voice:** Kokoro `am_onyx` (AI narration)

A 60-second explainer on Microduck, Pollen Robotics and Hugging Face's $399 open-source biped, and on sim-to-real training: the robot learns to walk in a physics simulation where thousands of copies practise and fall at no cost, then the policy is loaded onto the real motors.

## This week's contribution
- **Question:** How do you teach a tiny robot duck to walk, sit and nap?
- **Prediction:** I expected the story to be that simulation now transfers to real robots cleanly, and that Isaac Lab was the one way Microduck is trained.
- **What I built/tried:** 12 beats on the GTC Berlin keynote moment, Microduck's specs, what sim-to-real means, thousands of parallel simulated copies, exporting the policy to the real motors, why falls in sim are free, the on-stage fall, and sim-first as the emerging standard. The fall counts on screen come from a seeded toy run (`evidence/sim_to_real_toy.py`), labelled as such. Seven custom dual-aspect scenes in `scenes/MicroduckSim.tsx`, including a drawn duck that walks, sits and falls.
- **Observed result:** Both cuts render at native 4K (60.0 s). GATE F, L, T (unmodified checker) and V (0 blocker / 0 major) pass on 16:9 and 9:16.
- **Next experiment:** Run the public Microduck training stack in simulation and see which behaviours transfer and which don't.

## Human and AI work
**My decisions, implementation and verification:**
- Chose the topic and wrote the content brief (the points the beats cover), and set the 12-beat / ~60 s / Kokoro `am_onyx` / native 16:9 + 9:16 constraints.
- Set the branding: @HumanitariansAI channel, "Irreducibly Human" kicker, greetings ("Namaskaram, Likhith" on 16:9, "Hey, Likhith" on 9:16) and the required opening line.
- Watched both the 16:9 and 9:16 cuts, checked each claim in `FACTCHECK.md` against the sources, and approved the final masters.

**AI tools/voices used and what they generated:**
- Claude Code (Anthropic) drafted the beat sheet and narration, wrote the custom scenes in `scenes/`, ran the evidence code, checked claims against `SOURCES.md`, ran the Brutalist pipeline and gates, and fixed layout defects found in visual QC.
- Narration is an AI voice (Kokoro `am_onyx`, local). **It is not a recording of Likhith.**

**What I rejected or corrected:**
- "Traversing obstacles" corrected: the published recipe trains on flat ground, slopes, stairs, rough terrain and shoves; obstacle avoidance isn't described.
- Isaac Lab is the joint NVIDIA and Pollen path; Pollen's own default stack trains in MuJoCo, and the video doesn't claim Isaac Lab is the only way.
- On stage, 3 of 4 ducks fell when told to nap; the causes aren't known, so the video lists typical sim-to-real gap sources, not a diagnosis.
- "Becoming the standard", not "is the standard"; a toy "real transfer" result showed no meaningful gap and was removed rather than tuned.

**What remains unverified or failed:**
- The required intro "Hi, I am Likhith…" is spoken by the AI narrator; the AI narration is disclosed on screen (opening beat and outro).
- YouTube 4K processing check and the professors' publication decision are pending.

## Reproduce
- **Brutalist version/commit:** nikbearbrown/brutalist.art `a187fab` (Remotion 4.0.535 / React 19).
- **Source commit used for this export:** not committed — `a187fab` plus local changes: `scenes/MicroduckSim.tsx`, `scenes/JevExplainer.tsx`, `scenes/HaiOutro.tsx` under `runtime/remotion/src/`, each exported component registered in `Root.tsx` twice: under its own name at 1920×1080, and with a `916` suffix at 1080×1920. `type_check.py` is the unmodified toolkit version.
- **Beat sheet and custom scene files:** `beat_sheet.json` (16:9), `vertical/beat_sheet.json` (9:16), `scenes/MicroduckSim.tsx`, `scenes/JevExplainer.tsx`, `scenes/HaiOutro.tsx`.
- **Commands** (toolkit root, Python 3.12 venv, MacTeX on PATH; reel at `youtube/brutalist/claude-hai-microduck-sim-to-real/`):
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
- **Landscape** — [Watch `landscape/MicroduckSimToRealTraining_LikhithR.mp4`](https://drive.google.com/file/d/1Gfiez-yE_ONzBWlehFNAOv1gmIBuzP2j/view?usp=sharing) — 3840×2160 — 60.0 s — SHA-256 `c4c7a14d9ef9fb0444118fe90dabd7f2e5c0618ee2f3ca53b3c715eb5dae9259` (final master, `.verified.json` receipt: ready)
- **Vertical** — [Watch `vertical/MicroduckSimToRealTraining_LikhithR.mp4`](https://drive.google.com/file/d/1EPt_4CdZ7KpsNmj8V4RXvdl0h5BZN_r7/view?usp=sharing) — 2160×3840 — 60.0 s — SHA-256 `3058c41af48fa75f46ea617a71cea9b0a998bf23f09ecba9939237d857a3fc52` (final master, `.verified.json` receipt: ready)
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
