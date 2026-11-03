# FACTCHECK — The Judgment Is the Job.

DOUBLE-CHECK LAW + REBUILD LAW record. Written before audio lock.

## The governing constraint (explicit, from the human)

> "Please don't invent statistics or numbers I can't verify. If you want to make
> comparisons, use rankings or described models (like 'significantly faster' or
> 'increasingly common') rather than specific percentages or numbers, unless I give you
> a real source."

No source was supplied, so **this reel contains no statistic, percentage, count, rate, or
dated projection anywhere** — not in narration, not on a card, not on an axis. Every
comparison is either ordinal (position, length, order of appearance) or stated in words.

Three things enforce that rather than one:

1. **Structural.** The three purpose-built scenes (`JdgSplit`, `JdgOptions`, `JdgStakes`)
   have no prop that accepts a numeric datum to render. There is no code path that can
   print a figure, so the constraint cannot be violated by forgetting it later.
2. **Automated.** A numeral audit was run over every on-screen string in the beat sheet
   before the first render. It reported exactly one hit — see the exception below.
3. **Editorial.** The verdict card states the limit out loud: *"a shift in progress,
   described — not a prediction with a date, and no numbers are claimed here."*

### The one numeral on screen, and why it stays

`B08.command` reads "Here are my last **5** pieces of ad copy or creative."

That is a quantity in an *instruction the viewer pastes into Claude about their own work* —
it sets the size of their exercise. It is not a measurement, a claim about the industry,
or anything the viewer must take on trust. Kept deliberately; a vaguer "some recent
pieces" would make the handoff task worse, and HANDOFF LAW requires a genuinely useful
prompt.

## Claim ledger

| # | Beat | Claim as spoken | Verdict | Basis |
|---|---|---|---|---|
| 1 | B00 | "A tagline used to take a week and a room full of people" | ⚠ rhetorical framing | A characterisation of the old process, not a measured duration. Deliberately loose ("a week", "a room") rather than falsely precise. If this needs hardening, it needs a source. |
| 2 | B00 | The asker's premise (AI drafts their copy, taglines, social, and visual concepts) | ✓ | Spoken by the prompt's fictional author as the setup for the question, not asserted by the narrator. |
| 3 | B01 | AI replaced the *execution* of copy/art direction, not the judgment | ✓ — the thesis | Definitional rather than empirical, and the whole reel is the argument for it. Falsifiable at B06. |
| 4 | B02 | "AI is dramatically faster at all of it, and getting more so" | ✓ as described comparison | Exactly the form the human asked for — described, not quantified. No multiplier, no percentage. |
| 5 | B02 | Ledger: headlines / taglines / social variants / translations moved; legal-survival, brand voice, quality judgment did not | ✓ as ordinal split | The columns are a categorisation, not a measurement. Nothing is ranked numerically. |
| 6 | B04 | "A wall of concepts, faster than a designer could sketch one" | ✓ as described comparison | Comparative, unquantified. The wall shown is illustrative concept *labels*, not generated artwork — see the REBUILD LAW note below. |
| 7 | B04 | "the machine has no opinion about which is right" | ✓ | Load-bearing and defensible: the generator produces candidates; ranking them against a brand standard is not something it is doing here. |
| 8 | B05 | A role described as "producing assets" is "increasingly obsolete" | ✓ as described trend | "Increasingly" per the human's instruction. No timeline, no proportion, no headcount claim. |
| 9 | B05 | A role described as owning the standard "just got more leverage" | ⚠ contestable, and framed as such | Presented as one of *two* futures on a branch the viewer chooses between, not as a prediction. |
| 10 | B06 | Four things the machine cannot own: truth of a claim, voice over time, cultural landing, accountability | ✓ | The reel's strongest section and its falsifier. Each is a category, not a metric. |
| 11 | B06 | "If your work contains none of those, you're exposed" | ⚠ pointed, deliberately | This is the Teardown judgment. It is a conditional the viewer can test against their own work, which is what makes it fair rather than a scare line. |
| 12 | B07 | The verdict's four lines | ✓ | Each recapitulates something already shown. Verdict beats are exempt from no-source-no-verdict (they recapitulate, not assert). |

## Dating risk

- No model names, version numbers, or product claims in the body. **Same caveat as the
  previous reel:** the shipped `ClaudeComposerAsk` chrome renders a model chip (currently
  "Fable 5"), so a model name does appear in the three composer beats. It is component
  chrome, never referenced by the narration, and editing it means changing a shared
  fidelity component. The bookends will therefore date faster than the body.
- No dates, no "as of" figures, no headcount or salary claims.
- The argument is about which *half* of creative work a generator touches, so it survives
  any model generation.

## REBUILD LAW note on B04

The "wall of concepts" is rendered as native Remotion concept **cards carrying angle
labels** — "Commuter dawn", "Refill ritual", "The last plastic" — not as generated
imagery. Two reasons, both deliberate: generating twelve images would require a paid
image engine (out of scope for the free path, and the reel must never imply a spend), and
the beat's point is about *quantity of options and who chooses*, which labels carry
honestly. Nothing on screen is presented as a real generated ad.

## Register check

Could this script have been read off a source? No — there is no source. The Teardown move
is refusing both available clichés: it neither celebrates the productivity gain nor
predicts the death of the profession. It lands on a structural claim (execution moved,
judgment didn't), attaches a self-test the viewer can fail, and says plainly that it is a
description rather than a forecast.

## Corrections applied during authoring

1. Cut an early B02 line comparing drafting speed as a multiple — replaced with the
   described comparison "dramatically faster, and getting more so".
2. Cut a B05 line about proportions of creative roles affected — replaced with the
   two-futures branch, which makes the same point without a quantity.
3. Reworded B04 from "twelve concepts" in the narration to "a wall of concepts", so the
   voice asserts no count even though the grid happens to show twelve cards.
4. Added the no-numbers clause to the verdict card so the constraint survives into the
   recap rather than living only in this file.
