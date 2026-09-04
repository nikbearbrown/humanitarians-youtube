# BUILD-LOG — knowledge-work-plugins--claude-liam-knowledge-synthesis

## 2026-09-04 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-knowledge-synthesis/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `knowledge-synthesis`
enterprise-search skill, already fully built — no SCRIPT.md in the source;
source `beats[*].narration_text` served as the locked script). Built entirely
fresh this invocation — only SUBJECT.json existed on pickup. Source SKILL.md
path (`/Users/bear/.../knowledge-work-plugins/enterprise-search/skills/
knowledge-synthesis/SKILL.md`) is on Bear's other machine and unreachable
here; every fact was taken from the source beat_sheet's own narration_text
and LENS-AUDIT.md/PEDAGOGY.md, per the redo contract (source beat_sheet is
the locked script).

Question, facts, and full body argument carried over unchanged: the skill
combines search results from multiple sources into one coherent,
deduplicated answer with source attribution intact; it scores confidence by
weighing freshness and authority per source; it summarizes large result sets
as part of the same job; execution is a fixed pipeline — read the SKILL.md,
run its steps in order, linear unless a step branches; and the same input
always produces the same output.

**Beat count discipline:** source is 7 beats (B00 composer-ask cold open +
B01 anatomy + B02 pipeline + B03 design tell + BVDT verdict + BHTF your-turn
+ BOUT outro). This redo kept the same 7-beat shape: B00 replaced the
source's `ClaudeComposerAsk` typed-ask cold open with `BrutalistHesitantWriter`
(WRITER LAW) and absorbed the wrong-guess move directly into the on-screen
correction, since the source had no dedicated wrong-guess beat to preserve as
its own slot; B01+B02 (anatomy + pipeline) compressed into NB01; B03 (design
tell) became NB02, with the Teardown's "what it gets right / what it bites"
framing removed — Plain states the mechanism, it does not grade it; BVDT's
determinism fact folded into NB03 alongside the confidence-weighting fact
(the one part of B03's "interesting constraint" not yet covered), and BVDT's
"know the limit" verdict language dropped as Teardown judgment; the same
beat's act label changed `BVDT`→`BCRY` to carry the CARRY-OUT LAW sentence;
BHTF kept, with its prompt rewritten to be genuinely paste-ready (the source
had a grammar artifact, "I want to combines search results..."); BOUT kept,
re-skinned to `OutroSeries` (Humanitarians AI). Full audit in SCRIPT.md's
"Beat-count note (redo)" section.

No source beat was `ai-video-prompt`, pantry, or a human-drop slot — the
source's build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism` /
`ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no substitution
beyond B00's mandated cold-open swap. This redo's body (NB01–NB03) uses
GRAPHIC/Manim instead of the source's REMOTION cards — a legal substitution
(GRAPHIC is one of hai-simple's two permitted beat kinds) chosen to reuse the
proven generic chip-row template already validated on the
`claude-plugins-official--claude-liam-agent-development` sibling in the same
family.

**B00 WRITER LAW — two trigger words, both landed clean, no defect.** Text
"Does Claude\njust pick\nthe best\nsource?" (39 chars) with
`triggerWords: "pick, source"` / `replacementWords: "combine, sources"` — the
wrong guess has two parts (Claude selects ONE thing, not MANY), so both the
verb and the noun correct on screen, settling on "Does Claude just combine
the best sources?" Used the known-good fixed timing preset from the
`claude-plugins-official--claude-liam-agent-development` sibling (42ms/char,
mistakeRate 4%, hesitateWithin 2%, hesitateBetween 8%, jitter 26,
lead_silence_s 1.0) with even shorter text than that sibling's fix for extra
settle-time margin. Audio measured 9.83s (actual_duration_s), comfortably
over the TIMING LAW's >=8s floor. Frame-pulled at t=2.0s ("pick" doomed in
terracotta, mid-hesitation) and t=8.5s (both corrections settled: "Does
Claude just combine the best sources?" fully legible) — first attempt, no
fix needed.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`, one pass, no `--only` reruns needed); NB01–NB03 rendered via
`render_scenes.py` (foreground, generic chip-row Manim template copied
verbatim from the sibling, content swapped); B00/BCRY/BHTF/BOUT rendered via
`remotion_scenes.py` — this run exceeded the tool's 120s timeout and was
moved to background by the harness automatically; blocked on it via
`TaskOutput` before proceeding (COMPLETION LAW's foreground-render rule —
never treated the backgrounded render as "handled" without waiting on its
exit). All 4 Remotion beats rendered clean on the first attempt (exit 0).

`type_check.py` (GATE T): **PASS, 0 FAILs** on the first pass — no fix cycle
needed this build.

Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Result: `knowledge-work-plugins--claude-liam-knowledge-synthesis.mp4`, 7/7
beats filled real (no slate), 96.9s, 3840×2160 (native 4K — `compile.py`'s 4K
LAW, `--force` used because the local dev preview had defaulted low-res
before the forced full-res pass).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs
- GATE AUDIO: PASS — mean_volume **-24.1 dB** (ffmpeg volumedetect), max -2.9 dB
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 96.9s; mp4
  mtime (Sep 4 02:49:51) newer than beat_sheet.json mtime (Sep 4 02:47:31)
- Gate V (visual): pulled frames across the full runtime (t=5, 15, 20, 34,
  40, 52, 58, 66, 80, 88, 95) plus the two targeted B00 frames above. All
  legible, correct topic/title/@HumanitariansAI handle throughout, no text
  overlap or truncation, @HumanitariansAI first-beat overlay present and
  correctly gone by NB01. BHTF's on-screen prompt matches the paste-ready
  text; BOUT's OutroSeries card restates "Combine, Don't Pick." with the
  correct "KNOWLEDGE SYNTHESIS · @HumanitariansAI" eyebrow and crimson
  underline. No blockers.

Metadata file written: `knowledge-work-plugins--claude-liam-knowledge-synthesis.md`
(channel @HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors**). Per `playlists.json`, SUBJECT.json's family
(`knowledge-work-plugins`) is an exact key match in the map, resolving
directly to "Extending Claude — Skills, Plugins & Connectors" (no prefix
fallthrough needed). Direct code link per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate on the first pass —
no defects found or fixed this build.

## 2026-09-04 — Phase 4, DELIVERED

Master was already born native 3840×2160 (compile.py's 4K LAW), so copied
directly to `knowledge-work-plugins--claude-liam-knowledge-synthesis-4k.mp4`
rather than re-rendering at a higher resolution.

```
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Staged `DELIVERY/knowledge-work-plugins--claude-liam-knowledge-synthesis/`
(4K master + description) for the Drive sync. Committed to
`claude-bear/knowledge-work-plugins--claude-liam-knowledge-synthesis/`
(README.md = description, beat_sheet.json, SCRIPT.md, SUBJECT.json,
CARRY-OUT.md, QUESTION.md, BUILD-LOG.md — no mp3/mp4) as commit `ee57500b`,
pushed clean (no rebase conflicts).

**Status: DELIVERED.**
