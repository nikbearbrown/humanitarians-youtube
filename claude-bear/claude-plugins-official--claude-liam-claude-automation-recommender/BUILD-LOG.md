# BUILD-LOG — claude-plugins-official--claude-liam-claude-automation-recommender

## 2026-08-30 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-plugins-official/youtube/claude-liam-claude-automation-recommender/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic
`claude-automation-recommender` Claude Code Skill, already fully built — no
SCRIPT.md; source `beats[*].narration_text` served as the locked script,
per the redo contract). A prior filmloop worker had claimed this reel
(empty `.filmloop/claude-plugins-official--claude-liam-claude-automation-
recommender.w44071.out` log) but left no artifacts — only SUBJECT.json
existed on pickup. Built entirely fresh this invocation. (A separate,
unrelated sibling `claude-plugins--claude-liam-claude-automation-
recommender`, family `claude-plugins` not `claude-plugins-official`, exists
alongside this one with its own unstarted SUBJECT.json — a different queue
entry, different source, not touched.)

Question, facts, and full body argument carried over unchanged: the skill
is read-only — it scans a codebase for signals (language/framework from
package files, existing Claude config, test setup, CI config, database and
API code) and recommends automations across five extensibility types
(Hooks: event-driven; Subagents: parallel; Skills: deliberately invoked;
Plugins: bundles; MCP Servers: external tools); it works in three phases
(analyze, match-and-cap at one-to-two recommendations per category with an
explicit "ask for more" offer, then report); concrete signal examples
carried over verbatim (Prettier → format hook, GitHub repo → GitHub MCP
server, auth/payments code → security-reviewing subagent). B00 replaced
the source's `ClaudeComposerAsk` typed-ask cold open with
`BrutalistHesitantWriter` (WRITER LAW: "build" → "recommend" — the
newcomer's wrong guess that asking for automation recommendations means
Claude will build them, corrected toward the actual mechanism: it only
ever recommends). Register re-registered Teardown→Plain: the source's B05
"gets it right / where it bites" list was compressed to the single most
teachable, general-audience fact (recommending isn't the same as handing
you a runnable step — a subagent recommendation points at a template file
instead of a scaffold, a plugin recommendation names the plugin but not
the install command) rather than kept as a full strengths/gaps inventory —
the Claude-harness-internals gaps in the source (unenforced
beyond-reference-files instruction, no monorepo guidance, no
when-not-to-recommend guidance) were dropped as assuming a technical
audience simple/hai-simple doesn't target, not as a verdict on the skill's
quality. BVDT's verdict facts were merged into the single BCRY carry-out
sentence rather than kept as a separate bulleted artifact card, per
CARRY-OUT LAW. Close re-skinned to @HumanitariansAI (`OutroSeries`).

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01/B02
anatomy/design + B05 teardown analysis + BVDT verdict + BHTF your-turn +
BOUT outro). This redo kept the same 7-beat shape: B00 carries the
wrong-guess pedagogy per WRITER LAW instead of a dedicated beat; B01→NB01
(five types, trimmed of B01's trailing skill-authoring invocation-control
tangent — not about what the automation recommender does, and assumes a
skill-building audience this reel doesn't target), B02→NB02 (analyze,
match, cap, with concrete signal examples) kept as one beat each; B05's
long strengths/gaps list compressed into NB03 (the one fact a general
viewer needs and can act on); BVDT folded into BCRY; BHTF kept, with the
source's prompt ("Analyze this codebase and recommend Claude Code
automations") carried over, generalized to "any real project" rather than
the source's specific React TypeScript setup so the check works regardless
of the viewer's own stack; BOUT kept. Full audit in SCRIPT.md's "Beat-count
note (redo)" section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`AutomationRecommenderTypes` / `AutomationRecommenderSignals` /
`AutomationRecommenderTell` / `ClaudeVerdictArtifact`), so NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's mandated cold-open
swap.

All 3 GRAPHIC beats (NB01–NB03) built on the shared generic "chip row"
Manim template (`scenes.py`/`render_scenes.py`) copied verbatim from the
`claude-plugins-official--claude-liam-agent-development` sibling, adapted
with automation-recommender-specific labels.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`; B00 measured 10.28s, clearing the >=8s TIMING LAW floor on the
first pass — no retune needed). `remotion_scenes.py` (B00/BCRY/BHTF/BOUT)
exceeded the tool's 120s foreground timeout and was auto-backgrounded by
the harness; blocked on it explicitly via `TaskOutput` (exit 0) before
proceeding, per the ONE-SHOT/COMPLETION LAW — never treated the
backgrounded render as "handled" without waiting on it. NB01–NB03 rendered
via `render_scenes.py` in the foreground (well under the timeout). Frame
pulls at t≈2s/5.5s/9.5s on B00 confirmed the "build"→"recommend" correction:
"bui" doomed in terracotta at t≈2s, "recommend" already settled by t≈5.5s,
the full corrected question "Can I ask Claude to recommend my Claude Code
automations?" fully typed and legible at t≈9.5s of the 10.3s clip.

First `type_check.py` pass was **FAIL, 1 defect**, fixed at the root:

- **min-size §8.1, NB03** — smallest text run measured 17px, 3px under the
  20px floor. Renaming the flagged chip alone ("you look it up" → "your
  lookup") did not change the measurement at all, ruling out that chip as
  the cause. Diagnosed by rendering an intermediate frame: the actual
  culprit was the accented middle chip, "not the command" (15 chars, over
  the renderer's `len<=14` cutoff for the larger 26pt font tier, so it
  rendered at the smaller 22pt tier — and, being BOLD *and* over the
  chip's width-fit threshold, was additionally scale-compressed to fit,
  landing under the floor even though bold strokes are normally sturdier
  than the normal-weight failures seen on sibling reels). Fixed by
  shortening the label to "no command" (10 chars), which both bumped it
  back to the larger font tier and removed the width-driven compression —
  re-rendered NB03 only (NB01/NB02 untouched), and `beat_sheet.json`'s
  `graphic.production_viz.chips` for NB03 was synced to the fixed wording
  directly (not via a full `build_beat_sheet.py` re-run, which would have
  discarded the already-measured audio durations and render stamps)
  before the recompile, per COMPLETION LAW.

`type_check.py` went 1→**PASS, 0 FAILs**. Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Result: `claude-plugins-official--claude-liam-claude-automation-recommender.mp4`,
7/7 beats filled real (no slate), 148.6s, 3840×2160 (native 4K —
`compile.py`'s 4K LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (see 1 defect + fix above)
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (compile.py + independently
  verified via `ffmpeg volumedetect`), max -2.8 dB
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 148.58s; mp4
  mtime (1788146026) newer than beat_sheet.json mtime (1788145860)
- Gate V (visual): pulled frames across the full runtime (t=15/30/55/65/
  90/100/117/125/140/147s) plus targeted checks of B00 (t≈2s "bui" doomed
  in terracotta, t≈5.5s "recommend" settled, t≈9.5s full corrected
  question legible), NB01 (five chips: Hooks/Subagents/Skills/Plugins/MCP,
  all legible and evenly sized), NB02 (read codebase → match signal → cap
  at 1-2, accented and legible), NB03 (post-fix: names it / no command /
  your lookup, all legible, accent underline clean), BCRY (carry-out
  sentence + sparkline read clean, quote marks and italic serif intact),
  BHTF (correct topic "AUTOMATION RECOMMENDER · CLAUDE PLUGIN", correct
  segment title, correct @HumanitariansAI folder label, paste-ready prompt
  legible), and BOUT (OutroSeries: correct eyebrow "AUTOMATION
  RECOMMENDER · @HumanitariansAI", correct title restate "Recommend, Not
  Install.", crimson underline, no truncation). No blockers.
- B00 TIMING LAW: `actual_duration_s` 10.28s (≥8s requirement met); the
  "build" → "recommend" correction lands on screen by t≈5.5s and the full
  corrected question stays legible for the remainder of the clip.

Metadata file written: `claude-plugins-official--claude-liam-claude-automation-recommender.md`
(channel @HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors**). Per `playlists.json`, SUBJECT.json's family
(`claude-plugins-official`) matches the map's `"claude-plugins"` prefix (a
`str.startswith` match), which resolves to "Extending Claude — Skills,
Plugins & Connectors"; this is a more specific match than falling through
to the `hai-simple` skill-key default ("Claude Basics"), consistent with
the `access`/`agent-development`/`build-mcp-app`/`build-mcp-server`/
`build-mcpb`/`cardputer-buddy` siblings built in this same family. Direct
code link per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.

## 2026-08-30 — Phase 4, DELIVERED

Master was already born native 3840×2160 (compile.py's 4K LAW), so copied
directly to `claude-plugins-official--claude-liam-claude-automation-recommender-4k.mp4`
rather than re-rendering at a higher resolution.

```
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Staged `DELIVERY/claude-plugins-official--claude-liam-claude-automation-recommender/`
(4K master + description) for the Drive sync. Committed to
`claude-bear/claude-plugins-official--claude-liam-claude-automation-recommender/`
(README.md = description, beat_sheet.json, SCRIPT.md, SUBJECT.json,
CARRY-OUT.md, QUESTION.md, BUILD-LOG.md — no mp3/mp4) as commit
`46036b3c`, pushed clean (no rebase conflicts).

**Status: DELIVERED.**
