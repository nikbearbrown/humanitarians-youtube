# General-AI-Topic Explainer: Prompt Injection — The Vulnerability Hiding in Plain Text

**Fellow:** Sai Pranavi Jeedigunta
**Date:** August 30, 2026
**Format:** `ai-explainer` (short-form, runtime 147.94s), general AI/STEM topic explainer — distinct from this
fellow's weekly work-report series (e.g. `2026-08-30-the-update-that-almost-lied-about-what-it-sent/`).
Same framework-first genre and shape as `2026-08-17-why-ai-generated-code-still-needs-a-human/`
(this fellow's closest sibling video).
**Source status:** General AI/STEM topic explainer, not a report of the fellow's own engineering
work. Both worked examples are generic and hypothetical — see `FACTCHECK.md`.

This video opens on a silent title card, then teaches a reusable 3-question rubric —
"Source / Instruction-or-Data / Consequence" — for deciding whether text an AI agent reads from
the outside world (a web page, an email, a file) should ever be allowed to change what the agent
does. It shows the framework before any example, walks a worked example (a summarizer agent
tricked by a hidden instruction into forwarding a private email), stress-tests the rubric against
a falsifiability case that looks similar but isn't an attack (a recipe blog's imperative
instructions), and closes on a concrete audit task the viewer can run against their own agent
today.

## What this covers (and what it deliberately avoids)

**Covered:** the framework-first structure (rubric shown before any example), a worked example
applying all three rubric questions to a hidden-instruction attack, a falsifiability case (a
recipe-blog imperative sentence) that stress-tests the rubric against a naive "any imperative
sentence = injection" over-trigger, and a concrete audit task for the viewer.

**Deliberately avoided:** this is educational/defensive content, not an exploit tutorial. Neither
worked example is attributed to a real product, company, or disclosed incident/CVE — both are
generic, illustrative scenarios (a hypothetical research-summarizer agent; a hypothetical recipe
blog). No step-by-step attack construction guidance is given anywhere. The one external factual
claim (prompt injection as a named, widely-recognized vulnerability class) is sourced to OWASP's
Top 10 for LLM Applications (LLM01) — see `SOURCES.md` and `FACTCHECK.md`.

## Production state

- Plan: **approved (Gate P)** — fellow reviewed and approved the beat-by-beat outline 2026-08-30
- Fact-check gate: **resolved** — OWASP LLM01 citation added to B03; both worked examples confirmed
  generic/hypothetical; see `FACTCHECK.md`
- Narration approval: **approved** — cleared for audio generation 2026-08-30
- Voice: **Bella (`af_bella`)** — locked for this fellow's whole series, unchanged for this episode
- Audio lock: **locked** — Kokoro `af_bella`, all 9 beats (B00 silent via `ffmpeg anullsrc`, 4.05s;
  B01-B08 measured 15.60/18.29/23.57/25.44/27.65/22.68/9.17/1.51s)
- Previz: **complete** — `scenes.py` authored, 9/9 beats real Manim scenes, no slates. GATE A/W
  clean on all 9 scenes (after fixing an off-frame reveal-panel bug in B02, safe-area header
  positioning in B03/B04/B05, and canvas-fill underfill on B00/B01/B04/B05/B06/B07/B08)
- Final render: **complete** — `2026-08-30-what-prompt-injection-actually-looks-like.mp4`,
  3840×2160 @24fps, **147.94s**, rendered via `./art final`
- Visual QC (GATE V, true clean master, not the watermarked `-slate.mp4`): **0 BLOCKER, 1 MAJOR**
  (a mid-reveal sample on B04 at 51% canvas-fill, reviewed by eye via the contact sheet — the
  beat's full layout resolves to well over the 55% floor by the time all 3 rubric rows and the
  verdict are on screen)
- Publishing: **not authorized** — master stays in this folder only

## 9:16 Short (2026-08-31)

Built per `runtime/scripts/shorts.py`'s Shorts Law: this reel (147.94s) is under the 180s Shorts
cap, so the short is a full reformat of all 9 beats — no beats cut, no narration rewritten, every
mp3 reused from this reel's `mp3/`. All 9 beats are Manim `GRAPHIC` beats, so none were eligible
for an automatic center-cut; each got a genuine hand-authored portrait relayout in
`short/scenes.py` (1080x1920), not a mechanical crop. B02 (the browser/hidden-instruction hook),
B03 (the 3-question rubric), B04/B05 (the worked-example and falsifiability rubric-answer cards)
all got real top-to-bottom-stack redesigns — the parent's wide horizontal/side-by-side elements
(badge-beside-text rows, tag-beside-answer rows) don't fit a ~3.9-unit-wide portrait safe column,
so they were rebuilt as stacked blocks with re-wrapped text.

Building this short also surfaced and fixed a **toolkit-level bug**: Manim CE's CLI sets output
pixel dimensions from `-r WIDTH,HEIGHT`, but does not recompute `config.frame_width` to match — it
silently keeps the 16:9 default (14.22), so a portrait scene composed against an assumed
4.5-unit-wide frame actually renders at roughly a third of its intended size, clustered in the
middle of a much taller effective canvas. This was caught via GATE V measuring every beat at just
6-8% canvas-fill even after multiple rounds of spacing fixes — resolved by patching
`config.frame_width` at the top of `short/scenes.py` (the same fix already used in this fellow's
`2026-08-30-the-update-that-almost-lied-about-what-it-sent/short/scenes.py`). See `BUILD-LOG.md`
for the full diagnostic trail.

- **Master:** `short/2026-08-30-what-prompt-injection-actually-looks-like-short.mp4` — **1080x1920
  @24fps, 152.46s** (147.94s reformatted content + 4.5s silent branded endcard), 10/10 beats real,
  0 slates.
- **QC:** GATE B (`manim_layout_audit.py --portrait`) clean on all 9 portrait scenes pre-render;
  GATE V on the true clean master: **0 BLOCKER, 2 MAJOR** (both on the toolkit's auto-generated
  silent END card only — an inherent characteristic of a sparse handle-only card when no beats are
  cut, not an authored-beat defect). All 9 hand-authored beats are GATE-V-clean.
- Publishing: **not authorized** (same as the parent long).

## Deliverables (fellowship naming convention)

- `PromptInjection_SaiPranaviJeedigunta_20260830_16x9.mp4` — copy of the 16:9 master
- `PromptInjection_SaiPranaviJeedigunta_20260830_9x16.mp4` — copy of the 9:16 short master

## Useful project files

- `BEAT-SHEET.md` — the narrative beat sheet as drafted (premise, legibility contract, beats,
  production gate self-check)
- `beat_sheet.json` — the same plan in the pipeline's structured schema, stamped with build/gate
  state
- `scenes.py` / `short/scenes.py` — the 16:9 and 9:16 Manim scene source
- `BUILD-LOG.md` — dated build decisions and gate history, including the frame_width bug diagnosis
- `FACTCHECK.md` — claim-level review, including why both worked examples are generic rather than
  sourced
- `SOURCES.md` — sourcing status (OWASP Top 10 for LLM Applications, LLM01)
- `PEDAGOGY.md` — Gate P self-check against the `PROOF.md` rubric
- `PROMPTS.md` — pantry/asset status (N/A — self-contained Manim)
- `SHOTLIST.md` — beat-by-beat medium/timing table
