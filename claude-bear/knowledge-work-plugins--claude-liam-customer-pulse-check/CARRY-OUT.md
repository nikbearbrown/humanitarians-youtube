# CARRY-OUT.md — knowledge-work-plugins--claude-liam-customer-pulse-check

**Carry-out sentence (written first, per CARRY-OUT LAW):**

> Customer-pulse-check finds the repeating complaints and drafts a reply
> for each — it never decides which ones actually go out.

**Test:** if someone repeats only this in a meeting next week, is it still
true? Yes — it names the distinction (find-and-draft vs. send) without
naming the topic (PayPal/HubSpot/reviews), and it survives being repeated
cold.

**The wrong guess it's built to defeat:** that a skill built to handle
unhappy customers also sends the replies — that Claude resolves the
complaint end to end. `customer-pulse-check` is deliberately narrower: it
pulls from PayPal disputes, HubSpot tickets, and review exports, groups the
recurring themes, ranks the top three, and drafts a reply template for
each. Whether any drafted reply actually reaches a customer is not this
skill's job and isn't in its file. That narrowness is stated as a design
fact, not judged as a strength or weakness (Plain register, no verdict).

**Sentence it defeats, made explicit:** "the skill handles the unhappy
customers" → "the skill only finds the pattern and drafts the reply."
