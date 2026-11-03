# Claude, Icd10 Cm Skill.

Does Claude's `icd10-cm-skill` skill diagnose the patient, or just turn an
already-documented diagnosis into a billing code? A skill is a folder Claude
reads before it works — this one's `SKILL.md` is a short, linear instruction
set: read the steps, execute them in order, return the result. What it
actually does is narrow on purpose — extract billable ICD-10-CM diagnosis
codes from a clinical note, the way a professional coder builds the claim.
Coding a diagnosis, and making the diagnosis, are two different jobs, and
this skill only does the first one.

**Topic:** ICD10-CM-SKILL · ANTHROPIC SKILL
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/healthcare--claude-liam-icd10-cm-skill

---

## Chapters

0:00 The naive framing: "does it diagnose the patient?"
0:11 A skill is a folder Claude reads before it works
0:23 How the skill works — read, execute, return
0:33 The mechanism: just what's documented, coded
0:49 Carry-out
0:56 Your turn
1:13 Outro

---

## YOUR TURN

Here's a note: chest pain, shortness of breath, history of hypertension, leg
swelling on exam. List every diagnosis that's explicitly written down. Then,
separately, tell me what you'd be tempted to infer — like heart failure —
that you won't code, because it isn't documented.

Run that today, and watch where the line actually falls.

---

## Deliberately not claimed

No claim that `icd10-cm-skill` diagnoses, judges, or interprets a patient's
condition — its own spec stops at translating an already-documented diagnosis
into the matching billing code, and the reel states that limit directly
rather than treating it as a shortcoming. The Your Turn prompt uses a
hypothetical, non-patient note, not real clinical data.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Remotion (motion graphics).
No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #AgentSkills #ClaudeCode #LLM #HumanitariansAI #ProfessorBear #HealthcareAI

---
