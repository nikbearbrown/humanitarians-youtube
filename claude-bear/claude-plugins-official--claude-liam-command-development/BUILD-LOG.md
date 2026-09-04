# BUILD-LOG — claude-plugins-official--claude-liam-command-development

## 2026-08-31 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-plugins-official/youtube/claude-liam-command-development/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `command-development`
Claude plugin-dev Skill, already fully built — no SCRIPT.md on the source;
PEDAGOGY.md and the source `beats[*].narration_text` served as the locked
script). Built entirely fresh this invocation — only SUBJECT.json existed
on pickup.

Question, facts, and full body argument carried over unchanged: a slash
command is a Markdown file with YAML frontmatter whose body is a directive
TO Claude, not a message to the user; commands live in three locations
(project — team-shared, project-only; personal — all projects; plugin —
bundled with an installed plugin); frontmatter has five fields (description,
allowed-tools, model, argument-hint, disable-model-invocation); arguments
come as `$ARGUMENTS` (full string) or `$1`/`$2` (positional); file
references use `@` (argument-driven or static); plugin commands get
`CLAUDE_PLUGIN_ROOT` for hardcode-free paths; `.claude/commands/` is noted
as legacy in favor of `.claude/skills/<name>/SKILL.md`; and the one gap
carried into the general-audience cut — bash execution (`!` + backticks) is
the most useful dynamic feature but isn't shown inline in the skill that
teaches command-writing. B00 replaced the source's `ClaudeComposerAsk`
typed-ask cold open with `BrutalistHesitantWriter` (WRITER LAW: "them" →
"Claude" — the newcomer's wrong guess that a command body is written for
the person running it, corrected toward the actual for-Claude framing, the
single most-teachable point in the source). Register re-registered
Teardown→Plain: the source's B05 "gets it right / where it bites" list was
compressed to the single most teachable, general-audience gap (the bash
deferral) rather than kept as a full strengths/gaps inventory — the
Claude-harness-internals gaps in the source ($IF non-syntax misreadability,
unexplained `Bash(git:*)` namespace scope rules, uncompared
commands-vs-skills discovery) were dropped as assuming a technical audience
simple/hai-simple doesn't target, not as a verdict on the skill's quality.
BVDT's verdict facts were merged into the single BCRY carry-out sentence
rather than kept as a separate bulleted artifact card, per CARRY-OUT LAW.
Close re-skinned to @HumanitariansAI (`OutroSeries`).

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01/B02
anatomy/design + B05 teardown analysis + BVDT verdict + BHTF your-turn +
BOUT outro). This redo kept the same 7-beat shape: B00 carries the
wrong-guess pedagogy per WRITER LAW instead of a dedicated beat; B01→NB01,
B02→NB02 kept as one beat each; B05's long strengths/gaps list compressed
into NB03 (the one fact a general viewer needs and can act on); BVDT folded
into BCRY; BHTF kept, with the source's already-generic, already-runnable
prompt ("Create a slash command called review-pr that takes a PR number as
an argument, reads the changed files, and reviews them for code quality")
carried over unchanged; BOUT kept. Full audit in SCRIPT.md's "Beat-count
note (redo)" section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`CommandDevAnatomy` / `CommandDevContent` / `CommandDevTell` /
`ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01–NB03) built on the shared generic "chip row"
Manim template (`scenes.py`/`render_scenes.py`) copied verbatim from the
`claude-plugins-official--claude-liam-agent-development` sibling, adapted
with command-development-specific labels.

**B00 grammar defect caught and fixed, not a QC-sampling trap.** First
render's base text was "for the user?" with `triggerWords: "user"` →
`replacementWords: "Claude"`, which only swaps the single token and leaves
the article untouched — the settled correction read "for the Claude?", an
ungrammatical proper-noun-with-article error, confirmed by a frame pull at
t≈9.4s of the 9.6s clip. Root cause: any single-word swap from a common
noun (which takes "the") to a proper noun (which doesn't) will produce this
mismatch whenever the base sentence keeps the article. Fixed by rewording
the naive line's last token to a pronoun that needs no article either way
("for them?" → "for Claude?"), re-rendering B00 only. Reverified: "them"
sits doomed in terracotta at t≈7.0s, deletion/retype visible through
t≈7.8s, and "When I write a command body, am I writing it for Claude?"
settles legible by t≈8.4s of the 9.6s clip (TIMING LAW's ≥8s floor met).

**Two chip-label defects caught and fixed via Gate V, not GATE T (which
does not check word-spacing).** Manually pulling frames on NB01/NB03 before
GATE T (habit carried from prior siblings' "leading-digit chip" bug)
surfaced two real space-collapse renders:
- NB01's `"3 locations"`/`"5 fields"` rendered as `"3locations"`/`"5fields"`
  — the established digit-immediately-followed-by-space-then-letter
  collapse (same class as the `claude-md-improver` sibling's fix). Spelling
  out `"five fields"` (11 chars) stayed in the larger font tier and
  resolved cleanly, but the first respelling attempt, `"three locations"`
  (15 chars — one character over the ≤14-char tier cutoff), dropped to a
  smaller font tier and **introduced a new, independent GATE T min-size
  FAIL** (17px < 20px floor) on the first `type_check.py` pass after the
  respelling. Root-caused by char-count arithmetic against `scenes.py`'s
  tier thresholds (`fs=26` at ≤14 chars, `fs=22` beyond), not by guessing —
  the sibling's own proven fix (`"five locations"`, exactly 14 chars) had
  landed inside the safe tier by one character, which the naive "just
  spell it out" substitution missed. Fixed by shortening to `"three
  spots"` (11 chars), back in the fs=26 tier.
- NB03's `"most useful"` (NORMAL weight, no digit involved) rendered as
  `"mostuseful"` — a previously undocumented collapse variant, confirmed by
  cropping the exact chip and comparing against passing BOLD/accented
  two-word chips (`"reference file"`, `"@file refs"`) in the same beat,
  which isolated the failure to non-bold weight rather than to digits.
  Fixed by replacing the two-word label with the single word `"handiest"`,
  which removes the internal space entirely rather than trying to predict
  which letter-pairs are safe.

Both fixes were applied directly in `scenes.py`/`build_beat_sheet.py`/
`beat_sheet.json` (not a full `build_beat_sheet.py` re-run, which would
have discarded the already-measured audio durations and render stamps);
NB01 and NB03 were re-rendered individually via `render_scenes.py` (which
skips beats whose `manim/<id>.mp4` already exists, so the target file was
deleted first each time) before each recompile.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`, cost $0.00); B00 rendered and re-rendered via
`remotion_scenes.py` (foreground; both the full-sheet run and the B00-only
re-render exceeded the tool's 120s timeout and were moved to background by
the harness automatically — blocked on each via `TaskOutput` before
proceeding, per the COMPLETION LAW's foreground-render rule); NB01–NB03
rendered via `render_scenes.py` (all three render calls stayed under the
foreground timeout). First `type_check.py` pass (after the "three
locations" respelling) was **FAIL, 1 defect** (see chip fix above, second
bullet's parent cause); after the "three spots" fix, `type_check.py` went
to **PASS, 0 FAILs**.

Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Result: `claude-plugins-official--claude-liam-command-development.mp4`,
7/7 beats filled real (no slate), 132.8s, 3840×2160 (native 4K —
`compile.py`'s 4K LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (see chip-label defects + fixes above)
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (ffmpeg volumedetect), max -2.9 dB
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 132.8s; mp4
  mtime (1788149824) newer than beat_sheet.json mtime (1788149696)
- Gate V (visual): pulled frames across the full runtime (t=2/5/7/7.8/8.4/
  9.3/9.4s targeted on B00; ~10-15s spacing elsewhere) plus targeted checks
  of B00 (the "them"→"Claude" correction sequence), NB01–NB03 (all chips
  legible post-fix, parallel sizing, no space-collapse), BCRY (carry-out
  sentence + sparkline read clean), BHTF (correct topic/title/
  @HumanitariansAI handle, paste-ready prompt text legible), and BOUT
  (OutroSeries: correct eyebrow "COMMAND DEVELOPMENT · @HumanitariansAI",
  correct title restate, crimson underline, no truncation). No blockers.
- B00 TIMING LAW: `actual_duration_s` 9.58s narration + 1.0s lead_silence =
  10.58s total window (≥9s requirement met); rendered clip is 9.6s; the
  "them" → "Claude" correction lands on screen by t≈8.4s and stays legible
  through the end of the clip.

Metadata file written: `claude-plugins-official--claude-liam-command-development.md`
(channel @HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors**). Per `playlists.json`, SUBJECT.json's family
(`claude-plugins-official`) matches the map's `"claude-plugins"` prefix (a
`str.startswith` match), consistent with every other `claude-plugins-official`
sibling built to date (access, agent-development, build-mcp-app,
build-mcp-server, build-mcpb, cardputer-buddy,
claude-automation-recommender, claude-md-improver). Direct code link per
DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.

## 2026-08-31 — Phase 4, DELIVERED

Master was already born native 3840×2160 (compile.py's 4K LAW), so copied
directly to `claude-plugins-official--claude-liam-command-development-4k.mp4`
rather than re-rendering at a higher resolution.

```
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Staged `DELIVERY/claude-plugins-official--claude-liam-command-development/`
(4K master + description) for the Drive sync. Committed to
`claude-bear/claude-plugins-official--claude-liam-command-development/`
(README.md = description, beat_sheet.json, SCRIPT.md, SUBJECT.json,
CARRY-OUT.md, QUESTION.md, BUILD-LOG.md — no mp3/mp4) as commit
`6ff6a9e0`, pushed clean (no rebase conflicts).

**Status: DELIVERED.**
