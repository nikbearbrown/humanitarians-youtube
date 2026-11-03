# PROMPTS — `ai-data-quality`

Two kinds of prompt live in this file, and they are not the same thing.

---

## 1. The prompts that appear ON SCREEN

These are shown inside the Claude-skin composer beats. They are part of the
film, so they are quoted here verbatim — if the beat sheet and this file ever
disagree, the beat sheet wins and this file is stale.

### B00 — the cold open (ASK → RESULT: the ask lands answered)

> Our warehouse has 4,000 columns and 12 documented data rules. Profile the
> data, propose the missing rules as executable checks, rank them by what a
> silent failure would cost, and tell me which columns you are NOT confident
> enough to propose a rule for.

Result lines printed beneath it:

```
profiled 4,000 columns · 12 rules documented
proposed 318 candidate checks, ranked by blast radius
flagged 41 columns: no rule inferable — ask an owner
```

*Why this prompt:* the last clause is the whole thesis in miniature. Asking a
model where it is NOT confident is what turns a generator into an instrument.
318 and 41 are the numbers B06 later reconciles.

### B04 — the single-column ask (the RESULT is B05)

> Profile customers.country. Propose one executable expectation with a
> severity and an owner. Show the evidence: value counts, the long tail, and
> how many rows would newly fail. Do not modify a single value.

*Why this prompt:* it is deliberately the opposite of "clean my data." Four
constraints do the work — one column (scopeable), evidence (auditable), an
owner (accountable), no mutation (reversible).

### B10 — the handoff (HANDOFF LAW: read aloud, then discussed)

> Here is the schema and a 1,000-row sample of one table I own. For each
> column, propose one executable expectation with a severity and an owner,
> rank them by what a silent failure would cost, and list every column where
> you cannot infer a rule and must ask a human. Do not modify any values.

The narration reads it out and then says what to look for: *the columns it
refuses to guess on are the ones your organization never actually decided.*
That refusal list is the deliverable — which is why the beat holds on screen
long enough to pause on.

---

## 2. Open slots needing media

**None.** Every one of the twelve beats is filled by a Remotion composition
this repo renders. `pantry/` is empty and stays empty; there is no human
media owed on this reel, in either aspect ratio.

If a future revision *does* open a slot, it goes here in the form
`B0X — <what to make> — <where it drops>`, and `./art todo <reel>` will pick
it up automatically from the beat sheet.
