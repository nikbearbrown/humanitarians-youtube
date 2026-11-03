# CHECKS-REPORT — two-threads-one-week (v2 revision)
Written before the first slate compile, per PROOF GATE (cli-explainer SKILL.md).

## Per-beat classification

11 SHOW / 0 justified-HOLD / 0 PUNT-flagged

| Beat | Class | Why |
|---|---|---|
| B00 | SHOW | ClaudeComposerAsk, ask shown answered (cold open) |
| B01 | SHOW | Manim presenter card, names its artifact (Agrima intro + week summary) — NEW this revision, replaces the PROBLEM beat per user request |
| B02 | SHOW | ClaudeComposerAsk, real generation prompt |
| B03 | SHOW | ClaudeCodeBeat, actual weekly_log_v1.py source |
| B04 | SHOW | Manim log columns from the REAL v1 run (2 threads, 8 items, real statuses) |
| B05 | SHOW | ClaudeComposerAsk, real revision prompt |
| B06 | SHOW | ClaudeCodeBeat, actual weekly_log_v2.py source |
| B07 | SHOW | Manim log columns from the REAL v2 run (same 8 items + per-thread standout) |
| B08 | SHOW | Manim recap card, WRITING/LOON PROJECT restated, named on screen |
| B09 | SHOW | ClaudeComposerAsk handoff, prompt read + discussed (HANDOFF LAW) |
| B10 | SHOW | ClaudeTitleOutro, title restated |

Every OUTPUT beat (B04, B07) is motion (Manim), never a still — required by
the CLI-explainer spine. Every claim-bearing beat names its on-screen
artifact in `shot.visual_intent` or the Remotion/Manim props.

## Teaching-arc checklist

- FRAMEWORK ✓ — B01 (presenter intro) states who's talking and what the
  video covers BEFORE any code appears; per user request this beat carries
  the "why" instead of a separate PROBLEM beat — the premise ("this is a
  real log, not a highlight reel") IS the framework.
- WORKED EXAMPLE ✓ — the full v1 build → run → revise → v2 build → run
  cycle, with real code and real captured output at every step.
- FALSIFIABILITY ✓ — B04 shows the v1 script's actual limitation on
  screen (reads like a data dump — not asserted, demonstrated by the real
  captured output's flat, un-ordered shape); B08 states plainly which
  three Loon Project items are still in progress rather than declaring the
  week finished.
- SCAFFOLDED TASK ✓ — B09 hands the viewer a concrete, narrower version of
  the same exercise (turn your own week into an ordered log with a
  standout per thread).
- BOOKENDS ✓ — B00 cold open (Claude composer, ask answered) / B10 title
  restate outro — both present, correct order.
- NO-SOURCE-NO-VERDICT ✓ — see FACTCHECK.md: every claim is either
  reproducible from the two checked-in scripts, a direct transcription of
  what the user reported about their own week, or a qualitative paraphrase
  of the user's own article summaries with no added numbers.

## Deviations from house defaults (disclosed, not hidden)

1. **Register/voice**: this reel uses `af_bella` (Bella) and a
   conversational-balanced narration register, NOT the house Teardown
   register / `am_onyx` (Liam-in-for-Bear) that is `cli-explainer`'s
   documented default — matching the precedent already established on the
   ai-support-shift reel for this same user/channel.
2. **Tier**: `cli-explainer` is marked ADVANCED / Bear-only in this
   toolkit's own TIERS.md. Built anyway since the user requested this
   specific skill by name with a full spec — flagged for transparency.
3. **Channel handle**: `@HumanitariansAI` is used throughout, matching the
   branding already established for this user's other reel in this book.
4. **B01 replaces PROBLEM, per explicit user request**: the cli-explainer
   spine calls for a PROBLEM beat stating the stakes before any code. This
   revision folds that into the presenter-intro beat instead of running
   both — the user explicitly asked for the video to open with "Hi, I'm
   Agrima, I worked on..." in place of the prior why-this-matters framing.
   Logged here as a disclosed, intentional deviation, not an oversight.
5. **No numeric tally, per explicit user request**: the prior build's
   audit()/"N of 8 shipped" framing is removed from narration and on-screen
   text throughout. All 8 real items remain visible in every log beat —
   nothing is hidden — but the video no longer leads with or totals the
   pending count. See FACTCHECK.md #8.
6. **Numeric restraint (unchanged from v1)**: the user's own article-2
   summary included a specific benchmark figure (a performance gap closing
   from ~17.5 points to under 1). That number is deliberately NOT put on
   screen or read in narration — this toolkit can't independently verify
   it. See FACTCHECK.md #7.

GATE F: FACTCHECK.md / SHOTLIST.md / PROMPTS.md all present. CHECKS-REPORT
written before first render of this revision. Proceeding to audio
generation + compile.
