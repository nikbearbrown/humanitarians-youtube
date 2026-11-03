# Weekly Research Report: The Pipeline That Was Lying to Me

**Fellow:** Sai Pranavi J.
**Week ending:** July 26, 2026
**Project:** Project 29 — Financial Regulatory Intelligence System (`mycroft` repo, `scripts/regulatory-intel/`)
**Source status:** Real engineering work. All measured numbers below come from a rolled-back test transaction run against live RSS feeds and a local Postgres database, not a simulation.

## Watch

- Landscape (4K 16:9): [Drive link](https://drive.google.com/open?id=1vIWhuC1-6z8PvmQnLearM_P61Vsfm5cF)
- Vertical (4K 9:16): [Drive link](https://drive.google.com/open?id=1ML-wCn03WrlK8DcjLCPL8L1WImFOivvt)

This ~90-second AI-generated video asks: **can a pipeline lose real data without ever throwing an error?** It dramatizes one specific fix from this week's Layer 1 hardening pass: recovering title-only filings that a silent content filter had been dropping.

## What this covers (and what it deliberately leaves out)

The inherited n8n workflow (originally built by Darshan Rajopadhye) had several known problems on handoff: a dead Postgres credential, hand-rolled quote-escaping, no per-feed error isolation, silently dropped empty-description items, missing HTML escaping, source misclassification, and false-positive keyword scoring. This video is a deep-dive on **one** of those fixes — the dropped-empty-description bug — chosen because it has the clearest before/after proof (+73 recovered items per run) and the sharpest single takeaway for an engineering audience.

The other Layer 1 fixes (parameterized inserts, feed isolation, HTML escaping, threshold alignment) and the still-open items (source misclassification, Layer 2 LLM re-scoring) are candidates for future weekly reports, not this one.

## Production state

- Plan: **approved** (2026-07-26); reopened and re-closed 2026-08-26 for a program-feedback rebuild (4K + 2 new front beats)
- Fact-check gate: **resolved** — see `FACTCHECK.md` (B00 dramatization line removed; one flagged phrasing kept by fellow decision) — unchanged by the 2026-08-26 rebuild, no claims were touched
- Narration approval: **approved** for the original 7-beat cut — fellow reviewed that rendered master 2026-07-27. The rebuilt 9-beat cut adds B00 (silent, no narration) and B01 (executive-summary narration text fixed verbatim by the program feedback); **fellow re-review of this specific 9-beat cut is not yet recorded.**
- Voice: **Bella (`af_bella`)**, confirmed — the installed toolkit only ships two voices (Onyx `am_onyx`, Bella `af_bella`); `af_kore` from the original name-based suggestion doesn't exist
- Audio lock: **locked** — original 7 beats locked 2026-07-26; extended 2026-08-26 to 9 beats (B00 silent + B01 new), with the 7 original beats' audio regenerated and confirmed byte-for-byte-equivalent-length to the original lock
- Previz: **complete** — 9/9 beats real (no slates); master is `2026-07-26-recovering-the-silently-dropped-filings.mp4`, **3840x2160 (4K), 106.46s**
- Visual QC: 0 BLOCKER defects on the true clean master (checked directly, not the watermarked review cut); 11 MAJOR cosmetic notes (underfill/low-contrast) — the identical count/category as the pre-rebuild 7-beat master, now under shifted beat IDs, no new defects introduced by the rebuild
- Self-assessment: scored against `PROOF.md`'s rubric in `SELF-ASSESSMENT.md` — 4/12 (this is a single-insight case-study reel, not the framework-teaching genre PROOF's rubric targets; see that file for the honest breakdown and the one broadly-useful takeaway: put a visible source line next to the recovered-filings/count claims)
- Publishing: **not authorized**
- Code repository: paperwork/code (no media) pushed to `github.com/nikbearbrown/humanitarians-youtube`, branch `sai-pranavi-j-filings-4k-rebuild` (commit `51a476b`) — no PR opened yet
- **9:16 Short built (2026-08-28):** `short/2026-07-26-recovering-the-silently-dropped-filings-short.mp4` — **1080x1920, 110.96s**, the whole reel reformatted (under the 180s Shorts cap, so 0 beats dropped, all narration reused unchanged). All 9 GRAPHIC beats got a hand-authored portrait `short/scenes.py` (never auto-cropped, per THE REFORMAT RULE) — see `BUILD-LOG.md`'s 2026-08-28 entry for the two beats that needed a genuine top-to-bottom redesign (B03's pipeline diagram, B06's before/after count) and a Manim CLI portrait-frame quirk found and fixed along the way. GATE V clean (0 BLOCKER/0 MAJOR) on all 9 authored scenes; one MAJOR remains on the toolkit's own auto-generated endcard (flagged as a human design call, not fixable without editing `brutalist/`). Not yet authorized to publish.

<!-- BEGIN BRUTALIST REBUILD GUIDE -->

# The Pipeline That Was Lying to Me

## What this video is about

**Topic:** Recovering silently-dropped regulatory filings in Project 29

This is Bella, in for Humanitarians AI. Sai Pranavi inherited a financial regulatory intelligence pipeline this week and found it had been silently dropping real SEC and exchange filings — with no errors, no logs, just missing data. The video walks through the discovery, the fix, and the measured proof.

The current plan contains **9 beats** over roughly **106 seconds** (4K, 3840x2160) — a silent title card and a spoken executive-summary/personal-intro card were added at the front 2026-08-26 per program feedback, ahead of the original 7-beat hook-through-sign-off arc.

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
4. **Compile the previz:** render locally; missing beats stay as honest labeled slates until built. (All 9 beats are real Manim scenes — see `scenes.py`.)
5. **Watch, refine, and repeat.**
6. **Publish only by human decision** — a successful local render is not upload authorization.

## Useful project files

- `beat_sheet.json` — narrative and visual plan
- `scenes.py` — Manim source for all 9 beats (the actual video content)
- `BUILD-PROMPT.md` — the reproducible context/prompt this video was built from
- `BUILD-LOG.md` — dated build decisions and gate history
- `FACTCHECK.md` — claim-level evidence and corrections
- `SOURCES.md` — research, repo paths, and citation status
- `SHOTLIST.md` — beat-by-beat medium/timing table
- `PEDAGOGY.md` — Gate P sign-off (act structure + evidence discipline)
- `PROOF.md` / `SELF-ASSESSMENT.md` — the skeptical-explainer review protocol and an honest self-scoring of this cut against it

<!-- END BRUTALIST REBUILD GUIDE -->
