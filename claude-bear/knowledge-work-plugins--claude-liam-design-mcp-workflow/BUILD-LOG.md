# BUILD-LOG — knowledge-work-plugins--claude-liam-design-mcp-workflow

## 2026-09-03 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-design-mcp-workflow/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `design-mcp-workflow`
partner-built skill, Zoom plugin, already fully built — no SCRIPT.md; source
`beats[*].narration_text` served as the locked script). Built entirely fresh
this invocation — only SUBJECT.json existed on pickup.

Question, facts, and full body argument carried over unchanged: a Claude
skill is a folder Claude reads before it works; the SKILL.md file holds the
entire instruction set in plain language; Claude reads the file, then acts —
the file is the program; the instructions live in a Steps section, run in
order, start to finish, no branching unless a step says otherwise; and this
particular skill, design-mcp-workflow, has one job — design a Zoom MCP
workflow for Claude, written for three named moments (deciding whether Zoom's
MCP tools fit a task, planning a tool-based AI workflow, or separating MCP
responsibilities from Zoom's REST API), with nothing to say outside those
three moments. B00 replaced the source's `ClaudeComposerAsk` typed-ask cold
open with `BrutalistHesitantWriter` (WRITER LAW: "ability" -> "file" — the
newcomer's wrong guess that a skill hands Claude some new general ability,
corrected toward the actual mechanism: a skill is one file, scoped to one
job). Register re-registered Teardown -> Plain: the source's B03 "what it
gets right: repeatable results / what it bites: anything outside the spec"
verdict pairing was stripped to a plain scope statement (three named
moments, nothing outside them), per the NO JUDGMENT register check. BVDT's
verdict facts (repeatable same-input/same-output execution, and the
file-only limit) were merged into the single BCRY carry-out sentence rather
than kept as a separate bulleted artifact card, per CARRY-OUT LAW. BHTF's
prompt kept the source's structure (ask Claude to design the Zoom
MCP-vs-REST decision and explain its plan before acting — the same
artifact-vs-world move the source's own LENS-AUDIT.md had flagged as a Plato
move) but was rewritten into one genuinely paste-ready sentence, since the
source string was a truncated fragment ("use when deciding whether zoom mcp
fits a.") that would not actually run cleanly if pasted verbatim. Close
re-skinned to @HumanitariansAI (`OutroSeries`).

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01/B02
anatomy/pipeline + B03 design tell + BVDT verdict + BHTF your-turn + BOUT
outro). This redo kept the same 7-beat shape: B00 carries the wrong-guess
pedagogy per WRITER LAW instead of a dedicated beat; B01 and B02 kept as one
beat each, content essentially unchanged since the source text was already a
plain factual description, not Teardown judgment; B03's verdict pairing
compressed to a plain scope statement; BVDT folded into BCRY; BHTF kept,
reworded to be genuinely runnable; BOUT kept. Full audit in SCRIPT.md's
"Beat-count note (redo)" section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism` /
`ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no substitution
beyond B00's mandated cold-open swap. B01-B03 reuse the source's own generic
`SkillTeardownAnatomy`/`SkillTeardownPipeline`/`SkillTeardownMechanism`
components unchanged — `./art scenes --check` confirmed all patterns used in
this sheet (`BrutalistHesitantWriter`, `SkillTeardownAnatomy`,
`SkillTeardownPipeline`, `SkillTeardownMechanism`, `WantQuote`,
`ClaudeComposerAsk`, `OutroSeries`) are RENDERABLE before slating, so no new
component authoring or GATE L punt was needed.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`); all 7 beats rendered via `remotion_scenes.py` (foreground; the
full-sheet run exceeded the tool's 120s timeout and was moved to background
by the harness automatically — blocked on it via `TaskOutput` before
proceeding, per the COMPLETION LAW's foreground-render rule, never treating
a backgrounded render as "handled" without waiting on it).

First `type_check.py` pass was **FAIL, 1 defect**, fixed at the root:

- **no-wordy-card §8.5, B03** — the `SkillTeardownMechanism` `body` prop (27
  words) exceeded the 12-word pull-quote limit; the screen should show
  structure, not a sentence. Fixed by shortening the on-screen `body` to
  "One decision: Zoom MCP fit, workflow planning, or REST separation." (10
  words) while the full scope statement stayed in `narration_text`
  unchanged — re-rendered B03 only (`--only B03 --force`; the first retry
  attempt was killed by my own overly-tight `timeout 115` bash wrapper
  before Remotion finished, misreporting as a render FAIL with a truncated,
  unrelated Remotion-package-version-mismatch warning as the visible
  stderr tail — confirmed by re-running without an external timeout, which
  completed cleanly and rendered `media/B03.mp4` at 15:16 -- a process
  artifact, not a real defect).

`type_check.py` went 1 -> **PASS, 0 FAILs**. Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Result: `knowledge-work-plugins--claude-liam-design-mcp-workflow.mp4`, 7/7
beats filled real (no slate), 80.6s, 3840x2160 (native 4K — `compile.py`'s
4K LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840x2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (see 1 defect + fix above)
- GATE AUDIO: PASS — mean_volume **-24.1 dB** (ffmpeg volumedetect), max -3.0 dB
- ffprobe: video 3840x2160 h264, audio (aac) present, duration 80.617667s;
  mp4 mtime (1788463854) newer than beat_sheet.json mtime (1788463773)
- Gate V (visual): pulled frames every ~0.5s across the full runtime plus
  targeted checks of B00 (t~1.5s "abil" doomed in terracotta, t~4.0s "Claude
  got a / new file." settled, t~7.5s the full corrected question "Wait —
  what does this skill do?" legible and held to the clip's end), B01-B03
  (anatomy/pipeline/scope cards all legible, B03's shortened body text
  clean post-fix), BCRY (carry-out sentence + sparkline read clean), BHTF
  (correct topic/title/@HumanitariansAI handle, paste-ready prompt text
  legible), and BOUT (OutroSeries: correct eyebrow "DESIGN-MCP-WORKFLOW ·
  @HumanitariansAI", correct title restate, underline draws in, no
  truncation). No blockers.
- **Known library quirk, not a defect I introduced:** `OutroSeries` (and
  `OutroCTA`) hardcode `tokens/vox.ts` (`CREAM: '#FFFFFF'`, i.e. flat white,
  not warm cream; `CRIMSON: '#C8102E'`, not the humanitarians terracotta),
  so BOUT renders on flat white with a red-orange underline rather than the
  reel's `#F3EBDD` cream ground and `#E4572E` terracotta used everywhere
  else. The component's own doc comment still says "cream ground," which is
  stale against the current token file. This is a pre-existing library
  limitation (no palette prop on `OutroSeries`/`OutroCTA`), not something
  introduced by this build, and the `claude-plugins-official--claude-liam-
  agent-development` sibling shipped with the same component/props shape
  without flagging it as a blocker — logged here for visibility, not fixed
  (fixing it would mean authoring/patching a shared library component,
  outside this reel's scope).
- B00 TIMING LAW: `actual_duration_s` 8.17s + `lead_silence_s` 0.8s = 8.97s
  video window (>=8s floor met); the "ability" -> "file" correction lands on
  screen by t~4.0s and the full corrected question stays legible for the
  remainder of the 8.2s clip.

Metadata file written:
`knowledge-work-plugins--claude-liam-design-mcp-workflow.md` (channel
@HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors**). Per `playlists.json`, SUBJECT.json's family
(`knowledge-work-plugins`) is an exact key match in the map, resolving
directly to "Extending Claude — Skills, Plugins & Connectors" (no fallback
needed). Direct code link per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.

## 2026-09-03 — Phase 4, DELIVERED

Master was already born native 3840x2160 (compile.py's 4K LAW), so copied
directly to `knowledge-work-plugins--claude-liam-design-mcp-workflow-4k.mp4`
rather than re-rendering at a higher resolution.

```
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Staged `DELIVERY/knowledge-work-plugins--claude-liam-design-mcp-workflow/`
(4K master + description) for the Drive sync. Committed to
`claude-bear/knowledge-work-plugins--claude-liam-design-mcp-workflow/`
(README.md = description, beat_sheet.json, SCRIPT.md, SUBJECT.json,
CARRY-OUT.md, QUESTION.md, BUILD-LOG.md -- no mp3/mp4) as commit
`43bcee9b`, pushed clean (no rebase conflicts).

**Status: DELIVERED.**
