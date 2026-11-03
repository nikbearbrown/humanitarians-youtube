# It Reads Like Empathy. It's a Spec. — The Draft-Response Skill (Customer Replies)

A skill is a folder Claude reads before it works — this one is called
draft-response, and its SKILL.md holds the full instruction set in plain
language, no hidden logic. The pipeline lives in the Steps section: Claude
reads each step in order, then executes it, linearly, unless a step says
otherwise. This particular skill has exactly one job: draft a professional
customer-facing response, tailored to the situation and the relationship —
a product question, an escalation or outage, bad news like a delay or a
won't-fix, a declined feature request, or a billing issue. All of it lives
inside that one file's script, and nothing outside it is covered. It reads
like empathy — really it's a spec, and it runs the same way every time you
call it.

**Topic:** DRAFT-RESPONSE · ANTHROPIC SKILL
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/knowledge-work-plugins--claude-liam-draft-response

---

## Chapters

0:00 The naive framing: "does empathy write the reply?"
0:10 A skill is a folder
0:23 Read then execute
0:32 One file, one job
0:55 Carry-out
1:00 Your turn
1:14 Outro

---

## YOUR TURN

Paste this into Claude: Draft a reply to an escalation for my team. Walk me
through your plan before you act. That last clause matters — explaining
the plan first surfaces the real constraint logic, not just a draft.

Run that today, on your own team's actual escalation, not the video's
example.

---

## Deliberately not claimed

No claim about how Claude decides *which* skill to dispatch for a given
request — the source Skill documents its own trigger conditions (a product
question, an escalation or outage, a delay or won't-fix, a declined
feature request, a billing issue), not the general dispatch mechanism
across all skills. No claim that every Anthropic skill is built this same
way; the folder/SKILL.md/Steps-section shape described here is this
skill's actual structure, not a claim about the format in general. No
claim that the drafted reply itself is emotionally intelligent or
inauthentic — the reel's claim is narrower: the *process* that produces it
is a specification, not the model exercising judgment about tone in the
moment.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeCode #ClaudeSkills #ClaudePlugins #LLM #HumanitariansAI #ProfessorBear

---
