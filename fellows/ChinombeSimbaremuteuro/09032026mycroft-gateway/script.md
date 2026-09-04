# One Door In — script (final, as shot)

Channel claude-hai · Persona Simba · Register Pragmatist · Voice Kokoro `af_bella`
16:9 long cut: 5:58 (357.8s) · 9:16 Shorts: 0:56 (56.1s)

Timestamps and durations are Kokoro-measured from the locked audio, not estimates — this is exactly what's spoken in the final render. Pre-production shot notes, on-screen prop text, and build rationale live in `SCRIPT-mycroft-gateway.md`; this file is narration only, dated to the finished cuts.

## 16:9 — long cut

### B00 · INTRO (0:00–0:21)
> Hi, I am Simba, and this video is about the second Mycroft sprint — the one that built a single gateway all three model tiers have to go through. Cost and latency now get logged automatically on every call, with no way for a caller to skip it. This sprint also spent its first real money — three live calls, a fraction of a cent, checked by hand.

### B01 · SUMMARY (0:21–0:36)
> The rule this sprint enforced: a caller must not be able to make an unlogged call. If logging happened after a response came back, someone would eventually forget — and a missing row wouldn't look like an error. It would look like a cheaper month.

### B02 · STRUCTURE (0:36–0:52)
> So there's exactly one public door in: GatewayClient dot call. It wraps the model adapter and the logbook together, and it writes a row before it returns — even when the provider fails. You can't get a response out of this gateway without a record of what it cost.

### B03 · STRUCTURE (0:52–1:18)
> Underneath, the work is split into layers that each do one job. The adapter makes the call and reports tokens and latency — nothing else. The client prices, times, and records. The router, coming next sprint, only chooses a tier — no network access at all. If adapters logged their own calls, every new provider would be a chance to log slightly differently, and a later sprint's baseline needs every row shaped exactly the same.

### B04 · PROOF (1:18–1:40)
> Seven modules, just over a thousand lines, more than a third of it tests. A contract every provider has to satisfy. A fake adapter with no network, that every test runs against. The real Groq adapter. The one-door client. A loader for which model serves which tier. And a script that makes one real call and refuses to run without a price table.

### B05 · PROOF (1:40–2:22)
> Fifty-six tests pass, thirty-two of them new this sprint, and the whole suite runs in under half a second with no network and no API key — the real provider is tested through a stub that mimics its response shape. A few of those tests encode a rule directly: a failed call still gets recorded, not just a successful one. An unpriceable model gets refused before it's ever called. A response with no token counts raises an error instead of silently pricing itself at zero. One test even failed on purpose, mid-sprint — a stale assumption the tier ladder had outgrown — and that's the suite doing its job: a config change that should break a test, did.

### B06 · REASONING (2:22–2:48)
> Which models go in which tier wasn't obvious, because nobody could get PM or billing access this sprint — so it was decided by reading the code instead. Only one provider had real evidence of use: a single free Groq account, referenced by name in one script, and named directly in a blocked batch log with the fix suggested right there — upgrade the tier. Every other provider in the repo was only ever configured, never evidenced.

### B07 · REASONING (2:48–3:13)
> But the exact models the log showed in use don't publish a price — Groq lists them as contact sales. And the pricing rule refuses to run a model it can't honestly cost. So the gateway swapped to three priced models on that same Groq key instead — trading repo-evidenced status for a defensible cost number, because without one, two entire sprints later in this project have no headline result to report.

### B08 · REASONING (3:13–3:37)
> That substitution set the spread between tiers: about one to two between cheap and mid, and roughly one to nine between cheap and strong. Which matters, because the whole point of routing is only worth it if the cheap tier clears a bar — better than half the time against mid, better than about one time in nine against strong. The old setup, with a free tier priced at zero, would have made that comparison meaningless from the start.

### B09 · RESULTS (3:37–3:56)
> Three real calls went out on the cheap tier, each one cleared by a typed confirmation first. And the cost was checked by hand, independently of what got logged — input tokens times their rate, output tokens times theirs, added up — and it matched the logged figure exactly, to the ten-thousandth of a cent.

### B10 · FINDINGS (3:56–4:29)
> Two things showed up that weren't expected. First: one call spent most of its cost on a single word — "ok" — because this model reasons before it answers, and the reasoning gets billed like the answer does. On short tasks, that overhead doesn't shrink, so the real cost gap between tiers may be much smaller than the sticker price suggests. Second: the very same call, run twice, took three times as long the first time — a cold start. A speed baseline that doesn't account for that isn't measuring the same thing twice.

### B11 · FINDINGS (4:29–5:01)
> Third: all three tiers currently share one API key. A bad key doesn't fail on one tier — it fails on all of them the same way, which means escalating from a failed call to a more expensive one wouldn't help; it would just spend twice for the identical failure. Fourth, and the strangest one: one call came back marked "ok" with an empty answer — because the model hit its token limit before it said anything. The call succeeded. The answer was worth nothing. Money was spent either way.

### B12 · RISK (5:01–5:18)
> Which points at the sprint's one real risk carried forward: every tier still runs through a single provider and a single key. Groq's free tier has already blocked a production batch once. Whatever comes after this sprint needs to run at real volume without hitting that same wall again.

### B13 · SUMMARY (5:18–5:39)
> So: the gateway works, the door only opens with a logged record on the other side, and it's been proven against fifty-six tests and three real dollars-and-cents calls. What's not yet done: the mid and strong tiers haven't been live-checked the same way the cheap tier has, and there's still no real task corpus to route against. That's next.

### B14 · NEXT STEPS (5:39–5:53)
> Your turn. If you're wiring up more than one provider or more than one tier of anything, ask this: is there a single door every call has to pass through — and does that door log the failure case as carefully as it logs the success?

### B15 · OUTRO (5:53–5:58)
> The gateway with one door in. Simba, for Humanitarians AI.

## 9:16 — Shorts cut

### B00 · INTRO (0:00–0:14)
> Hi, I am Simba. This sprint built one gateway all three model tiers go through — cost and latency logged automatically, no way to skip it. And it spent its first real money: three live calls, checked by hand.

### B01 · SUMMARY (0:14–0:23)
> The rule this sprint enforced: a caller must not be able to make an unlogged call. A missing row wouldn't look like an error. It would look like a cheaper month.

### B02 · RESULTS (0:23–0:38)
> Three real calls went out, each one cleared by hand first. Cost was checked independently of the log — input tokens times their rate, output tokens times theirs — and it matched the logged figure exactly, to the ten-thousandth of a cent.

### B03 · SUMMARY (0:38–0:50)
> The gateway works. No caller can make an unlogged call — even failures write a row. Not yet done: the mid and strong tiers haven't been live-checked the same way. That's next.

### B04 · OUTRO (0:50–0:56)
> Full build, with all fifty-six tests, is on the channel. Simba, for Humanitarians AI.

---

Every figure in this script is the source sprint report's own (first-party, not independently fact-checked against an outside source). DOUBLE-CHECK LAW is honored by preserving every carried-forward caveat (the mid/strong tiers not yet live-checked, the single-provider risk, the reasoning-overhead and cold-start findings) rather than trimming them for a cleaner story.
