# BUILD-LOG — knowledge-work-plugins--claude-liam-cash-flow-snapshot

## 2026-09-02 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-cash-flow-snapshot/beat_sheet.json`
— a fully-filled, fully-narrated Teardown-register "skill-teardown" sheet
(metadata `register: "Teardown"`, `brand: "claude-liam"`, `audience:
"Claude"`, `source_skill` pointing at the cash-flow-snapshot small-business
Claude Tag Plugin skill). 7 beats: B00 cold open (ClaudeComposerAsk), B01
anatomy (skill = folder + SKILL.md), B02 pipeline (Steps section, linear
execution), B03 design tell, BVDT verdict (ClaudeVerdictArtifact), BHTF
handoff, BOUT outro — all already REMOTION, so NO-GENAI/NO-PANTRY LAW
required no substitution beyond the WRITER LAW swap at B00; no beat in the
source planned as `ai-video-prompt`, pantry, or a human-drop slot.

**Source defect found and disclosed, not worked around:** the source
batch-build pipeline substitutes a per-skill "job" phrase into a template
slot, visible in the delivered source as a bare `>` (e.g. B03: "Claude's
job: >."). Checked a sibling in the same batch
(`claude-liam-financial-statements/beat_sheet.json`) to confirm this is a
per-skill substitution failure, not an intentional device: that sibling's
slot filled correctly ("Generate financial statements..."); this skill's
never did, at every occurrence. No local copy of `cash-flow-snapshot`'s own
`SKILL.md` exists on this machine (its path in the source metadata,
`/Users/bear/Documents/CoWork/.../small-business/skills/cash-flow-snapshot/SKILL.md`,
resolves on a different machine) to recover the missing line. **This redo
does not invent it.** QUESTION.md and CARRY-OUT.md both log the disposition:
the reel states only the mechanism the source's *other* beats already
confirm as fact (a skill is a folder Claude reads, not code it writes;
SKILL.md is the instruction set; the Steps section runs linearly; same
input produces same output, every run) and never claims what fields or
formulas an actual cash flow snapshot would contain. Because every claim in
this reel is the source's own confirmed statement and none of it is this
reel's inference, **no ONE-FLAG beat was needed** — logged as a deliberate
choice in both QUESTION.md and SCRIPT.md's register audit, not an omission.

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
custom logic for this skill, corrected to the fact that a human already
wrote the instructions and Claude reads and follows them). Register
re-registered Teardown → Plain: the source's B03 framed the same facts as
"what it gets right" / "what it bites" — Teardown trade-off language —
restated here as mechanism and a determinism fact with no verdict on the
skill's design. Source's BVDT verdict recap folded into a dedicated BCRY
carry-out beat per CARRY-OUT LAW. Close re-skinned to `OutroCTA` /
@HumanitariansAI with Liam's sign-off. Anchor: B02 → B03, the "cash flow
snapshot · March" request submitted through three ordered steps, then run
again for an identical output, paid off against a different month's
request through the same three steps.

Built end to end this invocation:

1. GATE T (`type_check.py`) — PASS before any audio/render spend.
2. `generate_audio_kokoro.py` — 7 beats, free, `am_onyx`. Durations: B00
   11.37s, B01 17.05s, B02 16.28s, B03 25.09s, BCRY 8.94s, BHTF 11.86s,
   BOUT 3.46s.
3. Wrote `scenes.py` (3 Manim scenes, B01–B03, reel-unique names
   `CFSB01Scene`/`CFSB02Scene`/`CFSB03Scene` per the naming-collision
   lesson documented in sibling hai-simple BUILD-LOGs) and
   `render_scenes.py`; first pass hit one failure — `CFSB02Scene` used
   `ZERO` for an ORIGIN-position constant, which isn't a Manim name
   (`NameError: name 'ZERO' is not defined`); fixed to `ORIGIN` and
   re-ran clean.
4. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py`. The invocation
   exceeded the tool's 120s window and was moved to a background task by
   the harness; blocked on it directly with `TaskOutput` rather than
   ending the turn, per the one-shot-invocation law — all 4 beats
   completed, exit 0. B00 (BrutalistHesitantWriter) extended to 11.4s by
   the compile step to fill the narration window.

No defects found on first-pass frame inspection — verified directly, not
assumed:

- B00's typed text ("Claude built the cash-flow-snapshot skill. Right?")
  was checked at t=9.5s in the rendered clip before compiling into the
  master: the correction ("built" → "reads") is fully visible and the
  writer finishes the complete corrected question with the cursor resting
  at the end, satisfying WRITER LAW ("end ON the question") and TIMING LAW
  (media/B00.mp4 measured 11.4s, well above the 8s floor).
- B01–B03's Manim clips (9.5s / 11.5s / 13.9s native) were slowed 1.79x /
  1.42x / 1.81x by the compile step to fill their narration windows.
  Checked directly on frame pulls at 8s intervals through the full
  runtime: the folder listing (B01), the step-by-step anchor plant (B02),
  and the same-request-twice-then-a-different-month payoff (B03) all read
  as deliberate, legible pauses — no overlapping text, no clipped cards.

Compiled directly (`compile.py`, no `--force` needed — first compile):
`knowledge-work-plugins--claude-liam-cash-flow-snapshot.mp4`, 7/7 real (no
slate), 95.06s, 3840×2160 (THE 4K LAW — clean master forced to 4K
automatically).

**Gate V (visual):** pulled 12 frames at 8s intervals across the full
95.06s runtime plus a targeted late-frame check on B00, and read them
directly. B00's naive question and its "built"→"reads" correction read
cleanly, ending on the complete corrected question. B01's "no hidden
script — two items, that's all" (SKILL.md ~6k + reference/, nothing else)
reads cleanly. B02's THE ANCHOR (the "cash flow snapshot · March" request,
three ordered steps lighting up in sequence, one output card) reads
cleanly. B03's THE ANCHOR RETURNS (the same request run twice to two
identical output cards, a third run on "April" producing a different
card, both-directions caption beneath) reads cleanly — one frame caught a
mid-fade caption ("same steps, new input.") at partial opacity, confirmed
not a defect by checking the next frame, where it completes. BCRY's
carry-out card, BHTF's Your Turn composer card (the real explain-the-steps
prompt), and BOUT's outro/subscribe card render legibly with safe inset
respected. **Noted, not a defect introduced here:** `OutroCTA` renders on
a flat-white ground rather than the humanitarians cream (`#F3EBDD`) — same
shared-component behavior already logged unremarked in sibling hai-simple
reels (e.g. `redshift-api`); out of this reel's scope to fix.

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840x2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs)
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (ffmpeg volumedetect), max -2.8 dB
- ffprobe: video 3840x2160 h264, audio aac present; duration 95.06s;
  mp4 mtime (1788399951) newer than beat_sheet.json mtime (1788399834)

**Non-blocking warning (compile.py):** motion histogram remotion:4
graphic:3 — remotion at more than half of beats. Structural, not a defect:
hai-simple's mandated shape is B00 (writer) + BCRY + BHTF (Your Turn) +
BOUT (outro) all REMOTION by skill contract, against 3 GRAPHIC body beats
for this 7-beat reel — same disposition as every other short hai-simple
reel in this family.

Metadata file written:
`knowledge-work-plugins--claude-liam-cash-flow-snapshot.md` (channel
@HumanitariansAI, Playlist: **Extending Claude — Skills, Plugins &
Connectors** — resolved from `skills/make/hai-simple/loop/playlists.json`:
the reel's own family `knowledge-work-plugins` matches that exact prefix
in the map — plus the direct code link per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.

## 2026-09-02 — Phase 4 delivery

Master is already 3840x2160 (THE 4K LAW in compile.py forces any clean,
non-`--review` master to 4K), so the Fellows-facing 4K file is the same
render, copied to the `-4k` filename `deliver.py` expects:

```
cp knowledge-work-plugins--claude-liam-cash-flow-snapshot.mp4 \
   knowledge-work-plugins--claude-liam-cash-flow-snapshot-4k.mp4
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Staged to `DELIVERY/knowledge-work-plugins--claude-liam-cash-flow-snapshot/`
(4K master + description) and committed + pushed the text artifacts
(README.md = description, beat_sheet.json, SCRIPT.md, SUBJECT.json,
BUILD-LOG.md, CARRY-OUT.md, QUESTION.md — no media) to
`claude-bear/knowledge-work-plugins--claude-liam-cash-flow-snapshot/` in
the humanitarians-youtube clone: commit `676c80c5`, pushed clean
(`git status --short` empty after).

**Status: DELIVERED.**
