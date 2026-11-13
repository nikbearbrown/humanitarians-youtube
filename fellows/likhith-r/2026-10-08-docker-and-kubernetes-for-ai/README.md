# Docker and Kubernetes for AI

**Fellow:** Likhith R. · **Week:** 2026-10-05 to 2026-10-11 · **Builder:** `ai-explainer` on `claude-hai` · **Voice:** Kokoro `am_onyx` (AI narration)

A 60-second explainer on containerization for AI workloads: Docker packages a model with everything it needs so it runs the same anywhere, and Kubernetes runs many copies across machines, adding, replacing and balancing them as demand changes.

## This week's contribution
- **Question:** Why does my model work on my laptop but break in production?
- **Prediction:** I expected containers to make a model run identically everywhere, with Kubernetes just "running Docker" at scale.
- **What I built/tried:** 12 beats on works-on-my-laptop failures, environment drift, Docker images, the limits of one container, Kubernetes orchestration, scaling and self-healing, and how the two fit together. Seven custom dual-aspect scenes in `scenes/DockerK8s.tsx`. Length fitted to exactly 60 seconds.
- **Observed result:** Both cuts render at native 4K (60.0 s). GATE F, L, T (unmodified checker) and V (0 blocker / 0 major) pass on 16:9 and 9:16.
- **Next experiment:** Containerize a small model service and deploy it to a local Kubernetes cluster with an autoscaler, then see what breaks first.

## Human and AI work
**My decisions, implementation and verification:**
- Chose the topic and wrote the content brief (the points the beats cover), and set the 12-beat / ~60 s / Kokoro `am_onyx` / native 16:9 + 9:16 constraints.
- Set the branding: @HumanitariansAI channel, "Irreducibly Human" kicker, greetings ("Namaskaram, Likhith" on 16:9, "Hey, Likhith" on 9:16) and the required opening line.
- Watched both the 16:9 and 9:16 cuts, checked each claim in `FACTCHECK.md` against the sources, and approved the final masters.

**AI tools/voices used and what they generated:**
- Claude Code (Anthropic) drafted the beat sheet and narration, wrote the custom scenes in `scenes/`, checked claims against `SOURCES.md`, ran the Brutalist pipeline and gates, and fixed layout defects found in visual QC.
- Narration is an AI voice (Kokoro `am_onyx`, local). **It is not a recording of Likhith.**

**What I rejected or corrected:**
- "Runs identically anywhere" corrected: a container shares the host kernel, and GPU containers rely on the host's NVIDIA driver; an on-screen note says so.
- Kubernetes runs OCI images through a container runtime and doesn't need the Docker Engine itself; Docker is framed as the packaging step.
- Auto-scaling happens when configured (e.g. a HorizontalPodAutoscaler); the verdict adds that Kubernetes is often overkill for one small model.
- "A I" spelled as "AI" in the narration so the voice says the two letters clearly.

**What remains unverified or failed:**
- The required intro "Hi, I am Likhith…" is spoken by the AI narrator; the AI narration is disclosed on screen (opening beat and outro).
- YouTube 4K processing check and the professors' publication decision are pending.

## Reproduce
- **Brutalist version/commit:** nikbearbrown/brutalist.art `a187fab` (Remotion 4.0.535 / React 19).
- **Source commit used for this export:** not committed — `a187fab` plus local changes: `scenes/DockerK8s.tsx`, `scenes/JevExplainer.tsx`, `scenes/HaiOutro.tsx` under `runtime/remotion/src/`, each exported component registered in `Root.tsx` twice: under its own name at 1920×1080, and with a `916` suffix at 1080×1920. `type_check.py` is the unmodified toolkit version.
- **Beat sheet and custom scene files:** `beat_sheet.json` (16:9), `vertical/beat_sheet.json` (9:16), `scenes/DockerK8s.tsx`, `scenes/JevExplainer.tsx`, `scenes/HaiOutro.tsx`.
- **Commands** (toolkit root, Python 3.12 venv, MacTeX on PATH; reel at `youtube/brutalist/claude-hai-docker-kubernetes/`):
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
- **Landscape** — [Watch `landscape/DockerAndKubernetesForAI_LikhithR.mp4`](https://drive.google.com/file/d/1zq0usog23arKNvgwZs_FjeFiQj0CFyuR/view?usp=sharing) — 3840×2160 — 60.0 s — SHA-256 `399932114eb06143382dc9e33f139bb9ba564fbc1fb93ada21644b305877a09b` (final master, `.verified.json` receipt: ready)
- **Vertical** — [Watch `vertical/DockerAndKubernetesForAI_LikhithR.mp4`](https://drive.google.com/file/d/1gy3LaEHyAwLriSqfzGCYNzEQ0ZXu5GcR/view?usp=sharing) — 2160×3840 — 60.0 s — SHA-256 `ff2565d1f4400525aa3be0c199eb1027c004e38b25ae7a2ad7e07becb4ab61dc` (final master, `.verified.json` receipt: ready)
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
