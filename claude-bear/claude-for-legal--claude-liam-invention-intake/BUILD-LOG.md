# BUILD-LOG — claude-for-legal--claude-liam-invention-intake

## 2026-08-30 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-for-legal/youtube/claude-liam-invention-intake/beat_sheet.json`.

**Source-skill finding — DIFFERENT from this family's usual source-gap:** the source
sheet is fully "built" (7 beats, all VIDEO/filled, dated 2026-07-25) and its narration
carries the same unfilled `>` template placeholders the family's other redos hit
(`"The skill is invention-intake. >."`, `"Claude's job: >."`, `SkillTeardownMechanism.body`
= `">"`, a bare `">"` in `ClaudeVerdictArtifact.artifactLines`, `"I want to >."`). Its
`source_skill` field points at
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/ip-legal/skills/invention-intake/SKILL.md`
— that exact path does not exist on this machine, but the REAL file was found at the
parallel path `/Users/nik/Documents/Cowork/anthropics/claude-for-legal/ip-legal/skills/invention-intake/SKILL.md`
(22,732 bytes, matching the source sheet's own already-filled `"size": "22k"` prop —
confirms it's the same file). Read it completely (see QUESTION.md for the full fact
list). Unlike the `clearance`/`ai-inventory`/`ai-tool-handoff`/`diligence-issue-extraction`
siblings, this build used the REAL SKILL.md rather than reconstructing generically:
six named screens (novelty, obviousness, § 101 eligibility, public-disclosure/bar
dates, detectability, strategic value), a three-word bottom-line verdict (PURSUE /
INVESTIGATE / DECLINE), the explicit guardrail "Never say patentable," and the file's
own worked example (a cache-eviction algorithm using a learned model instead of LRU)
reused verbatim as the handoff-prompt anchor.

**What changed vs. source (per redo contract):**

- **Register:** Teardown → Plain. Source's B03 opened "Here is the Teardown moment"
  and BVDT carried a "Verdict" artifact label with "what it gets right / what it
  bites" framing. This build's B03 states the same class of constraint (six screens,
  three-word verdict, never "patentable") without a design-tell frame, and BCRY
  carries the fact as a plain carry-out sentence.
- **Cold open:** source's `ClaudeComposerAsk` → `BrutalistHesitantWriter`. Writer types
  the newcomer's wrong-guess word "PATENT" (implying Claude issues or grants a patent),
  hesitates, corrects to "screen" → lands "Can Claude screen my invention for me?".
  Picked up directly by B03's stated scope and BCRY's carry-out.
- **Beat count:** kept the source's 7-beat shape in substance (B00 → B01 anatomy → B02
  pipeline → B03 mechanism → BVDT/BCRY carry-out → BHTF handoff → BOUT outro), plus the
  fixed hai-simple outro split (`ClaudeTitleOutro` → `OutroSeries` + `OutroCTA`), 7 → 8
  beats — same restructuring precedent as every sibling in this family.
- **Facts/argument:** real, pulled from the found SKILL.md (see above and QUESTION.md)
  rather than reconstructed generically — a first for this family's redos.
- **Voice:** unchanged — Liam, Kokoro `am_onyx`.
- **Close:** BHTF's paste-ready prompt uses the source SKILL.md's own worked example
  (cache-eviction algorithm, learned model vs. LRU, internal prototype, not yet
  disclosed) with the same "explain your input requirements before you act" clause the
  family's other redos use.

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
  the DELIVERED `clearance`/`brief-section-drafter`/`legal-finance` siblings; left as-is
  per that precedent rather than reworded away from house style. Confirmed by frame
  pull (BOUT frame, t=73.8s) that the eyebrow line is fully legible, not truncated.
  0 pixel-beat FAILs, 0 shape FAILs.
- **TIMING LAW (B00):** narration 30 words + `lead_silence_s` 0.8 → measured
  `actual_duration_s` **9.8s**, clears the ≥8s floor (extended to 9.8s by compile.py's
  audio-clock rule). Late frame pull (t=9.3s) confirms the full corrected question
  "Can Claude screen / my invention / for me?" on screen with the correction landed.
- **GATE AUDIO:** PASS, mean_volume **-24.0 dB** (ffmpeg volumedetect, verified
  independently of `compile.py`'s own report), max -3.0 dB — well above the -40 dB
  floor.
- **Gate V (frame QC):** pulled 16 frames every 5s across the full 78.2s runtime, plus
  targeted pulls at t=9.3s (B00 correction), t=48s (BCRY), and t=73.8s (BOUT). All 8
  beats legible, correctly kerned, no text overlap, safe inset respected. `OutroSeries`/
  `OutroCTA` render on flat white rather than the humanitarians cream ground — same
  shared-component behavior already logged unremarked in sibling reels (`clearance`,
  `ai-inventory`, `books--claude-liam-legal-finance`). `@HumanitariansAI` folderLabel
  explicit on BHTF.
- **Lane-check / content-check / frame-check:** all PASS per `compile.py` output (8/8
  beats, no violations, canvas 3840×2160).
- **COMPLETION LAW:** master mp4 mtime (1788094020) newer than beat_sheet.json mtime
  (1788093989); beat_sheet.json was never touched after the compile that produced the
  review cut.

## Output

`claude-for-legal--claude-liam-invention-intake-slate.mp4` — 78.2s, 8/8 beats real (no
pipeline-owned slate; `-slate` is compile.py's fixed `--review` naming convention, not
an unfilled beat — `lane-check` confirms `known_slates=[]`), native 3840×2160 (Remotion
beats render at 4K already), audible narration throughout (mean_volume -24.0 dB,
ffmpeg-verified). This is the review cut (COMPLETION LAW satisfied).

**Playlist:** Claude Basics. `SUBJECT.json`'s `family: "claude-for-legal"` matches no
prefix in `playlists.json`'s map; falls to the `hai-simple` skill-key fallback →
"Claude Basics" — same resolution every other delivered `claude-for-legal--*` redo in
this family has used.

Metadata file written: `claude-for-legal--claude-liam-invention-intake.md` (channel
@HumanitariansAI, Playlist: **Claude Basics**, plus the direct code link per the
DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to Phase 4 (4K
render + deliver.py) in this same invocation.
