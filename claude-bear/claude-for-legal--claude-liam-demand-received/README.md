# Claude, Demand Received. — The Demand-Received Skill

When a demand letter comes in, Claude doesn't just reply to it — it triages
first. A Skill is a folder with one instruction file, SKILL.md, written in
plain language: no hidden logic, no freeform judgment. Claude reads it, then
executes each step in order — read the file, execute the steps, return the
result — linear, no branching unless a step says otherwise. One instruction
inside this particular Skill is specific: it extracts the letter's key
fields, cross-checks them against the portfolio, and assesses merit — then
it presents response options with a recommendation. Claude isn't deciding
whether to escalate on its own — when the assessment says escalate, it
hands off to matter-intake or demand-intake instead of handling it itself.

**Topic:** DEMAND-RECEIVED · ANTHROPIC SKILL
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-for-legal--claude-liam-demand-received

---

## Chapters

0:00 The naive framing: "does Claude just reply, or triage first?"
0:10 A Skill is a folder
0:23 Read, execute, return
0:34 The triage pipeline
0:51 Carry-out
1:00 Your turn
1:15 Outro

---

## YOUR TURN

Paste this into Claude: I have an inbound demand letter. Read the
demand-received skill, and before you triage it, walk me through what you
will do — the fields you'll extract, the portfolio cross-check, and the
conditions under which you'd escalate instead of recommending a response
yourself.

Run that today, on your own situation, not the video's example.

---

## Deliberately not claimed

No claim about what any specific demand letter says or how it should be
answered in a real case — the mechanism (a named folder, one instruction
file, a linear pipeline, and a specific triage sequence ending in an
escalation hand-off) holds regardless of the facts involved. No claim that
Claude replaces a lawyer's review or judgment; the video states the
opposite throughout — Claude triages and recommends, and escalation is a
hand-off decision, not a resolution Claude makes on its own.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #ClaudeForLegal #ClaudeCode #LLM #HumanitariansAI #ProfessorBear

---
