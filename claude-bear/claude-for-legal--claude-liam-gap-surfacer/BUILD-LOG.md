# BUILD-LOG — claude-for-legal--claude-liam-gap-surfacer

## 2026-08-30 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-for-legal/youtube/claude-liam-gap-surfacer/beat_sheet.json`.

**Source-gap finding (logged, not asked — see QUESTION.md for full detail):**
the source sheet is fully "built" (7 beats, all marked VIDEO/filled, dated
2026-07-25) but its narration text carries literal, never-filled template
placeholders (`>`) at every point where the actual skill-specific fact
should be: `"Claude's job: >."`, `"the SKILL.md is the spec — >."`,
`"I want to >."` Its `source_skill` field points at
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/regulatory-legal/skills/gap-surfacer/SKILL.md`
— searched the entire `books/` tree on this machine; neither that file nor
a `regulatory-legal` folder exists anywhere. The book's own audit files
(`_audit/audit_results.csv`, `_audit/REBUILD-WORKLIST.csv`) independently
flag this exact sheet `no-FACTCHECK`. So there were no real facts to carry
over from the source, only a name (gap-surfacer) and a shape (Teardown
skill-teardown format, 7 beats: cold open, anatomy, pipeline, design tell,
verdict, handoff, outro) — the same defect already found and logged for
the sibling `claude-liam-ai-inventory` redo in this factory.

**The call:** rather than block on a missing human answer, reconstructed
the evident subject from the skill's own name into a generic, defensible
account of what a checklist-vs-document gap check does and what a
"no match" from one actually means — described generically per the
fresh-script Phase 1 rule ("when in doubt, describe behavior generically")
rather than inventing this specific skill's exact steps, output format, or
trigger phrases. No fact in the resulting script is Claude-specific or
unverifiable.

Register re-registered Teardown -> Plain: the source's B03 framed
"Claude's job" and "what it gets right / where it bites" as a design-tell
verdict — Teardown language. Plain instead states the mechanism (walk a
checklist, scan for matches, flag absences) and both failure directions
(match ≠ good enough; no-match ≠ gone) as properties of the practice,
never a verdict on any specific skill's design. Source's BVDT verdict
recap folded into a dedicated BCRY carry-out beat per CARRY-OUT LAW (same
disposition as prior redos in this factory). B00 replaced the source's
`ClaudeComposerAsk` cold open with `BrutalistHesitantWriter` (WRITER LAW:
"bad" -> "missing" — the naive assumption that this kind of check reads
quality, corrected to the fact that it only checks for absence). Close
re-skinned to `OutroCTA` / @HumanitariansAI with Liam's sign-off. Added an
anchor (B02 -> B03: the assignment-clause checklist line flagged NO MATCH,
then found under different wording, "Transfer of Rights") and a
both-directions beat (B03) per this factory's PHASE 1 structure
requirement — the source (being unfilled) carried neither.

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 7 beats, free, `am_onyx`. First pass
   produced B00 at 8.21s (narration only 24 words) — under the WRITER LAW's
   >=9s design target (though above the >=8s hard verify floor). Lengthened
   B00's narration by ~9 words for a safer margin and regenerated just that
   beat with `--only B00`: 10.11s. Final durations: B00 10.11s, B01 16.75s,
   B02 16.98s, B03 15.66s, BCRY 8.17s, BHTF 17.77s, BOUT 4.29s.
2. Wrote `scenes.py` (3 Manim scenes, reel-unique names `GSRFB01Scene` /
   `GSRFB02Scene` / `GSRFB03Scene`) and `render_scenes.py`; rendered all
   three in the foreground — all passed on the first attempt.
3. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py` in the foreground.
   The first combined call exceeded the shell's 120s inline timeout mid-run
   (B00 had already rendered); per the COMPLETION LAW for one-shot
   invocations, re-ran the remaining beats one at a time with `--only
   <ID>` and an explicit longer per-call timeout rather than backgrounding
   the render — confirmed exit code 0 / "ok" on each call before
   proceeding. BOUT had in fact already completed during the timed-out
   run; `--only BOUT` correctly reported "filled already (skip)".
4. B00 verified directly: `media/B00.mp4` = 10.13s (comfortably clears the
   >=8s floor and the >=9s design target). Pulled frames at t=6.5s/9s: the
   correction ("bad"->"missing", landing as "missing clauses?") is fully
   complete and legible by t=9s.
5. First `compile.py` pass -> 7/7 real (no slate), 3840x2160 (THE 4K LAW),
   mean_volume -23.9 dB (already passing GATE AUDIO). Manim clips were
   slowed 1.6-1.7x to fill their beats (narration ran longer than the raw
   ~10s animations) — noted as a pacing choice, not a defect; verified
   below that every beat still reads as clean, legible motion, not stalled
   holds.

**GATE T (type_check.py) — PASS on the first attempt, 0 FAILs.** No
kerning or overflow findings across any of the 7 beats.

**Gate V (visual) — pulled frames every 5s across the full 90.7s runtime,
plus two extra frame-accurate pulls (t=25s, t=26s) to double-check a
`-ss`-before-`-i` artifact that had made B01's closing caption look
under-opacity in the coarse pass.** Read every frame directly:

- B00: writer types the naive framing, hesitates on "bad", corrects to
  "missing" — fully visible and legible.
- B01: "NOT A QUALITY CHECK" — magnifying-glass card struck through
  cleanly, checklist chip + scan + MATCH readout legible, closing caption
  ("does matching text show up anywhere? that's the only question.") full
  opacity and legible once seeked frame-accurately.
- B02: THE ANCHOR — three checklist chips (GOVERNING LAW / INDEMNIFICATION
  / ASSIGNMENT) scan cleanly to MATCH / MATCH / NO MATCH, "flagged, not
  yet resolved" caption clean.
- B03: THE ANCHOR RETURNS — ASSIGNMENT connects to TRANSFER OF RIGHTS,
  lights up "found", splits cleanly into the two both-directions cards
  (match-is-not-good-enough / no-match-is-not-gone) with clean strikes.
- BCRY: carry-out quote, alone, legible serif.
- BHTF: `ClaudeComposerAsk` composer card, legible mid-type (expected for
  a typing-effect capture).
- BOUT: `OutroCTA` — renders on flat white rather than the humanitarians
  cream ground; same shared-component behavior already logged unremarked
  in sibling reels in this family (e.g. `claude-liam-ai-inventory`), not a
  defect introduced here.

No text overflow, no card-clip, no overlapping elements, safe inset
respected throughout. **Gate V: PASS, zero fixes needed.**

**Gates (final state):**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840x2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs)
- Gate V: PASS (no defects found)
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (ffmpeg volumedetect), max
  -2.7 dB
- ffprobe: duration 90.739s; mp4 mtime (1788081338) newer than
  beat_sheet.json mtime (1788081234)

**Non-blocking warning (compile.py):** motion histogram remotion:4
graphic:3 — remotion at more than half of beats. Structural, not a defect:
hai-simple's mandated shape is B00 (writer) + BCRY + BHTF (Your Turn) +
BOUT (outro) all REMOTION by skill contract, against 3 GRAPHIC body beats
for this 7-beat reel — same disposition as every other short hai-simple
reel in this family.

**Playlist resolution:** family `claude-for-legal` does not match any
prefix key in `skills/make/hai-simple/loop/playlists.json`. Per the map's
documented fallback, fell through to matching the skill name itself:
`hai-simple` is a literal key in the map, resolving to **Claude Basics**
— same resolution already independently verified for the sibling
`claude-liam-ai-inventory` redo.

Metadata file written: `claude-for-legal--claude-liam-gap-surfacer.md`
(channel @HumanitariansAI, Playlist: **Claude Basics**, plus the direct
code link per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.

## 2026-08-30 — Phase 4 delivery

Master is already 3840x2160 (THE 4K LAW in compile.py forces any clean,
non-`--review` master to 4K), so the Fellows-facing 4K file is the same
render, copied to the `-4k` filename `deliver.py` expects:

```
cp claude-for-legal--claude-liam-gap-surfacer.mp4 \
   claude-for-legal--claude-liam-gap-surfacer-4k.mp4
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Outbox staged: `DELIVERY/claude-for-legal--claude-liam-gap-surfacer/`
(4K mp4 + description.md). Repo: committed + pushed to
`humanitarians-youtube/claude-bear/claude-for-legal--claude-liam-gap-surfacer/`
(README.md, beat_sheet.json, SCRIPT.md, SUBJECT.json, BUILD-LOG.md,
CARRY-OUT.md, QUESTION.md — no mp3/mp4), commit `bff9ac90`.

**Status: DELIVERED.** Both delivery targets staged/pushed. Reel complete.
