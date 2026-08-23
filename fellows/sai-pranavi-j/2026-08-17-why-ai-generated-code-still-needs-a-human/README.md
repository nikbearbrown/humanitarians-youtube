# General-AI-Topic Explainer: Why AI-Generated Code Still Needs a Human Who Understands the System

**Fellow:** Sai Pranavi Jeedigunta
**Date:** August 17, 2026
**Format:** `ai-explainer` (short-form, v3 runtime ~2:04), Film 1 of a new general-AI-topic series (distinct from the `2026-07-27-how-facial-recognition-actually-works/` topic-explainer series and the weekly-report series)
**Source status:** General-AI-topic explainer, not a report of the fellow's own engineering work. The worked example (a hand-escaped SQL insert vs. a parameterized-query fix) is a generic, illustrative code pattern — deliberately not attributed to a specific real incident or repo. See `FACTCHECK.md`.

This AI-generated video opens on a silent title card, then teaches a reusable rubric — "The 3 Questions Before You Trust a Fix" (Trace / Consequence / Why) — for deciding how much scrutiny an AI-suggested code fix needs. It moves to a fix that looks correct but still crashes production, shows the framework before any example, walks the rubric through a worked example, names a falsifiability case where quick trust is fine, and closes on a scaffolded viewer task.

**v2 revision (2026-08-17):** the fellow watched the v1 master (56.46s) and found the framework (B01), worked example (B02), and CTA (B04) too vague — they named or labeled the 3 items in each beat without explaining them. Narration for those 3 beats was rewritten with real explanatory depth and re-approved (Gate P v2), `scenes.py` was rebuilt to match with on-screen content that streams the explanations in step with the longer audio, and the whole reel was re-rendered. Runtime grew from 56s to ~1:59 as a direct, fellow-accepted result.

**v3 revision (2026-08-17):** the fellow watched the v2 master (119.03s) and requested two changes: (1) a silent title-card opening beat (new `B00`, 4.55s, no narration — video title + `@HumanitariansAI`) since v1/v2 dove straight into the crash log with zero title/branding intro; (2) the Trace question's jargon — "not just read the diff" — confused the fellow, reworded to "not just read what's different" in both narration and the on-screen caption. All 7 pre-existing beats renumbered B00-B06 -> B01-B07 to make room. Audio regenerated for all 8 beats, `scenes.py` rewritten (renames + new `B00_TitleCard` class), full re-render + re-QC. Runtime grew from 119.03s to 123.61s (the new title card), a direct, fellow-requested result.

**v3.1 patch (2026-08-19), layout-only:** the fellow watched the v3 master and screenshotted a real visual bug in `B01_HookCrashLog`'s first frame — the split-screen divider crossed through the glyphs of the left code panel's longest line ("const q = `INSERT INTO items"). Confirmed with real extracted Manim frames (before and after), not just static analysis: the divider (fixed at x=0) was never actually checked against the left code block's rendered right edge, which fit()'s generous width cap didn't prevent from landing past it. Fixed in `scenes.py` via a new `clear_of_divider()` helper that shifts the whole header+code block by an amount measured from its own rendered bounds, guaranteeing real clearance regardless of future edits. `B03_WorkedExampleDiff` and `B04_FalsifiabilityCase` were audited for the same pattern by direct measurement and found already clear — no changes needed there. No narration/audio change; full pipeline re-rendered (`./art run` then `./art final`), GATE A/W/V all re-confirmed clean (same accepted cosmetic-only MAJOR list as v3). Runtime unchanged at 123.61s (123.605s exact).

## What this covers (and what it deliberately avoids)

Covered: the framework-first structure (rubric shown before any example), a worked example applying all three rubric questions to a code fix, a falsifiability case (a low-stakes date-formatter function) that stress-tests the rubric against an absolutist "never trust AI code" reading, and a concrete 3-step viewer task.

Deliberately avoided: attributing the worked example to a specific real codebase or incident — it's presented as a generic, illustrative pattern (see `FACTCHECK.md` for why, and what was considered and set aside).

## Production state

- Plan: **approved (Gate P v3)** — Gate P (`PEDAGOGY.md`) signed VERDICT: PASS by the fellow, 2026-08-17; re-signed v2 (narration depth) and v3 (title card + wording fix) the same day
- Fact-check gate: **resolved** — no external sourcing required, worked example is generic by design; see `FACTCHECK.md`
- Narration approval: **approved (v3)** — B02's (was B01) Trace line reworded ("not just read the diff" -> "not just read what's different") per fellow request; all other narration unchanged since v2
- Voice: **Bella (`af_bella`)** — confirmed for this cut, matching this fellow's prior videos
- Audio lock: **locked (v3)** — Kokoro `af_bella`, all 8 beats regenerated 2026-08-17 under their new beat IDs. B00 carries a real *silent* mp3 (4.55s, `ffmpeg anullsrc` — not narration; see `beat_sheet.json` B00 `shot.note` for why `audio_file: null` was rejected — it would have silenced the whole film's narration in `compile.py`'s concat). B01/B03/B04/B05/B06/B07 measured at exactly the same durations as their v2 counterparts (narration unchanged); B02 measured 21.74s (was 21.70s, reworded Trace line). See `beat_sheet.json` → `actual_duration_s`.
- Previz: **complete (v3.1)** — new `B00_TitleCard` class added (title + `@HumanitariansAI`, silent); all 7 pre-existing classes renamed to their new B0N IDs; `B02_FrameworkRubric`'s on-screen Trace caption reworded to match narration. v3.1: `B01_HookCrashLog` fixed to add a `clear_of_divider()` helper (see `scenes.py`) so the split-screen divider can no longer cross into either panel's text — was crossing "items" on the left panel's longest line, caught by the fellow and confirmed with real extracted frames. All 8 beats are real Manim scenes, no slates. GATE A/W clean on all 8 classes (B01 re-verified after the v3.1 fix).
- Final render: **complete (v3.1)** — `2026-08-17-why-ai-generated-code-still-needs-a-human.mp4`, 3840×2160 @24fps, **123.61s** (unchanged from v3 — the v3.1 patch is layout-only, no beat duration changed), rendered 2026-08-19 via `./art final`
- Visual QC (GATE V, true clean master, not the watermarked `-slate.mp4` — a known false-positive edge-bleed source): **0 BLOCKER, 7 MAJOR** — identical count/category to v3's accepted cosmetic list (B01/B06/B07: dark-panel contrast heuristic, underfill on B06 and on B07's deliberately compact brand card), re-confirmed clean after the v3.1 divider fix — no new defects introduced. See `BUILD-LOG.md` for the full defect-by-defect account and the v3.1 divider-overlap fix.
- Publishing: **not authorized** — master stays in this folder only

## Compliance note

A channel/fellow sign-off card (B07, renumbered from B06: "@HumanitariansAI, in for Sai Pranavi Jeedigunta") was added 2026-08-17 to match the fellowship's requirement that videos demonstrably come from the volunteer, and the pattern in this fellow's other two videos — see `BUILD-LOG.md`.

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
