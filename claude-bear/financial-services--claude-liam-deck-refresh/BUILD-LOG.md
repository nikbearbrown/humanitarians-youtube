# BUILD-LOG — financial-services--claude-liam-deck-refresh

## 2026-09-01 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/financial-services/youtube/claude-liam-deck-refresh/beat_sheet.json`
(examining the Anthropic `deck-refresh` skill: updates a presentation with
new numbers — quarterly refreshes, earnings updates, comp rolls, rebased
market data; triggers on "update the deck with Q4 numbers", "refresh the
comps", "roll this forward", "swap in the new earnings", or literally
"change all the $485M to $512M"; anatomy = one-file SKILL.md instruction
set; pipeline = read→execute→return, linear, no branching unless a step
says so).

**Source-gap finding (logged, not asked — see QUESTION.md for full
detail):** the source sheet's narration is NOT an unfilled placeholder —
it already states the skill's real function and, unusually, its own
worked example verbatim ($485M → $512M). The `source_skill` path it names
(`/Users/bear/Documents/CoWork/bear-textbooks/.../pitch-agent/skills/deck-refresh/SKILL.md`)
does not exist on this machine (different machine's home directory), but
no reconstruction was needed — the source beat_sheet.json's own narration
and worked example carried enough to redo faithfully.

**The call:** register re-registered Teardown → Plain. Source's B03 framed
"what it gets right / what it bites" as a design-tell verdict — Teardown
language. Plain instead states the mechanism (a linear find-and-replace
over the deck) and its two failure directions (a changed figure is not a
re-checked sentence; a leftover figure is not always a miss) as properties
of the practice, never a verdict on the skill's design. Source's BVDT
verdict recap folded into a dedicated BCRY carry-out beat per CARRY-OUT
LAW. B00 replaced the source's `ClaudeComposerAsk` cold open (itself
already Remotion, not AI-video/puppet — no NO-GENAI violation in the
source) with `BrutalistHesitantWriter` per WRITER LAW: "story" → "numbers"
— the naive assumption that a "refresh" touches the deck's narrative,
corrected to: it touches the numbers only. Added a wrong-guess beat (B01:
reconsidering the story vs. a fixed find-and-replace, falsified by "ask it
to also rewrite the sentence built around that number, and it won't") and
literalized the source's own worked example as the anchor (B02 → B03:
$485M appearing on three slides — executive summary, comps table,
footnote — swapped in slide order to $512M, then split into the two
both-directions cautions) per this factory's PHASE 1 structure requirement
— the source's Teardown shape (anatomy / pipeline / design-tell / verdict)
carried neither. Close re-skinned to `OutroCTA` / @HumanitariansAI with
Liam's sign-off. Kept the source's 7-beat count (B00, B01, B02, B03, BCRY,
BHTF, BOUT) per the redo contract.

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 7 beats, free, `am_onyx`, first pass, no
   retries. B00 landed at 10.73s (clear of the ≥9s TIMING LAW floor) on
   the first narration draft (33 words + `lead_silence_s: 0.8`). Durations:
   B00 10.73s, B01 19.61s, B02 17.49s, B03 21.46s, BCRY 7.87s, BHTF 18.18s,
   BOUT 3.58s (+1.0s tail).
2. Verified B00's correction on frame pulls at t=6.5/9.5/10.3s: "story"
   still mid-typing (accent color) at 6.5s, fully backspaced and replaced
   with "the numbers?" by 9.5s, legible with margin before the 10.7s
   cutoff. TIMING LAW satisfied on the first pass — no rewrite needed.
3. Wrote `scenes.py` (3 Manim scenes, reel-unique names `DRB01Scene` /
   `DRB02Scene` / `DRB03Scene`) and `render_scenes.py`; rendered all three
   in the foreground, no render failures at any point.
4. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py`; the shell moved
   it to a background task past the 120s inline timeout — blocked on it
   with `TaskOutput` rather than ending the turn, per the one-shot
   COMPLETION LAW. Exit 0, all four beats rendered clean on the first pass
   (B00 extended to 10.7s, BCRY to 7.9s, BHTF to 18.2s, BOUT to 3.6s).
5. First `compile.py` pass → 7/7 real (no slate), native 3840×2160 (THE 4K
   LAW), GATE AUDIO mean_volume -24.1 dB inline.
6. GATE T (`type_check.py`) FAILED on the first pass: 1 pixel beat. B02's
   three slide-card labels ("EXECUTIVE SUMMARY" / "COMPS TABLE" /
   "FOOTNOTE") were set at font_size 15, under the 20px/1080p-logical
   floor. Fixed by bumping all three to font_size 18 (via `_fit_text` for
   the longest label, to guard against card overflow), re-rendered B02
   only, recompiled: GATE T → PASS, 0 FAILs, second pass.
7. Gate V (visual, manual): pulled 25 frames at 4s spacing across the full
   99.9s runtime and read every one directly. All legible, correct
   content, no clipping or overlap, correct anchor payoff (B02→B03 $485M
   → $512M composition), correct carry-out/handoff/outro with
   `@HumanitariansAI` branding. Noted, not a defect introduced here: the
   card labels in B01/B02/B03 (e.g. "RECONSIDER THE STORY", "COMPS
   TABLE") render with the inter-word space collapsed under this
   environment's SANS/Montserrat bold-caps Text() rendering — confirmed
   this is a pre-existing, systemic pipeline quirk by pulling a frame from
   the already-delivered `financial-services--claude-liam-3-statement-model`
   sibling, where "ANALYST JUDGMENT" renders identically as
   "ANALYSTJUDGMENT". Words stay parseable (case boundaries visible); not
   blocking. Also noted, same as every other `financial-services` sibling:
   `OutroCTA` renders on flat white rather than the humanitarians cream
   ground — same shared-component behavior already logged unremarked
   elsewhere in this family.
8. Audio presence: `ffprobe` + `ffmpeg -af volumedetect` on the final
   master → mean_volume **-24.1 dB**, max -2.8 dB. Master mtime
   (1788290670) is newer than beat_sheet.json mtime (1788290426).

**Gates (final state):**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs), second pass (B02 font-size fix above)
- Gate V: PASS, first pass — no defects requiring a fix (see noted,
  not-a-defect items above)
- GATE AUDIO: PASS — mean_volume **-24.1 dB** (ffmpeg volumedetect), max
  -2.8 dB
- ffprobe: duration 99.94s; mp4 mtime newer than beat_sheet.json mtime

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
resolution as every other `financial-services--*` sibling.

Metadata file written: `financial-services--claude-liam-deck-refresh.md`
(channel @HumanitariansAI, Playlist: **Claude Basics**, plus the direct
code link per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate (after the one fix
pass above). Proceeding to Phase 4 (4K render + deliver.py) in this same
invocation.

## 2026-09-01 — Phase 4 delivery

Master is already 3840×2160 (THE 4K LAW in compile.py forces any clean,
non-`--review` master to 4K), so the Fellows-facing 4K file is the same
render, copied to the `-4k` filename `deliver.py` expects:

```
cp financial-services--claude-liam-deck-refresh.mp4 \
   financial-services--claude-liam-deck-refresh-4k.mp4
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Outbox staged: `DELIVERY/financial-services--claude-liam-deck-refresh/`
(4K mp4 + description.md). Repo: committed + pushed to
`humanitarians-youtube/claude-bear/financial-services--claude-liam-deck-refresh/`
(README.md, beat_sheet.json, SCRIPT.md, SUBJECT.json, BUILD-LOG.md,
CARRY-OUT.md, QUESTION.md — no mp3/mp4), commit `fa2e0b9d`.

**Status: DELIVERED.** Both delivery targets staged/pushed. Reel complete.
