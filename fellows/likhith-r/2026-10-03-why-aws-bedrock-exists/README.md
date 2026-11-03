# Why AWS Bedrock Exists

**Fellow:** Likhith R. · **Week:** 2026-09-28 to 2026-10-04 · **Builder:** `ai-explainer` on `claude-hai` · **Voice:** Kokoro `am_onyx` (AI narration)

A 60-second explainer on Amazon Bedrock: a managed service that gives one API to foundation models from many providers, with no servers to run, so switching models is mostly a change of model ID.

## This week's contribution
- **Question:** If I want an AI model in my app, do I have to run the GPUs myself?
- **Prediction:** I expected Bedrock to be "a model from AWS", and switching providers to mean rewriting the integration.
- **What I built/tried:** 12 beats on running models yourself, per-model APIs, Bedrock as one managed layer, no servers, guardrails and fine-tuning, swapping models by ID, and combining models. The API names and the converse() call shape on screen come from an offline run of the real AWS SDK (`evidence/converse_shape.py`, no AWS call made). Seven custom dual-aspect scenes in `scenes/Bedrock.tsx`.
- **Observed result:** Both cuts render at native 4K (63.8 s). GATE F, L, T (unmodified checker) and V (0 blocker / 0 major) pass on 16:9 and 9:16.
- **Next experiment:** Call two different models through the Converse API on a small real task and note which parameters actually had to change.

## Human and AI work
**My decisions, implementation and verification:**
- Chose the topic and wrote the content brief (the points the beats cover), and set the 12-beat / ~60 s / Kokoro `am_onyx` / native 16:9 + 9:16 constraints.
- Set the branding: @HumanitariansAI channel, "Irreducibly Human" kicker, greetings ("Namaskaram, Likhith" on 16:9, "Hey, Likhith" on 9:16) and the required opening line.
- Watched both the 16:9 and 9:16 cuts, checked each claim in `FACTCHECK.md` against the sources, and approved the final masters.

**AI tools/voices used and what they generated:**
- Claude Code (Anthropic) drafted the beat sheet and narration, wrote the custom scenes in `scenes/`, ran the evidence code, checked claims against `SOURCES.md`, ran the Brutalist pipeline and gates, and fixed layout defects found in visual QC.
- Narration is an AI voice (Kokoro `am_onyx`, local). **It is not a recording of Likhith.**

**What I rejected or corrected:**
- The official name is Amazon Bedrock; "AWS Bedrock" is kept in the narration as common usage.
- "One API" softened: the Converse API is consistent across supported models, but model-specific parameters still exist.
- "No servers" is true for on-demand use, and the verdict says you still pay per use; fine-tuning is noted as supported models only.
- "Humanitarians A I" in the outro changed to "Humanitarians AI" so the voice says it clearly.

**What remains unverified or failed:**
- The required intro "Hi, I am Likhith…" is spoken by the AI narrator; the AI narration is disclosed on screen (opening beat and outro).
- YouTube 4K processing check and the professors' publication decision are pending.

## Reproduce
- **Brutalist version/commit:** nikbearbrown/brutalist.art `a187fab` (Remotion 4.0.535 / React 19).
- **Source commit used for this export:** not committed — `a187fab` plus local changes: `scenes/Bedrock.tsx`, `scenes/JevExplainer.tsx`, `scenes/HaiOutro.tsx` under `runtime/remotion/src/`, each exported component registered in `Root.tsx` twice: under its own name at 1920×1080, and with a `916` suffix at 1080×1920. `type_check.py` is the unmodified toolkit version.
- **Beat sheet and custom scene files:** `beat_sheet.json` (16:9), `vertical/beat_sheet.json` (9:16), `scenes/Bedrock.tsx`, `scenes/JevExplainer.tsx`, `scenes/HaiOutro.tsx`.
- **Commands** (toolkit root, Python 3.12 venv, MacTeX on PATH; reel at `youtube/brutalist/claude-hai-aws-bedrock/`):
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
- **Landscape** — [Watch `landscape/AWSBedrock_LikhithR.mp4`](https://drive.google.com/file/d/18Dg_jwDBVlHofRh__-Fj7wJFvooQIGWy/view?usp=sharing) — 3840×2160 — 63.8 s — SHA-256 `cbabbe1c42f8c8e4ff47934718a2fb297834c22d935bf3b67e5afca0b01a453a` (final master, `.verified.json` receipt: ready)
- **Vertical** — [Watch `vertical/AWSBedrock_LikhithR.mp4`](https://drive.google.com/file/d/1cyE9aTY_gxsksV0QLW05Z5upQzbyUEpX/view?usp=sharing) — 2160×3840 — 63.8 s — SHA-256 `0208315ae71bcf4da913463ba1121da1760f77137fafaea098d5f089ca08bf8b` (final master, `.verified.json` receipt: ready)
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
