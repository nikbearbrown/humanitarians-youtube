# QUESTION

**Claude, is this a problem?**

A genuine newcomer question about a Claude skill named `is-this-a-problem`
(family: `claude-for-legal`). The natural assumption is that Claude answers
by judgment — reading the situation and using its own sense of how bad it
is. It doesn't. A skill is a written specification, and the skill decides
what counts as "a problem" here, not Claude's live opinion.

Name: General viewer (not attributed).
Channel: @HumanitariansAI — Claude Basics series.

## Redo-mode note

Source: `anthropics/claude-for-legal/youtube/claude-liam-is-this-a-problem/beat_sheet.json`
(Teardown register, 7 beats, `source_skill` pointing at a path on a
different machine — `/Users/bear/Documents/CoWork/bear-textbooks/...` —
that does not exist on this one). The source's own narration for the
skill-*specific* claims (B00, B03, BVDT, BHTF) was never filled in — it
carries a literal `>` placeholder where the skill's actual behavior should
be. Only the generic facts about how a Claude skill works (B01: a skill is
a folder with a `SKILL.md` instruction set; B02: Claude reads the Steps
section and executes linearly) were actually written.

This redo keeps those generic facts unchanged and reconstructs the
skill-specific placeholder content at the only level the skill's own name
and topic tag (`IS-THIS-A-PROBLEM · ANTHROPIC SKILL`) support without
inventing legal specifics: `is-this-a-problem` is a triage skill — its
`SKILL.md` defines, as explicit criteria, what counts as "a problem" in
its domain, so Claude's answer comes from matching a situation against
that written list, not from independently weighing it. No specific legal
criteria, thresholds, or scenarios are invented; the generic mechanism is
the same one already established, truthfully, in B01–B02 of the source.
