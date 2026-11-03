# CHECKS-REPORT — ai-support-shift
Written before the first slate compile, per PROOF GATE (cli-explainer SKILL.md).

## Per-beat classification

11 SHOW / 0 justified-HOLD / 0 PUNT-flagged

| Beat | Class | Why |
|---|---|---|
| B00 | SHOW | ClaudeComposerAsk, ask shown answered (cold open) |
| B01 | SHOW | Manim 3-column card, names its artifact (Cost / 24-7 / Instant) |
| B02 | SHOW | ClaudeComposerAsk, real generation prompt |
| B03 | SHOW | ClaudeCodeBeat, actual support_bot_v1.py source |
| B04 | SHOW | Manim chat-transcript of the REAL v1 run (3 exchanges) |
| B05 | SHOW | ClaudeComposerAsk, real revision prompt |
| B06 | SHOW | ClaudeCodeBeat, actual support_bot_v2.py source |
| B07 | SHOW | Manim chat-transcript of the REAL v2 run (same 3 exchanges) |
| B08 | SHOW | Manim recap card, old-vs-new + tradeoffs, named on screen |
| B09 | SHOW | ClaudeComposerAsk handoff, prompt read + discussed (HANDOFF LAW) |
| B10 | SHOW | ClaudeTitleOutro, title restated |

Every OUTPUT beat (B04, B07) is motion (Manim), never a still — required by
the CLI-explainer spine. Every claim-bearing beat names its on-screen
artifact in `shot.visual_intent` or the Remotion/Manim props.

## Teaching-arc checklist

- FRAMEWORK ✓ — B01 states the "why" (cost, availability, speed) BEFORE any
  code appears.
- WORKED EXAMPLE ✓ — the full v1 build → test → revise → v2 build → test
  cycle, with real code and real captured output at every step.
- FALSIFIABILITY ✓ — B04 shows the old bot's actual failure case on
  screen (not asserted, demonstrated); B08 states plainly where even the
  improved bot still falls short, rather than declaring victory.
- SCAFFOLDED TASK ✓ — B09 hands the viewer a concrete, narrower version of
  the same exercise (classify one easy + one messy real message).
- BOOKENDS ✓ — B00 cold open (Claude composer, ask answered) / B10 title
  restate outro — both present, correct order.
- NO-SOURCE-NO-VERDICT ✓ — see FACTCHECK.md: every claim is either
  reproducible from the two checked-in scripts or stated as plain framing
  reasoning, never as an uncited statistic.

## Deviations from house defaults (disclosed, not hidden)

1. **Register/voice**: this reel uses `af_bella` (Bella) and a
   conversational-balanced narration register, NOT the house Teardown
   register / `am_onyx` (Liam-in-for-Bear) that is `cli-explainer`'s
   documented default — per the user's explicit request for "a
   conversational, curious tone rather than formal narration" and a
   non-default voice. The IN-FOR-BEAR LAW line and `@NikBearBrown`
   OUTRO-LOCK do not apply to this reel for the same reason.
2. **Tier**: `cli-explainer` is marked ADVANCED / Bear-only in this
   toolkit's own TIERS.md. Built anyway since the user requested this
   specific skill by name with a full spec — flagged for transparency,
   not blocking.
3. **Channel handle**: `@YourChannel` is a placeholder (this reel isn't
   tied to an existing catalog channel). One-line swap before publishing.

GATE F: FACTCHECK.md / SHOTLIST.md / PROMPTS.md all present. CHECKS-REPORT
written before first render. Proceeding to audio generation + compile.
