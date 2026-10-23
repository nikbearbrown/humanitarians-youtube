# Frictional log - 2026-10-16

**AI Debt Tracker, week 1 · feasibility · Building the answer key and choosing the model**

A frictional log is not a status report. It records where the work pushed back, what I did
about it, and what I still do not know. Every number here is traceable to `DESIGN.md`,
`docs/feasibility.md`, `docs/bakeoff.md`, `docs/universe_v1_review.md` or `docs/worklog.md`
in the project.

---

## What I was working on

A new project. The Private AI Valuation Agent was finished, and I went looking for the gap in
Mycroft's "Using AI to Invest in AI" coverage. There was no debt or credit agent at all, while
borrowing to pay for data centres, chips and power was one of the central AI-investing questions
of 2026. So I scoped an agent that keeps a ledger of every bond and loan 25 AI-sector companies
owe, built only from filings as they appear, and graded against each company's next quarterly
report.

Before writing any agent code, I wanted two things settled. Is there anything for an agent to
find? And can I grade it honestly? This week was that groundwork: the design, a feasibility spike
on real data, professor sign-off, the answer key, a point in time server, a bond matcher, and the
model choice.

## What I tried, and what I expected

I wrote the design with go/no-go checks and their pass lines fixed **before** running anything,
so a result could not move the goalposts. Four checks: are debt changes announced before the
report, is there headroom over doing nothing, can bonds be matched between reports, and can a
local model read the filings.

My expectations going in:

- **That most companies would be gradeable bond by bond.** The first probe counted debt tags and
  said 21 of 25.
- **That the larger model would win.** The design named `qwen3:8b` as the main pick and
  `qwen3:4b` as the fast fallback.
- **That a better matcher would carry most of the gain** over the Week 0 matching rate of 83%.

I also set the rules for the bake-off in advance: the same documents, the same prompt and one
shared pass line for every model, with the pick decided by the scores.

## Where it resisted, and what I did next

**The tag counts were lying.** When I looked at the instruments behind the counts, Microsoft's
13 "bonds" were issuance groups numbered One to Thirteen. Oracle's quarterly reports tagged only
that quarter's new bonds, 4 to 14 of about 56. IBM tagged maturity-year buckets, and Digital
Realty and Oracle tagged subtotals next to the bonds. I replaced counting with **coverage**: a
report is graded bond by bond only if its itemised instruments account for at least 80% of total
debt. Under that rule the answer is 15 of 25, not 21. That changed what the agent is even allowed
to be graded on, so it had to be fixed before anything else was built on top of it.

**The bulk data was not shaped the way the docs suggested.** The SEC publishes only the last 12
months as monthly files, with older months quarterly, so the loader handles both. The bulk data's
own `accepted` timestamp was hours off for the same filing, so every cutoff comes from the EDGAR
submissions index instead. A cutoff that is hours wrong is exactly how future information leaks
into a test.

**The bulk data rounds coupons.** 9.625% becomes 9.63. The member names usually keep the full
rate, so the parser reads the name and uses that. It also has to cope with filers writing numbers
in words, with typos (`ThreePointTwoFieveZero...`), and with years glued onto coupons.

**My Week 0 model test was too easy.** The spike's prompt told the model which coupon to look
for, so its perfect coupon score was built in. I made the bake-off harder on purpose: the model
gets only the document.

**The 8B models ran away.** Both of them looped on their own instrument lists until they hit the
output limit, and one `qwen3:8b` run looped for 10 minutes before a cap existed. I added the cap.
Even with the runaways left out, `qwen3:8b` reached 89% against the 4B model's 95%, and it also
labelled new issues as redemptions or exchanges. **So the smaller model won by the rule I had set
in advance, and I reversed the design's main pick.**

**The answer key was wrong in six places.** Using the next report as truth for an announcement
breaks when the two describe different moments: euro notes reported in dollars, a pricing release
quoted before the banks' extra allotment, a floating-rate spread read as a coupon, and one filing
with no amount at all. I logged the corrections in a separate file rather than editing the truth
data, and the scorer applies them. Re-scored, `qwen3:4b` reached 99%, `llama3.1:8b` 91% and
`qwen3:8b` 88%. The ranking did not change.

**The matcher was not where the gain came from.** The new matcher reached 93.4% on bond-by-bond
episodes. When I ran the Week 0 method on the same episodes it scored 92.1%. The matcher adds a
point or two. Grading each episode at the level the company actually reports does the rest. I
wrote that down instead of claiming the matcher's number as an improvement.

**Library and tooling decisions.** `mcp` 2.x renamed `FastMCP`, and the adapters I need in week 5
target 1.x, so I pinned it below 2.0. I kept Ollama at 0.34.0 so that Week 0 and Week 1 speeds
stay comparable. All the bulky data (2.8 GB of SEC zips, the filing cache and 4.9 GB of model
weights) lives outside the repo on a local drive, configured through a gitignored `.env`.

## What Claude contributed, and what I did with it

I used Claude Code as the implementer. It wrote most of the code to my design: the bulk loader,
the parser, the matcher, the point in time server and its tests, and the bake-off harness. It ran
the scripts against live data and drafted the documents.

What I kept for myself was the scope and the decisions:

- **The project choice and its fit with Mycroft**, and getting the professor's approval before
  committing to it.
- **The pass lines and the model rule, set before any result existed.** That is the only reason
  the reversal from 8B to 4B is a finding and not a preference.
- **The point in time rule.** The server refuses the report being graded and anything accepted at
  or after the cutoff, and fails closed on any filing it cannot date. I also wanted a structural
  test that nothing outside the evaluation code can import the answer key, so the agent can never
  reach it by accident.
- **Pushing past the first answer.** The first pass of the universe agreed with the Week 0 probe.
  I had the instruments themselves inspected rather than accepting the count, which is how the
  21 became 15.

**The week 1 gate review.** Checking 29 bond announcements and 14 companies' tagging needs a
reading of bond terms that I do not have yet. So I had Claude do that review and record it
explicitly as a model judgment (`docs/week1_review.md`). Then I read it, checked the decisions
it raised and made the call. Two of those were ties I resolved on substance, not by the default
rule: Meta moved to grading by offering, and TeraWulf to bond by bond. The gate record
(`manifests/week1_gate.json`) names me as the person who cleared it, and on what basis.

## What I understand now, and what I still do not

**Understood.** Ground truth has to be inspected before anything is built on it. A count looked
like a measurement and was not. An announcement and a later report can both be right about
different moments, so the agent's document reader must be scored against the document and its
ledger against the report. A small model given only the document can beat a larger one, and the
only way to know is to fix the rules before you run it. And an honest comparison sometimes shows
that your own improvement is smaller than it looks.

**What I still do not know.**

- **Whether the agent works.** Nothing in this week reads a filing end to end and updates a
  ledger. That starts in week 2, with the grader built first.
- **How far the model choice holds.** 29 documents from 12 companies, one prompt, thinking turned
  off. Zero-coupon convertibles answered as `null` instead of 0 cost a point each.
- **How to handle the companies that tag almost nothing** in their quarterly reports, such as
  Intel and Oracle. They can only be graded on totals, and across all episodes matching drops to
  85% because of them.
- **The finer points of bond terms.** Over-allotments, floating-rate spreads and currency
  conversions are where I am still learning, and they are where most of this week's corrections
  came from.
