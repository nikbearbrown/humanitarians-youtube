# ECIS Episode 5 — The System That Learned From Its Own Mistakes

**Skill:** ai-explainer
**Voice:** af_bella (Anjana) — source files say `am_onyx`; overridden per the
series convention set in Episode 1 (Anjana narrates, no channel handle)
**Target length:** ~4:40 (16:9 master) / ~2:45 (9:16 short)
**Register:** Teardown
**Series:** Sequel to Episodes 1–4. The system reviewed its own errors,
fine-tuned on the hardest boundary, added spread-scaled penalties, three new
detection layers, and signal decay tracking.

---

## Beat 0 — The Ask (cold open)

**Pattern:** `ClaudeComposerAsk` · **Duration:** ~12s

**Narration:**

Four episodes in, ECIS could read an earnings call. This week it did something
harder — it read its own mistakes. I'm Anjana. Here's what the system learned
about itself.

**Composer ask:**

> Last time, ECIS weighted every signal by who said it and how clean the source
> was. This week you went back through its errors and retrained on the one
> boundary it kept getting wrong. Can you show me what changed?

**Output lines (resolved on screen):**
- fine-tuned on its own corrections
- penalties that scale with disagreement
- every signal now has a shelf life

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
triangulates, scores, and self-corrects. That is the foundation. Here is what it
learned this week.

**Visual direction:**

The architecture builds left to right in sync with the narration. A transcript
document enters from the left and splits into chunks. The chunks flow into four
reader nodes stacked vertically — Keyword (blue), FinBERT (teal), NER (orange),
LLM (purple) — each lighting up as it is named. Arrows converge into the
Triangulator on the right; one signal exits carrying a direction and a
confidence badge. The signal drops into an append-only log and a padlock stamps
onto it. A timeline extends right with three checkpoints — 30, 90, 180 days —
and each gets graded. On "That is the foundation" the whole architecture settles
into a compact overview.

---

## Beat 2 — Fine-Tuning

**Duration:** ~15s brief / ~36s actual

**Narration:**

The hardest call in the pipeline was the line between maintained and none. The
system kept confusing "we are comfortable with our outlook" with "we remain
focused on execution." One is guidance reaffirmed. The other is not guidance at
all. So human-reviewed extractions were formatted into training data,
concentrated on that exact boundary. A QLoRA adapter was trained on top of the
base eight billion parameter model. Rank sixteen adapters, four-bit
quantization, five epochs. The adapter does not replace the model. It sharpens
the one edge where it was weakest.

**Visual direction:**

Two quote cards sit side by side — "We are comfortable with our current
outlook." tagged MAINTAINED in blue, and "We remain focused on execution."
tagged NONE in grey. A red decision-boundary zone pulses between them, littered
with red X marks: past misclassifications. The cards shrink into a stream of
training examples flowing into the base model from below, with a counter
reading "200+ reviewed extractions." A small rectangular QLoRA adapter block
glows beside the much larger base model, labelled "Rank 16 · 4-bit · 5 epochs" —
deliberately small, because it is a targeted refinement, not a retrain. The
adapter locks into the model's side, both quotes are re-read and tagged
correctly, and the red X marks in the boundary zone clear to green checkmarks.

**Label:** Same model. Sharper edge.

---

## Beat 3 — Smarter Penalties

**Duration:** ~12s brief / ~42s actual

**Narration:**

Self-consistency runs the same prompt three times and votes. Before, a
two-to-one vote always got the same flat penalty. But a close disagreement is
not the same as a wide one. Now the penalty scales with the spread. If the
majority says zero point eight and the minority says zero point seven five, the
penalty is small. If the majority says zero point eight and the minority says
zero point two, the penalty is large. And on top of that, where the signal came
from matters. Prepared remarks carry full weight. Q&A carries zero point eight.
Rehearsed language is more reliable than spontaneous answers.

**Visual direction:**

Two vote panels sit side by side, each showing three extraction passes. The
close vote reads maintained 0.80, maintained 0.78, raised 0.75 — a "2/3 agree"
tag, a small spread, a thin arrow nudging confidence 0.80 → 0.77, green border.
The wide vote reads maintained 0.80, maintained 0.82, raised 0.20 — the same
"2/3 agree" tag, a huge spread, a thick arrow pushing 0.80 → 0.62, amber border.
Same vote, different penalty: that is the whole point. Then a transcript splits
horizontally into Prepared Remarks with a green 1.0 badge and Q&A with an amber
0.8 badge, and the equation lands: 0.75 × 0.8 = 0.60.

**Label:** Rehearsed vs spontaneous.

---

## Beat 4 — New Detectors

**Duration:** ~12s brief / ~40s actual

**Narration:**

Three new detection layers. First, negation detection. Phrases like "not
raising," "won't increase," "does not expect" now force full extraction
regardless of fast-pass results. FinBERT handles negation inconsistently, so
negated chunks skip the shortcut and go straight to the LLM. Second, keyword
density. A chunk packed with guidance phrases is a strong explicit signal. A
chunk with no keyword matches but a FinBERT flag is sentiment-only, and less
reliable. Third, duplicate detection. Re-filed transcripts get caught by
matching and skipped. No inflated signal counts, no wasted compute.

**Visual direction:**

Three detector cards in rapid sequence, roughly four seconds each — an upgrade
montage. Negation: the chunk "We do not expect to raise guidance this quarter."
appears, "do not expect to raise" highlights red, a flag icon lands, and a
routing diagram shows the chunk bypassing the fast-pass lane straight to full
LLM extraction. Keyword density: two chunks side by side — one with multiple
guidance phrases highlighted blue and a density meter filling to 0.85 green, one
plain with only a FinBERT tag and a meter barely reaching 0.05 red; the first
chunk's arrow to the triangulator is thick, the second's thin and faded.
Duplicate: two identical transcript icons with matching hashes, the second
stamped DUPLICATE and greyed out, a counter reading "Skipped. Compute saved."

---

## Beat 5 — Signal Decay

**Duration:** ~8s brief / ~25s actual

**Narration:**

Not all predictions age the same way. A signal can be right at thirty days and
wrong at one hundred eighty. That is a decaying signal, short-term noise that
looked real. A signal that is right at all three horizons is persistent, a
genuine read. Now every signal carries a decay profile. The scorecard knows
which readers produce lasting predictions and which ones fade.

**Visual direction:**

A signal card for Company A reads "raised, 0.84" with a timeline running right
through three checkpoints: 30 days green check, 90 days amber question mark, 180
days red X. Its confidence bar fades from green to red along the timeline —
tagged "Decaying. Short-term noise." Below it, Company B reads "lowered, 0.79"
and checks green at all three horizons, its bar staying solid — tagged
"Persistent. Genuine read." Both starting confidences are close on purpose:
initial confidence alone tells you nothing about shelf life.

**Label:** Same confidence. Different shelf life.

---

## Beat 6 — Close

**Duration:** ~5s

**Narration:**

Five weight dimensions. Three horizons. One fine-tuned model. ECIS, episode
five.

**Visual direction:**

Three flashes, roughly 1.2 seconds each. Five weight-dimension bars stack
vertically — Reader, Model, Speaker, Quality, Section — different lengths,
different colors, the full evolution of the triangulator across five episodes.
Then the 30/90/180 timeline with three checkmarks. Then the base model with its
small QLoRA adapter attached. All fade, and the title lands: ECIS — Episode 5.

---

## Beat 7 — The Verdict

**Pattern:** `ClaudeVerdictArtifact` · **Duration:** ~22s

**Narration:**

Let's recap with Claude. The model was fine-tuned on its own reviewed errors,
sharpened on the one boundary it kept missing. Disagreement penalties now scale
with how far apart the votes actually are. Three new detectors catch negation,
weak lexical support, and duplicate filings before they reach the scorecard. And
every signal now carries a decay profile across all three horizons. The system
did not get bigger this week. It got more honest about where it was wrong.

---

## Beat 8 — Your Turn (handoff)

**Pattern:** `ClaudeComposerAsk` · **Duration:** ~45s

**Narration:**

Your turn. "I have a judgment call I make repeatedly where I keep getting the
same specific type of case wrong — not randomly wrong, wrong in one consistent
direction on one particular kind of input. Can you help me: one, name the exact
boundary where my judgment breaks down, as precisely as I can define it; two,
design a way to collect and review my own past calls on just that boundary so I
have real examples of the mistake rather than a vague sense of it; and three,
tell me honestly whether a targeted fix on that one edge would help more than
trying to get generally better at the whole task?" Paste that into Claude and
find the one edge where your own judgment is weakest.

**Why this prompt:** it is the episode's whole thesis pointed at the viewer — a
QLoRA adapter is a targeted fix on one boundary rather than a general retrain,
and most people's judgment fails the same way: in one specific place, not
everywhere at once.

---

## Beat 9 — Outro

**Pattern:** `ClaudeTitleOutro` · **Duration:** ~6s

**Narration:**

Fine-tuned on its own mistakes. That's Anjana.

---

## Production Notes

**Total estimated duration:** ~4:40 (16:9) — the six body beats run long
against their briefs because the source narration is dense; kept verbatim per
the series convention, with the evidence carried on screen so no beat becomes a
podcast.

**Voice:** `af_bella` (Anjana). The source `beats.json` and `README.md` say
`am_onyx`; every prior ECIS episode overrode this to Anjana's own voice, and
Episode 5 follows.

**Delivery:** rendered at 4K in both 16:9 (3840×2160) and 9:16 (2160×3840). The
9:16 short is a derivative cut via `runtime/scripts/shorts.py` and drops
whatever the 3:00 Shorts cap requires.

**Scope note:** every number on screen — rank 16, 4-bit, 5 epochs, 8B base
model, 200+ reviewed extractions, the 1.0/0.8 section weights, the 0.80/0.75 and
0.80/0.20 vote spreads — comes from the pre-authored narration and visual
briefs in this folder. No figure was invented for the video. See `PEDAGOGY.md`.

**No real company names or tickers anywhere in this reel** — the decay beat uses
Company A and Company B, matching the Episode 4 convention.
