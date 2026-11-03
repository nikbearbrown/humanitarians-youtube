# PEDAGOGY — How AI Agents Are Changing Payments (hai cli-explainer, STEM/AI concept video)

A concept video on AI agents in payments, built around one distinction: an agent with read access can give a wrong answer, while an agent with write access can make a wrong payment. It starts with the customer-service agent most people have met (Klarna's 2024 assistant, and its 2025 move back toward human agents), walks through the first live agentic payments in Europe in June 2026 (ING in the Netherlands, then Nordea in Finland, both with Mastercard Agent Pay), and ends on the open question: accountability. Google's Agent Payments Protocol (AP2) records what the user asked for and approved, but proof of authorization isn't the same as deciding who pays when something goes wrong.

## Act structure

- B00A presenter intro ✓
- B00 cold open — June 2026: an agent in Finland made a real purchase and payment from a person's instructions ✓
- B01 — Klarna's assistant: launch numbers (Klarna's own), then the 2025 return to human agents ✓
- B02 — read access vs write access: the risk changes from a bad reply to a bad transaction ✓
- B03 — the first live agentic payments: ING (customer approved) and Nordea (end to end); agentic tokens; pilots only ✓
- B04 — accountability: AP2 intent and cart mandates, the audit trail, and the liability question left open ✓
- B05 — HANDOFF, a concrete exercise: write the limits for one payment you'd delegate ✓
- B06 — OUTRO ✓

## Evidence discipline

| Claim | Source | Verdict |
|---|---|---|
| In June 2026, an AI agent in Finland bought a coffee tasting package and paid with a Nordea Mastercard, from a person's instructions | Nordea, "First ever Finnish AI Agent payment: Mastercard and Nordea completes live agentic transaction" (June 2026) | OK — directly stated; Nordea's page gives 5 June, CX Network gives 6 June, so the narration says "June" |
| Klarna's AI assistant, built on OpenAI technology, had 2.3 million conversations in its first month: two-thirds of customer service chats | Klarna press release, "Klarna AI assistant handles two-thirds of customer service chats in its first month" (27 Feb 2024) | OK — quoted; these are Klarna's own figures, and the narration says so |
| "The equivalent work of 700 full-time agents" | Same Klarna release | OK — exact phrase; a workload comparison, not a headcount figure (TechRadar notes it's unrelated to Klarna's 2022 layoff of 700) |
| In 2025, Klarna's CEO said the company was hiring human agents again because cost had driven too much of the decision and quality had suffered | Bloomberg interview with Sebastian Siemiatkowski, as reported by Entrepreneur and Computing (2025) | OK — consistent across secondary reports; the Bloomberg original was not read directly (see Friction) |
| Klarna's assistant handled refunds, returns and payment questions; the release doesn't say whether it could move money | Klarna release (lists refunds, returns, payment-related issues, cancellations, disputes, invoice inaccuracies) | OK — the absence is stated as an absence, not as "read-only" |
| Read access risks a wrong answer; write access (paying an invoice, making a purchase) risks a wrong payment | Reasoning from the two kinds of system access | OK — framed as the video's explanatory distinction, not a sourced finding |
| On 2 June 2026, ING in the Netherlands used Mastercard Agent Pay to buy concert tickets, with the customer approving the final choice | CX Network, "Europe ushers in machine customer era as AI agents buy coffee and concert tickets" (June 2026) | OK — directly stated |
| Days later, Nordea and Mastercard completed Finland's first live agentic payment, purchase and payment handled end to end by the agent | Nordea press release; CX Network | OK — directly stated |
| Agentic tokens kept the real card details away from the agent | Nordea press release ("agentic tokens, ensuring protection of sensitive data") | OK — paraphrased from the release |
| Both were pilots, not services customers can use yet | Nordea press release (described as a pilot); Nordea-linked post ("not available to our customers") | OK — directly stated for Nordea; ING's was also described as a first transaction, not a launch |
| AP2: the request is captured in a signed intent mandate; approval of exact items and price signs a cart mandate | Google Cloud, "Announcing Agent Payments Protocol (AP2)" (16 Sep 2025) | OK — directly stated |
| The sequence forms "a non-repudiable audit trail" | Same Google post ("creates a non-repudiable audit trail that answers the critical questions of authorization and authenticity, providing a clear foundation for accountability") | OK — exact quote |
| Google's announcement doesn't say who pays when something goes wrong | Same Google post: lists accountability as a problem but allocates no liability and describes no dispute process | OK — stated as an absence; "proof isn't liability" is the video's framing |

## Friction protected

- Kept: "two-thirds", not the brief's "67%". That's Klarna's own wording; 67% is a rounding of it.
- Kept: "the equivalent work of 700 full-time agents", not "700 human agents". It's a workload comparison, and the video doesn't imply 700 jobs were cut.
- Kept: Klarna's numbers are called "Klarna's own numbers", and B01 includes the 2025 reversal. The launch claims weren't independently verified, and the company later said quality had suffered.
- Kept: the 2025 reversal is sourced through two secondary reports of the same Bloomberg interview. The Bloomberg piece itself wasn't read.
- Kept: Klarna's assistant is not called "read-only". The release doesn't say either way, so the video says that.
- Kept: the brief's "executing trades" was dropped. No source found shows an agent executing trades, so write access is illustrated with paying an invoice and making a purchase.
- Kept: ING and Nordea are both described as pilots. Neither is available to customers yet.
- Kept: ING's customer approved the final choice, so the video doesn't call that one fully autonomous. Only Nordea's is described as end to end.
- Kept: AP2 is presented as Google's proposal, quoted in its own words, and not as an adopted standard. The video makes no claim about who uses it.
- Kept: the accountability question is left open. Google's post doesn't allocate liability, and the video doesn't guess who should pay.

VERDICT: PASS
