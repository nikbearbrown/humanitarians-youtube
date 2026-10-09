# The Context Window Isn't Memory

*The Context Window Isn't Memory.* Bella, in for Gomathy · Humanitarians AI · built 2026-09-28 – 2026-10-07

A context window is a fixed, shared token budget, not memory: the system prompt, tools, history, your message
and Claude's reply all draw on it, and past the ceiling what happens depends on the app.

Text and code only. **The masters live in the shared Google Drive**, not in this repository. See the link below.

## The files

| | File | |
|---|---|---|
| **16:9** | `claude-liam-context-window.mp4` | 3840×2160 · 1:03 (63.4 s) |
| **9:16** | `claude-liam-context-window-vertical.mp4` | 2160×3840 · 1:03 (63.3 s) |

12 beats, Plain register, Kokoro `af_bella` ("Bella").

## What's in this folder

- **16:9:** `beat_sheet.json` (source of truth), `scenes.py` (Manim beat), `SOURCES.md`, `FACTCHECK.md`,
  `PEDAGOGY.md`, `SHOTLIST.md`, `PROMPTS.md`, `CHECKS-REPORT.md`, `BUILD-LOG.md`.
- **`vertical/` (9:16):** its own `beat_sheet.json` and `scenes.py` (not a crop of the 16:9), plus `BUILD-LOG.md`,
  `FACTCHECK.md`, `SHOTLIST.md`, `PROMPTS.md`.

## Sources

Every claim is checked against Anthropic's own documentation (`SOURCES.md`, `FACTCHECK.md`):

- Anthropic, [Context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows)
- Anthropic, [Token counting](https://platform.claude.com/docs/en/build-with-claude/token-counting)

One claim (code, numbers, jargon and non-English text cost more tokens per word) is general tokenizer behaviour,
not an Anthropic statement; `SOURCES.md` flags it. Illustrative values on screen are labelled `ILLUSTRATIVE`.

## Links

| | Drive | YouTube |
|---|---|---|
| 16:9 and 9:16 masters | <!-- DRIVE_LINK --> [Drive](https://drive.google.com/drive/folders/1sdOqDlg0ozhcLBl_1GrlOm84u4vkGuPX?usp=share_link) | <!-- YOUTUBE_LINK --> *(to add)* |

## Rebuilding

Built with the [`brutalist.art`](https://github.com/nikbearbrown/brutalist.art) toolkit (`ai-explainer`, `claude-hai`
channel). Kokoro narration is generated from `beat_sheet.json` and its measured durations are the clock.
