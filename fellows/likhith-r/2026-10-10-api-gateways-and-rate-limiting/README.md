# API Gateways and Rate Limiting

**Fellow:** Likhith R. · **Week:** 2026-10-05 to 2026-10-11 · **Builder:** `ai-explainer` on `claude-hai` · **Voice:** Kokoro `am_onyx` (AI narration)

A 60-second explainer on API gateways and rate limiting: one entry point in front of many services handles auth, routing and logging once, and rate limits (token bucket, sliding window) stop any one client from draining shared capacity.

## This week's contribution
- **Question:** How do API gateways and rate limiting protect backend services?
- **Prediction:** I expected rate limiting to mean a hard block at a fixed count, and the two algorithms to differ only slightly.
- **What I built/tried:** 12 beats on duplicated protection across services, the gateway as one front door, its pipeline, rate limiting and 429 responses, token bucket, fixed versus sliding windows, and per-user quotas for AI APIs. Every on-screen outcome is reproduced by `evidence/rate_limit_toy.py`. Seven custom dual-aspect scenes in `scenes/ApiGateway.tsx`. Length fitted to exactly 60 seconds.
- **Observed result:** Both cuts render at native 4K (60.0 s). GATE F, L, T (unmodified checker) and V (0 blocker / 0 major) pass on 16:9 and 9:16.
- **Next experiment:** Add a token-bucket limiter in front of a small API and test how it behaves under a burst versus a sustained flood.

## Human and AI work
**My decisions, implementation and verification:**
- Chose the topic and wrote the content brief (the points the beats cover), and set the 12-beat / ~60 s / Kokoro `am_onyx` / native 16:9 + 9:16 constraints.
- Set the branding: @HumanitariansAI channel, "Irreducibly Human" kicker, greetings ("Namaskaram, Likhith" on 16:9, "Hey, Likhith" on 9:16) and the required opening line.
- Watched both the 16:9 and 9:16 cuts, checked each claim in `FACTCHECK.md` against the sources, and approved the final masters.

**AI tools/voices used and what they generated:**
- Claude Code (Anthropic) drafted the beat sheet and narration, wrote the custom scenes in `scenes/`, ran the evidence code, checked claims against `SOURCES.md`, ran the Brutalist pipeline and gates, and fixed layout defects found in visual QC.
- Narration is an AI voice (Kokoro `am_onyx`, local). **It is not a recording of Likhith.**

**What I rejected or corrected:**
- "Smooth out bursts rather than hard-blocking" sharpened: a token bucket allows short bursts up to its size, then holds clients to the refill rate.
- The fixed window is shown only as the problem the sliding window fixes.
- Real model APIs limit requests and tokens per minute; stated on screen instead of implying requests alone. All limits and traffic are illustrative.
- The 9:16 master was built after the 16:9 one; both now carry the same "Narrated by an AI voice." disclosure.

**What remains unverified or failed:**
- The required intro "Hi, I am Likhith…" is spoken by the AI narrator; the AI narration is disclosed on screen (opening beat and outro).
- YouTube 4K processing check and the professors' publication decision are pending.

## Reproduce
- **Brutalist version/commit:** nikbearbrown/brutalist.art `a187fab` (Remotion 4.0.535 / React 19).
- **Source commit used for this export:** not committed — `a187fab` plus local changes: `scenes/ApiGateway.tsx`, `scenes/JevExplainer.tsx`, `scenes/HaiOutro.tsx` under `runtime/remotion/src/`, each exported component registered in `Root.tsx` twice: under its own name at 1920×1080, and with a `916` suffix at 1080×1920. `type_check.py` is the unmodified toolkit version.
- **Beat sheet and custom scene files:** `beat_sheet.json` (16:9), `vertical/beat_sheet.json` (9:16), `scenes/ApiGateway.tsx`, `scenes/JevExplainer.tsx`, `scenes/HaiOutro.tsx`.
- **Commands** (toolkit root, Python 3.12 venv, MacTeX on PATH; reel at `youtube/brutalist/claude-hai-api-gateways/`):
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
- **Landscape** — [Watch `landscape/APIGatewaysAndRateLimiting_LikhithR.mp4`](https://drive.google.com/file/d/1qvLMdCVmZMtWk62elR9KDkrwJbkjMvNu/view?usp=sharing) — 3840×2160 — 60.0 s — SHA-256 `a0b32681a5ec440d6486a1a7debef220c89969025d88bf7488f040c9b70622cb` (final master, `.verified.json` receipt: ready)
- **Vertical** — [Watch `vertical/APIGatewaysAndRateLimiting_LikhithR.mp4`](https://drive.google.com/file/d/1MWy08GnwiHBl9dcZH8hre_m9s5HbZfkw/view?usp=sharing) — 2160×3840 — 60.0 s — SHA-256 `0443d30c002e58fb05b969ed22ccb1c127da0d38a703534697d64844e08218b0` (final master, `.verified.json` receipt: ready)
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
