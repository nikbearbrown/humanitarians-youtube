# BUILD-LOG — knowledge-work-plugins--claude-liam-email-sequence

## 2026-09-03 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-email-sequence/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `email-sequence`
Skill, already fully built — no SCRIPT.md; source `beats[*].narration_text`
served as the locked script, with B00's complete, untruncated skill
description used as the source of record over the truncated repeats in
B03/BVDT/BHTF).

Picked up **mid-build**: on invocation, SCRIPT.md, CARRY-OUT.md,
QUESTION.md, beat_sheet.json, all 7 mp3s + timings.json, manim/NB01-03.mp4,
and media/B00.mp4 + media/BCRY.mp4 already existed from an earlier pass.
Verified each artifact (ffprobe on B00/BCRY: both carried real audio
tracks, B00 at 10.37s clears the ≥8s TIMING LAW floor) rather than
re-deriving, then continued from the first missing step.

Question, facts, and full body argument carried over unchanged: a skill is
a folder Claude reads before it works, with SKILL.md as the complete
instruction set; the Steps section runs linearly, no branching unless a
step says otherwise; the actual job is designing a full multi-email
sequence — copy for every message, timing between sends, branching logic
for opens/clicks, exit conditions, and benchmarks — not one message; built
for onboarding, lead nurture, re-engagement, win-back, and launch flows.
B00 replaced the source's `ClaudeComposerAsk` typed-ask cold open with
`BrutalistHesitantWriter` (WRITER LAW: "email" → "sequence" — the
newcomer's wrong guess that the skill writes one good email, corrected to
the real question, "does Claude write one sequence?"). Register
re-registered Teardown→Plain: B03's "gets it right / where it bites"
framing was compressed into NB03 as a plain mechanism description (no
verdict, no trade-off language). BVDT's verdict facts (same input, same
output, every run; limit is only what the file says) were merged into the
single BCRY carry-out sentence rather than kept as a separate artifact
card, per CARRY-OUT LAW. Close re-skinned to @HumanitariansAI
(`OutroSeries`).

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01/B02
anatomy/pipeline + B03 design tell + BVDT verdict + BHTF your-turn + BOUT
outro). This redo kept the same 7-beat shape: B00→B00 (WRITER LAW
substitution), B01→NB01, B02→NB02, B03→NB03, BVDT folded into BCRY, BHTF
kept (source's prompt assumed an installed Anthropic Skill a general
viewer won't have, so this redo wrote a concrete, paste-ready prompt
exercising the identical mechanism — one goal in, a designed sequence with
timing/branch/exit out — without requiring any specific Skill install),
BOUT kept. Full audit in SCRIPT.md's six-move audit and beat-count note.

No source beat was ai-video-prompt, pantry, or a human-drop slot — source's
final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00's mandated cold-open swap.

Zero inference flags: per ONE-FLAG LAW, every claim in this reel is read
directly off the source sheet's own `narration_text` (principally B00's
untruncated skill description) — no flag needed.

All 3 GRAPHIC beats (NB01-NB03) built on the shared generic "chip row"
Manim template (`scenes.py`/`render_scenes.py`), copied verbatim from the
`knowledge-work-plugins--claude-liam-discover-brand` sibling and adapted
with email-sequence-specific labels — already rendered on pickup.

**Continuation work this invocation:** BHTF and BOUT carried no rendered
media on pickup. Rendered via:

```
python3 runtime/scripts/remotion_scenes.py <REEL_DIR> --only BHTF
python3 runtime/scripts/remotion_scenes.py <REEL_DIR> --only BOUT
```

(`--only` takes a single beat_id, not a comma list — ran twice.) The BHTF
render exceeded the tool's 120s foreground timeout and was moved to
background by the harness; per the COMPLETION LAW's foreground-render
rule, this was **not** treated as "handled" on backgrounding — blocked
synchronously on the render process's actual pid until it exited (a
Monitor-tool file-existence check fired prematurely on a still-growing,
not-yet-flushed mp4 with no `moov atom`; confirmed still-running via `ps`,
then waited on the real pid with a blocking shell loop before proceeding).
Reverified via ffprobe after the process actually exited: BHTF 19.37s with
audio, BOUT 3.4s with audio, both valid.

Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR>
```

Result: `knowledge-work-plugins--claude-liam-email-sequence.mp4`, 7/7 beats
filled real (no slate), 80.0s, 3840x2160 (native 4K — compile.py's 4K LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840x2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T (type_check.py): PASS, 0 FAILs (all 7 beats §8.10 SKIP — no
  drawtext overlays to check; PIL-overlay compositing)
- GATE AUDIO: PASS — mean_volume **-24.1 dB** (ffmpeg volumedetect, via
  compile.py), comfortably clears the -40 dB floor
- ffprobe: video 3840x2160 h264, audio (aac) present, duration 80.0s; mp4
  mtime (1788481343) newer than beat_sheet.json mtime (1788481256)
- Gate V (visual): pulled frames every 4s across the full runtime (20
  frames) and read all of them — B00 (both pre- and post-correction
  states: "email" doomed in terracotta, then settled "Does Claude write
  one sequence?", legible and held), NB01-NB03 (chip rows, arrows, accent
  underline, captions all legible, no overlap), BCRY (carry-out sentence +
  sparkline clean), BHTF (both text-wrap states of the paste-ready prompt
  read clean, correct @HumanitariansAI handle, correct title), BOUT
  (`OutroSeries`: eyebrow "EMAIL-SEQUENCE · @HumanitariansAI", title
  restate). No blockers. BOUT's white/cream-teal/crimson `OutroSeries`
  palette does not match the humanitarians ground/accent used in the body
  (`#F3EBDD`/`#E4572E`) — checked against two other already-published
  hai-simple siblings (`claude-plugins-official--claude-liam-agent-development`,
  `claude-tag-plugins--claude-liam-redshift-api`) and confirmed this is the
  established, series-wide `OutroSeries`/`OutroCTA` convention (the
  component has no palette props), not a defect introduced here.
- B00 TIMING LAW: `actual_duration_s` 10.35s (>=8s requirement met); "email"
  correction to "sequence" lands and settles well before the clip ends.

Metadata file written: `knowledge-work-plugins--claude-liam-email-sequence.md`
(channel @HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors**). Per `playlists.json`, SUBJECT.json's family
(`knowledge-work-plugins`) matches the map's `"knowledge-work-plugins"` key
directly. Direct code link per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.
