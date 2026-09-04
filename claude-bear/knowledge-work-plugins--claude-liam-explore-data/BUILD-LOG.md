# BUILD-LOG — knowledge-work-plugins--claude-liam-explore-data

## 2026-09-03 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-explore-data/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `explore-data`
Skill, already fully built — no SCRIPT.md; source `beats[*].narration_text`
served as the locked script, with B00's complete, untruncated skill
description used as the source of record over the truncated repeats in
B03/BVDT/BHTF — same defect class already logged on the
`knowledge-work-plugins--claude-liam-email-sequence` sibling built earlier
today).

Built entirely fresh this invocation (only SUBJECT.json present on
pickup). Read the same-day, same-family `claude-liam-email-sequence`
sibling as the nearest built precedent and matched its file structure,
beat_sheet.json shape, Manim chip-row scenes.py mechanism, and outro
convention exactly.

Question, facts, and full body argument carried over unchanged: a skill is
a folder Claude reads before it works, with SKILL.md as the complete
instruction set; the Steps section runs linearly, no branching unless a
step says otherwise; the actual job is a structured profile — shape,
quality, and patterns; null rates and column distributions; duplicates or
suspicious values; and which dimensions and metrics are worth analyzing —
not a written report. Use cases carried over: encountering a new table or
file, checking null rates and column distributions, spotting data quality
issues, deciding which dimensions/metrics to analyze.

B00 replaced the source's `ClaudeComposerAsk` typed-ask cold open with
`BrutalistHesitantWriter` (WRITER LAW: "report" → "profile" — the
newcomer's wrong guess that the skill freely explores the data and writes
back some kind of narrative report, corrected to the real question, "does
Claude write a profile?"). Register re-registered Teardown→Plain: source
B03's "gets it right / where it bites" framing was compressed into NB03 as
a plain mechanism description (no verdict, no trade-off language).
Source BVDT's verdict facts (same input, same output, every run; limit is
only what the file says) were folded into the single BCRY carry-out
sentence rather than kept as a separate artifact card, per CARRY-OUT LAW.
Close re-skinned to @HumanitariansAI (`OutroSeries`).

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01/B02
anatomy/pipeline + B03 design tell + BVDT verdict + BHTF your-turn + BOUT
outro). This redo kept the same 7-beat shape: B00→B00 (WRITER LAW
substitution), B01→NB01, B02→NB02, B03→NB03, BVDT folded into BCRY, BHTF
kept (source's prompt assumed an installed Anthropic Skill a general
viewer won't have — "read the explore-data skill and walk me through what
you will do" — so this redo wrote a concrete, paste-ready prompt
exercising the identical mechanism: a CSV in, a profile — rows/columns,
missing values, duplicates, which columns matter — out, with the same
"walk me through your plan before you start" Plato clause the source's own
LENS-AUDIT.md had flagged), BOUT kept. Full audit in SCRIPT.md's six-move
audit and beat-count note.

No source beat was ai-video-prompt, pantry, or a human-drop slot — source's
final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00's mandated cold-open swap. This redo built the
three GRAPHIC beats as fresh Manim (the generic chip-row template,
`scenes.py`/`render_scenes.py`, copied verbatim from the
`claude-liam-email-sequence` sibling and adapted with explore-data-specific
labels) rather than reusing the source's Remotion `SkillTeardown*`
components, matching that sibling's own construction pattern.

Zero inference flags: per ONE-FLAG LAW, every claim in this reel is read
directly off the source sheet's own `narration_text` (principally B00's
untruncated skill description) — no flag needed.

**Build steps, all foreground, all clean on the first pass:**

```
python3 runtime/scripts/generate_audio_kokoro.py <REEL_DIR>
```
7 beats generated, $0.00. B00 11.14s (clears the ≥8s TIMING LAW floor,
with lead_silence_s 1.0 giving the typing a comfortable window).

```
python3 render_scenes.py   # from inside the reel dir
```
3/3 Manim GRAPHIC beats (NB01-NB03) rendered ok, first pass.

```
python3 runtime/scripts/remotion_scenes.py <REEL_DIR>
```
Exceeded the tool's 120s foreground timeout and was moved to the
background by the harness; per the one-shot COMPLETION LAW's
foreground-render rule, this was **not** treated as done on backgrounding —
blocked synchronously on the actual task via `TaskOutput(block=true)`
until it exited (exit 0) before proceeding. All 4 Remotion beats
(B00/BCRY/BHTF/BOUT) confirmed `ok`.

```
python3 runtime/scripts/compile.py <REEL_DIR>
```
Result: `knowledge-work-plugins--claude-liam-explore-data.mp4`, 7/7 beats
filled real (no slate), 80.0s, 3840x2160 (native 4K — compile.py's 4K LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840x2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T (`type_check.py`): PASS, 0 FAILs, first pass (all 7 beats §8.10
  SKIP — no drawtext overlays; PIL-overlay compositing)
- GATE AUDIO: PASS — mean_volume **-24.0 dB**, max -3.0 dB (independently
  re-verified via a standalone `ffmpeg volumedetect` pass), comfortably
  clears the -40 dB floor
- ffprobe: video 3840x2160 h264, audio (aac) present, duration 80.04s; mp4
  mtime (1788484873) newer than beat_sheet.json mtime (1788484772)
- Gate V (visual): pulled 19 frames across the full 80s runtime, including
  4 dedicated pulls inside B00 (t=1.5/4/6/9.5s) to verify the correction
  timing. B00: naive framing types out, "report" appears doomed in
  terracotta at t=6s, corrects and settles to "Does Claude explore my data
  and write a profile?" fully legible and held by t=9.5s — clears the
  TIMING LAW window with margin. NB01-NB03: chip rows, arrows, single
  terracotta accent/underline, and captions all legible, no overlap,
  correct explore-data-specific labels ("explore-data", "build profile",
  "one dataset / the SKILL.md / the profile", "shape, quality, patterns").
  BCRY: carry-out quote + sparkline clean. BHTF: both text-wrap states of
  the paste-ready CSV-profiling prompt read clean, correct
  `@HumanitariansAI` folder label and title. BOUT (`OutroSeries`): eyebrow
  "EXPLORE-DATA · @HumanitariansAI", title restate "Claude, Explore Data."
  No blockers.
- Noted (not fixed, shared-component, matches every sibling logged today):
  `OutroSeries` renders on flat white with a crimson underline rather than
  the humanitarians cream/terracotta skin used everywhere else in the
  reel — the component has no palette props (hardcodes `tokens/vox.ts`).
  Confirmed against the `claude-liam-email-sequence`,
  `claude-liam-design-mcp-workflow`, and other same-day siblings in
  HAILOOP-LOG.md: this is the established series-wide convention, not a
  defect introduced here.

Metadata file written: `knowledge-work-plugins--claude-liam-explore-data.md`
(channel @HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors**). Per `playlists.json`, SUBJECT.json's family
(`knowledge-work-plugins`) matches the map's `"knowledge-work-plugins"` key
directly — no fallback needed. Direct code link per DELIVERY CONTRACT
format included.

**Status: review cut DONE.** Passed every Phase-3 gate.

## 2026-09-03 — Phase 4, DELIVERED

Master was already born native 3840x2160 (compile.py's 4K LAW), so copied
directly to `knowledge-work-plugins--claude-liam-explore-data-4k.mp4`
rather than re-rendering at a higher resolution.

```
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Staged `DELIVERY/knowledge-work-plugins--claude-liam-explore-data/` (4K
master + description) for the Drive sync. Committed to
`claude-bear/knowledge-work-plugins--claude-liam-explore-data/`
(README.md = description, beat_sheet.json, SCRIPT.md, SUBJECT.json,
CARRY-OUT.md, QUESTION.md, BUILD-LOG.md — no mp3/mp4) as commit
`6e91b76e`, pushed clean (no rebase conflicts).

**Status: DELIVERED.**
