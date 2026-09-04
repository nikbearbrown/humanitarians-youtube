# BUILD-LOG — knowledge-work-plugins--claude-liam-call-list

## 2026-09-02 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-call-list/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the Anthropic `call-list`
small-business plugin Skill, already fully built — no SCRIPT.md; source
`beats[*].narration_text` served as the locked script). Built entirely
fresh this invocation — only SUBJECT.json existed on pickup. Mirrored the
proven structural template from the `financial-services--claude-liam-
competitive-analysis` sibling (same source shape: skill-teardown, 7 beats),
including its shared "chip row" Manim scaffold (`scenes.py`/
`render_scenes.py`), adapted with call-list-specific labels.

Question, facts, and full body argument carried over unchanged: the
call-list skill is a folder — one SKILL.md file; Claude reads the file,
then acts; the pipeline is in a Steps section, executed linearly with no
branching unless a step says so; the skill ranks the top-5 leads most worth
calling today, pulls talking points from email history, blocks time on the
calendar, and drafts follow-up messages; it answers only within what that
file specifies. B00 replaced the source's `ClaudeComposerAsk` typed-ask
cold open with `BrutalistHesitantWriter` (WRITER LAW: "judged" →
"processed" — the newcomer's wrong guess that a ranked call list means
Claude judged which leads matter most, corrected toward the actual
mechanism: the skill just processes a fixed set of written steps). Register
re-registered Teardown→Plain: the source's B03 "what it gets right:
repeatable results / what it bites: anything outside the spec" framing was
stripped of its gets-right/bites verdict language and compressed into a
plain scope description (inside the written scope vs. outside it) — no
ruling on whether the design is good or bad, per the NO JUDGMENT register
check. BVDT's verdict facts (same input → same output every run; the limit
is only what the file says) were merged into the single BCRY carry-out
sentence rather than kept as a separate bulleted artifact card, per
CARRY-OUT LAW. Close re-skinned to @HumanitariansAI (`OutroSeries`).

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01/B02
anatomy/pipeline + B03 design tell + BVDT verdict + BHTF your-turn + BOUT
outro). This redo kept the same 7-beat shape: B00 carries the wrong-guess
pedagogy per WRITER LAW instead of a dedicated beat; B01→NB01, B02→NB02 kept
as one beat each; B03's concrete task list plus its gets-right/bites framing
compressed into NB03 (dropping the Teardown verdict language, keeping the
plain scope description and the anchor's concrete steps in narration); BVDT
folded into BCRY; BHTF kept, but its prompt was rewritten — the source's
version was a garbled, mid-template sentence ("I want to ranks the top-5
leads most worth calling today, supplies talking point. Read the call-list
skill...") that was not runnable as written, so it was replaced with a
concrete, grammatical, paste-ready prompt (rank leads from this week's
email threads, draft follow-ups) that keeps the source's own "walk me
through what you will do before you do it" clause; BOUT kept. Full audit in
SCRIPT.md's "Beat-count note (redo)" section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism` /
`ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no substitution
beyond B00's mandated cold-open swap.

**NB03 chip-count fix:** first attempt used 4 chips with longer labels
("calendar + follow-up") to carry the concrete task list visually; GATE T
flagged a 16px text run under the 20px floor once the chip-row layout
shrank to fit 4 wide labels in the generic template's chip width. Fixed by
reverting to the sibling's proven 3-chip pattern ("written scope" / "same
steps" / "outside: nothing") — the concrete task list stays in narration
only, which is where it was already carrying the anchor. Re-rendered NB03,
re-ran GATE T: PASS.

All 3 GRAPHIC beats (NB01–NB03) built on the shared generic "chip row"
Manim template, copied verbatim (mechanism, colors, GATE T exemption notes)
from the `financial-services--claude-liam-competitive-analysis` sibling,
adapted with call-list-specific labels.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`) — no manual timing fixes needed; B00's audio measured 10.39s
against a 34-word narration + 0.9s lead silence, clearing the WRITER LAW's
≥8s floor. Manim beats (NB01–NB03) rendered via `render_scenes.py` in the
foreground, no failures. Remotion beats (B00/BCRY/BHTF/BOUT) rendered via
`remotion_scenes.py` in the foreground (all extended cleanly to their audio
durations, no slates). `type_check.py` (GATE T) failed once (NB03 min-size,
see above), fixed, then passed clean, 0 FAILs.

Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR>
```

Result: `knowledge-work-plugins--claude-liam-call-list.mp4`, 7/7 beats
filled real (no slate), 82.1s, 3840×2160 (native 4K — `compile.py`'s 4K
LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (after the NB03 chip-count fix above)
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect, per
  compile.py's own gate)
- ffprobe: video 3840×2160 h264, audio (aac) present, duration 82.12s; mp4
  mtime (1788389522) newer than beat_sheet.json mtime (1788389395)
- Gate V (visual): pulled frames every ~4s across the full runtime plus
  targeted checks of B00 (t≈9.0s: "A ranked list means Claude processed my
  leads." — correction landed and legible), NB01 (SKILL.md / 1 file chips +
  "the file is the program" caption, accent underline on SKILL.md, all
  legible), NB02 (read/execute/return chips with arrows, accent underline
  on "execute steps"), NB03 (written scope / same steps / outside: nothing
  chips, accent on the last, "same input, same steps, every run" caption),
  BCRY (carry-out sentence + "Steps, not judgment." sparkline read clean),
  BHTF (correct topic "CALL-LIST · ANTHROPIC SKILL", title "Claude, Call
  List.", @HumanitariansAI handle, paste-ready prompt legible), and BOUT
  (OutroSeries: correct eyebrow "CALL LIST · @HumanitariansAI", correct
  title restate, crimson underline, no truncation). No blockers. Noted, not
  a defect: `OutroSeries` renders on flat white rather than the
  humanitarians cream ground, same shared-component behavior already
  logged unremarked across every other `hai-simple` redo in this loop
  (e.g. the `financial-services--claude-liam-competitive-analysis`
  sibling).
- B00 TIMING LAW: `actual_duration_s` 10.39s (≥8s requirement met); the
  "judged" → "processed" correction lands on screen and is legible well
  before the clip ends.

Metadata file written:
`knowledge-work-plugins--claude-liam-call-list.md` (channel
@HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins &
Connectors**). Per `playlists.json`, SUBJECT.json's family
(`knowledge-work-plugins`) matches the map's `knowledge-work-plugins` key
directly, resolving to "Extending Claude — Skills, Plugins & Connectors" —
never the bare "Claude". Direct code link per DELIVERY CONTRACT format
included.

**Status: review cut DONE.** Passed every Phase-3 gate.

## 2026-09-02 — Phase 4, DELIVERED

Master was already born native 3840×2160 (compile.py's 4K LAW), so copied
directly to `knowledge-work-plugins--claude-liam-call-list-4k.mp4` rather
than re-rendering at a higher resolution.

```
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Staged `DELIVERY/knowledge-work-plugins--claude-liam-call-list/` (4K master
+ description) for the Drive sync. Committed to
`claude-bear/knowledge-work-plugins--claude-liam-call-list/` (README.md =
description, beat_sheet.json, SCRIPT.md, SUBJECT.json, CARRY-OUT.md,
QUESTION.md, BUILD-LOG.md — no mp3/mp4) as commit `02da7fe6`, pushed clean
(no rebase conflicts).

**Status: DELIVERED.**
