# Weekly Research Report: The Synonyms the Classifier Never Learned

**Fellow:** Sai Pranavi Jeedigunta
**Week ending:** September 7, 2026
**Project:** Project 29 — Financial Regulatory Intelligence System (`mycroft` repo,
`scripts/regulatory-intel/`)
**Source status:** Real engineering work. Every claim traces to
`UNKNOWN-SOURCE-INVESTIGATION.md` (2026-08-30) — a live test run against all 5 real
regulatory-intel feeds as they existed that day. See `SOURCES.md` and `FACTCHECK.md`.

This ~2-minute AI-generated video asks: **what do you do with the fraction of a fix that's
genuinely, honestly not worth chasing?** It is the fourth report in the "Layer 1 hardening"
series — a partial fix, reported straight. After last week's `dc:creator` fix (recovering the
Federal Register misclassification), 18 items across the two Google News feeds still fell through
the source classifier into `'Unknown Source'`. Google News items carry no `dc:creator` field —
the fix that solved last week's bug doesn't apply here. This week's fix: two feed-agnostic synonym
checks ("adviser"/"RIA"/"Reg BI" language), added after reading all 18 real titles by hand.

## What this covers (and what it deliberately leaves out)

The 18 titles split into two real groups: some just used a word the classifier didn't check for
("adviser" alone, the "RIA" acronym, "Reg BI"); others had no named regulator at all, or named a
completely different one — one item was about the UK's Financial Conduct Authority, which this
pipeline was never built to track. The fix recovered **10 of 18 (56%)**, live-verified against all
5 feeds, **zero unexpected reclassifications** of items that were already correctly labeled. The
remaining 8 are shown honestly as a deliberate, reasoned stopping point — not a bug still to fix.

**What this deliberately leaves out:** a fuzzier NLP/content-based approach to the remaining 8 is
flagged in the source material as a candidate for a future report, not this one — an explicit
tradeoff (lower confidence for more coverage), not pursued here. B06's on-screen framing
("LEFT OPEN -- BY DESIGN") is FACTCHECK-locked to avoid any "coming soon" implication.

## Production state

- Plan: **approved** — 2026-08-31 (Gate P)
- Fact-check gate: **resolved** — see `FACTCHECK.md` (B06's "deliberate tradeoff" framing kept as
  drafted; the "eighteen" count confirmed fine stated plainly)
- Narration approval: **approved** — 2026-08-31, cleared for audio generation
- Voice: **Bella (`af_bella`)** — locked for this fellow's whole report series, unchanged from
  prior episodes
- Audio lock: **locked** — Kokoro `af_bella`, all 9 beats (measured 4.05/15.02/9.98/21.67/25.25/
  22.70/20.69/8.02/4.22s, total 131.6s)
- Previz: **complete** — 9/9 beats real (no slates); master is
  `2026-09-07-the-synonyms-the-classifier-never-learned.mp4`, **3840x2160 (4K), 131.58s**
- Visual QC: **0 BLOCKER, 0 MAJOR** on the true clean 4K master (checked directly, not the
  watermarked review cut — see `_qc/REPORT.md`)
- Publishing: **not authorized**
- **9:16 Short built (2026-09-07):**
  `short/2026-09-07-the-synonyms-the-classifier-never-learned-short.mp4` — **1080x1920, 136.1s**,
  the whole reel reformatted (under the 180s Shorts cap, so 0 beats dropped, all 9 beats'
  narration reused unchanged, plus a silent branded 4.5s END card). All 9 GRAPHIC beats got a
  hand-authored portrait `short/scenes.py` (never auto-cropped, per THE REFORMAT RULE) — see
  `BUILD-LOG.md` for the 3 beats that needed a genuine redesign (B03's field comparison, B04's
  two-title comparison, B05's five-feed results table — each converted from the parent's
  side-by-side/multi-column layout to a stacked or one-column mini-card layout) and the real
  layout/QC bugs GATE B and GATE V caught and fixed along the way. GATE V clean (0 BLOCKER/0
  MAJOR) on all 9 authored Manim beats; 2 MAJOR remain on the toolkit's own auto-generated silent
  END card (a human design call, not fixable without editing `brutalist/`).

## Deliverables

- `Mycroft_SaiPranaviJeedigunta_20260907_16x9.mp4` — 4K (3840x2160) master, 131.58s
- `Mycroft_SaiPranaviJeedigunta_20260907_9x16.mp4` — portrait (1080x1920) short, 136.1s

<!-- BEGIN BRUTALIST REBUILD GUIDE -->

# The Synonyms the Classifier Never Learned

## What this video is about

**Topic:** A partial fix to a source-classifier bug, honestly reported — including the part that
was deliberately left unfixed — in Project 29's regulatory-intel pipeline

This is Bella, in for Humanitarians AI. Sai Pranavi found 18 real items still falling into
'Unknown Source' after last week's fix — Google News feeds don't carry the field that fix relied
on. Reading all 18 titles by hand split them into two groups: some recoverable with a feed-agnostic
synonym check, others genuinely not recoverable without a much higher false-positive risk. The
video walks through the setup, the discovery, the fix and its live proof, and the honest limit.

The current plan contains **9 beats** over roughly **132 seconds** (4K, 3840x2160) — a silent title
card and a spoken executive-summary/personal-intro card up front, then hook through sign-off.

## Make your own version

Download the free local toolkit:

```bash
git clone https://github.com/nikbearbrown/brutalist.art.git
cd brutalist.art
./setup --install
./setup
```

The toolkit uses local Kokoro narration and does not require an API key. The beat sheet is the
source of truth: one beat per moment, with narration, visual intent, and shot instructions. For
this project, start with `beat_sheet.json`. **Preserve it before experimenting — make a copy or a
branded variant rather than overwriting a finished plan.** If this video needs a substantially
different cut (different bug, different voice, different length), create a new sibling folder
rather than editing this one in place.

Recommended builder: **`ai-explainer`** — one tight insight, not a multi-act documentary.

## Fact-check prompt

Run this after editing the narration:

> Audit `beat_sheet.json` beat by beat. Extract every factual, numerical, and named-entity claim
> (the 18/8 counts, the two synonym-check rules, the 5-feed before/after table, the two named
> example titles, the two remaining-failure categories). Check each against
> `UNKNOWN-SOURCE-INVESTIGATION.md` in the `mycroft` repo referenced in `SOURCES.md`. Produce a
> table with beat ID, claim, verdict (SUPPORTED / QUALIFY / UNSUPPORTED / OUTDATED), evidence,
> source, and required correction. Flag any beat that frames the remaining 8 as an unsolved bug or
> a promise to fix later rather than a deliberate, reasoned stop. Do not silently repair the
> script: list every proposed change for human review.

## Build and review loop

1. **Fact-check:** resolve every claim in `FACTCHECK.md` against the actual pipeline code and a
   live query before narration is finalized. (Done for this cut — see the resolution notes there.)
2. **Gate P — narration review:** read every line aloud; confirm the live-test framing and the
   18/8 counts are still accurate as of build time (the feeds are live and change daily).
3. **Generate local audio:** Kokoro voice `af_bella` (Bella), Pragmatist register.
4. **Compile the previz:** render locally; missing beats stay as honest labeled slates until built.
   (All 9 beats are real Manim scenes — see `scenes.py`.)
5. **Watch, refine, and repeat.**
6. **Publish only by human decision** — a successful local render is not upload authorization.

## Useful project files

- `beat_sheet.json` — narrative and visual plan
- `scenes.py` — Manim source for all 9 beats (the actual video content)
- `short/scenes.py` — hand-authored portrait (9:16) relayout of all 9 beats
- `BUILD-LOG.md` — dated build decisions and gate history
- `FACTCHECK.md` — claim-level evidence and corrections
- `SOURCES.md` — research, repo paths, and citation status
- `SHOTLIST.md` — beat-by-beat medium/timing table
- `PROMPTS.md` — pantry/asset status (N/A — all beats are self-contained Manim)

<!-- END BRUTALIST REBUILD GUIDE -->
