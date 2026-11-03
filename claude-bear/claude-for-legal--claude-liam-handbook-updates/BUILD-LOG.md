# BUILD-LOG — claude-for-legal--claude-liam-handbook-updates

## 2026-08-30 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-for-legal/youtube/claude-liam-handbook-updates/beat_sheet.json`.

**Source-gap finding (logged, not asked — see QUESTION.md for full detail):**
the source sheet is fully "built" (7 beats, all marked VIDEO/filled, dated
2026-07-25) but its narration text carries literal, never-filled template
placeholders (`>`) at every point where the actual skill-specific fact
should be: `"the skill is handbook-updates. >."`, `"Claude's job: >."`,
`"The SKILL.md is the spec — >."`, `"I want to >."` Its `source_skill`
field points at
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/employment-legal/skills/handbook-updates/SKILL.md`
— searched the entire `books/` tree on this machine; neither that file nor
an `employment-legal` folder exists anywhere. So there were no real facts
to carry over from the source, only a topic (HANDBOOK-UPDATES, an
Anthropic skill for employment-law handbook maintenance) and a shape
(Teardown skill-teardown format, 7 beats: cold open, anatomy, pipeline,
design tell, verdict, handoff, outro). Same pattern, same disposition, as
this factory's prior `claude-for-legal--claude-liam-ai-inventory` redo.

**The call:** rather than block on a missing human answer, reconstructed
the evident subject into a generic, defensible account of what "keeping a
handbook updated" actually means and why the naive approach (review it
once a year) misses the point — described generically per the fresh-script
Phase 1 rule ("when in doubt, describe behavior generically") rather than
inventing specific tool names, UI, or product claims. No fact in the
resulting script is Claude-specific or unverifiable.

Register re-registered Teardown -> Plain: the source's B03 framed
"Claude's job" and "what it gets right / where it bites" as a design-tell
verdict — Teardown language. Plain instead states the mechanism (a
trigger-based update: law change -> flagged section -> drafted fix ->
logged amendment) and its failure modes (flagged is not final; quiet is
not complete) as properties of the practice, never a verdict on any
specific skill's design. Source's BVDT verdict recap folded into a
dedicated BCRY carry-out beat per CARRY-OUT LAW. B00 replaced the source's
`ClaudeComposerAsk` cold open with `BrutalistHesitantWriter` (WRITER LAW:
"calendar" -> "law" — the naive assumption that a handbook update is
scheduled, corrected to the fact that it's triggered by a legal change).
Close re-skinned to `OutroCTA` / @HumanitariansAI with Liam's sign-off.
Added an anchor (B02 -> B03: a spring paid-leave minimum increase that
touches exactly one section, then logged with a dated amendment record)
and a both-directions beat (B03) per this factory's PHASE 1 structure
requirement — the source (being unfilled) carried neither.

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 7 beats, free, `am_onyx`. Initial B00 pass
   (25-word narration) produced only 7.98s of audio — too short: the
   `BrutalistHesitantWriter` composition's fixed 606-frame (20.2s @30fps)
   render gets TRIMMED to `actual_duration_s` by `remotion_scenes.py`'s
   `extend_clip_to_duration` (`ffmpeg -t <duration_s>`), which cuts the
   typing performance off wherever it happens to be at that timestamp —
   not a freeze-frame extension in this direction, a hard trim. At 7.98s /
   8.0s the correction ("calendar" -> "law") had not yet started
   (confirmed by pulling frames at t=6.5/7.0/7.5/7.9/8.0s — all showed
   "the calendar" still in accent color, mid-typing, never backspaced).
   Rewrote B00's narration to 32 words (within the 20-35 word TIMING LAW
   band) to push Kokoro's output to 9.22s, matching the ai-inventory
   sibling reel's successful ballpark (30 words -> 9.94s). Re-rendered B00
   with `--force`; pulled frames at t=8.5/9.0/9.1s — "the calendar" fully
   backspaced and replaced with "the law?" by t=9.0s, legible with margin
   before the 9.2s cutoff. TIMING LAW satisfied. Final durations: B00
   9.22s, B01 15.91s, B02 14.74s, B03 19.88s, BCRY 9.13s, BHTF 17.64s,
   BOUT 3.58s.
2. Wrote `scenes.py` (3 Manim scenes, reel-unique names `HBUB01Scene` /
   `HBUB02Scene` / `HBUB03Scene`) and `render_scenes.py`; rendered all
   three in the foreground on the first pass, no failures.
3. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py` in the foreground
   (full run, then a `--only B00 --force` re-run after the narration
   rewrite above) — both runs completed within the shell's inline timeout,
   no background job needed this time.
4. First `compile.py` pass -> 7/7 real (no slate), 3840x2160 (THE 4K LAW),
   mean_volume -24.0 dB (passing GATE AUDIO on the first compile).
5. GATE T (`type_check.py`): **PASS, 0 FAILs, first pass** — no kerning
   exemptions needed for this reel's titles.
6. Gate V (visual): pulled frames every 4s across the full 91.1s runtime
   (23 frames) plus targeted mid-animation frames for B01/B02/B03, and
   read every one directly. All clean: no text overflow, no bbox overlap,
   safe inset respected throughout. B00's correction lands and is fully
   legible before the beat ends (see step 1). Zero defects found — no
   fixes needed this pass.

**Noted, not a defect introduced here:** `OutroCTA` renders on flat white
rather than the humanitarians cream ground — same shared-component
behavior already logged unremarked in sibling reels in this family (e.g.
`claude-for-legal--claude-liam-ai-inventory`, `claude-code--claude-liam-writing-rules`).

**Gates (final state):**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840x2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs), first pass
- Gate V: PASS, first pass — no defects found
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max
  -2.9 dB
- ffprobe: duration 91.117s; mp4 mtime (1788084596) newer than
  beat_sheet.json mtime (1788084490)

**Non-blocking warning (compile.py):** motion histogram remotion:4
graphic:3 — remotion at more than half of beats. Structural, not a defect:
hai-simple's mandated shape is B00 (writer) + BCRY + BHTF (Your Turn) +
BOUT (outro) all REMOTION by skill contract, against 3 GRAPHIC body beats
for this 7-beat reel — same disposition as every other short hai-simple
reel in this family.

**Playlist resolution:** family `claude-for-legal` does not match any
prefix key in `skills/make/hai-simple/loop/playlists.json`. Per the map's
documented fallback ("match SUBJECT.json's family, or the hai-simple
prefix"), fell through to matching the skill name itself: `hai-simple` is
a literal key in the map, resolving to **Claude Basics** — same resolution
as the `ai-inventory` sibling reel.

Metadata file written:
`claude-for-legal--claude-liam-handbook-updates.md` (channel
@HumanitariansAI, Playlist: **Claude Basics**, plus the direct code link
per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate on the first
compile pass (after the B00 narration-length fix). Proceeding to Phase 4
(4K render + deliver.py) in this same invocation.

## 2026-08-30 — Phase 4 delivery

Master is already 3840x2160 (THE 4K LAW in compile.py forces any clean,
non-`--review` master to 4K), so the Fellows-facing 4K file is the same
render, copied to the `-4k` filename `deliver.py` expects:

```
cp claude-for-legal--claude-liam-handbook-updates.mp4 \
   claude-for-legal--claude-liam-handbook-updates-4k.mp4
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

See below for the outcome of this step.
