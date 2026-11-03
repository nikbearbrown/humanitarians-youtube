# BUILD-LOG — claude-for-legal--claude-liam-integration-management

## 2026-08-30 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-for-legal/youtube/claude-liam-integration-management/beat_sheet.json`.

**Source-gap finding (logged, not asked — see QUESTION.md for full detail):**
the source sheet is fully "built" (7 beats, all marked VIDEO/filled, dated
2026-08-03) but its narration text carries literal, never-filled template
placeholders (`>`) at every point where the actual skill-specific fact
should be: `"the skill is integration-management. >."`, `"Claude's job:
>."`, `"The SKILL.md is the spec — >."`, `"I want to >."` Its
`source_skill` field points at
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/corporate-legal/skills/integration-management/SKILL.md`
— searched the entire `books/` tree on this machine; neither that file nor
a `corporate-legal` folder exists anywhere. Same defect class already
logged on the `ai-inventory`/`ai-tool-handoff`/`aia-generation`/
`fto-triage`/`gap-surfacer`/`handbook-updates` siblings in this factory.

**The call:** rather than block on a missing human answer, reconstructed
the account from the two real, load-bearing phrases the source DID
contain (not placeholders) — B00's shot output and BVDT's artifactLines
both read `"Post-closing M&A integration tracker — phased workplan,"`.
Built a generic, defensible account of what a post-merger-integration
tracking practice looks like (workstream / owner / phase / status) from
that phrase, per the fresh-script Phase 1 rule ("when in doubt, describe
behavior generically") rather than inventing specific tool names, UI, or
output format. No fact in the resulting script is Claude-specific or
unverifiable.

Register re-registered Teardown -> Plain: the source's B03 framed
"Claude's job" and "what it gets right / what it bites" as a design-tell
verdict — Teardown language. Plain instead states the mechanism (the
tracker's four fields) and its failure modes (tracked is not on schedule;
staffed today is not permanent) as properties of the practice, never a
verdict on any specific skill's design. Source's BVDT verdict recap folded
into a dedicated BCRY carry-out beat per CARRY-OUT LAW (same disposition
as prior redos in this factory). B00 replaced the source's
`ClaudeComposerAsk` cold open with `BrutalistHesitantWriter` (WRITER LAW:
"plan" -> "tracker" — the naive assumption that post-close work starts
with a one-time document, corrected to the fact that it needs a living
tracker). Close re-skinned to `OutroCTA` / @HumanitariansAI with Liam's
sign-off. Added an anchor (B02 -> B03: the vendor-contract workstream
marked day-thirty with no owner assigned, then logged with the same four
fields as everything else) and a both-directions beat (B03) per this
factory's PHASE 1 structure requirement — the source (being unfilled)
carried neither. Kept the source's 7-beat shape (B00 writer -> B01
stakes/wrong-guess -> B02 mechanism/anchor-planted -> B03 anchor-payoff/
both-directions -> BCRY carry-out -> BHTF handoff -> BOUT outro).

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 7 beats, free, `am_onyx`. Durations: B00
   10.05s, B01 20.07s, B02 14.66s, B03 18.58s, BCRY 7.70s, BHTF 20.39s,
   BOUT 4.59s.
2. Wrote `scenes.py` (3 Manim scenes, reel-unique names `INTMB01Scene`/
   `INTMB02Scene`/`INTMB03Scene`, adapted from the `ai-inventory` sibling's
   card/chip renderer) and `render_scenes.py`; rendered all three in the
   foreground on the first attempt.
3. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py` in the foreground.
   The combined call exceeded the shell tool's 120s inline default twice in
   a row (B00 and BCRY had already landed by the second timeout); per the
   ONE-SHOT/COMPLETION LAW, re-ran with an explicit longer foreground
   timeout (300s) rather than backgrounding the render — the process had
   already finished BHTF/BOUT by then ("filled already (skip)"), confirmed
   exit 0 before proceeding.
4. B00 verified directly: `media/B00.mp4` = 10.07s (meets the >=8s TIMING
   LAW floor). Pulled frames at t=4s/9s: "plan" is visible mid-typing in
   accent orange at t=4s, and the correction to "tracker" is complete and
   legible with the full question typed out by t=9s.
5. First `compile.py` pass -> 7/7 real (no slate), 3840x2160 (THE 4K LAW),
   mean_volume -24.1 dB (already passing GATE AUDIO).

**GATE T (type_check.py) — one finding, confirmed false positive, not a
real defect:**

- First pass: FAIL (1 pixel beat). B02's kerning check flagged the SANS
  title "FOUR FIELDS — THE ANCHOR" (max inter-glyph gap 90px vs. threshold
  15px) — the identical string, identical false-positive class already
  documented and exempted for the `ai-inventory` sibling's `AINVB02Scene`
  (the em-dash glyph renders as a much narrower ink run than the
  surrounding letters, dragging the derived `mean_w` down). Pulled the
  exact frame the checker samples (t=dur*0.5 of the raw `manim/B02.mp4`)
  and read it directly: the title renders as one cleanly kerned, fully
  legible run. Registered `INTMB02Scene` in `KERNING_EXEMPT_PATTERNS` with
  the same documentation style as the `AINVB02Scene` entry.
- Second pass: **PASS (0 FAILs)**.

**Gate V (visual) — one real defect found and fixed:**

Pulled 19 frames every 5s across the full 97.0s runtime and read them
directly. Found one real defect at frame 10 (~t=45s, inside B03): the
outgoing dim-card labels ("vendor contracts — day 30" / "(no owner
assigned)") and the incoming four-field text ("task: ...", "owner: ...",
"phase: ...", "status: ...") were animated as a simultaneous
`FadeOut`/`FadeIn` crossfade at the same screen position, and — slowed
1.91x by `compile.py`'s beat-duration stretch — the resulting ~2.5s overlap
window rendered as garbled, unreadable double-exposed text. Root-caused to
`INTMB03Scene`'s single combined `self.play(FadeOut(...), FadeOut(...),
dim_card.animate..., FadeIn(field_lines), run_time=1.3)` call. Fixed by
splitting it into two sequential `self.play()` calls — old labels fully
fade out first (0.6s), then the new field lines fade in (0.7s) — so the
two texts never occupy the frame at the same time. Re-rendered B03 only,
recompiled, re-ran GATE T (still PASS, no regression), and re-pulled
frames at 1s granularity across the full t=42–48s transition window: the
old card fades to nothing cleanly, then the four-field card fades in
cleanly, no overlap anywhere. Re-checked audio (mean_volume unchanged,
-24.1 dB) and confirmed the master's mtime is newer than
`beat_sheet.json`'s after the recompile. All other 18 frames (B00, B01,
B02, rest of B03, BCRY, BHTF's composer card, BOUT) were clean on the
first pass — legible, no overlap, safe insets respected.

**Noted, not a defect introduced here:** `OutroCTA` (BOUT) renders on flat
white rather than the humanitarians cream ground — same shared-component
behavior already logged unremarked on sibling reels in this family (e.g.
`claude-for-legal--claude-liam-ai-inventory`).

**Gates (final state):**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840x2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs) after registering the confirmed em-dash kerning
  false-positive exemption above
- Gate V: PASS after fixing the B03 crossfade-overlap defect above
- GATE AUDIO: PASS — mean_volume **-24.1 dB** (ffmpeg volumedetect), max
  -3.1 dB
- ffprobe: duration 97.042s; mp4 mtime (1788089748) newer than
  beat_sheet.json mtime (1788089394)

**Non-blocking warning (compile.py):** motion histogram remotion:4
graphic:3 — remotion at more than half of beats. Structural, not a defect:
hai-simple's mandated shape is B00 (writer) + BCRY + BHTF (Your Turn) + BOUT
(outro) all REMOTION by skill contract, against 3 GRAPHIC body beats for
this 7-beat reel — same disposition as every other short hai-simple reel in
this family.

**Playlist resolution:** family `claude-for-legal` does not match any
prefix key in `skills/make/hai-simple/loop/playlists.json`. Per the map's
documented fallback ("match SUBJECT.json's family, or the hai-simple
prefix"), fell through to matching the skill name itself: `hai-simple` is
a literal key in the map, resolving to **Claude Basics** — consistent with
every delivered sibling in this family.

Metadata file written: `claude-for-legal--claude-liam-integration-management.md`
(channel @HumanitariansAI, Playlist: **Claude Basics**, plus the direct
code link per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.

## 2026-08-30 — Phase 4 delivery

Master is already 3840x2160 (THE 4K LAW in compile.py forces any clean,
non-`--review` master to 4K), so the Fellows-facing 4K file is the same
render, copied to the `-4k` filename `deliver.py` expects.

```
cp claude-for-legal--claude-liam-integration-management.mp4 \
   claude-for-legal--claude-liam-integration-management-4k.mp4
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Outbox staged: `DELIVERY/claude-for-legal--claude-liam-integration-management/`
(4K mp4 + description.md). Repo: committed + pushed to
`humanitarians-youtube/claude-bear/claude-for-legal--claude-liam-integration-management/`
(README.md, beat_sheet.json, SCRIPT.md, SUBJECT.json, BUILD-LOG.md,
CARRY-OUT.md, QUESTION.md — no mp3/mp4), commit `9487e1b4`.

**Status: DELIVERED.** Both delivery targets staged/pushed. Reel complete.
