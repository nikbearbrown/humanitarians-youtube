# When Claude Audits a Spreadsheet, Does It Fix Anything?

Ask Claude to audit a spreadsheet and it's tempting to picture it finding
the errors and quietly fixing them while it's in there. That's not what's
happening. Anthropic's `audit-xls` skill checks the balance sheet first —
because if it doesn't balance, everything downstream is suspect — then
scans the scoped range, sheet, or model for formula accuracy, errors, and
common mistakes, and reports what it finds, cell by cell. Watch the
anchor: a balance sheet off by a fixed amount — checked first, found,
cited, reported — then it stops. Nothing is rewritten. A clean
balance-sheet pass isn't the same as an error-free model, and a flagged
mismatch isn't the same as a confirmed wrong number — either way, the
spreadsheet itself is unchanged until you act on the report.

**Topic:** AUDIT-XLS · ANTHROPIC SKILL
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/financial-services--claude-liam-audit-xls

---

## Chapters

0:00 Can Claude just fix my spreadsheet?
0:09 Fix it, or report it?
0:30 One mismatch, four stops
0:47 Reported, waiting
1:11 Carry-out
1:22 Your turn
1:39 Outro

---

## YOUR TURN

"Give Claude a spreadsheet with one formula you already know is wrong,
and ask it to run the audit-xls skill: check balance first, then scan
for formula errors, and report what it finds by cell. Then open the
sheet afterward and check whether the formula itself changed."

Checking the sheet after is the fastest way to see that the skill
reports and cites, instead of repairing — rather than just trusting
that it does.

---

## Deliberately not claimed

This reel redoes a published Teardown-register skill-showcase reel
(`claude-liam-audit-xls`) in the Plain register for a general audience.
The underlying facts are unchanged from the source: the skill audits a
spreadsheet for formula accuracy, errors, and common mistakes, checking
balance-sheet balance first — it does not rewrite formulas, decide what
counts as an error beyond its checks, or invent cell references, dollar
amounts, or UI. This script makes no claim about specific spreadsheet
software — only the general mechanism (check, then report by cell) and
its two failure directions.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #Spreadsheets #FinTech #AIagents #AgenticAI #HumanitariansAI #ProfessorBear #ClaudeBasics

---
