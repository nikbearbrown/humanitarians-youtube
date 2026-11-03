# BUILD-LOG — financial-services--claude-liam-competitive-analysis

## 2026-09-01 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/financial-services/youtube/claude-liam-competitive-analysis/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `competitive-analysis`
market-researcher plugin Skill, already fully built — no SCRIPT.md; source
`beats[*].narration_text` served as the locked script; the source's own
`source_skill` path pointed at a machine this session has no access to, so
facts were taken from the source beat sheet's own narration, which already
paraphrases the SKILL.md completely). Built entirely fresh this invocation —
only SUBJECT.json existed on pickup.

Question, facts, and full body argument carried over unchanged: the
competitive-analysis skill is a folder — SKILL.md plus a references folder,
two files total; Claude reads the file, then acts; the pipeline is in a
Steps section, executed linearly with no branching unless a step says so;
the skill is a specification written as an instruction set, and its answer
holds only within what that file specifies; same input produces the same
output every run. B00 replaced the source's `ClaudeComposerAsk` typed-ask
cold open with `BrutalistHesitantWriter` (WRITER LAW: "judged" → "processed"
— the newcomer's wrong guess that a finished competitive-analysis deck means
Claude judged the market itself, corrected toward the actual mechanism: the
skill just processes a fixed set of written steps). Register re-registered
Teardown→Plain: the source's B03 "what it gets right: repeatable results /
what it bites: anything outside the spec" framing was stripped of its
gets-right/bites verdict language and compressed into a plain scope
description (inside the written scope vs. outside it) — no ruling on
whether the design is good or bad, per the NO JUDGMENT register check.
BVDT's verdict facts (same input → same output every run; the limit is only
what the file says) were merged into the single BCRY carry-out sentence
rather than kept as a separate bulleted artifact card, per CARRY-OUT LAW.
Close re-skinned to @HumanitariansAI (`OutroSeries`).

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01/B02
anatomy/pipeline + B03 design tell + BVDT verdict + BHTF your-turn + BOUT
outro). This redo kept the same 7-beat shape: B00 carries the wrong-guess
pedagogy per WRITER LAW instead of a dedicated beat; B01→NB01, B02→NB02 kept
as one beat each; B03 compressed into NB03 (dropping the Teardown
gets-right/bites framing, keeping the plain scope fact); BVDT folded into
BCRY; BHTF kept, but its prompt was rewritten — the source's version was a
garbled, mid-template sentence ("I want to framework for building
competitive landscape decks — market positioning, competi. Read the
competitive-analysis skill...") that was not runnable as written, so it was
replaced with a concrete, grammatical, paste-ready prompt (a
regional-business-banking competitive deck) that keeps the source's own
"walk me through what you will do before you do it" clause (the source
LENS-AUDIT.md's noted Plato move — artifact vs. world, forcing the plan
before the run); BOUT kept. Full audit in SCRIPT.md's "Beat-count note
(redo)" section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism` /
`ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no substitution
beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01–NB03) built on the shared generic "chip row" Manim
template (`scenes.py`/`render_scenes.py`), copied verbatim (mechanism,
colors, GATE T exemption notes) from the `claude-plugins-official--claude-
liam-agent-development` sibling, adapted with competitive-analysis-specific
labels.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`) — no manual timing fixes needed; B00's audio measured 11.29s
against a 20-35-word narration + 0.9s lead silence, giving the
BrutalistHesitantWriter typing performance (51 forward characters across 4
short lines) comfortable margin over the WRITER LAW's ≥9s floor. B00/BCRY/
BHTF/BOUT rendered via `remotion_scenes.py` (the full-sheet run exceeded the
tool's 120s timeout and was moved to background by the harness
automatically — blocked on it via `TaskOutput` before proceeding, per the
COMPLETION LAW's foreground-render rule, never treating a backgrounded
render as "handled" without waiting on it); NB01–NB03 rendered via
`render_scenes.py` in the foreground with no failures. `type_check.py`
(GATE T) passed clean on the first attempt, 0 FAILs.

Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR>
```

Result: `financial-services--claude-liam-competitive-analysis.mp4`, 7/7
beats filled real (no slate), 84.4s, 3840×2160 (native 4K — `compile.py`'s
4K LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max -3.0 dB
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 84.44s; mp4
  mtime (1788276309) newer than beat_sheet.json mtime (1788276202)
- Gate V (visual): pulled frames every ~8s across the full runtime plus
  targeted checks of B00 (t≈3.0s "judged" doomed in terracotta, t≈9.5s
  settled to "processed" and legible, held to the end of the 11.3s clip),
  NB01 (SKILL.md/references/2 files chips + "the file is the program"
  caption, all legible), NB02 (read/execute/return chips with arrows,
  accent underline on "execute steps"), NB03 (written scope/same steps/
  outside: nothing chips, accent on the last), BCRY (carry-out sentence +
  sparkline read clean), BHTF (correct topic/title/@HumanitariansAI handle,
  paste-ready prompt legible), and BOUT (OutroSeries: correct eyebrow
  "COMPETITIVE ANALYSIS · @HumanitariansAI", correct title restate, crimson
  underline, no truncation). No blockers. Noted, not a defect: `OutroSeries`
  renders on flat white rather than the humanitarians cream ground, same
  shared-component behavior already logged unremarked across every other
  `financial-services--*` sibling in this loop.
- B00 TIMING LAW: `actual_duration_s` 11.29s (≥8s requirement met); the
  "judged" → "processed" correction lands on screen well before the clip's
  midpoint and stays legible for the remainder.

Metadata file written: `financial-services--claude-liam-competitive-analysis.md`
(channel @HumanitariansAI, **Playlist: Claude Basics**). Per `playlists.json`,
SUBJECT.json's family (`financial-services`) matches no prefix in the map's
family table (no `financial-`/`finance-` entry exists); falling through to
the `hai-simple` skill-key entry, which resolves directly to "Claude Basics"
— the correct default per the algorithm (family checked first, then the
`hai-simple` skill key, then `_default`), not the bare "Claude". Direct code
link per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.

## 2026-09-01 — Phase 4, DELIVERED

Master was already born native 3840×2160 (compile.py's 4K LAW), so copied
directly to `financial-services--claude-liam-competitive-analysis-4k.mp4`
rather than re-rendering at a higher resolution.

```
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Staged `DELIVERY/financial-services--claude-liam-competitive-analysis/`
(4K master + description) for the Drive sync. Committed to
`claude-bear/financial-services--claude-liam-competitive-analysis/`
(README.md = description, beat_sheet.json, SCRIPT.md, SUBJECT.json,
CARRY-OUT.md, QUESTION.md, BUILD-LOG.md — no mp3/mp4) as commit `75f45c8e`,
pushed clean (no rebase conflicts).

**Status: DELIVERED.**
