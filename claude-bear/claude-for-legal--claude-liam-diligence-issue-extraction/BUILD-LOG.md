# BUILD-LOG — claude-for-legal--claude-liam-diligence-issue-extraction

## 2026-08-29 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-for-legal/youtube/claude-liam-diligence-issue-extraction/beat_sheet.json`
(Teardown skill-teardown of Anthropic's `diligence-issue-extraction` corporate-legal
skill, 7 beats: cold open, anatomy, pipeline, design tell, verdict, handoff, outro).

**Source-gap finding (see QUESTION.md):** the source sheet is fully "built" (7 beats,
all VIDEO/filled, dated 2026-07-25) but its narration carries literal, never-filled
template placeholders (`>`) at every skill-specific fact point, and its `source_skill`
field (`/Users/bear/.../corporate-legal/skills/diligence-issue-extraction/SKILL.md`)
does not exist anywhere on this machine — searched the full `books/` tree. Same defect
class as this family's `clearance`/`ai-inventory`/`ai-tool-handoff`/`aia-generation`
siblings, all already delivered. Per Phase 1's "when in doubt, describe behavior
generically" rule, reconstructed a generic, defensible account of what a diligence
issue-extraction skill does: screening a batch of deal documents against a checklist of
issue categories (change-of-control clauses, missing consents, expired licenses) and
returning a structured issues report. No fact asserted is Claude-specific, invented, or
tied to a real deal.

B00 replaced the source's `ClaudeComposerAsk` teardown-ask framing with
`BrutalistHesitantWriter` (WRITER LAW): writer types "Can Claude DECIDE which issues
kill this deal?", hesitates on DECIDE, corrects to "flag" → lands "Can Claude flag which
issues kill this deal?". Register re-registered Teardown→Plain: source's BVDT verdict
beat ("what it gets right / what it bites") dropped its judgment language; the
constraint statement was kept (B03) and the verdict's core fact compressed into BCRY as
a plain carry-out with no "Verdict" framing. Source's 7-beat shape carried over exactly:
B00→B00(Remotion writer), B01→B01(anatomy, unchanged), B02→B02(pipeline, unchanged),
B03→B03(mechanism, judgment dropped), BVDT→BCRY(carry-out, WantQuote), BHTF→BHTF(handoff,
placeholder concretized into a real vendor-contracts scenario), BOUT split into
BOUT(OutroSeries title restate)+BCTA(OutroCTA handle) per this skill's close pattern —
8 beats total (was 7; BOUT's dual role in the source is two beats here, matching the
`clearance` sibling's identical split). No source beat was ai-video-prompt, pantry, or a
human-drop slot — NO-GENAI/NO-PANTRY LAW required no substitution beyond B00.

**Build steps run, all foreground, this invocation:**
1. `generate_audio_kokoro.py` — 8/8 beats, `am_onyx`, `actual_duration_s` written back.
   B00 measured 11.16s (≥8s TIMING LAW floor; 35-word narration + `lead_silence_s` 0.8).
2. `remotion_scenes.py` — all 8 beats are REMOTION (matches source's all-Remotion
   skill-teardown shape); ran to completion, exit code 0, all 8 media/*.mp4 present.
3. `compile.py` — `claude-for-legal--claude-liam-diligence-issue-extraction.mp4`,
   3840×2160 (4K LAW forces master resolution), 80.2s, 8/8 beats real, no slate.

**Gates:**
- type_check.py: 1 non-blocking flag — §8.9 [BOUT/eyebrow] "CLAUDE BASICS ·
  HUMANITARIANS AI" reads as truncated; the middle-dot `·` character trips the
  heuristic. Same string, same false positive, already shipped unfixed in this family's
  delivered `clearance` sibling (and `brief-section-drafter`/`legal-finance` before it) —
  left as-is per that precedent rather than reworking house style. Pixel/shape checks
  (§8.10) all SKIP pre-render as expected; GATE T proper reduces to this one flag with no
  media-dependent FAILs once rendered.
- content-check: PASS (8 beats, no violations)
- frame-check: PASS (3840×2160, 8 beats, no violations)
- lane-check: PASS (cut=master, no lane violations)
- GATE AUDIO: PASS — `compile.py` reported mean_volume -23.9 dB; independently
  re-verified with `ffmpeg -af volumedetect`: mean -23.9 dB, max -2.9 dB. Well above the
  -40 dB floor.
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 80.208s; master mtime
  (1788054395) newer than beat_sheet.json mtime (1788054308) — beat_sheet.json was never
  touched after the compile that produced this master.
- Gate V (visual): pulled 13 frames at 6s spacing plus a targeted B00 late-pull (t=10s)
  and a targeted BCTA pull (t=78.5s), read directly. B00's correction ("DECIDE" →
  "flag", landing "Can Claude flag which issues kill this deal?") is legible and lands
  on screen. B01 anatomy, B02 pipeline (ISSUES REPORT output label correct), B03
  mechanism, BCRY carry-out quote, BHTF your-turn composer card (@HumanitariansAI
  folderLabel correct), BOUT title restate, and BCTA (@HumanitariansAI handle, subscribe
  chip) all legible, correctly kerned, safe inset respected, no text overlap. BOUT/BCTA
  render on flat white rather than the humanitarians cream ground — same
  shared-component behavior already logged unremarked in sibling reels
  (`ai-inventory`, `claude-liam-clearance`). No blockers.
- B00 TIMING LAW: `actual_duration_s` 11.16s (≥8s requirement met); correction lands
  on screen per the late frame pull.

**Non-blocking warning (compile.py):** motion histogram remotion:8 (100%), over the
~40% pantry cap in MOTION.md. Structural: the source's skill-teardown shape is entirely
REMOTION beats (ClaudeComposerAsk/SkillTeardownAnatomy/SkillTeardownPipeline/
SkillTeardownMechanism/ClaudeVerdictArtifact/ClaudeComposerAsk/ClaudeTitleOutro) with no
GRAPHIC body beats to begin with — this redo carries that shape over beat-for-beat per
the redo contract (shape and beat count are locked from source), so there is no GRAPHIC
content to convert the ratio against. Logged per the honesty rule rather than inventing
GRAPHIC beats the source never had.

**Playlist:** Claude Basics. `SUBJECT.json`'s `family: "claude-for-legal"` matches no
prefix in `playlists.json`'s map; falls to the `hai-simple` skill-key fallback →
"Claude Basics" — same resolution every other delivered `claude-for-legal--*` redo in
this family has used (`ai-inventory`, `ai-tool-handoff`, `auto-updater`,
`bar-prep-questions`, `board-minutes`, `brief-section-drafter`, `clearance`).

Metadata file written: `claude-for-legal--claude-liam-diligence-issue-extraction.md`
(channel @HumanitariansAI, Playlist: **Claude Basics**, plus the direct code link per
the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to Phase 4 (4K
render + deliver.py) in this same invocation.
