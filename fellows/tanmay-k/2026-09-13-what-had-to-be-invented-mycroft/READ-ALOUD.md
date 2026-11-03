# READ ALOUD — *What Had to Be Invented*

Generated from `beat_sheet.json` by `make_read_sheet.py`. **Do not edit here** —
edit the narration in `build_beat_sheet.py` and rebuild, or the words you read
stop being the words that ship.

am_onyx · Pragmatist register · presenter Tanmay Kulkarni, in for Humanitarians AI
16 beats · 965 words · target 4:50

Read against the 4K slates in `manim/` — one per beat, same ids.

**This film is about a method working.** Absences in the implementation it examines
are documented boundaries, not defects. If any line sounds like an accusation when
spoken, mark it FIX — that is the one thing the text must not do.

## How to run the pass

1. Read every beat **out loud, at pace**, with its slate on screen. Not in your
   head — the defects this gate exists for are audible only.
2. After each beat mark `PASS` / `FIX` / `CUT` below. If `FIX`, write **what you
   heard**, not what you would rewrite.
3. Answer the six questions in `PEDAGOGY.md`. Only the read can answer them.
4. Sign the verdict line in `PEDAGOGY.md`. **Audio stays blocked until it reads
   PASSED** — Gate P is a precondition for narration, not a review of it.

Watch for two things this film can fail on. **First, the three moves.** CONFIRM,
CONSTRUCT and REFUSE carry the whole argument, and the first two share a syllable — if they
do not separate cleanly in your mouth they will not separate in anyone's ear. **Second,
quoted code.** Seven beats read file contents aloud; a line that works on screen can be
unsayable. Also listen for `validated` against `not_validated`, which differ by one spoken
word and appear in the same breath at B07.

---

## B00 · COLD OPEN · ~21 s
*flat, quoting*

> slate: `manim/B00.png` · hold 4 s

Here is a comment from the middle of a working pipeline.

Not a readme.

Not a docstring.

A comment sitting three lines inside a function, at the exact place where it would have been easiest to make something up.

It reads: not a modeled failure mode.

The confirmed record gives this stub no disclosed behaviour for this case, so it degrades gracefully, rather than inventing a halt condition that isn't sourced.

`PASS / FIX / CUT` ____________

what I heard: 

---

## B01 · PRESENTER · ~12 s
*direct*

> say: **Kulkarni** = kul-KAR-nee
> say: **Concierge** = kon-see-AIRZH

This is Tanmay Kulkarni in for Humanitarians AI.

I built a reference implementation of Capital One's Chat Concierge using only what the company has published.

This video is about what that one constraint does to the code you end up with.

`PASS / FIX / CUT` ____________

what I heard: 

---

## B02 · FRAMEWORK · ~21 s
*instructive*

> slate: `manim/B02.png` · hold 3 s

To make any stage of a system actually run, you have to answer questions the public record does not answer.

There are three honest moves.

Confirm it, when a source states it.

Construct it, and say in the file that you did.

Or refuse, and leave the hole exactly where the evidence stopped.

I am going to walk five stages and show you which of the three each one took.

`PASS / FIX / CUT` ____________

what I heard: 

---

## B03 · STAGE ONE · ~18 s
*expository*

> slate: `manim/B03.png` · hold 4 s

Stage one.

Understanding the request.

Capital One's blog confirms the system understands natural language prompts.

It does not publish a request schema.

So what counts as a complete request?

That one was constructed, and the file says so out loud.

The parsing logic, the completeness criteria, and the shape of the object are all called this repository's own invention.

`PASS / FIX / CUT` ____________

what I heard: 

---

## B04 · STAGE ONE · ~20 s
*setup*

> slate: `manim/B04.png` · hold 4 s

Underneath that, a smaller choice with a consequence.

The list of vehicles the parser recognises is deliberately not the dealership's inventory list.

Two separate lists, allowed to disagree.

So here is a question worth answering before I do.

A customer names a car the parser knows and the dealership does not stock.

What should the code do?

Decide now.

We come back to it at stage five.

> **then stop. Do not answer it.** B09 collects this four beats later.

`PASS / FIX / CUT` ____________

what I heard: 

---

## B05 · STAGE TWO · ~11 s
*expository*

> slate: `manim/B05.png` · hold 3 s

Stage two.

Building the plan.

Confirmed: the system comes up with an action plan to execute on those prompts.

What makes a requested slot infeasible is not published.

So that was constructed too, and marked as constructed.

`PASS / FIX / CUT` ____________

what I heard: 

---

## B06 · STAGE THREE · ~28 s
*load-bearing*

> slate: `manim/B06.png` · hold 4 s

Stage three.

Validation.

Here the blog is specific.

Two checks, named separately.

Check for hallucinations or errors.

And simulate the execution of the action plan and determine if the outcome conforms to policies and business rules.

So the checks are confirmed.

The threshold is not.

What counts as good enough was never published, and this is where the build stops.

The gate ships with zero acceptance criteria.

No confidence threshold, no dollar amount, no approval default of any kind.

Ask it to run without a decision rule and it raises, at construction.

`PASS / FIX / CUT` ____________

what I heard: 

---

## B07 · STAGE THREE · ~9 s
*corroborating*

> slate: `manim/B07.png` · hold 3 s

It refuses twice.

If the rule you supply returns anything the gate does not recognise, it raises again rather than guessing.

An unrecognised value is never treated as an implicit approval.

`PASS / FIX / CUT` ____________

what I heard: 

---

## B08 · STAGE FOUR · ~15 s
*expository*

> slate: `manim/B08.png` · hold 4 s

Stage four.

Explaining the plan to the customer.

Confirmed by the blog.

And this file has no failure path at all.

That is not an oversight, and the file says why.

No source discloses this step failing, and inventing one here would add a scenario Capital One never described.

`PASS / FIX / CUT` ____________

what I heard: 

---

## B09 · STAGE FIVE · ~27 s
*the payoff*

> slate: `manim/B09.png` · hold 5 s

Stage five.

Writing the appointment to the dealership's own system.

Now remember the two lists that were allowed to disagree.

A customer names a car the parser knows and the dealership does not stock.

That is the moment to invent a failure mode.

The code does not.

It falls back, and the comment beside it says it degrades gracefully rather than inventing a halt condition that isn't sourced.

Every other refusal in this build sits in a docstring, where a reader expects hedging.

This one is in the running code.

`PASS / FIX / CUT` ____________

what I heard: 

---

## B10 · THE COST · ~17 s
*honest*

> slate: `manim/B10.png` · hold 4 s

Now the cost, because there is one.

A gate with no default hands you a halt you cannot act on until you supply the missing policy yourself.

That is more work, not less.

This discipline does not make the system smarter.

It makes the boundary visible, and somebody still has to decide where the line goes.

`PASS / FIX / CUT` ____________

what I heard: 

---

## B11 · WHAT THEY PUBLISHED · ~26 s
*corrective*

> slate: `manim/B11.png` · hold 4 s

And for one of these, Capital One did publish an answer.

On rejection, the evaluator sends the plan back to the planning agent to correct.

It does that based on its judgement of where the problem was, iteratively, until an acceptable plan is reached.

That loop is confirmed.

It sits outside this pipeline's scope, which is a scope line, not a missing piece.

What is still undisclosed here is narrower.

Whether there is a cap on those iterations, and what happens if they never converge.

`PASS / FIX / CUT` ____________

what I heard: 

---

## B12 · THE EDGE · ~28 s
*self-limiting*

> slate: `manim/B12.png` · hold 4 s

Now notice what that one does to my three moves, because it does not fit any of them.

It was not refused for want of evidence.

The evidence exists.

Confirm, construct and refuse cover what to do when the record is silent.

They do not cover what to do when the record speaks and you are not building that part.

That is a fourth thing.

I am not going to fold it in and pretend the framework always had four, because the useful part of a framework is knowing where its edge is.

`PASS / FIX / CUT` ____________

what I heard: 

---

## B13 · THE COUNT · ~16 s
*summary*

> slate: `manim/B13.png` · hold 4 s

Counted, not claimed.

Seven confirmed markers.

Ten constructed.

Fifteen development notes.

Eleven design decisions, each logged against the review pass that settled it.

Thirty two tests, all passing.

Method leaves a trail you can count, and that is the difference between a build that was disciplined and a build that says it was.

`PASS / FIX / CUT` ____________

what I heard: 

---

## B14 · YOUR TURN · ~17 s
*direct*

> slate: `manim/B14.png` · hold 4 s

Your turn, and it works on anything.

Take a reference implementation, or a vendor's description of an AI system.

Pick one component and ask what had to be invented to make it runnable.

Then check whether the artifact tells you which parts those were.

If it doesn't, you are not reading a system.

You are reading a demo.

`PASS / FIX / CUT` ____________

what I heard: 

---

## B15 · SIGNOFF · ~4 s
*flat*

> say: **Kulkarni** = kul-KAR-nee

What Had to Be Invented.

Tanmay Kulkarni, in for Humanitarians AI, signing off.

`PASS / FIX / CUT` ____________

what I heard: 

---

