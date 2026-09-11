# One File, No Contradictions — script

**Format** `ai-explainer` (16:9) · **Channel** claude-hai · **Register** Pragmatist
**Persona** Simba · **Voice** Kokoro `af_bella` · **Slug** `hai-mycroft-router`
**Sprint** Mycroft Sprint 3
**Runtime** ~4:15 (14 beats, estimated at Kokoro's measured ~3.6 words/sec — audio generation sets the real clock)

---

## The one idea

> Every task type's answer format, allowed labels, starting tier, and escalation rule live in
> exactly one file — so they can never disagree with each other. A pure router function reads
> that file and nothing else: no model, no clock, no network. Tested blind against 24 frozen,
> hand-labeled fixtures, it agrees with human judgment on 9 of 24 — and it structurally cannot
> reach the strong tier from a short input, which is exactly where every one of the human's
> "strong" labels lives.

**Every figure in this script is the sprint's own** — the 6 task types, the 24 fixtures, the 9-of-24
agreement, the 512/512/1,024 token budgets — and the caveats it carried forward on purpose (synthetic
fixtures, not real traffic; free checks that catch format, not correctness) are kept in, not
smoothed over.

---

## Beat sheet

### B00 · INTRO — cold open
`ClaudeComposerAsk` · ~17s

**On screen**
- Greeting types in: `Hi, Simba` · terracotta spark
- Composer holds the ask, send button arms
- `locking the policy…` then output lines land — the ask arrives already answered

```
topic:    MYCROFT · ROUTING WITHOUT CONTRADICTIONS
segment:  One File, No Contradictions
command:  "Six different kinds of request, three cost tiers — how do you decide
           which goes where, without the rules for one task type quietly
           disagreeing with the rules for another?"
output:   → one locked file: format, labels, tier, and escalation rule per task
          → one pure router function — no model, no clock, no guessing
          → tested blind against 24 fixtures: 9 of 24 agree with a human
folder:   @HumanitariansAI
```

**Narration**
> Hi, I am Simba, and this one's about the third Mycroft sprint — the router that decides, for
> every request Mycroft gets, whether a cheap model can handle it or whether it needs something
> stronger. Six kinds of task, three cost tiers, and one rule I wanted to hold myself to: nothing
> about how one task type is routed should be able to quietly contradict how another one is.

---

### B01 · EXECUTIVE SUMMARY — BLUF
`ClaudeStatement` · ~13s (one breath, mandatory)

**On screen**
- Single sentence sets, terracotta underline settles beneath it

**Narration**
> The rule: task types and their routing rules live in exactly one file. Not scattered across the
> router, the prompts, and someone's memory of what was decided last sprint — one file, so two
> rules can never quietly disagree.

---

### B02 · STRUCTURE — the policy file
Custom scene — **needs building** · ~22s

**On screen**
- `policy.json` + `policy.py` sit as one locked source
- Six task-type cards fan out beneath it: sentiment, topic, structured extraction, contradiction
  detection, summarization, RAG answer
- Each card shows its five locked fields: answer format · allowed labels · check used · starting
  tier · escalation tier + trigger length
- A small footnote: each type points at a real repo file — delete that file, and a test fails

**Narration**
> `policy.json` locks all six task types — sentiment, topic, structured extraction, contradiction
> detection, summarization, and a RAG answer. For each one it records the answer format, the
> allowed labels, the check used to grade it, which tier it starts on, which tier it escalates to,
> and the input length that triggers that promotion. Each type points at a real file in the repo
> that proves Mycroft actually does that kind of work — and if that file ever disappears, a test
> catches it.

---

### B03 · STRUCTURE — the router itself
Custom scene — **needs building** · ~24s

**On screen**
- `router.py` labeled plainly: "pure function — no network, no clock, no model"
- Three refusal/decision paths draw in: pinned task type → refused · unknown task type → refused ·
  known type → starts on its policy tier
- One promotion path: input length (measured in characters) crosses the threshold → tier +1
- A muted, struck-through note: the break-even rule — deliberately left out, "Sprint 8's clever version"

**Narration**
> The router itself is a pure function — no network call, no clock, no model involved in deciding.
> It refuses anything pinned or unrecognized. Otherwise, every request starts on the tier its
> policy says, and gets promoted one tier if the input is long — measured in characters, not
> tokens, because token counts depend on which model you'd even be asking. Every decision comes
> back with a one-sentence reason attached. One thing is deliberately missing: a break-even rule
> that would route on cost-versus-accuracy tradeoffs instead of just length. That's being left for
> later, on purpose — it's the clever version, and clever wasn't the goal this sprint.

---

### B04 · WHAT WAS BUILT — the bench
Custom scene — **needs building** · ~20s

**On screen**
- Three tools land as a compact list: `fixtures.py` — checks and freezes fixtures · `audit.py` —
  reports coverage · `label.py` — the labeling tool
- Beneath: `24 fixtures · 4 per type · 2 easy, 2 hard · fictional companies`
- A frozen stamp: `2026-09-10 · fingerprinted — any later edit fails a test`

**Narration**
> The bench folder holds three tools. `fixtures.py` checks the fixtures and freezes them.
> `audit.py` reports how much of the policy they actually cover. `label.py` is what I used to
> label them by hand. Twenty-four fixtures in total — four per task type, two easy and two hard —
> all built around fictional companies. They got frozen on September tenth, with a fingerprint of
> every file, so if anyone edits one later without meaning to, a test catches that too.

---

### B05 · DECISIONS — the fixtures are synthetic
`ClaudeCallout` or spark-card · ~20s

**On screen**
- Header: `SYNTHETIC, NOT REAL`
- Three evidence lines land: 203 of 217 script samples are placeholders · the one sample dataset in
  `data/raw/` declares itself fake · the Klarna mock data file is empty
- Closing line, terracotta: what this can and can't support

**Narration**
> Worth saying plainly: these fixtures are synthetic, not real. There's no real request data in
> this repo right now — two hundred three of two hundred seventeen script samples are placeholders,
> the one dataset that looks like sample data literally declares itself fake, and the Klarna mock
> data file is empty. So these results can tell you something about how models handle these kinds
> of tasks. They can't yet tell you what Mycroft's real traffic actually looks like.

---

### B06 · DECISIONS — labeling without anchoring
Custom scene — **needs building** · ~16s

**On screen**
- "Expected tier" defined: the cheapest tier you'd trust to get it right
- Two conditions, side by side: labeled *before* any model ran · labeling tool never showed the
  router's own choice

**Narration**
> The expected tier on each fixture is my own judgment — the cheapest tier I'd actually trust to
> get that answer right. I labeled every fixture before any model touched it, and the labeling
> tool never shows what the router would have picked. That ordering matters — it's the only way
> the comparison that's coming isn't just me agreeing with myself.

---

### B07 · RESULTS — the comparison
Custom scene — **needs building** · ~19s

**On screen**
- Table lands: `cheap / mid / strong` across the top, `your labels` and `the router` as rows —
  6/11/7 versus 8/16/0
- Closing stamp: `9 of 24 agree` — labeled clearly as a prediction, not yet a measurement

**Narration**
> Here's what it showed. My labels put six fixtures on cheap, eleven on mid, seven on strong. The
> router put eight on cheap, sixteen on mid, and zero — not one — on strong. Out of twenty-four
> fixtures, the router agreed with me on nine. And I want to be careful about that number: these
> are predictions being checked against a human's judgment. It isn't a measurement of real
> performance yet.

---

### B08 · FINDING — the tier the router can't reach
Custom scene — **needs building** · ~21s

**On screen**
- The router's two paths to strong draw in: a long input, or an escalation — both shown, both
  leading away from "short input"
- A third path — short input, straight to strong — draws in red, then crossed out: *no route exists*
- Beneath: all seven of the human's strong labels sit on short inputs with a trap

**Narration**
> That zero isn't a coincidence — it's structural. The simple router has exactly two ways to reach
> the strong tier: a long input, or an escalation. There's no path from a short input straight to
> strong. And every single fixture I labeled as strong is a short input with a trap in it — a
> sentence that reads simply but needs real reasoning to get right. As written, the router
> literally cannot agree with me on any of those seven. That's not a bug to patch quietly — it's
> the main gap this design has right now.

---

### B09 · FINDING — what the free checks actually catch
Custom scene — **needs building** · ~22s

**On screen**
- A model response card lands, marked "sarcasm misread"
- The check runs against it — green checkmark: *format valid, label allowed*
- Beneath, in terracotta: the check passed. The answer was wrong. Nothing escalated.
- Flag: `main design risk — Sprints 4–5`

**Narration**
> Here's the risk underneath all of this. The free checks catch answers in the wrong format — not
> answers that are simply wrong. A model that completely misreads sarcasm can still return a label
> the policy allows, the check passes, and nothing escalates. The router has no way to know the
> answer was bad if it was shaped correctly. That's the main design risk heading into the next two
> sprints.

---

### B10 · FINDING — fixtures built to break the checks
Custom scene — **needs building** · ~17s

**On screen**
- Two fixture IDs land side by side: `summ-004` and `extract-004`
- summ-004: a correct unit conversion → check result: **FAIL**
- extract-004: a made-up answer → check result: **PASS**

**Narration**
> A couple of fixtures exist specifically to test the checks, not the models. In summ-004, a
> genuinely correct unit conversion fails the check anyway. In extract-004, a flatly made-up answer
> passes it. Both are there on purpose — they're the honest edge cases the grading logic itself
> needs to survive.

---

### B11 · PROBLEMS HIT AND FIXED
Custom scene — **needs building** · ~24s

**On screen**
- Two fixed items stagger in: labeling tool now prints a `TASK:` line, plus `--redo` and `--ids`
  flags · first labeling pass — ten fixtures all landed on cheap, relabeled with two questions
  ("is there a trap? is there a reasoning step?")
- Two flagged-not-fixed items land beneath, muted: an 08-30 merge deleted two run-log entries ·
  the repo's conformance check can't find Python on Windows

**Narration**
> Two problems got fixed along the way. The labeling tool originally didn't show what each task
> was actually asking, so it now prints the task itself before every label, and I added a way to
> redo specific ones. And my very first labeling pass put everything on the cheap tier — so I
> relabeled those ten using the same two questions every time: is there a trap, and is there a
> reasoning step? Two more problems got found but not fixed here — someone else's merge on August
> thirtieth deleted two entries from the run log, and the repo's conformance check can't find
> Python on Windows. Both are flagged as their own separate tasks.

---

### B12 · VERDICT — what's locked, what's not yet proven
`ClaudeVerdictArtifact` · ~19s

**On screen**
- Artifact page, lines stagger in

```
title:    One File, No Contradictions
heading:  What's locked, what's not yet proven
lines:
  · Delivered: one policy file, a pure router, 24 frozen and fingerprinted fixtures.
  · Proven: the router agrees with human judgment on 9 of 24 — a starting point, not a benchmark.
  · NOT yet done: escalation is length-only, checks catch format not correctness, fixtures are synthetic.
```

**Narration**
> So: one file that can't disagree with itself, a router with no hidden state, and twenty-four
> fixtures frozen so nobody can quietly change the answer key. It agrees with human judgment on
> nine of twenty-four — a starting point, not a benchmark. What's not yet done: escalation only
> looks at length, the free checks only catch format, and every fixture behind these numbers is
> still synthetic, not real traffic.

---

### B13 · NEXT STEPS — handoff
`ClaudeComposerAsk`, greeting `Your turn.` · ~16s

**On screen**
- Composer, empty, greeting `Your turn.`
- The prompt types in as it's read aloud

```
command: "If you're routing requests across cost tiers — does your cheap check
          only catch the wrong shape, or would it catch a confidently wrong
          answer in the right shape too?"
```

**Narration**
> Your turn. If you're routing requests across cost tiers of your own: does your cheap check only
> catch the wrong shape of answer — or would it actually catch a confidently wrong answer that
> happens to come back in the right shape?

---

### B14 · OUTRO
`ClaudeTitleOutro` · ~5s

**On screen**
- Poster serif title, terracotta period · handle beneath

```
title:    One File, No Contradictions
handle:   @HumanitariansAI
subline:  one policy · no disagreement · Mycroft
```

**Narration**
> One file, no contradictions. Simba, for Humanitarians AI.

---

## Build notes

**GATE L not yet run.** This is the script-writing pass only — no scene search or component
authoring has happened yet. Every non-house beat below is marked "Custom scene — needs building"
rather than given a pattern name; that search and the actual authoring happens at build time, same
as the Sprint 2 gateway script.

**Renderable today** (no new component needed, once build starts) — B00, B13 →
`ClaudeComposerAsk` · B12 → `ClaudeVerdictArtifact` · B14 → `ClaudeTitleOutro`. B01 is a one-line
statement/spark card. B07's comparison table is a close cousin of `DataTable` (already built and
QC'd twice in this series) and likely reusable with new props rather than a new component — worth
checking at GATE L before authoring from scratch. B08's "no route exists" beat and B09's
check-passed-but-wrong beat are the two most novel visuals in this script and the most likely to
need real new components.

**ASK→RESULT LAW — applied selectively, same judgment call as the last two sprint scripts.**
Kept the ask→result pattern where it's structurally load-bearing — the cold open, which frames the
whole video as an answer to a question, and the handoff, which is the viewer's own ask — and let
the middle run as a straight vox-style illustrated report rather than an ask-beat before every one
of the ten illustration beats (B02–B11). Worth a second opinion before build.

**No 9:16 cut drafted.** Wasn't asked for this time. If a Short gets made, THE SHORTS LAW applies
the same way it has on every prior video: single cycle, no revision, probably B00 → B01 → B07 (the
comparison table, the one real "wait, what" moment) → B12 (verdict) → B14, since B08's structural
finding is arguably the actual hook but doesn't compress as cleanly as a single table does.

**Duration.** The estimates above are arithmetic (word count ÷ Kokoro's measured rate), not
measurement — same caveat as every script before this one. Generate audio first and let it set the
real clock.

---

## Sources

- The Mycroft Sprint 3 router/policy report as pasted directly into this session — a first-party
  account of completed work, not a third-party claim requiring independent verification. DOUBLE-CHECK LAW is
  honored here by preserving the report's own carried-forward caveats rather than trimming them for
  a cleaner story: the synthetic-fixtures caveat (B05), the format-not-correctness gap in the free
  checks (B09), and the two flagged-not-fixed problems (B11) are all in the script exactly as the
  source stated them, not softened or omitted.
- All figures — the 6 task types, the 512/512/1,024 token budgets, the 24 fixtures, the 6/11/7 vs.
  8/16/0 tier comparison, the 9-of-24 agreement, the summ-004/extract-004 fixture IDs, the two
  flagged bugs — are quoted or closely paraphrased from that report; nothing is rounded past what
  it states or invented to fill a beat.
