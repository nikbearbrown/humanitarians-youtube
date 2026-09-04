# BUILD-LOG — skills--claude-liam-internal-comms

## 2026-09-04 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/skills/youtube/claude-liam-internal-comms/beat_sheet.json` (a
Teardown skill-teardown walkthrough of the Anthropic `internal-comms`
Claude Skill, already fully built — no SCRIPT.md on the source; the
source's `PEDAGOGY.md`, `SOURCES.md`, and `beats[*].narration_text` served
as the locked script). Built entirely fresh this invocation — only
SUBJECT.json existed on pickup.

Question, facts, and full body argument carried over unchanged: the skill
covers seven kinds of internal writing mapped to four guideline files (3P
updates, company newsletters, FAQ answers, and status/leadership/project
updates/incident reports routing to the remaining files or a general-comms
fallback); the guideline file is authoritative — identify the type, load
the file, follow it exactly; the 3P format is the most constrained (one
emoji, team name, dates, then Progress/Plans/Problems at one to three
sentences each, data-driven, a 30-60s read, bigger teams needing bigger
3Ps); and the skill is built to ask when the type is unclear rather than
guess. B00 replaced the source's `ClaudeComposerAsk` typed-ask cold open
with `BrutalistHesitantWriter` (WRITER LAW: "write" → "format" — the
newcomer's wrong guess that asking Claude for a team update means it just
writes one however it sounds best, corrected toward the actual
identify-then-format framing, the single most-teachable point in the
source: "the skill is a router, not a writer"). Register re-registered
Teardown→Plain: the source's B05 "router insight + gets-right/bites"
teardown analysis was compressed into a both-directions mechanism
description (NB03: exact-match routing is fixed and strict; a fallback to
general-comms is looser; an unclear case gets an explicit ask) rather than
kept as a strengths/gaps verdict list — the producer/maintainer-flavored
gaps in the source (guideline files must be populated and maintained by
the team; the FAQ format needs company-wide source access Claude may not
have) were dropped as assuming a technical/maintainer audience
simple/hai-simple doesn't target, not as a verdict on the skill's quality.
BVDT's verdict facts were merged into the single BCRY carry-out sentence
rather than kept as a separate bulleted artifact card, per CARRY-OUT LAW.
Close re-skinned to @HumanitariansAI (`OutroSeries`), title borrowed
verbatim from the source's own best line: "A Router, Not A Writer."

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01
routing anatomy + B02 3P self-demo + B05 teardown analysis + BVDT verdict +
BHTF your-turn + BOUT outro). This redo kept the same 7-beat shape: B00
carries the wrong-guess pedagogy per WRITER LAW instead of a dedicated
beat; B01→NB01, B02→NB02 kept as one beat each; B05's router-insight
analysis compressed into NB03 (the both-directions fact a general viewer
needs and can act on); BVDT folded into BCRY; BHTF kept, with the source's
already-generic, already-runnable prompt (a 3P update for the Product
Design team covering onboarding redesign / user testing / design-system
blocker) carried over unchanged; BOUT kept. Full audit in SCRIPT.md's
"Beat-count note (redo)" section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`InternalCommsAnatomy` / `InternalComms3P` / `InternalCommsTell` /
`ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01–NB03) built on the shared generic "chip row"
Manim template (`scenes.py`/`render_scenes.py`) copied verbatim from the
`claude-plugins-official--claude-liam-command-development` sibling,
adapted with internal-comms-specific labels.

**Two chip-label space-collapse defects caught via Gate V frame pulls (not
GATE T, which does not check word-spacing), same defect class the
`command-development` sibling documented and fixed:**
- NB01's `"four files"` (NORMAL weight, two words) rendered as
  `"fourfiles"` at t=20s — confirmed by frame pull, compared against the
  same beat's `"seven types"` chip (also NORMAL, two words, same font
  tier), which rendered correctly, isolating the failure to this specific
  word pair rather than a general two-word-NORMAL rule. Fixed by replacing
  with the single word `"guides"` (11→6 chars, still describes the four
  guideline files, no internal space to collapse). Reverified at t=20s
  post-fix: "seven types → guides → load it" all legible, correctly spaced.
- NB03's `"ask first"` (BOLD/accented, two words) rendered as
  `"askfirst"` at t=63s — notable because the `command-development`
  sibling's accented two-word chips (`"five fields"`, `"reference file"`)
  had all passed clean, so accent/weight alone does not predict this
  bug; it is word-pair-specific and was previously undocumented for
  accented chips specifically. Fixed by replacing with the single word
  `"ask"` (already explained fully by the beat's own caption, "no clean
  match -> ask, never freestyle"). Reverified at t=63s post-fix: "exact
  match / general comms / ask" all legible, correctly spaced, terracotta
  underline intact.

Both fixes were applied directly in `scenes.py`/`build_beat_sheet.py`/
`beat_sheet.json` (not a full `build_beat_sheet.py` re-run, which would
have discarded the already-measured audio durations and render stamps);
NB01 and NB03 were re-rendered individually via `render_scenes.py` (which
skips beats whose `manim/<id>.mp4` already exists, so the target files
were deleted first) before recompiling.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`, cost $0.00 — B00 measured 10.18s, comfortably clearing the
TIMING LAW's >=9s floor with `lead_silence_s: 1.0`); B00/BCRY/BHTF/BOUT
rendered via `remotion_scenes.py` (foreground call exceeded the tool's
120s timeout and was moved to background by the harness automatically —
blocked on it via `TaskOutput` before proceeding, per the COMPLETION LAW's
foreground-render rule: never end a turn on an unawaited render); NB01–NB03
rendered via `render_scenes.py` (both the initial full run and the
two-beat re-render after the chip fix stayed under the foreground
timeout). First `type_check.py` pass: **PASS, 0 FAILs** (the chip
space-collapse defects were caught by Gate V frame pulls, which GATE T's
spacing checks do not cover); re-ran `type_check.py` after the chip fix and
recompile: still **PASS, 0 FAILs**.

Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Result: `skills--claude-liam-internal-comms.mp4`, 7/7 beats filled real (no
slate), 114.8s, 3840×2160 (native 4K — `compile.py`'s 4K LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (both passes; chip fixes caught by Gate V, not GATE T)
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (ffmpeg volumedetect, well
  above the -40 dB floor)
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 114.8s; mp4
  mtime (1788544172) newer than beat_sheet.json mtime (1788544050)
- Gate V (visual): pulled frames every 5s across the full runtime plus
  targeted checks — B00 at t=8.5s/9.8s (the "write"→"format" correction
  fully settled and legible, well inside the clip's 10.2s length), NB01
  (post-fix: all three chips legible, correctly spaced, arrows and
  terracotta underline intact), NB02 (emoji+dates / P/P/P / one read, all
  clean), NB03 (post-fix: all three chips legible, correctly spaced),
  BCRY (carry-out sentence + sparkline read clean), BHTF (correct
  topic/title/@HumanitariansAI handle, paste-ready prompt text legible),
  BOUT (OutroSeries: correct eyebrow "INTERNAL COMMS · @HumanitariansAI",
  correct title restate, crimson underline, no truncation). No blockers
  after the two chip fixes above.
- B00 TIMING LAW: `actual_duration_s` 10.18s narration + 1.0s lead_silence
  = 11.18s total window (>=9s requirement met); rendered clip is 10.2s;
  the "write" → "format" correction lands on screen and stays legible
  through the end of the clip.

**Playlist note:** SUBJECT.json's `family` is `"skills"`, which does not
literally prefix-match any key in `playlists.json` (the closest keys,
`"claude-skills"`/`"claude-agent-skills"`, are longer strings than
`"skills"` itself, so a strict `family.startswith(key)` check — the
mechanism confirmed by the `claude-plugins-official` siblings — finds no
hit). This whole batch of `skills--claude-liam-<name>` reels is a redo of
Anthropic's own Claude Agent Skills reference docs (pdf, docx, xlsx, pptx,
brand-guidelines, canvas-design, internal-comms, …) — content that is
unambiguously about Claude Skills, so I matched on topic rather than
falling through to the `hai-simple` self-match ("Claude Basics") or
`_default`: **Extending Claude — Skills, Plugins & Connectors**, the map's
dedicated playlist for exactly this subject matter. Direct code link per
DELIVERY CONTRACT format included in the description.

Metadata file written: `skills--claude-liam-internal-comms.md` (channel
@HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors**).

**Status: review cut DONE.** Passed every Phase-3 gate.
