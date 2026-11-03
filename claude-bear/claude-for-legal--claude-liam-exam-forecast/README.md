# Claude, Exam Forecast — What an Exam-Forecast Skill Actually Promises

Does a Claude skill called "exam forecast" mean it has somehow seen your
actual exam? It hasn't, and it can't — a professor's exam file is locked
until exam day. What it reads instead is what's already public: your
syllabus, your reading list, and past exams for the course. It counts how
often each topic has been tested before and hands back a ranked list, so
you know where to start studying first. Ranked first isn't a guarantee,
and ranked last isn't safe to skip — it re-orders your study time, it
never deletes a topic from it.

**Topic:** CLAUDE SKILLS · EXAM FORECAST
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-for-legal--claude-liam-exam-forecast

---

## Chapters

0:00 The naive framing: "it knows exactly what's on the exam"
0:12 The stakes — not enough time to reread everything
0:20 The anchor — a ranked list, planted
0:29 The wrong guess — has it seen the real exam?
0:37 Breaking it — one file is locked, one is public
0:46 How the skill works — SKILL.md, gather, count, rank
0:57 The one flag — no history, no forecast
1:07 The anchor returns — the ranked list, filled in
1:18 Ranked first isn't guaranteed
1:26 Ranked low isn't safe to skip
1:33 Carry-out
1:41 Your turn
1:57 Outro

---

## YOUR TURN

I have a final in three weeks. Here's my syllabus and reading list: read
them, and if I share past exams for the course, count which topics come
up most often. Then rank what's left by how often it's actually been
tested, and tell me where to start studying first.

Run that today, against your own next exam.

---

## Deliberately not claimed

No claim that Claude has seen any real exam — a professor's exam file is
locked until exam day, and the reel says so plainly. No claim of
certainty: a ranked list is a probability read from a public pattern
(syllabus, reading list, past exams), not a leak, and both failure
directions are stated (ranked first can still miss, ranked last can still
land). No invented Anthropic product name — "a skill is a folder Claude
reads before it works" and "SKILL.md lists the steps" describe Claude's
actual Agent Skills mechanism generically; "exam-forecast" is a custom
teaching skill in this family's law-student folder, not an official
Anthropic feature.

**Redo-mode note:** this reel rebuilds `claude-liam-exam-forecast`
(`anthropics/claude-for-legal/`) as `hai-simple`. The source sheet's
topic-specific narration was left as unresolved template placeholders and
its underlying `SKILL.md` no longer exists on this machine; the general
skill anatomy is kept from the source, and the exam-forecast-specific
facts were reconstructed generically from the skill's name and its
family's sibling law-student skills. Full detail in BUILD-LOG.md.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #AgentSkills #ClaudeForLegal #LLM #HumanitariansAI #ProfessorBear

---
