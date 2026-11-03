# One Retry, Never a Chain — script (final, as shot)

Channel claude-hai · Persona Simba · Register Pragmatist · Voice Kokoro `af_bella`
16:9 long cut: 5:31 (330.8s) · 9:16 Shorts: 0:49 (49.3s)

Timestamps and durations are Kokoro-measured from the locked audio, not estimates — this is exactly what's spoken in the final render. Pre-production shot notes, on-screen prop text, and build rationale live in `SCRIPT-mycroft-retry.md`; this file is narration only, dated to the finished cuts.

## 16:9 — long cut

### B00 · INTRO (0:00–0:19)
> Hi, I am Simba, and this one's the fourth Mycroft sprint — the one where the router finally gets to retry. One retry, ever, on the tier above — and the real question I built this sprint to answer: can a wrong answer in the right shape still slip through, with nothing catching it and no retry helping?

### B01 · SUMMARY (0:19–0:32)
> The rule: retry happens exactly once, on the escalation tier, triggered by a free check failing. There's no retry loop in the code — so a chain of retries isn't just discouraged, it's structurally impossible.

### B02 · STRUCTURE (0:32–0:55)
> validators.py holds five checks, one per task type: the answer is an allowed label, the JSON has its required keys, a contradiction verdict actually quotes the input, a summary's numbers all appear in the input, and a RAG answer cites a passage. Two more checks run on everything, no matter the task: the answer isn't empty, and it isn't cut off.

### B03 · STRUCTURE (0:55–1:27)
> gateway.py is the whole path: route to a tier, call the model, run the check, and if it fails, retry exactly once — on the tier above. That's the entire retry logic. No loop exists to walk back down or try a third time. And the adapters changed too: every failure now reports whether retrying could actually help. A bad API key, an unknown model, or a request that's simply too large are terminal — the gateway never retries those, because no retry fixes them.

### B04 · WHAT WAS BUILT (1:27–1:42)
> bench/run.py runs every frozen fixture through the whole path and grades each answer against your key, writing both a log and a results file. Tests went from ninety-six to a hundred forty-six over the sprint.

### B05 · RESULTS (1:42–2:07)
> Final sweep, twenty-four fixtures: twenty-four requests became twenty-six attempts. Escalation happened on eight percent — two fixtures. Failure: zero percent. Total cost: zero point zero zero two five zero dollars, about a hundredth of a cent per request. Latency: three ninety-three milliseconds at the median, seven thirty-four at the ninety-fifth percentile. Of the twenty-four, sixteen were graded — fourteen correct.

### B06 · FINDINGS (2:07–2:46)
> This sprint was built around one worry: a model returning a wrong answer in the right shape, where no free check catches it and no retry helps. Across twenty-four fixtures, including every deliberate trap — that happened zero times. The two flagged fixtures turned out to be your answer key, not the model: sent-001 and sent-004 are keyed negative, both models answered positive, and the models are right. The cheap twenty-b model even got sent-004 correct — the exact headline where the negative words belong to a rival company, the same trap that once reached a finished brief.

### B07 · PROBLEMS (2:46–3:24)
> Two things broke early. My quote check was too strict — all three first-sweep escalations were false alarms, because the models quoted both conflicting statements joined together, a reasonable answer the check rejected for wanting one contiguous span. Fixing the prompt dropped escalation from eleven percent to eight. And the strong tier's model just disappeared: qwen/qwen3.6-27b started returning 404 a week after working fine — Groq's own deprecation page still recommends it. Replaced with qwen3.8-27b.

### B08 · PROBLEMS (3:24–3:58)
> The replacement model was then refused on every call — its 1,024-token budget exceeded the account's cap of 1,000 output tokens per minute. Lowered to 896, and it worked. And the summary itself was wrong once: a smoke run and the full sweep shared one dated log file, double-counting three requests — twenty-seven instead of twenty-four. Log files are now stamped to the second. One more thing broke on purpose: a test that hardcoded 1,024 broke the moment the budget changed — correctly.

### B09 · FINDINGS (3:58–4:22)
> Two numbers are worth keeping. First: escalated requests cost three point two times a normal one — zero point zero zero zero two eight two dollars against zero point zero zero zero zero eight eight. Two of twenty-four requests took twenty-three percent of the spend. Retrying is cheap in absolute terms and expensive in relative terms — which is exactly why the trigger has to be right.

### B10 · FINDINGS (4:22–4:49)
> Second: the cost ladder isn't monotonic. On the gate prompt, the strong tier cost twenty percent less than the cheap tier — despite a thirteen-times higher sticker price on output. Cheap spent seventy-seven tokens thinking; strong answered in two. The crossover sits around five output tokens, so on real work, strong is far more expensive. What it proves is narrower, and still useful: sticker ratio and real ratio can point in opposite directions.

### B11 · SUMMARY (4:49–5:16)
> So: one retry, on the tier above, and no loop for it to become a chain. Zero failures across twenty-four fixtures, including every deliberate trap — the two flags this sprint found were a wrong answer key, not a wrong model. And two numbers worth carrying forward: an escalation costs three times a normal request, and the sticker price doesn't predict the real one. Both the retry trigger and the tier choice need real numbers, not list prices.

### B12 · NEXT STEPS (5:16–5:26)
> Your turn. If you're pricing tiers by sticker rate alone — have you actually checked where your own cost ladder crosses over? It might not be where the price list says.

### B13 · OUTRO (5:26–5:31)
> One retry, never a chain. Simba, for Humanitarians AI.

## 9:16 — Shorts cut

### B00 · INTRO (0:00–0:11)
> Hi, I am Simba. Mycroft's router can now retry — exactly once, on the tier above, if a free check fails. No loop exists, so a chain of retries can't happen.

### B01 · SUMMARY (0:11–0:18)
> Retry happens exactly once, triggered by a free check failing — there's no retry loop in the code for it to become a chain.

### B02 · RESULTS (0:18–0:30)
> Across twenty-four fixtures, including every deliberate trap: zero percent failure, eight percent escalation. The two flags that did show up turned out to be the answer key, not the model.

### B03 · SUMMARY (0:30–0:43)
> One retry, never a chain, and zero failures across every deliberate trap. What's still worth watching: an escalation costs three times a normal request, and sticker price doesn't predict the real one.

### B04 · OUTRO (0:43–0:49)
> Full build, with the cost findings, is on the channel. Simba, for Humanitarians AI.

---

This script covers the Mycroft Sprint 4 report ("Handle Failures") as pasted directly into the session. Every figure — the 96→146 test count, the 24-fixture final sweep (24/26 requests, 8% escalation, 0% failure, $0.00250 total cost, p50 393ms / p95 734ms latency, 16/24 graded with 14 correct), the sent-001/sent-004 answer-key correction, the five problems hit and fixed, and the two cost findings (3.2× escalation premium, the non-monotonic gate-prompt cost ladder) — is drawn from that report, per `SCRIPT-mycroft-retry.md`'s Sources. Nothing was estimated or invented.
