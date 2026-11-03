# BUILD-LOG — claude-plugins-official--claude-liam-skill-development

## 2026-08-31 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-plugins-official/youtube/claude-liam-skill-development/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `skill-development`
Claude Code plugin-dev Skill — the meta-skill for building Skills — already
fully built; no SCRIPT.md existed on the source, so source
`beats[*].narration_text` served as the locked script). Built entirely
fresh this invocation — only SUBJECT.json existed on pickup.

Question, facts, and full body argument carried over unchanged: a skill is
a folder Claude reads before it works (this one, skill-development,
contains a SKILL.md file — about 22 KB — plus a references folder);
SKILL.md is a plain-language instruction set with no hidden logic
underneath it, and Claude reads the file then acts on what it says; the
description field states when the skill applies (quoted verbatim from the
source's own trigger clause: wanting to "create a skill," "add a skill to
plugin," "write a new skill," "improve skill description," "organize skill
content," or needing guidance on skill structure); once a request matches,
Claude executes the Steps section in order, linear, no branching unless a
step says so; and the concrete limit that follows from being plain
instructions rather than code — same input, same output, every run, but
nothing hidden fills in for a request the file doesn't cover. B00 replaced
the source's `ClaudeComposerAsk` typed-ask cold open with
`BrutalistHesitantWriter` (WRITER LAW: "code" → "write" — the newcomer's
wrong guess that building a Skill means writing code Claude executes,
corrected toward the actual mechanism: SKILL.md is instructions Claude
reads and follows itself). Register re-registered Teardown→Plain: the
source's B03 "here is the Teardown moment... what it gets right / what it
bites" framing and BVDT's four-line verdict artifact were merged into a
single NB03 beat and stripped of judgment language, kept as the one fact a
general audience needs and can act on (repeatable results / only what's
written), per the NO JUDGMENT register check. BVDT's separate bulleted
artifact card was not kept as its own beat, per CARRY-OUT LAW — its facts
live in the single BCRY sentence instead. Close re-skinned to
@HumanitariansAI (`OutroSeries`).

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01/B02
anatomy/pipeline + B03 design tell + BVDT verdict + BHTF your-turn + BOUT
outro). This redo kept the same 7-beat shape: B00 carries the wrong-guess
pedagogy per WRITER LAW instead of a dedicated beat; B01→NB01, B02→NB02
kept as one beat each; B03+BVDT compressed into the single NB03; BHTF kept,
with the source's garbled inline clause ("I want to this skill should be
used when the user wants to...") rewritten to the actual trigger phrase the
skill's own description uses ("I want to create a skill"), since the
source text was a template-substitution artifact, not a deliberately
authored prompt; BOUT kept. Full audit in SCRIPT.md's "Beat-count note
(redo)" section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01–NB03) built on the shared generic "chip row"
Manim template (`scenes.py`/`render_scenes.py`) copied verbatim from the
`claude-plugins-official--claude-liam-agent-development` sibling, adapted
with skill-development-specific labels.

**B00 TIMING LAW.** Text: "How do I code / a new Skill / for Claude?" (39
chars, 3 lines) — shorter than the family's established-safe
agent-development config (60 chars) — rendered at the same known-good
parameters (charMs=42, mistakeRate=4%, hesitateWithin=2%, hesitateBetween=8%,
jitter=26, lead_silence_s=1.0). Narration 9.15s + 1.0s lead = 10.15s window
(≥9s floor). Verified by frame pull: "co" sits doomed in terracotta at
t≈2.5s, the corrected question "How do I write a new Skill for Claude?" is
settled and legible by t≈5s, and stays on screen through the clip's last
frame (t≈9.17s). No timing defect this time — the shorter text cleared the
established margin comfortably.

**One real GRAPHIC-beat defect caught and fixed, not a QC-sampling trap.**
First `type_check.py` pass was **FAIL, 1 defect**: NB01's accented chip
label "no hidden logic" measured 18px, under the 20px floor, after the
width-based scale-down (three words at font-size 22 exceeded the chip's
0.82×width budget, forcing an extra shrink past the min-size floor).
Shortened to "nothing hidden" (14 chars, moves into the ≤14 font-size-26
bucket) — `type_check.py` re-run went to PASS. But a **frame-pull read of
the recompiled beats (Gate V) caught a second, more serious defect that
GATE T's automated min-size check does not test: the BOLD-weight EB
Garamond accent chips were rendering with their inter-word spaces
collapsed** — "nothing hidden" displayed as "nothinghidden", NB02's
"trigger match" as "triggermatch", and NB03's "nothing outside it" as
"nothing outsideit" — all genuinely illegible as intended two/three-word
phrases, confirmed by cropped zoom frames. Non-bold captions and
non-accented chips at the same font sizes rendered spacing correctly, so
the defect is specific to this Manim/font combination at BOLD weight, not
a general chip-rendering problem. Root-caused and fixed by making all
three accented labels single hyphenated tokens instead of space-separated
phrases — "plain-text" (NB01), "trigger-match" (NB02), "no-fallback"
(NB03) — which carries the same teaching point without depending on a
space glyph inside a bold run. Re-rendered NB01–NB03, re-ran
`type_check.py` (PASS, 0 FAILs), and re-verified all three chips read
cleanly via fresh frame pulls before recompiling.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`, one pass, no re-generation needed); NB01–NB03 rendered via
`render_scenes.py` (foreground, re-rendered twice total as the two fixes
above landed); B00/BCRY/BHTF/BOUT rendered via `remotion_scenes.py` — the
first invocation exceeded the tool's 120s timeout and was moved to the
background by the harness automatically, blocked on via `TaskOutput`
before proceeding, per the COMPLETION LAW's foreground-render rule, never
treating a backgrounded render as "handled" without waiting on it.
`type_check.py` went FAIL→PASS (0 FAILs, 0 warnings). Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Result: `claude-plugins-official--claude-liam-skill-development.mp4`, 7/7
beats filled real (no slate), 101.1s, 3840×2160 (native 4K — `compile.py`'s
4K LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (see 2 defects + fixes above — one automated
  min-size catch, one Gate V frame-read catch that automated GATE T does
  not test)
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (ffmpeg volumedetect), max -2.9 dB
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 101.1s; mp4
  mtime (1788176752) newer than beat_sheet.json mtime (1788176574)
- Gate V (visual): pulled frames every 8s across the full runtime plus
  targeted checks of B00 (t≈2.5s "co" doomed in terracotta, t≈5s settled
  and correct, held to the clip's last frame), NB01–NB03 (all chips
  legible and correctly spaced post-fix), BCRY (carry-out sentence +
  sparkline read clean), BHTF (correct topic/title/@HumanitariansAI
  handle, full paste-ready prompt legible across the two-line wrap), and
  BOUT (OutroSeries: correct eyebrow "SKILL DEVELOPMENT ·
  @HumanitariansAI", correct title restate, crimson underline, no
  truncation). No blockers remaining.
- B00 TIMING LAW: `actual_duration_s` 9.2s (≥8s requirement met); the
  "code" → "write" correction lands on screen by t≈5s and the full
  corrected question stays legible for the remainder of the clip.

Metadata file written: `claude-plugins-official--claude-liam-skill-development.md`
(channel @HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors**). Per `playlists.json`, SUBJECT.json's family
(`claude-plugins-official`) matches the map's `"claude-plugins"` prefix (a
`str.startswith` match), which resolves to "Extending Claude — Skills,
Plugins & Connectors" — a more specific match than falling through to the
`hai-simple` skill-key default ("Claude Basics"), consistent with the
`claude-plugins-official--claude-liam-agent-development` sibling built in
this same family. Direct code link per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.
