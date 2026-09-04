# Claude, Branded.

Ask Claude to make your slides look like Anthropic made them, and the natural
guess is that it's making a design call — picking colors and fonts that just
feel right. It isn't. Brand two completely unrelated decks through the
brand-guidelines skill and you get the exact same seven hex codes and the
exact same two fonts, both times: a lookup, not a taste call. The skill is
one file, SKILL.md, and the pipeline is three steps — read the file, apply
it, write the file back out. Watch one plain slide — a title, three bullets,
a default font — go in, and come back with a bold Poppins headline, Lora
body text, and shapes that picked up a rotating terracotta/blue/green
accent, straight from the file's exact hex values. Feed it the same deck a
hundred times and you get the identical result a hundred times. Hand it a
deck meant for a bright projector, though, and it very likely keeps that
same cream background anyway — the spec has no way to sense the room it's
about to be shown in.

**Topic:** BRAND GUIDELINES · ANTHROPIC SKILL
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/skills--claude-liam-brand-guidelines

---

## Chapters

0:00 The naive framing: "can Claude just invent a brand look for my slides?"
0:10 SKILL.md, and nothing else
0:20 One plain slide, in
0:28 So it's picking a look? — the wrong guess
0:35 Same spec, two decks
0:44 Read, then write
0:54 The exact hex, not a guess
1:03 Three accents, rotating
1:13 24pt is the line
1:23 The anchor returns: the same slide, now on-spec
1:33 Run it again, get the same
1:42 It cannot see the room — one flag
1:53 Carry-out
1:59 Your turn
2:17 Outro

---

## YOUR TURN

I have a slide deck I want to look like it came from Anthropic. Use the
brand-guidelines skill. Start by telling me the exact colors and fonts
you're about to apply, and why, before you touch any code.

Run that today, on your own deck, not the video's example.

---

## Deliberately not claimed

No claim that the skill can judge context (projector brightness, print vs.
screen, dark mode) — the video states the opposite: it has no way to sense
the room. No invented model names or UI; the hex values and font names
shown (dark #141413, cream #faf9f5, mid gray #b0aea5, light gray #e8e6dc,
accent orange #d97757, blue #6a9bcc, green #788c5d, Poppins/Lora with
Arial/Georgia fallbacks) are the source skill's own spec, carried over
unchanged from the original Teardown-register build.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #AnthropicSkills #LLM #HumanitariansAI #ProfessorBear
