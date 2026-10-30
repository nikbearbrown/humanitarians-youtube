# PEDAGOGY — Gate P (narration review before audio)

*Agentic AI: From the Loop to MCP* · Friday 2026-09-04

## The one idea

**Planning is a bet that the world will hold still. It halves the work when the bet pays,
and is worth nothing when it does not — so a plan earns its call only when steps are
expensive, the world is stable, and order genuinely matters.**

## Stands alone

No back-references. Nothing in the narration assumes the viewer has seen anything before:
no "last week", no "as we covered", no episode or week number anywhere. A viewer arriving
cold loses nothing. Continuity with earlier work lives only in the code, and the script never
mentions it.

## HAI PM criteria

1. **Brutalist format** — `ai-explainer`, 13 beats, zero slates.
2. **4K at source** — mastered 3840×2160; the 9:16 cut at 2160×3840.
3. **Both aspect ratios** — 9:16 derived via `./art shorts` once the 16:9 locks.
4. **Formatting clean** — frame-level QC; all three mono tables sized from their longest
   line before authoring, not corrected afterwards.
5. **Intro line verbatim** — *"Hi, I am Adwait Changan, and this video is about what a plan
   actually costs an AI agent."*
6. **Real takeaway** — three conditions the viewer can apply to their own agent today, plus
   the "is the plan load bearing?" test, made active by BHTF.

## PROOF

- **Framework before examples** — B01 names the only two strategies before the first
  measurement appears at B02.
- **Falsifiability — B04.** The claim under test is the one the whole field acts on: that
  planning helps. It is measured and shown to degrade to zero advantage (18 against 18) when
  the surprise lands at step one. The beat exists to attack the video's own premise.
- **Side-by-side** — B02, B04 and B06 each hold both strategies in a single frame.
- **Worked example** — B02 and B06 run the framework on real printed output.

## Structure (13 beats, ~4 min)

Hook with the intro line → **the two strategies** (B01) → **price them when nothing goes
wrong** (B02) → a plan is a guess about later (B03) → **falsifiability: price them when
something does** (B04) → the three-condition test as nine real lines (B05) → the test run on
all four cases (B06) → the rule in plain terms (B07) → the expensive middle: a plan written
then ignored (B08) → is the plan load bearing? (B09) → verdict → scaffolded task → outro.

## Honesty notes confirmed at this gate

- [x] **It is a cost model, not a benchmark, and `planner.py` says so in its own docstring.**
      It counts model calls under stated assumptions. It does not measure answer quality and
      the narration never claims it does.
- [x] **A label error was caught before audio.** The k=1 row was printing "planning now costs
      MORE" when the two strategies actually tie at 18 calls. Overstating the case in the one
      beat whose job is honesty would have been the worst possible place for it. The label now
      distinguishes *advantage is GONE* from *costs MORE*, and the narration says "eighteen
      calls against eighteen — the entire advantage is gone."
- [x] **B05 is verbatim** via `inspect.getsource()`; "nine lines" was counted.
- [x] **No vendor, model, benchmark or price appears anywhere.**
- [x] **The verdict names the limit**, not just the capability: the costliest pattern is a
      plan that is written, displayed, then ignored.

## Verdict

- Plan: APPROVED — 13/13 Remotion, zero slates, no consecutive pattern repeats.
- Narration: APPROVED — body beats 41–63 words.
- Fact-check (`FACTCHECK.md`): CLEARED.

> VERDICT: PASS (FINAL scope) — prepared by the build agent under the fellow's standing
> delegation. Unlocks audio and the clean master render. Does not authorize publishing,
> Drive upload, or notification.
