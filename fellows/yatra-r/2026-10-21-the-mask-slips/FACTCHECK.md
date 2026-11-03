# FACTCHECK — The Mask Slips.

`yatra-the-mask-slips` · @Yatra · narrated by Kokoro `af_bella` ("Bella"), in for Yatra

---

## The standing instruction

> "Please don't invent additional numbers or details beyond what I've given you."
> — plus: paraphrase rather than quote, and cite sources on screen.

Everything below is enforced **structurally**, in the component types, not by discipline.

---

## 1. The complete list of supplied figures

**One source supplies every figure in this reel: Garbage Day, October 2026.**

| Figure | Rendered as | Beat |
|---|---|---|
| went viral 2 days after creation | `2 days` | B02 |
| 26,000 followers | `26,000` | B02 |
| 2.2 million likes | `2.2 million` | B02 |
| reportedly $13,700 from a single video | `$13,700` + `reported` chip | B03 |
| one early account lost ~50% engagement after being identified as AI | `roughly 50%` | B07 |
| another AI persona saw the same drop | `the same drop` | B07 |

**No other number appears anywhere in this reel**, on screen or in narration.

### How citation is enforced

Every scene that renders a figure **requires** a `source` string:
`MskSpike`, `MskMoney` and `MskDrop` cannot be constructed without one. A number cannot
reach the screen uncited, because the type will not permit it. `SourceLine` always renders
in `MUTE` and never in the accent — a citation is provenance, not emphasis.

### How the exact wording is preserved

Every `value` is typed as a **string printed verbatim**, never a number formatted at
render time. Consequences, all deliberate:

- `$13,700` is never reformatted, rounded or converted.
- `2.2 million` is never expanded to `2,200,000`.
- **`roughly 50%` keeps its hedge.** The supplied figure is approximate and the screen
  says so; it is never rendered as a clean `50%`.
- **`the same drop` is not a number at all**, and must not be coerced into one. It is the
  second case's `value`, printed exactly as the human described it.

Any bar length comes from a **separate** numeric prop, so no code path ever parses a
displayed string. (An earlier reel in this series shipped a bug where the house `num()`
helper read a range as a four-digit number and drew a bar nine times its own track.
Nothing here can repeat it.)

---

## 2. The two hedges, and why they render where they do

**"Reported", not audited.** `MskMoney` **requires** a `stamp`, and renders it hard
against the figure rather than in a footnote — anyone who sees `$13,700` sees `REPORTED`
in the same glance. The narration carries the same word, and the verdict card repeats
"Reported, not audited."

**"Roughly" 50%.** Rendered as supplied. The reel never states a precise engagement
figure because none was supplied.

---

## 3. Neither account is named — and cannot be

The human described the two accounts and named neither:

- "one of the earliest popular AI influencer accounts"
- "another AI persona"

Those descriptions are rendered verbatim as each case's `label`. **There is no `name`,
`handle`, `account` or `platform` prop anywhere in `MaskSlips.tsx`**, so no identification
can be made even by accident. The reel also never names the platform any of this happened
on, because that was not supplied either.

---

## 4. The one beat that could have invented data, and what stops it

**B05 (`MskArc`)** draws the rise-and-fall curve. A curve is an invitation to imply
magnitudes, so:

- the type has **no numeric prop at all**;
- the axis carries **no ticks and no scale**;
- an `axisNote` is **required** and renders on screen — *"Shape only — this curve carries
  no figures."*

It argues shape, which is all it is permitted to argue. The accent marks the
identification point, because the beat's claim is that the fall has a *cause*, not a rate.

---

## 5. Claims traced to source

| Claim | Where it comes from |
|---|---|
| an AI influencer account went viral 2 days after creation | supplied (Garbage Day, Oct 2026) |
| it reached 26,000 followers and 2.2 million likes | supplied, same |
| it reportedly earned $13,700 from a single video | supplied, same, with the hedge |
| an early AI influencer account lost ~50% engagement after identification | supplied, same |
| another AI persona saw the same drop | supplied, same |
| audiences "turn" rather than drift | the human's own narrative framing, presented as argument, not as a finding |
| authenticity is the lesson for marketers | the human's own conclusion, presented as such |

The last two are the human's stated narrative arc. They are rendered as **argument** — B08
reaches its conclusion by visibly ruling out alternatives rather than asserting a measured
result, and the verdict card frames the lesson as a lesson, not a finding.

---

## 6. The falsifiability beat (B09)

`MskLimits` **requires** both a `provenance` and a `falsifier` string. What it declines to
claim, on screen:

- that this is measured across the category — it's a handful of accounts
- that the money figure is audited — it is reported
- that AI content can't work — only that *undisclosed* AI content has a cliff

Provenance line: *"Every figure in this video comes from one report: Garbage Day, October
2026. No other numbers are claimed."*

Falsifier: **"Check the accounts yourself before you believe the pattern."**

---

## 7. Voice and identity

The narrator is Kokoro `af_bella`, introduced in B00's first breath as **"Bella, in for
Yatra"** and signed off the same way in B12, per IN-FOR-BEAR LAW in its Yatra form. The
footer chip stays `@Yatra` throughout.
