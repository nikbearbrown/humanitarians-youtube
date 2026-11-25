# The Context Window Isn't Memory — Gomathy S.

*The Context Window Isn't Memory.* Bella, in for Gomathy · Humanitarians AI · built 2026-09-28 – 2026-10-07

A context window is a fixed, shared token budget, not memory: the system prompt, tools, history, your message
and Claude's reply all draw on it, and past the ceiling what happens depends on the app.

Text and code only. **The masters live in the shared Google Drive**, not in this repository. See the link below.

**Type:** STEM.

**Opening line.** This video does not use the required opening line ("Hi, I am [name] and this video is about [summary]"). The rule was already in `FELLOWS-SUBMISSION.md` when it was built; it opens "Hi — Bella, in for Gomathy. Long chats seem to forget. It's a budget, not memory." instead, naming the Kokoro narrator but not saying it is an AI voice. Not re-rendered.

## This week's contribution

- **Question:** Why do long chats seem to forget? Is the context window a kind of memory?
- **Prediction:** Recorded only for the process: I expected the toolkit's template persona to need only a name change. It needed more (a voice conflict between toolkit files, and a locked outro that is only allowed on Bear's channel).
- **What I built/tried:** A 9-beat, 154.5 s long cut (2026-09-28), reworked to the 60-second, 12-beat format (2026-09-29); the 16:9 4K master (2026-10-01); a native 9:16 version (2026-10-07).
- **Observed result:** A context window is a fixed token budget shared by the system prompt, tools, history, the new message and Claude's reply. The first draft's claim that the oldest turns are always dropped was wrong: Anthropic's page says the behaviour depends on the app. Both masters are 4K, about 63 s.
- **Next experiment:** Carried into the next video: use only patterns that had already passed a final master with a working portrait version (see the knowledge-cutoff log).

## Human and AI work

- **My decisions, implementation and verification:** Chose Kokoro `af_bella` and renamed the narrator from Liam to Bella; directed the 60-second rework (restore "context rot" as one line, restate the thesis plainly in the summary, drop the on-screen inference tag on the token-density beat); passed the pedagogy gate as a fresh pass; kept "often" in the card sub-lines to match the sources.
- **AI tools/voices used and what they generated:** Claude drafted the sources table, narration, beat sheet and the cuts, and found the voice conflict and the outro lock in the toolkit docs. Kokoro `af_bella` generated the narration; the brutalist.art toolkit rendered the Remotion and Manim beats.
- **What I rejected or corrected:** Corrected "the oldest turns are always dropped" to the app-dependent behaviour; added Claude's reply to the budget; labelled invented chart values `ILLUSTRATIVE`; rejected a toolkit edit and removed the bar's accent colour instead.
- **What remains unverified or failed:** The token-density claim has no Anthropic source and is flagged as inference in `SOURCES.md`. The worked example and falsifiability beat are thinner than in the long cut (disclosed in `CHECKS-REPORT.md`). The outro card renders on its own white ground, a one-beat palette break.

Full record: [`FRICTIONAL.md`](FRICTIONAL.md).

## Reproduce

- **Brutalist version/commit and date checked:** brutalist.art [`ad329089`](https://github.com/nikbearbrown/brutalist.art/commit/ad329089aa2a9cde41a1c8927361187b8da8fb7c) (`main`, 2026-09-28), the only commit of the local checkout used for every build: cloned 2026-09-28, HEAD never moved (checked from its reflog on 2026-11-20). The checkout also has uncommitted local edits to 6 runtime files (20 lines added, 13 removed), last modified 2026-09-28/29, before this build, so the commit alone does not reproduce it exactly. The weekly version check the submission guide asks for was not recorded at build time.
- **Source commit used for this export:** the beat sheets and `scenes.py` files in this folder were committed in [`d7891147`](https://github.com/nikbearbrown/humanitarians-youtube/commit/d789114742d6b1ed1eced42ebd44a0e64ec0d18e) ([PR #229](https://github.com/nikbearbrown/humanitarians-youtube/pull/229)), after the export. They are byte-identical (SHA-256 compared 2026-11-20) to the copies the masters were built from.
- **Beat sheet and custom scene files:** `beat_sheet.json`, `scenes.py`, `vertical/beat_sheet.json`, `vertical/scenes.py`.
- **Commands or browser steps, dependencies, input/source links:** Built with the [`brutalist.art`](https://github.com/nikbearbrown/brutalist.art) toolkit (`ai-explainer`, `claude-hai` channel). Kokoro narration is generated from `beat_sheet.json` and its measured durations are the clock. Masters built with `./art final` (see `BUILD-LOG.md`). Sources are listed below and in `SOURCES.md`.
- **Approvals and checks:** [`CHECKS-REPORT.md`](CHECKS-REPORT.md), [`BUILD-LOG.md`](BUILD-LOG.md), [`PEDAGOGY.md`](PEDAGOGY.md) and the sign-off in [`FRICTIONAL.md`](FRICTIONAL.md) (pedagogy gate approved by me). No PM or professor approval is recorded.

## Watch and review

- **Landscape:** [Drive](https://drive.google.com/drive/folders/1sdOqDlg0ozhcLBl_1GrlOm84u4vkGuPX?usp=share_link) — 3840×2160 — 63.4 s — SHA-256 `e641c7029aae4c8d9e4c24c6320d89d9a59cc651f8298a85e9eabf0bdc0af938` (`claude-liam-context-window.mp4`, built 2026-10-01). Hashed from the local master `brutalist.art/renders/claude-liam-context-window.mp4` on 2026-11-20; it matches the build record. The Drive copy was not hashed.
- **Vertical:** [Drive](https://drive.google.com/drive/folders/1sdOqDlg0ozhcLBl_1GrlOm84u4vkGuPX?usp=share_link) — 2160×3840 — 63.3 s — SHA-256 `6dafda992436968650213fb7355e3b22c83b1f45fe23041d7684ec6bf74fe31f` (`claude-liam-context-window-vertical.mp4`, built 2026-10-07). Hashed from the local master `brutalist.art/renders/claude-liam-context-window-vertical.mp4` on 2026-11-20; it matches the build record. The Drive copy was not hashed.
- **Sources/large assets Drive link:** none recorded; the sources cited are listed in `SOURCES.md`.
- **PM review status:** in review (`RENEWAL.md`); no recorded outcome.
- **YouTube 4K processing check:** pending upload.
- **Professors' publication decision:** pending.

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
