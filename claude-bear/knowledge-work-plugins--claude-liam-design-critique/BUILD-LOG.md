# BUILD-LOG — knowledge-work-plugins--claude-liam-design-critique

## 2026-09-03 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-design-critique/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `design-critique`
Skill — structured design feedback on usability, hierarchy, and
consistency — already fully built; no SCRIPT.md existed on the source, so
source `beats[*].narration_text` served as the locked script). Built
entirely fresh this invocation — only SUBJECT.json existed on pickup.
Followed the `knowledge-work-plugins--claude-liam-brand-review` sibling as
the structural precedent: identical source shape (7 beats: composer-ask
cold open + anatomy/pipeline + design-tell + verdict + your-turn + outro),
identical redo pattern (BrutalistHesitantWriter cold open, merged
design-tell+verdict beat, OutroSeries close), same Manim chip-row
scenes.py template copied verbatim for the GRAPHIC beats.

Question, facts, and full body argument carried over unchanged: a skill is
a folder Claude reads before it works (this one, design-critique, is a
single SKILL.md file, about three kilobytes — the source's own file
listing gave the exact size); the SKILL.md is a plain-language instruction
set with no hidden logic underneath it, and Claude reads the file then
acts on what it says; the skill's job, quoted verbatim from its own
description field (only fully intact at source B00 — see truncation note
below): get structured design feedback on usability, hierarchy, and
consistency, triggering on "review this design", "critique this mockup",
"what do you think of this screen?", or sharing a Figma link or screenshot
for feedback at any stage from exploration to final polish; once
triggered, Claude executes the Steps section in order, linear, no
branching unless a step says so; and the concrete distinction that follows
from being a feedback tool rather than a redesign tool — same mockup, same
feedback, every time, but the skill never redesigns the screen itself, and
anything outside usability, hierarchy, and consistency is outside what it
checks.

B00 replaced the source's `ClaudeComposerAsk` typed-ask cold open with
`BrutalistHesitantWriter` (WRITER LAW: "fix" → "critique" — the newcomer's
wrong guess that asking Claude to critique a design means Claude will go
fix or redesign the mockup itself, corrected toward the actual mechanism:
the skill's own job description is to hand back structured feedback, not
to silently rework the screen). Register re-registered Teardown→Plain:
the source's B03 "here is the Teardown moment... what it gets right / what
it bites" framing and BVDT's four-line verdict artifact were merged into a
single NB03 beat and stripped of judgment language, kept as the one fact a
general audience needs and can act on (repeatable feedback / three-checks
limit), per the NO JUDGMENT register check. BVDT's separate bulleted
artifact card was not kept as its own beat, per CARRY-OUT LAW — its facts
live in the single BCRY sentence instead. NB02 additionally folded in the
job-description clause the source had only quoted inline at B00 (now
replaced), since B00 is no longer the composer-ask beat that carried it.
Close re-skinned to @HumanitariansAI (`OutroSeries`).

**Source truncation artifacts, corrected.** Three of the source's four
body beats quoted the skill's own description field mid-sentence and were
cut off by what reads as a template-substitution bug, not a deliberate
edit: B03 ended "...trigger with \"review this d." (missing the rest of
the trigger-phrase list and the exploration-to-polish clause), BVDT ended
"...trigger." (missing the same), and BHTF ended "...trigger." (same
pattern). Source B00 carried the description in full and un-truncated, so
this redo used that intact copy as the canonical wording throughout
NB02/BHTF rather than propagating any of the garbled fragments — the same
fix pattern the brand-review and accessibility-review siblings used for
their own truncations.

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01/B02
anatomy/pipeline + B03 design tell + BVDT verdict + BHTF your-turn + BOUT
outro). This redo kept the same 7-beat shape: B00 carries the wrong-guess
pedagogy per WRITER LAW instead of a dedicated beat; B01→NB01, B02→NB02
kept as one beat each; B03+BVDT compressed into the single NB03; BHTF
kept, with the source's truncated "...trigger." rewritten to the complete
job-description phrase; BOUT kept. Full audit in SCRIPT.md's "Beat-count
note (redo)" section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01–NB03) built on the shared generic "chip row"
Manim template (`scenes.py`/`render_scenes.py`) copied verbatim from the
`knowledge-work-plugins--claude-liam-brand-review` sibling, adapted with
design-critique-specific labels and single-hyphenated chip tokens
("plain-text", "one-file", "trigger-match", "steps-in-order",
"same-feedback", "every-time").

**B00 TIMING LAW.** Text: "How do I get Claude / to fix my design /
mockup?" (49 chars, 3 lines) — under the family's established-safe 60-char
config — rendered at the same known-good parameters (charMs=42,
mistakeRate=4%, hesitateWithin=2%, hesitateBetween=8%, jitter=26,
lead_silence_s=0.8). Narration measured 12.16s (≥8s floor, comfortably).
Verified by frame pull: "fix" is typed and sits doomed in terracotta at
t≈2.6–3.2s, struck and replaced by t≈4.5s, and the corrected question "How
do I get Claude to critique my design mockup?" is fully settled and
legible from t≈4.5s through the clip's last frame at t≈9.5s+ (actual
duration 12.17s, well past the ≥8s requirement).

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`, one pass, no re-generation needed); NB01–NB03 rendered via
`render_scenes.py` (foreground, one pass, no re-render needed on the
initial pass); B00/BCRY/BHTF/BOUT rendered via `remotion_scenes.py`
(foreground — the direct call exceeded the tool's 120s interactive
timeout and was moved to background by the harness automatically, not by
choice; waited on it via TaskOutput to completion (exit 0) before
proceeding, per the COMPLETION LAW's foreground-render rule — all 4
REMOTION beats confirmed present via ffprobe/frame pull before compiling).
Compiled once, hit GATE T FAIL (2 defects), fixed, recompiled once more:

```
python3 runtime/scripts/compile.py <REEL_DIR>
```

**Two real GRAPHIC/REMOTION-beat defects caught by GATE T's automated
scan.** First `type_check.py` pass was **FAIL, 2 defects**:

1. NB03's third chip, "three-checks-only" (18 chars, bold+accented),
   scaled down far enough under the chip's width constraint to produce a
   17px text run — under the 20px §8.1 floor at 1080p logical. Root-caused
   to the label being longer than the family's other passing accent chips
   ("spec-only" at 9 chars, "one-file" at 8). Fixed by reusing the
   brand-review sibling's own "spec-only" token (semantically identical —
   both mean "only checks what's in the defined scope") in place of the
   longer coinage, re-rendering NB03 alone; re-verified directly via frame
   pull (chip now reads clean, bold, fully legible) before recompiling.
2. BOUT's eyebrow line, "DESIGN CRITIQUE · @HumanitariansAI" (OutroSeries,
   italic tracked-caps), produced a text run measuring 37px — under the
   41px §8.1 floor at 4K — matching the exact defect class the
   accessibility-review sibling hit with its own longer eyebrow
   ("ACCESSIBILITY REVIEW · @HumanitariansAI"). Fixed the same way:
   shortened the eyebrow to "CRITIQUE · @HumanitariansAI" (dropping the
   redundant "DESIGN" — the outro's own title line, "Feedback, Not a
   Redesign.", already carries the concept) and re-rendered BOUT alone
   (`remotion_scenes.py --only BOUT --force`); re-verified visually via
   frame pull that the shorter eyebrow reads clean at 4K.

Re-ran `type_check.py` on the full reel post-recompile: **PASS, 0 FAILs.**

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: FAIL→PASS, 0 FAILs after the NB03 chip + BOUT eyebrow fixes above
- GATE AUDIO: PASS — mean_volume **-24.1 dB** (ffmpeg volumedetect), max -2.9 dB
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 99.78s; mp4
  mtime (1788460496) newer than beat_sheet.json mtime (1788460438)
- Gate V (visual): pulled frames across the full runtime (t=0.5, 6, 16, 25,
  34, 45, 55, 65, 75, 85, 92, 96, 99) plus targeted checks of B00 (t≈2.6s
  "fix" doomed in terracotta, t≈4.5s struck and replaced by "critique",
  full corrected question settled and legible through the clip's end),
  NB01–NB03 (all chips legible post-fix, correctly spaced, no
  collapsed-space defect), BCRY (carry-out sentence + sparkline read
  clean), BHTF (correct topic/title/@HumanitariansAI handle, full
  paste-ready prompt legible), and BOUT (post-fix eyebrow reads clean,
  correct title restate, crimson underline, clean fade to end, no
  truncation). No blockers remaining.
- B00 TIMING LAW: `actual_duration_s` 12.17s (≥8s requirement met); the
  "fix" → "critique" correction lands on screen by t≈4.5s and the full
  corrected question stays legible for the remainder of the clip.

Metadata file written: `knowledge-work-plugins--claude-liam-design-critique.md`
(channel @HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors**). Per `playlists.json`, SUBJECT.json's family
(`knowledge-work-plugins`) is an exact key in the map, resolving directly
to "Extending Claude — Skills, Plugins & Connectors" — consistent with the
`brand-review` and `accessibility-review` siblings built in the same
family. Direct code link per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.
