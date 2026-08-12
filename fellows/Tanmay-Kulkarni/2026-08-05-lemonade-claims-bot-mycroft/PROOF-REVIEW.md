# Feedback: "I Built Lemonade's Claims Bot" — Tanmay Kulkarni, film 3

**Verdict:** ~~unlisted-until-fixed~~ → **clear-for-public** *(fix applied
2026-08-10, verified on the shipped master — see Resolution below).*
Teaching **12/12**. Production gate **PASS**.

One line: *this film sets out to teach an honest audit of your own distance from
production, and delivers it — and now carries its own receipts for every claim
it makes, which is the standard it argues for.*

> **Original verdict, kept for the record:** unlisted-until-fixed, gate FAIL on
> "sources on screen." One claim about third-party coverage shipped with no
> source on screen — the exact move the film's own thesis argues against.

---

## Rubric

| Criterion | What it means | This cut |
|---|---|---|
| **Explicit framework** | Organizing idea shown as structure *before* the examples | **2** — B02B puts the four questions on screen as a board at ~0:48, before any stage is opened. Not narrated after the fact. |
| **Reusable rubric** | A viewer could apply the same axes to a new case without guessing | **2** — the axes are named, defined, lit on B04/B06/B08 as they're used, and restated as a copyable card at B10. See the caveat under *The problem*. |
| **Worked example** | One case walked through the framework live — the reasoning step | **2** — Sofia traced through all three stages with real extracted values (`0.95` confidence, `$120`, `2026-05-01`) and real demo output. Zeus's `not_authorized` shows the negative path. |
| **Falsifiability / edge case** | Framework stress-tested against a counterexample | **2** — B07B. `demo_only_policy` is invented like the other two values but deliberately carries no `[DEV]` marker, fitting none of the film's own rules. Not manufactured for the video: a logged exception in `DESIGN_DECISIONS.md` Decision 2 that predates it. |
| **Active task** | CTA requires structured work, not "ask Claude" | **2** — B10 hands over a copyable prompt, the four axes, and an explicit pass/fail ("one row moves to bucket three, you did it right; nothing moves, you defaulted past the gap"). |
| **Friction** | Viewer must resolve a tension, not just receive facts | **2** — B06B stops and makes the viewer commit before B07 reveals the gate is empty. The asymmetry it poses (two undisclosed values got labelled defaults, one got nothing) is genuinely arbitrary-looking until the rule lands. |

**Total 12/12.**

### Reverse-engineering check (Behavioral Rule 1)

The tell PROOF hunts is categories mapping one-per-example. These don't: four
questions distribute **2 / 3 / 1 / 1** across three production beats, not 4→4.
The framework also survived a real counterexample (B07B) rather than being
protected from one. It is not retrofitted.

---

## Production gate

| Criterion | Result |
|---|---|
| **Evidence legible at the moment of assertion** | **PASS** — verified on frames pulled from the finished master, not the per-beat renders. B07's entire gate file reads without scrolling. B09's right-hand panel was checked specifically at the moment of assertion (~65% of the beat) and measures ~97% opacity; an earlier 55% sample caught it mid-fade and was cleared. |
| **Sources on screen, not just voiced** | ~~FAIL~~ → **PASS** — one claim shipped unattributed (B06); fixed and re-verified on the shipped master. The finding is kept in full under *The problem*, and its fix under *Resolution*. |
| **Side-by-side at the moment of comparison** | **PASS** — B05/B06 hold identical row geometry so only the delta moves; B07B contrasts two `[DEV]`-marked values against one unmarked one in a single frame. |

---

## The problem

**B06, at roughly 3:00.** The narration says:

> "Lemonade's fraud system and its claims bot are two different things, and
> **outside coverage keeps merging them into one** — I didn't want my own code
> repeating that mistake."

That is a factual claim about the world — about what third-party coverage does.
It is sourced in the documentation (case study §6.5) and it is correctly hedged
in the narration. **But nothing on the B06 frame attributes it.** The right
column carries `mock_fraud_signal → your fraud system` and the design note
"Keep it independent — never a field on the record," and no source line
anywhere.

Every other external claim in the film is covered. B01 carries the filing date.
B07 puts the verbatim 10-K quote beside the code with its filing date. B03
labels Sofia illustrative on screen *and* in narration. B04 and B08 make
prescriptive engineering claims that are the creator's own judgment, not
citable facts, and need no citation. B02's claims are about the creator's own
artifact, which is on screen.

This one slipped, and it matters more here than it would in another film:
**B07's entire argument is that you must not assert a shape of answer your
source doesn't support.** A film making that case has to carry its own
receipts. PROOF's grade-the-graders rule is explicit — the video is held to its
own standard first.

Severity: minor in substance, structural in principle. One line of prop text.

---

## Do this before publishing

1. **[EDIT] Add a source line to B06's fraud card.** Something like
   *"Forensic Graph and AI Jim are separate systems in Lemonade's own
   disclosure — case study §6.5."* One prop string; the component already has
   a `note` slot rendering at that position.
   Cost: edit props → re-render B06 (~2 min) → recompile (~8 min) → re-run
   `pacing_pass.py` (~3 min) → re-verify. **~15 minutes, no reshoot.**

2. **[EDIT, optional] Attach the absence claim on B01 to its audit.** The right
   column asserts "No dollar threshold, claim-type list or confidence score
   appears in any filing, letter, deck or interview" while the only visible
   source sits in the left column under the statistics. The claim partly
   self-describes its own scope, so this is weaker than finding 1 — but an
   audited absence reads stronger with its audit named.

3. **[EDIT, optional] Thin axes.** Question 3 (*failure paths*) lights once, on
   B04; question 4 (*accountability*) lights once, on B08. Questions 1 and 2
   each carry two or three beats. The rubric is still applicable without
   guessing — which is what the criterion asks — but a viewer sees half of it
   demonstrated once. If a future cut has room, give 3 and 4 a second surface.

---

## What works — keep this

- **B07B is the strongest asset in the film.** A framework that meets a real
  exception, and comes out sharper for it, is the hardest thing on PROOF's
  rubric to fake. That it was a logged design decision *before* the video
  existed is what makes it credible rather than decorative.
- **The scaffold/production alternation is a genuine teaching grammar.** B05 and
  B06 hold identical geometry so the viewer reads the delta instead of
  re-orienting; three different interior motions (branch / substitute /
  accumulate) keep the middle from going metronomic.
- **The film states an absence as an absence.** It does not invent a threshold
  for Lemonade, and it says on screen that it won't. That restraint is the
  whole point.
- **Fact-recitation is ~7–11% of runtime**, far under the ~50% ceiling. The
  method gets the time.

---

## Note on scope

This review covers the rubric, the production gate, sourcing, pacing and
calibration from the finished 3840×2160 master, its beat sheet, and frames
pulled from the shipped file. It does not cover whether the film *plays* — the
feel of the pacing, whether the narration lands, whether the holds breathe.
PROOF cannot watch a video and neither can an automated check. That judgment
remains the creator's, and should happen before publishing regardless of this
verdict.

---

## Resolution — 2026-08-10

**Finding 1 fixed.** B06 now carries, beneath the fraud-system swap card:

> *Forensic Graph and AI Jim are separate systems in Lemonade's FY2025 Form
> 10-K — case study §6.5.*

Implemented as a new `sourceNote` prop on `LemonadeProduction` rather than by
extending an existing swap card's `note`. That separation is deliberate: a
design instruction ("keep it independent — never a field on the record") and a
source citation are different kinds of statement and must not read as one. The
attribution is styled as a source — smaller, ghost weight — not as body copy.

**Timing verified against the assertion, not just against the frame.** The
source resolves at ~24s into the beat; the narration makes the conflation claim
at ~28s. Confirmed by pulling the frame from the **shipped master** at 184.5s —
the moment the claim lands — where the line is fully legible.

Rebuild: re-render B06 → recompile at 2160p → re-run `pacing_pass.py` → verify.
Final master unchanged in every other respect: **369.79s, 3840×2160**, 14 beats,
13 holds.

Findings 2 and 3 remain open as optional edits. Neither blocks publishing:
finding 2 is a precision improvement on a claim that partly self-describes its
own scope, and finding 3 is a "if a future cut has room" note.

**Gate now passes all three criteria. Ship rule satisfied:
teaching 12/12 ≥ 8, gate PASS, and the film passes its own standard.**

The scope note above still stands — no automated check substitutes for watching
it.
