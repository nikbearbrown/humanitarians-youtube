# CARRY-OUT — financial-services--claude-liam-bond-futures-basis

**The line (written first, GATE C):**

> The cheapest bond to deliver is whichever one comes out lowest in a fixed
> comparison across the whole deliverable basket — not the bond Claude
> favors. It ranks delivery cost against the curve; it doesn't call whether
> the trade is worth putting on.

**Test:** if someone repeats only this in a meeting next week, is it still
true? Yes — it compresses the one distinction the reel is built to land (a
computed ranking across a fixed basket of bonds vs. a trader's feel for
which bond is best), not the topic (bond futures generally).

**The wrong guess it defeats:** that finding the cheapest-to-deliver bond
takes a trader's judgment — a feel for which bond will perform best, or
which one looks like the smart pick. It doesn't. The `bond-futures-basis`
skill prices every eligible bond against the futures contract using its
conversion factor, ranks them by actual computed delivery cost, and
separately compares the winning bond's implied repo rate against the
market's real financing rate to size the basis-trade opportunity. Ask it to
favor a bond because you like its prospects and it will not — it only
reports the one that is numerically cheapest to deliver.

**GATE C — signed:** derived directly from the source sheet's own stated
facts (see QUESTION.md) — the source beat_sheet.json's narration already
states the skill's scope; this line compresses it into the reel's
carry-out.
