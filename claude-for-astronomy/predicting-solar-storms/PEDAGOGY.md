/ PEDAGOGY — *The Same Sunspot, Twice.*

**GATE P.** A human reads the narration below and signs. Audio is not
generated until the verdict line below is changed from PENDING to a pass.
Kokoro is local and free, so this gate protects quality, never spend.

> Note for anyone editing this file: `generate_audio_kokoro.py` opens GATE P on
> a plain substring match anywhere in this document, so do **not** write the
> passing verdict string in prose — spelling it out in an explanatory sentence
> silently unlocks the gate. That is why this paragraph describes it instead of
> quoting it.

**VERDICT: PASSED**

Signed: Om Mali  Date: 10/09/2026

---

## Written to a length

| | words | predicted | measured |
|---|---|---|---|
| Ep. 09 | 436 | 2:39.2 | 2:43.6 |
| Ep. 10 | 429 | 2:41.0 | 2:27.7 |
| Ep. 11 | 419 | 2:24.3 | 2:29.0 |
| **Ep. 12** | **400** | **2:22.2** | — |

Margin ~38 s. The words-only model is noise of order ±5–10% **with no
consistent sign** — Ep. 06 +10.4%, Ep. 07 −0.4%, Ep. 08 −5.0%, Ep. 09 +2.7%,
Ep. 10 −8.2%, Ep. 11 +3.3%. The rate used is Ep. 11's measured 0.3556 s/word.
Even at the slowest rate in the series this lands at 2:30. If the measured
total somehow exceeds 3:00 the fix is `--speed`, not a rewrite of signed
narration.

## What this episode teaches, and why it is worth an episode

Topic 12 in the brief is "ML models forecasting solar flares that threaten
satellites and power grids". The obvious version is a capability story: the
Sun is dangerous, the data is huge, here comes the classifier, look at the
skill score. That version is true and it is also the thing most likely to
mislead.

The interesting thing is that **this is the first episode about the
evaluation rather than the system.** Every earlier limit lived in the model,
the data or the objective. Here all three can be fine and the number still be
wrong, because of how the test set was built. It is the earliest possible
failure — it happens before deployment is even a question — and it is the one
that decides whether anything else gets believed.

The mechanism is specific and ordinary. A sunspot region is measured every
hour for days, so one region contributes dozens of rows that barely differ.
Whether a region flares is a property *of the region*: a few complex ones
flare repeatedly, most never produce an M-class flare at all. Shuffle those
rows before splitting and the same region lands on both sides. A model with
enough capacity then recognises the region instead of forecasting the flare,
and the score you report is partly a memory test.

So I built it and measured it. 350 simulated active regions, hourly, a base
rate of 1 in 58 to match the published imbalance, two models chosen to differ
on capacity, three ways of splitting, twelve repeats, medians throughout.

- Under a **random row split**, every single region in the test set is also
  in the training set — **100%**. Under a by-region split, **0%**.
- The leak is measurable directly: the median distance from a test row to its
  nearest training row is **0.13** after shuffling and **0.38** when regions
  are kept apart.
- Under the random split the flexible model **wins**: **0.48** against the
  plain model's **0.36**. That is the headline you would publish.
- Split by region and the ordering **reverses**: the plain model does not move
  (0.36 → 0.37) and the flexible one falls to **0.12**. **Three quarters of
  its score was the split.**
- And it is the memorising that does it: remove the region's fingerprint from
  the features and the inflation goes from **+0.31 to exactly zero**.

The payoff is a fix that costs nothing. Split by region, not by row. One line.

The series pivot is stated at B01: eleven episodes asking whether the AI
works; this one is about how we checked.

## The narration, beat by beat

**B00 — cold open** (32 words)
> Hi, I'm Om Mali. This video is about forecasting the solar storms that
> knock satellites out of orbit, and why the score on the forecast is usually
> too good to be true.

**B01 — presenter** (21 words)
> Eleven episodes of AI in space. This one is about the number we use to
> decide whether any of it works.

**B02 — the whole idea in one breath** (31 words)
> Here is the whole idea. A sunspot region is measured every hour for days. If
> you shuffle those measurements before splitting them, the model gets tested
> on regions it already memorised.

**B03 — the stakes** (39 words)
> February twenty twenty-two. SpaceX launched forty-nine Starlink satellites
> into a moderate geomagnetic storm. The air thickened, drag rose, and
> thirty-eight of them came back down within days. A moderate storm. This is
> the thing we are trying to forecast.

**B04 — the shape of the data** (32 words)
> So here is the data. Each row is one active region, measured every hour for
> days. One region is dozens of rows that barely change. A few regions do all
> the flaring.

**B05 — the split** (25 words)
> Now split it for testing. Shuffle the rows, and every region lands on both
> sides, all of them. Split by region instead, and none do.

**B06 — the leak, measured** (34 words)
> You can measure the leak directly. For each test row, find the closest row
> the model trained on. After shuffling, it is nearly always the same region,
> an hour earlier. Almost the same numbers.

**B07 — the headline** (32 words)
> So, two models. A plain one, and a flexible one. Shuffle the rows and the
> flexible model wins: point four eight against point three six. That is the
> headline you would publish.

**B08 — the reversal** (29 words)
> Now split by region. The plain model does not move. The flexible one falls
> to point one two. Three quarters of its score was the split, not the Sun.

**B09 — twelve runs** (23 words)
> Twelve runs, same story every time. The plain model sits where it always
> sat. The flexible one is down here, every single run.

**B10 — the design tell** (34 words)
> And it is the memorising that does it. Strip the region's fingerprint out of
> the measurements and the gap goes to zero. So the fix is one line: split by
> region, not by row.

**B11 — verdict** (25 words)
> So: the model was never the problem. The split was. Ask how the test set was
> built before you believe any score, including your own.

**B12 — your turn** (32 words)
> Your turn. Read it. Here is how I split my data. Tell me what could appear
> on both sides, and what my score would look like if I split it properly
> instead.

**B13 — outro** (11 words)
> The Same Sunspot, Twice. Humanitarians AI. AI in Astronomy, episode twelve.

## Things a reader should push back on

Seven judgement calls, so the signer can overrule me rather than discover them:

1. **The centrepiece is a simulation, and the narration says "I built it" in
   the first person.** That is accurate, but a viewer could hear B04–B10 as a
   measurement of real flare data. Every one of those beats carries "computed
   in this reel" on its citation line. If you want the voice to say "I
   simulated it", that is a one-word change.
2. **The flexible model is a 25-nearest-neighbour, which nobody ships for
   flare forecasting.** I chose it because capacity is the variable that
   matters and kNN makes it legible — it answers by finding the most similar
   row, which is literally the leak. A random forest or a CNN would be more
   realistic and would hide the mechanism. The episode never says kNN; it
   says "a flexible one". A structures-minded viewer may still object that
   the demonstration is rigged toward memorisation. It is *designed* to be
   legible; the direction of the effect is what is claimed.
3. **The plain model winning is an artefact of my simulation, not a law.**
   In my generator the usable signal is close to linear, so logistic
   regression is near-optimal. On real data a flexible model may genuinely be
   better *and* still be inflated. The reel's claim is about the inflation,
   not about which model to use — but B08's picture does show the simple
   model winning, and a viewer could take the wrong lesson.
4. **"Three quarters of its score was the split"** is a median over twelve
   runs on one synthetic design. It is not a number that transfers to any
   real dataset, and the reel does not say it does.
5. **The episode does not name a single paper as affected.** That is
   deliberate — I have no evidence about which published results used which
   split, and the literature itself says the practice is inconsistent. But it
   means the voice says "the literature says this happens" without naming
   anyone, which asks for trust.
6. **"38 of 49" contradicts what most people remember.** SpaceX said up to 40
   and the press repeated it; the peer-reviewed and NASA figure is 38. A
   viewer who looks it up will find the 40 first. I think the primary number
   is the right one; it is worth knowing you will get mail about it.
7. **The chronological split is mentioned nowhere in the voice.** I measured
   it (plain 0.32, flexible 0.13 — it behaves like the honest split) and it
   is in FACTCHECK, but the narration only contrasts two splits. Adding a
   third would cost a beat and blur the fix.

## What the visuals do that the words do not

Shown and never spoken: the ring travelling to one track and the counter
running its 58 rows; the "1 flare row in 58" chip; both nearest-neighbour
numbers, 0.13 and 0.38; the "+0.13" bracket; the "rows shuffled" chip; the
plain model's 0.36 → 0.37; all twelve points in each column of B09; the
chronological column nowhere; the fingerprint sweep's whole curve, not just
its ends. **A viewer who only listens gets the argument; a viewer who watches
gets the receipts.**

## Audience check — `claude-hai` is for STUDENTS

The channel's spine question is when to use AI and when not to. This episode
answers with the case that precedes all the others: **you cannot decide
whether to use a model until you can trust the number that says it works.**

The transferable skill is one question a student can ask of any result,
including their own: *what repeats in my data, and could it be on both sides
of my split?* The patient. The user. The sensor. The active region. It costs
nothing to check and it is the single most common way a good-looking result
turns out to be a memory test.

No jargon before it is earned. "Data leakage", "temporal coherence", "True
Skill Statistic", "class imbalance" and "active region" appear nowhere in the
narration — the pictures carry those ideas and the citation lines name them
for anyone who wants to look them up. The voice says "sunspot region",
"shuffle", "split", "score" and "memorised".
