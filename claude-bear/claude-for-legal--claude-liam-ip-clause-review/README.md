# Claude, Ip Clause Review.

Someone asked whether Claude decides on its own whether an IP clause in a
contract is any good. It doesn't decide — it checks a list. The
`ip-clause-review` skill is a folder Claude reads before it acts: one file,
SKILL.md, holds the whole instruction set, written in plain language, no
hidden logic. Claude reads it, then works through its Steps in order — read
the file, apply each check, return the result. One check inside it is
specific: a clause that only grants a license doesn't move ownership at all;
only a clause that assigns the IP outright — all right, title, and interest,
transferred — actually hands it over. A clause can read like it hands over
ownership and still leave the work with whoever created it. Claude isn't
judging whether the clause is good — it's checking, one item at a time,
whether the clause actually assigns the IP instead of just licensing it.

**Topic:** IP-CLAUSE-REVIEW · ANTHROPIC SKILL
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-for-legal--claude-liam-ip-clause-review

---

## Chapters

0:00 The naive framing: "is Claude judging the clause?" — corrected on screen to "checking a list"
0:10 A Skill is a folder — one file, SKILL.md, holds the instructions
0:25 Read, check, return — a linear pipeline, no branching
0:36 The specific check: licenses it, or assigns it
0:53 Carry-out
1:01 Your turn
1:13 Outro

---

## YOUR TURN

Paste this into Claude:

> Here's an IP clause from a contract I'm reviewing: [paste the clause].
> Read the ip-clause-review skill, and before you tell me anything's wrong
> with it, walk me through exactly what you're checking for.

Run that today, against a clause you actually have in front of you.

---

## Deliberately not claimed

This reel does not describe the full contents of the `ip-clause-review`
skill's own SKILL.md — that file lives in a legal-clinic collection not
reachable from this build, and the source script this reel redoes never
filled in its skill-specific detail either (its own beat sheet still carries
unfilled `>` placeholders in three spots). Rather than invent a specific
checklist, this reel states one concrete, generically true fact about
contract drafting that is the actual reason an "IP clause review" is a task
worth having a skill for: the difference between a clause that licenses
rights and one that assigns them. See BUILD-LOG.md for the full account.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #AgentSkills #ClaudeCode #LLM #HumanitariansAI #ProfessorBear

---
