# CAMPAIGN-FEEDBACK — what-is-brutalist
# append-only log of human-feedback iterations after initial build

---

## 2026-07-12 — Box overflow + conductor-loop beat

### Feedback (verbatim)
> "Fix the boxes — make them wider to properly hold the text. Keep the bad (too-narrow) frame in
> this video, and add a new beat after B08 where my voice clone tells you to fix the boxes and you
> do it, on screen. Log my feedback."

### Root cause
B08_ScoreAndPlaying tool cards used `Rectangle(width=2.4, height=0.6)` — a fixed box that
overflowed when the VGroup(tool_name + role_name) exceeded 2.4 units wide. Same pattern in B03.

### Fix applied (general toolkit, not one-off)
- `runtime/manim/animated_graphics.py`: added `auto_box(content, h_pad, v_pad, …)` — measures
  content mob at render time and sizes the Rectangle to fit.
- `youtube/what-is-brutalist/scenes.py`: B08 and B03 updated to call `auto_box()`.

### Artifacts
- `media/box-before.png` + `media/box-before.mp4` — B08 frame at 3s (narrow box, visible overflow)

### New beat B08B (conductor loop, live)
- Position: immediately after B08
- narration: "Here's that loop — live, from building this very video…"
- Scene: BEFORE narrow box → INSTRUCTION chip → AFTER auto_box (Teardown palette)
- Audio: 17.5s (ElevenLabs NikBearBrown)
- Result: manim/B08B.mp4 ✓

### Recompile
- 17/17 beats filled · 191.9s narrated cut
- Deliverable: `what-is-brutalist-review.mp4`

### Toolkit fix promoted
`auto_box()` is now part of `runtime/manim/animated_graphics.py` — available to all future scenes
in this repo. Any card/label helper should call it instead of hardcoding a Rectangle size.

---

## 2026-07-12 — Review label explainer beat (B00B)

### Feedback (verbatim)
> "Keep the review labels in this video. Add an early beat that explains what the review label is
> and what it does. One beat, early — right after the intro."

### New beat B00B (act=INTRO)
- Position: after B00, before B01
- narration: "One quick thing before we start. You'll notice a small grey label in the corner of
  every shot. That's the review label…" (NikBearBrown voice, 23.07s actual)
- Scene: mock video frame + label chip → highlight ring → zoomed chip with 5 field callouts
  (beat id, engine, status, start time, duration) — all callout boxes use `auto_box()`
- Render: manim/B00B.mp4 ✓ (slowed 2.61× — see human-review note below)

### Human review note
B00B clip (8.8s) slowed 2.61× to fill 23.07s audio. Animations play at 38% speed — check
whether pacing feels natural or whether the narration should be trimmed.

### Recompile
- 18/18 beats filled · 215.0s narrated cut
- Deliverable: `what-is-brutalist-review.mp4`

---

## 2026-07-12 — Box overflow: real fix (B09 + B11)

### Feedback (verbatim)
> "The box fix was discussed but not actually applied — B09 (beat_sheet.json) and B11 (request
> card) still overflow. Make the text fit the boxes, or make the boxes wider. And verify the render
> — don't tell me it's fixed until you've looked at the frame."

### Root cause
B09 and B11 still had fixed-width Rectangles (3.6 and 3.8 units) from the original build.
auto_box() was only applied to B08 and B03 in the previous iteration.

### Fix
- `animated_graphics.py`: added `surround_box()` — SurroundingRectangle with teardown defaults.
  Canonical helper for any multi-line stack whose render width is unknown at code-write time.
- `scenes.py B09`: text_stack arranged first, heart_box = surround_box(text_stack)
- `scenes.py B11`: card_contents arranged first, card_box = surround_box(card_contents)

### Frame verification
- B09 @ 4s: both lines inside box ✓
- B11 @ 7s: all 4 lines including quoted line inside box ✓
- B08 @ 5s: all tool cards clean ✓
- B03 @ 5s: all question cards clean ✓

### Recompile
- 18/18 beats · 215.0s · no audio re-gen needed

---
