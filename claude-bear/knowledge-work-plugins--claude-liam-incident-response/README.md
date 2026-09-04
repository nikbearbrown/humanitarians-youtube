# Claude, Incident Response.

When production goes down, it's tempting to think Claude just knows what to
do — pure instinct. It isn't. When an "incident-response" skill is loaded,
Claude is reading a folder: one file, SKILL.md, written in plain language,
that it reads before it acts. Inside, a Steps section lists what to do, in
order — triage the alert, communicate a status update, then write a
blameless postmortem once it's resolved — and the file names exactly when
to start: phrases like "production is down," an alert that needs a
severity call, or a status update mid-incident. That's what buys you the
same three steps every time, first incident or fiftieth. But it also means
the file has nothing to say the moment what's actually happening isn't
triage, communicate, or postmortem — it only knows the page it was given.

**Topic:** INCIDENT-RESPONSE · ANTHROPIC SKILL
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/knowledge-work-plugins--claude-liam-incident-response

---

## Chapters

0:00 The naive framing: "Claude's incident response is pure instinct"
0:10 2 a.m., production down — the anchor
0:17 Instinct vs. the file — the wrong guess corrected
0:31 A skill is a folder — SKILL.md is the program
0:43 Steps, in order — linear execution
0:53 Triage. Communicate. Postmortem.
1:09 Same steps, every time
1:18 Outside the page — the limit (anchor payoff)
1:29 Carry-out
1:39 Your turn
1:50 Outro

---

## YOUR TURN

Paste this into Claude: I want to run an incident response workflow —
triage, communicate, and write a postmortem. Read the incident-response
skill and walk me through what you will do, before you do it.

Run that today, on your own incident-response skill or workflow, not the
video's example.

---

## Deliberately not claimed

No claim about what any specific team's incident-response SKILL.md
actually contains beyond triage/communicate/postmortem and its named
trigger phrases — those are the source skill's own stated job, not
invented detail. No severity taxonomy, tooling, or paging system asserted;
the mechanism (a written file, read before acting, executed step by step)
holds regardless of which team's playbook is loaded.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #IncidentResponse #ClaudeCode #LLM #HumanitariansAI #ProfessorBear

---
