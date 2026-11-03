# FACTCHECK — The Model That Doesn't Write Back

Every figure and factual claim on screen or in narration, and how it was
checked. "Archived" = the page as fetched on 2026-09-25 in `evidence/sources/`;
each quoted phrase was found there with `grep`.

## What Jev is (B00, B02, B08)

| Claim | Source | Result |
|---|---|---|
| Jev comes from TypeSafe (TypeSafe AI) | launch post (archived) | ✓ |
| Early access since 15 September 2026 | launch post header "Sep 15, 2026"; "early access" ×5 | ✓ |
| Returns typed values + probabilities, not text | launch post ("type-safe structured values"; LLMs produce "strings/generated text"); docs System One ("typed decisions and probabilities rather than generated text") | ✓ |
| Chatbots write one word at a time; Jev answers all at once | launch post: LLM sampling "sequential", Jev "parallel … all outputs in one query"; docs Introduction: one request, answers "evaluated in parallel" | ✓ |
| "your program has to read that text to dig out the answer" | launch post: LLM strings "requiring parsing and validation" | ✓ (paraphrase) |
| "it doesn't write text" | jaggedness doc: "Jev-1.13 is not trained to generate text"; launch post: Jev "gives up string generation" | ✓ |

## The name (B01)

| Claim | Source | Result |
|---|---|---|
| "System One model", after Kahneman's System 1 in *Thinking, Fast and Slow* | docs System One: "The System One name references Daniel Kahneman's Thinking, Fast and Slow" | ✓ |
| System 1 = fast, intuitive | same page: "System 1 thinking is fast and intuitive. System 2 is slower and more deliberate." | ✓ |
| The switchboard operator | a metaphor, not a claim about Jev; photos are real (see SHOTLIST) | — |

## The three question types (B03, B08)

| Claim | Source | Result |
|---|---|---|
| Choice — pick an option from a list | docs Introduction: Choice "Choose an option from a list" → `choice`, `probabilities`, `confidence` | ✓ |
| Score — rate on a rubric/scale | docs Introduction: Score "Score the state on a rubric" → `score`, `probabilities`, `confidence` | ✓ |
| Noul — "is this statement true?", a 0–1 value | docs Introduction: Noul "Is this statement true?" → `noul` (0–1) | ✓ |
| Several at once in one request | docs Introduction: "All three can be mixed in a single API call" | ✓ |
| The refund example (requested? duplicate? policy?) | docs System One: refund workflow asking whether a refund was requested, whether evidence indicates a duplicate charge, whether policy supports it | ✓ |

## What 0.8 means (B04) — algebra

- Row 1, `Noul(s) = p̂ ∈ [0, 1]` — the documented Noul return is a value in 0–1. ✓
- Row 2, `Pr(s true | p̂ = 0.8) ≈ 0.8` — the standard definition of calibration,
  evaluated at 0.8. `≈`, not `=`: calibration is a property of many answers. ✓
- Row 3, `100 × 0.8 = 80 true` — the expected count, exact arithmetic. ✓
- "calibration doesn't promise any single answer is right" — docs System One,
  verbatim: "Calibration is measured across groups of predictions; it does not
  guarantee that an individual answer is correct." ✓
- "Jev's probabilities are meant to be calibrated" — same page: "their
  probabilities are optimized against outcomes to reflect uncertainty". Worded
  "meant to be", because no independent calibration study has been published. ✓

**Reproducible numerical case** — `evidence/calibration.out` (seed 20260925):
a *constructed* source that says 0.8 every time gives 8/10, **82/100** and
7,952/10,000 true. It demonstrates the definition only; it is not Jev.

Typography: outlined SVG from `runtime/scripts/typeset_math.py` (STIX). `Noul`,
`Pr`, `true` upright; s, p italic; real hat on p̂, ∈, ≈, sized parentheses and
the conditional bar. No raw TeX in any text card.

### Rendered-frame review (MATH-TYPESETTING.md)

B04's equation frames were inspected in **both** aspects from the rendered clips
(`media/B04.mp4`, `vertical/media/B04.mp4`); frames in `_qc/look/` and
`vertical/_qc/look/`.

| Aspect | Frames | Result |
|---|---|---|
| 16:9 (3840×2160) | 15% (2.64s), 50% (8.79s), 85% (14.93s) | **pass** |
| 9:16 (2160×3840) | 15%, 50%, 85% | **pass** |

Reveal cues (measured mp3, 17.57s): row 1 at 1.49s ("Jev's probabilities"),
row 2 at 3.57s ("Take every answer"), row 3 at 8.34s ("In a simulation").

- Staged reveal verified: row 1 alone at 15%; all three by 50% and 85%. No
  invalid intermediate equality is ever shown.
- The hat on p̂ sits on the p in every row; the conditional bar, ∈, ≈ and ×
  resolve to real STIX glyphs. No tofu.
- `Noul`, `Pr`, `true` upright; s and p italic.
- Nothing clipped in either aspect; the portrait stack keeps clear margins and
  the note/conditions text does not overlap the rows.
- Row 3 was shortened to `100 × 0.8 = 80 true` (dropping ", 20 false") so its
  aspect stays near 9 and it renders large in portrait.

## Speed and price (B05, B07, B08)

| On screen | Value | Source |
|---|---|---|
| fastest reply | 70 ms | launch post: "70ms-500ms" end-to-end |
| slowest reply | 500 ms | same |
| $ per 1M input tokens | 0.042 | launch post: "$0.042 / MTok ($42 per billion tokens)" |
| output free | — | launch post: "FREE (too cheap to meter)" |
| 1M tickets, total $ | 21 | `evidence/cost.out`: 1,000,000 × 500 (assumed) = 500M tokens × $0.042/M = **$21.00** |
| "up to two hundred times faster" | 200× | launch post: "40x-200x faster" (peak internal figure 193.6×) |
| tests built by TypeSafe's own team | — | launch post: workflows made by "individuals on our model capabilities team", "some bias could exist"; gains "on the higher end of real world gains" |
| "Nobody independent has verified them yet" | — | SiliconANGLE, 16 Sep: "Those figures have not been independently verified"; TechStock², 17 Sep: "company-generated results, not independent measurements" |
| "thousands of prompts for cents" | — | arithmetic: 1,000 prompts × 1,000 tokens = 1M tokens = $0.042 |

Consistency check (not on screen): TypeSafe's Doom demo, "~$7/hour" at 10
queries/s, implies ~4,630 input tokens per query at the published price —
plausible for a structured game state (`evidence/cost.out`).

## The weakness list (B06, B08)

All from the jaggedness doc for jev-1.13 (archived), except the last:

| On screen | Source wording |
|---|---|
| Not a calculator — do the math in code | "Jev is not a calculator. We strongly recommend implementing any mathematical logic in code." |
| Reads dates as text — not as dates | "Reads dates as text, not as ordered quantities" |
| Can be steered by hidden instructions | "Does not treat [state] as hostile by default"; injected instructions and misleading framing can steer answers |
| Doesn't write | "Jev-1.13 is not trained to generate text" |
| Only reads text, no images yet | docs System One: "Jev currently accepts text input only" |

## "Can't hallucinate" (B07)

TypeSafe's launch post plots 0% hallucination and says: "Our number is not
empirical. Schema matching is guaranteed, thus we can confidently add 0% into
the plots." B07 therefore says "'can't hallucinate' means the answer always has
the right shape, not that it's right", matching TechStock²: "A schema can
guarantee that Jev returns one of the permitted shapes; it cannot guarantee the
chosen answer is right." ✓

## Claims deliberately not made

| Tempting claim | Why not |
|---|---|
| "Jev is 200× faster" | TypeSafe's own internal tests; said as "up to", attributed, then questioned |
| "Jev never makes mistakes" | Only the output *shape* is guaranteed |
| "invented RLHF / ChatGPT" | Contested credit; the founder isn't named at all |
| "$200 million startup" | True per Forbes/SiliconANGLE but not needed for a gentle introduction |
| Customer results | Single-developer anecdotes |
