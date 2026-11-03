# CARRY-OUT — financial-services--claude-liam-bond-relative-value

**The line (written first, GATE C):**

> A computed rich-or-cheap read isn't Claude's call on what to buy — it's a
> number built from price, the curve, the spread, and a stress test,
> waiting for a trader's decision.

**Test:** if someone repeats only this in a meeting next week, is it still
true? Yes — it compresses the one distinction the reel is built to land
(a computed relative-value read vs. a trader's own feel or judgment about
what to buy or avoid), not the topic (bond relative value analysis
generally).

**The wrong guess it defeats:** that asking Claude to tell whether a bond
is rich or cheap means it's drawing on some trader's sense for the market
— a feel for which bond will perform best. It isn't. The
`bond-relative-value` skill reads a written SKILL.md and computes a
relative-value read from four fixed inputs — the bond's price, the yield
curve it sits on, the credit spread over that curve, and a stress-tested
rate shock — nothing more. Give it a bond with no yield curve to compare
against and it has nothing to spread it against, so it has nothing to
read; it will not invent a curve from general market sense.

**GATE C — signed:** derived directly from the source sheet's own stated
facts (see QUESTION.md) — the source beat_sheet.json's narration already
states the skill's scope; this line compresses it into the reel's
carry-out.
