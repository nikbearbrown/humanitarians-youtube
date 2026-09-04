# BUILD-LOG — knowledge-work-plugins--claude-liam-accessibility-review

## 2026-09-02 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-accessibility-review/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `accessibility-review`
Skill — a WCAG 2.1 AA accessibility audit for a design or page — already
fully built; no SCRIPT.md existed on the source, so source
`beats[*].narration_text` served as the locked script). Built entirely
fresh this invocation — only SUBJECT.json existed on pickup. Followed the
`claude-plugins-official--claude-liam-skill-development` sibling as the
structural precedent: same source shape (7 beats: composer-ask cold open +
anatomy/pipeline + design-tell + verdict + your-turn + outro), same redo
pattern (BrutalistHesitantWriter cold open, merged design-tell+verdict
beat, OutroSeries close), same Manim chip-row scenes.py template copied
verbatim for the GRAPHIC beats.

Question, facts, and full body argument carried over unchanged: a skill is
a folder Claude reads before it works (this one, accessibility-review, is
a single SKILL.md file, about four kilobytes — no references folder,
unlike the skill-development sibling); the SKILL.md is a plain-language
instruction set with no hidden logic underneath it, and Claude reads the
file then acts on what it says; the skill's job, quoted from its own
description field: run a WCAG 2.1 AA accessibility audit on a design or
page, triggering on "audit accessibility," "check a11y," "is this
accessible?," or before handoff work touching color contrast, keyboard
navigation, touch target size, or screen reader behavior; once triggered,
Claude executes the Steps section in order, linear, no branching unless a
step says so; and the concrete distinction that follows from being an
audit rather than a repair tool — same design, same audit result, every
time, but the skill never rewrites the design to fix what it finds, and
anything outside WCAG 2.1 AA is outside what it checks.

B00 replaced the source's `ClaudeComposerAsk` typed-ask cold open with
`BrutalistHesitantWriter` (WRITER LAW: "fix" → "review" — the newcomer's
wrong guess that asking Claude to review a design for accessibility means
Claude will go fix the problems it finds, corrected toward the actual
mechanism: the skill's own job description is an audit, not a repair).
Register re-registered Teardown→Plain: the source's B03 "here is the
Teardown moment... what it gets right / what it bites" framing and BVDT's
four-line verdict artifact were merged into a single NB03 beat and
stripped of judgment language, kept as the one fact a general audience
needs and can act on (repeatable audit / standard-only limit), per the NO
JUDGMENT register check. BVDT's separate bulleted artifact card was not
kept as its own beat, per CARRY-OUT LAW — its facts live in the single
BCRY sentence instead. NB02 additionally folded in the trigger-phrase
clause the source had only quoted inline at B00 (now replaced), since B00
is no longer the composer-ask beat that carried it. Close re-skinned to
@HumanitariansAI (`OutroSeries`).

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01/B02
anatomy/pipeline + B03 design tell + BVDT verdict + BHTF your-turn + BOUT
outro). This redo kept the same 7-beat shape: B00 carries the wrong-guess
pedagogy per WRITER LAW instead of a dedicated beat; B01→NB01, B02→NB02
kept as one beat each; B03+BVDT compressed into the single NB03; BHTF
kept, with the source's garbled truncation artifact ("I want to run a
wcag 2.1 aa accessibility audit on a design or page. trigger with \"audit
a…") rewritten to the actual trigger phrase the skill's own description
uses ("I want to audit a design for accessibility"), since the source
text was a template-substitution artifact cut off mid-sentence, not a
deliberately authored prompt; BOUT kept. Full audit in SCRIPT.md's
"Beat-count note (redo)" section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01–NB03) built on the shared generic "chip row"
Manim template (`scenes.py`/`render_scenes.py`) copied verbatim from the
`claude-plugins-official--claude-liam-skill-development` sibling, adapted
with accessibility-review-specific labels. Learned from that sibling's own
BUILD-LOG note (a prior "words collapsed together" bold-chip defect) and
used single hyphenated tokens for every accented/multi-word chip label
from the start ("plain-text", "one-file", "trigger-match", "steps-in-order",
"same-result", "every-time", "standard-only") — no collapsed-spacing defect
occurred this build.

**B00 TIMING LAW.** Text: "How do I get Claude / to fix my design / for
accessibility?" (56 chars, 3 lines) — under the family's established-safe
60-char config — rendered at the same known-good parameters (charMs=42,
mistakeRate=4%, hesitateWithin=2%, hesitateBetween=8%, jitter=26,
lead_silence_s=0.8). Narration measured 11.24s + 0.8s lead ≈ 12s window
(≥9s floor, comfortably). Verified by frame pull: "fix" sits doomed in
terracotta mid-typing at t≈4.5s, and the corrected question "How do I get
Claude to review my design for accessibility?" is fully settled and
legible by t≈9s, holding through the clip's last frame (actual_duration_s
11.27s, ≥8s requirement met).

**One real GRAPHIC/REMOTION-beat defect caught and fixed via Gate V, not
GATE T's automated scan alone.** First `type_check.py` pass was **FAIL, 1
defect**: BOUT's eyebrow line, "ACCESSIBILITY REVIEW · @HumanitariansAI"
(OutroSeries, italic tracked-caps), produced an isolated trailing text-run
fragment ("...NSAI", the tail of the handle) measuring 36px — under the
41px §8.1 floor at 4K — where the sibling reel's shorter eyebrow
("SKILL DEVELOPMENT · @HumanitariansAI") had passed clean. Root-caused to
the longer string's letter-tracking pushing that fragment into a
different run-grouping than the passing sibling. Fixed by shortening the
eyebrow content to "ACCESSIBILITY · @HumanitariansAI" (dropping the
redundant "REVIEW" — the outro's own title line, "Review, Not Repair.",
already carries that word) and re-rendering BOUT alone; re-verified
directly via `type_check.check_min_size()` against the new frame (PASS,
42px >= 41px floor, individual-char fallback) before recompiling, then
confirmed visually via frame pull that the shorter eyebrow reads clean at
4K. Re-ran `type_check.py` on the full reel post-recompile: PASS, 0 FAILs.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`, one pass, no re-generation needed); NB01–NB03 rendered via
`render_scenes.py` (foreground, one pass, no re-render needed); B00/BCRY/
BHTF/BOUT rendered via `remotion_scenes.py` — the first invocation was
killed by an over-eager 120s shell timeout wrapper partway through (B00
and BHTF not yet rendered, BCRY/BOUT already done) rather than the
harness's own backgrounding; re-run to completion in the foreground with
an explicit 600s tool timeout, per the COMPLETION LAW's foreground-render
rule, confirming all 4 REMOTION beats present via ffprobe before
proceeding. BOUT was re-rendered a second time (`--only BOUT --force`)
after the eyebrow content fix above. Compiled twice (first cut, then the
BOUT fix + recompile):

```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Result: `knowledge-work-plugins--claude-liam-accessibility-review.mp4`,
7/7 beats filled real (no slate), 100.5s, 3840×2160 (native 4K —
`compile.py`'s 4K LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: FAIL→PASS, 0 FAILs after the BOUT eyebrow fix (see defect + fix
  above)
- GATE AUDIO: PASS — mean_volume **-24.2 dB** (ffmpeg volumedetect), max -3.0 dB
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 100.5s; mp4
  mtime (1788360221) newer than beat_sheet.json mtime (1788360092)
- Gate V (visual): pulled frames every ~5-10s across the full runtime
  (t=0.5 through t=99) plus targeted checks of B00 (t≈4.5s "fix" doomed in
  terracotta, t≈9s settled and correct through the clip's end), NB01–NB03
  (all chips legible, correctly spaced, no collapsed-space defect), BCRY
  (carry-out sentence + sparkline read clean), BHTF (correct topic/title/
  @HumanitariansAI handle, full paste-ready prompt legible; the two-line
  topic wrap sits directly above the title with no bbox-overlap per GATE T,
  consistent with the component's dynamic kicker-line spacing), and BOUT
  post-fix (shortened eyebrow "ACCESSIBILITY · @HumanitariansAI" reads
  clean, correct title restate, crimson underline, no truncation). No
  blockers remaining.
- B00 TIMING LAW: `actual_duration_s` 11.27s (≥8s requirement met); the
  "fix" → "review" correction lands on screen by t≈9s and the full
  corrected question stays legible for the remainder of the clip.

Metadata file written: `knowledge-work-plugins--claude-liam-accessibility-review.md`
(channel @HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors**). Per `playlists.json`, SUBJECT.json's family
(`knowledge-work-plugins`) is an exact key in the map, resolving directly
to "Extending Claude — Skills, Plugins & Connectors" — consistent with the
`claude-plugins-official--claude-liam-skill-development` sibling built in
the adjacent `claude-plugins` family. Direct code link per DELIVERY
CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.
