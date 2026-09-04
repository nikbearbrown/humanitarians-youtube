# BUILD-LOG — knowledge-work-plugins--claude-liam-month-heads-up

## 2026-09-04 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-month-heads-up/beat_sheet.json`
— a fully-filled, fully-narrated Teardown-register "skill-teardown" sheet
(metadata `register: "Teardown"`, `brand: "claude-liam"`, `audience:
"Claude"`, `source_skill` pointing at the month-heads-up small-business
Claude Tag Plugin skill). 7 beats: B00 cold open (ClaudeComposerAsk), B01
anatomy (skill = folder + SKILL.md), B02 pipeline (Steps section, linear
execution), B03 design tell, BVDT verdict (ClaudeVerdictArtifact), BHTF
handoff, BOUT outro — all already REMOTION, so NO-GENAI/NO-PANTRY LAW
required no substitution beyond the WRITER LAW swap at B00; no beat in the
source planned as `ai-video-prompt`, pantry, or a human-drop slot.

**Source condition, checked and disclosed:** unlike some siblings in this
batch (e.g. `cash-flow-snapshot`, which lost its per-skill job phrase to a
template-substitution bug), this source's B00 carries the skill's full job
description intact: "Runs on the 25th — shows the next 30-day cash-flow
outlook and flags anything that needs attention before month-end. Accepts
optional 30 or 60 day horizon." Later beats (B03, BVDT, BHTF) repeat a
truncated copy of the same phrase — a template-length artifact in the
source's batch build, not a missing fact, since the full line survives in
B00. Nothing in this reel is invented: the optional 30-/60-day horizon
parameter is the source's own stated fact and became the differentiator
for this redo's anchor (most siblings only vary the anchor's month/topic;
this one has a real configurable parameter to exercise). B01's `files`
list confirms the folder holds exactly one item — `SKILL.md`, ~2k — no
`reference/` folder for this skill, unlike `cash-flow-snapshot`'s two-item
folder; this redo kept that distinction rather than copying the sibling's
shape.

Given this reel's beat count (7, matching the source exactly per the
redo-mode "keep beat count" rule), the body beats compress the source's
three Teardown beats (B01 anatomy, B02 pipeline, B03 design tell) into
three GRAPHIC beats (B01, B02, B03) built fresh in Manim, following
hai-simple's Plain-register spine (stakes → wrong guess, falsified →
mechanism / anchor planted → anchor payoff / both directions) instead of
the source's anatomy/pipeline/tell structure.

B00 replaced the source's `ClaudeComposerAsk` cold open (which stated the
skill name with no wrong-guess framing) with `BrutalistHesitantWriter`
(WRITER LAW: "built" → "reads" — the naive assumption that Claude wrote
custom cash-flow logic for this skill, corrected to the fact that a human
already wrote the instructions and Claude reads and follows them).
Register re-registered Teardown → Plain: the source's B03 framed the same
facts as "what it gets right" / "what it bites" — Teardown trade-off
language — restated here as mechanism and a determinism fact with no
verdict on the skill's design. Source's BVDT verdict recap folded into a
dedicated BCRY carry-out beat per CARRY-OUT LAW. Close re-skinned to
`OutroCTA` / @HumanitariansAI with Liam's sign-off. Anchor: B02 → B03, the
"month check · 25th · 30-day horizon" request submitted through three
ordered steps, run again for an identical output, then paid off against a
60-day-horizon request through the same three steps — landing BOTH-
DIRECTIONS on a genuine feature of this specific skill (the optional
horizon parameter) rather than an arbitrary substitution.

Built end to end this invocation:

1. GATE T (`type_check.py`) — PASS before any audio/render spend.
2. `generate_audio_kokoro.py` — 7 beats, free, `am_onyx`. Durations: B00
   11.61s, B01 14.59s, B02 16.70s, B03 27.11s, BCRY 8.94s, BHTF 11.43s,
   BOUT 3.18s.
3. Wrote `scenes.py` (3 Manim scenes, B01–B03, reel-unique names
   `MHUB01Scene`/`MHUB02Scene`/`MHUB03Scene` per the naming-collision
   lesson documented in sibling hai-simple BUILD-LOGs) and
   `render_scenes.py`; all 3 rendered clean on first pass, no failures.
4. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py`. The invocation
   exceeded the tool's 120s foreground window and was moved to a
   background task by the harness; blocked on it directly with
   `TaskOutput` rather than ending the turn, per the one-shot-invocation
   law — all 4 beats completed, exit 0. B00 (BrutalistHesitantWriter)
   extended to 11.6s by the compile step to fill the narration window.

No defects found on first-pass frame inspection — verified directly, not
assumed:

- B00's typed text ("Claude built the month-heads-up skill. Right?") was
  checked at t=9.5s in the rendered clip before compiling into the
  master: the correction ("built" → "reads") is fully visible and the
  writer finishes the complete corrected question with the cursor resting
  at the end, satisfying WRITER LAW ("end ON the question") and TIMING LAW
  (media/B00.mp4 measured 11.6s, well above the 8s floor).
- B01–B03's Manim clips were slowed 1.47x / 1.38x / 1.77x by the compile
  step to fill their narration windows. Checked directly on 12 frame pulls
  at 8s intervals through the full runtime: the one-item folder listing
  (B01), the step-by-step anchor plant with the "month check · 25th ·
  30-day horizon" request (B02), and the same-request-twice-then-a-
  60-day-horizon payoff (B03) all read as deliberate, legible pauses — no
  overlapping text, no clipped cards. One frame (f04, mid-scene) caught a
  card fading in at partial opacity; confirmed not a defect by checking
  the next frame, where the full anchor diagram (request → three steps →
  output) is complete and legible.

Compiled directly (`compile.py`, no `--force` needed — first compile):
`knowledge-work-plugins--claude-liam-month-heads-up.mp4`, 7/7 real (no
slate), 94.6s, 3840×2160 (THE 4K LAW — clean master forced to 4K
automatically).

**Gate V (visual):** pulled 12 frames at 8s intervals across the full
94.6s runtime plus a targeted late-frame check on B00, and read them
directly. B00's naive question and its "built"→"reads" correction read
cleanly, ending on the complete corrected question. B01's "no hidden
script — one item, that's all" (SKILL.md ~2k, nothing else) reads
cleanly. B02's THE ANCHOR (the "month check · 25th · 30-day horizon"
request, three ordered steps lighting up in sequence, one output card)
reads cleanly. B03's THE ANCHOR RETURNS (the same request run twice to
two identical output cards, a third run at a 60-day horizon producing a
different card, both-directions caption beneath) reads cleanly. BCRY's
carry-out card, BHTF's Your Turn composer card (the real explain-the-steps
prompt), and BOUT's outro/subscribe card render legibly with safe inset
respected. **Noted, not a defect introduced here:** `OutroCTA` renders on
a flat-white ground rather than the humanitarians cream (`#F3EBDD`) — same
shared-component behavior already logged unremarked in sibling hai-simple
reels (e.g. `cash-flow-snapshot`, `redshift-api`); out of this reel's
scope to fix.

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840x2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs)
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (ffmpeg volumedetect, verified
  independently), max -2.9 dB
- ffprobe: video 3840x2160 h264, audio aac present; duration 94.581s;
  mp4 mtime (1788523538) newer than beat_sheet.json mtime (1788523447)

**Non-blocking warning (compile.py):** motion histogram remotion:4
graphic:3 — remotion at more than half of beats. Structural, not a defect:
hai-simple's mandated shape is B00 (writer) + BCRY + BHTF (Your Turn) +
BOUT (outro) all REMOTION by skill contract, against 3 GRAPHIC body beats
for this 7-beat reel — same disposition as every other short hai-simple
reel in this family.

Metadata file written:
`knowledge-work-plugins--claude-liam-month-heads-up.md` (channel
@HumanitariansAI, Playlist: **Extending Claude — Skills, Plugins &
Connectors** — resolved from `skills/make/hai-simple/loop/playlists.json`:
the reel's own family `knowledge-work-plugins` matches that exact prefix
in the map — plus the direct code link per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.
