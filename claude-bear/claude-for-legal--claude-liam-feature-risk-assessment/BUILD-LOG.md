# BUILD-LOG — claude-for-legal--claude-liam-feature-risk-assessment

## 2026-08-30 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-for-legal/youtube/claude-liam-feature-risk-assessment/beat_sheet.json`.

**Source-gap finding (logged, not asked — see QUESTION.md for full detail):**
the source sheet is fully "built" (7 beats, all marked VIDEO/filled, dated
2026-08-03) but most of its narration carries literal, never-filled template
placeholders (`>`) at every point where the actual skill-specific fact should
be: `"The skill is feature-risk-assessment. >."`, `"Claude's job: >."`, `"The
SKILL.md is the spec — >."`, `"I want to >."` (B00, B03, BVDT, BHTF). Its
`source_skill` field points at
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/product-legal/skills/feature-risk-assessment/SKILL.md`
— searched the whole `books/` tree on this machine; neither that file nor a
`product-legal` folder exists (identical defect class to most `claude-for-legal--*`
siblings already built in this batch). Unlike several of those siblings, B01
(anatomy) and B02 (pipeline) in THIS source were genuinely authored, not
placeholders — those two facts (one-file SKILL.md instruction set; linear
read-execute-return pipeline) are real and were carried forward. The B00
card's one-line description ("Deeper risk assessment for a single feature or
product area when the...") is itself cut off mid-sentence, but the
un-truncated portion is real and used: a deeper pass, scoped to one feature,
not a broad audit.

**The call:** reconstructed the missing beats (B00's framing, the
wrong-guess, the anchor mechanism, the verdict, the handoff) into a generic,
defensible account of what a scoped feature-risk-assessment actually
returns — a documented checklist write-up, never a safe/unsafe verdict —
illustrated with a generic, uncontroversial anchor (a photo-ID upload
feature; four checklist questions: what, where, how long, who) rather than
inventing this skill's real checklist fields or any legal specifics never
stated by the source.

Register re-registered Teardown -> Plain: the source's B03 framed "Claude's
job" and "what it gets right / where it bites" as a design-tell verdict —
Teardown language, and it was a placeholder anyway. Plain instead states the
mechanism (four boxes: what/where/how-long/who) and both failure directions
(all filled is not safe; one flag is not killed) as properties of any
checklist-driven review, never a verdict on any specific skill's design.
Source's BVDT verdict recap (also a placeholder) folded into a dedicated
BCRY carry-out beat per CARRY-OUT LAW. B00 replaced the source's
`ClaudeComposerAsk` cold open with `BrutalistHesitantWriter` (WRITER LAW:
"approve" -> "assess" — the naive assumption that Claude renders an
approve/reject verdict, corrected to assessing against a fixed checklist).
Close re-skinned to `OutroCTA` / @HumanitariansAI with Liam's sign-off.

Added an anchor (B02 -> B03: the photo-ID card's four checklist boxes, two
blank, then all four filled) and a both-directions beat (B03) per this
factory's PHASE 1 structure requirement — the placeholder portions of the
source carried neither.

## NO-GENAI / NO-PANTRY LAW

All 7 beats are REMOTION (B00 writer, BCRY carry-out, BHTF handoff, BOUT
outro) or GRAPHIC/Manim (B01, B02, B03), all in the humanitarians palette
(`#F3EBDD`/`#2F2A26`/`#E4572E`/`#1F4E5F`). No beat is AI-VIDEO, pantry, or a
human-drop slot.

## Built end to end this invocation

1. `generate_audio_kokoro.py` — 7 beats, free, `am_onyx`. Durations: B00
   10.77s, B01 19.03s, B02 19.43s, B03 19.99s, BCRY 6.55s, BHTF 14.40s,
   BOUT 3.65s.
2. Wrote `scenes.py` (3 Manim scenes, reel-unique names `FRAB01Scene` /
   `FRAB02Scene` / `FRAB03Scene`) and `render_scenes.py`; rendered all three
   in the foreground.
3. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py` in the foreground.
   **One pipeline defect caught and fixed:** the first invocation was wrapped
   in a `timeout 280` shell command (my own harness-timeout workaround); that
   external timeout killed the in-flight `npx remotion render` subprocess for
   BHTF (a 900-frame `--scale=2` composition needing ~3-4 minutes) partway
   through, which `remotion_scenes.py` correctly reported as `FAIL:
   ClaudeComposerAsk` rather than silently leaving a stale file. Caught by
   reading the reported FAIL rather than assuming success; fixed by
   re-invoking `remotion_scenes.py --only BHTF --force` with NO external
   `timeout` wrapper, letting the Bash tool's own long foreground timeout
   (590s) cover the full render — completed clean, `media/BHTF.mp4` 14.4s.
4. B00 verified directly: pulled frames at t=9.0s/10.5s of the 10.8s
   clip — the correction ("approve" -> "assess") is already complete and
   legible, full question reads "Claude, will you assess this new feature?"
5. `compile.py --review` first pass -> 7/7 real (no slate).

## GATE T — three real defects found and fixed, all via direct frame pulls

First `type_check.py` pass: FAIL, 2 findings.

- **B02**: "no text blobs detected" + contrast 3.22:1 < 4.5:1 WCAG. Root
  cause (confirmed by pulling the exact frame GATE T samples, `duration *
  0.5`): (a) "THE ANCHOR" label was colored TERRA on cream — a real WCAG
  contrast fail, same defect class already logged in the `cold-start-interview`
  sibling; (b) that same midpoint landed mid-`FadeIn(card)` (opacity ~60%),
  a genuine mid-transition sample. Fixed by recoloring "THE ANCHOR" (and
  B01's "the quick look never asked" line, which had the identical TERRA-
  on-cream defect) to INK, and by restructuring B02's timing so all motion
  is front-loaded into ~4.2s with a 5.5s stable tail — guaranteeing
  `duration * 0.5` always lands fully settled regardless of small run_time
  drift.
- **B03**: "smallest text run 15px < floor 20px" + "bbox-overlap 100%" +
  kerning gap 12.1x expected. Root cause: the four checklist boxes sat at
  `x=±2.7`, only 0.08 units from the scaled card's edge (`x=±1.47`) — borders
  and text runs were genuinely touching. Fixed by widening box offset to
  `x=±3.7` (real gap, not a false-positive suppression).

Second pass: FAIL, 1 finding (12px min-size at bbox (512-624, 762-794) —
mapped to the left split-card's "SAFE" label). Root cause, confirmed by
direct frame pull at the exact sampled timestamp: a `Line()` strike drawn
across the "SAFE" text — the exact anti-pattern this reel's own `scenes.py`
header comment already warns against ("no thin Line() strikes over text —
recolor text instead"), which splits the glyph run's ink mask into
above/below-the-line fragments, each reading as its own tiny blob. Fixed by
removing the strike entirely and stating the negation directly ("still not
proven safe") instead of striking "SAFE" — same fix class as the
`bar-prep-questions` sibling.

Third pass: FAIL, 1 finding (15px min-size, different bbox — the "documented
is not judged safe" / "flagged is not killed" caption row at font_size 16,
genuinely under the 20px floor for that font/weight). Fixed by bumping all
four B03 caption-row labels from font_size 16 to 20.

Fourth pass (also caught a separate defect en route to Gate V, not a GATE T
finding — GATE T's single fixed sample frame for B03 never happened to land
on it): during the second-pass diagnostic frame pulls, discovered B03's
value-fill animation used a separate `FadeOut(old)+FadeIn(new_val)` pair
where `new_val` was never added to the `boxes` VGroup — so when `group =
VGroup(card, boxes, filled)` later scaled and moved, the filled-in values
("90 days" / "support staff") stayed behind at full size while the boxes
shrank, and the original (opacity-faded, not removed) "—" reappeared once
the new value's independent FadeIn had nothing anchoring it to the group.
Fixed by replacing the FadeOut+FadeIn pair with a single in-place
`Transform(boxes[i][1][1], new_val)` so one persistent mobject carries
through every subsequent transform. Re-rendered with `--disable_caching` to
rule out any stale partial-movie-file reuse across edits.

GATE T PASS 0 FAILs after all four passes.

## Gate V (manual frame QC — caught one real defect GATE T's single sample missed)

Pulled frames at 8s intervals across the full 94.8s runtime plus targeted
pulls. Found B01's "LOOKS FINE" stamp centered directly on top of the
feature card's own "PHOTO ID UPLOAD" / "age verification" text (both were
centered at the same point by construction) — a genuine overlap that GATE T's
bbox-overlap check didn't happen to flag at its one sampled frame for B01.
Fixed by offsetting the stamp `DOWN * 0.75` within the card, clear of the
title text. Re-rendered, recompiled, re-ran GATE T (still PASS, no
regression), re-pulled all 13 frames — all legible, no overlap, correct
@HumanitariansAI skin on BHTF/BOUT.

**Noted, not a defect introduced here:** `OutroCTA` renders on flat white
rather than the humanitarians cream ground — same shared-component behavior
already logged unremarked in sibling reels in this family (e.g.
`claude-for-legal--claude-liam-ai-tool-handoff`).

## Gates

- **TIMING LAW (B00):** narration 35 words + `lead_silence_s` 0.8 ->
  measured `actual_duration_s` **10.77s**, clears the >=8s floor (compiled
  clip 10.8s). Correction ("approve" -> "assess") fully legible by t=9.0s.
- **content-check / frame-check / lane-check:** all PASS per `compile.py`
  output (7/7 beats, no violations, canvas 3840x2160).
- **GATE T (type_check.py):** PASS — 0 FAILs after four fix passes (see
  above).
- **Gate V (frame QC):** 13 frames at 8s spacing across the full 94.8s
  runtime, all legible, safe inset respected, no text overlap after the B01
  stamp fix.
- **GATE AUDIO:** PASS, mean_volume **-24.0 dB** (ffmpeg volumedetect,
  independently verified, well above the -40 dB floor), max -2.9 dB.
- ffprobe: master duration 94.833s; slate mp4 mtime (1788076381) newer than
  beat_sheet.json mtime (1788075248).

**Non-blocking note (compile.py motion histogram):** remotion:4 graphic:3 —
same structural disposition as every other short hai-simple reel in this
family (B00/BCRY/BHTF/BOUT are REMOTION by skill contract; 3 GRAPHIC body
beats).

## Playlist resolution

`SUBJECT.json`'s `family: "claude-for-legal"` has no literal entry in
`skills/make/hai-simple/loop/playlists.json`'s map (verified directly against
the map file). Per the map's documented fallback, fell through to the skill
name itself: `hai-simple` is a literal key in the map, resolving to
**Claude Basics** — same resolution as every other delivered
`claude-for-legal--*` sibling in this family.

Metadata file written:
`claude-for-legal--claude-liam-feature-risk-assessment.md` (channel
@HumanitariansAI, Playlist: **Claude Basics**, plus the direct code link per
the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.

## 2026-08-30 — Phase 4 delivery

`compile.py` (no `--review`) forces THE 4K LAW automatically — wrote
`claude-for-legal--claude-liam-feature-risk-assessment.mp4` natively at
3840x2160, 94.8s, 7/7 beats real, mean_volume -24.0 dB. Copied to
`claude-for-legal--claude-liam-feature-risk-assessment-4k.mp4` so
`deliver.py`'s `newest_master()` picks it as the explicit 4K variant.

```
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Outbox staged:
`DELIVERY/claude-for-legal--claude-liam-feature-risk-assessment/` (4K mp4 +
description.md, syncs to Drive `Claude_Bear/` on this machine's
Drive-for-desktop mount). Repo:
`humanitarians-youtube/claude-bear/claude-for-legal--claude-liam-feature-risk-assessment/`
(README.md, beat_sheet.json, SCRIPT.md, SUBJECT.json, BUILD-LOG.md,
CARRY-OUT.md, QUESTION.md — no media). Commit `4292b5b2`.

**Status: DELIVERED.** Both delivery targets staged/pushed. Reel complete.
