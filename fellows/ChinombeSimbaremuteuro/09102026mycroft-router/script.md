# One File, No Contradictions — script (final, as shot)

Channel claude-hai · Persona Simba · Register Pragmatist · Voice Kokoro `af_bella`
Sprint: Mycroft Sprint 3
16:9 long cut: 6:12 (372.45s) · 9:16 Shorts: 0:58 (58.07s)

Timestamps and durations are Kokoro-measured from the locked audio, not estimates — this is exactly what's spoken in the final render. Pre-production shot notes, on-screen prop text, and build rationale live in `SCRIPT-mycroft-router.md`; this file is narration only, dated to the finished cuts.

## 16:9 — long cut

### B00 · INTRO (0:00–0:22)
> Hi, I am Simba, and this one's about the third Mycroft sprint — the router that decides, for every request Mycroft gets, whether a cheap model can handle it or whether it needs something stronger. Six kinds of task, three cost tiers, and one rule I wanted to hold myself to: nothing about how one task type is routed should be able to quietly contradict how another one is.

### B01 · SUMMARY (0:22–0:37)
> The rule: task types and their routing rules live in exactly one file. Not scattered across the router, the prompts, and someone's memory of what was decided last sprint — one file, so two rules can never quietly disagree.

### B02 · STRUCTURE (0:37–1:08)
> policy dot json locks all six task types — sentiment, topic, structured extraction, contradiction detection, summarization, and a RAG answer. For each one it records the answer format, the allowed labels, the check used to grade it, which tier it starts on, which tier it escalates to, and the input length that triggers that promotion. Each type points at a real file in the repo that proves Mycroft actually does that kind of work — and if that file ever disappears, a test catches it.

### B03 · STRUCTURE (1:08–1:49)
> The router itself is a pure function — no network call, no clock, no model involved in deciding. It refuses anything pinned or unrecognized. Otherwise, every request starts on the tier its policy says, and gets promoted one tier if the input is long — measured in characters, not tokens, because token counts depend on which model you'd even be asking. Every decision comes back with a one-sentence reason attached. One thing is deliberately missing: a break-even rule that would route on cost-versus-accuracy tradeoffs instead of just length. That's being left for later, on purpose — it's the clever version, and clever wasn't the goal this sprint.

### B04 · WHAT WAS BUILT (1:49–2:20)
> The bench folder holds three tools. fixtures dot py checks the fixtures and freezes them. audit dot py reports how much of the policy they actually cover. label dot py is what I used to label them by hand. Twenty-four fixtures in total — four per task type, two easy and two hard — all built around fictional companies. They got frozen on September tenth, with a fingerprint of every file, so if anyone edits one later without meaning to, a test catches that too.

### B05 · DECISIONS (2:20–2:49)
> Worth saying plainly: these fixtures are synthetic, not real. There's no real request data in this repo right now — two hundred three of two hundred seventeen script samples are placeholders, the one dataset that looks like sample data literally declares itself fake, and the Klarna mock data file is empty. So these results can tell you something about how models handle these kinds of tasks. They can't yet tell you what Mycroft's real traffic actually looks like.

### B06 · DECISIONS (2:49–3:09)
> The expected tier on each fixture is my own judgment — the cheapest tier I'd actually trust to get that answer right. I labeled every fixture before any model touched it, and the labeling tool never shows what the router would have picked. That ordering matters — it's the only way the comparison that's coming isn't just me agreeing with myself.

### B07 · RESULTS (3:09–3:33)
> Here's what it showed. My labels put six fixtures on cheap, eleven on mid, seven on strong. The router put eight on cheap, sixteen on mid, and zero — not one — on strong. Out of twenty-four fixtures, the router agreed with me on nine. And I want to be careful about that number: these are predictions being checked against a human's judgment. It isn't a measurement of real performance yet.

### B08 · FINDINGS (3:33–4:05)
> That zero isn't a coincidence — it's structural. The simple router has exactly two ways to reach the strong tier: a long input, or an escalation. There's no path from a short input straight to strong. And every single fixture I labeled as strong is a short input with a trap in it — a sentence that reads simply but needs real reasoning to get right. As written, the router literally cannot agree with me on any of those seven. That's not a bug to patch quietly — it's the main gap this design has right now.

### B09 · FINDINGS (4:05–4:28)
> Here's the risk underneath all of this. The free checks catch answers in the wrong format — not answers that are simply wrong. A model that completely misreads sarcasm can still return a label the policy allows, the check passes, and nothing escalates. The router has no way to know the answer was bad if it was shaped correctly. That's the main design risk heading into the next two sprints.

### B10 · FINDINGS (4:28–4:51)
> A couple of fixtures exist specifically to test the checks, not the models. In summ dash zero-zero-four, a genuinely correct unit conversion fails the check anyway. In extract dash zero-zero-four, a flatly made-up answer passes it. Both are there on purpose — they're the honest edge cases the grading logic itself needs to survive.

### B11 · PROBLEMS (4:51–5:29)
> Two problems got fixed along the way. The labeling tool originally didn't show what each task was actually asking, so it now prints the task itself before every label, and I added a way to redo specific ones. And my very first labeling pass put everything on the cheap tier — so I relabeled those ten using the same two questions every time: is there a trap, and is there a reasoning step? Two more problems got found but not fixed here — someone else's merge on August thirtieth deleted two entries from the run log, and the repo's conformance check can't find Python on Windows. Both are flagged as their own separate tasks.

### B12 · SUMMARY (5:29–5:54)
> So: one file that can't disagree with itself, a router with no hidden state, and twenty-four fixtures frozen so nobody can quietly change the answer key. It agrees with human judgment on nine of twenty-four — a starting point, not a benchmark. What's not yet done: escalation only looks at length, the free checks only catch format, and every fixture behind these numbers is still synthetic, not real traffic.

### B13 · NEXT STEPS (5:54–6:07)
> Your turn. If you're routing requests across cost tiers of your own: does your cheap check only catch the wrong shape of answer — or would it actually catch a confidently wrong answer that happens to come back in the right shape?

### B14 · OUTRO (6:07–6:12)
> One file, no contradictions. Simba, for Humanitarians AI.

## 9:16 — Shorts cut

### B00 · INTRO (0:00–0:13)
> Hi, I am Simba. Six kinds of request, three cost tiers — how do you route them without one task type's rules quietly contradicting another's? One locked policy file, and a pure router function that never guesses.

### B01 · SUMMARY (0:13–0:21)
> The rule: task types and their routing rules live in exactly one file. So two rules can never quietly disagree.

### B02 · RESULTS (0:21–0:36)
> Here's what it showed. My labels put six fixtures on cheap, eleven on mid, seven on strong. The router put eight on cheap, sixteen on mid, and zero on strong. Nine of twenty-four agree — and that's a prediction, not a measurement yet.

### B03 · SUMMARY (0:36–0:52)
> One file that can't disagree with itself, and a router that agrees with human judgment on nine of twenty-four — a starting point, not a benchmark. Not yet done: escalation only looks at length, and the checks only catch the wrong format, not a wrong answer.

### B04 · OUTRO (0:52–0:58)
> Full build, with the design risks, is on the channel. Simba, for Humanitarians AI.

---

This script covers the Mycroft Sprint 3 router/policy report as pasted directly into this session — every figure (6/11/7 vs. 8/16/0, 9 of 24, 24 fixtures, the placeholder/fake-dataset counts, the two fixed problems, the two flagged-not-fixed problems) is drawn from that report, not invented for the video. B02's on-screen card notes are deliberately generic ("format · labels · check · tier · length") rather than per-task-type values, because the source report gave the aggregate tier counts but never each task type's individual tier assignment — see `SCRIPT-mycroft-router.md`'s build notes and `process-notes.md` for the self-check that caught this before it shipped.
