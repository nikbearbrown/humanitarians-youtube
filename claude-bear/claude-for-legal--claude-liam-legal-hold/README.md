# Claude, Legal Hold.

Claude picked up a skill called legal-hold — does it decide, on its own,
when documents need to be frozen for a lawsuit? No. A "skill" is a folder
holding one file, SKILL.md, that Claude reads before it starts and then
follows step by step. Before it issues or releases a hold, that file
stops Claude and asks whether an attorney has reviewed it — say no, and it
hands back a one-page brief instead of sending anything. The file routes by
flag (issue, refresh, release, status) and draws its own edges too: it
drafts, it logs, it calendars, but it never enforces preservation, never
sets scope alone, and never sends the notice — a person does every one of
those. Watching Claude draft a clean hold notice, or stall on a request,
proves nothing on its own about whether it understood the lawsuit.

**Topic:** CLAUDE · SKILLS
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-for-legal--claude-liam-legal-hold

---

## Chapters

0:00 The naive framing: "Claude decides who's on hold"
0:11 Sounds like Claude's call
0:19 Broken, with a case — the SKILL.md's own confirmation gate
0:29 The anchor: one file — legal-hold's single SKILL.md
0:44 Four modes, one file — issue, refresh, release, status
0:54 The payoff, and the limit
1:05 The anchor returns — same file, every run
1:19 Both directions — not proof, either way
1:35 Carry-out
1:42 Your turn
1:55 Outro

---

## YOUR TURN

Pick one document or process you do the same way every time. Write Claude a
SKILL.md for it — plain language, ordered steps — then have it read the
file back to you and walk you through exactly what it will do, before it
does it.

Run that today, against something you actually produce over and over.

---

## Deliberately not claimed

This reel is grounded directly in the real `legal-hold` SKILL.md (a
litigation-ops skill from a legal-clinic collection), read in full before
scripting — unlike a sibling redo in this series whose source file wasn't
reachable, this one was. Every specific claim here (the confirmation gate
before issuing or releasing a hold, the four flags, the "what this skill
does not do" edge list) is a direct read of that file, not an invented
procedure. See BUILD-LOG.md for the full account, including why this redo
expanded the source's compact 7-beat Teardown format to hai-simple's
mandatory wrong-guess/anchor/both-directions spine.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #AgentSkills #ClaudeCode #LLM #HumanitariansAI #ProfessorBear

---
