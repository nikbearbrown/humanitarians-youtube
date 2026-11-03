# Explainer — Why Jev Is Fast

**Week:** 21–25 Sep 2026
**Type:** STEM / AI explainer (general topic — no sprint report backs this one)


- **Video:** TO FILL
- **Drive:** https://drive.google.com/drive/folders/1LYJr3yRnV_77b5HQTvbN21b-z5r7EJEB?usp=sharing
- **Frictional log:** [FRICTIONAL.md](FRICTIONAL.md)
- **Script:** `why-jev-is-fast.md` in this folder

## What it covers

TypeSafe AI ships a model, Jev, that answers a structured decision in 70–500 ms
where a frontier language model doing the same decision takes 3 to over 300
seconds. The video explains **why** that gap exists, and is careful about which
parts of the story are mechanism and which are marketing.

## The argument

**The mechanism (not a vendor claim).** A general-purpose LLM decodes
autoregressively: the last token plus its cached context go in, one forward pass
runs, the next token comes out, and that repeats once per token. It is inherently
sequential, and the answer costs as many steps as it has tokens.

Jev is non-autoregressive. The whole input goes in, one forward pass runs, and
the entire typed answer comes out at once  because the answer is not open-ended
prose but one of a small, predefined set of shapes: a choice, a score, a yes/no,
with a confidence number attached.

Three things enable that: the output schema is fixed before generation rather
than discovered token by token; the training method (Reinforcement Learning for
Calibrated Decisions) targets a confidence-scored typed value rather than fluent
prose; and the answer space is closed, which the company says makes a type error
impossible by construction.

**The speed does not come from a better model. It comes from a smaller
question.** That part needs nobody's word for it  it is how non-autoregressive
generation works.

**The magnitude (entirely vendor-claimed).** TypeSafe's published figures, on
their own example task: 0.114 s versus 8.566 s, and $0.000081 versus $0.01388 
the source of the headline 193x faster and 445x cheaper.

**The state of the evidence.** No published architecture, no released weights, no
independent technical paper. The company's technical notes were written by its
own model-capabilities team, and the company itself says the reported gains
likely represent "the high end of real-world results." Outside observers have
guessed the model may build on an existing open-weight model — unverified. The
one piece of independent coverage, Tom's Hardware, declined to endorse the
numbers: *"only practical use will tell."*

**The comparison is a category comparison.** Jev does structured decisions.
Writing an email, summarising a document, holding a conversation — still an LLM's
job. Measuring Jev's speed against a general model on Jev's own task type is not
the same as asking which is faster in general.

## Why this topic

It is the same track as `hai-prefill-decode` and `hai-how-kv-cache-works`: why
inference costs what it costs. It also bears directly on the gateway project.
Mycroft's gateway validates an answer's *shape after the model has produced it*,
and two of those checks have now failed **correct** answers over formatting  a
quoted span in Sprint 4, a bracket glyph in Sprint 5. A closed answer space is
the claim that this class of bug cannot occur, because the shape is guaranteed
rather than inspected. Stronger in principle, if the claim holds.

## Production notes

All three diagram beats reuse existing components; nothing new was authored.
`AutoregressiveLoop` and `ParallelPass` come from `hai-prefill-decode`,
`GuardCards` pre-existed independently.

One editorial choice is recorded deliberately: the third `GuardCards` card is set
`ok:false` for the "cannot produce a type error" claim. That marks a **sourcing**
caveat  the claim is company-stated and unverified  not a technical failure of
the approach. B06–B08 unpack it immediately afterwards.

## Sources

- [TypeSafe AI — Introducing System One Models & Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) — company blog; published numbers and architecture description
- [TypeSafe AI homepage](https://typesafe.ai/) — headline claims (193.6x faster, 444.6x cheaper) on the company's own example task
- [Tom's Hardware — TypeSafe AI's Jev offers an alternative to LLMs](https://www.tomshardware.com/tech-industry/artificial-intelligence/typesafe-ais-jev-offers-an-alternative-to-llms-that-claims-to-be-193x-faster-and-445x-cheaper-system-one-type-model-is-bespoke-for-probabilistic-decision-making) — independent coverage, including the category-comparison caveat
- Wikipedia — *Jev (AI model)* — company background and funding, and the company's own acknowledgment about "the high end of real-world results"

