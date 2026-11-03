# Claude, Fhir.

Does connecting Claude to a hospital's FHIR server mean it reads and diagnoses the
patient? A skill is a folder Claude reads before it works — this one's `SKILL.md` is a
short, linear instruction set: read the steps, execute them in order, return the
result. What it actually does is narrow on purpose — connect to a FHIR R4 endpoint
(Epic, Oracle Health/Cerner, MEDITECH, athenahealth, or any SMART-on-FHIR system), pull
a patient's clinical data and notes, and extract structured findings. Not a diagnosis,
not clinical judgment. Pulling a record out of the system, and making sense of what it
means, are two different jobs, and this skill only does the first one.

**Topic:** FHIR · ANTHROPIC SKILL
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/healthcare--claude-liam-fhir

---

## Chapters

0:00 The naive framing: "it diagnoses the patient"
0:10 A skill is a folder Claude reads before it works
0:24 How the skill works — read, execute, return
0:36 The mechanism: just the data, structured
0:56 Carry-out
1:04 Your turn
1:24 Outro

---

## YOUR TURN

I want to connect to a hospital's FHIR R4 server — Epic, Oracle Health/Cerner,
MEDITECH, athenahealth, or any SMART-on-FHIR endpoint. Read the fhir skill and walk me
through what you'll do before you do it.

Run that on a real connection today, and watch the plan before the result.

---

## Deliberately not claimed

No claim that `fhir` interprets, diagnoses, or forms any clinical judgment about a
patient — its own spec stops at structured retrieval, and the reel states that limit
directly rather than treating it as a shortcoming. No internal file-path or maintainer
detail from the skill's source (which scripts other tools in the same plugin call, how
a bundled server keeps its own copy) — that's a note for whoever edits the skill, not a
fact a general viewer needs.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Remotion (motion graphics).
No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #AgentSkills #ClaudeCode #LLM #HumanitariansAI #ProfessorBear

---
