# One Door In — script

**Format** `ai-explainer` (16:9) · **Channel** claude-hai · **Register** Pragmatist
**Persona** Simba · **Voice** Kokoro `af_bella` · **Slug** `hai-mycroft-gateway`
**Runtime** ~4:45 (16 beats, estimated at Kokoro's measured ~3.6 words/sec — audio generation sets the real clock)

---

## The one idea

> A caller must not be able to make an unlogged call. Sprint 2 built one public door into three
> model tiers — `GatewayClient.call()` — that writes a logbook row before it ever returns,
> success or failure. Everything else this sprint did (which models, what they cost, what broke)
> follows from protecting that one guarantee.

**Every figure in this script is the sprint's own** — 56 passing tests, 3 live calls, a hand-verified
cost match, and the caveats it carried forward on purpose (mid/strong tiers not yet live-gated, one
provider as a single point of failure). Nothing here is rounded up or softened past what the source
report itself says.

---

## Beat sheet

### B00 · INTRO — cold open
`ClaudeComposerAsk` · ~17s

**On screen**
- Greeting types in: `Hi, Simba` · terracotta spark
- Composer holds the ask, send button arms
- `wiring the gateway…` then output lines land — the ask arrives already answered

```
topic:    MYCROFT · NO UNLOGGED CALLS
segment:  One Door In
command:  "This sprint has to give three different models one shared front door —
           how do you guarantee nobody can call a model without it being logged,
           or priced?"
output:   → one door in: GatewayClient.call()
          → no caller can skip the logbook
          → first real dollars spent: three calls, verified by hand
folder:   @HumanitariansAI
```

**Narration**
> Hi, I am Simba, and this video is about the second Mycroft sprint — the one that built a single
> gateway all three model tiers have to go through. Cost and latency now get logged automatically
> on every call, with no way for a caller to skip it. This sprint also spent its first real
> money — three live calls, a fraction of a cent, checked by hand.

---

### B01 · EXECUTIVE SUMMARY — BLUF
`ClaudeCallout` or spark-card · ~14s (one breath, mandatory)

**On screen**
- Single sentence sets, terracotta underline settles beneath it

**Narration**
> The rule this sprint enforced: a caller must not be able to make an unlogged call. If logging
> happened after a response came back, someone would eventually forget — and a missing row
> wouldn't look like an error. It would look like a cheaper month.

---

### B02 · STRUCTURE — the one door
Custom scene — **needs building** · ~14s

**On screen**
- `GatewayClient.call()` sits alone as the single labeled entry point
- Adapter and logbook draw in as two things it wraps, not two doors
- A failed call still produces a written row — shown explicitly, not implied

**Narration**
> So there's exactly one public door in: `GatewayClient.call()`. It wraps the model adapter and
> the logbook together, and it writes a row before it returns — even when the provider fails. You
> can't get a response out of this gateway without a record of what it cost.

---

### B03 · STRUCTURE — layer separation
Custom scene — **needs building** · ~21s

**On screen**
- Three labeled layers stack: Adapter (makes the call, reports tokens/latency) → Client (prices,
  times, records) → Router, *coming Sprint 3* (chooses a tier, no network at all)
- Each layer's "does not" is as visible as its "does"

**Narration**
> Underneath, the work is split into layers that each do one job. The adapter makes the call and
> reports tokens and latency — nothing else. The client prices, times, and records. The router,
> coming next sprint, only chooses a tier — no network access at all. If adapters logged their own
> calls, every new provider would be a chance to log slightly differently, and a later sprint's
> baseline needs every row shaped exactly the same.

---

### B04 · WHAT WAS BUILT
Custom scene — **needs building** · ~19s

**On screen**
- File list lands as a compact table: `adapters/base.py` · `adapters/fake.py` · `adapters/groq.py`
  · `client.py` · `tiers.py` · `tiers.json` · `first_live_call.py`
- Totals stamp beneath: 7 modules + 4 test files · 1,015 lines · 377 of them tests

**Narration**
> Seven modules, just over a thousand lines, more than a third of it tests. A contract every
> provider has to satisfy. A fake adapter with no network, that every test runs against. The real
> Groq adapter. The one-door client. A loader for which model serves which tier. And a script that
> makes one real call and refuses to run without a price table.

---

### B05 · PROOF — tests that encode a rule
Custom scene — **needs building** · ~28s

**On screen**
- `56 passing · 32 added this sprint · 0.4s · no network, no API key` stamps in
- Three test names surface as one-line rules, not code: a failed call still gets recorded · an
  unpriceable model gets refused before it's called · a response with no token counts raises
  rather than pricing at zero
- Closes on the one test that failed on purpose mid-sprint, and why that's a good sign

**Narration**
> Fifty-six tests pass, thirty-two of them new this sprint, and the whole suite runs in under half
> a second with no network and no API key — the real provider is tested through a stub that mimics
> its response shape. A few of those tests encode a rule directly: a failed call still gets
> recorded, not just a successful one. An unpriceable model gets refused before it's ever called.
> A response with no token counts raises an error instead of silently pricing itself at zero. One
> test even failed on purpose, mid-sprint — a stale assumption the tier ladder had outgrown — and
> that's the suite doing its job: a config change that should break a test, did.

---

### B06 · REASONING — what the repo actually evidenced
Custom scene — **needs building** · ~18s

**On screen**
- "No PM or billing access" stated plainly
- One evidence trail highlighted: a script referencing a real Groq credential, and a blocked-batch
  log line naming the fix — "upgrade the tier"
- Other providers labeled, muted: *configured, never evidenced*

**Narration**
> Which models go in which tier wasn't obvious, because nobody could get PM or billing access this
> sprint — so it was decided by reading the code instead. Only one provider had real evidence of
> use: a single free Groq account, referenced by name in one script, and named directly in a
> blocked batch log with the fix suggested right there — upgrade the tier. Every other provider in
> the repo was only ever configured, never evidenced.

---

### B07 · REASONING — the pricing pivot
Custom scene — **needs building** · ~21s

**On screen**
- The evidenced models' price tags read "Contact Sales" — a dead end, shown as a hard stop
- Three substitute models land instead, priced, on the same Groq key: cheap / mid / strong table

**Narration**
> But the exact models the log showed in use don't publish a price — Groq lists them as contact
> sales. And the pricing rule refuses to run a model it can't honestly cost. So the gateway swapped
> to three priced models on that same Groq key instead — trading repo-evidenced status for a
> defensible cost number, because without one, two entire sprints later in this project have no
> headline result to report.

---

### B08 · REASONING — why the spread matters
Custom scene — **needs building** · ~19s

**On screen**
- The break-even math lands as two plain thresholds: cheap-vs-mid needs >50%, cheap-vs-strong needs
  >11%
- A muted, struck-through note: the old free-tier setup priced one option at $0 — a comparison with
  no floor

**Narration**
> That substitution set the spread between tiers: about one to two between cheap and mid, and
> roughly one to nine between cheap and strong. Which matters, because the whole point of routing
> is only worth it if the cheap tier clears a bar — better than half the time against mid, better
> than about one time in nine against strong. The old setup, with a free tier priced at zero, would
> have made that comparison meaningless from the start.

---

### B09 · RESULTS — the live calls
Custom scene — **needs building** · ~15s

**On screen**
- Three call rows land: setup, tokens in/out, cost, latency, outcome — including the one that hit
  an invalid key on purpose
- A hand-recomputed cost line draws beside the logged figure and lands on **MATCHES**

**Narration**
> Three real calls went out on the cheap tier, each one cleared by a typed confirmation first. And
> the cost was checked by hand, independently of what got logged — input tokens times their rate,
> output tokens times theirs, added up — and it matched the logged figure exactly, to the
> ten-thousandth of a cent.

---

### B10 · FINDINGS 1–2 — cost and latency
Custom scene — **needs building** · ~24s

**On screen**
- Finding 1: a one-word answer ("ok") breaks down as mostly reasoning-token cost, shown as a
  lopsided cost bar
- Finding 2: identical prompt, two runs — 1,126ms then 382ms, roughly 3× — a cold-start marker
  between them

**Narration**
> Two things showed up that weren't expected. First: one call spent most of its cost on a single
> word — "ok" — because this model reasons before it answers, and the reasoning gets billed like
> the answer does. On short tasks, that overhead doesn't shrink, so the real cost gap between tiers
> may be much smaller than the sticker price suggests. Second: the very same call, run twice, took
> three times as long the first time — a cold start. A speed baseline that doesn't account for that
> isn't measuring the same thing twice.

---

### B11 · FINDINGS 3–4 — the escalation trap and the empty "ok"
Custom scene — **needs building** · ~25s

**On screen**
- Finding 3: all three tiers point at one shared key — a failure icon fans out identically to all
  three, not escalating past it
- Finding 4: a response card reading `outcome: ok` sits beside an empty content field — succeeded,
  said nothing

**Narration**
> Third: all three tiers currently share one API key. A bad key doesn't fail on one tier — it fails
> on all of them the same way, which means escalating from a failed call to a more expensive one
> wouldn't help; it would just spend twice for the identical failure. Fourth, and the strangest one:
> one call came back marked "ok" with an empty answer — because the model hit its token limit
> before it said anything. The call succeeded. The answer was worth nothing. Money was spent either
> way.

---

### B12 · RISK — single point of failure
Custom scene — **needs building** · ~14s

**On screen**
- All three tiers converge on one provider, one key — drawn as one shared choke point, not three
  independent paths
- A muted note: this has already blocked a production batch once

**Narration**
> Which points at the sprint's one real risk carried forward: every tier still runs through a
> single provider and a single key. Groq's free tier has already blocked a production batch once.
> Whatever comes after this sprint needs to run at real volume without hitting that same wall
> again.

---

### B13 · VERDICT — what shipped, what's proven, what's next
`ClaudeVerdictArtifact` · ~18s

**On screen**
- Artifact page, lines stagger in

```
title:    One Door In
heading:  What shipped, and what's still open
lines:
  · Delivered: one-door client, 3-tier gateway, 56 passing tests, 3 hand-verified live calls.
  · Proven: no caller can make an unlogged call — even failures write a row.
  · NOT yet done: mid and strong tiers live-checked the same way; a real task corpus to route against.
```

**Narration**
> So: the gateway works, the door only opens with a logged record on the other side, and it's been
> proven against fifty-six tests and three real dollars-and-cents calls. What's not yet done: the
> mid and strong tiers haven't been live-checked the same way the cheap tier has, and there's still
> no real task corpus to route against. That's next.

---

### B14 · NEXT STEPS — handoff
`ClaudeComposerAsk`, greeting `Your turn.` · ~15s

**On screen**
- Composer, empty, greeting `Your turn.`
- The prompt types in as it's read aloud

```
command: "If you're wiring up more than one provider or more than one tier of
          anything — is there a single door every call has to pass through, and
          does that door log the failure case as carefully as it logs the success?"
```

**Narration**
> Your turn. If you're wiring up more than one provider or more than one tier of anything, ask
> this: is there a single door every call has to pass through — and does that door log the failure
> case as carefully as it logs the success?

---

### B15 · OUTRO
`ClaudeTitleOutro` · ~5s

**On screen**
- Poster serif title, terracotta period · handle beneath

```
title:    One Door In
handle:   @HumanitariansAI
subline:  no unlogged calls · Mycroft
```

**Narration**
> The gateway with one door in. Simba, for Humanitarians AI.

---

## Build notes

**GATE L not yet run.** This is the script-writing pass only — no scene search or component
authoring has happened yet. Every non-house beat below is marked "Custom scene — needs building"
rather than given a pattern name; that search and the actual authoring happens at build time, same
as it did for Sprint 1.

**Renderable today** (no new component needed, once build starts) — B00, B14 →
`ClaudeComposerAsk` · B13 → `ClaudeVerdictArtifact` · B15 → `ClaudeTitleOutro`. B01 is a one-line
spark card and should be cheap regardless of exact pattern chosen. B09's live-call table and B07's
tier-price table are close cousins of `ResultsTable` (built for Sprint 1) and may be reusable with
new props rather than fully new components — worth checking at GATE L before authoring from
scratch.

**ASK→RESULT LAW — applied selectively, same judgment call as Sprint 1.** Applying the literal
ask-before-every-generated-visual rule here would mean an ask-beat before all eleven illustration
beats (B02–B12), which would roughly double the reel's length for content that is a sprint report,
not a live build session. Kept the ask→result pattern at the two places it's structurally
load-bearing — the cold open, which frames the whole video as an answer to a question, and the
handoff, which is the viewer's own ask — and let the middle run as a straight vox-style illustrated
report. Worth a second opinion before build.

**No 9:16 cut drafted.** Wasn't asked for this time. If a Short gets made, THE SHORTS LAW applies
the same way it did for Sprint 1: single cycle, no revision, probably B00 → B01 → B09 (the live
calls) → B13 (verdict) → B15, since the live-call table is the one moment with a real "wait, what"
in it and the verdict already carries the open items.

**Duration.** The estimates above are arithmetic (word count ÷ Kokoro's measured rate), not
measurement — same caveat as every script before this one. Generate audio first and let it set the
real clock.

---

## Sources

- The Sprint 2 report as pasted directly into this session by the Mycroft team — a first-party
  account of a completed sprint, not a third-party claim requiring independent verification.
  DOUBLE-CHECK LAW is honored here by preserving the report's own carried-forward caveats rather
  than trimming them for a cleaner story: the mid and strong tiers being un-gated, the Groq console
  not yet visually confirmed, and the single-provider risk are all in the script (B13, B12) exactly
  as the source flagged them, not softened or omitted.
- All figures — 56/32 tests, 1,015 lines, the 3 live-call table, the hand-verified cost match, the
  tier price table — are quoted or closely paraphrased from that report; nothing is rounded past
  what it states or invented to fill a beat.
