# FACTCHECK — Both Sides of the Table.

`yatra-both-sides-of-the-table` · @Yatra · narrated by Kokoro `af_bella` ("Bella"), in for Yatra

---

## The standing instruction

> "Please use these verified statistics (cite sources as shown, don't alter the numbers)…
> Please don't invent any additional statistics or details beyond what I've given you."

Seven figures were supplied, from **five different publishers**. That last fact is the
main risk in this episode: six numbers in one video read as one dataset unless the reel
works to stop them. Everything below is enforced **structurally**, in the types.

---

## 1. The complete list of supplied figures

| # | Figure | Rendered as | Source, as supplied | Beat |
|---|---|---|---|---|
| 1 | 86% of organizations use AI in hiring | `86%` | Gartner, via CI CoPilot, October 2026 | B02 |
| 2 | 4 in 5 job seekers use AI in their search | `4 in 5` | Greenhouse, via CI CoPilot, October 2026 | B03 |
| 3 | 63% interviewed by an AI | `63%` | Greenhouse, May 2026 | B06 |
| 4 | up 13 points in six months | `+13 points in six months` | Greenhouse, May 2026 | B06 |
| 5 | 38% walked away over an AI interview | `38%` | Greenhouse, May 2026 | B07 |
| 6 | 26% trust AI to evaluate them fairly | `26%` | Greenhouse Candidate AI Interview Report, 2026 | B08 |
| 7 | 66% of US adults wouldn't apply if AI decides | `66%` | Pew Research Center | B08 |
| 8 | 41% admit to prompt injections / hidden instructions | `41%` | SelectSoftwareReviews, 2026 | B09 |

**No other number appears anywhere in this reel**, on screen or in narration.

---

## 2. How citation is enforced

Every scene that renders a figure **requires** a `source` string — `TblSide`,
`TblInterview`, `TblWalk` and `TblInject` cannot be constructed without one.

**`TblTrust` goes further: it requires a SEPARATE source on each of its two figures.**
The 26% and the 66% come from different studies, asking different questions, of different
populations. The component renders each citation beneath its own column and has no shared
`source` field that could imply they are one finding. They are never added, never merged,
and never summarised as a single claim.

`SourceLine` always renders in `MUTE`, never in the accent — provenance is not emphasis.

---

## 3. How the exact wording is preserved: the `value` / `bar` split

Every `value` is a **string printed verbatim**. Every bar is driven by a **separate**
numeric `bar` prop. They are deliberately not derived from one another:

- **`4 in 5` is never rendered as `80%`.** Its bar draws at 80, but the published form is
  the form that reaches the screen. Converting it would be altering the number.
- Nothing parses a displayed string. An earlier reel in this series shipped a bug where
  the house `num()` helper read the range `"4–13%"` as `413` and drew a bar nine times its
  own track; that class of bug cannot recur here.

---

## 4. Four refusals worth naming

**(a) No remainder is ever captioned.** `TblTrust`'s 26% leaves 74% of its track visibly
unfilled, and that remainder carries **no label**. `100 − 26` is arithmetic, not a
published figure. The reel does not print arithmetic as if it were data. (The same
discipline is why no "so 74% don't trust it" line appears in the narration.)

**(b) The earlier interview figure is never shown or implied.** Only the *change* was
supplied (+13 points in six months). `TblInterview` has **no `previous` prop**, draws no
earlier bar, and carries a **required** `deltaNote` that says on screen why: *"Only the
change was published — the earlier figure is not shown here because it wasn't supplied."*
Subtracting 13 from 63 to display "50% six months ago" would be inventing a data point.

**(c) The 41% is marked self-reported.** `TblInject` **requires** a `stamp`, rendered
against the figure. The supplied wording is that candidates *admit to* this; the reel
never upgrades that to observed behaviour, and B10 says so explicitly.

**(d) No fabricated resume content.** `TblInject`'s page shows generic headings
(`Experience`, `Education`, `Skills`) and a hidden layer labelled *"written for the
screening AI, not for a reader"*. **No invented candidate, employer, or actual injection
string is rendered** — showing a working prompt injection would be supplying a technique,
not illustrating a statistic.

---

## 5. What the reel does NOT claim (B10)

`TblLimits` requires both a `provenance` and a `falsifier`. On screen:

- that these figures measure one population — **they are separate studies**
- that self-reported behaviour is observed behaviour
- that AI is making worse hires — **none of these measure hire quality**

The provenance line lists **every** source rather than a representative one, precisely
because the failure mode here is six figures from five publishers being read as one
coherent dataset.

Falsifier: **"Different studies. Read them before you stack them."**

---

## 6. Framing claims vs measured claims

The narrative arc — hiring as a standoff, "neither side trusts the process", "the humans
are waiting to find out who decided" — is the human's own framing and is presented as
**argument**, not as a finding. B05 (`TblTable`) carries it, and that scene has **no
numeric prop at all**: it argues an arrangement, which is the only thing it is permitted
to argue.

---

## 7. Voice and identity

The narrator is Kokoro `af_bella`, introduced in B00's first breath as **"Bella, in for
Yatra"** and signed off the same way in B13, per IN-FOR-BEAR LAW in its Yatra form. The
footer chip stays `@Yatra` throughout.
