# BUILD-LOG — knowledge-work-plugins--claude-liam-change-request

## 2026-09-02 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-change-request/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `change-request`
Skill — create a change management request with impact analysis and
rollback plan — already fully built; no SCRIPT.md existed on the source,
so source `beats[*].narration_text` served as the locked script). Built
entirely fresh this invocation — only SUBJECT.json existed on pickup.
Followed the `knowledge-work-plugins--claude-liam-accessibility-review`
sibling as the structural precedent: identical source shape (7 beats:
composer-ask cold open + anatomy/pipeline + design-tell + verdict +
your-turn + outro), identical redo pattern (BrutalistHesitantWriter cold
open, merged design-tell+verdict beat, OutroSeries close), same Manim
chip-row scenes.py template copied verbatim for the GRAPHIC beats.

Question, facts, and full body argument carried over unchanged: a skill is
a folder Claude reads before it works (this one, change-request, is a
single SKILL.md file, about three kilobytes); the SKILL.md is a
plain-language instruction set with no hidden logic underneath it, and
Claude reads the file then acts on what it says; the skill's job, quoted
from its own description field: create a change management request with
impact analysis and rollback plan, triggering on proposing a system or
process change that needs approval, preparing a change record for CAB
review, documenting risk and rollback steps before a deployment, or
planning stakeholder communications for a rollout; once triggered, Claude
executes the Steps section in order, linear, no branching unless a step
says so; and the concrete distinction that follows from being a proposal
document rather than an executed action — same proposed change, same
request, every time, but the skill never makes the change itself, and
anything outside the described change is outside what it checks.

B00 replaced the source's `ClaudeComposerAsk` typed-ask cold open with
`BrutalistHesitantWriter` (WRITER LAW: "make" → "request" — the newcomer's
wrong guess that asking Claude for "a change request" means Claude will go
make the system or process change itself, corrected toward the actual
mechanism: the skill's own job description is to write the request
document, not execute it). Register re-registered Teardown→Plain: the
source's B03 "here is the Teardown moment... what it gets right / what it
bites" framing and BVDT's four-line verdict artifact were merged into a
single NB03 beat and stripped of judgment language, kept as the one fact a
general audience needs and can act on (repeatable request / scope-only
limit), per the NO JUDGMENT register check. BVDT's separate bulleted
artifact card was not kept as its own beat, per CARRY-OUT LAW — its facts
live in the single BCRY sentence instead. NB02 additionally folded in the
trigger-phrase clause the source had only quoted inline at B00 (now
replaced), since B00 is no longer the composer-ask beat that carried it.
Close re-skinned to @HumanitariansAI (`OutroSeries`).

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01/B02
anatomy/pipeline + B03 design tell + BVDT verdict + BHTF your-turn + BOUT
outro). This redo kept the same 7-beat shape: B00 carries the wrong-guess
pedagogy per WRITER LAW instead of a dedicated beat; B01→NB01, B02→NB02
kept as one beat each; B03+BVDT compressed into the single NB03; BHTF
kept, with the source's garbled truncation artifact ("I want to create a
change management request with impact analysis and rollback p. Read the
change-request skill...") rewritten to a complete, paste-ready prompt,
since the source text was a template-substitution artifact cut off
mid-sentence, not a deliberately authored prompt; BOUT kept. Full audit in
SCRIPT.md's "Beat-count note (redo)" section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01–NB03) built on the shared generic "chip row"
Manim template (`scenes.py`/`render_scenes.py`) copied verbatim from the
`knowledge-work-plugins--claude-liam-accessibility-review` sibling,
adapted with change-request-specific labels ("SKILL.md/plain-text/
one-file", "description/trigger-match/steps-in-order",
"same-result/every-time/scope-only") — single hyphenated tokens for every
accented/multi-word chip label, per the sibling's own learned lesson
(collapsed-spacing defect avoided from the start). No collapsed-spacing
defect occurred this build.

**B00 TIMING LAW.** Text: "How do I get Claude / to make a change / to my
system?" (57 chars, 3 lines) — under the family's established-safe 60-char
config — rendered at the same known-good parameters (charMs=42,
mistakeRate=4%, hesitateWithin=2%, hesitateBetween=8%, jitter=26,
lead_silence_s=0.8). Narration measured 10.5s + 0.8s lead ≈ 11.3s window
(≥9s floor, comfortably). Verified by frame pull: "make" sits doomed in
terracotta mid-typing at t≈2–3s, already corrected to "request" by t≈4.5s,
and the corrected question "How do I get Claude to request a change to my
system?" is fully settled and legible by t≈9.5s, holding through the
clip's last frame (actual_duration_s 10.5s, ≥8s requirement met).

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`, one pass, no re-generation needed); NB01–NB03 rendered via
`render_scenes.py` (foreground, one pass, no re-render needed); B00/BCRY/
BHTF/BOUT rendered via `remotion_scenes.py` (foreground, one pass, no
re-render needed — no backgrounding or timeout issues this build).
Compiled once:

```
python3 runtime/scripts/compile.py <REEL_DIR>
```

Result: `knowledge-work-plugins--claude-liam-change-request.mp4`, 7/7
beats filled real (no slate), 95.8s, 3840×2160 (native 4K — `compile.py`'s
4K LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T (`type_check.py`): PASS, 0 FAILs on first pass (no defect this
  build, unlike the accessibility-review sibling's BOUT eyebrow fix)
- GATE AUDIO: PASS — mean_volume **-24.2 dB** (ffmpeg volumedetect), max -2.8 dB
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 95.78s; mp4
  mtime (1788401193) newer than beat_sheet.json mtime (1788401057)
- Gate V (visual): pulled frames every ~5-8s across the full runtime
  (t=0.5 through t=94) plus targeted checks of B00 (t≈2-3s "make" doomed
  in terracotta, t≈4.5s already corrected, t≈9.5s settled and correct
  through the clip's end), NB01–NB03 (all chips legible, correctly
  spaced, no collapsed-space defect, correct accent placement), BCRY
  (carry-out sentence + sparkline read clean), BHTF (correct topic/title/
  @HumanitariansAI handle, full paste-ready prompt legible), and BOUT
  (eyebrow "CHANGE REQUEST · @HumanitariansAI" reads clean at 4K, no
  truncation, correct title restate, crimson underline). No blockers.
- B00 TIMING LAW: `actual_duration_s` 10.5s (≥8s requirement met); the
  "make" → "request" correction lands on screen well before t=9s and the
  full corrected question stays legible for the remainder of the clip.

Metadata file written: `knowledge-work-plugins--claude-liam-change-request.md`
(channel @HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors**). Per `playlists.json`, SUBJECT.json's family
(`knowledge-work-plugins`) is an exact key in the map, resolving directly
to "Extending Claude — Skills, Plugins & Connectors" — consistent with the
`knowledge-work-plugins--claude-liam-accessibility-review` sibling built
in the same family. Direct code link per DELIVERY CONTRACT format
included.

**Status: review cut DONE.** Passed every Phase-3 gate.

## 2026-09-02 — Phase 4, DELIVERED

Master was already born native 3840x2160 (compile.py's 4K LAW), so copied
directly to `knowledge-work-plugins--claude-liam-change-request-4k.mp4`
rather than re-rendering at a higher resolution.

```
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Staged `DELIVERY/knowledge-work-plugins--claude-liam-change-request/`
(4K master + description) for the Drive sync. Committed to
`claude-bear/knowledge-work-plugins--claude-liam-change-request/`
(README.md = description, beat_sheet.json, SCRIPT.md, SUBJECT.json,
CARRY-OUT.md, QUESTION.md, BUILD-LOG.md — no mp3/mp4) as commit
`c9e42625`, pushed clean (no rebase conflicts).

**Status: DELIVERED.**
