# What Is a Knowledge Cutoff?

*What Is a Knowledge Cutoff?* Bella, in for Gomathy · Humanitarians AI · built 2026-10-07 – 2026-10-09

Claude only knows what it learned before its cutoff, so for anything recent or anything that may have changed,
paste in a current source or use web search.

Text and code only. **The masters live in the shared Google Drive**, not in this repository. See the link below.

## The files

| | File | |
|---|---|---|
| **16:9** | `knowledge-cutoff.mp4` | 3840×2160 · 1:01 (60.5 s) |
| **9:16** | `knowledge-cutoff-vertical.mp4` | 2160×3840 · 1:01 (60.5 s) |

12 beats, Plain register, Kokoro `af_bella` ("Bella").

## What's in this folder

- **16:9:** `beat_sheet.json` (source of truth), `scenes.py` (Manim beats), `SOURCES.md`, `FACTCHECK.md`,
  `PEDAGOGY.md`, `SHOTLIST.md`, `PROMPTS.md`, `CHECKS-REPORT.md`, `BUILD-LOG.md`.
- **`vertical/` (9:16):** its own `beat_sheet.json` and `scenes.py` (not a crop of the 16:9), plus `BUILD-LOG.md`,
  `SOURCES.md`, `FACTCHECK.md`, `PEDAGOGY.md`, `SHOTLIST.md`, `PROMPTS.md`.

## Sources

Every claim is checked against Anthropic's own pages (`SOURCES.md`, `FACTCHECK.md`):

- Anthropic, [Models overview](https://platform.claude.com/docs/en/about-claude/models/overview)
- Anthropic, [Web search tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool)
- Anthropic, [Context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows)
- Anthropic, [Transparency Hub](https://www.anthropic.com/transparency)

No model names or cutoff dates appear on screen, so the reel doesn't date. Two beats (B04, B06) are marked as
inference in `SOURCES.md`, and their visuals are labelled `ILLUSTRATIVE`.

## Links

| | Drive | YouTube |
|---|---|---|
| 16:9 and 9:16 masters | <!-- DRIVE_LINK --> [Drive](https://drive.google.com/drive/folders/1OTT2zEUN1pnyRdDwdY0A4gO_P_Zwokfd?usp=share_link) | <!-- YOUTUBE_LINK --> *(to add)* |

## Rebuilding

Built with the [`brutalist.art`](https://github.com/nikbearbrown/brutalist.art) toolkit (`ai-explainer`, `claude-hai`
channel). Kokoro narration is generated from `beat_sheet.json` and its measured durations are the clock.
