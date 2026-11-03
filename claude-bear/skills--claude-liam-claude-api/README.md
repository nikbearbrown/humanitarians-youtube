# Claude API

Ask Claude to write code that calls the Claude API, and the natural guess is
that it already knows the shape of that API — Anthropic built both. It
doesn't just know; it checks. The claude-api skill is a reference Claude
reads before it touches your file, triggered whenever a prompt names Claude
or Anthropic, or describes an LLM task with no provider named. Here's the
case that breaks the "it should just know" guess: extended thinking used to
take a parameter called budget_tokens — on today's models that same
parameter is rejected outright with an error, not a warning, so memory
alone would have shipped broken code. The skill also maps a task onto one
of three API surfaces (a single call, API plus tool use, or a managed
agent) and insists on one exact model ID string, never a guess and never a
date tacked onto the end. Watch one concrete ask — add extended thinking to
a Python app calling the Claude API — go in, get caught mid-mistake, and
come back out correct. And both directions matter: it catches every change
it was told about, but nothing forces the check, so a change nobody wrote
down yet can still slip straight through.

**Topic:** CLAUDE API · ANTHROPIC SKILL
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/skills--claude-liam-claude-api

---

## Chapters

0:00 The naive framing: "doesn't Claude already know its own API?"
0:11 A reference, read before the file opens
0:24 The ask, planted: extended thinking in a Python app
0:34 Does it already know? — the wrong guess
0:42 One old parameter, one error — the case that breaks it
0:55 The trigger, not a lookup
1:08 Three surfaces, not one
1:21 Four questions decide
1:32 The exact id is the contract
1:41 The anchor returns: the same ask, now correct
1:53 What it catches
2:02 What it misses — one flag
2:12 Carry-out
2:21 Your turn
2:39 Outro

---

## YOUR TURN

I want to call the Claude API from Python using extended thinking. Check
the claude-api skill for the current parameter shape, the exact model ID,
and any drift from your training. Show me a working example.

Then watch what Claude does before it writes a single line — does it check
first, or does it guess? Run it today, on your own task, not the video's
example.

---

## Deliberately not claimed

No specific model ID is asserted as "the current default" anywhere in this
video — a deliberate choice, since the video's own subject is training
priors going stale, and naming one here would risk demonstrating the exact
failure it teaches about. The mechanism carried over from the source skill
(pre-scan trigger timing, the three-surface decision framework, the
budget_tokens parameter shape change, the "exact ID, no date suffix" rule)
is stated as fact; no claim is made about which specific model or parameter
shape is current today.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #AnthropicSkills #LLM #HumanitariansAI #ProfessorBear
