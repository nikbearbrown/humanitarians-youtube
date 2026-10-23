# Frictional log — 2026-09-18

**Week 7 · analysis · Four questions asked of 5,479 marks, all four answered against
expectation**

A frictional log is not a status report. It records where the work pushed back, what I did
about it, and what I still do not know. Every number here is traceable to `docs/findings.md`,
`docs/_findings.json` or `docs/worklog.md`.

---

## What I was working on

The first week that **measures** rather than builds. Four questions put to the panel:

1. How often does a private mark actually change?
2. When several managers mark the same company on the same date, how far apart are they?
3. How fast does a new price travel from the first manager to the rest?
4. Cerebras went public — what happened to the private mark at the crossing?

## What I tried, and what I expected

The project plan carries an expectation for the first one: **30–40% of consecutive
observations unchanged.** Private marks are supposed to be sticky. That is the whole folk
model of private valuation, and it is why the thesis is interesting.

For the Cerebras study the plan calls it *"a free, clean, private-mark-to-public-price event
study with no additional data collection."*

## Where it resisted, and what I did next

**Marks move more often than the thesis assumed. 25.0% of 4,079 consecutive observations are
unchanged**, not 30–40%. And it is robust: the share only reaches 29.6% if I treat any move
under 1% as flat.

More useful than the headline is the variation underneath it: **Anthropic 2.2% unchanged,
OpenAI 1.1%, Groq 0%, against X.AI 48.5% and SpaceX 37.4%.** A single headline rate for
"private marks" hides a thirty-point spread between companies. I report the rate and
immediately undercut it.

**The dispersion measurement was comparing different securities, and the numbers were absurd
enough to catch it.** My first version reported spreads of **31,983% and 1,098%**. Those are
SpaceX preferred against SpaceX common (a 10x filing convention) and one Coatue mark of
`OPENAI GLOBAL, LLC` carrying **150,000,000 units at $1.5072** — an LLC interest priced per
dollar of commitment, not a share. Now computed within (company, class kind) with scale
outliers set aside and named. That Coatue row also finally pins the long-standing "$1.00
OpenAI" open issue to a single holding.

**The window was a radius, not a span.** I used ±45 days, which is a **90-day span** — and over
90 days Databricks genuinely moved 28.32 → 60.00. Calling that manager disagreement is
nonsense. Now a 31-day forward span, matching the plan's own 4/30-to-5/31 example.

**Propagation conflated staleness with slow propagation.** First-to-last gave lags of 427 and
396 days on Databricks levels — which is not slow propagation, it is managers still carrying a
2023 level in late 2024. The headline is now **first-to-half**, with first-to-last kept beside
it and labelled.

Final answers: **130 dispersion groups of 3+ managers, median spread 10.8%**, p90 40.5%,
widest 111.9% — but **92 of 130 contain more than one price level**, so the disagreement is
mostly about which round is reflected rather than about judgment. And **37 propagation events,
median 30 days to half the adopters**, 90 days to all.

**The Cerebras study cannot be run, and that is a finding about the data rather than an
oversight.** Two structural reasons:

1. The private layer is filtered to `FAIR_VALUE_LEVEL = '3'`, so Level 1 rows never entered
   Postgres — all 5,806 `raw_holdings` rows are Level 3.
2. The Level 1 observation's period end is 2026-05-29, which is in **unpublished 2026Q3**. The
   archive ends 2026-04-30.

I probed the raw zips directly with no fair-value filter: 22 Cerebras row groups in 2026Q2 and
10 in 2026Q1, **all Level 3**. So the earliest possible Level 1 period end is after the archive
ends. What I report instead is the Level 3 run-up — $21.46 → $100.26 across 19 period ends,
+367% — and the report **explicitly declines** to compare against the plan's $236.99, because
that number is in a plan document and not in any filing this project has ingested.

**Then I built the whole harness anyway, and the scan changed what I thought I knew twice.**

I had concluded "no Level 1 rows exist" from probing Cerebras in two quarters. Scanning **all
fourteen** at every level returned **10,566 non-Level-3 rows**, which looked like a flat
contradiction of my own finding.

It was not. **10,126 of them are false positives** — every one of the 7,175 Level 1 rows is
**Coherent Corp, ticker COHR**, caught by the `%COHERE%` canary I planted in week 3. 186 more
are the right company and the wrong instrument. **254 are genuine, and none is Level 1.** The
conclusion survives, and is now measured across fourteen quarters instead of inferred from two.

**And that produced the finding I did not expect: the Level 3 filter was doing double duty as
a precision filter.** Remove it and the frozen week 2 name patterns match the entire public
market — one public company alone produced 7,175 rows. Any future use of the public lane must
route through the matcher and the review queue, not the patterns. The canary earned its keep a
second time.

## What Claude contributed, and what I did with it

Claude wrote `src/signal/findings.py`, `scripts/analyze.py`, the event-study module and the
tests — including 8 that **inject a synthetic Level 1 observation** and assert the arithmetic
the report will print. A harness nobody will exercise for two months has to be proven now, or
the silence in November is ambiguous.

**The correction I most want on the record is a claim Claude wrote and the data did not
support.** The propagation figure asserted **"the biggest events are the fastest"** — a tidy,
plausible, quotable line. I tested it: events with 10+ managers have a median **27 days** to
half against **30** for the rest, and **12 of 28 smaller events land at zero days against 3 of
9 large ones.** The pattern is weak and partly runs the other way. Replaced with counts that
hold: 15 of 37 at zero days, slowest 92.

Three more hand-typed values standing in for measured ones, all caught by reading the rendered
figures:

- a subtitle hard-coded "Nine managers" when the Anthropic window holds **8 managers, 11
  marks**;
- the red/grey split in that window hard-coded at `price > 220`, now the same single-linkage
  level clustering the analysis actually uses;
- the dispersion highlight hard-coded at `spread >= 0.4`, now the measured p90.

**Two things I refused to claim.** Within-level agreement is **not** reported as a finding
anywhere — it is bounded by the 2% clustering threshold by construction, so quoting it would
restate a definition and dress it as a result. And same-date dispersion still mixes
disagreement with update timing; the level decomposition narrows that but does not remove it,
and the write-up says so.

**One more defect worth naming because it is invisible:** a bare `%` inside an **SQL comment**
broke a parameterised query. psycopg2 scans comments for placeholders too.

## What I understand now, and what I still do not

**Understood.** The folk model is wrong on this cohort — marks move. The interesting structure
is between companies, not in the average. Most same-date disagreement is about *which round a
manager has reflected*, not about valuation judgment, which means propagation speed is the
honest measurement and dispersion is a proxy for it. And a negative result that explains its
own cause is a deliverable; "the study cannot be run, here are the two structural reasons" is
more useful than a study run on data that does not support it.

**Not understood.** The Cerebras study unblocks only when `2026q3_nport.zip` publishes —
roughly November 2026 — and until then the harness is proven against injected data and nothing
else. The three-pile classifier in `scan_quality` is approximate; a few Level 2 LLC co-issuer
notes still land in the candidate pile, and the conclusion does not depend on it only because
no candidate is Level 1 under any classification. The `$1.00` OpenAI row is now identified but
still priced in the panel; excluding it is a universe change, not a findings change.

**Carried:** the live EDGAR path (which is exactly what the Cerebras study needs), non-USD
currency guarded but unexercised, 314 of 322 golden-set labels unattested, the 28 `%COHERE%`
holdings still inside the shipped universe layer, milestone PRs 1 and 2 still not opened.
