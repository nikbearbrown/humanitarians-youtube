# BUILD-LOG — k12-teacher-skills--claude-liam-k12-lesson-planning

## 2026-09-02 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/k12-teacher-skills/youtube/claude-liam-k12-lesson-planning/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `k12-lesson-planning`
skill). Source is a fully built 7-beat Teardown reel (`build.filled: 7, of:
7`) with no SCRIPT.md — source `beats[*].narration_text` served as the
locked script. Built entirely fresh this invocation — only SUBJECT.json
existed on pickup.

**Source defect found before scripting:** the source's B00, B03, and BVDT
narration carry literal, unfilled `>` placeholder tokens where a
per-skill fact should have been substituted by the original batch build —
e.g. B00 reads "The skill is k12-lesson-planning. >. A SKILL.md tells
Claude exactly how", B03 reads "Claude's job: >. What it gets right:
repeatable results. What it bites: anything outside the spec.", BVDT reads
"The SKILL.md is the spec — >." This is a broken batch-build artifact, not
a stylistic choice — confirmed by comparing against the
`k12-teacher-skills--claude-liam-k12-lesson-differentiation` sibling (built
earlier the same day), whose equivalent source beat had its `>` correctly
filled with the skill's real purpose text. This source's real
`k12-lesson-planning/SKILL.md`
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/k12-teacher-skills/plugin/skills/k12-lesson-planning/SKILL.md`)
does not exist on this machine (confirmed via `find`), and no other copy
of its content was found anywhere under `books/`. Its specific pedagogical
content cannot be read or verified from here — inventing lesson-planning
specifics to fill the placeholder gap would violate the no-fabrication
rule, so none were invented.

**Resolution:** kept every fact in the source that WAS real (not a
placeholder) — B01's file listing (LICENSE, SKILL.md 29k, `references/`,
`scripts/`, 4 files total), B02's linear read/execute/return pipeline, and
BVDT's two non-broken claims (repeatable execution: "same input, same
output, every run"; spec limit: "only what the file says"). For the
broken B03/BVDT "design tell" slot, built NB03 around the one specific,
checkable fact available: the folder ships not just prose (SKILL.md) but
a `references/` folder and a `scripts/` folder — a generically-true
mechanism claim about Claude Skills (instructions plus runnable code, not
prose alone), not an invented specific about lesson-planning pedagogy.
Full reasoning in SCRIPT.md's "Beat-count note (redo)".

**Beat-count discipline:** source is B00 (composer-ask cold open) +
B01/B02/B03 (anatomy / pipeline / design tell) + BVDT (verdict) + BHTF
(your turn) + BOUT (outro) — the same generic `SkillTeardownAnatomy` /
`SkillTeardownPipeline` / `SkillTeardownMechanism` / `ClaudeVerdictArtifact`
/ `ClaudeComposerAsk` / `ClaudeTitleOutro` component family used across the
whole `claude-liam-<skill>` batch, confirmed identical in shape to the
`k12-lesson-differentiation` sibling. This redo kept the same 7-beat shape:
B00 replaced 1:1 with BrutalistHesitantWriter; B01→NB01, B02→NB02 kept as
one beat each, Teardown framing stripped to plain mechanism description;
B03→NB03 content-substituted per above; BVDT's two real facts merged into
the single BCRY carry-out sentence (CARRY-OUT LAW: Plain carries one
carry-out sentence, not a bulleted verdict); BHTF kept as the your-turn
handoff, source's broken bracket-fill placeholder ("I want to >. Read the
k12-lesson-planning skill...") replaced with a concrete, grammatical,
paste-ready scenario (seventh-grade water-cycle lesson); BOUT kept,
re-skinned to the Humanitarians AI outro (`OutroSeries`). Total: B00 +
NB01–NB03 + BCRY + BHTF + BOUT = 7 beats, matching the source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — source
was already entirely REMOTION. The source's `SkillTeardownAnatomy` /
`SkillTeardownPipeline` / `SkillTeardownMechanism` components are not
registered in this toolkit's scene library, so NB01–NB03 were built fresh
as GRAPHIC (Manim) beats on the generic "chip row" template copied
verbatim (mechanism, colors, GATE T exemption notes) from the
`k12-lesson-differentiation` sibling.

**B00 — no defect this time:** the differentiation sibling caught and fixed
a bug where a multi-word `triggerWords` (e.g. "three lessons") never
matches `BrutalistHesitantWriter.tsx`'s single-token match logic, so the
correction silently never fires. Applying that lesson directly here:
`triggerWords: "improvise"` was chosen as a single whitespace token,
positioned as the last content word immediately before the terminal "?" in
"When Claude plans a lesson for my class, does it improvise?", correcting
to "follow written steps". First-attempt render was clean — no rework
needed. `actual_duration_s` 10.52s (clears the ≥8s TIMING LAW floor).
Frame-pull sweep (t=1/3/5/6.5/7.5/8.5/9.5/10.3s) confirmed: "im" doomed in
terracotta mid-typing at t≈6.5s, corrected question "...does it follow
written steps?" fully settled and legible by t≈9.5s, held through the
remainder of the clip.

Audio generated fresh for all 7 beats in one pass
(`generate_audio_kokoro.py`, free/local, `am_onyx`, $0.00, no `--only`
needed — no B00 rework this time). NB01–NB03 rendered via
`render_scenes.py` (Manim, foreground, single pass, all 3 ok, no errors).
B00/BCRY/BHTF/BOUT rendered via `remotion_scenes.py` (foreground, single
pass, no errors — 3 of 4 beats landed before the render tool's 120s
per-call cap moved the shell invocation to background; the render process
itself ran to completion in the foreground the whole time, confirmed by
`pgrep` still showing the Chrome headless render process alive, then a
second `remotion_scenes.py` invocation picked up the lock and rendered the
one remaining beat, BOUT, skipping the 3 already filled). `type_check.py`
(GATE T) ran clean: **PASS, 0 FAILs** (all `§8.10` redundancy checks SKIP,
no findings requiring action).

Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Result: `k12-teacher-skills--claude-liam-k12-lesson-planning.mp4`, 7/7
beats filled real (no slate), 85.3s, 3840×2160 (native 4K — compile.py's 4K
LAW). Motion histogram: remotion 4/7, graphic 3/7 (fixed spine cost of this
skill: cold open + carry-out + your-turn + outro are always REMOTION).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (compile.py's own ffmpeg
  volumedetect pass)
- ffprobe (independently re-verified): video 3840×2160 h264, audio aac
  present, duration 85.281s, mean_volume -23.9 dB / max -2.9 dB; mp4 mtime
  (1788351927) newer than beat_sheet.json mtime (1788351786)
- Gate V (visual): pulled frames across the full runtime (B00 dedicated
  correction-timing sweep at t=1/3/5/6.5/7.5/8.5/9.5/10.3s, plus NB01 at
  t≈16s, NB02 at t≈30s, NB03 at t≈45s, BCRY at t≈60s, BHTF at t≈73s, BOUT
  at t≈82s) — all chips legible and parallel-sized, single terracotta
  accent per beat, carry-out sentence + sparkline read clean, BHTF shows
  correct topic/title/@HumanitariansAI handle and the paste-ready prompt
  legible in the composer, BOUT shows correct eyebrow
  "K12-LESSON-PLANNING · @HUMANITARIANSAI" and title restate with crimson
  underline, no truncation, no overlap. No blockers.
- B00 TIMING LAW: `actual_duration_s` 10.52s (>=8s requirement met);
  "improvise" doomed in terracotta by t≈6.5s, corrected question settled
  and legible by t≈9.5s, held through the remainder of the clip.

Metadata file written:
`k12-teacher-skills--claude-liam-k12-lesson-planning.md` (channel
@HumanitariansAI, **Playlist: Claude Basics**). Per `playlists.json`,
SUBJECT.json's family (`k12-teacher-skills`) matches no map prefix; falls
through to the `hai-simple` skill-key match (→ "Claude Basics"), consistent
with every other `k12-teacher-skills--*` sibling in this batch. Direct code
link per DELIVERY CONTRACT format included. Description's "Deliberately not
claimed" section discloses the source-SKILL.md-unavailable limitation
explicitly.

**Status: review cut DONE.** Passed every Phase-3 gate.
