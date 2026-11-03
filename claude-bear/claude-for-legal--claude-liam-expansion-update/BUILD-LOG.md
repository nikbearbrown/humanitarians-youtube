# BUILD-LOG — claude-for-legal--claude-liam-expansion-update

## 2026-08-30 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-for-legal/youtube/claude-liam-expansion-update/beat_sheet.json`.

**Source-gap finding (logged, not asked — see QUESTION.md for full detail):** the
source sheet is fully "built" (7 beats, all marked VIDEO/filled, dated 2026-07-25) but
its narration text carries literal, never-filled template placeholders (`>`) at every
point where the actual skill-specific fact should be: `"The skill is expansion-update.
>."`, `"Claude's job: >."` (`SkillTeardownMechanism.body` left as `">"`),
`ClaudeVerdictArtifact.artifactLines` includes a bare `">"`, `"I want to >."` (BHTF's
own handoff prompt). Its `source_skill` field points at
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/employment-legal/skills/expansion-update/SKILL.md`
— searched the entire `books/` tree on this machine; neither that file nor an
`employment-legal` folder exists anywhere. Same defect class as the `clearance` /
`expansion-kickoff` / `entity-compliance` / `ai-inventory` / `ai-tool-handoff` siblings
already delivered in this family.

**The call:** reconstructed a generic, defensible account of what an employment-law
"expansion update" skill does — compare an existing policy document (handbook, offer
letter template, notice) against the requirements of a new jurisdiction or expanded
scope, and flag the specific sections that need updating. Described generically per the
fresh-script Phase 1 rule ("when in doubt, describe behavior generically") rather than
inventing a specific state's statute, a specific handbook clause, or a legal outcome.
No fact in the resulting script is Claude-specific, jurisdiction-specific, or a
legal-conclusion claim; the central fact (a flagged checklist is not a finished,
lawyer-approved handbook) holds regardless of the exact source text.

**What changed vs. source (per redo contract):**

- **Register:** Teardown → Plain. Source's B03 opened "Here is the Teardown moment" and
  BVDT carried a "Verdict" artifact label with "what it gets right / what it bites"
  framing. This build's B03 states the same class of constraint (compare against
  checklist, flag sections) without a design-tell frame, and BCRY carries the fact as a
  plain carry-out sentence.
- **Cold open:** source's `ClaudeComposerAsk` → `BrutalistHesitantWriter`. Writer types
  the newcomer's wrong-guess word "REWRITE" (implying Claude autonomously produces a
  finished, ready-to-publish handbook), hesitates, corrects to "flag" → lands "Can
  Claude flag our handbook for the new state?". Picked up directly by B03's stated
  scope and BCRY's carry-out.
- **Beat count:** kept the source's 7-beat shape in substance (B00 → B01 anatomy → B02
  pipeline → B03 mechanism → BVDT/BCRY carry-out → BHTF handoff → BOUT outro), plus the
  fixed hai-simple outro split (`ClaudeTitleOutro` → `OutroSeries` + `OutroCTA`), 7 → 8
  beats — same restructuring precedent as every sibling in this family.
- **Facts/argument:** reconstructed per the source-gap finding above (no real facts to
  carry over). B01's file size (2k) and B02's phase labels were already filled in the
  source's own REMOTION props (not placeholders) and are kept verbatim.
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

## One-shot / process notes

The first `remotion_scenes.py` full-sheet call auto-backgrounded after exceeding the
tool's 120s foreground timeout; blocked on the OS task via `TaskOutput` rather than
ending the turn (per the ONE-SHOT invocation rule). 7 of 8 beats rendered clean in that
run; BHTF (`ClaudeComposerAsk`) reported FAIL with only an unrelated Remotion
package-version warning printed after it — no root-cause error text was visible in the
truncated log. Retried `--only BHTF --force` in the foreground; it reported "lock held
by pid=98461 — taking over" (an ad hoc shell background attempt from mid-diagnosis) and
completed successfully, producing `media/BHTF.mp4` (14.1s). All 8 media files verified
present before compiling.

## Gates

- **TYPECHECK / GATE T:** one flag, confirmed false positive: `[BOUT/eyebrow] text ends
  truncated: 'CLAUDE BASICS · HUMANITARIANS AI'` — the middle-dot `·` character
  triggers the §8.9 truncation heuristic. Identical string, unfixed, already shipped in
  the DELIVERED `clearance`/`brief-section-drafter`/`legal-finance` siblings; left as-is
  per that precedent rather than reworded away from house style. 0 pixel-beat FAILs, 0
  shape FAILs.
- **TIMING LAW (B00):** narration 34 words + `lead_silence_s` 0.8 → measured
  `actual_duration_s` **9.81s**, clears the ≥8s floor. Late frame pull (t=9.3s)
  confirms the corrected question "Can Claude flag / our handbook / for the new stat[e]"
  on screen with the correction ("flag", not the accent-colored "REWRITE") already
  landed.
- **GATE AUDIO:** PASS, mean_volume **-23.9 dB** (ffmpeg volumedetect, verified
  independently of `compile.py`'s own report), max -3.0 dB — well above the -40 dB
  floor.
- **Gate V (frame QC):** pulled 14 frames every 5s across the full 70.4s runtime, plus
  targeted pulls at t=9.3s (B00 correction), t=66.0s (BOUT title card), and t=69.5s
  (BCTA subscribe/handle card). All 8 beats legible, correctly kerned, no text overlap,
  safe inset respected. `OutroSeries`/`OutroCTA` render on flat white rather than the
  humanitarians cream ground — same shared-component behavior already logged unremarked
  in sibling reels (e.g. `clearance`, `ai-inventory`). `@HumanitariansAI` folderLabel
  explicit on BHTF.
- **Lane-check / content-check / frame-check:** all PASS per `compile.py` output (8/8
  beats, no violations, canvas 3840×2160).
- **COMPLETION LAW:** master mp4 mtime (1788073670) newer than beat_sheet.json mtime
  (1788073596); beat_sheet.json was never touched after the compile that produced the
  final master.

## Output

`claude-for-legal--claude-liam-expansion-update.mp4` — 70.4s, 8/8 beats real (no
slate), native 3840×2160 (Remotion beats render at 4K already), audible narration
throughout (mean_volume -23.9 dB, ffmpeg-verified). This is the review cut (COMPLETION
LAW satisfied).

**Playlist:** Claude Basics. `SUBJECT.json`'s `family: "claude-for-legal"` matches no
prefix in `playlists.json`'s map; falls to the `hai-simple` skill-key fallback →
"Claude Basics" — same resolution every other delivered `claude-for-legal--*` redo in
this family has used (`clearance`, `entity-compliance`, `exam-forecast`,
`expansion-kickoff`).

Metadata file written: `claude-for-legal--claude-liam-expansion-update.md` (channel
@HumanitariansAI, Playlist: **Claude Basics**, plus the direct code link per the
DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to Phase 4 (4K
render + deliver.py) in this same invocation.

## 2026-08-30 — Phase 4 delivery

- **4K master:** `compile.py` (no `--review`) already enforced its 4K LAW during the
  Phase-3 compile — the master was born natively at 3840×2160 (Remotion beats render
  at native 4K), 70.4s, 8/8 beats real, mean_volume -23.9 dB. Verified via `ffprobe`
  and copied to `-4k.mp4` so `deliver.py`'s `newest_master()` picks it as the explicit
  4K variant (no Topaz upscale needed on flat-vector native-4K content).
- **Delivered:** `deliver.py --push` — outbox
  `DELIVERY/claude-for-legal--claude-liam-expansion-update/` (4K master + description,
  syncs to Drive `Claude_Bear/` on this machine's Drive-for-desktop mount); repo
  `humanitarians-youtube/claude-bear/claude-for-legal--claude-liam-expansion-update/`
  (README.md + beat_sheet.json + SCRIPT.md + SUBJECT.json + BUILD-LOG.md +
  CARRY-OUT.md + QUESTION.md — no media). Commit `cec65f16`, pushed clean (verified
  `git log` + `git status` against `origin/main`).

**Status: DELIVERED.**
