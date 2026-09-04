# BUILD-LOG — cwc-workshops--claude-liam-eval-audit-and-sweep

## 2026-09-01 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/cwc-workshops/youtube/claude-liam-eval-audit-and-sweep/beat_sheet.json`
— a Teardown skill-teardown cut of the Anthropic `eval-audit-and-sweep` skill.
Facts re-grounded directly against the skill's own SKILL.md (path recorded in
QUESTION.md) rather than trusted from the source narration: the source
Teardown cut had added an unsourced editorial claim — "the sweep grid is a
ranked artifact; the production system under real load is a different
world" — confirmed via the source's own REBUILD-LOG.md to be a deliberately
authored philosophical framing, not a quote from the skill file. This redo
drops that claim entirely. Kept from the source, verbatim in substance: the
two-phase audit-then-sweep order, enforced on any ambiguous-or-both request
because a sweep over a broken eval produces misleading numbers; no runnable
script — Claude reads the user's eval code plus the audit/sweep/tau2-bench
reference files and writes the glue; locating the golden set, scoring
function, and one-pass command; the audit checklist (task design, harness
design, metric hygiene, grader bias); the sweep as a full, non-trimmed
cross-product grid; and the <2-models boundary condition, where the skill's
own text says the result only ranks parameter settings within one model, not
"which model."

**Picked up mid-build, not started fresh.** SCRIPT.md, CARRY-OUT.md,
QUESTION.md, beat_sheet.json (14 beats), scenes.py, render_scenes.py, all
10 mp3s + timings.json, and media/B00.mp4 already existed on pickup from an
earlier invocation today. Verified each artifact rather than trusting it
(ffprobe on B00.mp4 confirmed both video and audio streams, 10.05s matching
timings.json) before continuing, per COMPLETION LAW. Gate T (`type_check.py`)
ran clean on the existing sheet before any further work: PASS, 0 FAILs.

**Beat count: 14** (source's Teardown cut is B00-B03/BVDT/BHTF/BOUT = 7).
Plain register's mandatory wrong-guess/anchor/both-directions/one-flag
structure re-segments the same source facts rather than padding with new
claims: B00 writer + S01 stakes + S02 wrong guess (planted) + S03 anchor
(planted) + S04 wrong guess broken with the misleading-numbers case + S05-S07
mechanism (glue code / locating the eval / audit checklist) + S08 anchor
payoff + S09/S10 both-directions mirror pair + BCRY carry-out + BHTF your-turn
+ BOUT outro. One-flag: zero flags used, correctly — every claim restates the
source SKILL.md's own text rather than this reel's inference (see SCRIPT.md
"Deliberately not claimed" for the full accounting).

**B00 WRITER LAW:** wrong guess — a newcomer assumes the eval skill jumps
straight to sweeping models for the best one. Typed text: "Claude's eval
skill picks my best model — it just sweeps? / What does it actually do?",
trigger "sweeps" → replacement "audits". Audio 10.05s clears the ≥9s TIMING
LAW floor. Frame-verified at t=9s (near end of beat): both the "audits"
correction and the full second line are typed and settled before cutoff.

**Render.** All 10 GRAPHIC beats (S01-S10) rendered via `render_scenes.py`
(manim -qk) — ran past the tool's 120s default foreground window and was
tracked as a background task; blocked on it explicitly (`while [ ! -f
manim/S10.mp4 ]` in a foreground Bash call) rather than ending the turn, per
the one-shot COMPLETION LAW. All 4 REMOTION beats (B00 pre-existing, BCRY/
BHTF/BOUT) rendered via `remotion_scenes.py` — BHTF and BOUT had in fact
already been rendered by the same earlier invocation; only BCRY needed a
fresh render this pass.

**Compile.** `compile.py` produced
`cwc-workshops--claude-liam-eval-audit-and-sweep.mp4` natively at 3840x2160
via the script's own 4K LAW (forces a clean master to 2160p by default) —
114.4s, 14/14 slots filled, content-check/frame-check/lane-check all PASS,
GATE AUDIO PASS (mean_volume -23.8 dB, max -3.0 dB, independently
re-verified via a standalone ffmpeg volumedetect pass). One non-blocking
compile WARNING: motion histogram graphic:10/remotion:4 (71% graphic) is
over MOTION.md's ~40% pantry-language guidance — not fixed, because 10
GRAPHIC body beats matches the hai-simple lineage's own documented shape
(`simple`'s "B01-B16 GRAPHIC" body per SKILL.md) and every other
`cwc-workshops--*`/`claude-tag-plugins--*` sibling redo in this loop carries
the identical ratio.

**Gate V.** Pulled frames at the settled end of every beat (not the
midpoint — early sampling at beat midpoints caught several Manim
in-progress animation states, e.g. S05's "your glue code" mid-type as
"your glue c" and S07's "GRADER BIAS" mid-fade, both of which resolved
cleanly by beat-end on a second pull; logged here so a future pass doesn't
mistake mid-animation frames for defects). All 14 beats legible at settled
end-of-beat, safe inset respected, no text overlap or truncation: B00's
correction visible, S03/S08 anchor pair identical composition as intended,
S09/S10 mirrored construction clean (three model-columns → one), BCRY quote
clean with no attribution line, BHTF composer card shows the full paste-ready
prompt and correct `@HumanitariansAI` folder label, BOUT outro clean on the
humanitarians skin. No defects found requiring a re-render.

**Delivery.** Master born natively 3840x2160 via compile.py's 4K LAW; copied
to `-4k.mp4` (no separate 4K re-render needed — the review-cut master already
meets the Fellows-facing resolution target). Playlist: Claude Basics
(`family: cwc-workshops` matches no `playlists.json` prefix; the `hai-simple`
skill-key entry resolves it, same fallback as every other `cwc-workshops--*`
sibling). `<slug>.md` written with chapters computed from actual
`actual_duration_s` cumulative offsets. `deliver.py --push` staged
DELIVERY/cwc-workshops--claude-liam-eval-audit-and-sweep/ (4K + description)
and committed+pushed the text artifacts to humanitarians-youtube
(commit `71428bd0`). DONE.
