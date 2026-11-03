# BUILD-LOG — knowledge-work-plugins--claude-liam-meeting-briefing

## 2026-09-04 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-meeting-briefing/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `meeting-briefing`
knowledge-work-plugins skill, already fully built — no SCRIPT.md, source
`beats[*].narration_text` served as the locked script). Built entirely
fresh this invocation — only SUBJECT.json existed on pickup. Source
SKILL.md itself is not reachable from this machine (source metadata records
its path on Bear's machine: `/Users/bear/Documents/CoWork/bear-textbooks/
books/anthropics/knowledge-work-plugins/legal/skills/meeting-briefing/
SKILL.md`), same defect class as several siblings in this family; nothing
here depended on reading it — every fact traces to the source beats'
`narration_text`, which already carried the skill's full description
("Prepare structured briefings for meetings with legal relevance and track
resulting action items...") and its generic anatomy/pipeline/consistency
argument.

Question, facts, and full body argument carried over unchanged: a Skill is
a folder Claude reads before it acts; the meeting-briefing skill prepares
structured briefings and tracks resulting action items; the instructions
live in one file, SKILL.md, plain language, no hidden logic; the plan
itself lives in a Steps section, executed linearly in order, no branching
unless a step says so; because the steps are fixed, the same request
produces the same kind of briefing every run; and the hard limit is the
file itself — anything the SKILL.md doesn't spell out isn't part of the
plan. B00 replaced the source's `ClaudeComposerAsk` typed-ask cold open
with `BrutalistHesitantWriter` (WRITER LAW: "improvise" → "follow" — the
newcomer's wrong guess that Claude improvises a plan for a meeting
briefing on the spot, corrected toward the actual mechanism: it follows an
already-written plan). Register re-registered Teardown→Plain: the source's
B03 "gets it right / where it bites" framing and BVDT's verdict recap were
compressed into the single most teachable, general-audience fact (the
consistency-and-limit pair) rather than kept as a full strengths/gaps
inventory, with Teardown's judgment language ("makes Claude execute...
reliably") dropped per the NO JUDGMENT register check. BVDT's facts were
then merged into the single BCRY carry-out sentence rather than kept as a
separate bulleted artifact card, per CARRY-OUT LAW. BHTF's source prompt
("Read the meeting-briefing skill and walk me through what you will do
before you do it") assumed the viewer already has that specific internal
Anthropic Skill installed, so it was replaced with a functionally
identical but genuinely runnable prompt — ask Claude to state its plan as
numbered steps before executing, on any meeting the viewer actually has —
teaching the same lesson without depending on a Skill most viewers don't
have. Close re-skinned to @HumanitariansAI (`OutroSeries`), with a new
title ("A Written Plan, Not a Guess.") restating the carry-out rather than
the source's literal "Claude, Meeting Briefing." title.

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01/B02
anatomy/pipeline + B03 teardown design-tell + BVDT verdict + BHTF your-turn
+ BOUT outro). This redo kept the same 7-beat shape: B00 carries the
wrong-guess pedagogy per WRITER LAW instead of a dedicated beat; B01→NB01,
B02→NB02 kept as one beat each; B03+BVDT compressed into NB03 (the one
fact a general viewer needs and can act on); NB03/BVDT's facts folded into
BCRY; BHTF kept, prompt rewritten to be actually runnable without an
installed Skill; BOUT kept. Full audit in SCRIPT.md's "Beat-count note
(redo)" section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01–NB03) built on the shared generic "chip row"
Manim template (`scenes.py`/`render_scenes.py`) copied verbatim from the
`claude-plugins-official--claude-liam-agent-development` sibling, adapted
with meeting-briefing-specific labels.

**B00 TIMING LAW** — used the already-calibrated rates from the
agent-development sibling's own fix (42ms/char, 4% mistakeRate, 2%
hesitateWithin, 8% hesitateBetween) from the start; audio 9.81s +
`lead_silence_s` 1.0 = 10.81s window, well past the ≥9s floor. Frame-
verified: "improvise" sits doomed in terracotta at t≈1.9–2.3s, corrects to
"follow" by t≈3.2s, and the full corrected question "Does Claude follow a
plan to brief me for a meeting?" is settled and legible by t≈8.5s, holding
to the clip's end.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`, cost $0.00), first pass, no re-run needed. `remotion_scenes.py`
(all 4 REMOTION beats) exceeded the tool's 120s foreground timeout and was
moved to background by the harness automatically — blocked on it via
`TaskOutput(block=true)` before proceeding, per the COMPLETION LAW's
foreground-render rule, confirmed exit 0, all 4 beats `ok`. `render_scenes.py`
(3 Manim GRAPHIC beats) ran and completed within the foreground window, no
backgrounding needed.

**Two GATE T / Gate V defects caught and fixed, both root-caused, neither a
checker artifact:**

1. **min-size §8.1, NB03** — the third chip's original label "only what's
   written" (19 chars) autoscaled to 18px, 1px under the 20px floor after
   fitting the 3.2-unit-wide card. Fixed by shortening to "the file" (8
   chars, same font-size bucket as the sibling's own similar fix) —
   re-rendered NB03 only, recompiled, GATE T PASS.
2. **Word-glue in NB02's bold accented chip, caught by Gate V frame
   inspection, not GATE T** — the label "Steps section" (two words, BOLD
   weight, EB Garamond) rendered with no visible inter-word gap, reading
   as the single garbled word "Stepssection" (confirmed by a cropped
   zoom-in frame pull at t=32s). This is a bold-weight + multi-word EB
   Garamond spacing defect in this Manim/font environment — the same class
   of defect several siblings in this log have hit on bold multi-word
   chips (e.g. the `contract-review` sibling's "LAWYER'S CALL"/"LAWYER
   DECIDES" overlap, fixed the same way). Fixed by shortening the label to
   the single word "Steps" (the beat's title, "THE PLAN IS THE STEPS
   SECTION," already carries the full phrase) — re-rendered NB02 only,
   recompiled, re-verified via a fresh frame pull: clean, legible, correct
   word spacing.

`type_check.py` went FAIL (1, the NB03 min-size)→PASS after the first fix;
the NB02 word-glue defect was never flagged by GATE T (no min-size,
overlap, or contrast rule catches two words rendering as one when neither
falls under any pixel-height or bbox threshold) — caught only by directly
reading the compiled frame, which is why Gate V's visual read is required
in addition to the automated checker. Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Result: `knowledge-work-plugins--claude-liam-meeting-briefing.mp4`, 7/7
beats filled real (no slate), 85.3s, 3840×2160 (native 4K — `compile.py`'s
4K LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (after the NB03 min-size fix above)
- GATE AUDIO: PASS — mean_volume **-24.1 dB** (ffmpeg volumedetect), max -3.1 dB
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 85.333s; mp4
  mtime (1788512398) newer than beat_sheet.json mtime (1788512316)
- Gate V (visual): pulled frames at 6s spacing across the full runtime plus
  targeted B00 correction-timing pulls (t=1.5/1.9/2.3/2.7/3.2/8.5s) and a
  zoomed crop on NB02's accented chip. B00: "improvise" doomed in
  terracotta t≈1.9–2.3s, corrected and settled by t≈3.2s, full question
  legible and held through clip-end (t=8.5s of the 9.8s clip). NB01: chips
  "meeting-briefing" → "SKILL.md" (accented) → "plain language", caption
  "the file is the program" — clean. NB02 (post-fix): chips "Steps"
  (accented) / "in order" / "executes", caption "linear, unless a step
  says otherwise" — clean, correct word spacing. NB03 (post-fix): chips
  "same steps" / "same result" / "the file" (accented), caption "the
  limit is the file, too" — clean. BCRY: carry-out quote + sparkline
  "A plan, not a guess." read clean. BHTF: correct topic/title/
  @HumanitariansAI folder label, paste-ready prompt text legible. BOUT
  (`OutroSeries`): correct eyebrow "MEETING BRIEFING · @HumanitariansAI",
  correct title restate "A Written Plan, Not a Guess.", crimson underline,
  no truncation. No blockers remaining after both fixes.
- B00 TIMING LAW: `actual_duration_s` 9.81s + `lead_silence_s` 1.0 = 10.81s
  window (≥9s requirement met); correction lands on screen by t≈3.2s and
  the full corrected question stays legible for the remainder of the clip.

Metadata file written: `knowledge-work-plugins--claude-liam-meeting-briefing.md`
(channel @HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors**). Per `playlists.json`, SUBJECT.json's family
(`knowledge-work-plugins`) is an exact key match in the map — no fallback
needed. Direct code link per DELIVERY CONTRACT format included. Description
carries a "Deliberately not claimed" section disclosing that the specific
internal Skill's exact Steps wording isn't reproduced verbatim, and that
the Your Turn prompt doesn't require the meeting-briefing Skill to be
installed.

**Status: review cut DONE.** Passed every Phase-3 gate.
