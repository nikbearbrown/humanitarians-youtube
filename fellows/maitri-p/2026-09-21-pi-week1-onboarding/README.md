# Week One: How Pi Works

**Type:** Project update — **catch-up report** for the week of 2026-09-21, produced 2026-10-23
**Fellow:** Maitri P. · **Voice:** Kokoro `af_bella` (Bella), a synthetic narrator — disclosed on the outro card.

## This week's contribution
**Question:** how does the Pi agent work, and where could memory fit?
**What I did:** after onboarding, read the company policies, installed arkenOS and set up Brutalist; picked the Pi agent for the memory-types research and studied its loop before changing anything.
**What I learned:** Pi sends a request with instructions and tools to the model; when the model asks to read a file or run a command, Pi executes it and returns the real output or error; this repeats until a final answer. Seeing an error within one run is not the same as remembering a lesson for a later run — the experiment needs a way to review a run, keep what is useful and bring it into a fresh task.
**Observed:** no measurement in week one — no memory improvement was claimed or measured.
**Next experiment:** run Pi on small tasks and inspect its tool calls, errors and results.

## Human and AI work
**My decisions and verification:** the week-one work and the account of it; approved the narration.
**AI tools and what they generated:** Claude Code (Anthropic) wrote the beat sheet from my account, added the trace notation (τ, review, ⊕) as a framing — labelled on screen as not a result — and rendered. Kokoro produced the narration.
**What I rejected or corrected:** see `FRICTIONAL.md`.
**What remains unverified or failed:** no data from week one exists; this is a description, not evidence of results.

## Reproduce
- **Brutalist toolkit:** commit `6fc9987` **plus local uncommitted changes** (scenes in `scenes/`, Windows fixes). Not yet upstream.
- **Beat sheets:** `beat_sheet.json` (16:9), `vertical/beat_sheet.json` (9:16 native layouts).
- **Checks:** `FACTCHECK.md`, `SHOTLIST.md`, `PROMPTS.md`. GATE V: 0 blockers on both aspects.

## Watch and review
- **Landscape** — `PiWeek1_MaitriP.mp4` — (Drive Link)[https://drive.google.com/file/d/1MkWJSq6NMZERfLqyP5FRCVWw1PbgVZMm/view?usp=sharing]
- **Vertical** — `PiWeek1_MaitriP.mp4` —  (Drive link)[https://drive.google.com/file/d/1ujihy3CPvTG-KGtECeVfhIFYwQ32J54q/view?usp=sharing]
