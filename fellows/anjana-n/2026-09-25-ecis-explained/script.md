# ECIS Episode 8 — Reading Between the Lines

**Skill:** ai-explainer
**Voice:** af_bella (Anjana) — source `beats.json` says `am_onyx`; overridden per
the series convention set in Episode 1 (Anjana narrates, no channel handle)
**Target length:** ~3:20 (16:9 master) / ~2:40 (9:16 short)
**Register:** Teardown
**Series:** Sequel to Episodes 1–7. Episode 7 taught the system to look
sideways — at consensus, at peers, at the sector. Episode 8 turns it back on
the transcript itself and asks not what management said but *how* they said it,
then asks whether the market had already figured it out.

---

## Beat 0 — The Ask (cold open)

**Pattern:** `ClaudeComposerAsk` · **Duration:** ~13s

**Narration:**

Seven episodes in, ECIS could read a transcript, weigh it against consensus,
and check it against the sector. It was still only reading the words. I'm
Anjana — this week it starts reading the delivery.

**Composer ask:**

> ECIS extracts what management said. But how they said it carries information
> too — hedging, complexity, a change in tone. And some of what a signal
> "predicts" may already be in the price. Can the system see either of those?

**Output lines (resolved on screen):**
- language style as a prediction feature
- signals weighted by how much the stock actually moved
- drift check: was it already priced in?

---

## Beat 1 — Recap

**Duration:** ~20s brief / ~22s actual

**Narration:**

Hello, Anjana here. Quick recap. ECIS reads earnings call transcripts through
four independent readers, triangulates their outputs into a single
confidence-scored signal, pre-registers that signal, and grades itself against
actual stock movement thirty days later. Last episode, the system added
consensus comparison and cross-company correlation. This week, it learns to
read between the lines.

**Visual direction:**

The now-familiar pipeline builds fast — transcript, four readers in parallel,
arrows converging on the triangulator, a "raised, 0.82" badge, the gold
prediction node, and Episode 7's consensus delta and correlation map flashing
past on their way to the 30-day market check. Then everything recedes and a
gold magnifying glass travels back over the transcript. Inside the lens the
plain text resolves into something else: hedging phrases and tone markers
lighting up in the body of the sentences. The label lands: reading between the
lines.

---

## Beat 2 — Linguistic Analytics

**Duration:** ~12s brief / ~24s actual

**Narration:**

Until now, the system extracted what management said. Now it analyzes how they
said it. A readability scorer tracks whether language complexity spikes before
guidance changes. A hedging index measures the ratio of phrases to
definitive statements. And a tone shift detector compares sentiment
distributions across consecutive quarters. When the way a company talks
changes, something is usually about to change in the numbers too.

**Visual direction:**

Three instruments stack down the left. A readability gauge runs simple to
complex and its needle swings well toward complex. A hedging gauge runs
definitive to hedging and settles in the middle. Below them, two sentiment
distributions side by side — last quarter mostly neutral, this quarter leaning
positive — with the delta called out between them. Each instrument sends a line
to the right, where three cells fill a small gold vector labelled linguistic
features, and that vector feeds the prediction node from Episode 6.

---

## Beat 3 — Market Impact

**Duration:** ~12s brief / ~28s actual

**Narration:**

A correct signal is not always a useful signal. The system now measures
reaction magnitude: how much the stock actually moved after the call. A raised
guidance signal followed by a twelve percent excess return is a stronger
confirmation than one followed by half a percent. It also tracks reaction
timing: did the market price it in on the same day, or did it take two weeks?
And it flags abnormal volume spikes, showing whether traders treated the
guidance change as material new information.

**Visual direction:**

Three measurements, top to bottom. Two bars for magnitude: a thin faint one at
half a percent beside a thick bright one at twelve — same verdict, different
weight. A four-segment timeline for timing, filled up to a glowing marker
sitting in "1–3 days". And ten days of trading volume as a bar chart with a
dashed trailing-average line running through it, where the call-day bar shoots
three times higher than the rest.

---

## Beat 4 — Pre-Signal Drift

**Duration:** ~10s brief / ~21s actual

**Narration:**

Here is the critical question. If the stock already moved five percent in the
same direction before the earnings call, the market may have already known. The
system now measures pre-signal drift: the excess return in the five and ten
trading days before the call. High drift in the same direction as the extracted
signal means the information was likely already priced in.

**Visual direction:**

A price line draws left to right across thirty days with a red dashed vertical
marking the earnings call. The ten days before the call shade amber, and the
line is already climbing inside that shading — plus five percent, labelled
"already moving". After the call it keeps climbing, plus three percent, labelled
"signal confirmed" in green. Then the badge slides up underneath and sits there:
correct, but already priced in.

---

## Beat 5 — Infrastructure Upgrade

**Duration:** ~12s brief / ~31s actual

**Narration:**

The data layer outgrew its original infrastructure. The system migrated from
SQLite to PostgreSQL with connection pooling and composite indexes on the most
frequent query patterns. Time-series market data moved into a TimescaleDB
hypertable with automatic partitioning. The outcome resolver now reads from a
local database instead of making live API calls for previously resolved dates.
Materialized views pre-compute the heaviest dashboard aggregations, so the
dashboard loads from cached results instead of recomputing on every page
refresh.

**Visual direction:**

A small dim SQLite box on the left. Gold particles stream out of it along a
migration arrow and arrive on the right, where a taller stack builds one layer
at a time: signals and outcomes in blue, a TimescaleDB hypertable in teal with
its partition slices, materialized views in green. Underneath, the query time
strikes through from 2.3 seconds in red to 0.1 in green, and a thin schema
version bar runs along the bottom with its markers: v1, v2, v3.

---

## Beat 6 — Close

**Duration:** ~7s brief / ~13s actual

**Narration:**

Linguistic profiling. Impact-weighted scoring. Pre-signal drift detection. And
a production-grade data layer underneath. The system now reads how management
talks, not just what they say.

**Visual direction:**

The whole architecture at once, with this episode's three additions glowing
gold in the order the video introduced them: the linguistic gauges clipped onto
the transcript stage, the impact charts hanging off the scoring stage, and the
Postgres stack standing where the old database icon used to be. They settle,
and the episode title rises underneath.

---

## Beat 7 — Verdict

**Pattern:** `ClaudeVerdictArtifact` · **Duration:** ~26s

**Narration:**

Let's recap with Claude. Style is now a feature — complexity, hedging and tone
shift all feed the prediction model alongside the numbers. Outcomes are no
longer just right or wrong: a signal followed by a twelve percent move counts
for more than one followed by half a percent. Drift is measured before the
call, so a signal the market had already priced in is not mistaken for
foresight. And the whole thing now sits on a data layer that can carry it.

**Artifact lines:**
- Readability, hedging and tone shift are extracted as features — *how* it was
  said, not just what.
- Outcomes are weighted by reaction magnitude, timing and abnormal volume.
- Pre-signal drift is measured over the 5 and 10 days before the call.
- The data layer moved to PostgreSQL, with TimescaleDB for market series and
  materialized views for the dashboard.

---

## Beat 8 — Your Turn

**Pattern:** `ClaudeComposerAsk` · **Duration:** ~35s

**Narration:**

Your turn. Take something you judge from what people write or say — reports,
updates, reviews, applications. Ask what the delivery is telling you that the
content isn't, whether the outcomes you count should all count the same, and
whether the thing you think you spotted was already obvious to everyone else
before you spotted it.

**Composer ask:**

> I make judgment calls from things people write or say — status updates,
> reports, reviews, applications. Can you help me: one, name what I could
> measure about *how* something is written that might predict what happens
> next, rather than what it says; two, work out whether all my outcomes should
> count equally, or whether some should be weighted by how much actually
> changed afterwards; and three, tell me honestly how I'd check whether a
> pattern I think I spotted early was already obvious to everyone else before I
> spotted it?

---

## Beat 9 — Title outro

**Pattern:** `ClaudeTitleOutro` · **Duration:** ~5s

**Narration:**

Anjana here, thanks for watching.

**Title:** ECIS — Episode 8
**Subline:** reading between the lines · episode eight
**Handle:** (none)
