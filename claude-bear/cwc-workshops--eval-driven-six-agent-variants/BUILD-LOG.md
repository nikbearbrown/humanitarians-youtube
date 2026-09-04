# BUILD-LOG — cwc-workshops--eval-driven-six-agent-variants

## 2026-09-01 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/cwc-workshops/youtube/eval-driven-six-agent-variants/beat_sheet.json`
— a Teardown workshop-teardown cut of the "Eval-Driven Agent Development"
Code with Claude 2026 workshop (a PowerPoint-writing Claude Managed Agent,
graded two ways and iterated across four rounds).

**Facts re-grounded against the primary source, not trusted from the source
narration.** The source's B03/B04 body beats describe the workshop loosely
correctly (typography/diagram/QA-loop rounds, structural+semantic grading),
but its B06 beat (`CwcVariantImprovementWaterfall`) narrates a fabricated
six-step cumulative climb — "naive… ReAct reasoning loop… memory store…
critic pass… tool planning… output formatting constraints," 42% to 81%.
None of that exists in the workshop repo
(`/Users/nik/Documents/Cowork/anthropics/cwc-workshops/eval-driven-agent-development`):
it's a slide-deck agent, not a ReAct/tool-planning agent, and there is no
`runs/` directory anywhere with recorded scores to source any percentage
from. Verified directly against the repo's own files: `src/graders/all.ts`
(7 code graders — produced-result, slide-count, slides-with-image,
text-heavy-slides, cluttered-slides, small-font-slides, emoji-count; 5
LLM-judge graders — text, image, layout, color, title-body-coherence),
`tasks.json` (5 fixed tasks), `src/eval-runner.ts` (deltas are always
measured against one pinned baseline, not the previous run), and
`solutions/01-polish.agent.yaml` through `04-model-swap.agent.yaml` (four
real rounds on a naive baseline; round 4 explicitly its own file's
description: "Tests the model lever vs the prompt lever" — a revert to the
plain prompt on a different model, not a fifth stacked prompt tweak). This
redo drops the fabricated waterfall and every invented label entirely. Full
accounting in QUESTION.md and SCRIPT.md's "Deliberately not claimed."

**The count problem, and how it was handled.** The workshop repo supports
five real configurations (a naive baseline plus four rounds), not six, and
the fourth round is a lever-isolation test rather than another additive
prompt change. SUBJECT.json's given title/question and the source's own
title both say "Six Agent Variants." Rather than silently repeat a count the
primary source doesn't support, or contradict the given title inside the
body (which would read as a self-contradicting reel), no beat in the body
asserts a specific total variant count — the mechanism (two-layer eval,
four real rounds, the prompt-vs-model boundary) is stated in full, and the
given title is used only as the episode's name at BOUT, exactly as handed
down. Logged here per the honesty rules rather than left unstated.

**Beat count: 14** — B00 writer + S01 stakes + S02 wrong guess (planted) +
S03 anchor (planted: the mandatory-diagram grader) + S04 wrong guess broken
(a font-size-floor violation invisible to a glance, caught by the code
grader in milliseconds) + S05-S07 mechanism (code layer, judge layer, the
three additive rounds) + S08 anchor payoff (round 4's model swap empties the
same diagram grader) + S09/S10 both-directions mirror pair + BCRY carry-out
+ BHTF your-turn + BOUT outro. One-flag: zero flags, correctly — every claim
restates the workshop repo's own files.

**B00 WRITER LAW:** naive claim "my new prompt looks better. Done." — the
classic vibe-check wrong guess (a glance, not a measurement), trigger
"looks" → replacement "scores". Audio 9.98s clears the ≥9s TIMING LAW floor
(narration 34 words + 0.8s lead silence). Frame-verified at t=9.5s: both the
"scores" correction and the full second line are typed and settled before
cutoff.

**Render.** All 10 GRAPHIC beats (S01-S10) rendered via `render_scenes.py`
(manim -qk); the command exceeded the tool's 120s foreground window and was
auto-backgrounded, so it was blocked on explicitly (`while [ ! -f
manim/S10.mp4 ]` in a foreground Bash call) rather than ending the turn, per
the one-shot COMPLETION LAW. All 4 REMOTION beats (B00/BCRY/BHTF/BOUT)
rendered via `remotion_scenes.py`, foreground.

**Compile.** `compile.py` produced the master natively at 3840×2160 via the
script's 4K LAW — 153.6s, 14/14 slots filled, content-check/frame-check/
lane-check all PASS, GATE AUDIO PASS (mean_volume −23.9 dB, max −2.9 dB,
independently re-verified via a standalone ffmpeg volumedetect pass). Two
non-blocking compile WARNINGs, both consistent with lineage precedent: an
extreme slow-mo stretch on S07 (4.3s clip into a 15.5s beat, logged to
`replace_log.md`, not fixed — the same class of warning the sibling
`claude-liam-eval-audit-and-sweep` build left unfixed), and the motion
histogram (graphic:10/remotion:4, 71% graphic) exceeding MOTION.md's ~40%
guidance — not fixed, because every `cwc-workshops--*` hai-simple sibling in
this loop carries the identical ratio (10 GRAPHIC body beats matches the
`simple` lineage's own documented "B01-B16 GRAPHIC" body shape).

**Gate V — four real defects found and fixed, then re-rendered and
recompiled.** Pulled frames at the settled end of every beat (2fps-style
spot pulls via ffmpeg -ss, not the midpoint) and read them:

1. S04 — the "10pt FLOOR" dashed line and the slide's solid border line both
   crossed directly through the "10" digits, degrading legibility. Fixed by
   moving the floor label above the dashed line instead of beside it, and
   insetting the dashed line off the slide's vertical borders.
2. S05 — the five-card check row bled to the literal last pixel of the
   frame (rightmost non-background pixel at x=3839/3840 — a hard safe-inset
   violation), and the gear icon overlapped the first card ("SLIDE COUNT")
   because its position was computed without accounting for the actual card
   row width. Fixed by shrinking card/gear sizing and recomputing positions;
   re-verified via pixel scan after the fix (margins 389px right / 239px
   left at 3840 width).
3. S07 — the QA-loop magnifying-glass icon overlapped the "P" in "LOOP".
   Fixed by moving the icon to the card's lower-right corner, clear of the
   text baseline.
4. S10 — "TITLE-BODY" text overflowed its containing ring on both sides
   (the ring was sized for a shorter label). Fixed by sizing the ring as an
   ellipse keyed to the actual rendered text width.

All four re-rendered via `render_scenes.py <beat>`, then `compile.py`
re-run clean (content/frame/lane/audio all PASS again, same 153.6s runtime).
Re-pulled and re-read all four frames after the fix: zero defects remaining.
Every other beat (B00, S01, S02, S03, S06, S08, S09, BCRY, BHTF, BOUT)
read clean on the first pass — legible, safe inset respected, no overlap.

**Delivery.** Master born natively 3840×2160 via compile.py's 4K LAW;
copied to `-4k.mp4` (no separate 4K re-render needed — the review-cut master
already meets the Fellows-facing resolution target). Playlist: Claude Basics
(`family: cwc-workshops` matches no `playlists.json` prefix; the `hai-simple`
skill-key entry resolves it, same fallback as every other `cwc-workshops--*`
sibling). `<slug>.md` written with chapters computed from actual
`actual_duration_s` cumulative offsets. DONE.
