# BUILD-LOG — knowledge-work-plugins--claude-liam-brand-review

## 2026-09-02 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-brand-review/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `brand-review`
Skill — reviewing content against a brand voice, style guide, and
messaging pillars — already fully built; no SCRIPT.md existed on the
source, so source `beats[*].narration_text` served as the locked script).
Built entirely fresh this invocation — only SUBJECT.json existed on
pickup. Followed the `knowledge-work-plugins--claude-liam-accessibility-review`
sibling as the structural precedent: identical source shape (7 beats:
composer-ask cold open + anatomy/pipeline + design-tell + verdict +
your-turn + outro), identical redo pattern (BrutalistHesitantWriter cold
open, merged design-tell+verdict beat, OutroSeries close), same Manim
chip-row scenes.py template copied verbatim for the GRAPHIC beats.

Question, facts, and full body argument carried over unchanged: a skill is
a folder Claude reads before it works (this one, brand-review, is a
single SKILL.md file, about twelve kilobytes — the source's own file
listing gave the exact size); the SKILL.md is a plain-language instruction
set with no hidden logic underneath it, and Claude reads the file then
acts on what it says; the skill's job, quoted verbatim from its own
description field (only fully intact at source B00 — see truncation note
below): review content against your brand voice, style guide, and
messaging pillars, flagging deviations by severity with specific
before/after fixes, triggering on checking a draft before it ships,
auditing copy for voice consistency and terminology, or screening for
unsubstantiated claims, missing disclaimers, and other legal flags; once
triggered, Claude executes the Steps section in order, linear, no
branching unless a step says so; and the concrete distinction that follows
from being a report rather than a rewrite tool — same draft, same flags,
every time, but the skill never rewrites the copy to close what it finds,
and anything outside the style guide and messaging pillars is outside what
it checks.

B00 replaced the source's `ClaudeComposerAsk` typed-ask cold open with
`BrutalistHesitantWriter` (WRITER LAW: "fix" → "review" — the newcomer's
wrong guess that asking Claude to review content for brand voice means
Claude will go fix the copy itself, corrected toward the actual mechanism:
the skill's own job description flags deviations with suggested fixes
shown, it does not silently rewrite the draft). Register re-registered
Teardown→Plain: the source's B03 "here is the Teardown moment... what it
gets right / what it bites" framing and BVDT's four-line verdict artifact
were merged into a single NB03 beat and stripped of judgment language,
kept as the one fact a general audience needs and can act on (repeatable
flags / spec-only limit), per the NO JUDGMENT register check. BVDT's
separate bulleted artifact card was not kept as its own beat, per
CARRY-OUT LAW — its facts live in the single BCRY sentence instead. NB02
additionally folded in the job-description clause the source had only
quoted inline at B00 (now replaced), since B00 is no longer the
composer-ask beat that carried it. Close re-skinned to @HumanitariansAI
(`OutroSeries`).

**Source truncation artifacts, corrected.** Three of the source's four
body beats quoted the skill's own description field mid-sentence and were
cut off by what reads as a template-substitution bug, not a deliberate
edit: B03 ended "...flagging deviations by ." (missing "severity with
specific before/after fixes"), BVDT ended "...messaging pillars, fla"
(missing "gging deviations by severity..."), and BHTF ended "...messaging
pi" (missing "llars"). Source B00 carried the description in full and
un-truncated, so this redo used that intact copy as the canonical
wording throughout NB02/NB03/BCRY/BHTF rather than propagating any of the
three garbled fragments — the same fix pattern the accessibility-review
sibling used for its own BHTF truncation.

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01/B02
anatomy/pipeline + B03 design tell + BVDT verdict + BHTF your-turn + BOUT
outro). This redo kept the same 7-beat shape: B00 carries the wrong-guess
pedagogy per WRITER LAW instead of a dedicated beat; B01→NB01, B02→NB02
kept as one beat each; B03+BVDT compressed into the single NB03; BHTF
kept, with the source's truncated "review content against your brand
voice, style guide, and messaging pi..." rewritten to the complete
job-description phrase; BOUT kept. Full audit in SCRIPT.md's "Beat-count
note (redo)" section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01–NB03) built on the shared generic "chip row"
Manim template (`scenes.py`/`render_scenes.py`) copied verbatim from the
`knowledge-work-plugins--claude-liam-accessibility-review` sibling,
adapted with brand-review-specific labels and single-hyphenated chip
tokens ("plain-text", "one-file", "trigger-match", "steps-in-order",
"same-flags", "every-time", "spec-only") to avoid that sibling's earlier
collapsed-spacing defect. No such defect occurred this build.

**B00 TIMING LAW.** Text: "How do I get Claude / to fix my content / for
brand voice?" (54 chars, 3 lines) — under the family's established-safe
60-char config — rendered at the same known-good parameters (charMs=42,
mistakeRate=4%, hesitateWithin=2%, hesitateBetween=8%, jitter=26,
lead_silence_s=0.8). Narration measured 10.73s + 0.8s lead ≈ 11.5s window
(≥9s floor, comfortably). Verified by frame pull: "fix" sits doomed in
terracotta mid-typing at t≈4.5s, and the corrected question "How do I get
Claude to review my content for brand voice?" is fully settled and
legible by t≈9s, holding through the clip's last frame (actual_duration_s
10.73s, ≥8s requirement met).

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`, one pass, no re-generation needed); NB01–NB03 rendered via
`render_scenes.py` (foreground, one pass, no re-render needed); B00/BCRY/
BHTF/BOUT rendered via `remotion_scenes.py` (foreground, one pass to
completion, all 4 REMOTION beats confirmed present via ffprobe before
compiling, per the COMPLETION LAW's foreground-render rule). Compiled once:

```
python3 runtime/scripts/compile.py <REEL_DIR>
```

Result: `knowledge-work-plugins--claude-liam-brand-review.mp4`, 7/7 beats
filled real (no slate), 103.9s, 3840×2160 (native 4K — `compile.py`'s 4K
LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs on first pass (no BOUT eyebrow overflow this time —
  "BRAND REVIEW · @HumanitariansAI" fit clean at the family's calibrated
  tracking, unlike the accessibility sibling's longer eyebrow which needed
  shortening)
- GATE AUDIO: PASS — mean_volume **-24.2 dB** (ffmpeg volumedetect), max -2.9 dB
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 103.875s; mp4
  mtime (1788368548) newer than beat_sheet.json mtime (1788368451)
- Gate V (visual): pulled frames across the full runtime (t=0.5, 5, 12, 20,
  28, 38, 48, 58, 68, 78, 88, 96, 100, 103) plus targeted checks of B00
  (t≈4.5s "fix" doomed in terracotta, t≈9s settled and correct through the
  clip's end), NB01–NB03 (all chips legible, correctly spaced, no
  collapsed-space defect), BCRY (carry-out sentence + sparkline read
  clean), BHTF (correct topic/title/@HumanitariansAI handle, full
  paste-ready prompt legible), and BOUT (correct eyebrow, title restate,
  crimson underline, clean fade to end, no truncation). No blockers found.
- B00 TIMING LAW: `actual_duration_s` 10.73s (≥8s requirement met); the
  "fix" → "review" correction lands on screen by t≈9s and the full
  corrected question stays legible for the remainder of the clip.

Metadata file written: `knowledge-work-plugins--claude-liam-brand-review.md`
(channel @HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors**). Per `playlists.json`, SUBJECT.json's family
(`knowledge-work-plugins`) is an exact key in the map, resolving directly
to "Extending Claude — Skills, Plugins & Connectors" — consistent with the
`accessibility-review` sibling built in the same family. Direct code link
per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.
