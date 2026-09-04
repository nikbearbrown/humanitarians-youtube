# BUILD-LOG — knowledge-work-plugins--claude-liam-discover-brand

## 2026-09-03 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-discover-brand/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `discover-brand`
Skill, already fully built — no SCRIPT.md; source `beats[*].narration_text`
served as the locked script). Built entirely fresh this invocation — only
SUBJECT.json existed on pickup.

**Source-material gap, handled honestly:** the source reel's own narration
carries unfilled `>` placeholders in four beats (B00, B03, BVDT, BHTF)
where the specific job discover-brand does was never written into the
original build. The source's `metadata.source_skill` path points at a
machine this build has no access to
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/knowledge-
work-plugins/partner-built/brand-voice/skills/discover-brand/SKILL.md`),
and a workspace-wide search confirmed no copy of that Skill's actual
SKILL.md exists anywhere under `books/`. A sibling reel in the same batch
(`claude-liam-brand-voice-enforcement`, already redone as
`knowledge-work-plugins--claude-liam-brand-voice-enforcement`) hit the
identical gap for its own Skill and supplied the template this build
followed directly: script structure, `scenes.py`/`render_scenes.py` Manim
chip-row template, and metadata shape.

Because `discover-brand` and `brand-voice-enforcement` are sibling skills
in the same `brand-voice` plugin, and the enforcement skill's confirmed job
(from its own already-built reel) is "check a draft against whatever a
spec lists," this build inferred discover-brand's complementary,
name-implied job — reading existing material to derive that spec in the
first place — and stated it as a single, explicitly flagged inference
(NB03's "one flag"), never as confirmed fact. No specific brand, word
list, or output format is invented anywhere in the reel; see the `.md`'s
"Deliberately not claimed" section and SCRIPT.md's source-material note
and One-flag audit.

Question, facts, and body argument carried over: a skill is a folder
Claude reads before it works; the SKILL.md holds the full instruction set
in plain language with no hidden logic; the Steps section runs linearly,
no branching unless a step says otherwise; same input produces same
output every run; the limit is exactly what it was given. B00 replaced the
source's `ClaudeComposerAsk` typed-ask cold open with
`BrutalistHesitantWriter` (WRITER LAW: "know" → "read" — the newcomer's
wrong guess that Claude already knows a brand's voice from training,
corrected toward the actual mechanism: it reads material it's given).
Register re-registered Teardown→Plain: the source's B03 "gets it right /
where it bites" framing was redistributed as a plain, flagged mechanism
description across NB03 (what gets read) and BCRY (the limit), per the NO
JUDGMENT register check. BVDT's verdict facts were merged into the single
BCRY carry-out sentence rather than kept as a separate bulleted artifact
card, per CARRY-OUT LAW. Close re-skinned to @HumanitariansAI
(`OutroSeries`).

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01/B02
anatomy/pipeline + B03 design tell + BVDT verdict + BHTF your-turn + BOUT
outro). This redo kept the same 7-beat shape: B00 carries the wrong-guess
pedagogy per WRITER LAW instead of a dedicated beat; B01→NB01, B02→NB02
kept as one beat each; B03 compressed into NB03; BVDT folded into BCRY;
BHTF kept — but since the source's own your-turn prompt was itself an
unfilled `>` placeholder ("I want to >. Read the discover-brand skill..."),
rather than inventing a call to a specific Anthropic skill a general
viewer likely doesn't have installed, this redo writes a concrete,
paste-ready prompt that exercises the identical mechanism (read real
material, extract the patterns, write them down) using materials any
viewer already has; BOUT kept. Full audit in SCRIPT.md's "Beat-count note
(redo)" section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01–NB03) built on the shared generic "chip row"
Manim template (`scenes.py`/`render_scenes.py`) copied from the
`knowledge-work-plugins--claude-liam-brand-voice-enforcement` sibling,
adapted with discover-brand-specific labels.

**B00 TIMING LAW:** text kept short (3 lines, 33 characters — "Does
Claude\nalready know\nmy brand's voice?") at a moderate charMs (42),
applying the fix pattern already documented on the brand-voice-enforcement
sibling proactively rather than discovering a timing failure by a failed
first render. Kokoro narration measured 8.70s; the rendered clip is 8.7s,
clearing the WRITER LAW's stated `media/B00.mp4 >= 8s` verification floor.
Frame-pulled at t=1.3s/1.6s/3.0s/8.0s: "know" sits doomed in terracotta at
1.6s; by 3.0s it has corrected to "read"; the full corrected question
"Does Claude already read my brand's voice?" is settled and legible and
holds through the end of the 8.7s clip. `lead_silence_s: 1.0` is set as
documented design intent, consistent with the sibling's finding that this
field is not mechanically applied by `remotion_scenes.py` in this toolkit
version.

**Font-kerning defect found and fixed (new finding, not seen on the
sibling):** GATE T first failed on NB02 — a text run measured 19px against
the 20px (1.9%-of-frame-height) floor. Root cause was the long caption
"linear — no branching unless a step says so" (46 characters) triggering
the chip-row renderer's `set_width(12.5)` clamp, which scaled the whole
caption down below the floor. Shortened to "linear. No branching." and
re-rendered — GATE T still failed, on the same beat, for a different
reason surfaced by a manual Gate-V frame pull: the accented chip label
"write the spec" was wide enough to trigger the *chip's* uniform
width/height scale-down, which also pushed it under the floor. Shortened
to "write spec" and GATE T passed.

A second, more interesting defect surfaced only by visually reading the
compiled frames (GATE T's automated check did not catch it): the NB03
accented chip "your writing" rendered as "yourwriting" — the space
visually collapsed, in bold EB Garamond, at this size. Isolated the cause
with a standalone Manim test scene rendering multiple two-word bold
phrases: **any word ending in "r" immediately before a space collapses
that space in this font/weight combination** ("for you", "over here", "our
writing" all reproduced the defect; "run test", "read the file", "my
writing", "raw writing" did not — the space survives when the preceding
word does not end in "r"). Fixed by relabeling the chip "my writing"
(same meaning, no trailing-"r" word before the space) and re-rendered;
confirmed clean on a frame pull. This is a real, reproducible font-hinting
quirk worth remembering for any future chip label in this Manim template:
avoid ending a word in "r" right before a space in a bold accented chip.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`, one pass, no retries needed); NB01–NB03 rendered via
`render_scenes.py` (Manim; NB01/NB03 succeeded first pass, NB02 required
two content fixes per above before passing GATE T); B00/BCRY/BHTF/BOUT
rendered via `remotion_scenes.py` (all 4 beats `ok` on the first pass, run
in the foreground, completed well inside the tool's timeout).
`type_check.py`: **GATE T: FAIL → FAIL → PASS** (two content fixes on
NB02/NB03 as detailed above; 0 FAILs on the third pass).

Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Result: `knowledge-work-plugins--claude-liam-discover-brand.mp4`, 7/7
beats filled real (no slate), 82.2s, 3840×2160 (native 4K —
`compile.py`'s 4K LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (after the two content fixes above)
- GATE AUDIO (compile.py): PASS — mean_volume **-24.2 dB** (ffmpeg
  volumedetect), max -2.9 dB
- Independent ffprobe/ffmpeg re-verification (COMPLETION LAW): video
  3840×2160 h264, audio aac present, duration 82.20s; mp4 mtime
  (1788469976) newer than beat_sheet.json mtime (1788469832); mean_volume
  -24.2 dB, well above the -40 dB floor
- Gate V (visual): pulled frames every 5s across the full 82.2s runtime,
  plus targeted frame pulls at t=1.3/1.6/3.0/8.0s for B00 (confirmed "know"
  doomed in terracotta at 1.6s, corrected to "read" by 3.0s, final question
  settled and held to the 8.7s end) and at t=5s into the re-rendered NB03
  (confirmed "my writing" now spaces correctly, no glyph fusion). NB01/NB02
  chips legible and parallel-sized, one accent per beat. BCRY (quote +
  sparkline "Read the file. Not the training." read clean). BHTF (correct
  topic/title/@HumanitariansAI handle, paste-ready prompt text legible).
  BOUT (correct eyebrow "DISCOVER-BRAND · @HumanitariansAI", correct title
  restate, crimson underline, no overlap/truncation). No blockers.

Metadata file written:
`knowledge-work-plugins--claude-liam-discover-brand.md` (channel
@HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors**). Per `playlists.json`, SUBJECT.json's family
(`knowledge-work-plugins`) is an exact key match in the map, resolving
directly to "Extending Claude — Skills, Plugins & Connectors" (no fallback
needed). Direct code link per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.
