# When Two Agents Disagree
**Runtime target:** ~9 minutes | **Tone:** Courtroom procedural, measured tension | **Audience:** High-school technicality

---

[VISUAL: Title card. Two identical desks face each other across a table, each with a small nameplate: "AGENT A" and "AGENT B." A single sheet of paper sits between them with two different numbers circled in red.]

**NARRATION:**

Two agents look at the exact same evidence — same filing, same numbers, same question — and come back with opposite answers. Agent A is confident the company's margins are improving. Agent B is just as confident they're not. Both wrote clean, well-reasoned explanations. Both cited real sources. Neither one is lying — they just can't both be right.

Make a single agent smarter and this problem never shows up. It only exists once you have two. So today: what actually happens the second two agents disagree, and why the instinctive fix — average their answers and move on — is about the worst thing you could do.

[VISUAL: Two speech bubbles, one green one red, both pointing at the same document, contradicting each other]

## Why This Wasn't a Problem Before

Everything covered in the last two videos assumed a single agent doing a single piece of reasoning that you then go check. Claim extraction, source verification, asking the same question twice — all of it interrogates one voice.

[VISUAL: A single microphone icon on a stand, then it splits and multiplies into four microphones arranged around a table]

But build a system with several specialized agents — one on financial analysis, one on competitive research, one reading patents, one checking earnings calls — and you've created something new: two independent lines of reasoning that can flatly contradict each other. Here's the thing, though — that disagreement isn't a bug. It's a signal. It's the system telling you something a single confident agent never could: maybe the honest answer is "we don't actually know."

## The Naive Fix, and Why It's the Wrong One

The obvious move is to blend the outputs — average the two confidence scores, split the difference on the conclusion, ship something moderate and hedged, and move on.

[VISUAL: The two contradicting speech bubbles — green and red — get fed into a blender icon, and out comes a single grey, wishy-washy speech bubble that says "results may vary"]

That instinct is exactly wrong. Averaging two agents who disagree doesn't get you closer to the truth — it gets you an answer that *looks* moderate but is really nobody's actual opinion. If Agent A is right and Agent B is wrong, blending them just makes the true answer worse. And it throws away the one piece of information in the whole exchange that was actually valuable: the fact that they disagreed at all. A controller that quietly smooths conflicting outputs into a neutral-sounding grade has taken the most informative moment in the pipeline and erased it.

## Detecting the Disagreement

Before you can do anything sensible about a disagreement, you have to actually catch one — and that's harder than it sounds.

[VISUAL: A dial gauge appears, needle sitting in a green "AGREEMENT" zone. As the narration continues, the needle creeps toward a red "DIVERGENCE" zone]

You can't just diff the text of two conclusions. Two agents can use totally different words to say the same thing, or nearly identical words to say opposite things. What gets compared instead is structured: the confidence score each agent assigned its own conclusion, plus something like a directional vector — is this conclusion bullish or bearish, improving or worsening, safe or risky. When the gap between those two vectors crosses a threshold, that's what triggers the alarm. Below it, phrasing differences get ignored — two agents restating the same conclusion in different words shouldn't set anything off. Above it, something real is happening, and it gets escalated.

## The Arbitration Step

Once a real divergence gets flagged, the system doesn't just pick a winner — it runs one bounded round of debate.

[VISUAL: The two agents' nameplates slide toward each other. A third node appears above them, labeled "ARBITRATION," with a single arrow going down to each agent and a single arrow coming back up from each]

Each agent sees the other's conclusion and reasoning, and gets exactly one chance to respond: defend, revise, or concede. Just one round, on purpose. Let two language models argue without a limit and you don't get closer to the truth — you get whichever agent happens to sound more persuasive, which has nothing to do with which one is actually right. A single exchange is enough to catch a plain error — "oh, you're right, I misread that line item" — without turning the arbitration itself into another source of confident-sounding nonsense.

[VISUAL: Two outcomes branch on screen — one path labeled "RESOLVED," showing the two nameplates merging into one conclusion. The other labeled "UNRESOLVED," showing the two nameplates staying apart, both still lit up]

That round ends one of two ways. Resolved: one agent updates, or they land on shared ground, and the system moves forward with a single conclusion, now backed by two independent lines of reasoning instead of one. Or unresolved: they still disagree, and instead of getting smoothed over or averaged away, that disagreement gets written down as its own output — recorded plainly, here is where two independent processes looked at the same evidence and landed in different places, and here's each one's case.

## What You Do With "Unresolved"

Here's the part that actually matters downstream: an unresolved disagreement needs to reach the human, or whoever makes the final call, still looking unresolved — front and center, not buried in a footnote.

[VISUAL: A final report document appears. Most of it is a single clean paragraph. But one section is boxed in a distinct color, labeled "AGENTS DISAGREED — SEE BOTH POSITIONS," clearly different from the rest of the layout]

If a downstream system takes that unresolved disagreement and quietly folds it into one clean final grade anyway, it's undone the entire reason you ran two agents in the first place — no matter how good the intentions were. "These two independent processes looked at the same evidence and reached different conclusions, and one round of debate didn't settle it" is a genuinely more useful thing to hand a decision-maker than a falsely confident single number. It tells them exactly where to look before they trust the result.

## The Part Nobody's Fully Solved

And here's the honest complication. This whole mechanism has a real blind spot: if both agents are drawing on the same underlying source, and that source is wrong or has been tampered with, they'll agree with each other — confidently, consistently — while both being wrong. Arbitration only fires on disagreement. Shared contamination produces agreement instead. The one mechanism built to catch trouble can't see the failure mode where both witnesses were handed the same bad evidence to begin with.

[VISUAL: Both agent nameplates now glow the same color, both pointing at a single shared document with a small crack running through it, unnoticed by either]

You can't patch that with a cleverer threshold. It's a real limit of arbitration-by-disagreement — it raises the cost of one agent going rogue, but two agents drawing from the same poisoned well will simply agree their way past it. Good to know going in: arbitration lowers your risk. It doesn't take it to zero.

[VISUAL: End card. The two nameplates return to their original positions across the table, this time with a small ledger between them reading "AFFIDAVIT OF DISAGREEMENT — UNRESOLVED," untouched, unaveraged.]

Disagreement between two reasoning systems isn't noise you clean up before the final answer ships — handled honestly, it's some of the most valuable information the system produces. Two agents disagreeing was never the failure. A system that can't tell you they did — that's the failure.

**[END]**

---

## Key Takeaways

1. **Multi-agent disagreement is a new category of signal, not a bug to average away.** Single-agent verification (extraction, source checks, consistency probing) can't produce this signal at all — it only exists once two independently-reasoned conclusions can be compared against each other.
2. **Averaging conflicting outputs is worse than picking one.** A blended answer looks moderate but represents nobody's actual reasoning, and it destroys the one useful fact in the whole exchange: that the two agents didn't agree.
3. **Detect divergence on structure, not prose.** Comparing raw text is unreliable — different wording can mean the same thing, similar wording can mean opposite things. Comparing structured signals (confidence scores, directional/sentiment vectors) against a calibrated threshold is what actually triggers arbitration correctly.
4. **Bound the debate.** A single round of cross-examination is enough to catch simple misreadings; an open-ended argument between models optimizes for persuasive tone, not correctness, and becomes a new source of unreliable output.
5. **"Unresolved" must survive to the final output, visibly.** A system that quietly folds an unresolved disagreement into one smooth final grade has defeated the entire purpose of running independent agents — the disagreement has to be delivered as its own labeled finding.
6. **Arbitration has a structural blind spot: shared contamination.** If both agents draw on the same bad or poisoned source, they'll confidently agree with each other while both being wrong — and a mechanism built to catch disagreement is, by definition, blind to agreement. This lowers risk; it does not eliminate it.
