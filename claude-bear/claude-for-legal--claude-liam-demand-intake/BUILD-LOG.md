# BUILD-LOG — claude-for-legal--claude-liam-demand-intake

## 2026-08-29 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-for-legal/youtube/claude-liam-demand-intake/beat_sheet.json`.

**Source note:** unlike the sibling `amendment-history`/`ai-inventory` redos
in this family, this source sheet's narration is **actually filled in** — no
unfilled `>` template placeholders. It states real facts: `demand-intake` is
"pre-drafting context gathering for a demand letter — parties, facts, basis,
leverage, BATNA, and privilege filters — written to a structured intake.md
the demand-draft skill reads." The named `source_skill` file
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/litigation-legal/skills/demand-intake/SKILL.md`)
does not exist on this machine (searched the whole `books/` tree — no
`demand-intake` SKILL.md, no `litigation-legal` folder), but that did not
block this redo the way it blocked `amendment-history`: the facts needed were
already sitting in the source's own narration, not missing from it. No fact
in this script was invented; see QUESTION.md.

Kept the source's 7-beat shape (cold open, anatomy, pipeline, design tell,
verdict, handoff, outro) and its question/facts/argument. Changes per
hai-simple's redo contract:

- B00 replaced the source's `ClaudeComposerAsk` cold open with
  `BrutalistHesitantWriter` (WRITER LAW): types "Can Claude just write my
  demand letter?", hesitates on "write", corrects to "prep for" — the
  newcomer's actual wrong guess (that you can just ask Claude to write the
  letter directly) corrected toward the real question (what does Claude need
  to prep for it).
- Register re-registered Teardown -> Plain: the source's B03 framed "Claude's
  job" and "what it gets right / where it bites" as a design-tell verdict —
  Teardown language. Plain instead states the six-question intake mechanism
  and its failure modes (a fact nobody mentions never makes it in; intake
  never drafts the letter itself) as properties of the pre-drafting step,
  never a verdict on the skill's design.
- Source's BVDT verdict recap folded into a dedicated BCRY carry-out beat per
  CARRY-OUT LAW (same disposition as prior redos in this factory).
- Close re-skinned to `OutroCTA` / @HumanitariansAI with Liam's sign-off.
- Added an anchor (B02 -> B03: an unpaid $40,000 invoice, 60 days late,
  resolved once all six intake questions are answered) and a both-directions
  beat (B03) per this factory's PHASE 1 structure requirement — the source's
  short Teardown beats carried neither.
- Handoff prompt (BHTF) is a real, generalizable Claude prompt a viewer can
  run today without the actual internal Anthropic skill installed (asks
  Claude to gather the six intake facts before drafting), rather than the
  source's "read the demand-intake skill" instruction, which assumes access
  to a file that doesn't exist on this machine.

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 7 beats, free, `am_onyx`. Durations: B00
   10.39s, B01 16.02s, B02 17.11s, B03 18.69s, BCRY 10.65s, BHTF 15.19s,
   BOUT 3.26s.
2. Wrote `scenes.py` (3 Manim scenes, reel-unique names `DIB01Scene` /
   `DIB02Scene` / `DIB03Scene`) and `render_scenes.py`; rendered all three in
   the foreground.
3. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py`; the process exceeded
   the shell tool's 120s inline timeout and was moved to a tracked background
   job mid-run. Per the COMPLETION LAW for one-shot invocations, blocked on
   `TaskOutput(task_id, block=true)` in the foreground rather than ending the
   turn — confirmed exit code 0 (all 4 beats ok) before proceeding.
4. B00 verified directly: `media/B00.mp4` = 10.4s (meets the >=8s TIMING LAW
   floor, clears the >=9s narration-window target). Pulled a frame at t=9s:
   the correction ("write"->"prep for") is complete and the full final
   question ("Can Claude just prep for my demand letter?") is legible.
5. First `compile.py` pass -> 7/7 real (no slate), 3840x2160 (THE 4K LAW),
   mean_volume -23.9 dB (already passing GATE AUDIO).

**GATE T (type_check.py) — one real finding, fixed (not a false positive):**

- First pass: FAIL (1 pixel beat, kerning). B02's mid-clip sample frame
  (t=dur*0.5 of the raw `manim/B02.mp4`) measured a max inter-glyph gap of
  78px against a 12px threshold on the title row "THE ANCHOR — THE SIX
  QUESTIONS" — reproduced the checker's own gap-measurement algorithm
  directly against the sampled frame and confirmed the finding is real: 9 of
  30 measured inter-run gaps (30%, at the fail threshold) exceeded the
  12px cutoff, driven by the em dash ("—") producing a genuinely isolated
  78px gap plus several ordinary word-spacing gaps in the 14-22px range at
  this small font size (26px design units on a 1080p raw Manim render).
  Fixed by simplifying the title to "THE SIX QUESTIONS" (dropping the
  "THE ANCHOR — " prefix and its em dash) — the anchor concept is already
  conveyed by the beat's mechanic (the invoice card returning at B03), so
  nothing pedagogical was lost.
- Second pass: **PASS (0 FAILs)**.

**Gate V (visual) — clean, no defects found:**

Pulled frames every 5s across the full 92.3s runtime (18 frames) plus a
targeted frame from the BOUT segment (the 5s sampling interval landed on
BHTF twice and skipped past BOUT). All 7 beats read legibly: B00's writer
card shows the full naive framing then the completed "write"->"prep for"
correction with the final question intact; B01's blank-fields demand-letter
card and "it can only guess" caption are clean; B02's six-question checklist
and invoice anchor card ($40,000, 60 days late) are legible with normal
word/letter spacing after the GATE T fix; B03's anchor payoff (invoice card
collapsing into "GROUND TO STAND ON") and both-directions split ("a fact
nobody mentions -> never makes it in" / "this step never drafts -> hands a
finished file onward" with the dashed line to "draft step") read cleanly
with no overlap; BCRY's carry-out quote and BHTF's Your Turn composer card
(paste-ready prompt, `@HumanitariansAI` folder label) are both clean; BOUT's
title-restate line and subscribe/@HumanitariansAI row are legible.

**Noted, not a defect introduced here:** `OutroCTA` renders on flat white
rather than the humanitarians cream ground — same shared-component behavior
already logged unremarked in sibling reels in this family (e.g.
`claude-for-legal--claude-liam-amendment-history`).

**Gates (final state):**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840x2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs) after fixing the confirmed kerning-threshold defect
  above
- Gate V: PASS — no defects found, no fixes needed
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (ffmpeg volumedetect), max
  -3.0 dB
- ffprobe: duration 92.317s, 3840x2160; mp4 mtime (1788050130) newer than
  beat_sheet.json mtime (1788049731)

**Non-blocking note (compile.py):** B01/B02/B03 Manim clips (6.9-9.4s raw)
were slowed 1.99x-2.32x to fill their 16.0-18.7s narration windows — under
compile.py's own 3.0x "extreme slow-mo" warning threshold, so not flagged as
a defect by the tool itself; noted here for visibility.

**Motion histogram:** remotion:4 graphic:3 — structural, not a defect:
hai-simple's mandated shape is B00 (writer) + BCRY + BHTF (Your Turn) + BOUT
(outro) all REMOTION by skill contract, against 3 GRAPHIC body beats for this
7-beat reel — same disposition as every other short hai-simple reel in this
family.

**Playlist resolution:** family `claude-for-legal` does not match any prefix
key in `skills/make/hai-simple/loop/playlists.json`. Per the map's documented
fallback ("match SUBJECT.json's family, or the hai-simple prefix"), fell
through to matching the skill name itself: `hai-simple` is a literal key in
the map, resolving to **Claude Basics** — same resolution as the sibling
`claude-for-legal--claude-liam-amendment-history` redo.

Metadata file written: `claude-for-legal--claude-liam-demand-intake.md`
(channel @HumanitariansAI, Playlist: **Claude Basics**, plus the direct code
link per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.
