Read the Receipt Backwards: Auditing an AI Agent's Purchase (Mastercard Agent Pay)

An AI shopping agent bought $42.50 of groceries. The receipt was complete, every field was
well-formed, and it said Morgan authorized the purchase. Morgan never saw it. That receipt came out
of an early version of my own build, a working reference pipeline for the checks Mastercard has
publicly described for Agent Pay.

This video reads that receipt backwards. Start at the bottom, and for every line ask one question:
which step checked this before it was written down? A line with an answer is earned. A line without
one is being carried along. Line by line, you'll see the check that earns each one, two real bugs
that review rounds and this video caught (and the fixes, with tests), and the one line the build
deliberately leaves open because the public record stops there.

Chapters:
0:00 A receipt that shouldn't exist
0:21 What this is, and what it gives you
0:47 The move: read it from the bottom up
1:05 The agent line: registered, then verified
1:23 The person line: does this agent belong to this person?
2:02 The category line: a capital H, found while making this video
2:33 Where that fix stops, on purpose
2:48 Amount and date
3:02 The path line, and a gate with no built-in rule
3:21 What a seal can and can't do
3:43 The merchant line: the open box
4:04 Your turn: audit one record of your own
4:25 Sign-off

Your turn: take one record your own system writes (a receipt, an approval, a log line). Go from the
bottom to the top, and next to every line write down the step that checked it. For any line with
nothing next to it, add the check, or say on the record that it isn't verified.

The build (82 tests, plain Python, no external services, runs on mock data):
https://github.com/nikbearbrown/mycroft/tree/main/case-study-workflows/mastercard-agent-pay-workflow

Sources, in order of appearance:

- Mastercard, "How Verifiable Intent builds trust in agentic AI commerce" (March 5, 2026)
  https://www.mastercard.com/global/en/news-and-trends/stories/2026/verifiable-intent.html
- Mastercard, "Agentic token framework: Driving trusted AI transactions" (October 14, 2025)
  https://www.mastercard.com/global/en/news-and-trends/stories/2025/agentic-commerce-framework.html
- Mastercard EEMEA newsroom, Signals report on agentic commerce (August 2026)
  https://www.mastercard.com/news/eemea/en/newsroom/press-releases/en/2026/august/building-trust-for-agentic-commerce-mastercard-signals-report-explores-the-path-forward/

What this video claims, and what it does not:

- The build is a reference implementation made only from what Mastercard has published. It is not
  Mastercard's system and doesn't use any Mastercard code, credentials or services.
- The opening receipt is a reconstruction of the early version (the ownership check removed, nothing
  else changed), and it's labelled that way on screen. Every other result on screen is a live run of
  the current build or its first version.
- Where Mastercard hasn't published a mechanism, the build says so instead of inventing one: what
  happens when a consumer never set a rule for a category (the gate ships with no built-in rule), how
  a merchant restriction is checked, and how the record is signed. Mastercard describes its record as
  tamper-resistant, with cryptographic proof. The build's record is a plain object, on purpose.
- "A seal protects a record after it's written; it can't make the lines true" is a general point
  about signed records, not a claim about how Mastercard's record works inside.
- Every quotation is on screen, with its source, while it's spoken.

Narration is a synthetic voice (Kokoro, run locally). Visuals are original animations and real
terminal output from the build; no third-party images, and open-licence fonts only.

Humanitarians AI — @HumanitariansAI
Tanmay Kulkarni, in for Humanitarians AI

Tags: Mastercard Agent Pay, agentic commerce, AI agents, Verifiable Intent, AI payments, agentic
tokens, AI shopping agent, software testing, audit trail, Humanitarians AI
