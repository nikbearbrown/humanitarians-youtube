# BUILD-LOG — financial-services--claude-liam-accrual-schedule

## 2026-09-01 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/financial-services/youtube/claude-liam-accrual-schedule/beat_sheet.json`.

**Source note:** the source sheet's narration already carries real,
specific facts about the Anthropic `accrual-schedule` skill (not an
unfilled placeholder shell) — see QUESTION.md. Facts preserved: the skill
builds the period-end accrual schedule; for each accrual it computes the
entry, cites the support, and drafts the JE; used during month-end close;
the JE is a draft for controller approval, not a posting. The
`source_skill` path it names does not exist on this machine (different
machine's home directory), but no reconstruction was needed.

**The call:** register re-registered Teardown → Plain. Source's B03
framed "what it gets right / where it bites" as a design-tell verdict —
Teardown language — removed; Plain states only the mechanism (compute the
entry, cite the support, draft the JE) and its two failure directions as
properties of the practice, never a verdict on the skill's design. B00
replaced the source's `ClaudeComposerAsk` cold open with
`BrutalistHesitantWriter` per WRITER LAW: "judgment" → "the support" — the
naive assumption that building the schedule takes Claude's own accounting
judgment, corrected to: it computes from what's cited. Added a wrong-guess
beat (B01: accounting judgment vs. compute/cite/draft, falsified by "an
expense with no supporting document gets nothing drafted") and an anchor
(B02 → B03: a December utility bill traveling identified → computed →
cited → drafted → stopped, waiting for approval) per this factory's
PHASE 1 structure requirement — the source's Teardown shape (anatomy /
pipeline / design-tell / verdict) carried neither. Close re-skinned to
`OutroCTA` / @HumanitariansAI with Liam's sign-off. Kept the source's
7-beat count (B00, B01, B02, B03, BCRY, BHTF, BOUT). No source beat was
AI-VIDEO, pantry, or a human-drop slot — every source beat was already
REMOTION, so NO-GENAI/NO-PANTRY LAW required no beat replacement beyond
B00 itself.

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 7 beats, free, `am_onyx`, first pass, no
   retries needed. B00 landed at 10.35s (clear of the ≥9s TIMING LAW
   floor) on the first narration draft (31 words + `lead_silence_s: 0.8`).
   Durations: B00 10.35s, B01 19.22s, B02 18.77s, B03 21.87s, BCRY 10.05s,
   BHTF 19.88s, BOUT 4.1s (+1.0s tail).
2. Wrote `scenes.py` (3 Manim scenes, reel-unique names `ACSB01Scene` /
   `ACSB02Scene` / `ACSB03Scene`) and `render_scenes.py`; rendered B01 and
   B03 clean on the first pass.
3. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py` in the foreground
   (the shell moved it to a background task past the 120s inline timeout;
   blocked on it with `TaskOutput` rather than ending the turn — no
   unsupervised background render was left running). All four rendered
   clean on the first pass.
4. First `compile.py` pass → 7/7 real (no slate), 3840×2160 (THE 4K LAW),
   mean_volume -24.0 dB (GATE AUDIO pass on the first compile).
5. GATE T (`type_check.py`) FAILED on B02 across four consecutive fix
   attempts before the root cause was found — logged in full since the
   failure mode is worth knowing for future beats with bordered-card
   layouts:
   - **Attempt 1** (original layout: card label at top-of-card, traveling
     token sliding into the card's bottom-of-card position): bbox-overlap
     — the label and the token, both inside the same small card, actually
     printed on top of each other on a settled frame. Fixed the real
     overlap (top/bottom margins inside the card).
   - **Attempt 2**: GATE T still FAILED at the *identical* pixel
     coordinates. Root cause: the token's `.animate.move_to()` slide
     between cards passed directly through the label's screen position
     mid-transition, and the checker's sampled frame (fixed at the
     midpoint of the raw Manim clip's duration, per `extract_frame()`)
     landed during that crossing. Switched the slide to a fade-out /
     fade-in at the destination — no continuous translation ever crosses
     another element.
   - **Attempt 3**: GATE T still FAILED, new coordinates. Suspected the
     connector `Arrow` between cards (colored TERRA, sitting in the
     narrow inter-card gap) was merging with adjacent text into one
     blob under the checker's naive connected-component detector. Removed
     the arrows entirely (recolor + fade only) — did not fix it.
   - **Root cause, attempt 4**: read `type_check.py`'s
     `check_bbox_overlap()` / `text_run_bboxes()` directly rather than
     keep guessing from pixel coordinates. The CARD BORDERS themselves
     (INK-colored `RoundedRectangle` strokes, aspect ratio ~4.2, small
     enough that the stroke's pixel count exceeded the "not an empty
     outline" 4%-of-bbox-area filter) were passing the checker's
     "plausible text run" filter. Since the label sits fully inside the
     card, its bbox is 100%-contained in the border's bbox — read as two
     overlapping text runs. This is the same false-positive class the
     checker already documents exemptions for elsewhere ("box border is
     structural, not a text run"), but this scene wasn't on that list.
     Per SKILL.md ("fix content, never the validator") and the hard
     NEVER-LOOSEN-A-VALIDATOR rule, did not touch `type_check.py` or its
     exemption list. Instead recolored B02's card borders from INK to
     TEAL — a color already in this scene's own palette that sits outside
     the checker's INK/MUTE detection range, so the border is invisible
     to the text detector while remaining visible on screen. GATE T →
     PASS, clean, no other changes needed.
   - Also redesigned the token's position from "stacked inside the same
     small card as the label" to "beside the card, off to the right in
     open ground" — belt-and-suspenders: even with TEAL borders, keeping
     two independent text elements in visibly separate zones is the more
     robust pattern for any future small-card beat.
6. Gate V (visual, manual): pulled 26 frames every 4s across the full
   105.25s runtime and read every one directly. B00's correction
   ("judgment" → "the support") lands legibly; B01's struck judgment box
   and lit procedure card read cleanly; B02's four-stop anchor (with the
   traveling "DEC. UTILITY BILL" token beside each card) is legible at
   every step; B03's anchor-return and both-directions split ("cited is
   not correct" / "no draft is not broken") read cleanly, including the
   strike-through on "CORRECT?"; BCRY's carry-out quote, BHTF's Your Turn
   composer card, and BOUT's title outro all render legibly with no
   overlap, no clipping, no contrast issues. No defects found.
7. Audio presence: `ffprobe` + `ffmpeg -af volumedetect` on the final
   master → mean_volume **-24.0 dB**, max -2.8 dB. Master mtime
   (Sep 1 06:20:40) is newer than beat_sheet.json mtime (Sep 1 05:59:37).

**Noted, not a defect introduced here:** `OutroCTA` renders on flat white
rather than the humanitarians cream ground — same shared-component
behavior already logged unremarked in sibling reels in this family (e.g.
`financial-services--claude-liam-3-statement-model`,
`claude-for-legal--claude-liam-handbook-updates`).

**Gates (final state):**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs), fourth pass (B02 border-color root-cause fix above)
- Gate V: PASS, first pass — no defects found
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max
  -2.8 dB
- ffprobe: duration 105.25s; mp4 mtime newer than beat_sheet.json mtime

**Non-blocking warning (compile.py):** motion histogram remotion:4
graphic:3 — remotion at more than half of beats. Structural, not a
defect: hai-simple's mandated shape is B00 (writer) + BCRY + BHTF (Your
Turn) + BOUT (outro) all REMOTION by skill contract, against 3 GRAPHIC
body beats for this 7-beat reel — same disposition as every other short
hai-simple reel in this family.

**Playlist resolution:** family `financial-services` does not match any
prefix key in `skills/make/hai-simple/loop/playlists.json`. Per the map's
documented fallback ("match SUBJECT.json's family, or the hai-simple
prefix"), fell through to matching the skill name itself: `hai-simple` is
a literal key in the map, resolving to **Claude Basics** — same
resolution as the `3-statement-model` sibling reel in this same family.

Metadata file written:
`financial-services--claude-liam-accrual-schedule.md` (channel
@HumanitariansAI, Playlist: **Claude Basics**, plus the direct code link
per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.
