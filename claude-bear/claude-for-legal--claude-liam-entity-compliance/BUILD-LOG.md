# BUILD-LOG — claude-for-legal--claude-liam-entity-compliance

## 2026-08-30 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-for-legal/youtube/claude-liam-entity-compliance/beat_sheet.json`.

**Source-gap finding (logged, not asked — see QUESTION.md for full detail):**
the source sheet is fully "built" (7 beats, all marked VIDEO/filled, dated
2026-07-25) but its narration text carries literal, never-filled template
placeholders (`>`) at every point where the actual skill-specific fact
should be: `"The skill is entity-compliance. >."`, `"Claude's job: >."`,
`"The SKILL.md is the spec — >."`, `"I want to >."` Its `source_skill`
field points at
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/corporate-legal/skills/entity-compliance/SKILL.md`
— searched the entire `books/` tree on this machine; neither that file nor
a `corporate-legal` folder exists anywhere. This is the identical gap
already logged and resolved for the sibling reel
`claude-for-legal--claude-liam-ai-inventory` (same family, same source
defect pattern, same missing-file-on-this-machine outcome).

**The call:** rather than block on a missing human answer, reconstructed
the evident subject into a generic, defensible account of what "entity
compliance" is in ordinary corporate legal-ops practice — keeping every
legal entity a company has current against its own recurring set of state
filing deadlines (annual/biennial report, registered agent, foreign
qualification, franchise tax) — described generically per the fresh-script
Phase 1 rule ("when in doubt, describe behavior generically") rather than
inventing specific tool names, UI, or product claims. No fact in the
resulting script is Claude-specific or unverifiable.

Register re-registered Teardown -> Plain: the source's B03 framed
"Claude's job" and "what it gets right / where it bites" as a design-tell
verdict — Teardown language. Plain instead states the mechanism (four
recurring obligations per entity) and its failure modes (current at home
is not compliant everywhere; clean today is not clean forever) as
properties of the practice, never a verdict on any specific skill's
design. Source's BVDT verdict recap folded into a dedicated BCRY carry-out
beat per CARRY-OUT LAW (same disposition as prior redos in this factory).
B00 replaced the source's `ClaudeComposerAsk` cold open with
`BrutalistHesitantWriter` (WRITER LAW: "done" -> "current" — the naive
assumption that registering finishes the compliance job, corrected to the
fact that compliance is an ongoing, recurring status). Close re-skinned to
`OutroCTA` / @HumanitariansAI with Liam's sign-off. Added an anchor
(B02 -> B03: the Delaware subsidiary spun up for a single product launch,
unwatched for three years, then found lapsed in financing diligence) and a
both-directions beat (B03) per this factory's PHASE 1 structure
requirement — the source (being unfilled) carried neither.

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 7 beats, free, `am_onyx`. Durations: B00
   9.92s, B01 18.26s, B02 19.97s, B03 22.14s, BCRY 6.63s, BHTF 16.94s,
   BOUT 5.14s.
2. Wrote `scenes.py` (3 Manim scenes, reel-unique names `ENTB01Scene` /
   `ENTB02Scene` / `ENTB03Scene`) and `render_scenes.py`; rendered all
   three in the foreground.
3. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py` in the foreground
   (the process exceeded the shell's 120s inline timeout and was moved to
   a tracked background job mid-run; per the COMPLETION LAW for one-shot
   invocations, blocked on `TaskOutput` in the foreground rather than
   ending the turn — confirmed exit code 0 before proceeding).
4. B00 verified directly: `media/B00.mp4` = 9.93s (meets the >=8s TIMING
   LAW floor). Pulled frames at t=6.5s/9s: the correction
   ("done" -> "current") is already complete and visible by t=6.5s, full
   corrected question legible by t=9s.
5. First `compile.py` pass -> 7/7 real (no slate), 3840x2160 (THE 4K LAW),
   mean_volume -24.0 dB (already passing GATE AUDIO).

**GATE T (type_check.py):** PASS, 0 FAILs, both before and after the Gate V
fix below (no kerning or content violations at any point).

**Gate V (visual) — first pass found one real defect, fixed:**

Pulled frames every 5s across the full 100s runtime and read them
directly. Found one real, viewer-visible defect: **B03**'s crossfade
transition (`FadeOut(dim_blank)`, `FadeOut(dim_label)`,
`dim_card.animate.set_stroke(opacity=1)`, `FadeIn(field_lines)` all played
simultaneously over `run_time=1.3`) produced a mid-transition frame where
the old dim-card labels ("DE subsidiary — product launch" /
"(no dates filled in)") ghosted through, at reduced opacity, behind the
newly-arriving field-lines text ("report date: missed 3 cycles" etc.) —
overlapping, hard-to-read text at the ~55s mark. Because `compile.py`
slows the whole B03 clip 2.27x to fill its narration-driven 22.1s beat
(original Manim scene ~9.8s), this crossfade — already borderline at
1.3s in real time — stretches to roughly 3s of overlapping ghost text on
screen, well past "a fraction of a frame."

Root-caused to the simultaneous FadeOut/FadeIn of two text blocks sharing
the same screen position — Manim renders both mid-fade at once, so any
sampled instant during the transition shows a blend. Fixed in
`scenes.py`'s `ENTB03Scene` by splitting the single simultaneous
`self.play(...)` into two sequential plays — `FadeOut` the old labels
fully (run_time 0.5s), then `FadeIn` the new field lines (run_time 0.8s)
— so the old text is completely gone before the new text starts
appearing, eliminating any overlap while preserving the total ~1.3s
transition pacing. Re-rendered B03 only, recompiled (all other beats
unchanged, reused from cache), re-ran GATE T (still PASS, no regression),
and re-sampled the entire B03 window at 1s resolution (23 frames,
48s-71s): clean fade to an empty card, then clean fade to the fully
resolved four-field card, no ghosting at any sampled instant. Re-checked
the split-card (both-directions) moment further into the beat as well —
clean throughout.

**Noted, not a defect introduced here:** `OutroCTA` renders on flat white
rather than the humanitarians cream ground — same shared-component
behavior already logged unremarked in sibling reels in this family (e.g.
`claude-for-legal--claude-liam-ai-inventory`, `claude-code--claude-liam-writing-rules`).

**Gates (final state):**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840x2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs)
- Gate V: PASS after fixing the B03 crossfade-ghosting defect above
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max
  -2.7 dB
- ffprobe: duration 100.000s; mp4 mtime (1788066677) newer than
  beat_sheet.json mtime (1788066091) — no sheet edits after this compile

**Playlist resolution:** family `claude-for-legal` does not match any
prefix key in `skills/make/hai-simple/loop/playlists.json` as a string
prefix. Per the map's documented fallback ("match SUBJECT.json's family,
or the hai-simple prefix"), matched the skill name itself: `hai-simple` is
a literal key in the map, resolving to **Claude Basics** — same resolution
already used for the sibling `ai-inventory` reel in this family.

Metadata file written: `claude-for-legal--claude-liam-entity-compliance.md`
(channel @HumanitariansAI, Playlist: **Claude Basics**, plus the direct
code link per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.
