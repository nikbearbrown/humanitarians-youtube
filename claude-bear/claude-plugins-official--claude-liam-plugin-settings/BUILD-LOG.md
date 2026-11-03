# BUILD-LOG — claude-plugins-official--claude-liam-plugin-settings

## 2026-08-31 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-plugins-official/youtube/claude-liam-plugin-settings/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `plugin-settings`
Claude plugin-dev Skill, already fully built — no SCRIPT.md on the source;
the source `beats[*].narration_text` served as the locked script). Built
entirely fresh this invocation — only SUBJECT.json existed on pickup.

Question, facts, and full body argument carried over unchanged: a plugin's
settings live in one file, `.claude/plugin-name.local.md`, in the project
root, with two parts (YAML frontmatter for structured settings, a markdown
body for prompts/instructions); three consumers read it (bash hooks,
command files, agent instructions); it's per-project, user-managed, never
committed to git; the operational patterns that make it safe are
schema-first design with sensible defaults, a quick-exit guard in hooks,
and a gitignore entry that must be added manually per project; and no
change takes effect until a full Claude Code restart (no hot reload). B00
replaced the source's `ClaudeComposerAsk` typed-ask cold open with
`BrutalistHesitantWriter` (WRITER LAW: "now" → "later" — the newcomer's
wrong guess that a toggled setting applies immediately, corrected toward
the actual restart-required framing, the single most-repeated gotcha in
the source, called "the key constraint" at B00 and repeated at B02/B05/
BHTF). Register re-registered Teardown→Plain: the source's B05
"gets it right / where it bites" list was compressed to the single most
teachable, general-audience gap (settings don't carry over between
projects) rather than kept as a full strengths/gaps inventory — the
Claude-harness-internals gaps in the source (sed's CRLF parsing failure,
grep/sed's silent YAML-array mis-parsing) were dropped as assuming a
technical, script-authoring audience simple/hai-simple doesn't target, not
as a verdict on the skill's quality. BVDT's verdict facts were merged into
the single BCRY carry-out sentence rather than kept as a separate bulleted
artifact card, per CARRY-OUT LAW. Close re-skinned to @HumanitariansAI
(`OutroSeries`).

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01/B02
anatomy/design + B05 teardown analysis + BVDT verdict + BHTF your-turn +
BOUT outro) — the identical shape to the `command-development` sibling
built the same day. This redo kept the same 7-beat shape: B00 carries the
wrong-guess pedagogy per WRITER LAW instead of a dedicated beat; B01→NB01,
B02→NB02 kept as one beat each; B05's long strengths/gaps list compressed
into NB03 (the one fact a general viewer needs and can act on: no
carryover between projects); BVDT folded into BCRY; BHTF kept, trimmed
from the source's five watch-items to three (dropping the two that assume
the viewer is authoring the plugin's own bash hooks); BOUT kept. Full
audit in SCRIPT.md's "Beat-count note (redo)" section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`PluginSettingsAnatomy` / `PluginSettingsPatterns` / `PluginSettingsTell` /
`ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01–NB03) built on the shared generic "chip row"
Manim template (`scenes.py`/`render_scenes.py`) copied verbatim from the
`claude-plugins-official--claude-liam-command-development` sibling,
adapted with plugin-settings-specific labels.

**Title changed mid-build after a GATE T investigation, not guessed
around.** First compile's title "No Restart, No Effect." (BOUT/OutroSeries)
FAILed GATE T min-size: smallest text run 38px < 41px floor. Rather than
assume this was a known false positive and add a blanket pattern-name
exemption (OutroSeries has no existing min-size exemption in
`type_check.py`, unlike the documented Manim-scene isolated-glyph
exemptions), instrumented `type_check.py`'s own
`visible_text_mask`/`labeled_blobs`/`text_run_bboxes` functions directly
against a pulled frame to locate the exact failing blob: a single
58×38px bbox at (1559,1097)-(1617,1135) — the lowercase "o" in "No",
isolated from the "N" by kerning and measuring shorter than the serif
font's cap-height run at this exact font size. Per hai-simple SKILL.md
("fix content, never the validator"), tested an alternative title
("Restart Required.") by patching the beat, re-rendering only BOUT, and
re-running the same measurement script directly on the output frame before
committing to the change — confirmed PASS (min_h 48px via the
individual-char fallback path) before touching any other file. Title
propagated to metadata.title, BOUT's narration + `line` prop, BHTF's
`segment` prop, build_beat_sheet.py, and SCRIPT.md; BOUT/BHTF audio (only
BOUT's narration text changed) and both beats re-rendered.

**Two chip-label space-collapse defects caught by Gate V, not GATE T
(which does not check word-spacing) — same class of bug as the
`command-development` sibling's documented "leading-digit" collapse, but
triggered by different word pairs.** Frame-pulling the full compiled cut
(the mandatory Gate V pass, run twice — once before and once after the
title fix, since NB01/NB02/NB03 were re-rendered in between) surfaced
three real space-collapse renders, none caught by GATE T (a pixel-size
check, not a spacing check):
- NB01's `"3 consumers"` rendered as `"3consumers"` — the established
  digit-immediately-followed-by-space-then-letter collapse. Spelling out
  `"three consumers"` (15 chars) crossed the chip-label font-size tier
  boundary (>14 chars drops to fs=22) and re-triggered a genuine, separate
  GATE T min-size FAIL (18px < 20px) once scaled down to fit the box width
  — the same tier-boundary trap documented in the `command-development`
  sibling's BUILD-LOG. Fixed by shortening to `"three readers"` (13
  chars), landing back inside the fs=26 tier with no digit-leading prefix.
- NB02's `"defaults first"` (NORMAL weight, no digit involved) rendered as
  `"defaultsfirst"` — a word-pair-specific collapse, not digit- or
  weight-related (the sibling's own note that this bug correlates with
  non-bold weight did not hold here: NB03's collapsed chip below was
  BOLD/accented and still collapsed). Fixed by hyphenating to
  `"defaults-first"`, matching the already-passing `"quick-exit"` chip's
  proven safe pattern.
- NB03's `"not global"` (BOLD/accented) rendered as `"notglobal"` — same
  word-pair collapse class, confirmed by side-by-side comparison against
  the same beat's non-collapsing `"no carryover"` chip (also two words, no
  hyphen, not accented) — isolating the defect to the specific
  letter-pair/kerning combination in "t"+"g", not a general
  weight/digit/length rule. Fixed by hyphenating to `"not-global"`.

All three fixes applied directly in `scenes.py`/`build_beat_sheet.py`/
`beat_sheet.json` (not a full `build_beat_sheet.py` re-run, which would
have discarded the already-measured audio durations and render stamps);
affected beats were deleted from `manim/` and re-rendered individually via
`render_scenes.py` (which skips beats whose output already exists) before
each recompile. Re-pulled frames after each round of fixes confirmed
clean legible chips with correct spacing.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`, cost $0.00; BOUT regenerated once after the title change); B00/
BCRY/BHTF/BOUT rendered via `remotion_scenes.py` (foreground; the initial
full-sheet run and the later BOUT+BHTF re-render both exceeded the tool's
120s timeout and were moved to background by the harness automatically —
blocked on each via `TaskOutput` before proceeding, per the COMPLETION
LAW's foreground-render rule); NB01–NB03 rendered via `render_scenes.py`
(all render calls, including the three individual re-renders, stayed under
the foreground timeout). Final `type_check.py` pass: **PASS, 0 FAILs**.

Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Result: `claude-plugins-official--claude-liam-plugin-settings.mp4`, 7/7
beats filled real (no slate), 97.8s, 3840×2160 (native 4K — `compile.py`'s
4K LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (see title + chip-label defects/fixes above)
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max -2.8 dB
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 97.8s; mp4
  mtime (1788168062) newer than beat_sheet.json mtime (1788167964)
- Gate V (visual): pulled frames across the full runtime (every 6-8s) plus
  targeted checks of B00 (the "now"→"later" correction, confirmed legible
  and complete by t≈8s of the ~12s clip), NB01–NB03 (all chips legible
  post-fix, correct spacing, no space-collapse, no font-tier truncation),
  BCRY (carry-out sentence + sparkline read clean), BHTF (correct topic/
  title/@HumanitariansAI handle, paste-ready prompt text legible mid-type),
  and BOUT (OutroSeries: correct eyebrow "PLUGIN SETTINGS ·
  @HumanitariansAI", correct title restate "Restart Required.", crimson
  underline, no truncation, no sub-floor text). No blockers.
- B00 TIMING LAW: `actual_duration_s` 12.05s narration + 1.0s lead_silence
  = 13.05s total window (≥9s requirement met); rendered clip extended to
  12.1s; the "now"→"later" correction lands on screen well before the clip
  ends.

Metadata file written: `claude-plugins-official--claude-liam-plugin-settings.md`
(channel @HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors**). Per `playlists.json`, SUBJECT.json's family
(`claude-plugins-official`) matches the map's `"claude-plugins"` prefix (a
`str.startswith` match), consistent with every other `claude-plugins-official`
sibling built to date (access, agent-development, build-mcp-app,
build-mcp-server, build-mcpb, cardputer-buddy,
claude-automation-recommender, claude-md-improver,
command-development). Direct code link per DELIVERY CONTRACT format
included.

**Status: review cut DONE.** Passed every Phase-3 gate.
