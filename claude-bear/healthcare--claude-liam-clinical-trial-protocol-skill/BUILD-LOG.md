# BUILD-LOG — healthcare--claude-liam-clinical-trial-protocol-skill

## 2026-09-02 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/healthcare/youtube/claude-liam-clinical-trial-protocol-skill/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic
`clinical-trial-protocol-skill` Claude Skill, from the `healthcare` book's
plugin set; already fully built, no SCRIPT.md — source `beats[*].narration_text`
plus its `AUDIT.md`/`PEDAGOGY.md` served as the locked script/facts). Built
entirely fresh this invocation — only SUBJECT.json existed on pickup.

Question, facts, and full body argument carried over: a skill is a folder
Claude reads before it works, containing SKILL.md (plain language, no
hidden logic) plus README.md, assets/, references/, and scripts/ — five
files/folders total (per the source's own `SkillTeardownAnatomy` file
list); the pipeline runs as three linear steps — read SKILL.md, execute
each step from the Steps section in order, return the result — no
branching unless a step says so; the skill's job is generating clinical
trial protocols for medical devices or drugs, for requests like "create a
clinical trial protocol" or "help me design a clinical study"; it follows
the SKILL.md's instructions exactly, so the same request produces the same
kind of protocol every run; it only covers what the file specifies. B00
replaced the source's `ClaudeComposerAsk` typed-ask cold open with
`BrutalistHesitantWriter` (WRITER LAW: "decide" -> "draft" — the
newcomer's wrong guess that a skill this consequential must be exercising
clinical/regulatory judgment, corrected toward the actual mechanism: it
drafts a document to a fixed spec, and a person still decides the trial
design). Register re-registered Teardown -> Plain: the source's B03 "gets
it right: repeatable results / what it bites: anything outside the spec"
framing was restated in NB03 as a plain mechanism-and-boundary fact, per
the NO JUDGMENT register check. BVDT's verdict facts (same input -> same
output every run; limited to what the file specifies) were merged into
NB03/BCRY rather than kept as a separate bulleted artifact card, per
CARRY-OUT LAW. BHTF's prompt was adapted, not copied verbatim: the source
asked the viewer to "read the clinical-trial-protocol-skill skill," which
requires a plugin install a general viewer won't have, so this redo
substitutes an equivalent, actually paste-ready prompt exercising the same
spec-discipline on any document/outline, with no medical subject matter
required. Close re-skinned to @HumanitariansAI (`OutroSeries`).

**No content correction against the source was needed** (unlike the
`clinical-note-extract-skill` sibling): this source's own `AUDIT.md`
passed its content-accuracy checks (Check 9, Check 10) with only cosmetic
fixes logged (truncated strings, sparkline word count, a datable
`modelLabel` claim) — no factual/pipeline error is documented, so NB02
keeps the source's three-phase pipeline description as-is. See
QUESTION.md for the full note.

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01
anatomy + B02 pipeline + B03 teardown design-tell + BVDT verdict + BHTF
your-turn + BOUT outro). This redo kept the same 7-beat shape: B00 carries
the wrong-guess pedagogy per WRITER LAW instead of a dedicated beat;
B01->NB01, B02->NB02 kept as one beat each; B03's Teardown framing
compressed into NB03 (a plain mechanism-and-boundary fact); BVDT folded
into BCRY; BHTF kept (prompt adapted, see above); BOUT kept. Full audit in
SCRIPT.md's "Beat-count note (redo)" section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01-NB03) built on the shared generic "chip row"
Manim template (`scenes.py`/`render_scenes.py`) copied verbatim (mechanism,
colors, GATE T exemption notes) from the
`healthcare--claude-liam-clinical-note-extract-skill` sibling (itself
copied from `financial-services--claude-liam-kyc-rules`), adapted with
clinical-trial-protocol-skill-specific labels.

**B00 TIMING LAW** — rates (42ms/char, 8% hesitateBetween, 4% mistakeRate,
short 3-line text) reused directly from the same
`financial-services--claude-liam-kyc-rules` sibling's proven working
configuration. `actual_duration_s` (narration) 11.78s + `lead_silence_s`
1.0 gave the writer a 12.78s window; rendered clip extended to 11.8s,
comfortably clearing the >=8s TIMING LAW floor. Verified by frame pulls at
t=2.0s ("decide" mid-type in terracotta) and t=5.0s/9.5s/11.0s (full
corrected question "Does Claude draft a clinical trial protocol?" settled
and legible, holding to the end of the clip, @HumanitariansAI overlay
present) — correction lands and settles well inside the clip.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`, cost $0.00). NB01-NB03 rendered via `render_scenes.py`
(foreground, all 3 ok first pass). B00/BCRY/BHTF/BOUT rendered via
`remotion_scenes.py` — the invocation exceeded the tool's 120s timeout and
was moved to background by the harness automatically; blocked on it via
`TaskOutput` (block=true) before proceeding, per the COMPLETION LAW's
foreground-render rule, and confirmed exit code 0 with all four beats
reporting `ok` before moving on.

Compiled:
```
python3 runtime/scripts/compile.py <REEL_DIR>
```
Result: `healthcare--claude-liam-clinical-trial-protocol-skill.mp4`, 7/7
beats filled real (no slate), 94.8s, 3840x2160 (native 4K — `compile.py`'s
4K LAW).

**Gate V finding: none.** Pulled frames at t=2/5/9.5/11 (B00 correction
timing), t=20/30 (NB01/NB02), t=45/60 (NB02/NB03), t=67 (BCRY), t=75/88
(BHTF), t=93 (BOUT). NB02's bold accented chip "execute steps" looked
ambiguous at thumbnail resolution (the exact glyph-gluing failure mode the
`clinical-note-extract-skill` sibling hit on "explicit null"), so it was
re-checked with a full-resolution ffmpeg crop of just that chip before
ruling — at full res it reads "execute steps" cleanly, properly spaced;
the ambiguity was a downscaling artifact of the thumbnail, not a render
defect. No fix needed. All other beats (B00 writer + overlay, NB01 chips,
NB03 chips, BCRY quote + sparkline, BHTF prompt + folder label, BOUT
eyebrow/title) read clean on first pass — zero blockers, no re-render
needed.

Compiled with all gates passing on the first compile (`compile.py`, no
`--force` needed):
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840x2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T (`type_check.py`): PASS, 0 FAILs
- GATE AUDIO: PASS — mean_volume **-24.1 dB** (ffmpeg volumedetect), max
  -3.0 dB
- ffprobe: video 3840x2160 h264, audio (aac) present, duration 94.78s; mp4
  mtime (1788336888) newer than beat_sheet.json mtime (1788336782)
- Gate V (visual): see finding above — no blockers.

Metadata file written:
`healthcare--claude-liam-clinical-trial-protocol-skill.md` (channel
@HumanitariansAI, **Playlist: Claude Basics**). Per `playlists.json`,
SUBJECT.json's family (`healthcare`) matches no specific vertical prefix
in the map (no `healthcare-`/`clinical-` entry exists), so resolution
falls through in map order to the `hai-simple` key itself (present in the
map precisely as this general fallback), which resolves to "Claude Basics"
— reached before `_default` ("Claude Across the Curriculum") is ever
considered, matching the disposition of both the `clinical-note-extract-skill`
and `kyc-rules` siblings exactly. Direct code link per DELIVERY CONTRACT
format included.

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.

## 2026-09-02 — Phase 4, DELIVERED

Master was already born native 3840x2160 (compile.py's 4K LAW), so copied
directly to `healthcare--claude-liam-clinical-trial-protocol-skill-4k.mp4`
rather than re-rendering at a higher resolution.

```
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Staged `DELIVERY/healthcare--claude-liam-clinical-trial-protocol-skill/`
(4K master + description) for the Drive sync. Committed to
`claude-bear/healthcare--claude-liam-clinical-trial-protocol-skill/`
(README.md = description, beat_sheet.json, SCRIPT.md, SUBJECT.json,
CARRY-OUT.md, QUESTION.md, BUILD-LOG.md — no mp3/mp4).

**Status: DELIVERED.**
