# SHOTLIST — two-threads-one-week (v2 revision — "a log, not a highlight reel")
# Typed work order per beat. Gate F open. Pass 1 (pre-audio-lock estimates).

## OPEN — INTRO (B00–B01)

B00 · ClaudeComposerAsk (Remotion)
  action: render → media/B00.mp4
  props: greeting="Hola,", command="claude \"show me, with real code, a log
         of what I actually worked on this week...\"", output=[3 lines]
  show: composer types → running indicator → output lands
  status: RENDERABLE

B01 · Manim B01_AgrimaIntro (scenes.py) — NEW this revision, replaces
      B01_TwoThreads
  action: render → manim/B01.mp4
  show: presenter card — "Hi, I'm Agrima." + short summary of the week's
        two threads. Functions as both the personal intro AND the "why"
        beat (per user request to lead with the introduction).
  status: RENDERABLE

## ACT I — the first pass (B02–B04)

B02 · ClaudeComposerAsk (Remotion)
  action: render → media/B02.mp4
  props: greeting="The ask,", command=(write weekly_log_v1.py prompt)
  status: RENDERABLE

B03 · ClaudeCodeBeat (Remotion)
  action: render → media/B03.mp4
  props: title="weekly_log_v1.py", code=(trimmed real source), sparkLine
  status: RENDERABLE

B04 · Manim B04_LogV1 (scenes.py)
  action: render → manim/B04.mp4
  show: 2 log columns (WRITING, LOON PROJECT), every item + its real
        status ("done"/"published"/"in progress") — from the REAL run of
        weekly_log_v1.py. No tally, no scoring.
  status: RENDERABLE

## ACT II — the revision (B05–B07)

B05 · ClaudeComposerAsk (Remotion)
  action: render → media/B05.mp4
  props: greeting="The change,", command=(turn the dump into a log prompt)
  status: RENDERABLE

B06 · ClaudeCodeBeat (Remotion)
  action: render → media/B06.mp4
  props: title="weekly_log_v2.py", code=(trimmed real source), sparkLine
  status: RENDERABLE

B07 · Manim B07_LogV2 (scenes.py)
  action: render → manim/B07.mp4
  show: SAME 2 log columns, now each headed by a "* highlight: ..." line
        (the thread's standout, computed for real) — from the REAL run of
        weekly_log_v2.py
  status: RENDERABLE

## CLOSE — SUMMARY / HANDOFF / OUTRO (B08–B10)

B08 · Manim B08_Summary (scenes.py)
  action: render → manim/B08.mp4
  show: WRITING + LOON PROJECT recap cards, closing tagline "Not a
        highlight reel — the actual log." (no numeric tally this revision)
  status: RENDERABLE

B09 · ClaudeComposerAsk (Remotion) — HANDOFF LAW
  action: render → media/B09.mp4
  props: greeting="Your turn.", command=(viewer prompt: turn your week
         into a log with a standout per thread, not a highlight reel)
  status: RENDERABLE

B10 · ClaudeTitleOutro (Remotion)
  action: render → media/B10.mp4
  props: title="Two Threads, One Week: The Work Log.",
         handle="@HumanitariansAI",
         subline="built with Claude, taken apart"
  status: RENDERABLE

## Notes

- No pantry / archival stills used in this reel — every visual is either a
  Claude-skin Remotion composer/code/outro beat or a from-scratch Manim
  scene built for this reel (scenes.py). No open pantry slots.
- All 4 Manim scenes render at 4K by default via `./art run` (HEIGHT=2160).
- `@HumanitariansAI` in B00/B02/B05/B09/B10 matches the branding precedent
  set on the ai-support-shift reel.
- `weekly_log_v1.py` and `weekly_log_v2.py` are real, runnable scripts
  checked into this folder — both were actually executed to capture the
  OUTPUT-beat transcripts shown in B04/B07. They replace the prior
  `weekly_recap_v1.py` / `weekly_recap_v2.py` pair from the v1 build.
- v2 revision (this build): added the B01 presenter-intro beat, replacing
  the prior PROBLEM/B01_TwoThreads beat; dropped the audit()/tally
  framing throughout — B04/B07/B08/B10 no longer state a numeric
  "N of 8 shipped" line. All 8 real items are still shown in every log
  beat (nothing hidden), per explicit user instruction to keep them but
  stop leading with the pending count.
