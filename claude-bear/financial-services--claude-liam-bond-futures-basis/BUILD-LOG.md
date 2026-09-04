# BUILD-LOG — financial-services--claude-liam-bond-futures-basis

## 2026-09-01 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/financial-services/youtube/claude-liam-bond-futures-basis/beat_sheet.json`.

**Source-gap finding (logged, not asked — see QUESTION.md for full detail):**
like its same-day sibling `financial-services--claude-liam-3-statement-model`,
this source sheet is NOT a placeholder shell. Its narration already states
the `bond-futures-basis` skill's real facts: it prices bond futures,
identifies the cheapest-to-deliver (CTD) bond, and compares against yield
curves to assess delivery-option value and basis-trading opportunities;
triggered when analyzing bond futures, computing the basis, identifying
CTD bonds, calculating implied repo rates, or evaluating basis trades.
The `source_skill` path it names
(`/Users/bear/Documents/CoWork/bear-textbooks/.../plugins/partner-built/lseg/skills/bond-futures-basis/SKILL.md`)
does not exist on this machine (different machine's home directory), but
no reconstruction was needed — the source beat_sheet.json's own narration
carried enough to redo faithfully.

**The call:** register re-registered Teardown -> Plain. Source's B03 framed
"Claude's job" and "what it gets right / where it bites" as a design-tell
verdict — Teardown language. Plain instead states the mechanism (price a
bond, compute its implied repo rate) and its two failure directions
(cheapest is not profitable; expensive today is not excluded forever) as
properties of the practice, never a verdict on the skill's design. Source's
BVDT verdict recap folded into a dedicated BCRY carry-out beat per
CARRY-OUT LAW. B00 replaced the source's `ClaudeComposerAsk` cold open
(itself already Remotion, not AI-video/puppet — no NO-GENAI violation in
the source) with `BrutalistHesitantWriter` per WRITER LAW: "feel" ->
"the math" — the naive assumption that finding the cheapest bond takes a
trader's feel, corrected to: it takes a computed comparison. Added a
wrong-guess beat (B01: trader's feel vs. priced ranking, falsified by "ask
it to favor a bond because you like its prospects and it won't") and an
anchor (B02 -> B03: futures price + conversion factor -> delivery cost ->
implied repo rate, planted then paid off) per this factory's PHASE 1
structure requirement — the source's Teardown shape (anatomy / pipeline /
design-tell / verdict) carried neither. Close re-skinned to `OutroCTA` /
@HumanitariansAI with Liam's sign-off. Kept the source's 7-beat count (B00,
B01, B02, B03, BCRY, BHTF, BOUT) per the redo contract.

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 7 beats, free, `am_onyx`, first pass, no
   retries needed. Durations: B00 9.81s, B01 21.38s, B02 16.62s, B03
   22.40s, BCRY 13.48s, BHTF 18.09s, BOUT 4.46s (+1.0s tail).
2. First B00 render (34-word narration, `lead_silence_s: 0.8`, 4-line
   writer text "How does Claude / pick the cheapest / bond to deliver — /
   by feel?") produced a video whose correction never lands: at t=9.5s
   (near the 9.83s cutoff) the writer is still mid-typing "fe" of "feel,"
   never reaching the backspace-and-replace to "the math." Root cause: the
   text was too long (4 lines, ~10 words before the trigger word) for the
   fixed charMs=55/hesitateBetween=22 typing budget inside a ~9.8s window.
   Fixed by shortening the writer text to 3 lines ("The cheapest bond / to
   deliver — / by feel?", same trigger/replacement params as the
   `3-statement-model` sibling) and re-rendering. Re-verified via frame
   pulls at t=5.0/7.0/9.5s: "feel" visible mid-type in accent color at
   7.0s, fully backspaced and replaced with "the math?" by 9.5s, legible
   with margin before the 9.83s cutoff. TIMING LAW satisfied on the second
   pass.
3. Wrote `scenes.py` (3 Manim scenes, reel-unique names `BFBB01Scene` /
   `BFBB02Scene` / `BFBB03Scene`) and `render_scenes.py`; rendered all
   three in the foreground on the first pass, no render failures.
4. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py` in the foreground.
   The first invocation (no `--only`) hit the shell's 2-minute inline
   timeout mid-render (exit 143) after B00 had already fully rendered;
   confirmed via `ps aux` that no orphaned Remotion/Chromium/node render
   process was left running (the timeout killed the whole process tree
   cleanly) before continuing. Re-ran with a longer timeout and it
   completed BCRY/BHTF/BOUT cleanly (B00 later re-rendered once more after
   the TIMING LAW fix in step 2, with `--only B00 --force`).
5. First `compile.py` pass -> 7/7 real (no slate), 3840x2160 (THE 4K LAW),
   mean_volume -24.0 dB (GATE AUDIO pass on the first compile).
6. GATE T (`type_check.py`) FAILED on the first pass: B03 had a text run
   at 12px, under the 20px/1.9%-of-1080px floor. Root cause: the small
   "FUT"/"BOND"/"REPO" card labels (font_size=17) sat inside a VGroup that
   gets `.scale(0.6)`'d when the anchor composition shrinks and slides up
   to make room for the both-directions split — post-scale they fell
   under the floor. Fixed by bumping those labels to font_size=30
   pre-scale, plus adding margin to the other small B03 labels
   (left_txt/right_txt 18->20, left_right_word 21->23, left_label/
   right_label/right_note 17->19) for headroom. Re-rendered B03,
   recompiled: GATE T -> PASS, 0 FAILs, second pass.
7. Gate V (visual, manual): pulled frames every 4s across the full 107.25s
   runtime (27 frames) and read every one directly. No defects found —
   B00's correction lands cleanly, B01's struck trader's-feel side and lit
   priced-ranking side are legible with no overlap, B02/B03's anchor
   travels and returns correctly with the both-directions split readable,
   BCRY/BHTF/BOUT render as expected. One non-blocking cosmetic note
   (not a defect introduced here, same disposition as the
   `3-statement-model` sibling and other family reels): `OutroCTA` renders
   on flat white rather than the humanitarians cream ground — a known
   shared-component behavior, already logged unremarked elsewhere in this
   family.
8. Audio presence: `ffprobe` + `ffmpeg -af volumedetect` on the final
   master -> mean_volume **-24.0 dB**, max -2.7 dB. Master mtime
   (1788262259) is newer than beat_sheet.json mtime (1788261989).

**Gates (final state):**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840x2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs), second pass (B03 font-size fix above)
- Gate V: PASS, first pass after the GATE T fix — no defects remain
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max
  -2.7 dB
- ffprobe: duration 107.25s; mp4 mtime newer than beat_sheet.json mtime

**Non-blocking warning (compile.py):** motion histogram remotion:4
graphic:3 — remotion at more than half of beats. Structural, not a defect:
hai-simple's mandated shape is B00 (writer) + BCRY + BHTF (Your Turn) +
BOUT (outro) all REMOTION by skill contract, against 3 GRAPHIC body beats
for this 7-beat reel — same disposition as every other short hai-simple
reel in this family.

**Playlist resolution:** family `financial-services` does not match any
prefix key in `skills/make/hai-simple/loop/playlists.json`. Per the map's
documented fallback ("match SUBJECT.json's family, or the hai-simple
prefix"), fell through to matching the skill name itself: `hai-simple` is
a literal key in the map, resolving to **Claude Basics** — same resolution
as the `3-statement-model`, `ai-inventory`, and `handbook-updates` sibling
reels.

Metadata file written:
`financial-services--claude-liam-bond-futures-basis.md` (channel
@HumanitariansAI, Playlist: **Claude Basics**, plus the direct code link
per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate (after the two fix
passes above: B00 timing, B03 type-check). Proceeding to Phase 4 (4K
render + deliver.py) in this same invocation.

## 2026-09-01 — Phase 4 delivery

Master is already 3840x2160 (THE 4K LAW in compile.py forces any clean,
non-`--review` master to 4K), so the Fellows-facing 4K file is the same
render, copied to the `-4k` filename `deliver.py` expects:

```
cp financial-services--claude-liam-bond-futures-basis.mp4 \
   financial-services--claude-liam-bond-futures-basis-4k.mp4
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Outbox staged: `DELIVERY/financial-services--claude-liam-bond-futures-basis/`
(4K mp4 + description.md). Repo: committed + pushed to
`humanitarians-youtube/claude-bear/financial-services--claude-liam-bond-futures-basis/`
(README.md, beat_sheet.json, SCRIPT.md, SUBJECT.json, BUILD-LOG.md,
CARRY-OUT.md, QUESTION.md — no mp3/mp4), commit `c1ce346d`.

**Status: DELIVERED.** Both delivery targets staged/pushed. Reel complete.
