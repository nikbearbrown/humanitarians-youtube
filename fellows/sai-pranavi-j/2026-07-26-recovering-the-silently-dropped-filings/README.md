# Weekly Research Report: The Pipeline That Was Lying to Me

**Fellow:** Sai Pranavi Jeedigunta
**Week ending:** July 26, 2026
**Project:** Project 29 — Financial Regulatory Intelligence System (`mycroft` repo, `scripts/regulatory-intel/`)
**Source status:** Real engineering work. All measured numbers below come from a rolled-back test transaction run against live RSS feeds and a local Postgres database, not a simulation.

This ~90-second AI-generated video asks: **can a pipeline lose real data without ever throwing an error?** It dramatizes one specific fix from this week's Layer 1 hardening pass: recovering title-only filings that a silent content filter had been dropping.

## What this covers (and what it deliberately leaves out)

The inherited n8n workflow (originally built by Darshan Rajopadhye) had several known problems on handoff: a dead Postgres credential, hand-rolled quote-escaping, no per-feed error isolation, silently dropped empty-description items, missing HTML escaping, source misclassification, and false-positive keyword scoring. This video is a deep-dive on **one** of those fixes — the dropped-empty-description bug — chosen because it has the clearest before/after proof (+73 recovered items per run) and the sharpest single takeaway for an engineering audience.

The other Layer 1 fixes (parameterized inserts, feed isolation, HTML escaping, threshold alignment) and the still-open items (source misclassification, Layer 2 LLM re-scoring) are candidates for future weekly reports, not this one.

## Production state

- Plan: **approved**
- Fact-check gate: **resolved** — see `FACTCHECK.md` (B00 dramatization line removed; one flagged phrasing kept by fellow decision)
- Narration approval: **approved** — fellow reviewed the rendered master
- Voice: **Bella (`af_bella`)**, confirmed — the installed toolkit only ships two voices (Onyx `am_onyx`, Bella `af_bella`); `af_kore` from the original name-based suggestion doesn't exist
- Audio lock: **locked**
- Previz: **complete** — 7/7 beats real (no slates); master is `2026-07-26-recovering-the-silently-dropped-filings.mp4` (88.5s)
- Visual QC: 0 blocking defects on the clean master; a handful of cosmetic "underfill" notes remain (optional polish)
- Publishing: **not authorized**

<!-- BEGIN BRUTALIST REBUILD GUIDE -->

# The Pipeline That Was Lying to Me

## What this video is about

**Topic:** Recovering silently-dropped regulatory filings in Project 29

This is Bella, in for Humanitarians AI. Sai Pranavi inherited a financial regulatory intelligence pipeline this week and found it had been silently dropping real SEC and exchange filings — with no errors, no logs, just missing data. The video walks through the discovery, the fix, and the measured proof.

The current plan contains **7 beats** over roughly **90 seconds**.

## Make your own version

Download the free local toolkit:

```bash
git clone https://github.com/nikbearbrown/brutalist.art.git
cd brutalist.art
./setup --install
./setup
```

The toolkit uses local Kokoro narration and does not require an API key. The beat sheet is the source of truth: one beat per moment, with narration, visual intent, and shot instructions. For this project, start with `beat_sheet.json`. **Preserve it before experimenting — make a copy or a branded variant rather than overwriting a finished plan.** If this video needs a substantially different cut (different bug, different voice, different length), create a new sibling folder rather than editing this one in place.

Recommended builder: **`ai-explainer`** — one tight insight, not a multi-act documentary. Use `cli-explainer` instead if a future cut wants to show the actual prompt → code → verification loop live rather than dramatizing it after the fact.

## Fact-check prompt

Run this after editing the narration:

> Audit `beat_sheet.json` beat by beat. Extract every factual, numerical, and named-entity claim (recovered-item counts, specific filing names, before/after totals). Check each against the actual `mycroft` repo test-transaction output and BUILD-LOG entries referenced in `SOURCES.md`. Produce a table with beat ID, claim, verdict (SUPPORTED / QUALIFY / UNSUPPORTED / OUTDATED), evidence, source, and required correction. Flag any named filing whose exact citation/URL has not been independently confirmed. Do not silently repair the script: list every proposed change for human review.

## Build and review loop

1. **Fact-check:** resolve every claim in `FACTCHECK.md` against the actual pipeline run logs before narration is finalized. (Done for this cut — see the resolution notes there.)
2. **Gate P — narration review:** read every line aloud; confirm the +73 number and filing names are still accurate as of build time (feed content changes).
3. **Generate local audio:** Kokoro voice `af_bella` (Bella), Pragmatist register.
4. **Compile the previz:** render locally; missing beats stay as honest labeled slates until built. (All 7 beats are now real Manim scenes — see `scenes.py`.)
5. **Watch, refine, and repeat.**
6. **Publish only by human decision** — a successful local render is not upload authorization.

## Useful project files

- `beat_sheet.json` — narrative and visual plan
- `scenes.py` — Manim source for all 7 beats (the actual video content)
- `BUILD-PROMPT.md` — the reproducible context/prompt this video was built from
- `BUILD-LOG.md` — dated build decisions and gate history
- `FACTCHECK.md` — claim-level evidence and corrections
- `SOURCES.md` — research, repo paths, and citation status
- `SHOTLIST.md` — beat-by-beat medium/timing table
- `PEDAGOGY.md` — Gate P sign-off (act structure + evidence discipline)

<!-- END BRUTALIST REBUILD GUIDE -->
