# Frictional log — 2026-09-25

**Week 8 · data integration · Two new SEC sources, and a join that would have been wrong**

A frictional log is not a status report. It records where the work pushed back, what I did
about it, and what I still do not know. Every number here is traceable to `docs/context.md`,
`docs/identity_queue.md` or `docs/worklog.md`.

---

## What I was working on

Adding two sources beside the marks panel, both answering questions N-PORT structurally
cannot:

- **Form D** — when a company actually sold stock, and how much it raised.
- **The Reg S-X 12-12 restricted-securities footnote in N-CSR/N-CSRS** — when a fund bought in,
  and what it paid.

Neither produces a price. Neither can produce a valuation. The point is corroboration: if a
fund says it acquired shares on a date, and the issuer independently says it sold shares on
that same date, those two filings agree without citing each other.

## What I tried, and what I expected

The obvious implementation is a name join. Scan the Form D archive for universe company names,
group by company, and you have round timing and amounts.

I expected that to mostly work, with some noise to filter.

## Where it resisted, and what I did next

**84.3% of the name matches are feeder funds, and a name join would have published a clean
table of numbers that no company's filing ever produced.**

Scanning 49 quarters (2014Q1–2026Q1) for universe company names returns **706 issuer rows.
595 of them are self-declared pooled investment vehicles.** "Anthropic Jan 2026 a Series of
CGF2021 LLC" is a feeder raising money to buy Anthropic shares on the secondary market. Its
`TOTALAMOUNTSOLD` is the *feeder's* raise, not Anthropic's round. Summing those per company and
calling it "round timing and amounts" would have been confidently, precisely wrong.

The plan said "join on resolved issuer identity, not name string". **This is the number behind
that sentence** — I did not know it was 84.3% until I measured it.

So the architecture changed: name scan → **candidate pool**, machine triage on the filer's own
`ISPOOLEDINVESTMENTFUNDTYPE` declaration (a filed fact, not an inference), then a named human
affirms the CIK. Until a CIK is affirmed, `form_d.resolved()` returns nothing and every
timeline's Form D leg is empty. **That is the designed state, not a gap.**

I then affirmed all **46 identity decisions** myself — 7 `operating_company`, 12 `vehicle`, 27
`not_in_universe`, 0 outstanding. **`x.ai, inc.` (CIK 1609052) was rejected, and that is the
one the automated proposer got wrong and the evidence got right.** The join went from 706 name
matches to **47 real filings**: SpaceX 19, Databricks 17, X.AI 6, Groq 3, Figure AI 1,
Perplexity 1.

**Five filers, five layouts, one parser.** Reg S-X names the required *contents*, not the
columns. Baron, Fidelity, Lincoln and Neuberger each use a different table — and **BlackRock
uses no table at all**, putting "(Acquired 10/22/19, cost $3,030,010)" inline in the Schedule
of Investments line. I map columns by reading the header row, so a sixth filer with a labelled
header needs no code at all; the inline form needed its own parser, and until it had one every
BlackRock filing returned zero.

**Two more things the filings forced.** Acquisition dates are often **ranges**
("11/15/2017-8/4/2020") — both ends are stored. And cost is not always per position: Baron
gives one cost per fund and says so, which is why `cost_basis_scope` records `position`,
`fund_total` or `absent` rather than pretending every number means the same thing.

**The finding, and the denominator that makes or breaks it.**

With both lanes joined on an affirmed CIK, **10 of 18 fund acquisition dates fall on the exact
day an issuer reported a first sale (56%)**, and 11 of 18 within a week. Databricks' 2019-10-22
$400m round is the clearest case: five separate registrants independently disclose acquiring
Databricks stock that day.

**But that 56% is only honest because of how the denominator is drawn.** I count only
acquisitions *inside* a company's Form D filing window. SpaceX stopped filing Form D in July
2022, and 9 of its 13 single-date acquisitions postdate that — measured against the nearest
round they give gaps of 873, 911, 1090 and 1293 days, each of which is the distance to the end
of the archive rather than anything about a fund. **Left in the denominator, a real 56% reads
as 33%.** Date ranges are excluded for the same reason: a position built over three years has
no single acquisition date, and picking an endpoint would manufacture the match or the miss.

I put both numbers in the write-up and in the video, because a reader who only sees 56%
cannot check me.

## What Claude contributed, and what I did with it

Claude wrote `src/ingest/form_d.py`, `src/ingest/ncsr.py`, `src/resolve/identity.py`,
`src/signal/exposure.py` and 74 tests, with no new Python dependency and downloads reusing the
existing fetcher parameterised by base URL rather than copied.

**The date parser is the bug I want recorded**, because it failed silently and completely.
Every pre-2020 Form D filing returned a NULL date — 706 rows, hundreds of them unusable, and
nothing raised. The archive switches `FILING_DATE` format partway through its history: older
sets use `2015-03-31 17:28:10`, newer ones use `30-SEP-2024`. The parser handled one. Fixed to
strip any time component and try three formats; **all 706 now parse.** A parser that returns
None on an unknown format is a parser that discards half your archive and tells you nothing.

**Two guards I added after watching what the code would otherwise accept:**

- **`affirm` let `reviewer="auto"` through.** The guard only tested that the reviewer string
  was non-empty. The entire point of the affirmation step is that a *person* decided; a
  non-empty string is not a person. Added a rejected-names set covering "auto", "system",
  "claude" and similar.
- **The N-CSR parser guessed a fund name from prose, and guessed wrong.** Fidelity's footnote
  is preceded by "each Fidelity Central Fund's financial statements…", so the last fund-shaped
  phrase before the footnote was a real fund — just not the one holding the position. Now the
  fund name is read **only** from table heading rows, and is NULL everywhere else. A plausible
  wrong answer is worse than a null.

**A re-ingest duplicated lots** — 715 rows where 252 were parsed — because the unique key
contains parsed fields, so improving the parser changes the key. Fixed by deleting and
rewriting a filing's lots as a unit. The filing is immutable; its *parse* is not.

**And one check tested the wrong thing.** `footnote_present` tested raw HTML, but BlackRock's
inline parenthetical is split across tags — so it reported `footnote_found=False` and
short-circuited the parse on exactly the filer that needed the new code path. Now it tests
flattened text, and parses unconditionally.

**One claim in my own draft log was overstated and I caught it before writing.** I had written
that three independent filers showed cost-to-value multiples of 13.27×, 13.91× and 14.32×. It
is **two** distinct registrants, and 13.91 was a different lot. Corrected before it shipped.

## What I understand now, and what I still do not

**Understood.** Identity has to be an affirmed EDGAR CIK, not a normalised name — and the cost
of getting that wrong is quantified at 84.3%, not asserted. Two filings agreeing without citing
each other is evidence; it is not causation, and the write-up says so. The denominator *is* the
method on a corroboration statistic.

**Something I can observe but cannot explain.** **Anthropic, OpenAI, Anduril and Cerebras have
filed no Form D under their own identity anywhere in the published archive.** Every hit on
their names is a vehicle. Two explanations fit — reliance on the statutory Section 4(a)(2)
exemption, which requires no Form D, or a form or quarter the archive does not carry — and
filings alone cannot distinguish them. So I report the observation and decline the cause.

**Not understood, and stated as limits.** Entry dates are a **floor, not a history**: only the
latest annual and semi-annual report per registrant were fetched, so an older purchase
disclosed in an older report is simply not in view. N-CSR coverage is the top 30 of 98
registrants holding a top-three company. And milestone PRs 1 and 2 are still not opened — git
is mine to run and I have not.
