# Claude, Doc Extract.

Does Claude's `doc-extract` skill read a document for you, or just get the
text out of it? A skill is a folder Claude reads before it works — this one's
`SKILL.md` is a short, linear instruction set: read the steps, execute them
in order, return the result. What it actually does is narrow on purpose —
turn a document (PDF, DOCX, XLSX, PPTX, RTF, or plain text/markdown/HTML)
into plain text. Not a summary, not an analysis. Turning a document into
text, and understanding that text, are two different jobs, and this skill
only does the first one.

**Topic:** DOC-EXTRACT · ANTHROPIC SKILL
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/healthcare--claude-liam-doc-extract

---

## Chapters

0:00 The naive framing: "it summarizes the PDF"
0:09 A skill is a folder Claude reads before it works
0:20 How the skill works — read, execute, return
0:31 The mechanism: just the words, extracted
0:46 Carry-out
0:53 Your turn
1:11 Outro

---

## YOUR TURN

I want to extract plain text from a document — PDF, DOCX, XLSX, PPTX, RTF,
or plain text, markdown, or HTML. Read the doc-extract skill and walk me
through what you'll do before you do it.

Run that on a real file today, and watch the plan before the result.

---

## Deliberately not claimed

No claim that `doc-extract` interprets, summarizes, or analyzes a document —
its own spec stops at plain text, and the reel states that limit directly
rather than treating it as a shortcoming. No internal file-path or
maintainer detail from the skill's source (which other tools call the same
extractor, how a bundled server keeps its own copy) — that's a note for
whoever edits the skill, not a fact a general viewer needs.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Remotion (motion graphics).
No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #AgentSkills #ClaudeCode #LLM #HumanitariansAI #ProfessorBear

---
