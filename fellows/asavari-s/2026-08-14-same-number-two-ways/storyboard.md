# Storyboard — Same Number, Two Ways

_Fellow: Asavari (Ash) Shejwal · Mycroft (SEC Agent) · 2026-08-14 · 16:9 + 9:16 · 4K (3840×2160)_

Official Brutalist beat-sheet format (renders via brutalist.art / kokoro voice `af_kore`).
Beat two is the executive summary ("why this matters"), per review.

## Beat 1 — GREETING

**On screen:** This is Humanitarians.

**Narration:** This is Humanitarians.

## Beat 2 — OPEN

**On screen:** Can you trust a number an AI hands you?

**Narration:** Can you trust a number an AI hands you? A number can look completely normal and still be wrong, and the usual checks won't catch it. Only one thing does.

## Beat 3 — Why This Matters

**On screen:** What is this video about, and why should I watch it?

**Narration:** Hi, I'm Asavari, a fellow at Humanitarians AI. This video is about how to trust a number an AI hands you. In a couple of minutes you'll learn a simple check that catches wrong numbers even when they look completely normal, using a real bug from a tool I built on SEC financial data. If you work with data or AI outputs and want to avoid confident mistakes, this is for you.

## Beat 4 — THE PROBLEM

**On screen:** FY2025 revenue = $211.9B

**Narration:** This is a real revenue figure my tool first produced for Microsoft. Correctly formatted, right range, passes every structural check. It's also wrong, by two years. Nothing flagged it, because nothing had anything to compare it against.

## Beat 5 — THE MECHANISM

**On screen:** Rules + cross-check

**Narration:** The tool trusts nothing by default and checks in two ways. Deterministic rules catch impossible values, a margin over a hundred percent, a balance sheet that doesn't balance. But a plausible wrong number sails through those. To catch it, you compare against a figure you did not derive from the same data. And every number keeps a link back to its filing.

## Beat 6 — WE TESTED IT

**On screen:** Self-consistent PASS vs independent CAUGHT IT

**Narration:** Here's the moment it mattered. Group the data by the filing's own year field and you get two hundred eleven point nine billion, and it looks fine. Cross-check it against Microsoft's actually reported revenue, two hundred eighty-one point seven billion, and the mismatch is obvious. The self-consistent version passed. Only the independent check caught it. And the correct figure carries its exact tag and filing link, so it's verifiable.

## Beat 7 — THE LIMIT

**On screen:** The honest limit

**Narration:** The honest limit. A number can be correctly tagged, well formed, and still wrong. No stack of rules fixes that, because the rules share the data's blind spot. The cross-check is the one test that doesn't, because it comes from outside the data.

## Beat 8 — The verdict

**On screen:** Run this on any number an AI hands you

**Narration:** So next time an AI hands you a number, run four checks. Can you trace it to its source? Is there a rule that catches the impossible? Can it say I don't know? And the one that matters most, did you check it against something you didn't derive from the same data? Fail that last one, and you're just trusting a number because it looks clean.

## Beat 9 — OUTRO

**On screen:** Same Number, Two Ways — outro card

**Narration:** Same Number, Two Ways. From Humanitarians AI.
