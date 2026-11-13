# Cold Start, Warm Start

**Type:** AI/STEM explainer
**Fellow:** Maitri P. · **Voice:** Kokoro `af_bella` (Bella), a synthetic narrator — disclosed on the outro card.

## This week's contribution
Explainer on why the first AWS Lambda request can be slower: execution environments, cold and warm starts, why traffic bursts cause cold starts (N ≈ λ × d), and the trade-offs of lighter initialization and provisioned concurrency.

## Human and AI work
**My decisions and verification:** chose the topic and wrote the explanation the video follows; reviewed the cuts.
**AI tools and what they generated:** Claude Code (Anthropic) turned my explanation into the beat sheet, built and rendered the scenes, and fact-checked the claims (see `FACTCHECK.md`). Kokoro produced the narration.

## Reproduce
- **Brutalist toolkit:** commit `6fc9987` plus local uncommitted changes (scenes in `scenes/`). Not yet upstream.
- **Beat sheets:** `beat_sheet.json` (16:9), `vertical/beat_sheet.json` (9:16 native layouts).
- **Checks:** `FACTCHECK.md`, `SHOTLIST.md`, `PROMPTS.md`.

## Watch and review
- **Landscape** — `LambdaColdStart_MaitriP.mp4` — 3840×2160 — 1:24.6 — SHA-256 `48a1788e4922972f57191c2e2b8e404b7053fb1090c5f164c4cea8346242c969`
  Drive: https://drive.google.com/file/d/1zOImrdpq6cb8k-QIplrydQVnJE3JESxe/view?usp=sharing
- **Vertical** — `LambdaColdStart-vertical.mp4` — 2160×3840 — 1:24.6 — SHA-256 `6cdbd0a6622a12b41a7e8a353be3ba32652bf3e4de14a04e97957f663e48b9a7`
  Drive: https://drive.google.com/file/d/19Zx6uaGg6UuJDbUZsJY4AUZLdYAytW1Q/view?usp=sharing
