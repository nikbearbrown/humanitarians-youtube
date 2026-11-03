# BUILD-LOG — claude-for-legal--claude-liam-leave-tracker

## 2026-08-30 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-for-legal/youtube/claude-liam-leave-tracker/beat_sheet.json`.

**Source-gap finding (logged, not asked — see QUESTION.md for full detail):** the
source sheet is fully "built" (7 beats, all marked VIDEO/filled, dated 2026-07-25) but
its narration text carries literal, never-filled template placeholders (`>`) at every
point where the actual skill-specific fact should be: `"The skill is leave-tracker.
>."`, `"Claude's job: >."`, `SkillTeardownMechanism.body` left as `">"`,
`ClaudeVerdictArtifact.artifactLines` includes a bare `">"`, `"I want to >."`. Its
`source_skill` field points at
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/employment-legal/skills/leave-tracker/SKILL.md`
— searched the entire `books/` tree on this machine; neither that file nor an
`employment-legal` folder exists anywhere. Same defect class as the `clearance` /
`ai-inventory` / `ai-tool-handoff` / `aia-generation` / `amendment-history` siblings
already delivered in this family.

**The call:** reconstructed a generic, defensible account of what a leave-tracker
skill does — check a requested or logged absence against the accrual rules,
eligibility windows, and blackout dates a SKILL.md defines, and return a structured
report that flags anything outside the policy — per the fresh-script Phase 1 rule
("when in doubt, describe behavior generically"). No fact in the resulting script is
Claude-specific, jurisdiction-specific, or an approval-outcome claim; the central fact
(a policy check is not an approval decision) holds regardless of the exact source
text.

**What changed vs. source (per redo contract):**

- **Register:** Teardown → Plain. Source's B03 opened "Here is the Teardown moment"
  and BVDT carried a "Verdict" artifact label with "what it gets right / what it
  bites" framing. This build's B03 states the same class of constraint (accrual rules,
  eligibility windows, blackout dates, flag mismatches) without a design-tell frame,
  and BCRY carries the fact as a plain carry-out sentence.
- **Cold open:** source's `ClaudeComposerAsk` → `BrutalistHesitantWriter`. Writer types
  the newcomer's wrong-guess word "APPROVE" (implying Claude issues a final leave
  decision), hesitates, corrects to "check" → lands "Can Claude check my leave
  request?". Picked up directly by B03's stated scope and BCRY's carry-out.
- **Beat count:** kept the source's 7-beat shape in substance (B00 → B01 anatomy → B02
  pipeline → B03 mechanism → BCRY carry-out → BHTF handoff → BOUT outro), plus the
  fixed hai-simple outro split (`ClaudeTitleOutro` → `OutroSeries` + `OutroCTA`), 7 → 8
  beats — same restructuring precedent as every sibling in this family.
- **Facts/argument:** reconstructed per the source-gap finding above (no real facts to
  carry over). B01's file size (1k) was already filled in the source's own REMOTION
  props (not a placeholder) and is kept verbatim.
- **Voice:** unchanged — Liam, Kokoro `am_onyx`.
- **Close:** BHTF's paste-ready prompt is a new, complete first-person Claude prompt
  (the source's own handoff was an unfilled `"I want to >."` template) using the same
  "explain your input requirements before you act" clause the family's other redos use.

## NO-GENAI / NO-PANTRY LAW

Every one of the source's 7 beats was already REMOTION (`ClaudeComposerAsk`,
`SkillTeardownAnatomy`, `SkillTeardownPipeline`, `SkillTeardownMechanism`,
`ClaudeVerdictArtifact`), so this redo reuses the same REMOTION components rather than
converting to Manim/GRAPHIC — no beat in either version was ever AI-VIDEO, pantry, or a
human-drop slot. `compile.py`'s motion-histogram WARNING (`remotion` 8/8 = 100%, over
the ~40% pantry cap) is expected and accepted for the same reason every prior
all-REMOTION sibling logged it (e.g. `claude-for-legal--claude-liam-clearance`):
NO-GENAI/NO-PANTRY LAW forces every beat to GRAPHIC or REMOTION, and this reel's body
legitimately has no illustrative-figure beats to draw as Manim — it is a
file/pipeline/constraint explainer, not a worked-example narrative.

## Gates

- **TYPECHECK / GATE T:** one flag, confirmed false positive: `[BOUT/eyebrow] text
  ends truncated: 'CLAUDE BASICS · HUMANITARIANS AI'` — the middle-dot `·` character
  triggers the §8.9 truncation heuristic. Identical string, unfixed, already shipped in
  the DELIVERED `clearance`/`brief-section-drafter`/`legal-finance` siblings; left
  as-is per that precedent. Frame QC (below) confirms the full string renders
  unclipped on screen. 0 pixel-beat FAILs, 0 shape FAILs.
- **TIMING LAW (B00):** narration 31 words + `lead_silence_s` 0.8 → measured
  `actual_duration_s` **9.98s**, clears the ≥8s floor. Late frame pull (t=9.5s)
  confirms the full corrected question "Can Claude check / my leave / request?" on
  screen with the correction landed.
- **GATE AUDIO:** PASS, mean_volume **-23.9 dB** (ffmpeg volumedetect, verified
  independently of `compile.py`'s own report), max -2.9 dB — well above the -40 dB
  floor.
- **Gate V (frame QC):** pulled 14 frames every 5s across the full 68.9s runtime, plus
  targeted pulls for B00's late frame and BOUT's title card. All 8 beats legible,
  correctly kerned, no text overlap, safe inset respected, including the B02 pipeline
  diagram (YOUR REQUEST → Read SKILL.md → Execute → Return output → LEAVE REPORT) and
  BOUT's eyebrow rendering the full "CLAUDE BASICS · HUMANITARIANS AI" string
  unclipped. `@HumanitariansAI` folderLabel explicit on BHTF.
- **Lane-check / content-check / frame-check:** all PASS per `compile.py` output (8/8
  beats, no violations, canvas 3840×2160).
- **COMPLETION LAW:** master mp4 mtime (1788109475) newer than beat_sheet.json mtime
  (1788109365); beat_sheet.json was never touched after the compile that produced the
  final master.

## Output

`claude-for-legal--claude-liam-leave-tracker.mp4` — 68.9s, 8/8 beats real (no slate),
native 3840×2160 (Remotion beats render at 4K already, so the master 4K LAW pass
produced the deliverable directly), audible narration throughout (mean_volume -23.9 dB,
ffmpeg-verified). This is the review cut (COMPLETION LAW satisfied).

**Playlist:** Claude Basics. `SUBJECT.json`'s `family: "claude-for-legal"` matches no
prefix in `playlists.json`'s map; falls to the `hai-simple` skill-key fallback →
"Claude Basics" — same resolution every other delivered `claude-for-legal--*` redo in
this family has used (`clearance`, `ai-inventory`, `ai-tool-handoff`, `auto-updater`,
`bar-prep-questions`, `board-minutes`, `brief-section-drafter`).

Metadata file written: `claude-for-legal--claude-liam-leave-tracker.md` (channel
@HumanitariansAI, Playlist: **Claude Basics**, plus the direct code link per the
DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to Phase 4 (4K
render + deliver.py) in this same invocation.
