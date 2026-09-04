# Is Claude's Duration Number Its Own Judgment?

Ask Claude to review a bond portfolio and it's tempting to picture it forming
an opinion about how risky the holdings are — the way an analyst who's
studied the portfolio reaches a conclusion. That's not what's happening.
Anthropic's `fixed-income-portfolio` skill prices each bond from reference
data — coupon, maturity, current price — and computes duration and DV01:
the dollar change in price for a one basis point move in rates. Watch the
anchor: shock the portfolio by 100 basis points, and DV01 says exactly how
many dollars that move costs or gains — no opinion, just arithmetic. That
same shock is what a scenario analysis runs, again and again, at different
sizes. A portfolio that swings hard under one rate scenario isn't
necessarily poorly built — a large DV01 can be an intentional, hedged
position. And a portfolio that holds steady under that one scenario doesn't
mean it's safe from rate risk generally — a bigger move, or a shift that
isn't parallel across the curve, can still hurt it. A portfolio's duration
and DV01 are Claude running the rate move you specify through a fixed
computation, not its opinion of how risky the portfolio is.

**Topic:** FIXED-INCOME-PORTFOLIO · ANTHROPIC SKILL
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/financial-services--claude-liam-fixed-income-portfolio

---

## Chapters

0:00 What decides a portfolio's risk — the numbers?
0:12 Risk judgment, or the numbers?
0:33 One shock, one number
0:52 The same shock, sized again
1:14 Carry-out
1:26 Your turn
1:45 Outro

---

## YOUR TURN

"Give Claude a small bond portfolio — coupon, maturity, and current price
for two or three bonds — and ask it to run the fixed-income-portfolio
skill: compute duration and DV01, then stress test a 100 basis point rate
move. Then double the shock size and watch how the dollar impact scales."

That's the fastest way to see that DV01 is a fixed sensitivity number,
not a risk verdict — instead of just trusting that it is.

---

## Deliberately not claimed

This reel redoes a published Teardown-register skill-showcase reel
(`claude-liam-fixed-income-portfolio`) in the Plain register for a general
audience. The underlying facts are unchanged from the source: the skill
prices bonds from reference data, computes duration and DV01, analyzes
cashflows, and runs scenario analysis — it does not form an independent
opinion about how risky a portfolio is, decide which bonds belong in it, or
choose the scenario size itself. This script makes no claim about any
specific bond, dollar figure, or spreadsheet UI — only the general
mechanism (a rate shock that produces a computed dollar sensitivity) and
its two failure directions.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #FixedIncome #BondPortfolio #FinTech #AIagents #AgenticAI #HumanitariansAI #ProfessorBear #ClaudeBasics

---
