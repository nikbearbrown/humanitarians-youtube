# Feedback Before The Commit.

Ask whether Claude just commits a workshop attendee's solution and opens a PR, and
the natural read is that it's a git task, full stop. It isn't, quite. The
submit-solution skill runs five steps in a fixed order, and the first one has
nothing to do with git: three questions — which subagent approach they used,
what was the hardest part of the workshop, and one thing they'd change. Only
after that does Claude check the diff (an empty one usually means they edited
a different file, not that they're finished), pull the eval score, commit,
and open the PR. The PR body itself carries two sections in one document —
the code summary, and the workshop feedback right below it — because that PR
is also the form facilitators read to shape the next workshop. Skip the
questions and the commit still happens; the feedback half just stays blank.

**Topic:** SUBMIT-SOLUTION · ANTHROPIC SKILL
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/cwc-workshops--claude-liam-submit-solution

---

## Chapters

0:00 The naive framing: "it's a git task, right?"
0:10 Anatomy: five steps, fixed order
0:28 Mechanism: three questions, then git
0:54 The PR body has two sections: code summary and feedback
1:17 Carry-out
1:29 Your turn
1:48 Outro

---

## YOUR TURN

Paste this into Claude: I just finished a coding exercise and want to submit
my solution as a pull request. Before you touch git, ask me what approach I
used, what was hardest, and what I'd change — then show me the diff, and
write a PR description with two sections: my code summary, and my feedback.

Run that today, against your own finished exercise.

---

## Deliberately not claimed

Every claim in this reel restates the source SKILL.md's own text directly:
the fixed five-step order (ask, show diff, commit and push, open PR,
confirm); the exact three interview questions (subagent approach for cycle
three, hardest part, one thing to change); the empty-diff-means-check-a-
different-file case; the PR body template's two sections (decomposition
summary, workshop feedback); and the confirmation step naming that
facilitators read every PR and the feedback shapes the next workshop run.
This redo drops the source Teardown cut's "what it bites" design verdict —
a judgment on the skill's scope, not a mechanism description — and rewrites
the your-turn prompt to be self-contained (the source named "the
submit-solution skill" by file and quoted a task string truncated mid-word;
this version states the scenario directly so it's runnable in any Claude
conversation today, no skill install required). See BUILD-LOG.md for the
full account.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #AgentSkills #ClaudeCode #LLM #HumanitariansAI #ProfessorBear

---
