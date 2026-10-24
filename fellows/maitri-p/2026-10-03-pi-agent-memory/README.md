# Memory Systems for the Pi Agent

**Type:** Project update (planned research)
**Fellow:** Maitri P. · **Voice:** Kokoro `af_bella` (Bella), a synthetic narrator — disclosed on the outro card.

## This week's contribution
A project update on memory systems for the Pi agent harness: what the project studies (external memory for a frozen agent across sessions, no weight changes), how memory is captured, stored and retrieved, prior work it builds on, and the planned evaluation. **No experimental results are claimed — this is the research plan.**

## Human and AI work
**My decisions and verification:** chose the topic and the brief; chose the Bella voice; set the length; approved every change to the shared toolkit; reviewed the rendered cuts.
**AI tools and what they generated:** Claude Code (Anthropic) drafted the beat sheet and narration from my brief, wrote the custom Remotion scenes in `scenes/`, ran the render pipeline and the QC gates. Narration audio is Kokoro (local, free).
**What I rejected or corrected:** see `FRICTIONAL.md`.
**What remains unverified or failed:** see `FACTCHECK.md` and `FRICTIONAL.md`.

## Reproduce
- **Brutalist toolkit:** commit `6fc9987` **plus local uncommitted changes** — new scenes in `scenes/` and Windows fixes in `compile.py` / `remotion_scenes.py` / `type_check.py` / `ClaudeCodeBeat.tsx`. Not yet upstream.
- **Beat sheets:** `beat_sheet.json` (16:9) and `vertical/beat_sheet.json` (9:16 — native portrait layouts, not a crop).
- **Custom scenes:** `scenes/*.tsx` — copy into `runtime/remotion/src/scenes/`, register in `Root.tsx`, then `./art scene-index`.
- **Commands:** `python3 runtime/scripts/generate_audio_kokoro.py <reel>` → `python3 runtime/scripts/remotion_scenes.py <reel>` → `./art final <reel>`; vertical via `./art vertical <reel>`.
- **Checks:** `FACTCHECK.md`, `SHOTLIST.md`, `PROMPTS.md`. Render gates: GATE T passed; GATE V reported 0 blockers on both aspects (remaining warnings are the typing-animation underfill on B01).

## Watch and review
- **Landscape** — `PiAgentMemory_16x9.mp4` — 3840×2160 — 1:29.9 — SHA-256 `74f90f0a414f091e674b0d531e017487ca945cb2732b09e73131d57d3babcd5b`
  Drive: https://drive.google.com/file/d/1XgYX_h-TFXsUqq58dSsjM4PE_9LbPJMY/view?usp=sharing
- **Vertical** — `PiAgentMemory_9x16.mp4` — 2160×3840 — 1:29.9 — SHA-256 `dc648460480b1b15efa7733ecaa54db2792b2bc43b948bdb3de832d9af5c8830`
  Drive: https://drive.google.com/file/d/1zS5pRcoQfu4jmyhTS6UlQ0kCYEnxCTxk/view?usp=sharing
