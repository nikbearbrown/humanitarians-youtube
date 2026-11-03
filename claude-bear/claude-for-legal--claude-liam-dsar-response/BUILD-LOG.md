# BUILD-LOG — claude-for-legal--claude-liam-dsar-response

## 2026-08-30 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-for-legal/youtube/claude-liam-dsar-response/beat_sheet.json`.

**Source-gap finding (logged, not asked — see QUESTION.md for full detail):**
the source sheet is fully "built" (7 beats, all marked VIDEO/filled, dated
2026-07-25) but its narration text carries literal, never-filled template
placeholders (`>`) at every point where the actual skill-specific fact
should be: `"The skill is dsar-response. >."`, `"Claude's job: >."`, `"The
SKILL.md is the spec — >."`, `"I want to >."`. Its `source_skill` field
points at
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/privacy-legal/skills/dsar-response/SKILL.md`
— searched the entire `books/` tree on this machine; neither that file nor
a `privacy-legal` folder exists anywhere. Same source-gap pattern already
logged for the sibling `claude-for-legal--claude-liam-amendment-history` /
`-ai-inventory` / `-ai-tool-handoff` / `-aia-generation` / `-board-minutes`
redos in this same family. So there were no real facts to carry over from
the source, only a topic (DSAR RESPONSE, a privacy-legal Anthropic skill)
and a shape (Teardown skill-teardown format, 7 beats: cold open, anatomy,
pipeline, design tell, verdict, handoff, outro).

**The call:** rather than block on a missing human answer, reconstructed
the evident subject into a generic, defensible account of what responding
to a Data Subject Access Request actually requires — a person asks what
personal data an organization holds on them, the organization must search
every system that could hold a record under every identifier the person
has used, and must ship back only that person's data, not anyone else's
mixed into the same record — described generically per the fresh-script
Phase 1 rule ("when in doubt, describe behavior generically") rather than
inventing specific tool names, UI, or product claims. No fact in the
resulting script is Claude-specific or unverifiable.

Register re-registered Teardown -> Plain: the source's B03 framed
"Claude's job" and "what it gets right / where it bites" as a design-tell
verdict — Teardown language. Plain instead states the mechanism
(search-every-system-under-every-identifier) and its failure modes (a
no-hit under one identifier isn't a no-data finding; a hit isn't
automatically ready to ship) as properties of a DSAR response, never a
verdict on any specific skill's design. Source's BVDT verdict recap folded
into a dedicated BCRY carry-out beat per CARRY-OUT LAW (same disposition
as prior redos in this factory). B00 replaced the source's
`ClaudeComposerAsk` cold open with `BrutalistHesitantWriter` (WRITER LAW:
"database" -> "systems" — the naive assumption that one database answers
the request, corrected to needing every system). Close re-skinned to
`OutroCTA` / @HumanitariansAI with Liam's sign-off. Added an anchor (B02 ->
B03: one requester found under three different identifiers — current
email / name-only / a closed-out email) and a both-directions beat (B03)
per this factory's PHASE 1 structure requirement — the source (being
unfilled) carried neither.

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 7 beats, free, `am_onyx`. Durations: B00
   10.33s, B01 20.31s, B02 20.14s, B03 27.22s, BCRY 9.39s, BHTF 20.82s,
   BOUT 3.48s.
2. Wrote `scenes.py` (3 Manim scenes, reel-unique names `DSRB01Scene` /
   `DSRB02Scene` / `DSRB03Scene`, reusing the amendment-history sibling's
   `_spaced_text()` fix for ALL-CAPS multi-word labels and keeping
   terracotta off body text from the first pass) and `render_scenes.py`;
   rendered all three in the foreground, no failures.
3. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py`; the process
   exceeded the shell tool's inline timeout and was moved to a tracked
   background job mid-run. Per the COMPLETION LAW for one-shot
   invocations, blocked on `TaskOutput(task_id, block=true)` in the
   foreground rather than ending the turn — confirmed exit code 0 (all 4
   beats ok) before proceeding.
4. B00 verified directly: `media/B00.mp4` = 10.33s (clears the >=8s TIMING
   LAW floor and the >=9s narration-window target). Pulled a frame at
   t=9.5s: the correction ("database"->"systems") is complete and the
   full final question is legible.
5. First `compile.py` pass -> 7/7 real (no slate), 3840x2160 (THE 4K LAW),
   mean_volume -24.2 dB. WARNING: B03's raw 7.5s Manim clip was slowed
   3.6x to fill its 27.2s beat — over compile.py's own 3.0x "extreme
   slow-mo" threshold, logged to replace_log.md. Fixed (not left as a
   note, since it crossed the tool's own threshold): extended
   `DSRB03Scene`'s final `wait()` from 2.4s to 4.4s, bringing the raw clip
   to 9.5s; re-rendered; recompiled — slow-mo ratio now 2.85x, no warning.

**GATE T (type_check.py) — one real finding, fixed (not a false positive):**

- First pass: FAIL (1 sweep gate). §8.9 [BHTF/topic] flagged
  `"DSAR RESPONSE · PRIVACY & LEGAL AI"` as truncated in the
  `ClaudeComposerAsk` topic slot. Shortened to `"DSAR RESPONSE · PRIVACY
  LAW"` in both `metadata.topic` and the BHTF beat's `remotion.props.topic`
  (metadata.topic edit needed a direct Python string-replace after an
  Edit-tool mismatch from compile.py's build-stamp rewriting the file
  between reads — verified the replacement landed in both places by
  grep). Re-rendered BHTF, recompiled.
- Second pass: **PASS (0 FAILs)**.

**Gate V (visual) — pulled 19 frames across the full 112.7s runtime,
read directly, no defects found:**

B00's writer card, B01's system-chip slide, B02's three-identifier anchor,
B03's collapse-and-split (including the struck-through "coworker" redaction
detail), BCRY's carry-out quote, BHTF's composer card (topic no longer
truncated), and BOUT's outro all render legibly, safe inset respected, no
text overlap, no card-clip. Noted, not a defect introduced here: `OutroCTA`
renders on flat white rather than the humanitarians cream ground — same
shared-component behavior already logged unremarked in sibling reels in
this family (`claude-for-legal--claude-liam-amendment-history`,
`-board-minutes`, `claude-code--claude-liam-writing-rules`, etc.).

**Gates (final state):**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840x2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs) after fixing the confirmed BHTF/topic truncation
- Gate V: PASS (19 frames, full runtime, no defects)
- GATE AUDIO: PASS — mean_volume **-24.2 dB** (ffmpeg volumedetect), max
  -2.7 dB
- ffprobe: duration 112.667s; mp4 mtime (1788064637) newer than
  beat_sheet.json mtime (1788064559)

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
resolution as the sibling redos in this family.

Metadata file written:
`claude-for-legal--claude-liam-dsar-response.md` (channel
@HumanitariansAI, Playlist: **Claude Basics**, plus the direct code link
per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.
