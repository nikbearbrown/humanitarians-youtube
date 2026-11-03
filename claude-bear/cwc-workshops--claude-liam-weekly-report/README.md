# One Script, Not One Call Each.

Ask whether Claude checks a weekly inventory report one SKU at a time, and
the natural read is a tool call per row — the stock file alone runs about
sixty-seven thousand SKUs. That's not what the weekly-report skill does.
Its rule is explicit: write one script, run it once. The script loads every
backing file — stock levels, products, sales history, open purchase
orders — computes stockouts and days of cover for all of them together,
and prints the finished markdown in a single pass, zero per-SKU tool
calls. What that script actually prints still depends on what was asked:
the full weekly review adds an aging-PO check (any open order older than
its supplier's usual lead time gets flagged), while the shorter daily
sweep drops the open-orders and forecast-risk sections and leads with
whatever action was already taken.

**Topic:** WEEKLY-REPORT · ANTHROPIC SKILL
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/cwc-workshops--claude-liam-weekly-report

---

## Chapters

0:00 The naive framing: "does Claude call a tool per SKU?"
0:10 Anatomy: a skill is a folder (4 sections, 4 backing data files)
0:29 Mechanism: one script over 67k rows, not one call each — both directions (weekly adds aging; daily drops sections)
1:04 Carry-out
1:17 Your turn
1:38 Outro

---

## YOUR TURN

Paste this into Claude: I have a stock-levels file with about sixty
thousand rows and a separate purchase-orders file. Give me this week's
inventory report — stockouts, low stock, open orders, and which of those
orders are now aging past their lead time. Would you check this row by
row with tool calls, or write one script that computes it in a single
pass? Show me what that script would need to read, and what the top of
the report would say.

Run that today, against your own inventory scenario.

---

## Deliberately not claimed

Every claim in this reel restates the source SKILL.md's own text directly:
the four report sections (stockouts, low stock, open purchase orders,
forecast risk); the four backing files each section reads from; the
~67,000-row size of the stock file; the explicit "write one script, run it
once" instruction; the cadence table's contents (weekly adds the aging-PO
check, daily drops open-orders and forecast-risk); and the aging rule
itself (elapsed days since a PO was placed, compared against the
supplier's lead_time_days). This redo drops the source Teardown cut's
generic "Read SKILL.md → Execute → Return output" pipeline diagram — true
of any skill, not specific to this one — and its design-tell verdict
framing, replacing both with the one-script mechanism and the
both-directions cadence pair, stated without judgment. See BUILD-LOG.md
for the full account.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #AgentSkills #ClaudeCode #LLM #HumanitariansAI #ProfessorBear

---
