# Claude, Escalation Flagger.

When a Claude Skill named `escalation-flagger` flags something for a human
to look at, is that Claude's own judgment about what looks risky, or a match
against criteria written down somewhere a person could read? Every Claude
Skill is a folder with one file, `SKILL.md`, written in plain sentences, not
code — the file is the whole program. Claude reads it and checks each
criterion in order, top to bottom, flagging only where one actually matches.
Remove a criterion from that file and inputs that used to trigger it stop
getting flagged; nothing hidden fills the gap. Run the same input through it
twice and you get the same match and the same flag both times — but that
guarantee holds only for input inside what the file describes. Send through
a case the list never anticipated, and nothing gets flagged, not because
Claude judged it safe, but because nothing in the file matched.

**Topic:** SKILLS · ANTHROPIC AGENT SKILLS
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-for-legal--claude-liam-escalation-flagger

---

## Chapters

0:00 Claude's escalation flagger — is it flagging by judgment, or by match?
0:11 SKILL.md is the file — the anchor: a numbered checklist of criteria
0:30 Checked, not sensed — the wrong guess, falsified
0:47 The anchor returns — same match twice, then a case with nothing to match
1:06 Carry-out
1:17 Your turn
1:32 Outro

---

## YOUR TURN

"Write me a SKILL.md with three short numbered criteria for flagging
something I deal with often. Then hand it inputs on both sides — one that
matches, one that doesn't — and watch whether the flag follows the file, not
a feeling."

Watch whether the flag fires exactly where a criterion matches and stays
silent everywhere else — that's whether the match-not-judgment claim actually
holds for a Skill written by hand.

---

## Deliberately not claimed

Not what the `escalation-flagger` skill this reel is named after specifically
checks for, or who/what it escalates to — the original source video's own
narration never actually says (four of its seven beats carry an unfilled
template placeholder exactly where that content should be, a batch-build
defect, not a stylistic choice), and the real file lives on a machine this
build can't reach. This reel states only what's generically true of any
Claude Skill's matching mechanism, using `escalation-flagger` as the example's
name and its plain-language category of behavior — checks input, flags
matches for a human — never as a source of invented criteria. Not a verdict
on the design — the source called this "the Teardown moment" and framed it
as "what it gets right / what it bites"; this reel keeps the same underlying
mechanism (repeatable inside the spec, silent outside it) but states it as a
boundary, not a critique. Not a claim that Claude never reasons about
anything — only that this mechanism, a Skill's written criteria checked step
by step, is what decides the flag.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #AgenticAI #AIagents #HumanitariansAI #ProfessorBear #ClaudeBasics

---
