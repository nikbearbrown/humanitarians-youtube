# Higgsfield and Claude: Directing AI Video

**Fellow:** Likhith R. · **Week:** 2026-11-02 to 2026-11-08 · **Builder:** `ai-explainer` on `claude-hai` · **Voice:** Kokoro `am_onyx` (AI narration)

A 60-second explainer on Higgsfield AI and how it pairs with Claude Fable: Claude plans the script, shots and prompts and checks each clip, while Higgsfield's video models generate the shots, connected through Higgsfield's official MCP connector or its CLI.

## This week's contribution
- **Question:** How does a chatbot end up directing an animated film?
- **Prediction:** I expected Claude to be generating the video itself, and I took the Voyager demo and the "native 4K" and "15-second clip" figures at face value.
- **What I built/tried:** 12 beats: the one-prompt hook, what Higgsfield gathers in one place, how Claude connects (connector, CLI and skills), who does what, why clips are planned and stitched, Higgsfield's Voyager demo, the limits (paid credits, character drift, labelling), and the shift from operating the camera to directing. All diagrams are rebuilt natively; no Higgsfield account, tool or credit was used. Eight custom dual-aspect scenes in `scenes/Higgsfield.tsx`, with a new Higgsfield logo set in the toolkit's logo library.
- **Observed result:** Both cuts render at native 4K (60.0 s). GATE F, L, T (unmodified checker) and V (0 blocker / 0 major) pass on 16:9 and 9:16.
- **Next experiment:** Plan a six-shot film with Claude for free, then decide which shots would be worth generating if I ever had credits.

## Human and AI work
**My decisions, implementation and verification:**
- Chose the topic and wrote the content brief (the points the beats cover), and set the 12-beat / ~60 s / Kokoro `am_onyx` / native 16:9 + 9:16 constraints.
- Set the branding: @HumanitariansAI channel, "Irreducibly Human" kicker, greetings ("Namaskaram, Likhith" on 16:9, "Hey, Likhith" on 9:16) and the required opening line.
- Watched both the 16:9 and 9:16 cuts, checked each claim in `FACTCHECK.md` against the sources, and approved the final masters.

**AI tools/voices used and what they generated:**
- Claude Code (Anthropic) drafted the beat sheet and narration, wrote the custom scenes in `scenes/`, checked claims against `SOURCES.md`, ran the Brutalist pipeline and gates, and fixed layout defects found in visual QC.
- Narration is an AI voice (Kokoro `am_onyx`, local). **It is not a recording of Likhith.**

**What I rejected or corrected:**
- "A few minutes later" → "then": the timing in the hook is illustrative.
- "Native 4K" → "up to 4K on some tools": 4K is only claimed for some Higgsfield tools.
- "OAuth" → "sign in"; "~15 s cap" → "clips are short" (15 s is an April changelog figure, later models reach 30 s).
- The Voyager piece is Higgsfield's own demo, so it is called a "one-minute film", not a documentary, and captioned "Redrawn from Higgsfield's demo". Sora was dropped from the model list.

**What remains unverified or failed:**
- The required intro "Hi, I am Likhith…" is spoken by the AI narrator; the AI narration is disclosed on screen (opening beat and outro).
- Higgsfield's demo and most of its claims come from Higgsfield itself (marketing sources); I didn't run the pipeline, by design, to avoid spending credits.
- The Voyager demo was read through a mirror because x.com returned 402.
- YouTube 4K processing check and the professors' publication decision are pending.

## Reproduce
- **Brutalist version/commit:** nikbearbrown/brutalist.art `a187fab` (Remotion 4.0.535 / React 19).
- **Source commit used for this export:** not committed — `a187fab` plus local changes: `Higgsfield.tsx`, `JevExplainer.tsx`, `HaiOutro.tsx` under `runtime/remotion/src/`, each exported component registered in `Root.tsx` twice: under its own name at 1920×1080, and with a `916` suffix at 1080×1920. `type_check.py` is the unmodified toolkit version.
- **Beat sheet and custom scene files:** `beat_sheet.json` (16:9), `vertical/beat_sheet.json` (9:16), `scenes/Higgsfield.tsx`, `scenes/JevExplainer.tsx`, `scenes/HaiOutro.tsx`.
- **Commands** (toolkit root, Python 3.12 venv, MacTeX on PATH; reel at `youtube/brutalist/claude-hai-higgsfield/`):
  ```bash
  python3 runtime/scripts/generate_audio_kokoro.py <reel> --speed <s>          # speeds used: 1.25 (B00 and B10 at 1.2)
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
- **Landscape** — [Watch `landscape/HiggsfieldAndClaudeDirectingAIVideo_LikhithR.mp4`](https://drive.google.com/file/d/131A4cSMZXkNWo1lBTwOzSHQ01VLNDDCa/view?usp=share_link) — 3840×2160 — 60.0 s — SHA-256 `6e561418404b6044f6f21343db4a64f7fa52b81daf1873c6b17bc95ff98ca58f` (final master, `.verified.json` receipt: ready)
- **Vertical** — [Watch `vertical/HiggsfieldAndClaudeDirectingAIVideo_LikhithR.mp4`](https://drive.google.com/file/d/19mlOYeWVJAZ8OlY6StJGMMp9siL_agFD/view?usp=share_link) — 2160×3840 — 60.0 s — SHA-256 `282ea27cf20a6f9c0fd3cb1ca54bb434c79f67f581322a21f45064b9403c8e0b` (final master, `.verified.json` receipt: ready)
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
