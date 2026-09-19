# Measuring how private marks move and propagate

**Runtime target:** 3:00 · **Spoken words:** ~470 · **Figures:** 5

Every number spoken below is read from `docs/_figdata_week8.json`, which is generated
from the marks panel. No figure in this deck is hand-typed.

---

## [0:00] Opening — camera

Hi I'm Om Mali. This video is about measuring how private company share prices
actually move, and how a new price spreads from one fund manager to the next.

The project derives per share prices for private AI companies out of SEC filings.
Mutual funds hold stakes in Anthropic, OpenAI, Databricks, SpaceX and others, and
they report a value and a share count every month. Divide one by the other and you
get a price. Up to now the work was building that panel. This week I stopped
building it and started measuring it. Five thousand four hundred and seventy nine
marks, four questions.

## [0:30] How often does a price actually change? — `w8-remark.png`

First question: how often does a mark just get carried forward unchanged? The plan
expected thirty to forty percent. The measured number is twenty five.

And this is not an artifact of where I drew the line. I widened the test three
ways — exactly equal, any move under a tenth of a percent, any move under one
percent — and even the most generous reading stays below the plan's band. Private
marks move more than the plan assumed they would.

## [1:00] The headline rate hides almost everything — `w8-bycompany.png`

The second thing the measurement showed is that one number across the whole panel
would have been true and useless. Split by company, the same statistic runs from
one percent unchanged for OpenAI to forty eight percent for X.AI. Anthropic and
OpenAI are repriced at nearly every observation. X.AI and SpaceX get carried
forward a third to a half of the time. Same panel, same rule, completely different
behaviour.

## [1:30] Do two managers agree on the same date? — `w8-dispersion.png`

Third question: when two managers price the same company on the same date, do they
agree? Mostly not. Across one hundred and thirty same date groups, the median
spread between the highest and lowest price is just under eleven percent. Ninety
two of those groups hold more than one distinct price level. Disagreement is the
normal state here, not the exception.

## [2:05] Is that disagreement, or a round arriving? — `w8-window.png`

That raises an obvious objection: maybe those gaps are just timing. A new round
lands, and some managers have picked it up and others have not. So I opened one
window and looked. Anthropic preferred stock, across two consecutive period ends.
Eight managers, eleven marks, running from one forty one up to two sixty two. You
can see the old level, you can see the new level, and you can see managers crossing
from one to the other. That is a round arriving, one manager at a time.

## [2:35] How fast does a new level travel? — `w8-propagation.png`

Which is the last question. I took every price that three or more managers adopted,
thirty seven of them, and measured how long it took to reach half its holders.
Median, thirty days. Fifteen of the thirty seven get there on the very same period
end. The slowest takes ninety two days.

## [2:50] Close — camera

Every one of those numbers runs behind a guard: no blocked mark, no incomplete run,
no unadjudicated split. And the report states plainly what none of it shows — these
are fund marks, not transactions. Thanks for watching.
