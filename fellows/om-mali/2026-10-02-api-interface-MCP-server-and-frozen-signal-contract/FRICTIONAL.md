# Frictional log — 2026-10-02

**Week 9 · API & interface · A read-only MCP server, and a signal contract frozen at 1.0**

A frictional log is not a status report. It records where the work pushed back, what I did
about it, and what I still do not know. Every number here is traceable to `docs/mcp_server.md`,
`docs/signal_and_commentary.md` or `docs/worklog.md`.

---

## What I was working on

Making the data usable by something other than me.

Up to this week everything was a script I run and a document I read — fine for building,
useless to anyone else. Two pieces: an **MCP server** so an AI assistant can query the panel
directly, and a **frozen JSON signal contract** another system can parse without guessing.

## What I tried, and what I expected

I expected the protocol to be the hard part. It was not; the server took an afternoon.

## Where it resisted, and what I did next

**The real constraint is size, and it is severe.** `get_marks('Databricks, Inc.')` returns
**2,151 rows**, which serialise to **575,000 characters — roughly 143,000 tokens.** Past most
context windows, and useless even where it fits, because a model handed 2,151 rows does not
read them.

Bounded, the same call is **18,000 characters**. So every response is summary-first: a summary
describing the **whole result set**, one bounded page, and an opaque cursor. The summary detail
matters — one computed over page one would say "3 managers" about a company held by thirty.

**Two bounds, not one.** A row limit (50, max 200) *and* a hard ceiling on the serialised
response (48,000 chars). Row width is not uniform — a fund-exposure row is several times a
marks row — so a row count alone is not a size bound. And cursors are bound to their query: a
cursor from `get_marks("Databricks")` reused on `get_marks("Anthropic")` is rejected rather
than silently returning Anthropic rows numbered from Databricks' offset.

**I was wrong three times in a row about how a client launches a server, and all three were
invisible from inside it.**

1. I wrote a config using the `cwd` key with `args: ["-m", "src.mcp.server"]`. Claude Desktop
   does not apply `cwd` before Python resolves `-m`, so it reported
   `ModuleNotFoundError: No module named 'src'`. That configuration could never have worked.
2. I then suggested `claude mcp add --cwd`. **That flag does not exist** —
   `error: unknown option '--cwd'`.
3. The command finally succeeded and registered the server under
   `projects["C:/WINDOWS/System32"]`, because the default `--scope` is local and that was the
   working directory.

The fix is to launch `src/mcp/server.py` **by absolute path** — it puts the project root on
`sys.path` itself and loads `.env` explicitly, so it needs no working directory at all.
Verified from `C:\Windows`. Registered at user scope, `claude mcp list` reports
**private-ai-valuations - Connected**, and the selftest answered 6 of 6 tools in the same
session.

**The test gap is the part worth keeping.** My existing stdio test passed `cwd=ROOT` to
`StdioServerParameters` — so it proved the server works *when something sets the working
directory*, and the one client that matters does not. **A test that supplies what the real
caller omits cannot find that class of bug.** I added three tests, including one that starts
the server with no cwd and no `PYTHONPATH`.

(The documentation test then failed on the documentation of its own fix: a character window ran
into the prose quoting the broken `-m` form in order to warn against it. Now scoped to the JSON
fence.)

**The model the plan names has been retired.** `llama-3.3-70b-versatile` returned HTTP 404
"model does not exist or you do not have access to it" on a valid key. The refusal path did its
job — it recorded the error rather than inventing a note. I fixed it as a *class* rather than a
substitution: a preference **list** resolved against the live `/models` endpoint, with the
plan's choice first so a substitution stays visible, and the signal records the resolved model
id rather than the backend name.

**That model then exposed four defects:**

1. **An empty note was accepted.** It passes every content check trivially — nothing to
   fabricate, nothing to rank, no placeholder. A reasoning model had spent all 700 tokens on
   its hidden channel and returned no prose, reported as "0 words" with `refused: false`.
   `max_tokens` raised to 4,000 and `MIN_WORDS = 60` added.
2. **Spelled-out numbers were unchecked.** "across sixty-one groups" was correct — and would
   have passed identically if it had been wrong.
3. **`median_days_to_half` was glossed as "days to halve the price impact"** — wrong reading,
   right number, and no mechanical check disputes it. The prompt now defines the term.
4. **Check order was wrong.** A short draft containing a fabricated figure was told only that
   it was short. Length now runs last.

## What Claude contributed, and what I did with it

Claude wrote the server, the paging module, the queries, the contract, the quarterly graph and
the commentary module.

**The finding of the week came from Claude's output being wrong in a way my check could not
see.** The first real commentary run passed grounding cleanly — every number in the prose was
one the model had been given — and the prose still said *"Anduril has the lowest number of
marks, at 509"* one sentence before *"Figure AI has the lowest number of marks, at 31."*

Both numbers were real. The **ranking** was invented, and it contradicted itself within a
paragraph.

So there is now a **superlative check**: a claimed extreme whose figure is not the extreme
value of any field fails the draft, and the draft goes back to the model with that specific
complaint, up to three attempts. **A check beats a bigger model, because it fails the same way
on any model.** (Tightening its regex then made end-of-sentence numbers unmatchable, because
`(?![\d.])` rejects a trailing period — fixed to `(?!\d)(?!\.\d)`.)

**Two refusals I want recorded as decisions rather than omissions.**

**Read-only is a design decision.** Nothing in the server writes — no tool records a decision,
clears a gate or changes a mark. A resolution decision needs a named human, and a tool a model
can call is the opposite of that. A model using this server reads every judgment already made
and sees what is still open; it cannot make one.

**No model, no template.** With no backend reachable the commentary is refused and the reason
is recorded, and the signal is emitted without it. A templated paragraph carrying
`is_model_output: true` would be indistinguishable from model output while not being any.

The contract itself refuses **ten field names** — `valuation`, `market_cap`,
`shares_outstanding`, `irr` and the rest — enforced by the JSON Schema *and* by an independent
name scan for anywhere the schema does not reach. That is structural rather than stylistic:
these filings give a fund's share count, never the company's total shares, so there is no
arithmetic here to a company's value. A field for it would invite a consumer to fill it from
somewhere else and inherit that source's error.

**And I corrected two of my own documents for overstating.** `docs/mcp_server.md` said no
external client had been exercised (false once Claude Code connected) and implied the
in-process stdio roundtrip was sufficient evidence a desktop client could call the server —
which three consecutive failures disproved. The README first claimed "295 regression tests, 39
skip"; both numbers move with the environment, so it now states **334 collected** and says the
split depends on the machine.

## What I understand now, and what I still do not

**Understood.** Shipping data to a model is a budgeting problem before it is a protocol
problem. A grounding check that verifies every number is still blind to a relationship *between*
numbers — correctness of parts is not correctness of claims. And the class of bug I hit three
times is a property of the caller's environment, which means a test has to *withhold* something
to find it.

**Not understood, and stated.** **Claude Desktop itself was not exercised** — Claude Code and
Claude Desktop read different config files, so one connecting does not prove the other, and I
said exactly that rather than generalising from the client that worked. Qualitative adjectives
in the generated commentary are unchecked by design; only numbers and rankings are mechanically
verified. And milestone PRs 1 and 2 are still not opened.
