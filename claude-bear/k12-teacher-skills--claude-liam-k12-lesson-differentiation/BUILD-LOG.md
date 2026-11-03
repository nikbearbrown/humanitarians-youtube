# BUILD-LOG — k12-teacher-skills--claude-liam-k12-lesson-differentiation

## 2026-09-02 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/k12-teacher-skills/youtube/claude-liam-k12-lesson-differentiation/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `k12-lesson-differentiation`
skill: adapts an existing K-12 lesson for three proficiency tiers — below /
at / above grade level — producing 1 teacher-facing differentiation plan +
3 student-ready tier documents as editable Word documents in a single output
turn, rendered from one material-source JSON via bundled scripts so shared
content is written once and tiers cannot drift; uses the Learning Commons
Knowledge Graph when connected, works without it; not for creating a new
lesson from scratch, not for grading/rubrics/assessment). Source is a fully
built 7-beat Teardown reel (`build.filled: 7, of: 7`) with no SCRIPT.md —
source `beats[*].narration_text` served as the locked script. Built entirely
fresh this invocation — only SUBJECT.json existed on pickup.

**Beat-count discipline:** source is B00 (composer-ask cold open) +
B01/B02/B03 (anatomy / pipeline / design tell) + BVDT (verdict) + BHTF
(your turn) + BOUT (outro) — the exact same shape as the
`claude-for-legal--claude-liam-cease-desist` sibling, which served as the
direct structural and script template (same generic `SkillTeardownAnatomy`
/ `SkillTeardownPipeline` / `SkillTeardownMechanism` / `ClaudeVerdictArtifact`
/ `ClaudeComposerAsk` / `ClaudeTitleOutro` component family). This redo kept
the same 7-beat shape: B00 replaced 1:1 with BrutalistHesitantWriter;
B01→NB01, B02→NB02 kept as one beat each, Teardown framing stripped to
plain mechanism description. B03→NB03 required a content substitution
beyond re-registration: the source's B03 narration ("Here is the Teardown
moment... What it gets right: repeatable results. What it bites: anything
outside the spec.") is generic template filler shared across the whole
`claude-liam-<skill>` batch, not a skill-specific fact — NB03 instead uses
the one specific, checkable design fact from the skill's own purpose text
(quoted in source B00's narration): outputs "rendered from one
material-source JSON via bundled scripts (shared content is written once so
tiers cannot drift)". Same beat slot, same design-tell function in the
six-move audit, drawn from documented behavior rather than boilerplate.
BVDT's two verdict facts (reliable execution, and the single-source limit)
merged into the single BCRY carry-out sentence (CARRY-OUT LAW: Plain
carries one carry-out sentence, not a bulleted verdict). BHTF kept as the
your-turn handoff, source's broken bracket-fill placeholder ("I want to
adapts an existing k-12 lesson... for stude") replaced with a concrete,
grammatical, paste-ready scenario. BOUT kept, re-skinned to the
Humanitarians AI outro (`OutroSeries`, matching the cease-desist sibling's
fix for `OutroCTA`'s small-glyph min-size defect — used proactively here
rather than discovered fresh). Total: B00 + NB01–NB03 + BCRY + BHTF + BOUT =
7 beats, matching the source exactly. Full audit in SCRIPT.md's "Beat-count
note (redo)" section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — source
was already entirely REMOTION. The source's `SkillTeardownAnatomy` /
`SkillTeardownPipeline` / `SkillTeardownMechanism` components are not
registered in this toolkit's scene library, so NB01–NB03 were built fresh
as GRAPHIC (Manim) beats on the generic "chip row" template copied verbatim
(mechanism, colors, GATE T exemption notes) from the cease-desist sibling.

**B00 defect caught and fixed at Gate V, before compiling the full master:**
first attempt set `triggerWords: "three lessons"` (a two-word phrase) with
text ending "...so I write three lessons?". Frame-pulling B00 alone
(t=3–10.5s of an initial 10.8s render) showed the correction never fired —
"three lessons?" sat static with a blinking caret through the entire clip.
Root cause, found by reading `BrutalistHesitantWriter.tsx`: the component
splits `text` on whitespace into single tokens and matches `triggerWords`
against one token's punctuation-stripped core (`tokens = p.text.split(/(\s+)/)`,
`ti = triggers.indexOf(core.toLowerCase())`) — a multi-word trigger phrase
can never equal a single token, so the substitution branch is silently
never taken and typing just continues normally to the end of the literal
text. Neither sibling precedent read (`cease-desist`, `access-scaffolding`)
had used a multi-word trigger, so this failure mode was new to this reel,
not a repeat of a documented one. Fixed by redesigning B00's naive framing
so the wrong concept is expressed as a single, unique, last-content word
before the terminal "?": text changed to "When Claude tiers\na lesson for
three levels,\ndoes it write separate?", `triggerWords: "separate"`,
`replacementWords: "one shared version"` (multi-word replacement text is
fine — only the trigger match itself must be a single token). Regenerated
B00 audio only (`generate_audio_kokoro.py --only B00`, 11.11s, clearing the
>=8s TIMING LAW floor) and re-rendered B00 only (`remotion_scenes.py --only
B00 --force`) rather than rebuilding the whole sheet. Second render
frame-verified clean: "separate" doomed in terracotta by t≈6.5s, corrected
question ("...does it write one shared version?") settled and legible by
t≈9.5s, held through the 11.1s clip. SCRIPT.md, CARRY-OUT.md, and
QUESTION.md updated to match the corrected wording; `build_beat_sheet.py`'s
B00 block and its inline `note` field updated in place so a future rebuild
from that script reproduces the fix, not the defect, and document the
single-token trigger constraint for the next redo in this batch.

Audio generated fresh for the other 6 beats (`generate_audio_kokoro.py`, no
`--only` flag, free/local, `am_onyx`, single pass, no re-gen needed) before
the B00 defect was found; NB01–NB03 rendered via `render_scenes.py` (Manim,
foreground, single pass, no errors); B00/BCRY/BHTF/BOUT rendered via
`remotion_scenes.py` (foreground, single pass on first attempt, one
targeted `--only B00 --force` re-render after the fix). `type_check.py`
(GATE T) ran clean: **PASS, 0 FAILs** (all `§8.10` redundancy checks SKIP,
no findings requiring action).

Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Result: `k12-teacher-skills--claude-liam-k12-lesson-differentiation.mp4`,
7/7 beats filled real (no slate), 81.5s, 3840×2160 (native 4K — compile.py's
4K LAW). Motion histogram: remotion 4/7, graphic 3/7 (fixed spine cost of
this skill: cold open + carry-out + your-turn + outro are always REMOTION).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (compile.py's own ffmpeg
  volumedetect pass)
- ffprobe (independently re-verified): video 3840×2160 h264, audio aac
  present, duration 81.48s; mp4 mtime (1788350589) newer than beat_sheet.json
  mtime (1788350391)
- Gate V (visual): pulled frames across the full runtime (B00 dedicated
  correction-timing sweep at t=3/5/6.5/7.5/8.5/9.5/10.5/11.0s post-fix, plus
  NB01 at t≈16s, NB02 at t≈33s, NB03 at t≈42s, BCRY at t≈58s, BHTF at
  t≈66-72s, BOUT at t≈76-79s) — all chips legible and parallel-sized,
  carry-out sentence + sparkline read clean, BHTF shows correct
  topic/title/@HumanitariansAI handle and the paste-ready prompt legible,
  BOUT shows correct eyebrow "K12-LESSON-DIFFERENTIATION · @HumanitariansAI"
  and title restate with crimson underline, no truncation. No blockers.
- B00 TIMING LAW: `actual_duration_s` 11.13s (>=8s requirement met);
  "separate" doomed in terracotta by t≈6.5s, corrected question settled and
  legible by t≈9.5s, held through the remainder of the clip.

Metadata file written:
`k12-teacher-skills--claude-liam-k12-lesson-differentiation.md` (channel
@HumanitariansAI, **Playlist: Claude Basics**). Per `playlists.json`,
SUBJECT.json's family (`k12-teacher-skills`) matches no map prefix; falls
through to the `hai-simple` skill-key match (→ "Claude Basics"), consistent
with every other `k12-teacher-skills--*` sibling in this batch. Direct code
link per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.

## 2026-09-02 — Phase 4, DELIVERED

Master was already born native 3840×2160 (compile.py's 4K LAW), so copied
directly to
`k12-teacher-skills--claude-liam-k12-lesson-differentiation-4k.mp4` rather
than re-rendering at a higher resolution.

```
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Staged `DELIVERY/k12-teacher-skills--claude-liam-k12-lesson-differentiation/`
(4K master + description) for the Drive sync. Committed to
`claude-bear/k12-teacher-skills--claude-liam-k12-lesson-differentiation/`
(README.md = description, beat_sheet.json, SCRIPT.md, SUBJECT.json,
CARRY-OUT.md, QUESTION.md, BUILD-LOG.md — no mp3/mp4).

**Status: DELIVERED.**
