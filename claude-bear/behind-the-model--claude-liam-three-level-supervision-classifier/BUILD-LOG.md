# BUILD-LOG — behind-the-model--claude-liam-three-level-supervision-classifier

## 2026-09-05 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/youtube/behind-the-model/claude-liam-three-level-supervision-classifier/beat_sheet.json`
(a CLI-explainer build asking Claude Code to write a Python Sheridan-Verplank
supervision classifier: 8 interaction descriptions, Level I/II/III + a gap
flag via the Anthropic API; demoed on Priya's 3 interactions — variable
rename, market-size citation, architecture proposal — on a usage/supervision
grid; revised to label the flag; re-run finds 4/8 flagged; closes with a
run-it-on-your-own-history next step).

**The call:** register CLI/Teardown -> Plain, general audience. Dropped the
source's Claude Code invocation, its Python script (the `gap_flag` boolean
line), and its named classifier model (`claude-3-5-haiku`) — no invented or
stale product specifics for a general viewer; the mechanism survives as
plain narration ("a simple rule: flag any interaction where the checking was
short but the task handed over the real decision"). B00 replaced the
source's `NikBearBrownOpen` title card with `BrutalistHesitantWriter` per
WRITER LAW: "same" -> "right" (typed first as "the same amount", corrected
to "the right amount"), directly seeding the carry-out. Added a wrong-guess
beat (B01: one fixed comfort level vs. matched to the task, falsified by
"renaming a variable and proposing a whole system architecture aren't the
same task") and an anchor (B03 -> B05: the source's own Priya grid,
literalized — her three interactions plotted on a usage/supervision grid,
two of three below the calibrated diagonal) per this factory's PHASE 1
structure, since the source's CLI spine (INTRO/PROBLEM/ASK/CODE/OUTPUT/
CHANGE/OUTPUT-revised/SUMMARY/NEXT-STEPS) carried neither in the Plain
sense. Added the required ONE-FLAG (B04): applying the 1978 Sheridan-
Verplank automation framework to an AI chat interface is this reel's
adaptation of their scale, not a claim from their own research — the
source treats the analogy as a given. Beat count compressed from the
source's ~9-body-beat CLI spine (B01-B08 plus YOURTURN) to a 9-beat Plain
spine (B00, B01-B05, BCRY, BHTF, BOUT) — the source's CODE beat is dropped
entirely (no code shown to a general audience) and its PROBLEM/ASK/OUTPUT/
CHANGE/OUTPUT-revised/SUMMARY/NEXT-STEPS beats collapse into the wrong-guess/
mechanism/anchor-planted/one-flag/anchor-payoff-and-both-directions arc.
Close re-skinned to `OutroCTA` / @HumanitariansAI with Liam's sign-off. See
QUESTION.md for the full source-mapping detail and CARRY-OUT.md for the
line and the wrong guess it defeats.

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 9 beats, free, `am_onyx`, first pass, no
   retries. B00 landed at 10.39s (clear of the >=9s TIMING LAW floor) on
   the first narration draft (33 words + `lead_silence_s: 0.8`). Durations:
   B00 10.39s, B01 21.61s, B02 22.81s, B03 20.27s, B04 22.68s, B05 22.29s,
   BCRY 6.78s, BHTF 18.54s, BOUT 4.25s (+1.0s tail).
2. Verified B00's correction on frame pulls at t=3.0/5.5/9.5s: "sam" (the
   truncated typing of "same") typed in accent color at t=3.0s, corrected to
   "right amount" by t=5.5s, full final question "Am I trusting AI / the
   right amount / every time?" settled well before the 10.4s cutoff.
   TIMING LAW satisfied on the first pass — no rewrite needed.
3. Wrote `scenes.py` (5 Manim scenes, reel-unique names `TLSB01Scene`
   through `TLSB05Scene`) and `render_scenes.py`; rendered all five in the
   foreground, no render failures.
4. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py` in the foreground
   (no `--concurrency` flag exists on this version, per the sibling reel's
   note — plain invocation used). All four beats native 3840x2160, no
   failures.
5. First `compile.py` pass -> 9/9 real (no slate), native 3840x2160 (THE 4K
   LAW), GATE AUDIO mean_volume -24.0 dB inline. Non-blocking WARNING:
   motion histogram graphic:5 remotion:4 (55%, over the ~40% pantry cap) —
   structural, same as prior siblings in this family: hai-simple's 4 fixed
   REMOTION slots (writer/carry-out/your-turn/outro) don't scale with body
   length.
6. GATE T (`type_check.py`) FAILED on the first pass: 3 pixel beats.
   - B01 kerning: title "ONE COMFORT LEVEL, OR MATCHED TO THE TASK?" (SANS
     Bold, font_size 22) tripped the pixel gap analyser at frac_over=0.30 —
     narrow glyphs (I/L/O/T) dragged mean letter width down so ordinary
     word-spacing read as oversized kerning gaps. Fix attempt 1: shortened
     to "ONE LEVEL, OR MATCHED BY TASK?" (still SANS) — frac_over dropped
     but stayed at 0.31, still FAIL. Fix attempt 2: switched the title font
     from SANS to SERIF (EB Garamond, font_size 30, the checker's own
     canned remediation) — frac_over dropped to 0.22, PASS.
   - B03 overflow: title "PRIYA'S AFTERNOON, ONE GRID" at `UP*3.5`
     (font_size 26) put its top 8px above the title-safe box's y>=54
     boundary. Fix: moved title to `UP*3.25` and `anchor_label` to
     `UP*2.6` — cleared the safe box, PASS.
   - B04 min-size: `applied_txt` ("-> applied to AI chat (this reel's
     adaptation)") and `flag_marker` ("FLAG — ONE") at font_size 15 were
     being auto-shrunk by `_fit_text` to fit their max_width, landing at a
     measured 14px < the 20px floor. Fix: shortened `applied_txt` to
     "-> applied to AI chat" at font_size 22 and `flag_marker` to "ONE
     FLAG: ADAPTATION" at font_size 20 — both now fit without triggering
     the auto-shrink, PASS.
   Re-rendered all three beats, recompiled, re-ran GATE T -> PASS, 0 FAILs.
7. Gate V (visual, manual): pulled 19 frames at 8s spacing across the full
   150.6s runtime plus a targeted re-check after the B03 fix, and read every
   one directly. One non-blocking visual defect found and fixed during this
   pass (not a GATE T failure — GATE T's automated bbox-overlap check
   passed throughout): B03's "propose an architecture" dot/label sat low
   enough that its dashed "FAR BELOW THE LINE" box and label crossed the
   x-axis line and arrowhead. Fix: raised the dot's data position, shrank
   the dashed box to fit inside the plotted range, and moved both labels to
   stack above the dot instead of below/beside it. Re-rendered B03,
   recompiled, re-verified with a fresh frame pull — clean separation from
   the axis, no overlap. All other beats: legible, correct content, no
   clipping; correct anchor payoff (B03->B05 grid, danger dots flagged,
   split into the two both-directions cards); correct carry-out/handoff/
   outro with `@HumanitariansAI` branding on B00 and BOUT.
8. Audio presence: `ffprobe` + `ffmpeg -af volumedetect` on the final
   master -> mean_volume **-24.0 dB**, max -3.0 dB. Master mtime
   (1788608117) is newer than beat_sheet.json mtime (1788607066).

**Gates (final state):**
- content-check: PASS (9 beats, no violations)
- frame-check: PASS (3840x2160, 9 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs), second pass (B01 font swap, B03 title reposition,
  B04 font-size/text-length fixes above)
- Gate V: PASS, second pass (B03 axis-overlap layout fix above; no other
  defects requiring a fix)
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max
  -3.0 dB
- ffprobe: duration 150.625s; mp4 mtime newer than beat_sheet.json mtime

**Playlist resolution:** family `behind-the-model` matches the map's
`behind-the-model` key directly in
`skills/make/hai-simple/loop/playlists.json`, resolving to **Behind the
Model** — no fallback needed.

Metadata file written:
`behind-the-model--claude-liam-three-level-supervision-classifier.md`
(channel @HumanitariansAI, Playlist: **Behind the Model**, plus the direct
code link per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate (after the GATE T
and Gate V fix passes above). Proceeding to Phase 4 (4K render + deliver.py)
in this same invocation.
