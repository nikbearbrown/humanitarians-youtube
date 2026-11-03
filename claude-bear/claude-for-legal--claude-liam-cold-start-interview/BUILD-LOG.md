# BUILD-LOG — claude-for-legal--claude-liam-cold-start-interview

## 2026-08-29 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-for-legal/youtube/claude-liam-cold-start-interview/beat_sheet.json`.

**Source-gap finding (logged, not asked — see QUESTION.md for full detail):**
the source sheet is fully "built" (7 beats, all marked VIDEO/filled, dated
2026-08-03) but its narration text carries literal, never-filled template
placeholders (`>`) at every point where the actual skill-specific fact
should be: `"Claude's job: >."`, `"The SKILL.md is the spec — >."`, `"I
want to >. Read the cold-start-interview skill…"` Its `source_skill` field
points at
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/ai-governance-legal/skills/cold-start-interview/SKILL.md`
— searched the entire `books/` tree on this machine; neither that file nor
an `ai-governance-legal` folder exists anywhere. Same defect class already
logged for numerous siblings in this family (`ai-inventory`,
`ai-tool-handoff`, `amendment-history`, `aia-generation`, `auto-updater`,
…): a batch-built Teardown shell whose skill-specific fact was never
actually authored.

**The call:** rather than block on a missing human answer, reconstructed a
generic, defensible account from the skill's own name
(cold-start-interview) plus one genuinely verifiable Claude property (a new
conversation carries no memory of a prior one, absent context explicitly
carried forward) — described generically per the fresh-script Phase 1 rule
("when in doubt, describe behavior generically") rather than inventing a
specific question list, UI, or product claim for what the skill actually
asks. No fact in the resulting script is an invented Claude-specific
behavior.

Register re-registered Teardown -> Plain: the source's B03 framed "Claude's
job" and "what it gets right / where it bites" as a design-tell verdict —
Teardown language. Plain instead states the mechanism (fixed questions vs.
a remembered brief) and its failure modes (answered is not remembered;
thorough is not complete) as properties of the practice, never a verdict on
any specific skill's design. Source's BVDT verdict recap folded into a
dedicated BCRY carry-out beat per CARRY-OUT LAW (same disposition as every
prior redo in this factory). B00 replaced the source's `ClaudeComposerAsk`
cold open with `BrutalistHesitantWriter` (WRITER LAW: "brief" -> "interview"
— the naive assumption that a new matter needs a written brief, corrected
to the fact that it needs a fixed interview instead). Close re-skinned to
`OutroCTA` / @HumanitariansAI with Liam's sign-off. Added an anchor (B02 ->
B03: jurisdiction, the detail everyone assumes goes without saying, planted
unanswered then paid off answered) and a both-directions beat (B03) per this
factory's PHASE 1 structure requirement — the source (being unfilled)
carried neither. Kept the source's 7-beat shape (B00 writer + B01
stakes/wrong-guess-falsified + B02 mechanism/anchor-planted + B03
anchor-payoff/both-directions + BCRY carry-out + BHTF handoff + BOUT outro).

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 7 beats, free, `am_onyx`. First B00 draft
   (24-word narration) measured only 7.51s, under the WRITER LAW's >=8s
   floor (TIMING LAW: needs a >=9s window). Lengthened B00 narration to 31
   words (20-35 word band, unchanged `lead_silence_s: 0.8`), regenerated
   B00 audio only -> 9.90s. Final durations: B00 9.90s, B01 19.99s, B02
   17.26s, B03 20.99s, BCRY 8.19s, BHTF 14.72s, BOUT 3.43s.
2. Wrote `scenes.py` (3 Manim scenes, reel-unique names `CSIB01Scene` /
   `CSIB02Scene` / `CSIB03Scene`) and `render_scenes.py`; rendered all three
   in the foreground.
3. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py` in the foreground
   (first invocation exceeded the shell's 120s inline default and was
   re-run with an explicit longer tool-level timeout per the COMPLETION LAW
   for one-shot invocations — waited on the real exit code rather than
   backgrounding it and ending the turn).
4. B00 verified directly: after the narration fix, `media/B00.mp4` = 9.9s
   (meets the >=8s TIMING LAW floor). Pulled a frame at t=9.5s: the
   correction ("brief" -> "interview") is complete and legible, full
   question on screen.
5. First `compile.py` pass -> 7/7 real (no slate), 3840x2160 (THE 4K LAW),
   mean_volume -24.1 dB (already passing GATE AUDIO).

**GATE T (type_check.py) — one real defect, fixed at the root (not a false
positive; same recurring class as sibling redos `amendment-history` et
al.):**

- First pass: FAIL (1 pixel beat). B02's "THE ANCHOR" label, rendered in
  terracotta (`#E4572E`, bold, font_size 24) directly on the cream ground,
  measured 2.74:1 contrast — below the 4.5:1 WCAG floor (hand-verified the
  WCAG luminance math independently; genuine fail, not a sampling
  artifact). Grepped the whole `scenes.py` for every other `color=TERRA`
  usage on a `Text()` run and found three more instances of the same
  pattern that would have failed the same check on a different frame:
  B03's `"jurisdiction: answered"` line, the struck-through `"REMEMBERED"`
  word, and the `"answered is not remembered"` label. Fixed all four by
  recoloring the text itself to INK and keeping terracotta only on
  structural marks — a new underline bar beneath "THE ANCHOR" (Rectangle,
  not text) and the existing strike-through `Line()` — matching this
  toolkit's established convention (`type_check.py`'s
  `STRUCTURAL_TERRACOTTA_PATTERNS` table: terracotta is a structural
  accent, never a legible word's color).
- Re-rendered B02/B03, recompiled, re-ran GATE T: **PASS (0 FAILs)**.

**Gate V (visual) — clean on first pass after the GATE T fix:** pulled 19
frames at 5s intervals across the full 95.5s runtime and read every one
directly. B00's writer correction lands and stays legible; B01's brief
card and the sliding unlabeled "jurisdiction" chip read cleanly with no
overlap; B02's five fixed-question chips and the anchor callout are
legible and correctly inked; B03's payoff (jurisdiction answered, sliding
into place, then the two both-directions cards with the struck
"REMEMBERED") is clean, safe inset respected; BCRY's quote card is legible
serif on cream; BHTF's composer types the real paste-ready prompt cleanly.
**Noted, not a defect introduced here:** BOUT's `OutroCTA` renders on flat
white rather than the humanitarians cream ground — same shared-component
behavior already logged unremarked in sibling reels in this family.

**Gates (final state):**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840x2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs) after recoloring the four TERRA-on-cream text
  instances above to INK
- Gate V: PASS (19 frames across the full runtime, no defects)
- GATE AUDIO: PASS — mean_volume **-24.1 dB** (ffmpeg volumedetect), max
  -3.0 dB
- ffprobe: duration 95.481s; mp4 mtime (1788039166) newer than
  beat_sheet.json mtime (1788038727)

**Non-blocking note (compile.py):** B01-B03 Manim clips rendered shorter
than their beats' measured narration (raw clips 9.3s/8.1s/9.8s vs.
20.0s/17.3s/21.0s beats) and compile.py time-stretched each ~2.1x to fill
the beat, per its normal fill-to-audio-duration behavior. Reviewed in Gate
V: all three beats still read as deliberate, unhurried holds, not as
visibly slowed motion — no action needed.

**Playlist resolution:** family `claude-for-legal` does not match any
prefix key in `skills/make/hai-simple/loop/playlists.json`. Per the map's
documented fallback ("match SUBJECT.json's family, or the hai-simple
prefix"), fell through to matching the skill name itself: `hai-simple` is a
literal key in the map, resolving to **Claude Basics** — same resolution as
every other `claude-for-legal` redo in this factory.

Metadata file written:
`claude-for-legal--claude-liam-cold-start-interview.md` (channel
@HumanitariansAI, Playlist: **Claude Basics**, plus the direct code link
per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.
