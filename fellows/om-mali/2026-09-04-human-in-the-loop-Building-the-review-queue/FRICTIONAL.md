# Frictional log — 2026-09-04

**Week 5 · human in the loop · A resumable review queue that decides nothing on its own**

A frictional log is not a status report. It records where the work pushed back, what I did
about it, and what I still do not know. Every number here is traceable to
`docs/entity_resolution.md` §10, `docs/review_queue.md` or `docs/worklog.md`.

---

## What I was working on

The week's claim is a **subtraction**. The software routes, groups and presents. It decides
nothing.

Week 3 established that no threshold separates the hard cases and week 4 established that a
model makes them worse. What is left is a queue: resolve what can be resolved mechanically,
stop at the rest, and put a named human in front of exactly those.

Built as a LangGraph graph — `candidates → recall → triage → (accept | review) → persist` —
with `interrupt()` on the review branch and a Postgres checkpointer, so a paused review lives
in a database rather than in a process.

## What I tried, and what I expected

I expected the queue to be long. 5,806 holdings, 24 X.AI spellings, a corpus full of SPV
wrappers — I budgeted for a tedious afternoon of answering.

## Where it resisted, and what I did next

**The unit of work was wrong, and the plan contradicted itself.** The plan asks for both
`unique (raw_id)` *and* "keyed so the same ambiguity is never presented twice". One table
cannot do both: 5,806 holdings are only **231 distinct (issuer, title) pairs**, so a
holding-keyed queue asks the Databricks question 85 times.

I split it into two tables. `review_decisions` is keyed by the **question**;
`match_decisions` keeps `unique (raw_id)` and is the per-holding audit trail. Both invariants
intact, and I logged the conflict against the plan rather than silently picking one.

The result is the number the week turns on: **4,537 of 5,806 holdings (78.1%) resolved with no
human at all** — alias 2,760, LEI 1,681, fuzzy 57, SPV 39 — and the remaining 1,269 holdings
arrive as **42 paused cards behind only 8 real questions.** One human answer fans out to every
holding that shares its key. I answered all eight in seven commands.

**The queue found the Cohere canary by itself.** Week 3 logged 28 `%COHERE%` holdings
contaminating the shipped universe layer. Nothing was added to make the queue look for them;
the card surfaced on its own, showing the disagreement plainly — matcher says nothing, frozen
pattern says `Cohere Inc. [FALSE POSITIVE]`.

**My split trigger's tolerance was proportional, and that is wrong.** It used 2% of the ratio.
At a ratio of 348 that is a window of **±7**, so it flagged three OpenAI questions at 348x,
320x and 306x as "near-integer". Those are the `$1.00` placeholder rows carried since week 2,
not splits. Changed to an absolute ±0.02 with the ratio capped at 20; flagged questions fell
**19 → 9**, and the survivors are SpaceX and Perplexity at exactly 10.0000 and Anthropic at
4.0181. A test pins both what the rule catches and what it must not. *(Week 6 found this fix
was still not enough — see that week's log.)*

**Three more defects, each a different kind:**

- **`match_decisions.decision_key` had a foreign key to `review_decisions`.** It rejected every
  auto-accepted holding — exactly the 78% that never needed a reviewer. The key is a grouping
  identity, not a reference. FK dropped, index kept.
- **The review card broke when redirected.** Windows hands Python a cp1252 stdout, so the
  card's em dashes encoded to bytes that are not valid UTF-8; piping to a file produced
  something `grep` called binary and refused to print. The card is a human artifact, so the CLI
  now forces UTF-8 on stdout.
- **My first band test asserted the wrong side of the boundary.** `DXYZ SpaceX I LLC` scores
  0.90 exactly, which is accepted, not reviewed. Replaced with the week 3 blended-class string
  that scores 0.80, plus a test pinning the band ceiling as exclusive.

**Then the database disappeared, twice, and both were instructive.**

First, the project's Supabase instance stopped resolving. I did not wait for it — I `initdb`-ed
a **local Postgres 17.2 cluster into a scratch directory with no admin rights**, loaded it from
the Parquet layer, and ran the week there. It reproduced the documented counts exactly: 5,806
holdings, 14 quarters, 1 null price, 64 SPVs.

Then **that** cluster died. I had started it from a long-running foreground command, and when
that command was terminated the server went with it (`terminated by exception 0xC0000142`). A
status report I had written minutes earlier said it was running; it was not, and I corrected
that rather than quietly restarting.

Restarting restored everything — 5,806 holdings, 4,537 match decisions, 231 checkpoint threads,
the same 42 paused reviews behind the same 8 questions. The relevant test asserts a paused
review survives a *process* exiting. **This was a server crash and a cold restart with WAL
replay, which is a stronger claim than the test makes** — arrived at by accident, so I logged
it as accidental evidence rather than rewriting the test to take credit.

I also fixed the cause: `DATABASE_SETUP.md` now writes `port` and `listen_addresses` into
`postgresql.conf` rather than passing them with `-o`, and redirects `pg_ctl`'s output so the
server outlives the shell that launched it.

**The root cause of the Supabase outage turned out to be IPv6.** `db.<ref>.supabase.co`
resolves **to an IPv6 address only** — the retired IPv4 direct host. Not a paused project. It
works from a machine with IPv6 egress. I re-ran the whole queue against the real database and
got **identical figures on a different server with nothing migrated**: 231 questions, 189
auto-accepted, 4,537 holdings decided, 42 paused, the same 8 questions, every number matching
the local run to the row. That is the reproducibility claim being cashed rather than asserted.

## What Claude contributed, and what I did with it

Claude built the graph, the CLI (`--run --status --list --show --decide --decide-company
--report --export-fixture`) and 16 tests.

**The eight answers are mine, and three of them disagree with each other — which is the point.**

- **SpaceX, 894 holdings: not a split.** A filing-unit artifact; the same fund reports common
  at 81.00 and preferred at 810.00 on the same date.
- **Perplexity, 18 holdings: a real 10:1 split.** 6,081 → 60,810 shares with value identical at
  $4,228,993.75. This is the plan's own verification case, caught before it entered a series as
  a 90% price crash.
- **Anthropic, 13 holdings: a repricing**, consistent with the verified staircase. The 4.0181
  ratio near 4 is coincidence.

**A detector that treats all three the same way is wrong two times out of three.** That is a
judgment about what the numbers mean, made by looking at share counts across periods — not
something the ratio alone can tell you.

I also refused three things Claude's design would have allowed by default. **Model confidence
is not a queue trigger** — week 4 measured it at 1.000 on 315 of 322 answers including 12 of
the 15 wrong ones, so sorting by it puts the wrong rows at the bottom. **A split is asked even
at 1.00 matcher confidence**, because a suspected split is never auto-adjusted. And **naming a
company outside `companies` is rejected outright** — admitting a company is a
universe-version decision at the week 1 gate, not something to slip in through a review prompt.

**And one correction the figures forced on my own write-up.** I had written "all four `split`
triggers" and "wrong three times out of four". Counted from `review_decisions` it is **three**
split-triggered questions, so it is two times out of three. Same failure mode as week 4's
confidence numbers: a count typed by hand instead of queried, caught only because a figure was
generated from the source data. Perplexity's unchanged value is **$4,228,993.75**, not
$4,228,994 — an earlier query had rounded it with `::numeric(14,0)` before the number reached a
decision rationale.

## What I understand now, and what I still do not

**Understood.** The expensive resource is human attention, and the way to conserve it is to
change the unit of work, not to raise a threshold. 5,806 holdings really are 8 questions.
Durability has to be in the database, not the process — and I now have stronger evidence for
that than I designed.

**Not understood, and carried forward.** The split trigger still does not catch the `$1.00`
OpenAI placeholder; different defect, still open. `securities` is created and empty until week
6 fills it. And the three split answers point in three directions, which means week 6 needs a
detector that distinguishes them rather than one that flags them — I knew that going in and it
turned out to be harder than I expected.

**Carried unchanged:** the live EDGAR path, the 16 `NPORT-P/A` amendments, 314 of 322
golden-set labels unattested, and milestone PR 1 still not opened.
