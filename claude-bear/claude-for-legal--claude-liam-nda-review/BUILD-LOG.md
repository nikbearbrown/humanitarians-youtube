# BUILD-LOG — claude-for-legal--claude-liam-nda-review

## 2026-08-30 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-for-legal/youtube/claude-liam-nda-review/beat_sheet.json`.

**Source-gap finding (logged, not asked — see QUESTION.md for full detail):**
the source sheet is fully "built" (7 beats, all marked VIDEO/filled, dated
2026-07-26) but its narration text carries literal, never-filled template
placeholders (`>`) at every point where the actual skill-specific fact
should be: `"The skill is nda-review. >."`, `"Claude's job: >. What it gets
right: repeatable results. What it bites: anything outside the spec."`,
`"nda-review makes Claude execute one task reliably. The SKILL.md is the
spec — >."`, `"I want to >. Read the nda-review skill and walk me through
what you will do before you do it."` Its `source_skill` field points at
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/commercial-legal/skills/nda-review/SKILL.md`
— searched the entire `books/` tree on this machine; neither that file nor
a `commercial-legal` or `bear-textbooks` folder exists anywhere (identical
defect class to the `claude-for-legal--claude-liam-memo`, `-board-minutes`,
`-ai-tool-handoff`, `-ai-inventory`, and `-dsar-response` siblings already
built in this batch).

**The call:** rather than block on a missing human answer, reconstructed
the evident subject into a generic, defensible account of what reviewing
an NDA actually involves and what a Claude-assisted first pass can and
can't finish by itself — described generically per the fresh-script Phase 1
rule ("when in doubt, describe behavior generically") rather than inventing
specific tool names, UI, or product claims. The one substantive fact this
script leans on — a confidentiality clause conventionally carries carve-outs
(information that's already public, independently developed, already known,
or required to be disclosed by law), and what counts as a reasonable scope
or duration for those carve-outs varies by jurisdiction and deal — is
ordinary contract-drafting convention, not a Claude-specific or
unverifiable claim.

Register re-registered Teardown -> Plain: the source's B03 framed "Claude's
job" and "what it gets right / where it bites" as a design-tell verdict —
Teardown language. Plain instead states the mechanism (an NDA review's three
parts: clauses in, baseline check, flag list out) and both failure
directions (no flag isn't confirmation; heavy flagging isn't failure) as
properties of any NDA review, never a verdict on any specific skill's
design. Source's BVDT verdict recap folded into a dedicated BCRY carry-out
beat per CARRY-OUT LAW (same disposition as prior redos in this factory).
B00 replaced the source's `ClaudeComposerAsk` cold open with
`BrutalistHesitantWriter` (WRITER LAW: "CLEAR" -> "REVIEW" — the newcomer
assumption that an NDA review means Claude clears it for signing, corrected
to the fact that it reviews and flags against a baseline). Close re-skinned
to `OutroCTA` / @HumanitariansAI with Liam's sign-off.

Added an anchor (B02 -> B03: an NDA clause stamped "FLAGGED — NO
CARVE-OUT", returning stamped "CHECKED — OK TO SIGN") and a both-directions
beat (B03) per this factory's PHASE 1 structure requirement — the source
(being unfilled) carried neither.

## NO-GENAI / NO-PANTRY LAW

All 7 beats are REMOTION (B00 writer, BCRY carry-out, BHTF handoff, BOUT
outro) or GRAPHIC/Manim (B01, B02, B03), all in the humanitarians palette
(`#F3EBDD`/`#2F2A26`/`#E4572E`/`#1F4E5F`). No beat is AI-VIDEO, pantry, or a
human-drop slot.

## Built end to end this invocation

1. `generate_audio_kokoro.py` — 7 beats, free, `am_onyx`. Measured durations:
   B00 11.09s, B01 26.82s, B02 19.22s, B03 27.63s, BCRY 7.94s, BHTF 19.71s,
   BOUT 4.78s.
2. Wrote `scenes.py` (3 Manim scenes, reel-unique names `CFLNB01Scene` /
   `CFLNB02Scene` / `CFLNB03Scene`, adapted from the memo sibling's
   already-proven card geometry) and `render_scenes.py`. Pre-sized B02's
   final `wait()` (2.0s -> 12.2s) against the measured 19.22s narration
   before rendering, since the raw scene (~9.0s) would otherwise have
   needed a ~2.1x stretch at compile; B01 and B03's raw timings (~29.4s,
   ~28.7s) already sat close enough to their measured audio (26.82s,
   27.63s) to need no change. Rendered all three in the foreground, one
   pass, no failures.
3. Rendered B00/BCRY/BHTF/BOUT (all Remotion) via `remotion_scenes.py` in
   the foreground. The render exceeded the tool's default inline timeout
   and was moved to a tracked background task by the harness; per the
   COMPLETION LAW (never end a turn on an unsupervised render), blocked on
   it directly by polling its output file in the foreground until the
   task-completion notification confirmed exit code 0, then read the log —
   4/4 beats rendered clean, no failures.
4. B00 verified directly: pulled a frame at t=10.0s — the correction
   ("CLEAR" -> "REVIEW") is already complete and visible, full question
   legible: "Can Claude REVIEW this NDA for me?" `ffprobe` confirms
   `media/B00.mp4` = 11.1s, clearing the >=8s TIMING LAW floor.
5. `compile.py` -> 7/7 real (no slate), no B01/B02/B03 stretch warnings
   (the B02 pre-sizing in step 2 avoided the extreme-slow-mo class of
   defect the memo sibling hit), master
   `claude-for-legal--claude-liam-nda-review.mp4`, 118.2s, mean_volume
   -24.0 dB.
6. Gate V: full frame sweep, 6s interval, all 20 frames read directly.
   Every beat legible, correct contrast, no text overlap, no clipping,
   safe inset respected, correct @HumanitariansAI branding and outro title
   throughout. No defects found — no re-render needed.

## Gates

- **TIMING LAW (B00):** narration 30 words + `lead_silence_s` 0.8 ->
  measured `actual_duration_s` **11.09s** (rendered 11.1s), clears the
  >=8s floor. Correction visible on-screen by t=10.0s (confirmed via
  direct frame read: "Can Claude REVIEW this NDA for me?").
- **content-check / frame-check / lane-check:** all PASS per `compile.py`
  output (7/7 beats, no violations, canvas 3840x2160).
- **GATE T (type_check.py):** PASS — 0 FAILs.
- **Gate V (frame QC):** full sweep at 6s intervals across the 118.2s
  runtime (20 frames), all read directly. Clean on first pass — legible,
  safe inset respected, no text overlap, no clipping, correct
  @HumanitariansAI branding and outro title. (BOUT/OutroCTA renders on
  flat white, not the humanitarians cream ground — same shared-component
  note already logged unfixed in every sibling in this family, e.g.
  `-memo`.)
- **GATE AUDIO:** PASS, mean_volume **-24.0 dB** (ffmpeg volumedetect via
  `compile.py`, well above the -40 dB floor).
