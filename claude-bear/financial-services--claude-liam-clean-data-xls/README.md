# What Does Claude Actually Do When You Say "Clean This Data"?

Ask Claude to clean up a messy spreadsheet and it's tempting to picture it
looking the sheet over, deciding what's wrong, and fixing it however it
thinks best. That's not what's happening. Anthropic's `clean-data-xls`
skill reads a written SKILL.md and runs exactly six fixed operations — trim
whitespace, fix inconsistent casing, convert numbers stored as text,
standardize dates, remove duplicates, flag mixed-type columns — nothing
more. Watch the anchor: one Revenue column holding " 1,200 ", "1300",
"N/A", and " 1,400.00 " — trimmed, converted, then flagged because "N/A"
can't become a number. A value that converts cleanly from text to a number
isn't verified as the *correct* number, and a column flagged as mixed-type
isn't automatically broken. Clean this data doesn't mean Claude judges
what looks messy — it runs one fixed checklist, in order, and a column
that comes back clean has been reformatted, not fact-checked.

**Topic:** CLEAN-DATA-XLS · ANTHROPIC SKILL
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/financial-services--claude-liam-clean-data-xls

---

## Chapters

0:00 What decides what gets cleaned — judgment?
0:10 Judgment, or a checklist?
0:39 One column, four stops
1:05 Flagged, waiting
1:34 Carry-out
1:46 Your turn
2:06 Outro

---

## YOUR TURN

"Give Claude a spreadsheet with a messy column — mixed date formats, extra
whitespace, a duplicate row or two — and ask it to run the clean-data-xls
skill. Then add one problem that's not on its checklist, like the same
currency symbol covering two different currencies, and run it again."

Watching what changes, and what doesn't, is the fastest way to see that
the skill runs a fixed list of operations, instead of general-purpose
judgment — rather than just trusting that it does.

---

## Deliberately not claimed

This reel redoes a published Teardown-register skill-showcase reel
(`claude-liam-clean-data-xls`) in the Plain register for a general
audience. The underlying facts are unchanged from the source: the skill
trims whitespace, fixes inconsistent casing, converts numbers stored as
text, standardizes dates, removes duplicates, and flags mixed-type
columns — it does not decide what "clean" should mean, invent a fix
outside that list, or exercise judgment beyond what's written in the
SKILL.md. This script makes no claim about any specific spreadsheet,
company, or UI — only the general mechanism (a fixed checklist) and its
two failure directions.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #FinTech #DataCleaning #AIagents #AgenticAI #HumanitariansAI #ProfessorBear #ClaudeBasics

---
