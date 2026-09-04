# CARRY-OUT — financial-services--claude-liam-fixed-income-portfolio

**The line (written first, GATE C):**

> A portfolio's duration and DV01 aren't Claude's judgment about how risky
> it is — they're computed sensitivities to a rate move you specify.
> Change the size of that move, and the numbers change with it.

**Test:** if someone repeats only this in a meeting next week, is it still
true? Yes — it compresses the one distinction the reel is built to land (a
computed rate-sensitivity number vs. an analyst's independent judgment
about risk), not the topic (fixed income portfolio review generally).

**The wrong guess it defeats:** that Claude decides how risky a bond
portfolio is — the way an analyst who has studied the holdings forms an
opinion. It doesn't. The `fixed-income-portfolio` skill reads a written
SKILL.md and executes a fixed procedure: price each bond from reference
data (coupon, maturity, current price), compute duration and DV01 (the
dollar change in price for a one-basis-point move in rates), sum DV01
across the portfolio, and run whatever rate-shock scenario it's told to.
Give it a different price for one bond and the numbers move without
protest — it never argues that your bond is too risky, because it never
had an opinion about the bond to begin with.

**GATE C — signed:** derived directly from the source sheet's own stated
facts (see QUESTION.md) — the source beat_sheet.json's narration already
states the skill's scope; this line compresses it into the reel's
carry-out.
