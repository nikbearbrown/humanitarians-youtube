# How Does Claude Tell Whether a Bond Is Rich or Cheap?

Ask Claude to say whether a bond is rich or cheap and it's tempting to
picture it working from a trader's feel — some sense for the market.
That's not what's happening. Anthropic's `bond-relative-value` skill
computes a relative-value read from four fixed inputs: the bond's price,
the yield curve it sits on, the credit spread over that curve, and a
stress-tested rate shock. Watch the anchor: a ten-year corporate bond
trading forty basis points over the curve — priced, curve read, spread
decomposed, stress-tested — then it stops, with a single computed read,
waiting. A bond that comes back cheap by the read isn't the same as a
bond worth buying, and a bond that comes back rich isn't automatically
one to avoid. A computed rich-or-cheap read is a number built from
price, the curve, the spread, and a stress test — not Claude's own call
on what to buy.

**Topic:** BOND-RELATIVE-VALUE · ANTHROPIC SKILL
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/financial-services--claude-liam-bond-relative-value

---

## Chapters

0:00 Which bond is rich or cheap — by feel?
0:10 Trader's feel, or a written procedure?
0:32 One bond, four stops
0:53 A computed read, then a split
1:16 Carry-out
1:25 Your turn
1:42 Outro

---

## YOUR TURN

"Give Claude one bond, its price, and a yield curve to compare it
against, and ask it to run the bond-relative-value skill: decompose the
spread and stress-test it against a rate shock. Then swap in a
different curve for the same bond."

Watching the read move when the curve changes is the fastest way to see
that the skill computes from the inputs you give it, instead of a fixed
opinion about the bond — rather than just trusting that it does.

---

## Deliberately not claimed

This reel redoes a published Teardown-register skill-showcase reel
(`claude-liam-bond-relative-value`) in the Plain register for a general
audience. The underlying facts are unchanged from the source: the skill
performs relative value analysis on bonds by combining pricing, yield
curve context, credit spreads, and scenario stress testing — it does not
decide which bond to buy, invent a curve, or exercise trading judgment
beyond what the inputs already define. This script makes no claim about
any specific bond, issuer, or trading desk — only the general mechanism
(a written procedure that computes and reads) and its two failure
directions.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #FixedIncome #FinTech #AIagents #AgenticAI #HumanitariansAI #ProfessorBear #ClaudeBasics

---
