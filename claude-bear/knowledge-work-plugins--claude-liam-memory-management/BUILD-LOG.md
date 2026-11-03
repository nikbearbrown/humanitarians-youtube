# BUILD-LOG — knowledge-work-plugins--claude-liam-memory-management

## 2026-09-04 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-memory-management/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `memory-management`
productivity Skill, already fully built — no SCRIPT.md; source
`beats[*].narration_text` served as the locked script). Built entirely
fresh this invocation — only SUBJECT.json existed on pickup.

Question, facts, and full body argument carried over unchanged: a skill is
a folder Claude reads before it works; memory-management runs on two
files — CLAUDE.md for working memory (the handful of facts kept in view on
every request) and a memory/ directory for the fuller knowledge base;
Claude reads CLAUDE.md then checks memory/ in order, which is what lets it
decode a team's shorthand, acronyms, and nicknames the way an established
colleague would; and a memory entry itself can be as informal as "Cubs fan,
likes talking baseball" alongside a job title or ticket history. B00
replaced the source's `ClaudeComposerAsk` typed-ask cold open with
`BrutalistHesitantWriter` (WRITER LAW: "remember" -> "read notes about" —
the newcomer's wrong guess that Claude automatically remembers a team the
way a person would, corrected toward the actual mechanism: it reads notes
that were written down for it). Register re-registered Teardown->Plain: the
source's B03 "the interesting constraint... a deliberate trade-off" framing
around the "Cubs fan" example was cut as a design verdict; the example
itself is kept unchanged, restated as a plain description of what a memory
entry looks like. Source BVDT's verdict ("same input, same output, every
run... know the limit") was merged into the single BCRY carry-out sentence
rather than kept as a separate bulleted artifact card, per CARRY-OUT LAW.
Close re-skinned to @HumanitariansAI (`OutroSeries`).

**Source data-quality note:** the source's B00 and BHTF narration contained
garbled, apparently mis-substituted template text (a stray double period in
B00; BHTF's prompt trailing off mid-sentence: "I want to two-tier memory
system that makes claude a true workplace collaborator. decodes ."). The
underlying facts (two-tier file split; decodes shorthand/acronyms/
nicknames) were kept unchanged but restated as grammatical sentences, and
BHTF's your-turn prompt was written fresh as a genuinely paste-ready
exercise carrying the same teaching point, since the source's version was
not runnable as written. Logged in SCRIPT.md's "Source data-quality note."

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01/B02
anatomy/pipeline + B03 design tell + BVDT verdict + BHTF your-turn + BOUT
outro). This redo kept the same 7-beat shape: B00 carries the wrong-guess
pedagogy per WRITER LAW instead of a dedicated beat, and absorbs the source
B00 cold open's two facts (the two-tier system; the shorthand-decoding
purpose) into NB01/NB02 since that beat no longer exists; B01->NB01,
B02->NB02 kept as one beat each; B03's example kept unchanged in NB03;
BVDT folded into BCRY; BHTF kept, rewritten to be genuinely runnable; BOUT
kept. Full audit in SCRIPT.md's "Beat-count note (redo)" section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00's mandated cold-open swap. NB01-NB03 were built as
a generic Manim "chip row" template (copied verbatim, mechanism/colors/
GATE-T notes, from the `claude-plugins-official--claude-liam-agent-
development` sibling) rather than reusing `SkillTeardownAnatomy`/
`Pipeline`/`Mechanism` verbatim, because `ClaudeVerdictArtifact`'s verdict
framing and that template family's Teardown-genre visual language carry
design-judgment connotations this Plain-register redo needs to avoid; the
chip row is a neutral structural diagram with no built-in verdict
semantics.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`; B00 measured 9.09s, meeting the >=9s TIMING LAW window on the
first attempt); NB01-NB03 rendered via `render_scenes.py`; B00/BCRY/BHTF/
BOUT rendered via `remotion_scenes.py` (the full-sheet run exceeded the
tool's 120s foreground timeout and was moved to background by the harness
automatically — blocked on it via `TaskOutput` before proceeding, per the
COMPLETION LAW's foreground-render rule, never treating a backgrounded
render as "handled" without waiting on it; exit code 0, all 4 beats
confirmed rendered in the output). Frame pull at t=2s and t=8.5s of
media/B00.mp4 confirmed "remember" sits doomed in terracotta early and the
full corrected question "Does Claude actually read notes about our team?"
is settled and legible well before the clip ends.

First `type_check.py` pass was **FAIL, 1 defect**, fixed at the root:

- **min-size §8.1, NB02** — smallest text run 18px, under the 20px floor.
  The accented (bold) chip label "decode shorthand" (16 chars) scaled down
  further than its NB01/NB03 siblings' accented labels to fit the chip
  box, the same accent/weight interaction class documented in the
  `claude-plugins-official` sibling reels' own fixes. Fixed by shortening
  the label to "decode terms" (12 chars) — re-rendered NB02 only (NB01/NB03
  untouched), and `beat_sheet.json`'s `graphic.production_viz.chips` for
  NB02 was synced to the fixed wording directly before the recompile, per
  COMPLETION LAW (never editing beat_sheet.json after a compile without
  recompiling).

`type_check.py` went 1->**PASS, 0 FAILs**. Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Result: `knowledge-work-plugins--claude-liam-memory-management.mp4`, 7/7
beats filled real (no slate), 96.3s, 3840x2160 (native 4K — `compile.py`'s
4K LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840x2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (see 1 defect + fix above)
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (ffmpeg volumedetect), max -3.0 dB
- ffprobe: video 3840x2160, audio present, duration 96.33s; mp4 mtime
  (1788515769) newer than beat_sheet.json mtime (1788515635)
- Gate V (visual): pulled frames every ~8s across the full runtime plus
  targeted checks of B00 (t~2s "remember" doomed in terracotta, t~8.5s
  settled+correct), NB01-NB03 (all chips legible post-fix, arrows and
  captions clean), BCRY (carry-out quote + sparkline "Notes, not recall."
  read clean), BHTF (correct topic/title/@HumanitariansAI handle,
  paste-ready prompt legible), and BOUT (OutroSeries: correct eyebrow
  "MEMORY MANAGEMENT · @HumanitariansAI", correct title restate, crimson
  underline, no truncation). No blockers.
- B00 TIMING LAW: `actual_duration_s` 9.09s (>=8s requirement met); the
  "remember" -> "read notes about" correction lands on screen by t~2s and
  the full corrected question stays legible for the remainder of the clip.

Metadata file written: `knowledge-work-plugins--claude-liam-memory-management.md`
(channel @HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors**). Per `playlists.json`, SUBJECT.json's family
(`knowledge-work-plugins`) is an exact key match in the map, resolving
directly to "Extending Claude — Skills, Plugins & Connectors" (no prefix
fallback needed). Direct code link per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.
