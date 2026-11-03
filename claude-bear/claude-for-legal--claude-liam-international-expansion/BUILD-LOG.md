# BUILD-LOG — claude-for-legal--claude-liam-international-expansion

## 2026-08-30 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-for-legal/youtube/claude-liam-international-expansion/beat_sheet.json`.

**Source-gap finding (logged, not asked — see QUESTION.md for full detail):**
the source sheet is fully "built" (7 beats, all marked VIDEO/filled, dated
2026-08-03) but its narration text carries literal, never-filled template
placeholders (`>`) at every point where the actual skill-specific fact
should be: `"The skill is international-expansion. >."`, `"Claude's job:
>."`, `"The SKILL.md is the spec — >."`, `"I want to >."` Its
`source_skill` field points at
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/employment-legal/skills/international-expansion/SKILL.md`
— searched the entire `books/` tree on this machine; neither that file nor
an `employment-legal` folder under `claude-for-legal` exists. So there were
no real facts to carry over from the source, only a topic
(INTERNATIONAL-EXPANSION, an Anthropic skill referenced as "an
implementation-planning framework for international hiring") and a shape
(Teardown skill-teardown format, 7 beats: cold open, anatomy, pipeline,
design tell, verdict, handoff, outro). Same defect class already found and
logged in this family's `claude-liam-ai-inventory` redo.

**The call:** rather than block on a missing human answer, reconstructed
the evident subject into a generic, defensible account of what a legal/HR
team must decide before a first international hire — worker classification
and choice of legal employer — described generically per the fresh-script
Phase 1 rule ("when in doubt, describe behavior generically") rather than
inventing a specific country's statutory test, specific product screens, or
output format. No fact in the resulting script is Claude-specific,
jurisdiction-specific, or unverifiable; Germany appears once as a concrete
anchor scenario, never as a stated legal conclusion.

Register re-registered Teardown -> Plain: the source's B03 framed "Claude's
job" and "what it gets right / where it bites" as a design-tell verdict —
Teardown language. Plain instead states the mechanism (classification, legal
employer, mandatory terms) and its failure modes (contractor-shaped today
isn't locked in; employee-shaped doesn't require your own entity) as
properties of the practice, never a verdict on any specific skill's design.
Source's BVDT verdict recap folded into a dedicated BCRY carry-out beat per
CARRY-OUT LAW (same disposition as prior redos in this factory). B00
replaced the source's `ClaudeComposerAsk` cold open with
`BrutalistHesitantWriter` (WRITER LAW: "contract" -> "classification" — the
naive assumption that the first move is drafting a contract, corrected to
the fact that classification has to be decided first). Close re-skinned to
`OutroCTA` / @HumanitariansAI with Liam's sign-off. Added an anchor (B02 ->
B03: the Berlin developer, full control/one client/employer-provided
equipment, unclassified, then run through the checks and split into the two
both-directions cautions) per this factory's PHASE 1 structure requirement
— the source (being unfilled) carried neither an anchor nor a
both-directions beat.

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 7 beats, free, `am_onyx`. Durations: B00
   11.01s, B01 18.26s, B02 21.53s, B03 23.44s, BCRY 11.67s, BHTF 20.42s,
   BOUT 3.80s.
2. Wrote `scenes.py` (3 Manim scenes, reel-unique names `INTLB01Scene` /
   `INTLB02Scene` / `INTLB03Scene`) and `render_scenes.py`; rendered all
   three in the foreground.
3. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py` in the foreground
   (the process exceeded the shell's 120s inline timeout and was moved to a
   tracked background job mid-run; per the COMPLETION LAW for one-shot
   invocations, polled the job's own output file in a blocking foreground
   loop rather than ending the turn — confirmed exit code 0 before
   proceeding).
4. B00 verified directly: `media/B00.mp4` = 11.03s (meets the >=8s TIMING
   LAW floor). Pulled frames at t=8.5s/10.5s: the correction
   ("contract"->"classification") is already complete and legible by t=8.5s,
   full question legible at t=10.5s.
5. First `compile.py` pass -> 7/7 real (no slate), 3840x2160 (THE 4K LAW),
   mean_volume -24.1 dB (already passing GATE AUDIO).

**Gate V (visual) — one real defect found and fixed, rest clean:**

Pulled frames every 5s across the full 111s runtime plus targeted crops, and
read them directly. Found one defect:

1. **B01**: the "EMPLOYEE" stamp was positioned at the contract card's
   vertical center, landing on top of the three status chips ("their
   hours" / "your gear" / "one client") instead of over just the header —
   the chip text was partially obscured underneath the stamp.

Root-caused to `stamp_group.move_to(contract_box.get_center() + UP * 0.1)`
in `scenes.py` — a hardcoded offset that happened to land mid-card rather
than on the header it was meant to mark. Fixed by moving the stamp to
`header_label.get_center()` instead, so it lands cleanly over the
"CONTRACT: CONTRACTOR" header and leaves the chip row fully clear.
Re-rendered B01, recompiled, and re-pulled the frame at t=28s: "EMPLOYEE"
now sits over the header, all three chips ("their hours", "your gear", "one
client") fully legible with no overlap. Re-checked all other beats (B00,
B02, B03, BCRY, BHTF, BOUT) across the full runtime — all clean, legible,
safe inset respected, no other text overlap.

**GATE T (type_check.py) — one finding, confirmed false positive, not a
real defect:**

- First pass: FAIL (1 pixel beat). B02's kerning check flagged the SANS
  title "THREE CHECKS — THE ANCHOR" (max inter-glyph gap 90px vs. threshold
  15px). Same documented false-positive class as the `AINVB02Scene` /
  `INTMB02Scene` exemptions already in this file's
  `KERNING_EXEMPT_PATTERNS`: the em-dash glyph renders as a much narrower
  ink run than the surrounding letters, dragging the derived `mean_w` down
  so ordinary inter-glyph advance elsewhere in the title reads as an
  oversized gap. Pulled the exact frame the checker samples (t=dur*0.5 of
  the raw `manim/B02.mp4`) and read it directly: the title renders as one
  cleanly kerned, fully legible run. Registered `INTLB02Scene` in
  `KERNING_EXEMPT_PATTERNS` with the same documentation style as the
  existing entries.
- Second pass: **PASS (0 FAILs)**.

**Noted, not a defect introduced here:** B01/B02/B03's raw Manim clips
(7.6s/8.3s/9.8s) were slowed 2.4-2.6x by `compile.py` to fill their
18.3s/21.5s/23.4s narration beats — below the 3.0x hard-warning threshold,
so no `_log_replace` entry was written, and the same ratio class is already
present unremarked in this family's sibling reels built by this pipeline.
`OutroCTA` renders on flat white rather than the humanitarians cream ground
— same shared-component behavior already logged unremarked in sibling
reels in this family (e.g. `claude-liam-ai-inventory`).

**Gates (final state):**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840x2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs) after registering the confirmed em-dash kerning
  false-positive exemption above
- Gate V: PASS after fixing the B01 stamp/chip overlap defect above
- GATE AUDIO: PASS — mean_volume **-24.1 dB** (ffmpeg volumedetect), max
  -3.0 dB
- ffprobe: duration 111.148s, 3840x2160; mp4 mtime (1788092476) newer than
  beat_sheet.json mtime (1788092204)

**Playlist resolution:** family `claude-for-legal` does not match any
prefix key in `skills/make/hai-simple/loop/playlists.json` (verified by
running the match algorithm directly — no key is a prefix of
`claude-for-legal`). Per the map's documented fallback ("match SUBJECT.json's
family, or the hai-simple prefix"), fell through to matching the skill name
itself: `hai-simple` is a literal key in the map, resolving to **Claude
Basics** — same resolution as this family's other redos.

Metadata file written:
`claude-for-legal--claude-liam-international-expansion.md` (channel
@HumanitariansAI, Playlist: **Claude Basics**, plus the direct code link
per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.

## 2026-08-30 — Phase 4 delivery

Master is already 3840x2160 (THE 4K LAW in compile.py forces any clean,
non-`--review` master to 4K), so the Fellows-facing 4K file is the same
render, copied to the `-4k` filename `deliver.py` expects:

```
cp claude-for-legal--claude-liam-international-expansion.mp4 \
   claude-for-legal--claude-liam-international-expansion-4k.mp4
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Outbox staged:
`DELIVERY/claude-for-legal--claude-liam-international-expansion/` (4K mp4 +
description.md). Repo: committed + pushed to
`humanitarians-youtube/claude-bear/claude-for-legal--claude-liam-international-expansion/`
(README.md, beat_sheet.json, SCRIPT.md, SUBJECT.json, BUILD-LOG.md,
CARRY-OUT.md, QUESTION.md — no mp3/mp4), commit `ad15ed38`.

**Status: DELIVERED.** Both delivery targets staged/pushed. Reel complete.
