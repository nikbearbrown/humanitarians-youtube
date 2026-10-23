# Frictional log — 2026-08-08

**Week 1 · data verification · Can a per-share price be derived from SEC Form N-PORT?**

A frictional log is not a status report. It records where the work pushed back, what I did
about it, and what I still do not know. Every number here is traceable to
`docs/feasibility.md`, `docs/worklog.md` or `logs/RUN_LOG.md` in the project repo.

---

## What I was working on

Establishing whether the whole project was possible at all.

The idea is simple arithmetic: a mutual fund that holds private company stock must file Form
N-PORT, and that filing reports the position's value in dollars and its balance in shares.
Divide one by the other and you get a per-share price for a company that has no public price.

Everything downstream depends on that being true in practice and not just on paper. So week
one was deliberately not a build week. It was: go to EDGAR, open real filings by hand, do the
division myself, and see whether the number means what I think it means.

## What I tried, and what I expected

I hand-verified **19 Anthropic PBC positions across 6 fund families** — Fidelity, T. Rowe
Price, Alger, ARK, BlackRock and Capital Group — reading `primary_doc.xml` directly off EDGAR
rather than through any library.

My expectation was that managers would disagree. Private marks are discretionary; six firms
valuing the same illiquid asset should produce six different numbers, and I assumed the
interesting result would be measuring the spread between them.

I also expected to be able to separate private positions from public ones using the filter the
project plan specified: `CUSIP = 'N/A'` plus `isRestrictedSec = 'Y'`.

## Where it resisted, and what I did next

**The managers agreed, and that was the surprise.** Four of them marked Anthropic at
**$259.14** on the same period ends, and the repricing to **$589.0095** showed up across
filers too. Agreement, not dispersion, was the finding — which changed what the project is
about. If managers converge, the measurable thing is *how fast* a new price propagates between
them, not how much they differ. That reframing drove the entire rest of the plan.

**The plan's filter was broken, and it took hand-checking to see it.** It kept **1 of 6
managers**. Two independent causes:

- `CUSIP = 'N/A'` misses the `000000000` placeholder, which other filers use for the same
  thing. The field is free text `VARCHAR2(9)`, not a validated CUSIP, so spellings vary by
  filer and there is no canonical form to match on.
- **ARK and Capital Group report `isRestrictedSec = 'N'` on restricted stock.** The flag is
  simply wrong in their filings. I passed it through verbatim rather than repairing it,
  because the ingest layer's job is to preserve what was filed.

I replaced the filter with `fairValLevel = 3` as the load-bearing field, demoting CUSIP and
the restricted flag to supporting signals. That is written up as `docs/feasibility.md` §2 and
had to be settled before any ingestion could start.

**Then the replacement filter failed in the opposite direction.** Once I downloaded the bulk
quarter — 440.7 MB, 5,347,869 holding rows — the corrected filter kept **693,951 rows, 11.3%
of the quarter**, where the plan predicted "a few thousand". `CUSIP='N/A'` is the generic
no-CUSIP placeholder used by bonds, derivatives and cash equivalents. It is not a
private-company marker at all.

So I **inverted the pipeline**: match the universe by issuer name *first*, then confirm with
the fair-value level. The plan's filter-then-resolve order would have fed 600,000 rows into
entity resolution; name-first reduces it to roughly 1,000 per quarter. Anthropic is 149 rows.

**Two name-matching traps, caught before they became a data set.** `%COHERE%` matches
**Coherent Corp**, a public NYSE optics company — 1,094 rows, none at Level 3. A substring
matcher would have invented an entire price series for a company that was not there. And
`%X.AI%` is mostly `X.AI LLC TL 1L BANKDEBT` and 144A bonds priced per $100 of face value;
only 7 rows are actually Level 3 equity.

**One error was mine.** Three positions were recorded under accession `0000035402-26-003312`
when the bulk data showed they belonged to `0000035402-26-003406`. A transcription slip on my
side, not a discrepancy in the data. I fixed the fixture and re-ran; the comparison then came
out **15/15, 0 mismatches**.

## What Claude contributed, and what I did with it

Claude wrote the downloader (`src/ingest/download_bulk.py` — User-Agent, 10 req/s throttle,
resumable via HTTP Range) and the comparison script, and it drafted `docs/feasibility.md`.
That is the right division: those are mechanical, well-specified jobs.

What it could not do is the part that mattered. **The filter defect was only visible because I
opened six filings by hand and noticed that five managers' positions had vanished.** No amount
of code review finds that, because the code was correct — it implemented the plan faithfully,
and the plan was wrong. Claude also initially accepted the plan's "a few thousand rows"
estimate; the 606,028-row measurement that contradicted it came from running the thing and
reading the output, which is a decision to distrust the spec rather than a capability.

I also rejected the instinct to "fix" ARK's incorrect restricted-securities flag. Claude's
first pass at the comparison treated the mismatch as something to normalise. It is not — it is
a filed fact, and correcting it in ingest would mean the database no longer says what the SEC
says. That rule became structural: the raw layer is the SEC's bytes, rearranged but never
repaired.

## What I understand now, and what I still do not

**Understood.** The arithmetic works, and `fairValLevel = 3` is the only field that reliably
separates private marks — which also means the project inherits whatever the filer decided
when they assigned that level. Managers converge rather than diverge, so propagation speed is
the real measurable. Every field in the DERA layout is nullable, **including the fair-value
level the whole filter now depends on**, so `NULL` has to be handled explicitly rather than
assumed away.

**Not understood, and stated as such at the gate.** Whether the corrected filter's precision
holds on quarters I have not looked at — recall is 100% on the verified set, precision is
untested. Whether the bulk DERA TSVs preserve the raw XML's placeholder values across all
quarters, or only the one I checked. And the universe itself is a judgment, not a measurement:
I froze it at 6 full members plus Figure AI carried thin, on a criterion of 28+ distinct filers
per quarter, and that threshold is mine. Cerebras stays in despite being the smallest member
purely because its Level 3 → Level 1 IPO transition is the only external validity check the
project has.

**The gate was cleared by me, by name, on 2026-08-08.** Not by the pipeline.
