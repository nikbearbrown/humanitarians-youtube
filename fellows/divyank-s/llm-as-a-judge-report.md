# Report: Claude, Judged. — LLM-as-a-Judge, Two Cuts

**Topic:** LLM-as-a-judge evaluation systems
**Skill:** `deep-explainer` (brutalist.art toolkit)
**Location:** `humanitarians-youtube/llm-as-a-judge/`
**Cost:** $0.00 (Kokoro TTS, local Remotion rendering, no API keys)

## 1. Deliverables

| | 16:9 master | 9:16 Short |
|---|---|---|
| **File** | `claude-liam-llm-as-a-judge.mp4` | `short/claude-liam-llm-as-a-judge-short.mp4` |
| **Resolution** | 3840×2160 (4K UHD) | 2160×3840 (4K UHD, vertical) |
| **Duration** | 420.35s (7:00.4) | 152.26s (2:32.3) |
| **File size** | 125.4 MB | 40.9 MB |
| **Beats** | 32 | 11 |
| **Gate** | `PEDAGOGY.md` — `VERDICT: PASS` | `short/PEDAGOGY.md` — `VERDICT: PASS` (covers the one new line, the rewritten outro) |

Both are real, rendered, playable files — not previews. Neither is
published or authorized for publication.

## 2. The 8 required points, and where each one is covered

The 16:9 master is structured as 4 acts of 2 points each:

| Act | Points | Beats |
|---|---|---|
| **I — Define the Case** | (i) Test case structure, (ii) Judge prompts | `A1-1`–`A1-6` |
| **II — Read the Verdict** | (iii) Output parsing, (iv) Bias mitigation | `A2-1`–`A2-6` |
| **III — Judge at Scale** | (v) Metric abstraction, (vi) Batch evaluation runner | `A3-1`–`A3-6` |
| **IV — Ship the Judgment** | (vii) Aggregation, (viii) CI/CD integration | `A4-1`–`A4-6` |

Specifically, on screen:

- **(i) Test case structure** (`A1-2`): four fields, always in this order —
  input, candidate output, reference (optional), rubric — shown as a
  `ClaudeScienceLayerStack`.
- **(ii) Judge prompts** (`A1-4`): the four required parts of a working
  judge prompt — role framing ("you are an impartial judge"), the rubric,
  the candidate output verbatim, and a fixed answer format — plus the
  reference-based/reference-free fork (`A1-5`, `BinaryBranch`) and the
  reasoning-before-verdict technique (`A1-6`).
- **(iii) Output parsing** (`A2-2`, `DivergentFates`): free-text regex
  extraction (brittle) vs. constrained/JSON-mode output (reliable at
  generation time, not parse time).
- **(iv) Bias mitigation** (`A2-4`, `A2-5`): the three biases named and
  measured by Zheng et al. (2023) — position, verbosity, self-enhancement —
  and the specific fix for position bias (swap answer order, require
  agreement, don't average disagreement away).
- **(v) Metric abstraction** (`A3-2`, `ClaudeScienceLayerStack`): separating
  WHAT is measured (a pluggable metric interface — correctness,
  helpfulness, safety, groundedness) from HOW the judge-calling machinery
  works underneath.
- **(vi) Batch evaluation runner** (`A3-3`–`A3-6`): rate limits, retries,
  concurrency, response caching on identical inputs, and partial-failure
  handling (log-and-continue vs. stop-on-first-failure) at real scale.
- **(vii) Aggregation** (`A4-2`, `A4-3`): mean score, pass rate, win rate,
  category breakdown, and — the beat singled out as the one that actually
  matters — comparison against the last known-good baseline, not the score
  in isolation.
- **(viii) CI/CD integration** (`A4-4`, `A4-5`): wiring the baseline
  comparison into a build gate (`BinaryBranch` — above threshold passes,
  below it fails, the same way a broken unit test would) and publishing
  the report as a build artifact tied to the commit, not a chat message.

`A4-6` closes with an explicit boundary: the judge is still a model, and
Zheng et al.'s own validation against human preference agreement is cited
as the reason periodic human spot-checks stay in the loop.

## 3. Sourcing and fact-check method

This topic has no single source document (unlike the three prior builds
this week, each grounded in one already-read book chapter). Every claim in
`FACTCHECK.md` is tagged one of two ways:

- **General** — a well-established engineering pattern with no single
  citable origin (most of the reel: test case shape, prompt structure,
  caching, concurrency, aggregation, CI gating).
- **Cited** — attributed by name. Exactly one citation appears anywhere in
  either cut: **Zheng, L. et al. (2023), "Judging LLM-as-a-Judge with
  MT-Bench and Chatbot Arena"** — used only for the three named biases and
  the human-preference validation claim.

Deliberately excluded: any specific commercial eval framework's internal
behavior, any benchmark percentage, any latency or cost figure — none of
these were independently verified for this build, so none appear on
screen.

## 4. The archival imagery — used honestly as metaphor, not evidence

The topic is a 2023-era software pattern with no historical photographic
referent, so the 6 real archival stills (all public domain, CC0, or CC BY,
sourced via the Wikimedia Commons API — Smithsonian's own search page
returns `HTTP 403` to non-browser fetches) illustrate a CONCEPT, never the
subject itself:

| Beat | Image | Stands in for |
|---|---|---|
| A1-1 | Boston Index Card Co. filing folders (LOC) | a structured record |
| A1-3 | Courtroom gavel (Flickr, CC0) | the judge role |
| A2-1 | Helen Campbell, wireless telegraph operator (LOC) | turning a raw signal into data |
| A2-3 | Scales of Justice statue, Middlesbrough | fairness/bias |
| A3-1 | Airacobra P-39 assembly line (LOC) | running many cases at scale |
| A4-1 | Douglas SBD-5 Dauntless production line, 1943 | continuous production (CI/CD) |

Every beat's `shot.prompt` and `media/<BID>.source.txt` sidecar states this
explicitly — none claims to depict LLM evaluation literally.

## 5. Building the two aspect ratios from one production

Rather than hand-authoring two separate 32-beat scripts, the 9:16 cut was
**derived** from the 16:9 master using the toolkit's own `shorts.py`
mechanism — this is the toolkit's documented way of producing a Shorts-style
vertical cut, not an improvised shortcut.

- `shorts.py`'s hard cap is 180 seconds; the 420s master is far over it, so
  the auto-planner proposed dropping the 16 longest unprotected beats.
- Two Remotion compositions this build relies on, `DivergentFates` and
  `BinaryBranch`, are already resolution-agnostic (they read their own
  width/height from `useVideoConfig()` rather than hardcoding 1280×720),
  so two new `<Composition>` entries — `DivergentFates916` and
  `BinaryBranch916` — were added to `runtime/remotion/src/Root.tsx` with
  **zero new component code**, giving those beats real portrait coverage.
- `ClaudeScienceChipGrid` and `ClaudeScienceLayerStack` (used for most
  other content beats) are **not** resolution-agnostic — they hardcode
  pixel math against a 1280-wide canvas — so no portrait variant was
  attempted for them; adding one would have meant real component rework,
  out of scope for this build.
- Given that constraint, the auto-planner's proposed drop list was
  **overridden by hand** (`shorts.py --drop <22 explicit beat IDs>`) to
  keep only beats with real, working 916 coverage: the cold open, 5
  `BinaryBranch`/`DivergentFates` mechanism beats (one from each act, two
  from Act II), 2 VOX stills (which center-crop safely regardless of
  Remotion support), the "Your Turn" handoff, and the outro. The verdict
  recap (`BVDT`, 38.7s, the single longest beat) was cut in this plan
  rather than kept, since a Short is a funnel to the long, not a
  replacement for it.
- The one genuinely new piece of narration in the whole Short — the
  auto-rewritten outro, whose first draft stitched raw narration fragments
  into a broken sentence ("the full video also covers Act one: define the
  case., Four layers, always in the…") — was hand-rewritten to a clean
  funnel line before its audio was generated, and that specific rewrite
  was the only thing sent through GATE P again (`short/PEDAGOGY.md`).

## 6. Known limitations

- **No frame-level Visual QC** was run on either cut (`ART_QC=0`, per this
  session's standing agreement bypassing the `claude-liam` channel's
  hardcoded branding-kicker lint) — both compile and play back correctly
  but have not had a 9-point-rubric frame inspection.
- **The `ClaudeScienceLayerStack`/`ChipGrid`-heavy majority of the 16:9
  master has no 9:16 path at all** — this is why the Short keeps only 11
  of the master's 32 beats rather than a lightly-trimmed version of it.
  A future pass adding real portrait layouts to those two components would
  let a Short retain far more of the master's content.
- **Neither video is published or authorized for publication.**
