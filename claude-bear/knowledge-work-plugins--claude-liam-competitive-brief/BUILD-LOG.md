# BUILD-LOG — knowledge-work-plugins--claude-liam-competitive-brief

## 2026-09-03 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-competitive-brief/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `competitive-brief`
marketing Skill: research competitors and generate a positioning and
messaging comparison with content gaps, opportunities, and threats — used
for sales battlecards, finding unclaimed positioning/messaging angles, or
assessing the impact of a competitor's move; already fully built — no
SCRIPT.md; source `beats[*].narration_text` served as the locked script,
same pattern as the `claude-plugins-official--claude-liam-agent-development`
precedent used as the structural template here). Built entirely fresh this
invocation — only SUBJECT.json existed on pickup.

Question, facts, and full body argument carried over unchanged: a Skill is
a folder Claude reads before it works; this one is competitive-brief;
SKILL.md is the full plain-language instruction set (no hidden logic); the
pipeline lives in a Steps section, executed linearly with no branching
unless a step says otherwise; the skill's one job is researching
competitors and generating a positioning/messaging comparison covering
content gaps, opportunities, and threats; and whatever isn't in those
steps, the skill doesn't do. B00 replaced the source's `ClaudeComposerAsk`
typed-ask cold open with `BrutalistHesitantWriter` (WRITER LAW: "algorithm"
→ "checklist" — the newcomer's wrong guess that Claude runs some hidden,
proprietary research algorithm, corrected toward the actual mechanism: a
plain-language checklist file executed step by step). Register
re-registered Teardown→Plain: source B03's "what it gets right / what it
bites" verdict language was compressed to a plain mechanism-and-boundary
statement (NB03) — the underlying facts (repeatable results, nothing
outside the spec) were kept, only the verdict framing was dropped. BVDT's
verdict facts were merged into the single BCRY carry-out sentence rather
than kept as a separate bulleted artifact card, per CARRY-OUT LAW. Close
re-skinned to @HumanitariansAI (`OutroSeries`).

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01/B02
anatomy/pipeline + B03 design tell + BVDT verdict + BHTF your-turn + BOUT
outro). This redo kept the same 7-beat shape: B00 carries the wrong-guess
pedagogy per WRITER LAW instead of a dedicated beat; B01→NB01, B02→NB02
kept as one beat each; B03 recast into NB03 (mechanism + boundary, no
verdict language); BVDT folded into BCRY; BHTF kept, with the source's
prompt (research competitors, generate the comparison, then ask Claude to
explain its plan first) carried over essentially unchanged; BOUT kept.
Full audit in SCRIPT.md's "Beat-count note (redo)" section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00's mandated cold-open swap. NB01–NB03 render as
GRAPHIC (Manim, the generic "chip row" template shared verbatim with the
`claude-plugins-official--claude-liam-agent-development` sibling) rather
than the source's Remotion anatomy cards.

**B00 TIMING LAW — timing risk pre-empted, not re-discovered.** Copied the
render parameters (charMs=42, jitter=26, mistakeRate=4, hesitateWithin=2,
hesitateBetween=8) directly from the already-debugged fix on the
`claude-plugins-official--claude-liam-agent-development` sibling, since
this reel's B00 text ("Does Claude have / a special algorithm / for
competitor / research?", 61 chars) is nearly identical in length to that
sibling's proven-safe fixed text (60 chars) — the sibling's own first
attempt at a similar length with slower/higher-hesitation settings had run
out of its window. Using the proven-safe parameters from the start avoided
reproducing that failure: first render came in at 10.1s (audio measured
10.09s), comfortably clearing the ≥8s TIMING LAW floor. Frame-verified at
t=2.0s ("Does Claude have" settled, cursor blinking before the trigger
word), t=4.5s ("algorit" mid-typed in terracotta, correction in progress),
and t=9.5s (full corrected question "Does Claude have a special checklist
for competitor research?" fully settled and legible, holding to the end of
the 10.1s clip).

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`, cost $0.00, clean first pass: B00 10.09s, NB01 15.55s, NB02
9.75s, NB03 14.27s, BCRY 10.26s, BHTF 18.84s, BOUT 3.67s). `render_scenes.py`
(Manim, foreground) clean first pass, all 3 beats ok. `remotion_scenes.py`
(foreground) exceeded the 120s tool timeout and was moved to background by
the harness automatically; blocked on it via `TaskOutput(block=true)` per
the COMPLETION LAW foreground-render rule before proceeding — confirmed
exit 0, all 4 beats ok (B00/BCRY/BHTF/BOUT). `type_check.py` (GATE T)
PASS, 0 FAILs, first pass (all beats §8.10 SKIP — no wordy-card triggers).

First `compile.py` pass: 7/7 beats real (no slate), native 4K (3840×2160)
via the 4K LAW, GATE AUDIO PASS (mean_volume -24.1 dB, max -2.8 dB).

**Gate V caught 1 real defect on the frame sweep, not caught by GATE T:**
NB02's first chip label, "Steps section," rendered as a visually merged
"Stepssection" with no perceptible space — confirmed on a fully-settled
frame (all three chips visible, animation complete), not a fade-in
artifact; the sibling chips on the same beat ("in order", "no branching")
rendered with normal spacing, isolating the defect to that specific
two-word boundary (likely a font-kerning interaction at the "s"/"s"
juncture in EB Garamond via Manim's Pango layout). Fixed at the root by
rewording the label to "the Steps" (same meaning, no adjacent-s boundary);
synced `beat_sheet.json`'s `graphic.production_viz.chips` for NB02 directly
(not via a full `build_beat_sheet.py` re-run, which would have discarded
the already-measured audio durations and render stamps), re-rendered NB02
only, and recompiled with `--force`. Reverified by frame pull: "the Steps"
renders with a clean, legible space, matching its sibling chips.

Full Gate V frame sweep (14 frames every 6s across the 83.4s runtime, plus
the three targeted B00 timing pulls above): all 7 beats legible, safe
inset, single accent per beat, no text overlap; BCRY's carry-out sentence
and sparkline ("A checklist, not an algorithm.") read clean; BHTF shows the
correct topic/title/@HumanitariansAI folder label and a legible paste-ready
prompt; BOUT (`OutroSeries`) shows the correct eyebrow ("COMPETITIVE BRIEF
· @HumanitariansAI"), correct title restate, crimson underline, no
truncation. Zero blockers after the NB02 fix.

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs
- GATE AUDIO: PASS — mean_volume **-24.1 dB** (independently re-verified via
  a standalone ffmpeg volumedetect pass), max -2.8 dB
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 83.4s; mp4
  mtime (1788412299) newer than beat_sheet.json mtime (1788412216)
- Gate V (visual): see frame sweep above — 1 defect found and fixed (NB02
  chip spacing), zero blockers remaining
- B00 TIMING LAW: `actual_duration_s` 10.1s (≥8s requirement met); the
  "algorithm" → "checklist" correction lands on screen by t≈4.5-9.5s and
  the full corrected question stays legible for the remainder of the clip.

Metadata file written: `knowledge-work-plugins--claude-liam-competitive-brief.md`
(channel @HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors**). Per `playlists.json`, SUBJECT.json's family
(`knowledge-work-plugins`) matches the map's `knowledge-work-plugins` key
directly (no fallback needed), consistent with every other
`knowledge-work-plugins--*` sibling in this log. Direct code link per
DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.

## 2026-09-03 — Phase 4, DELIVERED

Master was already born native 3840×2160 (compile.py's 4K LAW), so copied
directly to `knowledge-work-plugins--claude-liam-competitive-brief-4k.mp4`
rather than re-rendering at a higher resolution.

```
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Staged `DELIVERY/knowledge-work-plugins--claude-liam-competitive-brief/`
(4K master + description) for the Drive sync. Committed to
`claude-bear/knowledge-work-plugins--claude-liam-competitive-brief/`
(README.md = description, beat_sheet.json, SCRIPT.md, SUBJECT.json,
CARRY-OUT.md, QUESTION.md, BUILD-LOG.md — no mp3/mp4) as commit
`86e250c0`, pushed clean (no rebase conflicts).

**Status: DELIVERED.**
