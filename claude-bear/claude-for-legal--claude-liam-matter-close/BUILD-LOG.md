# BUILD-LOG — claude-for-legal--claude-liam-matter-close

## 2026-08-30 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-for-legal/youtube/claude-liam-matter-close/beat_sheet.json`.

**Source check:** the source sheet's `source_skill` field points at
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/litigation-legal/skills/matter-close/SKILL.md`
— searched the entire `books/` tree on this machine; neither that file nor a
`litigation-legal` folder exists here. Unlike several siblings in this family
(`clearance`, `ai-inventory`, `ai-tool-handoff`, `aia-generation`, `amendment-history`),
this source's own narration was **fully filled in** — no unfilled `>` template
placeholders. The complete task statement ("Close a matter — capture outcome, final
exposure, and lessons, then archive it out of the active portfolio without deleting the
record...") appears verbatim in the source's B00 and B03 beats. No reconstruction was
needed; every fact used in this redo is carried directly from that text. See
QUESTION.md for the full source-file check.

**What changed vs. source (per redo contract):**

- **Register:** Teardown → Plain. Source's B03 opened "Here is the Teardown moment"
  and BVDT carried "what it gets right / what it bites" verdict framing. This build's
  B03 states the same constraint (capture scope, archive-not-delete) without a design-
  tell frame, and BCRY carries the fact as a plain carry-out sentence.
- **Cold open:** source's `ClaudeComposerAsk` → `BrutalistHesitantWriter`. Writer types
  the newcomer's wrong-guess word "DELETE" (implying closing a matter erases it),
  hesitates, corrects to "archive" → lands "Can Claude archive a closed matter when
  it's done?". Picked up directly by B03's stated scope and BCRY's carry-out.
- **Beat count:** kept the source's 7-beat shape in substance (B00 → B01 anatomy → B02
  pipeline → B03 mechanism → BVDT/BCRY carry-out → BHTF handoff → BOUT outro), plus the
  fixed hai-simple outro split (`ClaudeTitleOutro` → `OutroSeries` + `OutroCTA`), 7 → 8
  beats — same restructuring precedent as the `clearance` sibling in this family.
- **Facts/argument:** unchanged from source (no source-gap this time) — B01's file size
  (6k) and B02's phase labels were already filled in the source's own REMOTION props and
  are kept verbatim; B03's constraint and BCRY's carry-out are compressed directly from
  the source's own task statement and BVDT verdict-recap text.
- **Voice:** unchanged — Liam, Kokoro `am_onyx`.
- **Close:** BHTF's paste-ready prompt reuses the source's own handoff prompt (which was
  already fully filled, unlike `clearance`'s unfilled template) with the family's
  standard "explain your input requirements before you act" clause appended.

## NO-GENAI / NO-PANTRY LAW

Every one of the source's 7 beats was already REMOTION (`ClaudeComposerAsk`,
`SkillTeardownAnatomy`, `SkillTeardownPipeline`, `SkillTeardownMechanism`,
`ClaudeVerdictArtifact`), so this redo reuses the same REMOTION components rather than
converting to Manim/GRAPHIC — no beat in either version was ever AI-VIDEO, pantry, or a
human-drop slot. `compile.py`'s motion-histogram WARNING (`remotion` 8/8 = 100%, over
the ~40% pantry cap) is expected and accepted for the same reason every prior
all-REMOTION sibling logged it: NO-GENAI/NO-PANTRY LAW forces every beat to GRAPHIC or
REMOTION, and this reel's body legitimately has no illustrative-figure beats to draw as
Manim — it is a file/pipeline/constraint explainer, not a worked-example narrative.

## Gates

- **TYPECHECK / GATE T:** one flag, confirmed false positive: `[BOUT/eyebrow] text
  ends truncated: 'CLAUDE BASICS · HUMANITARIANS AI'` — the middle-dot `·` character
  triggers the §8.9 truncation heuristic. Identical string, unfixed, already shipped in
  the DELIVERED `clearance`/`brief-section-drafter`/`legal-finance` siblings; left as-is
  per that precedent rather than reworded away from house style. 0 pixel-beat FAILs, 0
  shape FAILs.
- **TIMING LAW (B00):** narration 29 words + `lead_silence_s` 0.8 → measured
  `actual_duration_s` **9.54s**, clears the ≥8s floor. Late frame pull (t=8.7s) confirms
  the full corrected question "Can Claude archive / a closed matter / when it'—" already
  on screen (correction landed well before the beat ends); an earlier pull (t=5s) shows
  the writer mid-correction, confirming the hesitation is visible in real time, not just
  at the very end.
- **GATE AUDIO:** PASS, mean_volume **-24.0 dB** (ffmpeg volumedetect, verified
  independently of `compile.py`'s own report), max -2.9 dB — well above the -40 dB
  floor.
- **Gate V (frame QC):** pulled 15 frames every 5s across the full 72.7s runtime, plus a
  targeted pull at t=8.7s for B00's correction. All 8 beats legible, correctly kerned,
  no text overlap, safe inset respected. `OutroSeries`/`OutroCTA` render on flat white
  rather than the humanitarians cream ground — same shared-component behavior already
  logged unremarked in sibling reels (`clearance`, `ai-inventory`,
  `books--claude-liam-legal-finance`). `@HumanitariansAI` folderLabel explicit on BHTF.
- **Lane-check / content-check / frame-check:** all PASS per `compile.py` output (8/8
  beats, no violations, canvas 3840×2160).
- **COMPLETION LAW:** master mp4 mtime (1788122302) newer than beat_sheet.json mtime
  (1788122200); beat_sheet.json was never touched after the compile that produced the
  final master.

## Output

`claude-for-legal--claude-liam-matter-close.mp4` — 72.7s, 8/8 beats real (no slate),
native 3840×2160 (Remotion beats render at 4K already; `compile.py`'s 4K LAW forced the
clean master to 2160p), audible narration throughout (mean_volume -24.0 dB,
ffmpeg-verified). This is the review cut (COMPLETION LAW satisfied).

**Playlist:** Claude Basics. `SUBJECT.json`'s `family: "claude-for-legal"` matches no
prefix in `playlists.json`'s map; falls to the `hai-simple` skill-key fallback →
"Claude Basics" — same resolution every other delivered `claude-for-legal--*` redo in
this family has used (`clearance`, `ai-inventory`, `ai-tool-handoff`, `auto-updater`,
`bar-prep-questions`, `board-minutes`, `brief-section-drafter`, `case-brief`).

Metadata file written: `claude-for-legal--claude-liam-matter-close.md` (channel
@HumanitariansAI, Playlist: **Claude Basics**, plus the direct code link per the
DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to Phase 4 (4K
render + deliver.py) in this same invocation.

## 2026-08-30 — Phase 4 delivery

- **4K master:** `compile.py`'s 4K LAW forces the clean master from 720p to 2160p
  automatically (no `--review` flag) — wrote
  `claude-for-legal--claude-liam-matter-close.mp4` natively at 3840x2160 (Remotion beats
  were already rendered at native 4K), 72.7s, 8/8 beats real, mean_volume -24.0 dB.
  Copied to `-4k.mp4` so `deliver.py`'s `newest_master()` picks it as the explicit 4K
  variant.
