# Weekly Work Report: The Classifier That Learned When Not to Guess

**Fellow:** Sai Pranavi J.
**Week ending:** October 6, 2026
**Project:** Project 29 — Financial Regulatory Intelligence System (`mycroft` repo, `scripts/regulatory-intel/`)
**Source status:** Real engineering work. Every claim traces to `B2-VERIFICATION.md` (the 2026-10-06 addendum) and the matching `logs/RUN_LOG.md` entry in the `mycroft` repo — a local-LLM (Ollama) fallback classification step built and verified live against the actual 21 `Unknown Source` database rows and the shipped `workflow.dev.json` code.

## Watch

- Landscape (4K 16:9): [Drive link](https://drive.google.com/open?id=1kFgZEsCVaIy_rFppUWlmbNGUl805EtBj)
- Vertical (4K 9:16): [Drive link](https://drive.google.com/open?id=1-Vk0ggysQepob9euT6P9GzjTpv1RL33v)

This video covers a continuation of the B2 source-classification fix: 21 headlines were falling through the keyword/pattern classifier to "Unknown Source." Prior fixes (closed 2026-08-30, narrowed 2026-09-07) brought that down to 13 already resolved as of this session — verified live by re-running the real `identifySource()` function against the actual 21 DB rows — leaving a genuine residual of 8 generic headlines no fixed keyword list can resolve without false-positiving on unrelated content. This video covers adding a local-LLM (Ollama) fallback classification step for just that residual, and the honestly modest result: it resolved 1 of 8, correctly declining to guess on the rest rather than force a label onto genuinely ambiguous content.

## What this covers (and what it deliberately leaves out)

Covered: the real 21 → 13 resolved → 8 residual breakdown with real verbatim example headlines, the new node's exact position in the pipeline and its conditional gate (`ONLY IF source_feed == 'Unknown Source'`), the fail-open validation design, the 4 live-verification numbers shown together (0 mutated / 1 resolved / 7 declined / 0 errors), the one resolved headline and its new label, and an honest framing of 1-of-8 as the correct outcome rather than a shortfall.

Deliberately left out: this is not a claim that the LLM fallback generally resolves "Unknown Source" items at scale — it is a report on this specific 8-item residual, honestly scored.

## Production state

- Plan: **approved (Gate P)** — signed 2026-10-06
- Fact-check gate: **resolved** — see `FACTCHECK.md`; B06's "1 of 8" framing kept at full weight, no softening
- Narration approval: **approved** — Kokoro `af_bella`, locked 2026-10-09
- Voice: **Bella (`af_bella`)** — persistent for this fellow's whole report series
- Previz: **complete** — 9/9 beats real Manim, no slates, both aspects
- Final render — **16:9 landscape:** `ClassifierFallbackClassification_SaiPranaviJ.mp4`, 3840x2160, 24fps, h264/aac, **159.875s**. GATE V on the true clean master: **0 BLOCKER, 0 MAJOR**.
- Final render — **9:16 vertical (full-length, native portrait, not a Shorts cut):** `ClassifierFallbackClassification_SaiPranaviJ.mp4`, 2160x3840, 24fps, h264/aac, **159.875s** (identical duration to the landscape master — every beat kept, nothing dropped). GATE V on the true clean master: **0 BLOCKER, 0 MAJOR**.
- Personally re-verified (not just trusting the build report): extracted and viewed real frames from B04 (the pipeline diagram's conditional gate), B06 (the honest-limits framing and 7 dimmed declined headlines), and B08 (brand sign-off) directly from both final deliverables. No text-rendering artifacts, no clipping, no overlap; B04 clearly shows the YES/NO gate and the untouched bypass path in both aspects.
- Publishing: **not authorized** — masters stay in this folder only, ready for fellow/PM review

## Built under the toolkit's new submission spec

This project follows the toolkit's official spec (`brutalist/docs/FELLOWS-SUBMISSION.md`, effective 2026-09-07): `ProjectName_VolunteerName.mp4` naming (no date/aspect suffix), separate `deliverables/landscape/` and `deliverables/vertical/` folders, and a true full-length 4K 2160x3840 vertical companion built via `./art vertical` (not a ≤180s Shorts-style cut) — every beat, no cuts, no added endcard.

## Human and AI work

**My decisions, implementation and verification:** the underlying engineering (the `Layer 2 - LLM Source Classification` node, its conditional gate, fail-open design, and the live verification harness) is my own work on Project 29, done before this video session; the facts and numbers reported here (21/13/8, 0 mutated/1 resolved/7 declined/0 errors) were measured in that prior session and are carried into this video unchanged.

**AI tools/voices used and what they generated:** Claude Code authored all 9 Manim scenes (both aspects), generated the Kokoro `af_bella` narration audio, ran the full render/compile/QC pipeline, and wrote this paperwork set. Nothing in the pipeline fabricated or altered the underlying numbers or quoted headlines.

**What I rejected or corrected:** none this session — the beat sheet and fact-check were already approved; the build work focused on authoring the visuals accurately against the approved claims and fixing real layout/canvas-fill defects caught by GATE A/B/V (documented in `BUILD-LOG.md`).

**What remains unverified or failed:** nothing — both final masters are GATE V clean (0 BLOCKER, 0 MAJOR) and personally frame-checked.

## Reproduce

- Brutalist version/commit and date checked: this repo's `brutalist/` at the time of this build, 2026-10-11
- Source commit used for this export: `mycroft` repo state as documented in `SOURCES.md` (B2-VERIFICATION.md 2026-10-06 addendum, `workflow.dev.json`)
- Beat sheet and custom scene files: `beat_sheet.json`, `scenes.py` (landscape), `vertical/beat_sheet.json`, `vertical/scenes.py` (portrait)
- Commands: `python3 brutalist/runtime/scripts/generate_audio_kokoro.py <reel>` (Kokoro TTS), `ffmpeg -f lavfi -i anullsrc ...` (B00 silent track), `./art run <reel>` (landscape review + QC gates), `./art final <reel>` (landscape 4K master), `./art run <reel>/vertical` + `./art final <reel>/vertical --height 3840` (vertical 4K master), `final_frame_check.py --lenient` (standalone GATE V re-check on both true finals)
- Approvals and checks: see `FACTCHECK.md`, `BEAT-SHEET.md` (Gate P sign-off), `BUILD-LOG.md` (build history, bugs found/fixed, GATE V results)

## Watch and review

- Landscape — `deliverables/landscape/ClassifierFallbackClassification_SaiPranaviJ.mp4` — 3840×2160 — 159.875s — SHA-256 in the adjacent `.verified.json`
- Vertical — `deliverables/vertical/ClassifierFallbackClassification_SaiPranaviJ.mp4` — 2160×3840 — 159.875s — SHA-256 in the adjacent `.verified.json`
- PM review status: pending
- YouTube 4K processing check: pending upload
- Professors' publication decision: pending

## Useful project files

- `BEAT-SHEET.md` — the narrative beat sheet as drafted and approved
- `beat_sheet.json` / `vertical/beat_sheet.json` — the same plan in the pipeline's structured schema, both aspects
- `FACTCHECK.md` — claim-level review against `B2-VERIFICATION.md`
- `SOURCES.md` — claim → source mapping
- `SHOTLIST.md` / `PROMPTS.md` (and `vertical/` copies) — beat-by-beat medium/timing table and pantry/asset status
- `scenes.py` / `vertical/scenes.py` — the Manim source for both aspects
- `BUILD-LOG.md` — dated build decisions, bugs found and fixed, and gate history
