# BUILD-LOG — claude-for-legal--claude-liam-memo

## 2026-08-30 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-for-legal/youtube/claude-liam-memo/beat_sheet.json`.

**Source-gap finding (logged, not asked — see QUESTION.md for full detail):**
the source sheet is fully "built" (7 beats, all marked VIDEO/filled, dated
2026-07-26) but its narration text carries literal, never-filled template
placeholders (`>`) at every point where the actual skill-specific fact
should be: `"The skill is memo. >."`, `"Claude's job: >."`, `"The SKILL.md
is the spec — >."`, `"I want to >. Read the memo skill and walk me through
what you will do before you do it."` Its `source_skill` field points at
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/legal-clinic/skills/memo/SKILL.md`
— searched the entire `books/` tree on this machine; neither that file nor
a `legal-clinic` folder exists anywhere (identical defect class to the
`claude-for-legal--claude-liam-board-minutes`, `-ai-tool-handoff`,
`-ai-inventory`, and `-dsar-response` siblings already built in this
batch). So there were no real facts to carry over from the source, only a
topic (MEMO) and a shape (Teardown skill-teardown format, 7 beats: cold
open, anatomy, pipeline, design tell, verdict, handoff, outro).

**The call:** rather than block on a missing human answer, reconstructed
the evident subject into a generic, defensible account of what a legal
memo actually is and what a drafting handoff to Claude can and can't
finish by itself — described generically per the fresh-script Phase 1 rule
("when in doubt, describe behavior generically") rather than inventing
specific tool names, UI, or product claims. The one substantive fact this
script leans on — a legal memo is a predictive, internal analysis of law
applied to facts (issue-rule-application-conclusion), not a final verified
opinion, and its citations are conventionally checked against current law
before anyone relies on it — is ordinary legal-practice convention, not a
Claude-specific or unverifiable claim.

Register re-registered Teardown -> Plain: the source's B03 framed
"Claude's job" and "what it gets right / where it bites" as a design-tell
verdict — Teardown language. Plain instead states the mechanism (a memo
handoff's three parts: question, draft, verify) and both failure directions
(no flag isn't confirmation; heavy correction isn't failure) as properties
of any legal-memo handoff, never a verdict on any specific skill's design.
Source's BVDT verdict recap folded into a dedicated BCRY carry-out beat per
CARRY-OUT LAW (same disposition as prior redos in this factory). B00
replaced the source's `ClaudeComposerAsk` cold open with
`BrutalistHesitantWriter` (WRITER LAW: "OPINION" -> "MEMO" — the newcomer
assumption that Claude produces a final legal opinion, corrected to the
fact that a memo is a working draft analysis). Close re-skinned to
`OutroCTA` / @HumanitariansAI with Liam's sign-off.

Added an anchor (B02 -> B03: a memo page stamped "FLAGGED — VERIFY",
returning stamped "VERIFIED — RELIABLE") and a both-directions beat (B03)
per this factory's PHASE 1 structure requirement — the source (being
unfilled) carried neither.

## NO-GENAI / NO-PANTRY LAW

All 7 beats are REMOTION (B00 writer, BCRY carry-out, BHTF handoff, BOUT
outro) or GRAPHIC/Manim (B01, B02, B03), all in the humanitarians palette
(`#F3EBDD`/`#2F2A26`/`#E4572E`/`#1F4E5F`). No beat is AI-VIDEO, pantry, or a
human-drop slot.

## Built end to end this invocation

1. `generate_audio_kokoro.py` — 7 beats, free, `am_onyx`. Durations: B00
   11.86s, B01 29.42s, B02 18.22s, B03 28.95s, BCRY 7.42s, BHTF 17.79s,
   BOUT 4.61s.
2. Wrote `scenes.py` (3 Manim scenes, reel-unique names `CFLMB01Scene` /
   `CFLMB02Scene` / `CFLMB03Scene`) and `render_scenes.py`; rendered all
   three in the foreground.
3. First compile flagged B01 and B03 as "extreme slow-mo" (9.2s/8.9s raw
   clips stretched 3.2x/3.3x into 29.4s/28.9s beats, logged to
   `replace_log.md`) — root-caused to `self.wait()` durations sized for a
   much shorter narration draft. Fixed by extending the hold times in
   `scenes.py` (not by loosening the gate): re-rendered B01 to 29.5s and
   B03 to 28.8s, both now within the compiler's non-extreme stretch range.
   Recompiled clean — no warnings, no `replace_log.md` entries.
4. Rendered B00/BCRY/BHTF/BOUT (all Remotion) via `remotion_scenes.py` in
   the foreground, one pass, no failures.
5. B00 verified directly: pulled a frame at t=10.5s — the correction
   ("OPINION" -> "MEMO") is already complete and visible, full question
   legible: "Can Claude give me a legal MEMO on my case?" `ffprobe`
   confirms `media/B00.mp4` = 11.87s, clearing the >=8s TIMING LAW floor.
6. Gate V (full frame sweep, 6s interval, all 20 frames read): caught a
   real defect the automated gates missed — in the first cut, the citation
   stamp ("FLAGGED — VERIFY" in B02, "VERIFIED" in B03) sat directly on top
   of the "Conclusion: likely, if valid" memo line, and the "reliable"
   caption was visually clipped to "rdiable". Root cause: the stamp/text
   vertical positions were copied from the board-minutes template without
   re-checking clearance against this reel's card size and font. Fixed by
   enlarging the card, moving the memo text well below the stamp's
   position, and moving "reliable" below the whole card instead of beside
   the stamp box. Re-rendered B02/B03, recompiled, re-verified with fresh
   frame pulls at the same timestamps — stamp and text now fully clear of
   each other, "reliable" reads correctly.
7. `compile.py` -> 7/7 real (no slate), master
   `claude-for-legal--claude-liam-memo.mp4`, 119.28s, mean_volume -23.8 dB.

## Gates

- **TIMING LAW (B00):** narration 34 words + `lead_silence_s` 0.8 ->
  measured `actual_duration_s` **11.86s** (rendered 11.87s), clears the
  >=8s floor. Correction visible on-screen by t=10.5s (confirmed via
  direct frame read).
- **content-check / frame-check / lane-check:** all PASS per `compile.py`
  output (7/7 beats, no violations, canvas 3840x2160).
- **GATE T (type_check.py):** PASS — 0 FAILs.
- **Gate V (frame QC):** full sweep at 6s intervals across the 119.28s
  runtime (20 frames) plus targeted spot-checks on B02/B03 before and
  after the stamp-overlap fix. One real defect found and fixed (see above,
  item 6); final sweep clean — legible, safe inset respected, no text
  overlap, no clipping, correct @HumanitariansAI branding and outro title.
- **GATE AUDIO:** PASS, mean_volume **-23.8 dB** (ffmpeg volumedetect,
  well above the -40 dB floor), max -2.7 dB.
