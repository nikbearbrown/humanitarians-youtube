# SHOTLIST — ai-support-shift
# Typed work order per beat. Gate F open. Pass 1 (pre-audio-lock estimates).

## OPEN — INTRO (B00)

B00 · ClaudeComposerAsk (Remotion)
  action: render → media/B00.mp4
  props: greeting="Hi,", command="claude \"show me, with real code, what
         actually changes when a company swaps its phone-tree support bot
         for an AI chatbot\"", output=[3 lines, ask shown answered]
  show: composer types → running indicator → output lands
  status: RENDERABLE (no missing deps)

## ACT I — the old bot (B01–B04)

B01 · Manim B01_WhyShift (scenes.py)
  action: render → manim/B01.mp4
  show: title + 3-column card (Cost / 24-7 Availability / Instant Response)
  status: RENDERABLE

B02 · ClaudeComposerAsk (Remotion)
  action: render → media/B02.mp4
  props: greeting="The ask,", command=(write support_bot_v1.py prompt)
  status: RENDERABLE

B03 · ClaudeCodeBeat (Remotion)
  action: render → media/B03.mp4
  props: title="support_bot_v1.py", code=(trimmed real source), sparkLine
  status: RENDERABLE

B04 · Manim B04_OldBotFails (scenes.py)
  action: render → manim/B04.mp4
  show: 3-exchange chat transcript from the REAL run of support_bot_v1.py;
        3rd exchange tagged "MISSED — no keyword matched"
  status: RENDERABLE

## ACT II — the revision (B05–B07)

B05 · ClaudeComposerAsk (Remotion)
  action: render → media/B05.mp4
  props: greeting="The change,", command=(revise-to-intent+urgency prompt)
  status: RENDERABLE

B06 · ClaudeCodeBeat (Remotion)
  action: render → media/B06.mp4
  props: title="support_bot_v2.py", code=(trimmed real source), sparkLine
  status: RENDERABLE

B07 · Manim B07_NewBotUnderstands (scenes.py)
  action: render → manim/B07.mp4
  show: SAME 3-exchange transcript from the REAL run of support_bot_v2.py;
        3rd exchange tagged "UNDERSTOOD + escalated to a human"
  status: RENDERABLE

## CLOSE — SUMMARY / HANDOFF / OUTRO (B08–B10)

B08 · Manim B08_Summary (scenes.py)
  action: render → manim/B08.mp4
  show: OLD vs NEW recap cards + "still true either way" tradeoffs line
  status: RENDERABLE

B09 · ClaudeComposerAsk (Remotion) — HANDOFF LAW
  action: render → media/B09.mp4
  props: greeting="Your turn.", command=(viewer prompt, read + discussed)
  status: RENDERABLE

B10 · ClaudeTitleOutro (Remotion)
  action: render → media/B10.mp4
  props: title="From Phone Trees to Chatbots: What Actually Changed.",
         handle="@YourChannel" (placeholder — swap for the real channel),
         subline="built with Claude, taken apart"
  status: RENDERABLE

## Notes

- No pantry / archival stills used in this reel — every visual is either a
  Claude-skin Remotion composer/code/outro beat or a from-scratch Manim
  scene built for this reel (scenes.py). No open pantry slots.
- All 4 Manim scenes render at 4K by default via `./art run` (HEIGHT=2160).
- `@YourChannel` in B00/B10 is a placeholder brand handle — this reel isn't
  tied to an existing toolkit channel; swap it for the user's real handle
  before publishing anywhere.
