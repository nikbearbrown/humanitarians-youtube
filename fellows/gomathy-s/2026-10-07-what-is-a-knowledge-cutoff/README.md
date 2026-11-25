# What Is a Knowledge Cutoff? — Gomathy S.

*What Is a Knowledge Cutoff?* Bella, in for Gomathy · Humanitarians AI · built 2026-10-07 – 2026-10-09

Claude only knows what it learned before its cutoff, so for anything recent or anything that may have changed,
paste in a current source or use web search.

Text and code only. **The masters live in the shared Google Drive**, not in this repository. See the link below.

**Type:** STEM.

**Opening line.** This video does not use the required opening line ("Hi, I am [name] and this video is about [summary]"). The rule was already in `FELLOWS-SUBMISSION.md` when it was built; it opens "Hi — Bella, in for Gomathy. Ask Claude about last week — it may not know. Here's why." instead, naming the Kokoro narrator but not saying it is an AI voice. Not re-rendered.

## This week's contribution

- **Question:** Why might Claude not know about something that happened last week, and what should you do about it?
- **Prediction:** Using only patterns that had passed a final master with a working portrait version would mean fewer component surprises. There were fewer.
- **What I built/tried:** Script, sources and both review cuts (2026-10-07); fixes, sign-off and both 4K masters (2026-10-09).
- **Observed result:** Claude only knows what it learned before its cutoff; for anything recent, bring a current source or use web search. Model names and cutoff dates were kept off screen so the video doesn't date. Both masters (60.5 s) passed GATE T and GATE V.
- **Next experiment:** Not recorded at the time.

## Human and AI work

- **My decisions, implementation and verification:** Changed two lines in script review ("Near that edge" → "Between those dates"; the "stable facts" line now says only that the cutoff matters less for them); set the composer's model chip to "Claude" in both formats; reviewed and approved the pedagogy gate with four known weaknesses accepted.
- **AI tools/voices used and what they generated:** Claude drafted the sources, narration and both cuts, and carried video 1's lessons into a table in `BUILD-LOG.md`. Kokoro `af_bella` generated the narration; the brutalist.art toolkit rendered the beats.
- **What I rejected or corrected:** Removed model names and dates; replaced a framing that implied the training-data range always runs later than the reliable-knowledge date with the doc's own words; replaced the toolkit's default model chip ("Fable 5").
- **What remains unverified or failed:** Two beats (B04, B06) are inference, hedged and labelled `ILLUSTRATIVE`. Accepted weaknesses: falsifiability is partial, the 4.6 s opening summary is shorter than the ≥ 9 s the doctrine asks for, two cards echo their narration, some labels are terse to fit portrait. The outro's white-ground palette break is still open.

Full record: [`FRICTIONAL.md`](FRICTIONAL.md).

## Reproduce

- **Brutalist version/commit and date checked:** brutalist.art [`ad329089`](https://github.com/nikbearbrown/brutalist.art/commit/ad329089aa2a9cde41a1c8927361187b8da8fb7c) (`main`, 2026-09-28), the only commit of the local checkout used for every build: cloned 2026-09-28, HEAD never moved (checked from its reflog on 2026-11-20). The checkout also has uncommitted local edits to 6 runtime files (20 lines added, 13 removed), last modified 2026-09-28/29, before this build, so the commit alone does not reproduce it exactly. The weekly version check the submission guide asks for was not recorded at build time.
- **Source commit used for this export:** the beat sheets and `scenes.py` files in this folder were committed in [`d7891147`](https://github.com/nikbearbrown/humanitarians-youtube/commit/d789114742d6b1ed1eced42ebd44a0e64ec0d18e) ([PR #229](https://github.com/nikbearbrown/humanitarians-youtube/pull/229)), after the export. They are byte-identical (SHA-256 compared 2026-11-20) to the copies the masters were built from.
- **Beat sheet and custom scene files:** `beat_sheet.json`, `scenes.py`, `vertical/beat_sheet.json`, `vertical/scenes.py`.
- **Commands or browser steps, dependencies, input/source links:** Built with the [`brutalist.art`](https://github.com/nikbearbrown/brutalist.art) toolkit (`ai-explainer`, `claude-hai` channel). Kokoro narration is generated from `beat_sheet.json` and its measured durations are the clock. Masters built with `./art final` (see `BUILD-LOG.md`). Sources are listed below and in `SOURCES.md`.
- **Approvals and checks:** [`CHECKS-REPORT.md`](CHECKS-REPORT.md), [`BUILD-LOG.md`](BUILD-LOG.md), [`PEDAGOGY.md`](PEDAGOGY.md) and the sign-off in [`FRICTIONAL.md`](FRICTIONAL.md) (pedagogy gate approved by me). No PM or professor approval is recorded.

## Watch and review

- **Landscape:** [Drive](https://drive.google.com/drive/folders/1OTT2zEUN1pnyRdDwdY0A4gO_P_Zwokfd?usp=share_link) — 3840×2160 — 60.5 s — SHA-256 `eb822ea98e622ae91dc17571094070fbc90d48c78d64b1a9a923b35cf1740359` (`knowledge-cutoff.mp4`, built 2026-10-09). Hashed from the local master `brutalist.art/renders/knowledge-cutoff.mp4` on 2026-11-20; it matches the build record. The Drive copy was not hashed.
- **Vertical:** [Drive](https://drive.google.com/drive/folders/1OTT2zEUN1pnyRdDwdY0A4gO_P_Zwokfd?usp=share_link) — 2160×3840 — 60.5 s — SHA-256 `06e49d636b7e1becc4b148ccd7c1ef1b56431676c5c0610a8d08fc1f50354f50` (`knowledge-cutoff-vertical.mp4`, built 2026-10-09). Hashed from the local master `brutalist.art/renders/knowledge-cutoff-vertical.mp4` on 2026-11-20; it matches the build record. The Drive copy was not hashed.
- **Sources/large assets Drive link:** none recorded; the sources cited are listed in `SOURCES.md`.
- **PM review status:** in review (`RENEWAL.md`); no recorded outcome.
- **YouTube 4K processing check:** pending upload.
- **Professors' publication decision:** pending.

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
