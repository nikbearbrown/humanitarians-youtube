# BUILD-LOG — claude-for-legal--claude-liam-comments

## 2026-08-29 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-for-legal/youtube/claude-liam-comments/beat_sheet.json`.

**Source-gap finding (logged, not asked — see QUESTION.md for full detail):**
the source sheet's `source_skill` field points at
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/regulatory-legal/skills/comments/SKILL.md`
— searched the whole `books/` tree on this machine; no `regulatory-legal`
folder exists anywhere under `claude-for-legal`, same missing-source-file
class already logged for sibling redos in this family
(`claude-for-legal--claude-liam-amendment-history`,
`claude-for-legal--claude-liam-ai-inventory`). **Unlike those siblings,
this source sheet is NOT a placeholder shell** — its narration carries
real, specific facts: the `comments` skill reviews open NPRM (Notice of
Proposed Rulemaking) comment periods, logs decisions, tracks deadlines,
and records a filing / not-filing / waived decision via a `--decide
CMT-ID` flag. So this redo lifts those facts directly rather than
reconstructing a generic account from just the title, as the
placeholder-shell siblings required.

**The call:** kept the source's question, facts, and 7-beat shape (cold
open, anatomy, pipeline, design tell, verdict, handoff, outro), folding
the source's BVDT verdict recap into a dedicated BCRY carry-out beat (same
disposition as prior redos in this factory). Register re-registered
Teardown -> Plain: the source's B03 framed "Claude's job" and "what it
gets right / what it bites" as a design-tell verdict; Plain instead states
the mechanism (a skill logs what it's told; the filing decision stays
human) and its two failure directions (a decision logged on time doesn't
prove the comment was good; an unlogged decision doesn't prove it was
missed), never a verdict on the skill's own design. B00 replaced the
source's `ClaudeComposerAsk` cold open with `BrutalistHesitantWriter`
(WRITER LAW: "know" -> "track" — the naive assumption that Claude already
knows which comment deadlines are due on its own, corrected to the fact
that it only tracks what a skill tells it to track). Close re-skinned to
`OutroCTA` / @HumanitariansAI with Liam's sign-off. Added an anchor (B02
-> B03: a proposed rule opening its comment window March 2nd, a sixty-day
clock, resolved to filed on day 59) and a both-directions beat (B03) per
this factory's PHASE 1 structure requirement — the source's Teardown shape
carried neither.

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 7 beats, free, `am_onyx`. Durations: B00
   10.62s, B01 20.93s, B02 20.05s, B03 22.08s, BCRY 9.45s, BHTF 14.17s,
   BOUT 2.77s.
2. Wrote `scenes.py` (3 Manim scenes, reel-unique names `CMTB01Scene` /
   `CMTB02Scene` / `CMTB03Scene`) and `render_scenes.py`; rendered all
   three in the foreground — TERRA restricted to borders/rings from the
   start (never on legibility-critical text), per the contrast lesson
   already logged on the sibling `amendment-history` redo.
3. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py`; the process
   exceeded the shell tool's 120s inline timeout and was moved to a
   tracked background job mid-run. Per the COMPLETION LAW for one-shot
   invocations, blocked on `TaskOutput(task_id, block=true)` in the
   foreground rather than ending the turn — confirmed exit code 0 (all 4
   beats ok) before proceeding.
4. B00 verified directly: `media/B00.mp4` = 10.63s (meets the >=8s TIMING
   LAW floor, and clears the >=9s narration-window target). Pulled a frame
   at t=9s: the correction ("know"->"track") is complete and the full
   final question is legible.
5. First `compile.py` pass -> 7/7 real (no slate), 3840x2160 (THE 4K LAW),
   mean_volume -24.1 dB (already passing GATE AUDIO).

**GATE T (type_check.py) — one real finding, fixed (not a false positive):**

- First pass: FAIL (1 pixel beat, B03). "no text-run blobs above noise
  threshold — the filter discarded every candidate" at the checker's
  mid-clip sample frame (t=dur*0.5 of the raw `manim/B03.mp4`, t≈3.92s of
  7.83s). Traced the frame directly: at that instant the "MAR 2 RULE"
  card, countdown ring, and title had just finished fading out, and the
  only surviving element — the "FILED" stamp — had just been scaled to
  0.65x and moved as part of the same transition, shrinking its
  originally font_size=20 text below the ~20px (1.9% frame-height) floor
  at the manim clip's native resolution. Confirmed by pulling the exact
  frame and reading it: "FILED" was legible to the eye but small relative
  to the other passing beats' text. Fixed by increasing the stamp's
  `Text("FILED", ...)` font_size from 20 to 32 and reducing the
  post-transition shrink from `scale(0.65)` to `scale(0.85)` (effective
  ~27px, comfortable margin over the ~20px floor, similar ratio to the
  passing B02 min-size reading of 23/20). Re-rendered B03 only (B01/B02
  untouched), recompiled.
- Second pass: **PASS (0 FAILs)**.

**Gate V (visual) — 20 frames pulled at 5s intervals across the full
101.1s runtime, read directly:** all beats legible, correct contrast, safe
inset respected, no text overlap. B00's `BrutalistHesitantWriter` shows
the "know"->"track" correction landing cleanly. B01's docket-watching
assumption card dims and the two fact-chips slide past without touching
it, as designed. B02's SKILL.md-unfurls-to-three-instructions beat and
the "RULE OPENS · MAR 2" / "60 DAYS" anchor read cleanly. B03's anchor
payoff (ring fills to "DAY 59", "FILED" stamp locks in, now comfortably
legible after the GATE T fix) and its both-directions split
("logged ≠ good" / "not logged ≠ missed") are both clean. BCRY's
`WantQuote` carry-out and BHTF's `ClaudeComposerAsk` Your Turn card are
clean. BOUT's `OutroCTA` renders on flat white rather than the
humanitarians cream ground — same shared-component behavior already
logged unremarked in sibling reels in this family (e.g.
`claude-for-legal--claude-liam-amendment-history`); not a defect
introduced here.

**Gates (final state):**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840x2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs) after fixing the confirmed B03 min-size defect
  above
- Gate V: PASS (20 frames across full runtime, read directly)
- GATE AUDIO: PASS — mean_volume **-24.1 dB** (ffmpeg volumedetect), max
  -3.0 dB (floor is -40 dB; comfortably clear)
- ffprobe: duration 101.082s, 3840x2160; mp4 mtime (1788040748) newer
  than beat_sheet.json mtime (1788040399)

**Non-blocking note (compile.py):** B01/B02/B03 Manim clips (8.9-10.0s
raw) were slowed 2.10x-2.82x to fill their 20.1-22.1s narration windows —
under compile.py's own 3.0x "extreme slow-mo" warning threshold (not
flagged by the tool), noted here for visibility.

**Motion histogram:** remotion:4 graphic:3 — remotion at more than half of
beats. Structural, not a defect: hai-simple's mandated shape is B00
(writer) + BCRY + BHTF (Your Turn) + BOUT (outro) all REMOTION by skill
contract, against 3 GRAPHIC body beats for this 7-beat reel — same
disposition as every other short hai-simple reel in this family.

**Playlist resolution:** family `claude-for-legal` does not match any
prefix key in `skills/make/hai-simple/loop/playlists.json`. Per the map's
documented fallback ("match SUBJECT.json's family, or the hai-simple
prefix"), fell through to matching the skill name itself: `hai-simple` is
a literal key in the map, resolving to **Claude Basics** — same
resolution as sibling redos in this family.

Metadata file written:
`claude-for-legal--claude-liam-comments.md` (channel @HumanitariansAI,
Playlist: **Claude Basics**, plus the direct code link per the DELIVERY
CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.

---

## Phase 4 — delivery

`compile.py`'s non-review invocation already renders under THE 4K LAW
(clean masters are forced to 3840x2160 unless `--review` is passed), so
`claude-for-legal--claude-liam-comments.mp4` IS the 4K master — confirmed
3840x2160 via ffprobe above. Copied it to
`claude-for-legal--claude-liam-comments-4k.mp4` so `deliver.py`'s
`newest_master()` picks the explicit 4K name first.

```
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Staged `DELIVERY/claude-for-legal--claude-liam-comments/` (4K master +
description) and committed the text artifacts (README.md = description,
beat_sheet.json, SCRIPT.md, SUBJECT.json, BUILD-LOG.md, CARRY-OUT.md,
QUESTION.md, TYPECHECK.md) to
`humanitarians-youtube/claude-bear/claude-for-legal--claude-liam-comments/`
— no mp3/mp4 in the repo copy, per the hard guard in `deliver.py`.

**Status: DELIVERED.**
