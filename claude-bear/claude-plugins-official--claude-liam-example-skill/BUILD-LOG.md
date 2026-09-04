# BUILD-LOG — claude-plugins-official--claude-liam-example-skill

## 2026-08-31 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-plugins-official/youtube/claude-liam-example-skill/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `example-skill`
reference template — the SKILL.md schema for model-invoked skills — already
fully built; no SCRIPT.md, so source `beats[*].narration_text` served as the
locked script, cross-checked against the source's own `PEDAGOGY.md`). Built
entirely fresh this invocation — only SUBJECT.json existed on pickup. The
plugin's actual `SKILL.md` file is not present on this machine (the
`plugins/` tree wasn't checked out locally, same situation as the
`claude-cookbooks--claude-liam-creating-financial-models` precedent) — every
fact in this reel is carried from the source reel's already-narrated,
already-reviewed content, nothing invented beyond it.

Question, facts, and full body argument carried over unchanged: a skill is
one file (SKILL.md) in a folder under skills/; frontmatter has four fields
— name (required, identifier) and description (required, the activation
trigger — the field that decides whether Claude activates the skill at
all) plus version and license (optional); the description's own good
pattern names specific trigger phrases, keywords, or topic areas rather
than a topic summary; three activation modes exist (skill = Claude decides
autonomously from context, command = user types the slash, agent = Claude
spawns it for a subtask); the optional directory structure (references/,
examples/, scripts/) supports a complex skill beyond the single-file
minimum; and the concrete gap — nothing specifies how Claude actually
matches a description to a request, and the only testing advice ("test that
it activates for expected queries") comes with no method to run that test.
B00 replaced the source's `ClaudeComposerAsk` typed-ask cold open with
`BrutalistHesitantWriter` (WRITER LAW: "subject" → "trigger" — the
newcomer's wrong guess that a one-line description of the skill's subject
matter is enough for Claude to find it, corrected toward the actual
mechanism: only a description written as a trigger condition gets read at
activation).

Register re-registered Teardown→Plain: the source's B05 "gets it right /
where it bites" list (five strengths, five gaps) was compressed to the
single most teachable, general-audience-actionable fact — you can't verify
your description actually matches, so most people never do — rather than
kept as a full strengths/gaps inventory; the Claude-harness-internals gaps
in the source (embedding vs. keyword vs. exact-phrase matching, the
version/license runtime effect, overlap-detection tooling) were dropped as
assuming a technical audience simple/hai-simple doesn't target, not as a
verdict on the reference template's quality. BVDT's verdict facts were
merged into the single BCRY carry-out sentence rather than kept as a
separate bulleted artifact card, per CARRY-OUT LAW. Close re-skinned to
@HumanitariansAI (`OutroSeries`).

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01/B02
anatomy/design + B05 teardown analysis + BVDT verdict + BHTF your-turn +
BOUT outro). This redo kept the same 7-beat shape: B00 carries the
wrong-guess pedagogy per WRITER LAW instead of a dedicated beat; B01→NB01,
B02→NB02 kept as one beat each; B05's long strengths/gaps list compressed
into NB03 (the one fact a general viewer needs and can act on); BVDT folded
into BCRY; BHTF kept, with the source's already-generic, already-runnable
prompt ("Build a model-invoked skill for a plugin that helps with database
query optimization") carried over unchanged; BOUT kept. Full audit in
SCRIPT.md's "Beat-count note (redo)" section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`ExampleSkillAnatomy` / `ExampleSkillDesign` / `ExampleSkillTell` /
`ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01–NB03) built on the shared generic "chip row"
Manim template (`scenes.py`/`render_scenes.py`) copied verbatim from the
`claude-plugins-official--claude-liam-agent-development` sibling, adapted
with example-skill-specific labels.

**B00 TIMING LAW — trigger word had to change once GATE CONTENT caught
it, not a QC-sampling trap.** First B00 draft used trigger word "topic"
(text: "Does my skill's / topic description / tell Claude / when to use
it?", triggerWords="topic" → "trigger"). Audio generated fine (10.62s) and
the Remotion render completed (10.6s, correction verified legible by frame
pull), but `compile.py`'s GATE CONTENT (`content_check.py`) refused the
compile: `[PLACEHOLDER] BrutalistHesitantWriter.props.triggerWords — value
is a placeholder or sentinel: 'topic'` — "topic" is a literal entry in the
script's generic `_FILLER` sentinel set (alongside "lorem", "tbd",
"placeholder", etc.), matched exactly regardless of context. This is a
real content defect per COMPLETION LAW ("fix content, never the
validator"), not a validator bug: fixed by changing the trigger word to
"subject" (text: "Does my skill's / subject description / tell Claude /
when to use it?", triggerWords="subject" → "trigger", same meaning,
same-length swap), which is not in the filler set. Re-generated B00's audio
only (10.67s) and re-rendered B00 only via `--only B00 --force`
(foreground; the harness moved this and the full-sheet remotion run to
background automatically past the 120s tool timeout — blocked on both via
`TaskOutput` before proceeding, per COMPLETION LAW's foreground-render
rule). Reverified by frame pull: "subject" sits doomed in terracotta at
t≈3.2s, the full corrected question "Does my skill's trigger description
tell Claude when to use it?" is settled and legible by t≈9.8s, held to the
end of the 10.7s clip (well past the ≥8s TIMING LAW floor). Parameters
(42ms/char, 4% mistakeRate, 2% hesitateWithin, 8% hesitateBetween, 26%
jitter) were copied from the `claude-plugins-official--claude-liam-agent-
development` sibling's own proven-safe post-fix settings from the start
(this text is comparable length — 63 vs. that sibling's fixed 60 chars —
so no separate overrun-and-fix cycle was needed for the timing itself).

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`; B00 regenerated once after the trigger-word fix via `--only
B00`); B00/BCRY/BHTF/BOUT rendered via `remotion_scenes.py` (foreground;
both the full-sheet run and the B00-only re-render exceeded the tool's 120s
timeout and were moved to background by the harness automatically —
blocked on each via `TaskOutput` before proceeding, per the COMPLETION
LAW's foreground-render rule); NB01–NB03 rendered via `render_scenes.py`.
First `type_check.py` pass was **PASS, 0 FAILs** — no GATE T defects this
build.

First `compile.py` run was **REFUSED at GATE CONTENT** (the B00
"topic"-sentinel collision above). Fixed per the note above, then a second
gate — Gate V (manual frame-pull review, run after a clean compile) —
caught a second real defect:

- **NB03 chip-label glyph collapse, "no test method"** — a frame pull at
  the beat's accented (BOLD) chip showed "test" and "method" rendered with
  no visible space, reading as "no testmethod." Cropped and re-inspected at
  higher resolution to confirm this wasn't a QC-sampling artifact: the
  space glyph genuinely collapses at BOLD weight in this chip's font/size
  combination, the same weight-dependent spacing-defect class the sibling's
  own NB03 fix (min-size, not spacing) already documented for this
  template. `type_check.py`'s automated §8.1/§8.6b checks did not catch it
  (no min-size or bbox-overlap violation — the glyphs render at full size,
  just without the inter-word gap), so this was caught by the required
  human Gate V frame-read, not by GATE T alone. Fixed by shortening the
  chip label to a single word, "untestable" (semantically equivalent — "no
  test method" and "untestable" both describe the same gap), which cannot
  collapse a space it doesn't contain. Synced `beat_sheet.json`'s
  `graphic.production_viz.chips` for NB03 directly (not via a full
  `build_beat_sheet.py` re-run, which would have discarded the
  already-measured audio durations and render stamps) before re-rendering
  NB03 only and recompiling, per COMPLETION LAW.

`type_check.py` stayed **PASS, 0 FAILs** through both fixes. Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Result: `claude-plugins-official--claude-liam-example-skill.mp4`, 7/7 beats
filled real (no slate), 126.5s, 3840×2160 (native 4K — `compile.py`'s 4K
LAW).

**Gates:**
- content-check: PASS (7 beats, no violations) — after the B00 trigger-word
  fix
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (both compile attempts)
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max -2.8 dB
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 126.46s; mp4
  mtime (1788155880) newer than beat_sheet.json mtime (1788155721)
- Gate V (visual): pulled frames across the full runtime (NB01/NB02/NB03
  chip rows, BCRY carry-out, BHTF your-turn, BOUT outro) plus targeted
  checks of B00 (t≈3.2s "subject" doomed in terracotta, t≈9.8s settled and
  correct, held to the end of the 10.7s clip) and the NB03 fix (re-pulled
  post-fix frame confirms "untestable" renders as one legible word with the
  terracotta accent underline intact). BHTF confirmed correct
  topic/title/@HumanitariansAI handle and paste-ready prompt text; BOUT
  confirmed correct eyebrow "EXAMPLE SKILL · @HumanitariansAI", correct
  title restate, crimson underline, no truncation. No blockers remaining.
- B00 TIMING LAW: `actual_duration_s` 10.7s (≥8s requirement met); the
  "subject" → "trigger" correction lands on screen by t≈9.8s and stays
  legible to the end of the clip.

Metadata file written: `claude-plugins-official--claude-liam-example-skill.md`
(channel @HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors**). Per `playlists.json`, SUBJECT.json's family
(`claude-plugins-official`) matches the map's `"claude-plugins"` prefix (a
`str.startswith` match — `"claude-plugins-official".startswith("claude-
plugins")`), which resolves to "Extending Claude — Skills, Plugins &
Connectors"; this is a more specific match than falling through to the
`hai-simple` skill-key default ("Claude Basics"), consistent with the
`claude-plugins-official--claude-liam-agent-development` sibling built
earlier in this same family. Direct code link per DELIVERY CONTRACT format
included.

**Status: review cut DONE.** Passed every Phase-3 gate.
