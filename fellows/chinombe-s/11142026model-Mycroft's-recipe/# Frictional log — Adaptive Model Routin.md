# Frictional log — Adaptive Model Routing Gateway, Sprint 12

Research and diagrams: Simba. Beat sheet and production (audio, render,
compile, QC): Claude, from Simba's research and diagrams.

## 2026-11-17 — the model we cannot buy

- **Video:** TO FILL
- **Drive:** TO FILL
- **Report:** [REPORT.md](REPORT.md)
- **Commit:** TO FILL (Sprint 12 on `chinombesimbaremuteuro/adaptive-model-routing`)

> Written 2026-11-18, the day after the work.

**What I was working on.** Clearing the two blockers Sprint 11 found. Mycroft's
only real LLM requests — 16 of them, from the contradiction-detection agent —
name a model my price table has no rate for, and each asks for 2,000 output
tokens against a budget of 512. Neither can be served as written.

**What I tried, and what I expected.**
- I expected the pricing blocker to be a five-minute job: look up
  `llama-3.3-70b-versatile`, add a row to `prices.json`, bump the version.
- I expected the token budget to be the hard one, because raising it means
  arguing with a limit I set myself in Sprint 4.
- Both expectations were wrong, in opposite directions.

**Where it resisted, and what I did next.**
- **There is no price.** The model is sold on Groq's Enterprise tier with
  "Contact Sales" where the per-token rate should be. My planned fix — add the
  row — was not a fix, because there is no number to put in it. Two months ago
  I assumed this was a gap in my table. It is a gap in the market.
- **That made my own error message wrong.** When the gateway refused one of
  these requests it said "add it to prices.json with a source URL and the date
  read". That sends whoever reads it after a figure that does not exist. I had
  written a confident instruction for a situation I had not thought about.
  Fixed: an entry can now be recorded as `unpriced` with the reason in words,
  and the refusal quotes it.
- **While changing that I found a hole I had left open.** A price entry with
  no rates and no explanation was accepted silently. That is precisely how a
  missing price turns into a zero further down the line — the failure mode this
  whole table exists to prevent, sitting in the table itself. It now raises.
- **A conclusion from Sprint 4 turned out to be mis-attributed.** I had
  recorded a 1,000-output-tokens-per-minute cap as a property of the strong
  model, and set its budget at 896 because of it. The published developer-plan
  limit is 250,000 tokens per minute. The cap is my *account*, not the model.
  The budget is still right for this account; the reason I gave for it was
  wrong, and that is in the record now.
- **The biggest thing I found is not mine to fix.** If the model is
  Enterprise-only, that recipe probably cannot call it on a developer key at
  all — gateway or no gateway. I can report it; I cannot resolve it, and the
  person who owns that recipe does not know yet.
- **I deliberately stopped short.** The obvious next move was one live call to
  see what a contradiction review actually emits, which settles the 2,000-token
  question. I pushed it to next sprint rather than squeezing it in. Last time I
  rushed a measurement to close a sprint, I froze a wrong answer key.

**What Claude contributed, and what I did with it.**
- Claude read the published model list with me and drafted the changes to
  `prices.py`, `prices.json` and the tests. I ran everything; 238 passing.
- Accepted: recording a model as unpriced *with its reason*, rather than just
  leaving it absent. The absence and the explanation are different facts, and
  only one of them is useful to the next person.
- Accepted: rejecting a price entry that has neither rates nor a reason.
- Mine: the decision not to make the live call this sprint.

**What I understand now, and what I still do not.**
- Understood: an error message is part of the design, not decoration. Mine
  confidently gave advice that could not be followed, and nothing would have
  caught that except someone hitting it.
- Understood: "we have no price for this" and "this cannot be priced" are
  different problems with different answers, and I had only built for the first.
- Understood: a limit I measured was real, but the reason I attached to it was
  not. Measuring something correctly and explaining it correctly are separate
  acts.
- Not understood: what a real contradiction review actually emits. Until that
  is measured, 512 and 2,000 are both guesses.
- Not understood: whether an Enterprise model is callable at all on this key.
  One request to the provider's model-list endpoint would answer it, and I have
  not made it.