# The Logbook Before the Router — script (final, as shot)

Channel claude-hai · Persona Simba · Register Pragmatist · Voice Kokoro `af_bella`
16:9 long cut: 3:44 (223.6s) · 9:16 Shorts: 0:51 (51.4s)

Timestamps and durations are Kokoro-measured from the locked audio, not estimates — this is exactly what's spoken in the final render. Pre-production shot notes, on-screen prop text, and build rationale live in `SCRIPT-mycroft-logbook.md`; this file is narration only, dated to the finished cuts.

## 16:9 — long cut

### B00 · INTRO (0:00–0:12)
> Hi, I am Simba, and this video is about the Mycroft logbook — the record every AI request leaves behind, and why we built it before we built anything that acts on it. Here's the whole idea.

### B01 · SUMMARY (0:12–0:29)
> Mycroft sends every AI request to whichever model a project happened to pick — no record of what that cost, how long it took, or whether it was even the right call. This sprint didn't fix that. It built the logbook: the thing that has to exist before any fix can be measured.

### B02 · PROBLEM (0:29–0:47)
> Right now, easy requests can land on expensive models they never needed. Hard requests sometimes land on a cheap model and come back fluent but wrong. And nothing writes any of that down. You can't fix a routing problem you can't see — and today, Mycroft can't see it at all.

### B03 · REASONING (0:47–1:11)
> So why build the record before the router? Two reasons. Every number this project will ever report comes out of this logbook — change its format later, and you can't compare before to after, which is exactly the comparison October's decision depends on. And the logbook ships no matter what October decides — even if the simple version wins, Mycroft still ends up able to answer: which model produced this claim.

### B04 · STRUCTURE (1:11–1:29)
> Every request now produces one record: which model answered, which rule sent it there, what it cost, how long it took, whether it retried and why, and a quality score. Four version stamps ride along too, so a run from one week can be told apart from a run three weeks later.

### B05 · STRUCTURE (1:29–1:47)
> Every record lands in two places: a plain text log, written first, then a database for querying, written second. Crash between the two, and the text log still has it — the database rebuilds from that. Reverse the order, and a crash loses the record outright. The order isn't a style choice.

### B06 · STRUCTURE (1:47–2:01)
> On top of the raw records, three summaries exist specifically for October: cost per task type, retry rate per task type, and which requests are slowest. This is the shape of the decision — not the answer to it yet.

### B07 · PROOF (2:01–2:24)
> Two of the sixteen tests exist because measurement quietly lies. Money is stored as exact decimals, not approximations — hundreds of small costs adding up in floating-point drift right past a percentage threshold. And a retried request counts as one request costing both attempts — counted the obvious way, retries make average cost look lower, which is backwards.

### B08 · PROOF (2:24–2:41)
> The other two guard the record itself. A retried record can't be created without saying which model it escalated from — a record that can't explain why the model changed isn't a record of anything. And writing the same request twice never creates a duplicate row.

### B09 · RESULTS (2:41–3:05)
> A short trial run — made-up figures, checking the arithmetic rather than measuring anything real: one retried, hard request cost roughly two hundred sixty times a simple lookup. If Mycroft's real traffic is mostly lookups sent to expensive models, the savings are large. If it's mostly the hard kind, they aren't. Nobody knows which yet — that's what the next five sprints answer.

### B10 · SUMMARY (3:05–3:26)
> So: the logbook works, and it's tested. What shipped is the record format, the log writer, the database and query layer, three summary functions, sixteen passing tests, and a README. What it proves is that the measurement is correct — not that anything real has been measured yet. That's the honest line, and it's the whole point of building in this order.

### B11 · NEXT STEPS (3:26–3:39)
> Your turn. Pick something you run that currently explains nothing about itself, and ask that. The dual-write question — what goes first — is the one that'll teach you the most, because it's the one that's easy to get backwards.

### B12 · OUTRO (3:39–3:44)
> The logbook before the router. Simba, for Humanitarians AI.

## 9:16 — Shorts cut

### B00 · INTRO (0:00–0:10)
> Hi, I am Simba, and this video is about the Mycroft logbook — the record every AI request leaves behind, built before the router that would act on it.

### B01 · SUMMARY (0:10–0:20)
> Mycroft can't fix how it routes AI requests until it can measure it — and a measurement nobody trusts is worse than none. This sprint built the measuring, not the fix.

### B02 · RESULTS (0:20–0:35)
> A trial run, made-up figures, checking the arithmetic rather than measuring anything real: one retried, hard request cost roughly two hundred sixty times a simple lookup. Real traffic mix? Nobody knows yet.

### B03 · SUMMARY (0:35–0:46)
> The logbook works, and it's tested — sixteen passing tests. It proves the measurement is correct. It does not prove anything real has been measured yet. That's the honest line.

### B04 · OUTRO (0:46–0:51)
> Full build, with all sixteen tests, is on the channel. Simba, for Humanitarians AI.

---

Every figure in this script is the source sprint report's own (first-party, not independently fact-checked against an outside source). DOUBLE-CHECK LAW is honored by preserving the results-table caveat verbatim (B09 / Shorts B02) rather than softening or removing it.
