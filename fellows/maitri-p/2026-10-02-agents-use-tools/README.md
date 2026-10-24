# How AI Agents Actually Use Tools

**Type:** STEM/AI explainer
**Fellow:** Maitri P. · **Voice:** Kokoro `af_bella` (Bella), a synthetic narrator — disclosed on the outro card.

## This week's contribution
An explainer on how an AI agent goes beyond a plain LLM: a runtime exposes tools, the model requests one, the runtime executes it, and the observation returns as text. Includes a real local worked example (largest file in a repository) and the reliability arithmetic that explains why agents check their results.

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
- **Checks:** `FACTCHECK.md`, `SHOTLIST.md`, `PROMPTS.md`, `CHECKS-REPORT.md`. Render gates: GATE T passed; GATE V reported 0 blockers on both aspects (remaining warnings are the typing-animation underfill on B01).

## Watch and review
- **Landscape** — `AgentsUseTools_MaitriP.mp4`
  [Drive](https://drive.google.com/file/d/19FrfNUM_zKFsz20cABHxEAez9aASpRPz/view?usp=sharing)
- **Vertical** — `AgentsUseTools_Maitri-9x16.mp4`
  [Drive](https://drive.google.com/file/d/1GvPz8WNdgz0eTSJylaz83x3MkBFSzntG/view?usp=sharing)
