# System One Models and Jev

**Fellow:** Likhith R. · **Week:** 2026-09-21 to 2026-09-27 · **Builder:** `ai-explainer` on `claude-hai` · **Voice:** Kokoro `am_onyx` (AI narration)

A 60-second explainer on TypeSafe's Jev, the first "System One" model: instead of generating text token by token, it returns typed, structured decisions in one parallel pass, each with a calibrated confidence score, aimed at the "smart if-statements" inside automated software.

## This week's contribution
- **Question:** What are System One models, and how does TypeSafe's Jev differ from a chat LLM?
- **Prediction:** I expected the vertical version to mostly fall out of the landscape one, and Jev's claims to be simple to state from TypeSafe's launch post.
- **What I built/tried:** 12 beats covering six points I set: the automation hook; sequential strings vs parallel typed outputs; no type errors; TypeSafe's reported 70–500 ms latency and pipeline fit; RLCD-calibrated confidence; the smart if-statement close. Rendered natively in 16:9 and 9:16, with eight custom dual-aspect scenes in `scenes/JevExplainer.tsx`.
- **Observed result:** Both cuts render at native 4K (65.0 s). 16:9 passes GATE F, L and V (0 blocker / 0 major); every 9:16 scene passes GATE V on its own frames.
- **Next experiment:** Test Jev hands-on with a small classification task if early access allows, and compare its confidence scores with how often it is actually right.

## Human and AI work
**My decisions, implementation and verification:**
- Chose the topic and wrote the content brief (the points the beats cover), and set the 12-beat / ~60 s / Kokoro `am_onyx` / native 16:9 + 9:16 constraints.
- Set the branding: on-screen greeting "Namaskaram, Likhith", the @HumanitariansAI channel, and the required opening line.
- Watched both the 16:9 and 9:16 cuts, checked each claim in `FACTCHECK.md` against the sources, and approved the final masters.

**AI tools/voices used and what they generated:**
- Claude Code (Anthropic) drafted the beat sheet and narration, wrote the custom scenes in `scenes/`, checked claims against `SOURCES.md`, ran the Brutalist pipeline and gates, and fixed layout defects found in visual QC.
- Narration is an AI voice (Kokoro `am_onyx`, local). **It is not a recording of Likhith.**

**What I rejected or corrected:**
- Did not use the "never hallucinates" claim from secondary coverage; the video says what TypeSafe says (no type errors) and adds "typed is not the same as right".
- The 70–500 ms figure is attributed to TypeSafe; the LLM side says "often seconds" with no invented number; example values are labelled illustrative.
- The stock outro filled 8% of the frame (GATE V fail), so a Humanitarians AI outro with the full-size mark replaced it.
- Portrait layout defects fixed after visual QC (B01 fill, B04 edge, B08 threshold label, title/pill collision).

**What remains unverified or failed:**
- The required intro "Hi, I am Likhith…" is spoken by the AI narrator; the AI narration is disclosed on screen (opening beat and outro).
- YouTube 4K processing check and the professors' publication decision are pending.

## Reproduce
- **Brutalist version/commit and date checked:** nikbearbrown/brutalist.art `6a8380a` (2026-09-20), checked 2026-09-26.
- **Source commit used for this export:** not committed — `6a8380a` plus local changes: `scenes/JevExplainer.tsx`, `scenes/HaiOutro.tsx` added under `runtime/remotion/src/`, each exported component registered in `Root.tsx` twice: under its own name at 1920×1080, and with a `916` suffix at 1080×1920, and `durationSeconds` hooks added to `ClaudeComposerAsk916`, `BrutalistHesitantWriter916`, `ClaudeVerdictArtifact916`.
- **Beat sheet and custom scene files:** `beat_sheet.json` (16:9), `vertical/beat_sheet.json` (9:16), `scenes/JevExplainer.tsx`.
- **Commands** (toolkit root, Python 3.12 venv, MacTeX on PATH; reel at `youtube/brutalist/claude-hai-system-one-jev/`):
  ```bash
  python3 runtime/scripts/generate_audio_kokoro.py <reel>
  python3 runtime/scripts/remotion_scenes.py <reel>
  ./art run <reel>                                              # 16:9
  ./art vertical <reel>                                         # then restore vertical/beat_sheet.json from this folder
  python3 runtime/scripts/remotion_scenes.py <reel>/vertical
  python3 runtime/scripts/compile.py <reel>/vertical --review --height 3840
  ./art final <reel>                                            # 16:9 master (GATE T first)
  ./art final <reel>/vertical --height 3840                     # 9:16 master
  ```
- **Input/source links:** [SOURCES.md](SOURCES.md)
- **Approvals and checks:** [FACTCHECK.md](FACTCHECK.md) (signed off by Likhith), [TYPECHECK.md](TYPECHECK.md) and [vertical/TYPECHECK.md](vertical/TYPECHECK.md) (GATE T PASS), [CHECKS-REPORT.md](CHECKS-REPORT.md), [BUILD-LOG.md](BUILD-LOG.md).

## Watch and review
- **Landscape** — [Watch `landscape/SystemOneJev_LikhithR.mp4`](https://drive.google.com/file/d/1nxV_JQcHsPwBnky3fB3ENPdZzyK9q4Cf/view?usp=sharing) — 3840×2160 — 65.0 s — SHA-256 `55a99873422352870b60c66d892cc289044bf8d572e67b1df6e54256e4916eb0` (final master, `.verified.json` receipt: ready)
- **Vertical** — [Watch `vertical/SystemOneJev_LikhithR.mp4`](https://drive.google.com/file/d/1OZtmR40iJ4lzRANqn3Ah3NmRsVekl4BJ/view?usp=sharing) — 2160×3840 — 65.0 s — SHA-256 `3f7399d39876d0dc846d888f83751b72ef8d2adb7cc3c32fc7343fb0c1eb985e` (final master, `.verified.json` receipt: ready)
- Sources/large assets Drive link: none
- PM review status: pending
- YouTube 4K processing check: pending upload
- Professors' publication decision: pending

## Folder contents
- `README.md` — this report · `FRICTIONAL.md` — process log · `description.txt` — video description
- `beat_sheet.json` / `vertical/beat_sheet.json` — 16:9 / 9:16 production plans · `SCRIPT.md` — narration
- `SOURCES.md`, `FACTCHECK.md`, `SHOTLIST.md`, `PROMPTS.md`, `CHECKS-REPORT.md`, `BUILD-LOG.md`, `TYPECHECK.md` (+ `vertical/TYPECHECK.md`) — sources, claims, shots, prompts, pre-render checks, build record, type-lock gate
- `scenes/` — custom Remotion scene code
