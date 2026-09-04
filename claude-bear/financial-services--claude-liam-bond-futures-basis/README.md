# How Does Claude Find the Cheapest Bond to Deliver?

Ask Claude to find the cheapest bond to deliver into a futures contract and
it's tempting to picture it working from a trader's feel — some sense for
which bond will perform best. That's not what's happening. Anthropic's
`bond-futures-basis` skill prices every eligible bond against the futures
contract using its conversion factor, and ranks them by actual computed
delivery cost. Watch the anchor: the futures price and a bond's conversion
factor combine into its delivery cost, and that cost becomes the bond's
implied repo rate — the return you'd earn buying it, holding it, and
delivering it into the contract. Finding the cheapest bond to deliver isn't
the same as finding a profitable trade, and a bond that ranks expensive
today isn't excluded forever — yields move, so the ranking gets rerun. The
cheapest bond to deliver is whichever one comes out lowest in the
comparison — not the bond Claude favors.

**Topic:** BOND-FUTURES-BASIS · ANTHROPIC SKILL
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/financial-services--claude-liam-bond-futures-basis

---

## Chapters

0:00 The cheapest bond to deliver — by feel?
0:10 Feel, or a priced ranking?
0:31 One bond, one number
0:48 Cheapest, not necessarily profitable
1:12 Carry-out
1:25 Your turn
1:44 Outro

---

## YOUR TURN

"Give Claude a small basket of deliverable bonds — a price and conversion
factor for each — along with the futures price and the market's repo rate,
and ask it to run the bond-futures-basis skill to find the cheapest one to
deliver. Then change one bond's price and watch whether the ranking flips."

Watching whether the ranking flips when a single bond's price changes is
the fastest way to see that the skill is comparing numbers, not forming an
opinion about which bond is "best."

---

## Deliberately not claimed

This reel redoes a published Teardown-register skill-showcase reel
(`claude-liam-bond-futures-basis`) in the Plain register for a general
audience. The underlying facts are unchanged from the source: the skill
prices bond futures, identifies the cheapest-to-deliver bond, and compares
against yield curves to assess delivery-option value and basis-trading
opportunities — it does not exercise trading judgment about which bond is
"best," predict market direction, or decide whether a trade is worth
putting on. This script makes no claim about specific bonds, prices, or UI
— only the general mechanism (a computed comparison across a fixed
deliverable basket) and its two failure directions.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #BondFutures #FixedIncome #FinTech #AIagents #AgenticAI #HumanitariansAI #ProfessorBear #ClaudeBasics

---
