# BUILD-LOG — financial-services--claude-liam-ic-memo

## 2026-09-01 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/financial-services/youtube/claude-liam-ic-memo/beat_sheet.json`, following
the `financial-services--claude-liam-buyer-list` sibling (built the same day) as the
structural precedent.

**Source check:** the source sheet's `source_skill` field points at
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/financial-services/plugins/agent-plugins/valuation-reviewer/skills/ic-memo/SKILL.md`
— confirmed absent on this machine (scoped `find`/`ls`, not a full-filesystem scan).
Unlike some siblings in this family (e.g. `claude-for-legal--claude-liam-clearance`),
**this source sheet is NOT a placeholder shell** — every beat's `narration_text` and
REMOTION props already carry real, specific facts: file size `2k`, the exact skill
description ("Draft a structured investment committee memo for PE deal approval.
Synthesizes due diligence findings, financial analysis, and deal terms into a
professional IC-ready document."), the verdict recap. No unfilled `>` placeholders
anywhere. So this redo carries those facts forward directly (see QUESTION.md) rather
than reconstructing them generically.

**What changed vs. source (per redo contract):**
- **Register:** Teardown → Plain. Source's B03 framed itself explicitly as "the
  Teardown moment" with "what it gets right / what it bites" verdict language; this
  build's B03 states the same underlying facts (spec, inputs, scope limit) without
  that judgment frame, and the verdict recap (BVDT) becomes a plain carry-out (BCRY).
- **Cold open:** source's `ClaudeComposerAsk` → `BrutalistHesitantWriter` (WRITER LAW).
  Writer types the newcomer's wrong-guess word "app" (implying ic-memo is an
  autonomous app that writes the memo on its own), hesitates, corrects to "skill" →
  lands "How does the ic-memo skill write our memo?" Picked up directly by B01's
  anatomy beat and the carry-out.
- **Beat count:** kept the source's 7-beat shape exactly (B00 → B01 anatomy → B02
  pipeline → B03 mechanism+scope → BCRY [folded from BVDT] → BHTF handoff → BOUT
  outro) — same precedent as `buyer-list`, which kept 7 beats rather than the 8-beat
  BOUT/BCTA split some earlier siblings (e.g. `clearance`) used.
- **Facts/argument:** unchanged — carried forward verbatim from the source's own real
  (non-placeholder) narration and props (file size, skill description, scope limit).
- **Voice:** unchanged — Liam, Kokoro `am_onyx`.
- **Close:** BHTF's paste-ready prompt is new — the source's own handoff prompt named
  a specific deal/shortlist viewers don't have; this build substitutes a generically
  runnable prompt (explain a Claude Skill + walk through a toy 3-step SKILL.md for a
  one-page investment memo), same substitution pattern as `buyer-list`'s BHTF.
- **Outro:** `ClaudeTitleOutro` (locked to @NikBearBrown) → `OutroSeries` with the
  Humanitarians AI skin (`@HumanitariansAI`, eyebrow "HUMANITARIANS AI · CLAUDE
  BASICS"), single beat carrying both the title restate and "Liam, in for Bear."

## NO-GENAI / NO-PANTRY LAW

Every one of the source's 7 beats was already REMOTION (`ClaudeComposerAsk`,
`SkillTeardownAnatomy`, `SkillTeardownPipeline`, `SkillTeardownMechanism`,
`ClaudeVerdictArtifact`), so this redo reuses the same REMOTION components rather than
converting to Manim/GRAPHIC — no beat in either version was ever AI-VIDEO, pantry, or a
human-drop slot. This reel is a file/pipeline/constraint explainer, not a
worked-example narrative, so an all-REMOTION body is the honest shape (no illustrative
figure beats to draw as Manim) — same justification already logged unremarked on every
prior all-REMOTION sibling in this family.

## Gates

- **GATE T (type_check.py):** PASS, 0 FAILs, both before media existed (structural
  pass) and after full render (pixel pass). All prose cards are short pull-quotes
  (B03's on-screen body trimmed to 10 words: "Draft an IC memo from diligence,
  financials, and deal terms." — well under the 12-word §8.5 budget).
- **TIMING LAW (B00):** narration 36 words + `lead_silence_s: 0.8` → measured
  `actual_duration_s` **11.33s**, clears the ≥8s floor / ≥9s window. Frame pulls at
  t=5.0s (mid-typing, "app" visible in terracotta, about to be deleted) and t=10.0s
  (settled, full corrected question "How does the ic-memo skill write our memo?" on
  screen) both confirm the correction lands well before the beat ends.
- **GATE AUDIO:** PASS, mean_volume **-24.0 dB** (ffmpeg `volumedetect`, verified
  independently of `compile.py`'s own report), max -2.8 dB — well above the -40 dB
  floor.
- **Gate V (frame QC):** pulled 15 frames every 5s across the full 76.5s runtime, plus
  a targeted pull at t=74.5s for BOUT. All 7 beats legible, correctly kerned, no text
  overlap, safe inset respected, `@HumanitariansAI` folderLabel explicit on BHTF.
  **Known, previously-logged limitation (not a new defect):** `OutroSeries` imports
  `tokens/vox` (flat white background, crimson underline) rather than the true
  humanitarians cream/terracotta palette — the same componentry gap already logged
  unremarked in the `buyer-list`/`ai-inventory`/`books--claude-liam-legal-finance`
  siblings. BOUT's text and eyebrow are correct and legible; only the background/rule
  color diverges from the palette.
- **Lane-check / content-check / frame-check:** all PASS per `compile.py` output (7/7
  beats, no violations, canvas 3840×2160).
- **COMPLETION LAW:** master mp4 mtime (Sep 1 22:00:41) newer than beat_sheet.json
  mtime (Sep 1 21:51:59); beat_sheet.json was never touched after the compile that
  produced the final master. Audio and resolution independently re-verified via
  ffprobe/ffmpeg (not just trusted from compile.py's own printed report).

## Output

`financial-services--claude-liam-ic-memo.mp4` — 76.5s, 7/7 beats real (no slate),
native 3840×2160 (Remotion beats render at 4K already; `compile.py`'s 4K LAW forced
720p→2160p with no separate upscale needed), audible narration throughout (mean_volume
-24.0 dB, ffmpeg-verified). This is the review cut (COMPLETION LAW satisfied).

**Playlist:** Claude Basics. `SUBJECT.json`'s `family: "financial-services"` matches
no prefix in `playlists.json`'s map; falls to the `hai-simple` skill-key fallback →
"Claude Basics" — same resolution every other delivered `financial-services--*` redo
in this family has used (confirmed by grepping every sibling's `.md` — all say Claude
Basics).

Metadata file written: `financial-services--claude-liam-ic-memo.md` (channel
@HumanitariansAI, Playlist: **Claude Basics**, plus the direct code link per the
DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to Phase 4 (4K
render + deliver.py) in this same invocation.

## 2026-09-01 — Phase 4 delivery

- **4K master:** the compiled master was already native 3840×2160 (all 7 beats are
  Remotion, rendered at 4K natively via `compile.py`'s 4K LAW) — no separate upscale
  render needed. Copied directly to `financial-services--claude-liam-ic-memo-4k.mp4`
  (verified via ffprobe: width=3840, height=2160) so `deliver.py`'s `newest_master()`
  picks it as the explicit 4K variant.
- **Delivered:** `deliver.py --push` — outbox
  `DELIVERY/financial-services--claude-liam-ic-memo/` (4K master + description, syncs
  to Drive `Claude_Bear/` on this machine's Drive-for-desktop mount); repo
  `humanitarians-youtube/claude-bear/financial-services--claude-liam-ic-memo/`
  (README.md + beat_sheet.json + SCRIPT.md + SUBJECT.json + BUILD-LOG.md +
  CARRY-OUT.md + QUESTION.md — no media). Commit `b218ab42`, pushed clean (verified
  `git log` + `git status` + `git log origin/main..HEAD` against `origin/main`, no
  divergence).

**Status: DELIVERED.**
