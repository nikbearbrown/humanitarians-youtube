# PDF

Does Claude reach for one all-purpose PDF library, or does the `pdf` skill route
to a different tool depending on the job? It routes: `pypdf` for manipulation
(merge, split, rotate, encrypt), `pdfplumber` for extraction (text, tables →
pandas), `reportlab` for creation (Canvas or Platypus) — plus CLI tools and two
specialist files (`FORMS.md`, `REFERENCE.md`) for forms and advanced use. There's
no do-everything PDF library; the skill's whole job is routing each task to the
tool built for it.

**Topic:** PDF · ANTHROPIC SKILL
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/skills--claude-liam-pdf

---

## Chapters

0:00 The naive framing: "one library for every job"
0:11 Anatomy — pypdf, pdfplumber, reportlab, CLI tools, specialist files
0:54 Quick reference — task → tool → code, plus the reportlab gotcha
1:40 The mechanism: route by task, never guess
2:00 Carry-out
2:08 Your turn
2:26 Outro

---

## YOUR TURN

I have a scanned invoice, saved as invoice.pdf. Extract all the text, pull out
any tables, and save the tables to an Excel file.

Watch what Claude does with the scan: a real extraction needs OCR first
(`pdf2image` → `pytesseract`), not a direct text read, and the tables need to
land as an actual spreadsheet, not a wall of numbers. Run it today and see
where the routing decision actually happens.

---

## Deliberately not claimed

No claim that the `pdf` skill covers PDF accessibility, tagging, or digital
signatures — its own spec stops short of those, and the reel states that gap
directly rather than treating it as a shortcoming. The reportlab Unicode-
subscript gotcha and the two-step OCR pipeline are stated as fact, not flagged
as inference — both come directly from the skill's own documentation.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Remotion (motion graphics).
No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #AgentSkills #ClaudeCode #LLM #HumanitariansAI #ProfessorBear #PDF

---
