# Joining filed rounds to fund entry dates

**Runtime target:** 3:00 · **Spoken words:** ~475 · **Figures:** 5

Every number spoken below is read from `docs/_figdata_week9.json`, which is generated from the
database at build time. No figure in this deck carries a hand-typed value.

---

## [0:00] Opening — camera

Hi I'm Om Mali. This video is about joining two different SEC filings together, so that a
private company's funding round and the day a mutual fund actually bought into it can be lined
up against each other.

Up to now this project has worked from one form. N-PORT tells you what a fund's position in a
private company is worth at the end of a month. It never tells you when the fund bought it, or
what it paid. Two other filings do: Form D, which a company files when it sells shares, and the
restricted securities footnote in a fund's annual report. This week was about getting both in,
and joining them correctly.

## [0:35] Why the obvious join is wrong — `w9-nametrap.png`

The obvious way to find a company's Form D filings is to search for its name. I did that across
forty nine quarters and got seven hundred and six rows.

Five hundred and ninety five of them, about eighty four percent, are not the company. They're
feeder funds named after it, raising money to buy that company's shares on the secondary market.
The amount they sold is their own raise. Add those up, call it a funding round, and you've
published numbers no company ever filed.

So the join runs on an EDGAR identifier a person has confirmed, not on a name. The code
proposes; a human decides. That mattered: one filer from twenty fourteen normalises to exactly
the same string as xAI, and is a completely different company.

## [1:20] Five filers, five layouts — `w9-layouts.png`

The second source has no bulk dataset and no required format. The regulation says what must be
disclosed, not what the columns are called, so every fund family writes it differently. Four use
tables with different headings. One uses no table at all, putting the date and cost inside a
line of the portfolio listing.

So the parser reads each filer's header to work out which column is which, and a sixth filer
needs no new code. That got me two hundred and forty nine positions, two hundred and twenty
seven with a cost.

## [1:55] What that buys — `w9-entries.png` and `w9-exposure.png`

Two things the marks panel could not say before. Entry dates reaching back to January twenty
fifteen, nearly eight years before its first observation. And an exposure map: who holds what,
and how much of their fund it is, using each filer's own percentage.

## [2:20] The two sources agree — `w9-corroborate.png`

Then the part I didn't expect. With both joined, ten of eighteen fund acquisition dates fall on
the exact day a company reported selling shares.

The clearest case is Databricks, October twenty nineteen. The company filed saying it sold four
hundred million dollars of stock. Five separate fund managers independently name that same day.

The company files because it sold. The funds file because they own. Neither cites the other, so
the agreement is evidence, not arithmetic.

## [2:50] Close — camera

One caution: that denominator only counts purchases made while a company was still filing. Count
the rest and a real fifty six percent reads as thirty three. Thanks for watching.
