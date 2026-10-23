# Week 1 video — narration script

**Target:** 2:00 · ~305 words · ~150 words per minute
**Figures:** `images/private-ai-valuation-agent/w1-{convergence,filter-defect,universe}.png`

Read at a steady, unhurried pace. The numbers are the point — let them land. Spoken forms
are written out below where they differ from the on-screen figure.

---

### 0:00 — Opening · on camera, or title card

> Hi, I'm Om Mali, and this project is a Private AI Valuation Agent.
>
> Most of the AI industry's value sits in companies you can't buy. OpenAI, Anthropic,
> Databricks — no ticker, no earnings call, no public price. But the mutual funds that own
> pieces of them have to report every holding to the SEC, with a dollar value and a share
> count. Divide one by the other, and you get a price per share for a company that has no
> public price. This project reads those filings and turns them into a price history.

*Shot: title card, then a scroll of the raw Anthropic block in `primary_doc.xml` on EDGAR —
let the viewer see `<balance>` and `<valUSD>` for a beat.*

---

### 0:27 — What I did · cut to `w1-convergence.png`

> In week one, I verified that by hand. I pulled nineteen Anthropic positions from six
> different fund families straight out of the filings, and did the arithmetic myself.
>
> Fidelity, T. Rowe Price, Alger and ARK all priced Anthropic at two hundred fifty-nine
> dollars and fourteen cents. Identical — to the cent. Then a new funding round repriced it,
> and BlackRock and Capital Group both marked it at five eighty-nine, matching to four
> decimal places, two days apart.

*Shot: hold on the convergence figure. If you animate one thing, animate the dashed jump.*

---

### 0:57 — Problems · cut to `w1-filter-defect.png`

> Then I hit the problems.
>
> My plan had a filter that was supposed to isolate private holdings. It dropped five of my
> six managers — silently, with no error. Different funds write "N slash A" or nine zeros
> for a missing identifier, and two of them flag restricted stock as unrestricted.
>
> The plan also expected a few thousand private rows per quarter. The real number was six
> hundred and six thousand. So I inverted the pipeline — match companies by name first,
> confirm they're private second. That shrank the hardest part of the project by about five
> hundred times.

*Shot: the six-manager list, then the two bars. Consider a beat of silence after
"six hundred and six thousand."*

---

### 1:32 — Output · cut to `w1-universe.png`

> So the output for week one: the approach is proven. The SEC's bulk data matched my
> hand-read filings fifteen out of fifteen, exactly. And universe version one is frozen at
> six companies — with SpaceX added, and Cohere removed, because every single Cohere match
> turned out to be Coherent Corp, a public optics company.

*Shot: universe figure. Let the ochre Cohere callout hold for the last line.*

---

### 1:54 — Next week

> Next week: load eight quarters into the database, and start on entity resolution.

*Shot: back to camera, or end card.*

---

## Notes

**If you run long,** cut the second sentence of the opening ("OpenAI, Anthropic,
Databricks — no ticker...") and the phrase "silently, with no error." That buys ~12 seconds
without losing a finding.

**Say "five eighty-nine," not "five hundred and eighty-nine point zero zero nine five."**
The precision is on screen; speaking it kills the pace.

**The strongest line is "identical — to the cent."** Slow down there. That single fact is
what makes the whole project worth doing, and it is the one thing a viewer will remember.

**Don't oversell.** Every number here is measured and traceable to a filing. That is the
project's actual claim to attention — not novelty, not a trading edge.
