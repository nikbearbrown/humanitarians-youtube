# BUILD-LOG — financial-services--claude-liam-investment-proposal

## 2026-09-01 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/financial-services/youtube/claude-liam-investment-proposal/beat_sheet.json`,
following the `financial-services--claude-liam-ic-memo` sibling (same family, same
source shape) as the structural precedent.

**Source check:** the source sheet's `source_skill` field points at
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/financial-services/plugins/agent-plugins/meeting-prep-agent/skills/investment-proposal/SKILL.md`
— confirmed absent on this machine (scoped `find` under `anthropics/financial-services`
and for `meeting-prep-agent` generally, not a full-filesystem scan). The source sheet is
**not** a placeholder shell — every beat's `narration_text` and REMOTION props already
carry real, specific facts: file size `3k`, the exact skill description ("Create
professional investment proposals for prospective clients. Covers the firm's approach,
proposed allocation, expected outcomes, and fee structure. Use when pitching new clients
or presenting a new investment strategy."), the trigger phrases, the verdict recap. No
unfilled `>` placeholders anywhere. This redo carries those facts forward directly (see
QUESTION.md) rather than reconstructing them generically.

**What changed vs. source (per redo contract):**
- **Register:** Teardown → Plain. Source's B03 framed itself explicitly as "the
  Teardown moment" with "what it gets right / what it bites" verdict language; this
  build's B03 states the same underlying facts (spec, inputs, scope limit) without that
  judgment frame, and the verdict recap (BVDT) becomes a plain carry-out (BCRY).
- **Cold open:** source's `ClaudeComposerAsk` → `BrutalistHesitantWriter` (WRITER LAW).
  Writer types the newcomer's wrong-guess word "app" (implying investment-proposal is an
  autonomous app that picks the client's investments on its own), hesitates, corrects to
  "skill" → lands "How does the investment-proposal skill write our proposal?". Picked up
  directly by B01's anatomy beat and the carry-out.
- **Beat count:** kept the source's 7-beat shape exactly (B00 → B01 anatomy → B02
  pipeline → B03 mechanism+scope → BCRY [folded from BVDT] → BHTF handoff → BOUT outro) —
  same precedent as `ic-memo`/`buyer-list`, which kept 7 beats.
- **Facts/argument:** unchanged — carried forward verbatim from the source's own real
  (non-placeholder) narration and props (file size, skill description, scope limit).
- **Voice:** unchanged — Liam, Kokoro `am_onyx`.
- **Close:** BHTF's paste-ready prompt is new — the source's own handoff prompt named a
  specific client/pitch viewers don't have; this build substitutes a generically runnable
  prompt (explain a Claude Skill + walk through a toy three-step SKILL.md for a one-page
  investment proposal outline), same substitution pattern as `ic-memo`/`buyer-list`'s
  BHTF.
- **Outro:** `ClaudeTitleOutro` (locked to @NikBearBrown) → `OutroSeries` with the
  Humanitarians AI skin (`@HumanitariansAI`, eyebrow "HUMANITARIANS AI · CLAUDE BASICS"),
  single beat carrying both the title restate and "Liam, in for Bear."

## NO-GENAI / NO-PANTRY LAW

Every one of the source's 7 beats was already REMOTION (`ClaudeComposerAsk`,
`SkillTeardownAnatomy`, `SkillTeardownPipeline`, `SkillTeardownMechanism`,
`ClaudeVerdictArtifact`), so this redo reuses the same REMOTION components rather than
converting to Manim/GRAPHIC — no beat in either version was ever AI-VIDEO, pantry, or a
human-drop slot. This is a file/pipeline/constraint explainer, not a worked-example
narrative, so an all-REMOTION body is the honest shape — same justification already
logged unremarked on every prior all-REMOTION sibling in this family (`ic-memo`,
`buyer-list`).

## Gates

- **GATE T (type_check.py):** PASS, 0 FAILs — run twice: before media existed
  (structural pass, all beats SKIP on §8.10 redundancy) and after full render (pixel
  pass: min-size, overflow, contrast, contrast-local, bbox-overlap, card-clip all PASS
  across 7/7 beats, canvas 3840×2160).
- **TIMING LAW (B00):** narration 37 words + `lead_silence_s: 0.8` → measured
  `actual_duration_s` **12.42s**, well clear of the ≥8s floor / ≥9s window. Frame pulls
  at t=5.0s (mid-typing "investment-p…", with a stray typo character shown in
  terracotta per ACCENT LAW — the component's per-character mistake simulation, ahead of
  the later "app"→"skill" correction) and t=11.0s (settled, full corrected question "How
  does the investment-proposal skill write our proposal?" on screen) both confirm the
  correction lands well before the beat ends.
- **GATE AUDIO:** PASS, mean_volume **-24.0 dB** (ffmpeg `volumedetect`, verified
  independently of `compile.py`'s own report), max -2.8 dB — well above the -40 dB
  floor.
- **Gate V (frame QC):** pulled frames every 5s across the full 79.5s runtime, plus
  targeted B00 pulls at t=5s/t=11s. All 7 beats legible, correctly kerned, no text
  overlap, safe inset respected, `@HumanitariansAI` folderLabel explicit on BHTF.
  **Known, previously-logged limitation (not a new defect):** `OutroSeries` renders on
  a flat white background with a crimson underline rather than the true humanitarians
  cream/terracotta palette — the same componentry gap already logged unremarked in the
  `ic-memo`/`buyer-list`/`ai-inventory` siblings. BOUT's text and eyebrow are correct
  and legible; only the background/rule color diverges from the palette.
- **Lane-check / content-check / frame-check:** all PASS per `compile.py` output (7/7
  beats, no violations, canvas 3840×2160).
- **COMPLETION LAW:** master mp4 mtime (Sep 1 23:36:02, epoch 1788320162) newer than
  beat_sheet.json mtime (epoch 1788320052); beat_sheet.json was never touched after the
  compile that produced the final master. Audio and resolution independently
  re-verified via ffprobe/ffmpeg (not just trusted from compile.py's own printed
  report): 3840×2160, mean_volume -24.0 dB, duration 79.5s.

## Output

`financial-services--claude-liam-investment-proposal.mp4` — 79.5s, 7/7 beats real (no
slate), native 3840×2160 (Remotion beats render at 4K already; `compile.py`'s 4K LAW
forced 720p→2160p with no separate upscale needed), audible narration throughout
(mean_volume -24.0 dB, ffmpeg-verified). This is the review cut (COMPLETION LAW
satisfied).

**Playlist:** Claude Basics. `SUBJECT.json`'s `family: "financial-services"` matches no
prefix in `playlists.json`'s map; falls to the `hai-simple` skill-key fallback →
"Claude Basics" — same resolution every other delivered `financial-services--*` redo in
this family has used.

Metadata file written: `financial-services--claude-liam-investment-proposal.md`
(channel @HumanitariansAI, Playlist: **Claude Basics**, plus the direct code link per
the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to Phase 4 (4K
render + deliver.py) in this same invocation.
