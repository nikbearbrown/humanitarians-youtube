# Week 2 video — narration script

**Target:** 2:55 · 438 spoken words · ~150 words per minute
(taking both cuts in the Notes brings it to ~2:35)
**Figures:** `images/private-ai-valuation-agent/w2-{funnel,anthropic-staircase,spacex-trap}.png`

Same pacing as week 1 — steady, unhurried, let the numbers land. Spoken forms are written
out below where they differ from what's on screen.

---

### 0:00 — Opening · on camera, or title card

> Week two of the Private AI Valuation Agent.
>
> Last week I proved by hand that SEC filings give you a share price for companies that
> have no public price. This week I scaled that up from one company to fourteen quarters
> of data — and the machine immediately found three things my hand-check had missed.

*Shot: title card, or straight to camera. Keep this tight — week one did the introducing.*

---

### 0:22 — The scale · cut to `w2-funnel.png`

> I pulled fourteen quarters of the SEC's bulk data. About six gigabytes, and eighty and a
> half million individual holdings — every position held by every registered fund in the
> country.
>
> That filters down to twenty-two million private positions, and then to about fifty-eight
> hundred marks on the AI companies I'm tracking. Every stage reconciles against the stage
> above it, and all of it now sits in a Postgres database.

*Shot: hold on the funnel. If you animate anything, animate the drop from the second bar to
the third — that collapse is the whole point.*

---

### 0:52 — What that buys you · cut to `w2-anthropic-staircase.png`

> And here's what that gets you. A price history for Anthropic, rebuilt entirely from
> filings. Thirty-three separate observation dates, from about twelve dollars a share in
> twenty twenty-three to over three hundred this April.
>
> Look at the shape of it. It's a staircase. The price sits perfectly flat for months, and
> then it jumps — because these marks only move when there's a new funding round. That was
> the project's core assumption, and now I can actually see it in the data.
>
> And at that two-fifty-nine step: seven completely independent fund managers — BlackRock,
> Fidelity, T. Rowe Price, Capital Group and three more — all report the identical price,
> to the cent, on the same date.

*Shot: hold on the staircase. Slow down on "identical price, to the cent."*

---

### 1:37 — The problem · stay on the staircase, point to the dashed line

> Then I went looking for something and couldn't find it.
>
> Last week I verified a mark of five eighty-nine by hand. It is not in this data at all.
>
> It turns out the bulk archive is organized by *when a fund files*, not by what period the
> filing covers. Funds file about eight weeks late — so the newest data in the second-quarter
> archive only reaches April thirtieth. The whole archive is structurally two months further
> behind than its own label suggests. That single fact reshapes next week's work.

*Shot: hold on the dashed "bulk ends" line and the hollow circle floating past it.*

---

### 2:11 — Two traps · cut to `w2-spacex-trap.png`

> Two more traps, both caught before they did damage.
>
> Four of Fidelity's funds file under a name that never says "Fidelity." So my code was
> counting one manager as five — inflating the exact number this project exists to measure.
>
> And this: one SpaceX filing, one company, common stock at a hundred and twelve dollars and
> preferred at eleven-twenty. Exactly ten times apart, inside a single document. Three
> hundred and nine cases of it — and no other company in the data does it at all.

*Shot: let the two price columns hold. The red eleven-twenty against the black hundred-twelve
does the work.*

---

### 2:42 — Next week

> Fourteen quarters loaded, thirty-three tests passing. Next week: the live filings — because
> that's now the only way to reach anything recent.

*Shot: back to camera, or end card.*

---

## Notes

**If you run long,** cut the second sentence of the opening and the Fidelity trap (it's the
least visual of the three findings). That buys about twenty seconds.

**Say "fifty-eight hundred," not "five thousand eight hundred and six."** Same for "eighty
and a half million." The exact figures are on screen; speaking them kills the pace.

**The strongest line is "it's a staircase."** That is the one idea a viewer will actually
carry away — private valuations don't drift like a stock price, they sit still and then
jump. Land it, then pause before the seven-managers line.

**Say "independent managers," not "filers" or "funds."** Seven is the honest number: those
twenty-four filings collapse to seven actual decision-makers once you group Fidelity's many
registrations together. Getting that distinction right is the point of the second trap, so
don't undercut it by quoting the bigger number here.

**Don't oversell the price history.** It is a record of what funds *marked* Anthropic at —
not what Anthropic is worth. Every number on screen traces to a filing, and that restraint
is the project's actual claim to attention.
