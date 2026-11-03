# BUILD-LOG — knowledge-work-plugins--claude-liam-debug

## 2026-09-03 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-debug/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `debug` engineering
Skill, already fully built — no SCRIPT.md; source `beats[*].narration_text`
served as the locked script). Built entirely fresh this invocation — only
SUBJECT.json existed on pickup.

Question, facts, and full body argument carried over unchanged: `debug` is
a folder Claude reads before it acts, containing one SKILL.md; its job is a
structured debugging session run as four ordered steps — reproduce,
isolate, diagnose, fix — never skipped, never reordered; the session starts
on any of a few trigger conditions (an error message or stack trace, "works
in staging but not prod," "broke after the deploy," or behavior that
diverges from expected with no obvious cause); running it twice on the same
problem yields the same four steps in the same order (repeatable); and the
guarantee stops at the edge of those trigger conditions — outside that
list, the skill has nothing to say. B00 replaced the source's
`ClaudeComposerAsk` typed-ask cold open with `BrutalistHesitantWriter`
(WRITER LAW: "fix" → "debug" — the newcomer's wrong guess that asking
Claude to "fix" code and asking it to "debug" are the same one-shot
request, corrected toward the actual mechanism: invoking `debug`
specifically commits Claude to the four-step session before any fix
happens). Register re-registered Teardown→Plain: source B03's "gets it
right / where it bites" list and BVDT's verdict facts were merged into a
single mechanism-and-limit description (NB03), stripped of Teardown
judgment language, per the NO JUDGMENT register check. Close re-skinned to
@HumanitariansAI (`OutroSeries`).

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01
anatomy + B02 pipeline + B03 design tell + BVDT verdict + BHTF your-turn +
BOUT outro). This redo kept the same 7-beat shape: B00 carries the
wrong-guess pedagogy per WRITER LAW instead of a dedicated beat; B01→NB01
kept as anatomy; B02→NB02 re-scoped from the source's generic
"read → execute → return" pipeline description to the debug-specific
trigger conditions the source's own B00/BHTF narration already named — a
more concrete, skill-specific fact than restating the generic pipeline
every skill-teardown episode in this family already covers; B03+BVDT
merged into NB03; BHTF kept, built from the source's own generic handoff
template ("I want to [use case]. Read the debug skill and walk me through
what you will do before you do it.") filled with one of the source's own
listed triggers ("works in staging but not prod") so the prompt is
concrete and paste-ready rather than a fill-in-the-blank; BOUT kept. Full
audit in SCRIPT.md's "Beat-count note (redo)" section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism` /
`ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01–NB03) built on the shared generic "chip row"
Manim template (`scenes.py`/`render_scenes.py`) copied verbatim from the
`claude-plugins-official--claude-liam-agent-development` sibling, adapted
with debug-specific labels.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`); B00/BCRY/BHTF/BOUT rendered via `remotion_scenes.py`
(foreground — the first invocation exceeded the Bash tool's default 120s
timeout and was killed with zero media written; re-ran with the tool's
timeout raised to its 600s max, per the COMPLETION LAW's foreground-render
rule, never treating a killed/backgrounded render as "handled" without a
verified exit); NB01–NB03 rendered via `render_scenes.py`.

First `type_check.py` pass was **FAIL, 2 defects**, fixed at the root:

- **min-size §8.1, NB02 + NB03** — smallest text runs measured 16px/17px,
  under the 20px floor. Root cause: the chip labels were too long
  ("error / stack trace" 20 chars, "diverges, unclear why" 21 chars,
  "same order, every run" 22 chars, "outside the list?" 18 chars), pushing
  the shared `_chip()` renderer's width-fit scale-down past the legibility
  floor even at the mid font-size tier — the same defect class documented
  on the `claude-plugins-official--claude-liam-agent-development` sibling's
  own NB03 fix. Fixed by shortening every over-length label to ≤14 chars
  ("error / stack trace"→"stack trace", "diverges, unclear why"→"unclear
  cause", "same order, every run"→"same order", "outside the list?"→"off
  the list"), landing all chips in the top font-size tier — re-rendered
  NB02/NB03 only (NB01 untouched), and `beat_sheet.json`'s
  `graphic.production_viz.chips` for both beats was synced to the fixed
  wording directly (not via a full sheet regeneration, which would have
  discarded already-measured audio durations and render stamps) before the
  recompile, per COMPLETION LAW.

`type_check.py` went 2→**PASS, 0 FAILs**. Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Result: `knowledge-work-plugins--claude-liam-debug.mp4`, 7/7 beats filled
real (no slate), 86.4s, 3840×2160 (native 4K — `compile.py`'s 4K LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (see 2 defects + fix above)
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (ffmpeg volumedetect), max -3.0 dB
- ffprobe: video 3840×2160 h264, audio present, duration 86.36s; mp4 mtime
  newer than beat_sheet.json mtime
- Gate V (visual): pulled frames every 6s across the full runtime plus
  targeted checks of B00 (t≈4s "fix" doomed in terracotta, last frame
  t≈10.5s settled on the corrected "...to debug this broken code right
  now?"), NB01 (chip "4-step order" legible at full res — a "4-" glyph
  reads as a strikethrough only at thumbnail scale, confirmed clean on
  crop), NB02–NB03 (all chips legible post-fix, arrows/underline/strike
  render correctly), BCRY (carry-out sentence + sparkline "Reproduce
  first. Fix last." read clean), BHTF (correct topic/title/@HumanitariansAI
  handle, paste-ready prompt text legible across its multi-second type-in),
  and BOUT (OutroSeries: eyebrow "DEBUG · @HumanitariansAI", title restate
  "Reproduce First, Fix Last.", crimson underline, no truncation). No
  blockers.
- B00 TIMING LAW: `actual_duration_s` 10.84s (≥8s requirement met); the
  "fix" → "debug" correction is mid-type by t≈4s and the full corrected
  question is settled and legible for the remainder of the clip.

Metadata file written: `knowledge-work-plugins--claude-liam-debug.md`
(channel @HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors**). Per `playlists.json`, SUBJECT.json's family
(`knowledge-work-plugins`) is an exact key in the map, resolving directly to
"Extending Claude — Skills, Plugins & Connectors" — no prefix-matching
ambiguity. Direct code link per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.
