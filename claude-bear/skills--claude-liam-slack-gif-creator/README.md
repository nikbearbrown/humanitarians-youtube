# Slack GIF Creator

Ask Claude for a bouncing star GIF for Slack, and the natural guess is
that it just makes the whole animation for you. It doesn't. The Slack GIF
Creator skill hands over the exact numbers Slack enforces — emoji GIFs at
128x128 pixels under 3 seconds, message GIFs at 480x480 — plus a toolkit:
GIFBuilder to assemble PIL frames and quantize colors, an easing module
with seven motion curves, and two validators to check compliance before
anything ships. What it doesn't do is draw the animation for you: there's
no `bounce()` function to call, the per-frame PIL drawing is code you
write yourself, driven by the easing curve you picked. Watch one concrete
ask — a bouncing star emoji GIF for a team channel — go from spec, to
drawn frames, to a validator's yes. And passing the validator only proves
compliance: size, timing, color count. It says nothing about whether a
complex shape renders cleanly, whether the color quantization dithers
visibly, or whether the loop is seamless — those are still yours to get
right by hand.

**Topic:** SLACK GIF CREATOR · ANTHROPIC SKILL
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/skills--claude-liam-slack-gif-creator

---

## Chapters

0:00 The naive framing: "does Claude just make it?"
0:10 Two formats, one enforced spec
0:25 The ask, planted: a bouncing star emoji GIF
0:34 Ready-made templates? — the wrong guess
0:41 No bounce() to call — the case that breaks it
0:52 GIFBuilder: frames in, GIF out
1:03 Easing: progress in, motion out
1:14 Validate before it ships
1:24 One flag: named gaps, not all gaps
1:38 The anchor returns: the star, built and checked
1:49 What a pass proves
1:56 What a pass doesn't prove
2:08 Carry-out
2:16 Your turn
2:39 Outro

---

## YOUR TURN

Make me a pulsing fire emoji GIF for Slack. Smooth loop, energetic, under
3 seconds. Use the Slack GIF Creator skill.

Then watch three things: does it look up the emoji spec (128x128, under 3
seconds, 48-128 colors) before writing any code? Does it use GIFBuilder
and the easing module rather than reinventing frame assembly? And does it
call `is_slack_ready` or `validate_gif` before calling the GIF done?

---

## Deliberately not claimed

The source skill file logged in the source sheet's metadata
(`../anthropics/skills/skills/slack-gif-creator/SKILL.md`) could no longer
be located at that path by the time of this build — the skills tree has
been reorganized since. Facts are carried over unchanged from the locked
source script (the two format tracks, the three utilities, the seven
easing curves, the eight animation concepts, the five documented
limitations) rather than re-verified against a live skill file, per this
series' redo contract.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #AnthropicSkills #LLM #HumanitariansAI #ProfessorBear
