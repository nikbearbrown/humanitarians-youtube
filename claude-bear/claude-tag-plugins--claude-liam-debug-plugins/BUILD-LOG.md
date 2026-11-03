# BUILD-LOG — claude-tag-plugins--claude-liam-debug-plugins

## 2026-08-31 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-tag-plugins/youtube/claude-liam-debug-plugins/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Claude Code `debug-plugins`
Skill — a six-step diagnostic ladder for plugin/skill loading run from
inside the session container — already fully built, no SCRIPT.md; source
`beats[*].narration_text` served as the locked script). Built entirely
fresh this invocation — only SUBJECT.json existed on pickup.

Question, facts, and full body argument carried over unchanged: a plugin
diagnostic collects three pieces of evidence before explaining anything —
what arrived in the mount (plugin zips, standalone skill folders, or
pre-seeded marketplace mounts), what flags Claude Code was actually
launched with, and what the startup log recorded; then it walks a
five-cause failure ladder (zip absent, zip present but no matching launch
flag, extraction failure, malformed manifest — often just a stray capital
letter or space in the name — or a broken SKILL.md frontmatter); a session
reads its configuration once, at start, so a setting flipped mid-chat
needs a fresh conversation, not a refresh; and some of Claude Code's
startup errors go to a channel (stdout) this diagnostic can't see inside
the container, so a clean log is not proof nothing went wrong. B00
replaced the source's `ClaudeComposerAsk` typed-ask cold open with
`BrutalistHesitantWriter` (WRITER LAW: "broken" → "stale" — the newcomer's
wrong guess that a missing plugin means broken configuration, corrected
toward the actual mechanism: it's usually a stale, once-read session, not
a broken config).

Register re-registered Teardown→Plain: the source's B05 "gets it right /
where it bites" analysis (the security note on untrusted log content, the
unzip-via-Bash-vs-read-only tension, no report template, no missing-log
fallback, seed-mounts uninspectable) was dropped as assuming a technical,
Claude-Code-internals audience simple/hai-simple doesn't target, not as a
verdict on the skill's quality — the session-snapshot rule and the stdout
gap were kept and reframed as NB03's BOTH-DIRECTIONS beat (a caught error
isn't proof of total failure; a clean log isn't proof of none). BVDT's
verdict facts were merged into the single BCRY carry-out sentence rather
than kept as a separate bulleted artifact card, per CARRY-OUT LAW. Close
re-skinned to @HumanitariansAI (`OutroSeries`).

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01/B02
anatomy/design + B05 teardown analysis + BVDT verdict + BHTF your-turn +
BOUT outro). This redo kept the same 7-beat shape: B00 carries the
wrong-guess pedagogy per WRITER LAW instead of a dedicated beat; B01's
three-step evidence order became NB01; B02's failure ladder and B05's
teardown analysis merged into NB02 (five failure causes); B02's
session-snapshot rule and stdout gap became NB03 (both-directions); BVDT
folded into BCRY; BHTF kept, trimmed from the source's five things-to-watch
to three so it stays paste-ready and runnable without a live
Claude-Code-internals audit; BOUT kept. Full audit in SCRIPT.md's
"Beat-count note (redo)" section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`DebugPluginsAnatomy` / `DebugPluginsDesign` / `DebugPluginsTell` /
`ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01–NB03) built on the shared generic "chip row"
Manim template (`scenes.py`/`render_scenes.py`) copied verbatim from the
`claude-plugins-official--claude-liam-agent-development` sibling, adapted
with debug-plugins-specific labels.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`); B00 measured 10.43s with `lead_silence_s: 0.8`, clearing the
WRITER LAW's ≥9s window on the first attempt (no re-render needed, unlike
the agent-development sibling's B00 timing defect). B00/BCRY/BHTF/BOUT
rendered via `remotion_scenes.py` (the harness moved the run to background
after its 120s foreground timeout; blocked on it via `TaskOutput` before
proceeding, per the COMPLETION LAW's foreground-render rule — never
treating a backgrounded render as "handled" without waiting on it);
NB01–NB03 rendered via `render_scenes.py` in the foreground. Verified B00
by frame pull: "broken" sits doomed in terracotta at t≈4.0s, the corrected
"My plugin isn't showing up. Is my config stale?" is settled and legible
by t≈5.5s, and holds through the end of the 10.4s clip.

First `type_check.py` pass was **FAIL, 3 defects**, fixed at the root, not
by loosening the validator:

- **NB01 min-size** and **NB03 min-size** (smallest text run 19px / 16px,
  under the 20px floor) — diagnosed as the §8.1 checker measuring rendered
  glyph-ink bounding-box height, not declared font size: chip labels
  composed entirely of x-height/ascender letters with no descender
  (g/j/p/q/y) measure a shorter ink bbox than labels containing one, at
  the *same* font-size tier — NB01's original "what launched" chips (12–14
  chars, fs=26 tier, no descender) and NB03's "read once, at start" /
  "some errors uncaptured" (drops to the fs=22 tier at 19–22 chars, then
  scales down further against the 3.2-unit chip width, with no descender
  to keep the ink bbox tall) both fell under the floor. Fixed by shortening
  NB01's chips to single words ("arrived" / "launched" / "logged" — the
  existing "logged" already carries a descender) and replacing NB03's
  chips with shorter labels that include a descender letter ("config
  once" / "gaps possible") — confirmed against NB01/NB02's already-passing
  siblings, which share the identical chip_w/chip_h/font-tier logic and
  differ only in label content.
- **NB02 bbox-overlap** (two text-run bboxes overlapping 22%, coordinates
  in the frame's top ~10%, matching the title row, not the chip row) —
  diagnosed as the original 32-character title ("FIVE WAYS A PLUGIN GOES
  MISSING") being long enough to sit near the shared-template's
  `set_width(12.6)` scale-down boundary, unlike every passing sibling
  title (16–27 chars). Fixed by shortening to "FIVE FAILURE CAUSES" (19
  chars, in line with sibling title lengths) — did not touch the shared
  `render_chip_row`/`_chip` mechanism, which is copied verbatim and known
  to pass elsewhere.

All three fixes applied to `scenes.py`, `build_beat_sheet.py` (kept in
sync for reproducibility), and `beat_sheet.json`'s
`graphic.production_viz` fields directly (not via a full
`build_beat_sheet.py` re-run, which would have discarded the
already-measured audio durations and render stamps), per COMPLETION LAW.
Only the affected beats (NB01, NB02's label/caption, NB03) were
re-rendered; B00/BCRY/BHTF/BOUT were untouched. `type_check.py` went
3→2→1→**PASS, 0 FAILs** across three iterative fix-and-rerun cycles.

Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Result: `claude-tag-plugins--claude-liam-debug-plugins.mp4`, 7/7 beats
filled real (no slate), 99.6s, 3840×2160 (native 4K — `compile.py`'s 4K
LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (see 3 defects + fixes above)
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (ffmpeg volumedetect,
  independently re-verified), max -2.9 dB
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 99.6s; mp4
  mtime (1788201138) newer than beat_sheet.json mtime (1788200996)
- Gate V (visual): pulled frames every ~5-10s across the full runtime plus
  targeted checks of B00 (t≈4.0s "broken" doomed in terracotta, t≈5.5s
  settled+correct, held to the end of the 10.4s clip), NB01-NB03 (all
  chips legible and parallel-sized post-fix), BCRY (carry-out sentence +
  sparkline read clean), BHTF (correct topic/title/@HumanitariansAI
  handle, paste-ready prompt text legible), and BOUT (OutroSeries: correct
  eyebrow "DEBUG PLUGINS · @HumanitariansAI", correct title restate
  "Stale, Not Broken.", crimson underline, no truncation). No blockers.
- B00 TIMING LAW: `actual_duration_s` 10.43s (≥9s requirement met, no
  re-render needed); "broken" → "stale" correction lands on screen by
  t≈5.5s and the full corrected question stays legible for the remainder
  of the clip.

Metadata file written: `claude-tag-plugins--claude-liam-debug-plugins.md`
(channel @HumanitariansAI, **Playlist: Claude Basics**). Per
`playlists.json`, SUBJECT.json's family (`claude-tag-plugins`) does not
match any listed prefix via `str.startswith` (it does not start with
`claude-plugins`, `claude-code`, or any other key), so resolution falls
through to the `hai-simple` skill-key entry, which maps to "Claude
Basics" — confirmed consistent with every other built
`claude-tag-plugins--*` sibling in this family (asana-api, bigquery-api,
config-guide, confluence-api, datadog-api all use "Claude Basics"). Direct
code link per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.
