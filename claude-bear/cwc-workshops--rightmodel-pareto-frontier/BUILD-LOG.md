# BUILD-LOG — cwc-workshops--rightmodel-pareto-frontier

## 2026-09-01 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/cwc-workshops/youtube/rightmodel-pareto-frontier/beat_sheet.json`
— a Teardown worked-example cut (Code with Claude 2026 Workshop material) on
choosing between Opus/Sonnet/Haiku via the pareto cost/accuracy frontier.
This is not a skill teardown (no SKILL.md to re-ground against) — the source
is its own worked example, and its own narration already self-flags the
pricing/quality figures as illustrative ("These numbers are relative.
Always check current pricing before you build."). This redo keeps that
exact caveat, compressed into the reel's ONE-FLAG beat (S07), and keeps
every other fact and number unchanged from the source: the customer-support
classification example (Opus 98%/$0.08 per call, Sonnet 90%/$0.04, Haiku
82%/$0.01), the per-million-token cost table (Opus $15/$75, Sonnet $3/$15,
Haiku $0.25/$1.25), and the $4,000-per-100k-calls saving.

Started fresh — the reel dir held only SUBJECT.json on pickup. Built from
scratch: QUESTION.md, CARRY-OUT.md, SCRIPT.md, beat_sheet.json (14 beats),
scenes.py (10 Manim scenes), render_scenes.py, all 14 mp3s via
generate_audio_kokoro.py, all Remotion beats via remotion_scenes.py.

**Beat count: 14** (B00 + S01-S10 + BCRY + BHTF + BOUT), matching the
hai-simple lineage's documented shape and this reel family's other
`cwc-workshops--*` siblings. The source Teardown cut runs B00-B10 +
BVDT/BHTF/BOUT (also 14 beats including bookends); this redo re-segments
the same worked example onto Plain's mandatory
wrong-guess/anchor/both-directions/one-flag structure. Six-move audit: S01
stakes; S02 wrong guess (planted, grab an extreme) -> S04 broken (both
extremes lose on the customer-support eval); S03 anchor (the frontier
curve, abstract) -> S08 anchor payoff (same axes+curve, real named dots);
S05-S07 mechanism (the sweep, the frontier rule, the one-flag numbers
table); S09/S10 both-directions mirror pair (high threshold keeps only
Opus, low threshold keeps only Haiku); BCRY carry-out.

**B00 WRITER LAW:** wrong guess — a newcomer assumes the smartest model
(Opus) is always the right pick. Typed text: "Just pick the smartest
model? / Opus wins on accuracy. / Which model wins here?", trigger
"smartest" -> replacement "frontier". First render's on-screen text ("So
which model actually belongs there?") did not finish typing before the
beat's audio-driven cutoff (11.16s) — frame-verified at t=10.9s showed
"...belongs ther|" mid-character. Shortened the third line to "Which model
wins here?" and re-rendered; frame-verified again at t=10.9s of the 11.16s
clip: all three lines fully typed and settled, "frontier" correction clean
and visible, well before cutoff. Logged here so a future pass doesn't
re-introduce a text length that outruns the audio window.

**Render.** All 10 GRAPHIC beats (S01-S10) rendered via `render_scenes.py`
(manim -qk) — ran past the tool's foreground timeout and was moved to a
background task; blocked on it explicitly with a `while` loop polling for
`manim/S10.mp4` in a foreground Bash call rather than ending the turn, per
the one-shot COMPLETION LAW. All 4 REMOTION beats (B00, BCRY, BHTF, BOUT)
rendered via `remotion_scenes.py` in the foreground.

**Compile.** First `compile.py` run used `--review`, which unconditionally
names its output `<slug>-slate.mp4` regardless of whether any beat is a
real placeholder (confirmed by reading the script: `--review` controls
resolution and the review-label overlay, not slate status) — all 14 beats
were already real (VIDEO/MANIM), so this was not a defect, just the wrong
invocation for a final. Recompiled without `--review`: 4K LAW forced the
clean master to 3840x2160 natively, content-check/frame-check/lane-check
all PASS, GATE AUDIO PASS (mean_volume -23.9 dB, independently re-verified
via a standalone `ffmpeg -af volumedetect` pass: mean -23.9 dB, max -3.0
dB — well above the -40 dB floor). Wrote
`cwc-workshops--rightmodel-pareto-frontier.mp4`, 134.8s, 14/14 slots
filled. Two non-blocking WARNINGs: S07's manim clip needed 3.8x slow-mo to
fill its 15.4s beat (extreme slow-mo per compile.py's own threshold, logged
to replace_log.md but not fixed — the beat is legible and the content is
correct, just longer than the clip's native animation length); and the
motion histogram (graphic:10/remotion:4, 71% graphic) exceeds MOTION.md's
~40% pantry-language guidance, matching every other `cwc-workshops--*`
sibling redo in this loop and the hai-simple lineage's own documented
"B01-B16 GRAPHIC" body shape.

**Gate V.** Pulled frames at the settled end of every beat (computed from
cumulative `actual_duration_s` + `tail_silence_s`; `lead_silence_s` is not
implemented anywhere in the current audio/compile pipeline — confirmed via
grep — so it contributes nothing to beat duration, and an initial
frame-pull pass using the SKILL.md-documented lead+tail formula landed on
the wrong timestamps and pulled blank/mid-transition frames; recomputed
using actual_duration_s + tail_silence_s only, which matched the compiled
134.8s total exactly). All 14 beats legible at settled end-of-beat, safe
inset respected: B00's "frontier" correction visible and the full three-line
text settled; S03/S08 anchor pair identical axes+curve composition as
intended (abstract dots, then real named Opus/Sonnet/Haiku dots); S09/S10
mirrored construction clean (same axes, opposite threshold outcome); BCRY
quote clean with no attribution line; BHTF composer card shows the full
paste-ready sweep prompt and correct `@HumanitariansAI` folder label; BOUT
outro clean on the humanitarians skin. One defect found and fixed: S06's
"ON THE FRONTIER" label overlapped the ascending dashed frontier line
(the curve crossed through the text). Fixed by shifting the label up and
left in scenes.py, re-rendered S06 only, re-verified clean, recompiled
(only S06 re-rendered — the other 13 beats were cached). Zero blockers
remain.

**Delivery.** Master born natively 3840x2160 via compile.py's 4K LAW; will
be copied to `-4k.mp4` for the Fellows-facing delivery target (no separate
4K re-render needed — the review-cut master already meets the target
resolution). Playlist: Claude Basics (`family: cwc-workshops` matches no
`playlists.json` prefix directly; the `hai-simple` skill-key entry resolves
it, same fallback as every other `cwc-workshops--*` sibling in this loop).
`<slug>.md` written with chapters computed from actual cumulative
`actual_duration_s`/`tail_silence_s` offsets.
