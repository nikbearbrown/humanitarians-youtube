# Weekly Research Report: The Update That Almost Lied About What It Sent

**Fellow:** Sai Pranavi Jeedigunta
**Week ending:** August 30, 2026
**Project:** Project 29 — Financial Regulatory Intelligence System (`mycroft` repo, `scripts/regulatory-intel/`)
**Source status:** Real engineering work. Every claim traces to `A7-VERIFICATION.md` (2026-08-30) and `logs/RUN_LOG.md`'s two 2026-08-30 entries; the live-row count was re-verified directly against the DB at build time (2026-08-30 21:04), not just quoted from the doc.

This ~2-minute AI-generated video asks: **can a step that only records "this got emailed" quietly re-derive its own copy of the rule for what counts as high-priority — and drift from it?** It dramatizes one specific fix from this week's continued Layer 1 hardening pass on the same regulatory-intel pipeline as the 2026-07-26 report: the "Mark email sent" Postgres node was using its own copy of the high-priority rule instead of reading what the email step had actually sent.

## What this covers (and what it deliberately leaves out)

The alert path is simple: insert the item, filter for `urgency_score > 6` ("High Priority Filter", feeds the email), build and send an email from exactly those rows, then mark those rows sent. The "Mark email sent" node was supposed to just record that — instead it re-derived its own condition (`urgency_score > 7 OR impact_level IN ('Critical','High')`), which could disagree with the email filter because `determineImpactLevel()` has an enforcement/fraud keyword bypass that can set `impact_level` to High or Critical regardless of how low the score is. A live query against the real `regulatory_feeds` table found 12 rows right now — including a genuine SEC insider-trading enforcement action (id 153) — that the email filter would never select but that the old query would have silently flipped to `email_sent = TRUE` the next time it ran. The fix: stop re-deriving the rule; read the exact ids the email step already produced (`WHERE id = ANY($1::int[])`).

The still-open source-misclassification bug and the Google News link-unwrapping task (confirmed this week to be a bigger scrape-based project, not a quick fix) are candidates for a future report, not this one.

## Production state

- Plan: **approved** — 2026-08-30 (Gate P)
- Fact-check gate: **resolved** — see `FACTCHECK.md` (B05's forward-looking "would have" framing approved as written; the "12" count re-verified live at build time, identical ids to the `A7-VERIFICATION.md` snapshot)
- Narration approval: **approved** — 2026-08-30, cleared for audio generation
- Voice: **Bella (`af_bella`)** — locked for this fellow's whole report series, unchanged from prior episodes
- Audio lock: **locked** — Kokoro `af_bella`, all 9 beats (B00 silent via `ffmpeg anullsrc`, 4.05s measured; B01-B08 measured 18.02/13.44/16.68/23.52/21.55/7.97/10.61/5.62s)
- Previz: **complete** — 9/9 beats real (no slates); master is `2026-08-30-the-update-that-almost-lied-about-what-it-sent.mp4`, **3840x2160 (4K), 121.41s**
- Visual QC: **0 BLOCKER, 0 MAJOR** on the true clean 4K master (checked directly, not the watermarked review cut — see `BUILD-LOG.md` for the two rounds of real layout fixes: B02's panel/caption overhang, B03's divider-crossing mismatch line, plus underfill fixes on B00/B02/B04/B07/B08)
- Publishing: **not authorized**
- **9:16 Short built (2026-08-30):** `short/2026-08-30-the-update-that-almost-lied-about-what-it-sent-short.mp4` — **1080x1920, 125.96s**, the whole reel reformatted (under the 180s Shorts cap, so 0 beats dropped, all narration reused unchanged). All 9 GRAPHIC beats got a hand-authored portrait `short/scenes.py` (never auto-cropped, per THE REFORMAT RULE) — see `BUILD-LOG.md` for the 3 beats that needed a genuine top-to-bottom redesign (B03's two conditions, B05's query+count+row, B06's before/after fix — each converted from the parent's side-by-side layout to a stacked one with a horizontal divider) and the real layout bugs GATE B caught and fixed along the way (a mis-positioned node, a mismatch line sitting directly on a divider, a code caption colliding with trailing code lines, a panel-overhang). GATE V clean (0 BLOCKER/0 MAJOR) on all 9 authored scenes; 2 MAJOR remain on the toolkit's own auto-generated silent END card (flagged as a human design call, not fixable without editing `brutalist/`).

## Deliverables

- `Mycroft_SaiPranaviJeedigunta_20260830_16x9.mp4` — 4K (3840x2160) master, 121.41s
- `Mycroft_SaiPranaviJeedigunta_20260830_9x16.mp4` — portrait (1080x1920) short, 125.96s

<!-- BEGIN BRUTALIST REBUILD GUIDE -->

# The Update That Almost Lied About What It Sent

## What this video is about

**Topic:** A re-derived rule silently drifting from the rule it was supposed to match, in Project 29's regulatory-intel pipeline

This is Bella, in for Humanitarians AI. Sai Pranavi found a database update in the same regulatory pipeline from last week that could mark high-priority alerts "emailed" even when no email had actually gone out for them — because it re-derived its own copy of the high-priority rule instead of reading what the email step had actually sent. The video walks through the discovery, the live proof, and the fix.

The current plan contains **9 beats** over roughly **121 seconds** (4K, 3840x2160) — a silent title card and a spoken executive-summary/personal-intro card up front, then hook through sign-off.

## Make your own version

Download the free local toolkit:

```bash
git clone https://github.com/nikbearbrown/brutalist.art.git
cd brutalist.art
./setup --install
./setup
```

The toolkit uses local Kokoro narration and does not require an API key. The beat sheet is the source of truth: one beat per moment, with narration, visual intent, and shot instructions. For this project, start with `beat_sheet.json`. **Preserve it before experimenting — make a copy or a branded variant rather than overwriting a finished plan.** If this video needs a substantially different cut (different bug, different voice, different length), create a new sibling folder rather than editing this one in place.

Recommended builder: **`ai-explainer`** — one tight insight, not a multi-act documentary.

## Fact-check prompt

Run this after editing the narration:

> Audit `beat_sheet.json` beat by beat. Extract every factual, numerical, and named-entity claim (the two conditions' exact thresholds, the "12" row count, the named example row and its fields, the before/after SQL). Check each against `A7-VERIFICATION.md` and `logs/RUN_LOG.md` in the `mycroft` repo referenced in `SOURCES.md`. Produce a table with beat ID, claim, verdict (SUPPORTED / QUALIFY / UNSUPPORTED / OUTDATED), evidence, source, and required correction. Flag any claim that asserts something already happened ("were marked sent") rather than the forward-looking, conditional truth ("would have been"). Do not silently repair the script: list every proposed change for human review.

## Build and review loop

1. **Fact-check:** resolve every claim in `FACTCHECK.md` against the actual pipeline code and a live query before narration is finalized. (Done for this cut — see the resolution notes there.)
2. **Gate P — narration review:** read every line aloud; confirm the "12" count and the row-153 example are still accurate as of build time (the table is live and growing).
3. **Generate local audio:** Kokoro voice `af_bella` (Bella), Pragmatist register.
4. **Compile the previz:** render locally; missing beats stay as honest labeled slates until built. (All 9 beats are real Manim scenes — see `scenes.py`.)
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
