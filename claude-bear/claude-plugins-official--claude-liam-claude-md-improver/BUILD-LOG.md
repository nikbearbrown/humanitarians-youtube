# BUILD-LOG — claude-plugins-official--claude-liam-claude-md-improver

## 2026-08-30 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-plugins-official/youtube/claude-liam-claude-md-improver/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `claude-md-improver`
Claude plugin skill, already fully built — no SCRIPT.md; source
`beats[*].narration_text` served as the locked script, per the same pattern
as the `claude-plugins-official--claude-liam-agent-development` sibling).
The source skill's own SKILL.md file
(`anthropics/claude-plugins-official/plugins/claude-md-management/skills/
claude-md-improver/SKILL.md`, referenced in the source sheet's metadata) no
longer exists at that path in this workspace — the source `beat_sheet.json`
narration was treated as the locked script instead, consistent with the
sibling's precedent for sources whose own doc has moved/gone. Built entirely
fresh this invocation — only SUBJECT.json existed on pickup.

Question, facts, and full body argument carried over unchanged: CLAUDE.md
files can live in five locations (project root — shared, git-tracked; local
override — gitignored, personal; global — user-wide defaults; package —
per-monorepo-package; subdirectory — feature-specific), all auto-discovered
by walking parent directories; each file is scored against a six-criterion
rubric (commands/workflows, architecture clarity, non-obvious patterns,
conciseness, currency, actionability) into an A–F letter grade; the
process runs in phases — discovery, scoring, and then a **hard-gated**
quality report that must be shown before any file is touched — only after
approval does the skill propose targeted updates in diff-with-why format
(file, exact addition, one-line reason), never a full rewrite; and one
concrete practical limit — the discovery step's `head -50` cap silently
truncates results in monorepos with more than fifty CLAUDE.md files. B00
replaced the source's `ClaudeComposerAsk` typed-ask cold open with
`BrutalistHesitantWriter` (WRITER LAW: "rewrite" → "score" — the newcomer's
wrong guess that asking Claude to "improve" a CLAUDE.md means an immediate
full rewrite, corrected toward the actual mechanism: the file is scored
against the rubric first, before anything changes). Register re-registered
Teardown→Plain: the source's B05 "gets it right / where it bites" list
(five-location taxonomy, the report-before-update hard gate, the weighted
rubric, the diff-with-why format, the user tips — versus the
unattended-confirmation gap, unclear criterion-weight arithmetic, the
external template reference with no fallback, the `head -50` silent
truncation, and no guidance for when the structure itself is the problem)
was compressed to the single most teachable, general-audience-actionable
fact — the fifty-file discovery cap — rather than kept as a full
strengths/gaps inventory; the Claude-harness-internals gaps (unattended
confirmation flow, criterion weight arithmetic, external template fallback,
"preserve structure" ambiguity) were dropped as assuming a technical
audience simple/hai-simple doesn't target, not as a verdict on the skill's
quality. BVDT's verdict facts (the five-location taxonomy, the
report-before-update gate, the diff-with-why format) were merged into the
single BCRY carry-out sentence rather than kept as a separate bulleted
artifact card, per CARRY-OUT LAW. Close re-skinned to @HumanitariansAI
(`OutroSeries`).

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01/B02
anatomy/design + B05 teardown analysis + BVDT verdict + BHTF your-turn +
BOUT outro). This redo kept the same 7-beat shape: B00 carries the
wrong-guess pedagogy per WRITER LAW instead of a dedicated beat; B01→NB01,
B02→NB02 kept as one beat each; B05's long strengths/gaps list compressed
into NB03 (the one fact a general viewer needs and can act on); BVDT folded
into BCRY; BHTF kept, with the source's already-generic, already-runnable
prompt ("Check and improve my CLAUDE.md files.") carried over unchanged;
BOUT kept. Full audit in SCRIPT.md's "Beat-count note (redo)" section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`ClaudeMdImproverLocations` / `ClaudeMdImproverWorkflow` /
`ClaudeMdImproverTell` / `ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW
required no substitution beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01–NB03) built on the shared generic "chip row"
Manim template (`scenes.py`/`render_scenes.py`) copied verbatim from the
`claude-plugins-official--claude-liam-agent-development` sibling, adapted
with claude-md-improver-specific labels.

**B00 TIMING LAW — verified on first render, no rework needed.** Config
(charMs=42, mistakeRate=4%, hesitateWithin=2%, hesitateBetween=8%, jitter=26)
reused directly from the already-fixed, verified-working configuration on
the `agent-development` sibling (its own first attempt had failed the
timing window at higher rates/slower charMs; this build started from the
post-fix values rather than repeating that discovery). Narration ran 12.37s
(35 words), B00 audio+lead_silence measured 12.4s total. Frame pulls
confirmed: at t≈2.2s "rewrite" sits in terracotta (marked for deletion), by
t≈4.5s it is corrected to "score" with the full question "Will asking
Claude to improve my CLAUDE.md just score the file?" settled, and it stays
legible through the clip's last frame (t≈12s) — well past the ≥8s TIMING
LAW floor.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`); B00/BCRY/BHTF/BOUT rendered via `remotion_scenes.py`
(foreground); NB01–NB03 rendered via `render_scenes.py` (foreground).

First `type_check.py` pass was **FAIL, 1 defect**, fixed at the root:

- **min-size §8.1, NB02** — smallest text run measured 9px, well under the
  20px floor. Root cause: the third chip's original label "diff + why"
  contained a bare "+" glyph, which in this Manim/EB-Garamond render forms
  its own tiny isolated connected-component bounding box (a math-axis-height
  plus sign is far shorter than surrounding letter strokes), tripping the
  min-size check as a separate "text run." Fixed by renaming the chip to
  "the diff" (no symbol characters) — re-rendered NB02 only (NB01/NB03
  untouched), and `beat_sheet.json`'s NB02
  `graphic.production_viz.chips` was patched directly to match (not via a
  full `build_beat_sheet.py` re-run, which would have discarded the
  already-measured audio durations and render stamps) before the recompile,
  per COMPLETION LAW. Second chip also renamed "your OK" → "you approve"
  at the same time (the former rendered with its internal space visually
  collapsed — "yourOK" — a legibility concern caught by eye during the same
  review pass, not a GATE T failure).

`type_check.py` went 1→**PASS, 0 FAILs**.

**Gate V catch beyond GATE T's scope — NB01 chip legibility.** Frame pulls
of the compiled NB01 beat showed the chips "5 locations" and "6 criteria"
rendering with the space after the leading digit visually collapsed
("5locations", "6criteria") — legible on close inspection but reading as a
single fused token at normal viewing distance, a genuine Gate V defect that
GATE T's automated size/contrast checks did not catch (word-spacing, not
size or contrast). Fixed by spelling out the numbers ("five locations",
"six criteria") — re-rendered NB01 only, patched `beat_sheet.json` and
`scenes.py`/`build_beat_sheet.py` directly. Re-verified by a fresh frame
pull, zoomed: the tight-but-clear word gap now reads unambiguously as two
words (confirmed against a control chip, "first 50" in NB03, where a
trailing rather than leading digit renders with a normal, unambiguous
space) — accepted as a font/renderer tracking characteristic, not a defect,
once the digit was no longer the leading character.

Recompiled after both fixes:

```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Result: `claude-plugins-official--claude-liam-claude-md-improver.mp4`, 7/7
beats filled real (no slate), 115.9s, 3840×2160 (native 4K — `compile.py`'s
4K LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (see 1 defect + fix above)
- GATE AUDIO: PASS — mean_volume **-24.1 dB** (ffmpeg volumedetect), max -3.0 dB
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 115.9s; mp4
  mtime (1788147852) newer than beat_sheet.json mtime (1788147652)
- Gate V (visual): pulled frames across the full runtime (every ~8s) plus
  targeted checks of B00 (t≈0s naive framing typing, t≈2.2s "rewrite"
  doomed in terracotta, t≈4.5s settled+correct, held to the clip's last
  frame at t≈12s), NB01 (post-fix "five locations"/"six criteria" legible,
  "A–F grade" accented and underlined correctly), NB02 (post-fix "report" /
  "you approve" / "the diff" all legible, no stray symbols), NB03 ("find" /
  "first 50" / "rest: skipped" legible, control case for the digit-spacing
  question), BCRY (carry-out sentence + sparkline "Score first. Rewrite
  never." read clean once fully faded in), BHTF (correct
  topic/title/@HumanitariansAI handle, paste-ready prompt "Check and
  improve my CLAUDE.md files." legible), and BOUT (OutroSeries: correct
  eyebrow "CLAUDE MD IMPROVER · @HumanitariansAI", correct title restate
  "It Scores Before It Edits.", crimson underline, no truncation). No
  remaining blockers.
- B00 TIMING LAW: `actual_duration_s` 12.4s (≥8s requirement met); the
  "rewrite" → "score" correction lands on screen by t≈4.5s and the full
  corrected question stays legible for the remainder of the clip.

Metadata file written: `claude-plugins-official--claude-liam-claude-md-improver.md`
(channel @HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors**). Per `playlists.json`, SUBJECT.json's family
(`claude-plugins-official`) matches the map's `"claude-plugins"` prefix (a
`str.startswith` match), which resolves to "Extending Claude — Skills,
Plugins & Connectors"; this is a more specific match than falling through
to the `hai-simple` skill-key default ("Claude Basics"), consistent with
the `claude-plugins-official--claude-liam-agent-development` sibling built
in this same family. Direct code link per DELIVERY CONTRACT format
included.

**Status: review cut DONE.** Passed every Phase-3 gate.

## 2026-08-30 — Phase 4, DELIVERED

Master was already born native 3840×2160 (compile.py's 4K LAW), so copied
directly to `claude-plugins-official--claude-liam-claude-md-improver-4k.mp4`
rather than re-rendering at a higher resolution.

```
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Staged `DELIVERY/claude-plugins-official--claude-liam-claude-md-improver/`
(4K master + description) for the Drive sync. Committed to
`claude-bear/claude-plugins-official--claude-liam-claude-md-improver/`
(README.md = description, beat_sheet.json, SCRIPT.md, SUBJECT.json,
CARRY-OUT.md, QUESTION.md, BUILD-LOG.md — no mp3/mp4) as commit
`882a5426`, pushed clean (no rebase conflicts).

**Status: DELIVERED.**
