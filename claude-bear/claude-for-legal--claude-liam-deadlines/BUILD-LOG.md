# BUILD-LOG — claude-for-legal--claude-liam-deadlines

## 2026-08-29 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-for-legal/youtube/claude-liam-deadlines/beat_sheet.json`.

**Source-gap finding (logged, not asked — see QUESTION.md for full detail):** the
source sheet is fully "built" (7 beats, all marked VIDEO/filled, dated 2026-07-25) but
its narration text carries literal, never-filled template placeholders (`>`) at every
point where the actual skill-specific fact should be: `"The skill is deadlines. >."`,
`"Claude's job: >."`, `SkillTeardownMechanism.body` left as `">"`,
`ClaudeVerdictArtifact.artifactLines` includes a bare `">"`, `"I want to >."`. Its
`source_skill` field points at
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/legal-clinic/skills/deadlines/SKILL.md`
— searched the entire `books/` tree on this machine; neither that file nor a
`legal-clinic` folder exists anywhere. Same defect class as the `clearance` /
`ai-inventory` / `ai-tool-handoff` / `aia-generation` / `amendment-history` siblings
already delivered in this family.

**The call:** reconstructed a generic, defensible account of what a legal-deadlines
skill does — take a triggering date and a stated rule (a filing window, a response
period, a limitations period), compute the resulting date, and return a calendar of
what's due and when — per the fresh-script Phase 1 rule ("when in doubt, describe
behavior generically"). No fact in the resulting script is Claude-specific,
jurisdiction-specific, or a legal-outcome claim; the central fact (the skill computes
from the rule you give it — it does not independently know or discover the controlling
rule) holds regardless of the exact source text.

**What changed vs. source (per redo contract):**

- **Register:** Teardown → Plain. Source's B03 opened "Here is the Teardown moment" and
  BVDT carried a "Verdict" artifact label with "what it gets right / what it bites"
  framing. This build's B03 states the same class of constraint (triggering date, rule,
  computed result) without a design-tell frame, and BCRY carries the fact as a plain
  carry-out sentence.
- **Cold open:** source's `ClaudeComposerAsk` → `BrutalistHesitantWriter`. Writer types
  the newcomer's wrong-guess word "TRACK" (implying Claude independently monitors or
  discovers deadlines), hesitates, corrects to "compute" → lands "Can Claude compute my
  deadlines?". Picked up directly by B03's stated scope and BCRY's carry-out.
- **Beat count:** kept the source's 7-beat shape in substance (B00 → B01 anatomy → B02
  pipeline → B03 mechanism → BVDT/BCRY carry-out → BHTF handoff → BOUT outro), plus the
  fixed hai-simple outro split (`ClaudeTitleOutro` → `OutroSeries` + `OutroCTA`), 7 → 8
  beats — same restructuring precedent as every sibling in this family.
- **Facts/argument:** reconstructed per the source-gap finding above (no real facts to
  carry over). B01's file size (10k, kept verbatim from source's own
  `SkillTeardownAnatomy` prop) and B02's phase labels were already filled in the
  source's own REMOTION props (not placeholders) and are kept.
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
all-REMOTION sibling logged it (e.g. `claude-for-legal--claude-liam-clearance`,
`brief-section-drafter`): NO-GENAI/NO-PANTRY LAW forces every beat to GRAPHIC or
REMOTION, and this reel's body legitimately has no illustrative-figure beats to draw as
Manim — it is a file/pipeline/constraint explainer, not a worked-example narrative.

## Gates

- **TYPECHECK / GATE T:** one flag, confirmed false positive: `[BOUT/eyebrow] text
  ends truncated: 'CLAUDE BASICS · HUMANITARIANS AI'` — the middle-dot `·` character
  triggers the §8.9 truncation heuristic. Identical string, unfixed, already shipped in
  the DELIVERED `clearance`, `brief-section-drafter`, and `legal-finance` siblings; left
  as-is per that precedent rather than reworded away from house style. 0 pixel-beat
  FAILs, 0 shape FAILs.
- **TIMING LAW (B00):** narration 32 words + `lead_silence_s` 0.8 → measured
  `actual_duration_s` **10.09s**, clears the ≥8s floor. Frame QC at t=9.5s confirms the
  full corrected question "Can Claude compute / my deadlines?" on screen with the
  correction landed; an earlier-window frame confirms the wrong-guess word "TRACK" in
  accent mid-hesitation before the correction.
- **GATE AUDIO:** PASS, mean_volume **-24.0 dB** (ffmpeg volumedetect, verified
  independently of `compile.py`'s own report), max -2.9 dB — well above the -40 dB
  floor.
- **Gate V (frame QC):** pulled 14 frames every 5s across the full 68.2s runtime, plus a
  targeted pull at t=9.5s for B00. All 8 beats legible, correctly kerned, no text
  overlap, safe inset respected. `OutroCTA` renders on flat white rather than the
  humanitarians cream ground — same shared-component behavior already logged unremarked
  in sibling reels (e.g. `clearance`, `ai-inventory`). `@HumanitariansAI` folderLabel
  explicit on BHTF. BHTF's `ClaudeComposerAsk` shows the component's own default model
  badge ("Fable 5") since no `modelLabel`/`effortLabel` prop was set — identical,
  unremarked precedent in `clearance`'s BHTF beat (same prop set, same component
  default).
- **Lane-check / content-check / frame-check:** all PASS per `compile.py` output (8/8
  beats, no violations, canvas 3840×2160 native from Remotion source, review cut
  compiled at 1280×720).
- **COMPLETION LAW:** review-cut mp4 mtime (1788044311) newer than beat_sheet.json
  mtime (1788044277); beat_sheet.json was never touched after the compile that produced
  it.

## Output

`claude-for-legal--claude-liam-deadlines-slate.mp4` — 68.2s, 8/8 beats real (no slate
despite the filename — `compile.py --review` names its output this way regardless of
fill state; every slot is VIDEO), 1280×720 review resolution, audible narration
throughout (mean_volume -24.0 dB, ffmpeg-verified). This is the review cut (COMPLETION
LAW satisfied).

**Playlist:** Claude Basics. `SUBJECT.json`'s `family: "claude-for-legal"` matches no
prefix in `playlists.json`'s map; falls to the `hai-simple` skill-key fallback →
"Claude Basics" — same resolution every other delivered `claude-for-legal--*` redo in
this family has used (`clearance`, `ai-inventory`, `ai-tool-handoff`, `auto-updater`,
`bar-prep-questions`, `board-minutes`, `brief-section-drafter`).

Metadata file written: `claude-for-legal--claude-liam-deadlines.md` (channel
@HumanitariansAI, Playlist: **Claude Basics**, plus the direct code link per the
DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to Phase 4 (4K
render + deliver.py) in this same invocation.
