# PEDAGOGY — Gemma 4, Unified? (nbb claude explainer)

**GATE P document.** Narration does not go to audio until a human writes
`VERDICT: PASS` at the bottom of this file.

## Thesis

One sentence the viewer couldn't say before:

> Gemma 4's newest member reasons about images and sound with almost no
> perception hardware in front of it — Google deleted a 550-million-parameter
> vision encoder down to a 35-million-parameter matrix multiply, and deleted the
> audio encoder entirely — but nobody has run the experiment that would prove
> that's a good idea.

## The misconception being broken

**Brief said:** generators and discriminators need different architectures, but
architectures are converging, and Gemma 4 is an any-to-any model.

**What the sources say** (FACTCHECK #23–#27): Gemma 4 emits **text only** — the
"any-to-any" phrase is a `transformers` *pipeline name*, not an output
capability. And with no generative visual head and no discriminator, Gemma 4 is
not an instance of generator/discriminator convergence at all.

**Reframed misconception (what the reel actually breaks):**

> *Each modality needs its own specialist architecture — a vision transformer to
> see, a Conformer to hear, a language model to reason.*

This is a better target than the original because (a) it is what Gemma 4 is
literally evidence about, (b) it is what most practitioners currently believe and
build, and (c) the refutation is visual and countable — a 550M box shrinks to a
35M box and a 305M box disappears. The generator/discriminator thread the brief
asked about is still paid off, at B09, as a correction plus a reading list.

**Why the reframe is more honest, not just safer:** the original framing would
have had the narration assert two things the sources contradict. Under
`no source, no verdict` that is a fail, not a stylistic choice.

## Act structure

- **B00 ASK** — cold open in the composer. Question typed; a shorter line spoken.
- **B01 SUMMARY** — *added 2026-08-03 at the user's request, after the sign-off
  below.* Presenter line, the thesis in one sentence, and a three-card roadmap of
  what the reel will do. This is an advance organizer: stating the structure up
  front lowers the cost of following it. It does not spend ILLUSTRATE LAW budget
  (not a UI beat). Beats after it renumbered B02–B11.
- **B01 EXHIBIT** — the old regime: three frozen specialists bolted to the front
  of a decoder. Gemma 4's April four are the old regime.
- **B02 MECHANISM** — the vision deletion: 48×48×3 patches, 550M → 35M.
- **B03 MECHANISM** — the audio deletion, which goes further: encoder *gone*,
  raw 40 ms frames projected into the token embedding space.
- **B04 PREDICT** — viewer commits **before** the scores. "You removed the
  perception hardware. Did perception get worse?"
- **B05 EVIDENCE** — the numbers cut both ways: worse on MMMU-Pro, better on ASR.
- **B06 TWIST** — both readings are junk. Every comparison moves two variables.
  The report never runs the matched-size ablation.
- **B07 VERDICT** — artifact page, three lines: deletion real, efficiency real,
  parity unproven.
- **B08 REFRAME** — encoder convergence ≠ generator/discriminator convergence;
  here's where that other thread actually lives.
- **B09 HANDOFF** — `Your turn.` composer with a prompt the viewer can run.
- **B11 OUTRO** — title restate + `@HumanitariansAI`.

**ILLUSTRATE LAW compliance:** the Claude UI appears at B00, B07, B09, B10 only.
B01–B03 and B05–B06 are concept exhibits (custom scenes); B04 is PredictCard,
B08 is a concept exhibit. No two consecutive beats share a visual state — B01/B02/B03
are three distinct focus states of the encoder-stack exhibit, B05/B06 are two
distinct focus states of the scoreboard.

**PREDICT placement:** B04, immediately before the evidence and two beats before
the twist. The commit is what makes B06 land — a viewer who has privately guessed
"worse" gets to watch *both* their guess and its opposite get invalidated by the
same confound.

## Evidence discipline

Every factual claim is in `FACTCHECK.md` with a primary source and a verdict.
Two claims from the brief are **rejected there and cut from the reel** (#25, #26);
one claim is excluded as unverified (#31). Three statements are labelled
ARGUMENT (#21, #22, #27) and are spoken as reasoning, not as fact. One is
labelled a vendor claim (#19) and is attributed to Google out loud.

The single load-bearing secondary source is the 12B release date (#2, Wikipedia).
Narration therefore says "two months later" rather than a date, and the
architecture claims it introduces are sourced to the technical report.

## Friction

**Kept (germane load):**
- B04's commit before the reveal — the twist *is* the lesson, so the viewer has
  to have something at stake.
- Both benchmark directions in B05. Showing only MMMU-Pro would make an easier,
  wronger video ("encoder-free is worse"). The contradiction is the point.
- The parameter counts spoken aloud. 550 → 35 is the whole argument in two numbers.

**Removed (extraneous load):**
- Attention interleaving, pp-RoPE, KV-cache sharing, the 262k tokenizer
  (FACTCHECK #4–#6). Real, verified, irrelevant to this thesis. They belong to a
  "how Gemma 4 is built" reel, not a "what got deleted" reel.
- MoE routing and the effective-vs-total parameter distinction, except where B06
  needs the raw counts for the confound.
- The full unified-generation reading list. B08 names six models and stops; no
  claims about any of them.

## Pacing note

Sized to content, not to a clock: 11 beats, estimated ~2 min 30 s once audio is
measured. The brief asked for "short." If that estimate comes back too long, the
cheapest honest cuts are **B08** (the reframe — costs the payoff to the brief's
original question) and then **B01** (fold the old regime into B02's before-state).
Do **not** cut B04 or B06; without them this is a press release.

## GATE P checklist

- [x] Thesis is one sentence, and is a claim rather than a topic
- [x] Misconception named, and the reframe justified rather than quietly swapped
- [x] Every factual claim sourced in FACTCHECK.md; rejects logged, not deleted
- [x] ARGUMENT and VENDOR CLAIM statements labelled as such in narration
- [x] PREDICT beat commits the viewer before the reveal
- [x] ILLUSTRATE LAW: UI only at ASK / VERDICT / HANDOFF / OUTRO
- [x] Numbers written as spoken (FACTCHECK, final section)
- [x] **Human read the narration in NARRATION.md**

VERDICT: PASS

Signed by the user on 2026-08-03: *"I am happy with narration and duration and
everything."* Approved as written — the reframed thesis (encoder convergence, not
generator/discriminator convergence) stands, and the ~2m53s runtime is accepted
rather than cut. Audio generation released.
