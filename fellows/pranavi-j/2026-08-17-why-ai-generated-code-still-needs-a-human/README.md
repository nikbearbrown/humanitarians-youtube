# General-AI-Topic Explainer: Why AI-Generated Code Still Needs a Human Who Understands the System

**Fellow:** Sai Pranavi Jeedigunta
**Date:** August 17, 2026
**Format:** `ai-explainer` (short-form, v3 runtime ~2:04), Film 1 of a new general-AI-topic series (distinct from the `2026-07-27-how-facial-recognition-actually-works/` topic-explainer series and the weekly-report series)
**Source status:** General-AI-topic explainer, not a report of the fellow's own engineering work. The worked example (a hand-escaped SQL insert vs. a parameterized-query fix) is a generic, illustrative code pattern — deliberately not attributed to a specific real incident or repo. See `FACTCHECK.md`.

## Watch

- Landscape (4K 16:9): [Drive link](https://drive.google.com/open?id=1uI8pl27qQHJ-exRhi_A_6Fq9bpfIcSlP)
- Vertical (4K 9:16): [Drive link](https://drive.google.com/open?id=1b8Uwo22D3OLkzDS1_uMLj0jvZXEsiBTg)

This AI-generated video opens on a silent title card, then teaches a reusable rubric — "The 3 Questions Before You Trust a Fix" (Trace / Consequence / Why) — for deciding how much scrutiny an AI-suggested code fix needs. It moves to a fix that looks correct but still crashes production, shows the framework before any example, walks the rubric through a worked example, names a falsifiability case where quick trust is fine, and closes on a scaffolded viewer task.

**v2 revision (2026-08-17):** the fellow watched the v1 master (56.46s) and found the framework (B01), worked example (B02), and CTA (B04) too vague — they named or labeled the 3 items in each beat without explaining them. Narration for those 3 beats was rewritten with real explanatory depth and re-approved (Gate P v2), `scenes.py` was rebuilt to match with on-screen content that streams the explanations in step with the longer audio, and the whole reel was re-rendered. Runtime grew from 56s to ~1:59 as a direct, fellow-accepted result.

**v3 revision (2026-08-17):** the fellow watched the v2 master (119.03s) and requested two changes: (1) a silent title-card opening beat (new `B00`, 4.55s, no narration — video title + `@HumanitariansAI`) since v1/v2 dove straight into the crash log with zero title/branding intro; (2) the Trace question's jargon — "not just read the diff" — confused the fellow, reworded to "not just read what's different" in both narration and the on-screen caption. All 7 pre-existing beats renumbered B00-B06 -> B01-B07 to make room. Audio regenerated for all 8 beats, `scenes.py` rewritten (renames + new `B00_TitleCard` class), full re-render + re-QC. Runtime grew from 119.03s to 123.61s (the new title card), a direct, fellow-requested result.

**v3.1 patch (2026-08-19), layout-only:** the fellow watched the v3 master and screenshotted a real visual bug in `B01_HookCrashLog`'s first frame — the split-screen divider crossed through the glyphs of the left code panel's longest line ("const q = `INSERT INTO items"). Confirmed with real extracted Manim frames (before and after), not just static analysis: the divider (fixed at x=0) was never actually checked against the left code block's rendered right edge, which fit()'s generous width cap didn't prevent from landing past it. Fixed in `scenes.py` via a new `clear_of_divider()` helper that shifts the whole header+code block by an amount measured from its own rendered bounds, guaranteeing real clearance regardless of future edits. `B03_WorkedExampleDiff` and `B04_FalsifiabilityCase` were audited for the same pattern by direct measurement and found already clear — no changes needed there. No narration/audio change; full pipeline re-rendered (`./art run` then `./art final`), GATE A/W/V all re-confirmed clean (same accepted cosmetic-only MAJOR list as v3). Runtime unchanged at 123.61s (123.605s exact).

**v4 (2026-08-26), program feedback:** applied three pieces of program-wide feedback (also applied to this fellow's other two videos): (1) confirmed 4K — already 3840x2160 since v3; (2) added a new **B01 executive-summary beat** right after the B00 title card — "Hi, I'm Sai Pranavi Jeedigunta. This video is about why a fix that looks right isn't always a fix that's actually right — and the three questions to ask before you trust one." All prior content beats (old B01-B07) renumbered to B02-B08. Rebuilt on the freshly-updated brutalist toolkit (pulled to latest upstream). (3) Self-assessed against `PROOF.md` (copied into this folder) — 11/12 on the teaching rubric, all Production Gate items PASS; see `PEDAGOGY.md`. Runtime grew from 123.605s to 134.64s (the new exec-summary beat).

## What this covers (and what it deliberately avoids)

Covered: the framework-first structure (rubric shown before any example), a worked example applying all three rubric questions to a code fix, a falsifiability case (a low-stakes date-formatter function) that stress-tests the rubric against an absolutist "never trust AI code" reading, and a concrete 3-step viewer task.

Deliberately avoided: attributing the worked example to a specific real codebase or incident — it's presented as a generic, illustrative pattern (see `FACTCHECK.md` for why, and what was considered and set aside).

## Production state

- Plan: **approved (Gate P v3)** — Gate P (`PEDAGOGY.md`) signed VERDICT: PASS by the fellow, 2026-08-17; re-signed v2 (narration depth) and v3 (title card + wording fix) the same day
- Fact-check gate: **resolved** — no external sourcing required, worked example is generic by design; see `FACTCHECK.md`
- Narration approval: **approved (v3)** — B02's (was B01) Trace line reworded ("not just read the diff" -> "not just read what's different") per fellow request; all other narration unchanged since v2
- Voice: **Bella (`af_bella`)** — confirmed for this cut, matching this fellow's prior videos
- Audio lock: **locked (v4)** — Kokoro `af_bella`, all 9 beats. New B01 exec-summary measured 11.04s; all other beats' narration/durations unchanged from v3.1.
- Previz: **complete (v4)** — new `B01_ExecSummary` class added; all beats from old B01-B07 renamed to B02-B08. All 9 beats are real Manim scenes, no slates. GATE A/W clean.
- Final render: **complete (v4)** — `2026-08-17-why-ai-generated-code-still-needs-a-human.mp4`, 3840×2160 @24fps, **134.64s**, rendered 2026-08-26 via `./art final` on the freshly-updated brutalist toolkit
- Visual QC (GATE V, true clean master, not the watermarked `-slate.mp4`): **0 BLOCKER** (74 MAJOR under the toolkit's newly stricter/denser sampling, visually spot-checked as legible/cosmetic — see `PEDAGOGY.md`'s v4 self-assessment and `BUILD-LOG.md` for the full account)
- Self-assessment: **11/12** against `PROOF.md`'s teaching rubric, all binary Production Gate items PASS — see `PEDAGOGY.md`
- Publishing: **not authorized** — master stays in this folder only
- Code repository: paperwork/code (no media) pushed to `github.com/nikbearbrown/humanitarians-youtube`, branch `sai-pranavi-j-ai-code-4k-rebuild` (commit `ea79b66`) — no PR opened yet

## Compliance note

A channel/fellow sign-off card (B07, renumbered from B06: "@HumanitariansAI, in for Sai Pranavi Jeedigunta") was added 2026-08-17 to match the fellowship's requirement that videos demonstrably come from the volunteer, and the pattern in this fellow's other two videos — see `BUILD-LOG.md`.

## 9:16 Short (2026-08-28)

Built per `runtime/scripts/shorts.py`'s Shorts Law: this reel (134.64s) is under the 180s Shorts cap, so the short is a full reformat of all 9 beats — no beats cut, no narration rewritten, every mp3 reused from this reel's `mp3/`. All 9 beats are Manim `GRAPHIC` beats, so none were eligible for the auto center-cut; each got a genuine portrait re-layout in `short/scenes.py` (1080x1920), not a mechanical crop. The three wide side-by-side compositions were redesigned as top/bottom stacks: the hook's fix.js/server.log split screen, the worked example's before/after SQL diff (now a sequential single-panel reveal that crossfades BEFORE->AFTER for the WHY step), and the falsifiability beat's rubric-chips-next-to-code-panel layout.

- **Master:** `short/2026-08-17-why-ai-generated-code-still-needs-a-human-short.mp4` — **1080x1920 @24fps, 139.18s** (134.64s reformatted content + 4.5s silent branded endcard), 10/10 beats real, 0 slates.
- **QC:** GATE A/W clean on all 9 new portrait scenes pre-render; GATE V on the true clean master: **0 BLOCKER**, 6 MAJOR (all visually confirmed legible/cosmetic — 2 borderline low-contrast findings inherited from the parent's own color choices, 1 underfill on the toolkit's deliberately-minimal auto-generated endcard). See `BUILD-LOG.md`'s "9:16 Short" section for the full account, including a latent manim/`run.sh` portrait frame-geometry bug found and worked around, a real teal-on-ink contrast bug found and fixed, and a wrong-handle endcard bug found and fixed.
- Publishing: **not authorized** (same as the parent long).

## Useful project files

- `BEAT-SHEET.md` — the narrative beat sheet as drafted (premise, legibility contract, beats, production gate self-check)
- `beat_sheet.json` — the same plan in the pipeline's structured schema (pre-production; no media built yet)
- `BUILD-PROMPT.md` — the reproducible context/prompt this video was built from
- `BUILD-LOG.md` — dated build decisions and gate history
- `FACTCHECK.md` — claim-level review, including why the worked example is generic rather than sourced
- `SOURCES.md` — sourcing status (no external sources required for this cut)
- `PEDAGOGY.md` — Gate P self-check against the PROOF.md rubric
- `PROMPTS.md` — pantry/asset status
- `SHOTLIST.md` — beat-by-beat medium/timing table
