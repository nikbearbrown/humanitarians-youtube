# ECIS Episode 6 — From Reading to Predicting

**Skill:** ai-explainer
**Voice:** af_bella (Anjana) — source files say `am_onyx`; overridden per the
series convention set in Episode 1 (Anjana narrates, no channel handle)
**Target length:** ~4:20 (16:9 master) / ~2:45 (9:16 short)
**Register:** Teardown
**Series:** Sequel to Episodes 1–5. The system now predicts next-quarter
guidance direction before the earnings call happens, using features built
entirely from its own signal history.

---

## Beat 0 — The Ask (cold open)

**Pattern:** `ClaudeComposerAsk` · **Duration:** ~12s

**Narration:**

Five episodes in, ECIS could read an earnings call and grade itself on what it
read. This week it stopped waiting for the call. I'm Anjana — here's how a
system that only ever looked backward started looking forward.

**Composer ask:**

> Last time, ECIS fine-tuned on its own mistakes and gave every signal a shelf
> life. This week you built a model that predicts what a company will say
> before the earnings call even happens. Can you show me how that works?

**Output lines (resolved on screen):**
- features built from its own decision log
- predictions locked before the call
- two scorecards, graded independently

---

## Beat 1 — What ECIS Is

**Duration:** ~20s brief / ~40s actual

**Narration:**

ECIS is a system that reads earnings call transcripts and extracts financial
guidance signals automatically. It runs four independent readers on every chunk
of every transcript: keyword matching, FinBERT sentiment analysis, named entity
recognition, and a large language model. A triangulator fuses their outputs.
Every signal is pre-registered before anyone knows the outcome, then graded
against the market at thirty, ninety, and one hundred eighty days. The system
does not trust any single reader or any single confidence number. It
triangulates, scores, and self-corrects. That is the foundation. Here is what
comes next.

**Visual direction:**

The same left-to-right pipeline build as Episode 5's recap — transcript, four
reader nodes lighting in narration order, the triangulator, the padlocked log,
the 30/90/180 grading timeline. The difference lands on the last two lines: on
"That is the foundation" the whole architecture settles into a compact overview
on the LEFT half of the frame, and on "Here is what comes next" an empty region
opens on the RIGHT, separated by a subtle dotted border. The extraction pipeline
is the past. The right side is the future. That spatial split is the visual
language for the rest of the episode.

---

## Beat 2 — The Feature Vector

**Duration:** ~15s brief / ~38s actual

**Narration:**

Until now, ECIS read the past. Transcripts came in, signals went out. But the
signal history itself contains patterns. What direction did Company A report
last quarter? How many consecutive quarters has it raised? Has the stock
already moved before the call? What are peer companies saying this quarter?
These are features, and they are all computed from data the system already
has. No new sources. No new APIs. Just the decision log it has been building
all along. A logistic regression model takes these features and predicts where
guidance will go next quarter, before the CEO opens their mouth.

**Visual direction:**

The append-only log glows on the left, full of history — Company A raising
three quarters running, Company B maintaining then lowering, Company C lowering
then maintaining. From the log, six features pull themselves out and line up in
the future region on the right, each in its own labelled box: prior direction,
trend length, stock momentum, sector aggregate, days since last call, prior
confidence. The boxes snap into a single feature-vector strip with a gold
border — gold is the prediction color, distinct from extraction blue. The strip
feeds a deliberately simple node labelled "Logistic Regression," which outputs a
gold prediction card: raised, 0.73.

**Label:** No new data. Just the patterns in what it already knows.

---

## Beat 3 — Pre-Registered Predictions

**Duration:** ~12s brief / ~34s actual

**Narration:**

The prediction follows the same honesty rules as every extraction. It is
logged before the earnings call happens. Ticker, predicted direction,
confidence, the full feature vector snapshot, model version, and timestamp.
Locked. Append-only. After the call, the transcript is extracted and the actual
guidance direction is known. Only then does the scorecard grade the
prediction. Did the model get it right? The prediction cannot be revised,
softened, or deleted after the fact. The same discipline that governs
extraction now governs forecasting.

**Visual direction:**

A gold prediction record card lands — Company A, raised, 0.73, a collapsed row
of feature icons, model v1.0, a timestamp — and a padlock stamps onto it. A
timeline runs right from the locked card toward a future marker, "Earnings
call," with days visibly ticking past in the empty space between. The marker
arrives, a transcript appears, the extraction pipeline flashes compactly, and a
blue actual-result card lands beside the gold prediction: predicted raised,
actual raised. A green checkmark stamps between them.

**Label:** Predicted before. Graded after. No edits.

---

## Beat 4 — Two-Level Grading

**Duration:** ~12s brief / ~40s actual

**Narration:**

Now there are two scorecards asking two different questions. Level one. Did
the prediction model correctly forecast what the company would say? Predicted
raised, actual raised, correct. Predicted maintained, actual lowered, wrong.
This grades the prediction against the extraction. Level two. Did the
extracted guidance correctly predict stock performance? Raised guidance, stock
outperformed, correct. This grades the extraction against the market. Two
levels. The prediction predicts the guidance. The guidance predicts the stock.
Each level is graded independently. A prediction can be right about what the
CEO said and still wrong about what the market did.

**Visual direction:**

A two-tier diagram builds top to bottom. Level 1: a gold prediction card and a
blue extraction card, arrow between them, green check — "Did we predict the
guidance?" Level 2: the same blue extraction card and a white market-outcome
card reading "+3.2% excess return," arrow, green check — "Did the guidance
predict the stock?" A vertical line links the extraction card across both
tiers so the chain reads prediction → guidance → market. Then the divergence
case: Level 1 stays green, Level 2 flips to "-1.4%" with a red X. Right about
the words, wrong about the money.

**Label:** Two questions. Two scorecards. Both honest.

---

## Beat 5 — The Forecast View

**Duration:** ~8s brief / ~24s actual

**Narration:**

The dashboard now has a forecast view. For every company with an upcoming
earnings call, you see the predicted direction, the confidence, which features
drove the prediction, and whether it agrees or disagrees with what the rest of
the sector is saying. A timeline shows how accurate past predictions were for
that company. One screen to see what the system expects before the call
happens.

**Visual direction:**

Three gold-bordered forecast cards in a row — Company A predicted raised at
0.73 driven by three consecutive raises and agreeing with its sector; Company B
predicted maintained at 0.68 on a mixed sector signal; Company C predicted
lowered at 0.61 on stock momentum of -6%, disagreeing with its sector. Below
them, Company A's prediction timeline: Q1 right, Q2 right, Q3 wrong, and an
open, unfilled Q4 dot — the prediction still waiting on its call.

---

## Beat 6 — Close

**Duration:** ~5s

**Narration:**

From extraction to prediction. The system that read the past now forecasts
the future. ECIS, episode six.

**Visual direction:**

A left-to-right arc: the compact extraction pipeline labelled "The Past," the
glowing decision log in the center labelled "The Bridge," the prediction model
and a gold forecast card on the right labelled "The Future." An arrow flows
through all three. On "episode six" all three pulse together, then fade, and
the title lands: ECIS — Episode 6.

---

## Beat 7 — The Verdict

**Pattern:** `ClaudeVerdictArtifact` · **Duration:** ~24s

**Narration:**

Let's recap with Claude. The features come entirely from the decision log the
system was already keeping — no new sources, no new APIs. A logistic regression
model turns them into a prediction, and that prediction is locked before the
call, exactly the way every extraction always was. Then two scorecards grade
two different things: whether the model predicted the guidance, and whether the
guidance predicted the stock. The system that read the past is now forecasting
the future, and it's grading itself on both.

---

## Beat 8 — Your Turn (handoff)

**Pattern:** `ClaudeComposerAsk` · **Duration:** ~45s

**Narration:**

Your turn. "I keep a record of decisions I've made and how they turned out —
a log, a spreadsheet, a journal, anything with a history in it. Can you help
me: one, name three patterns in that history that might predict my next
decision before I make it, using only what's already in the log; two, tell me
which of those patterns I could actually check against a real outcome later,
and which are just vibes; and three, ask me honestly whether I'd be willing to
write down my prediction before the outcome, so I can't quietly revise it
afterward?" Paste that into Claude and find out whether your own history is
predictable — and whether you'd let it be graded.

**Why this prompt:** it takes the episode's two hard moves — features from the
log you already have, and pre-registration you can't edit — and points them at
the viewer's own records. The third clause is the honest one: most people are
happy to predict and much less happy to be graded.

---

## Beat 9 — Outro

**Pattern:** `ClaudeTitleOutro` · **Duration:** ~5s

**Narration:**

From reading the past to forecasting the future. That's Anjana.

---

## Production Notes

**Total estimated duration:** ~4:20 (16:9). The body beats run long against
their briefs because the source narration is dense; kept verbatim per the
series convention, with the evidence carried on screen.

**Voice:** `af_bella` (Anjana). The source `beats.json` and `README.md` say
`am_onyx`; every prior ECIS episode overrode this to Anjana's own voice.

**Color law for this episode:** gold (#D4A853) is the prediction color and
appears only on prediction cards, the feature vector, the model node, and the
forecast view. Extraction stays blue, the market outcome is white. The
past/future spatial split from Beat 1 — extraction left, prediction right —
holds through Beats 2 and 6.

**Delivery:** rendered at 4K in both 16:9 (3840×2160) and 9:16 (2160×3840).

**Scope note:** the model type (logistic regression), the six features, the
pre-registration record fields, and the two-level scorecard are claims about
the real system and come from the pre-authored narration and briefs in this
folder. The confidences (0.73 / 0.68 / 0.61), the market returns (+3.2% /
-1.4%), the momentum figures, and the dates are illustrative placeholders for
Company A / B / C. See `PEDAGOGY.md`. No real company names or tickers anywhere.
