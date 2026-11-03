# BUILD-LOG — claude-plugins-official--claude-liam-agent-development

## 2026-08-30 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-plugins-official/youtube/claude-liam-agent-development/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `agent-development`
Claude Code plugin-dev Skill, prose-trigger version, already fully built —
no SCRIPT.md; source `beats[*].narration_text` served as the locked script).
Built entirely fresh this invocation — only SUBJECT.json existed on pickup.

Question, facts, and full body argument carried over unchanged: an agent
file is YAML frontmatter (name, description, model, color, tools) + a
markdown system-prompt body; name is lowercase-hyphenated, 3-50 chars,
alphanumeric start/end; description is the field that decides dispatch,
loaded into context whenever the agent is registered; model `inherit` is
the recommended default; color is cosmetic; tools should be the minimum
the task needs; the body carries role/responsibilities/output format plus
a "When to invoke" section (2-4 prose-bullet worked scenarios); the
description's own format in this Skill version is "Use this agent
when...", "Typical triggers include [scenarios]", then a pointer to the
body's When to invoke section — two locations serving two audiences
(Claude's dispatch decision vs. the agent's own worked scenarios once
invoked); and the concrete cost of that two-location design — nothing
keeps the two in sync, so a scenario that only lives in a stale location
never gets checked at the moment that matters (dispatch, which reads the
description alone). B00 replaced the source's `ClaudeComposerAsk` typed-ask
cold open with `BrutalistHesitantWriter` (WRITER LAW: "skills" → "triggers"
— the newcomer's wrong guess that listing an agent's skills/capabilities in
the description is enough for Claude to know when to use it, corrected
toward the actual mechanism: only stated trigger conditions get read at
dispatch). Register re-registered Teardown→Plain: the source's B05 "gets it
right / where it bites" list was compressed to the single most teachable,
general-audience fact (the sync problem) rather than kept as a full
strengths/gaps inventory — the Claude-harness-internals gaps in the source
(pattern-match vs. LLM-judgment dispatch, no model-override guidance, no
system-prompt length guidance) were dropped as assuming a technical
audience simple/hai-simple doesn't target, not as a verdict on the skill's
quality. BVDT's verdict facts were merged into the single BCRY carry-out
sentence rather than kept as a separate bulleted artifact card, per
CARRY-OUT LAW. Close re-skinned to @HumanitariansAI (`OutroSeries`).

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01/B02
anatomy/design + B05 teardown analysis + BVDT verdict + BHTF your-turn +
BOUT outro). This redo kept the same 7-beat shape: B00 carries the
wrong-guess pedagogy per WRITER LAW instead of a dedicated beat; B01→NB01,
B02→NB02 kept as one beat each; B05's long strengths/gaps list compressed
into NB03 (the one fact a general viewer needs and can act on); BVDT folded
into BCRY; BHTF kept, with the source's already-generic, already-runnable
prompt ("Create an agent for my plugin that reviews pull request diffs for
security issues") carried over unchanged; BOUT kept. Full audit in
SCRIPT.md's "Beat-count note (redo)" section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`AgentDevAnatomy` / `AgentDevTriggerProse` / `AgentDevTell2` /
`ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01–NB03) built on the shared generic "chip row"
Manim template (`scenes.py`/`render_scenes.py`) copied verbatim from the
`claude-plugins-official--claude-liam-access` sibling, adapted with
agent-development-specific labels.

**B00 TIMING LAW — one real defect caught and fixed, not a QC-sampling
trap.** First render (text "If I describe / my agent's skills, / will
Claude know / when to use it?", 4 lines / 67 forward-typed characters,
charMs=48, mistakeRate=6%, hesitateWithin=2%, hesitateBetween=14%, audio
10.56s) ran out of its window: verified by a frame pull at the clip's exact
last frame — the writer had settled on "will Claude know" but the fourth
line, "when to use it?", never started typing. Root cause, confirmed by
hand-tracing `buildActs`/`buildTimeline`: 70 forward keystrokes at 48ms +
fixed pauses (3 newlines, the trigger-word backspace/retype cycle, an
apostrophe-punctuation pause, a terminal "?" pause) + the *expected* random
hesitation/typo time at those rates summed to ≈10.5s against a 10.56s
budget — effectively zero margin, so ordinary seeded variance pushed it
over. Fixed by shortening the text to "Does listing / my agent's skills /
tell Claude / when to use it?" (60 chars, one fewer punctuation pause, 10
words instead of 12), dropping mistakeRate to 4%, hesitateBetween to 8%,
and speeding charMs to 42 — re-generated B00's audio only (10.09s) and
re-rendered B00 only (media/B00.mp4 unaffected other beats' stamps).
Reverified by frame pull: "skills" sits doomed in terracotta at t≈2.2s,
the full corrected question "Does listing my agent's triggers tell Claude
when to use it?" is settled and legible by t≈4.0s, and stays on screen for
the remaining ~6s of the 10.1s clip (well past the ≥8s TIMING LAW floor).

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`; B00 regenerated once after the text fix via `--only B00`);
B00/BCRY/BHTF/BOUT rendered via `remotion_scenes.py` (foreground; both the
full-sheet run and the B00-only re-render exceeded the tool's 120s timeout
and were moved to background by the harness automatically — blocked on
each via `TaskOutput` before proceeding, per the COMPLETION LAW's
foreground-render rule, never treating a backgrounded render as "handled"
without waiting on it); NB01–NB03 rendered via `render_scenes.py`. First
`type_check.py` pass was **FAIL, 1 defect**, fixed at the root:

- **min-size §8.1, NB03** — smallest text run measured 19px, 1px under the
  20px floor. Diagnosed against the NB01/NB02 siblings (both PASS at
  identical chip-box dimensions and font-size tier): NB03's middle chip
  label, `"when to invoke"` (14 chars, same bucket as NB02's identical
  label), was rendered at NORMAL weight in NB03 (accent marks a different
  chip there) versus BOLD weight in NB02 (where that same label IS the
  accented chip) — the thinner, non-bold glyph strokes at that width
  measured under the floor after scale-to-fit, the same accent/weight
  interaction class documented in the `claude-plugins-official--claude-
  liam-access` sibling's own NB02 fix. Fixed by shortening the label to
  `"the body"` (8 chars) — re-rendered NB03 only (NB01/NB02 untouched), and
  `beat_sheet.json`'s `graphic.production_viz.chips`/`label` for NB03 was
  synced to the fixed wording directly (not via a full `build_beat_sheet.py`
  re-run, which would have discarded the already-measured audio durations
  and render stamps) before the recompile, per COMPLETION LAW.

`type_check.py` went 1→**PASS, 0 FAILs**. Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Result: `claude-plugins-official--claude-liam-agent-development.mp4`, 7/7
beats filled real (no slate), 146.2s, 3840×2160 (native 4K — `compile.py`'s
4K LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (see 1 defect + fix above)
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (ffmpeg volumedetect), max -2.8 dB
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 146.2s; mp4
  mtime (1788135188) newer than beat_sheet.json mtime (1788134960)
- Gate V (visual): pulled frames every ~10-20s across the full runtime plus
  targeted checks of B00 (t≈1.5-2.2s "skills" doomed in terracotta, t≈4.0s
  settled+correct, held to the end of the 10.1s clip), NB01-NB03 (all chips
  legible and parallel-sized post-fix, including the recompiled NB03),
  BCRY (carry-out sentence + sparkline read clean), BHTF (correct
  topic/title/@HumanitariansAI handle, paste-ready prompt text legible),
  and BOUT (OutroSeries: correct eyebrow "AGENT DEVELOPMENT ·
  @HumanitariansAI", correct title restate, crimson underline, no
  truncation). No blockers.
- B00 TIMING LAW: `actual_duration_s` 10.1s (≥8s requirement met); the
  "skills" → "triggers" correction lands on screen by t≈4.0s and the full
  corrected question stays legible for the remainder of the clip.

Metadata file written: `claude-plugins-official--claude-liam-agent-development.md`
(channel @HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors**). Per `playlists.json`, SUBJECT.json's family
(`claude-plugins-official`) matches the map's `"claude-plugins"` prefix (a
`str.startswith` match — `"claude-plugins-official".startswith("claude-
plugins")`), which resolves to "Extending Claude — Skills, Plugins &
Connectors"; this is a more specific match than falling through to the
`hai-simple` skill-key default ("Claude Basics"), consistent with the
`claude-plugins-official--claude-liam-access` sibling built in this same
family earlier today. Direct code link per DELIVERY CONTRACT format
included.

**Status: review cut DONE.** Passed every Phase-3 gate.
