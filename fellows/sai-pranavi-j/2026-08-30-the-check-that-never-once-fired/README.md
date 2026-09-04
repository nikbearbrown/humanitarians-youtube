# Weekly Research Report: The Check That Never Once Fired

**Fellow:** Sai Pranavi Jeedigunta
**Week ending:** August 30, 2026
**Project:** Project 29 — Financial Regulatory Intelligence System (`mycroft` repo, `scripts/regulatory-intel/`)
**Source status:** Real engineering work. Every claim traces to `B2-VERIFICATION.md` (2026-08-30) and `logs/RUN_LOG.md`'s 2026-08-30 B2 entry — a live test run against all 5 real regulatory-intel feeds as they existed today, explicitly not a claim about the pipeline's full historical run log. See `SOURCES.md` and `FACTCHECK.md`.

This ~2-minute AI-generated video asks: **what happens when a safeguard is never actually tested against real input?** It dramatizes a second fix from this week's continued Layer 1 hardening pass on the same regulatory-intel pipeline as the two prior reports: the source classifier had a rule specifically written to catch CFTC filings and route them to a `CFTC Regulations` label — and when tested against every live CFTC item available today, it matched **zero of them**.

## What this covers (and what it deliberately leaves out)

The classifier's `identifySource()` heuristic checks whether a feed item's link contains `commodity-futures` or its title contains `cftc` — a rule that reads like it should catch every CFTC filing. Tested live against all 5 real regulatory-intel feeds today, it caught **0 of 12** real CFTC Regulations items (a real filing like "Swap Execution Facility Order Book Requirement for Permitted Transactions" has neither string anywhere in its title or link — the check was structurally looking for something that can't appear). The same live test found 83 of 146 "Securities" items were actually other agencies (FCC, EEOC, DOT) misfiled under a shared search term, while the SEC, FINRA, and Investment Advisor Rules feeds — already correct — showed **zero regressions**. The fix: read the feed's actual `dc:creator` field instead of guessing from link/title strings. After the fix, all 12/12 real CFTC items are caught correctly.

**What this deliberately leaves out:** the still-open 21 "Unknown Source" Google-News items (no reliable classification signal exists there) and B3 (Google News link unwrapping) are candidates for a future report, not this one.

## Production state

- Plan: **approved** — 2026-08-30 (Gate P)
- Fact-check gate: **resolved** — see `FACTCHECK.md` (the "tested live today" / "pulled live" framing confirmed sufficient; no implied real-world downstream incident anywhere in the script)
- Narration approval: **approved** — 2026-08-30, cleared for audio generation
- Voice: **Bella (`af_bella`)** — locked for this fellow's whole report series, unchanged from prior episodes
- Audio lock: **locked** — Kokoro `af_bella`, all 9 beats (measured 4.05/18.74/11.38/19.32/19.66/29.42/13.94/10.56/6.26s, total 133.33s; B01 regenerated 2026-08-31 to remove an inaccurate "last two weeks" timeframe claim, was 18.98s)
- Previz: **complete** — 9/9 beats real (no slates); master is `2026-08-30-the-check-that-never-once-fired.mp4`, **3840x2160 (4K), 133.32s**
- Visual QC: **0 BLOCKER, 0 MAJOR** on the true clean 4K master (checked directly, not the watermarked review cut — see `_qc/REPORT.md`)
- Publishing: **not authorized**
- **9:16 Short built (2026-08-30, re-rendered 2026-08-31):** `short/2026-08-30-the-check-that-never-once-fired-short.mp4` — **1080x1920, 137.83s**, the whole reel reformatted (under the 180s Shorts cap, so 0 beats dropped, all 9 beats' narration reused unchanged, plus a silent branded 4.5s END card). All 9 GRAPHIC beats got a hand-authored portrait `short/scenes.py` (never auto-cropped, per THE REFORMAT RULE) — see `BUILD-LOG.md` for the 3 beats that needed a genuine top-to-bottom redesign (B04's real-filing-vs-condition, B05's five-feed results table, B06's before/after fix — each converted from the parent's side-by-side layout to a stacked one with a horizontal divider) and the real layout/QC bugs GATE B and GATE V caught and fixed along the way (B04 caption running off-frame, B05 header/caption crossing the safe ceiling/floor, B06's AFTER code block crossing the safe floor, B02's "0 MATCHES" stamp box and B05's CFTC highlight box both edge-bleeding past the safe x-extent, B07's canvas underfill). GATE V clean (0 BLOCKER/0 MAJOR) on all 9 authored scenes; 2 MAJOR remain on the toolkit's own auto-generated silent END card (a human design call, not fixable without editing `brutalist/`).

## Deliverables

- `Mycroft_SaiPranaviJeedigunta_20260830b_16x9.mp4` — 4K (3840x2160) master, 133.32s
- `Mycroft_SaiPranaviJeedigunta_20260830b_9x16.mp4` — portrait (1080x1920) short, 137.83s

(The `b` suffix disambiguates this video from another Mycroft video already published for the same date, `Mycroft_SaiPranaviJeedigunta_20260830_16x9.mp4`, from a different fix in the same pipeline.)

<!-- BEGIN BRUTALIST REBUILD GUIDE -->

# The Check That Never Once Fired

## What this video is about

**Topic:** A safeguard written to catch a specific category of filings that, tested against real live data, never once matched — in Project 29's regulatory-intel pipeline

This is Bella, in for Humanitarians AI. Sai Pranavi found a source classifier in the same regulatory pipeline as the two prior reports whose CFTC-detection rule looked correct on paper but, tested against every real CFTC filing available today, caught none of them — because it was checking for strings that structurally can't appear in the feed's real title/link format. The video walks through the hook, the live proof across all 5 feeds, and the fix.

The current plan contains **9 beats** over roughly **134 seconds** (4K, 3840x2160) — a silent title card and a spoken executive-summary/personal-intro card up front, then hook through sign-off.

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

> Audit `beat_sheet.json` beat by beat. Extract every factual, numerical, and named-entity claim (the CFTC-detection condition's exact string checks, the 5-feed test counts, the named example filing and its fields, the before/after `identifySource()` code). Check each against `B2-VERIFICATION.md` and `logs/RUN_LOG.md` in the `mycroft` repo referenced in `SOURCES.md`. Produce a table with beat ID, claim, verdict (SUPPORTED / QUALIFY / UNSUPPORTED / OUTDATED), evidence, source, and required correction. Flag any claim that generalizes a single live test into a permanent historical claim about the pipeline's full run history. Do not silently repair the script: list every proposed change for human review.

## Build and review loop

1. **Fact-check:** resolve every claim in `FACTCHECK.md` against the actual pipeline code and a live query before narration is finalized. (Done for this cut — see the resolution notes there.)
2. **Gate P — narration review:** read every line aloud; confirm the live-test framing and the 5-feed counts are still accurate as of build time (the feeds are live and change daily).
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
