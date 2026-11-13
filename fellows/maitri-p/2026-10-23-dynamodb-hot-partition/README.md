# Where Traffic Lands

**Type:** AI/STEM explainer
**Fellow:** Maitri P. · **Voice:** Kokoro `af_bella` (Bella), a synthetic narrator — disclosed on the outro card.

## This week's contribution
Engineering explainer on why a DynamoDB table can throttle with spare capacity: a single partition key hashes every write to one hot partition capped at about 1,000 write units per second; write sharding spreads the load at the cost of multi-shard reads.

## Human and AI work
**My decisions and verification:** chose the topic and wrote the explanation the video follows; reviewed the cuts.
**AI tools and what they generated:** Claude Code (Anthropic) turned my explanation into the beat sheet, built and rendered the scenes, and fact-checked the claims (see `FACTCHECK.md`). Kokoro produced the narration.

## Reproduce
- **Brutalist toolkit:** commit `6fc9987` plus local uncommitted changes (scenes in `scenes/`). Not yet upstream.
- **Beat sheets:** `beat_sheet.json` (16:9), `vertical/beat_sheet.json` (9:16 native layouts).
- **Checks:** `FACTCHECK.md`, `SHOTLIST.md`, `PROMPTS.md`.

## Watch and review
- **Landscape** — `DynamoDBHotPartition_MaitriP.mp4` — 3840×2160 — 1:29.0 — SHA-256 `9dbb4e467b1a78a2d35cd0aad010c49d271711e6831d6e0a09eb0e31ded7c395`
  Drive: https://drive.google.com/file/d/1CD71KmGXaR7pT9VlP3P0pPVLxtpiByNE/view?usp=sharing
- **Vertical** — `DynamoDBHotPartition_vertical.mp4` — 2160×3840 — 1:29.0 — SHA-256 `a4b8290cda0865ef2d4becc9a7e0634910ed180135f0db9b1f74c017ac72c997`
  Drive: https://drive.google.com/file/d/1hYKVjL6GVJ7hc1S4QN1JqO-gSQAHCFez/view?usp=sharing
