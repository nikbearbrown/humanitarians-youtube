# BUILD-LOG — knowledge-work-plugins--claude-liam-comp-analysis

## 2026-09-03 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-comp-analysis/beat_sheet.json`,
following the `financial-services--claude-liam-investment-proposal` sibling (same
7-beat skill-teardown source shape) as the structural precedent.

**Source check:** the source sheet's `source_skill` field points at
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/knowledge-work-plugins/human-resources/skills/comp-analysis/SKILL.md`
— confirmed absent on this machine (scoped `find` under
`anthropics/knowledge-work-plugins`, not a full-filesystem scan). The source sheet is
**not** a placeholder shell — its B00 beat carries a real, specific, untruncated skill
description ("Analyze compensation — benchmarking, band placement, and equity modeling.
Trigger with 'what should we pay a [role]', 'is this offer competitive', 'model this
equity grant', or when uploading comp data to find outliers and retention risks.") and
file size `3k`. Several *later* source beats (B03, BVDT, BHTF) carry a
**truncated/garbled copy** of that same description, cut off mid-word (e.g. "...Trigger
with \"what should" / "...only what the SKILL.md specifies. Trigge") — a known
templating defect already logged in this family's other skill-teardown redos. This
build reuses only the untruncated B00 copy of the description everywhere it's needed
(see QUESTION.md), never propagating the truncation.

**What changed vs. source (per redo contract):**
- **Register:** Teardown → Plain. Source's B03 framed itself explicitly as "the
  Teardown moment" with "what it gets right / what it bites" verdict language; this
  build's B03 states the same underlying facts (spec, inputs, scope limit) without that
  judgment frame, and the verdict recap (BVDT) becomes a plain carry-out (BCRY).
- **Cold open:** source's `ClaudeComposerAsk` → `BrutalistHesitantWriter` (WRITER LAW).
  Writer types the newcomer's wrong-guess word "app" (implying comp-analysis is an
  autonomous app that decides pay on its own), hesitates, corrects to "skill" → lands
  "How does the comp-analysis skill set our pay bands?". Picked up directly by B01's
  anatomy beat and the carry-out.
- **Beat count:** kept the source's 7-beat shape exactly (B00 → B01 anatomy → B02
  pipeline → B03 mechanism+scope → BCRY [folded from BVDT] → BHTF handoff → BOUT
  outro) — same precedent as `investment-proposal`/`ic-memo`/`buyer-list`.
- **Facts/argument:** unchanged — carried forward verbatim from the source's own real,
  untruncated narration and props (file size, skill description, scope limit).
- **Voice:** unchanged — Liam, Kokoro `am_onyx`.
- **Close:** BHTF's paste-ready prompt is new — the source's own handoff prompt named a
  business-specific role/pitch viewers don't have; this build substitutes a generically
  runnable prompt (explain a Claude Skill + walk through a toy three-step SKILL.md for
  benchmarking one role's pay against a public salary range), same substitution pattern
  as `investment-proposal`/`ic-memo`/`buyer-list`'s BHTF.
- **Outro:** `ClaudeTitleOutro` (locked to @NikBearBrown) → `OutroSeries` with the
  Humanitarians AI skin (`@HumanitariansAI`, eyebrow "HUMANITARIANS AI · CLAUDE
  BASICS"), single beat carrying both the title restate and "Liam, in for Bear."

## NO-GENAI / NO-PANTRY LAW

Every one of the source's 7 beats was already REMOTION (`ClaudeComposerAsk`,
`SkillTeardownAnatomy`, `SkillTeardownPipeline`, `SkillTeardownMechanism`,
`ClaudeVerdictArtifact`), so this redo reuses the same REMOTION components rather than
converting to Manim/GRAPHIC — no beat in either version was ever AI-VIDEO, pantry, or a
human-drop slot. This is a file/pipeline/constraint explainer, not a worked-example
narrative, so an all-REMOTION body is the honest shape — same justification already
logged unremarked on every prior all-REMOTION sibling in this family.

## Gates

- **GATE T (type_check.py):** PASS, 0 FAILs — run twice: before media existed
  (structural pass, all beats SKIP on §8.10 redundancy) and after full render (pixel
  pass: min-size, overflow, contrast, contrast-local, bbox-overlap, card-clip all PASS
  across 7/7 beats, canvas 3840×2160).
- **TIMING LAW (B00):** narration 35 words + `lead_silence_s: 0.8` → measured
  `actual_duration_s` **11.31s**, clear of the ≥8s floor / ≥9s window. Frame pulls at
  t=5.0s (mid-typing "comp-analyp", stray typo character shown in terracotta per
  ACCENT LAW — the component's per-character mistake simulation, ahead of the later
  "app"→"skill" correction), t=10.0s (correction already landed: "comp-analysis skill"
  visible, still typing "pay ban…"), and t=11.0s (settled, full corrected question "How
  does the comp-analysis skill set our pay bands?" on screen, caret idle) confirm the
  correction lands well before the beat ends.
- **GATE AUDIO:** PASS, mean_volume **-24.0 dB** (ffmpeg `volumedetect`, verified
  independently of `compile.py`'s own report), max -2.8 dB — well above the -40 dB
  floor.
- **Gate V (frame QC):** pulled frames every 8s across the full 76.6s runtime, plus
  targeted B00 pulls at t=5s/t=10s/t=11s. All 7 beats legible, correctly kerned, no
  text overlap, safe inset respected, `@HumanitariansAI` folderLabel explicit on BHTF.
  **Known, previously-logged limitation (not a new defect):** `OutroSeries` renders on
  a flat white background with a crimson underline rather than the true humanitarians
  cream/terracotta palette — the same componentry gap already logged unremarked in the
  `investment-proposal`/`ic-memo`/`buyer-list`/`ai-inventory` siblings. BOUT's text and
  eyebrow are correct and legible; only the background/rule color diverges from the
  palette.
- **Lane-check / content-check / frame-check:** all PASS per `compile.py` output (7/7
  beats, no violations, canvas 3840×2160).
- **COMPLETION LAW:** master mp4 mtime (epoch 1788410929) newer than beat_sheet.json
  mtime (epoch 1788410859) — the build-stamp write to beat_sheet.json happens mid-compile,
  before the mp4 is written; beat_sheet.json was never touched after that stamp. Audio
  and resolution independently re-verified via ffprobe/ffmpeg (not just trusted from
  compile.py's own printed report): 3840×2160, mean_volume -24.0 dB, duration 76.58s.

## Output

`knowledge-work-plugins--claude-liam-comp-analysis.mp4` — 76.6s, 7/7 beats real (no
slate), native 3840×2160 (Remotion beats render at 4K already; `compile.py`'s 4K LAW
forced 720p→2160p with no separate upscale needed), audible narration throughout
(mean_volume -24.0 dB, ffmpeg-verified). This is the review cut (COMPLETION LAW
satisfied).

**Playlist:** Extending Claude — Skills, Plugins & Connectors. `SUBJECT.json`'s
`family: "knowledge-work-plugins"` matches that exact key in `playlists.json`'s map.

Metadata file written: `knowledge-work-plugins--claude-liam-comp-analysis.md` (channel
@HumanitariansAI, Playlist: **Extending Claude — Skills, Plugins & Connectors**, plus
the direct code link per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to Phase 4 (4K
render + deliver.py) in this same invocation.

## 2026-09-03 — Phase 4 delivery

- **4K master:** the compiled master was already native 3840×2160 (all 7 beats are
  Remotion, rendered at 4K natively via `compile.py`'s 4K LAW) — no separate upscale
  render needed. Copied directly to
  `knowledge-work-plugins--claude-liam-comp-analysis-4k.mp4` (verified via ffprobe:
  width=3840, height=2160) so `deliver.py`'s `newest_master()` picks it as the explicit
  4K variant.
- **Delivered:** `deliver.py --push` — outbox
  `DELIVERY/knowledge-work-plugins--claude-liam-comp-analysis/` (4K master +
  description, syncs to Drive `Claude_Bear/` on this machine's Drive-for-desktop mount);
  repo `humanitarians-youtube/claude-bear/knowledge-work-plugins--claude-liam-comp-analysis/`
  (README.md + beat_sheet.json + SCRIPT.md + SUBJECT.json + BUILD-LOG.md + CARRY-OUT.md +
  QUESTION.md — no media). Commit `a4857b53`, pushed clean in one shot (verified
  `git log` + `git status` + `git log origin/main..HEAD` against `origin/main`, no
  divergence, working tree clean).

**Status: DELIVERED.**
