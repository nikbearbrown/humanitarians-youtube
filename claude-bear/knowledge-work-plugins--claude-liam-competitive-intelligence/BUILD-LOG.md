# BUILD-LOG — knowledge-work-plugins--claude-liam-competitive-intelligence

## 2026-09-03 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-competitive-intelligence/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `competitive-intelligence`
sales Skill, already fully built — no SCRIPT.md; source `beats[*].narration_text`
served as the locked script). Built entirely fresh this invocation — only
SUBJECT.json existed on pickup.

Question, facts, and full body argument carried over unchanged: the skill is
a folder Claude reads before acting (SKILL.md = "the file is the program");
its job is to research named competitors and build one interactive
battlecard (an HTML artifact — clickable competitor cards + a comparison
matrix); the pipeline is linear (read the trigger phrase, research, build,
in order, no branching unless a step says so); and the design's whole limit
is that it only ever produces what the SKILL.md specifies — same input,
same output, every run, nothing for a competitor or output shape the file
doesn't cover. B00 replaced the source's `ClaudeComposerAsk` typed-ask cold
open with `BrutalistHesitantWriter` (WRITER LAW: "watch" → "research" — the
newcomer's wrong guess that a "competitive intelligence" skill means Claude
continuously monitors competitors, corrected toward the actual mechanism:
Claude researches once, on request, following one fixed recipe). Register
re-registered Teardown → Plain: the source B03's "what it gets right / what
it bites" framing was flattened to a plain mechanism-and-consequence
description (NB03), and BVDT's verdict facts were merged into the single
BCRY carry-out sentence rather than kept as a separate bulleted artifact
card, per CARRY-OUT LAW. Close re-skinned to @HumanitariansAI (`OutroSeries`).

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01 anatomy
+ B02 pipeline + B03 design tell + BVDT verdict + BHTF your-turn + BOUT
outro). This redo kept the exact same 7-beat shape, 1:1, with no compression
needed: B00 replaced with BrutalistHesitantWriter (carrying the wrong-guess
pedagogy per WRITER LAW instead of a dedicated beat); B01→NB01, B02→NB02,
B03→NB03 kept as one beat each, facts unchanged; BVDT→BCRY (verdict merged
into the carry-out sentence); BHTF kept — but its source narration_text
carried a mid-word truncation bug from an automated shortening pass
("outputs an html a."), so it was rewritten as an actually paste-ready
prompt with the same ask (read the skill, walk through the plan, then run
it and check the two-part battlecard output); BOUT kept, re-skinned to the
Humanitarians AI outro. Full audit in SCRIPT.md's "Beat-count note (redo)"
section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism` /
`ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no substitution
beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01–NB03) built on the shared generic "chip row"
Manim template (`scenes.py`/`render_scenes.py`), copied verbatim from the
`claude-plugins-official--claude-liam-agent-development` sibling and adapted
with competitive-intelligence-specific labels (folder → SKILL.md → the
program; trigger phrase → research → battlecard; named competitors → the
battlecard → anything else).

B00 used the tuned typing rates already established by that sibling's own
first-attempt timing fix (42ms/char, 4% mistakeRate, 8% hesitateBetween,
1.0s lead_silence) rather than re-discovering the same defect — rendered
11.93s on the first attempt, comfortably past the ≥8s TIMING LAW floor.
Verified by frame pull: "watch" sits doomed in terracotta mid-typing, and
the full corrected question "Can Claude research my competitors for me?"
is settled and legible in the clip's last frame.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`); NB01–NB03 rendered via `render_scenes.py` (Manim, foreground);
B00/BCRY/BHTF/BOUT rendered via `remotion_scenes.py` (foreground — the
harness's 120s default Bash timeout auto-backgrounded both the full-sheet
run and the later BHTF-only re-render; both were blocked on via `TaskOutput`
before proceeding, per the COMPLETION LAW's foreground-render rule, never
treating a backgrounded render as "handled" without waiting on its exit
code). `type_check.py` (GATE T) passed clean on the first attempt, 0 FAILs.

**One real defect caught at Gate V, not a QC-sampling trap.** A frame pull
at BHTF's on-screen text (t≈70s) showed the two-line eyebrow
("COMPETITIVE INTELLIGENCE · ANTHROPIC SKILL" wrapped to a second line,
"SKILL") sitting with zero visible gap above the segment title ("Same
Battlecard, Every Time.") — GATE T's automated check didn't flag it (its
overlap detector targets the Manim beats' text masks per the scenes.py
exemption notes, not this Remotion component), but the crop showed the
"SKILL" glyphs' descenders directly adjacent to "Same"'s ascenders, a real
crowding defect under VISUAL QC LAW. Fixed by shortening the `ClaudeComposerAsk`
topic prop to "COMPETITIVE INTELLIGENCE · SKILL" (33 chars, fits one line) —
re-rendered BHTF only (other beats' stamps untouched) and recompiled.
Reverified by frame pull: the eyebrow now sits on one line with clean
spacing above the title.

Compiled: `python3 runtime/scripts/compile.py <REEL_DIR> --force`. Result:
`knowledge-work-plugins--claude-liam-competitive-intelligence.mp4`, 7/7
beats filled real (no slate), 89.6s, 3840×2160 (native 4K — compile.py's 4K
LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max -3.1 dB
- ffprobe: video 3840×2160 h264, audio (aac, 48kHz) present, duration 89.58s;
  mp4 mtime (1788413882) newer than beat_sheet.json mtime (1788413805)
- Gate V (visual): pulled frames every ~8s across the full runtime plus
  targeted checks of B00 (mid-typing "watch" doomed in terracotta,
  last-frame "Can Claude research my competitors for me?" settled and
  legible for the full 11.93s clip), NB01–NB03 (all chip rows legible,
  arrows/accent underlines correct, captions read clean — "the file is the
  program" / "clickable cards + comparison matrix" / "only what the file
  says"), BCRY (carry-out sentence + sparkline read clean), BHTF (fixed
  topic line, correct title, @HumanitariansAI handle, paste-ready prompt
  text legible), and BOUT (OutroSeries: correct eyebrow "COMPETITIVE
  INTELLIGENCE · @HumanitariansAI", correct title restate, crimson
  underline, no truncation — renders on a white ground rather than the
  humanitarians cream, matching the `claude-plugins-official--claude-liam-
  agent-development` sibling's identical OutroSeries behavior exactly;
  the component exposes only `eyebrow`/`line` props, no palette/ground prop,
  so this is the shared component's established behavior, not a defect
  introduced by this build). No blockers after the BHTF fix.
- B00 TIMING LAW: `actual_duration_s` 11.93s (≥8s requirement met, no
  re-render needed).

Metadata file written: `knowledge-work-plugins--claude-liam-competitive-intelligence.md`
(channel @HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors**). Per `playlists.json`, SUBJECT.json's family
(`knowledge-work-plugins`) matches the map's `"knowledge-work-plugins"` key
exactly — a direct match, not a prefix fallthrough. Direct code link per
DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.
