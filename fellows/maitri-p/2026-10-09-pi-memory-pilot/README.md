# Pi Memory Pilot: First Results

**Type:** Project update (recorded pilot results)
**Fellow:** Maitri P. · **Voice:** Kokoro `af_bella` (Bella), a synthetic narrator — disclosed on the outro card.

## This week's contribution
**Question:** does frozen external memory change how the Pi agent searches a multi-file corpus?
**Prediction:** procedural and metacognitive lessons would reduce tool calls on new, similar questions.
**What I built / ran:** a multi-hop pilot — 3 practice questions, a review step that turned traces into lessons, frozen memory, then 6 held-out questions × 4 conditions (none / procedural / metacognitive / both) in fresh sessions.
**Observed (recorded pilot, 1 repetition):** mean tool calls 6.00 / 4.33 / 5.00 / 6.83. All numeric answers correct; "both" lost one evidence-valid task to a citation-compliance failure. Metacognitive logged 0 tool errors. **Early signals, not proven improvement.**
**Next experiment:** repeat each condition 3 times before claiming any difference.

## Human and AI work
**My decisions and verification:** designed and ran the pilot; chose the three scenes, the labels and the caveats; supplied the recorded results; reviewed the cuts.
**AI tools and what they generated:** Claude Code (Anthropic) read the recorded files read-only, wrote the beat sheet and narration, built `EvidenceBars` and `LessonExcerpt` scenes, and rendered. Kokoro produced the narration. No Pi experiment was re-run and no API call was made for the film.
**What I rejected or corrected:** see `FRICTIONAL.md`.
**What remains unverified or failed:** see `FACTCHECK.md` — one repetition; overlapping intervals; lesson usefulness unverified.

## Reproduce
- **Brutalist toolkit:** commit `6fc9987` **plus local uncommitted changes** (new scenes in `scenes/`, Windows fixes). Not yet upstream.
- **Evidence:** `evidence.json` — the only data copied from the recorded run (no paths, logs or credentials).
- **Beat sheets:** `beat_sheet.json` (16:9), `vertical/beat_sheet.json` (9:16 native layouts).
- **Checks:** `FACTCHECK.md`, `SHOTLIST.md`, `PROMPTS.md`. GATE V: 0 blockers on both aspects.

## Watch and review
- **Landscape** — `PiMemoryPilot_MaitriP.mp4` — [Drive Link](https://drive.google.com/file/d/1zxl7Krfp6hWkd0CC0VtDfpQD1Gp-zOPT/view?usp=sharing)