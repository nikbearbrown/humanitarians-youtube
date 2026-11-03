# Weekly Research Report: The Link That Pointed Nowhere

**Fellow:** Sai Pranavi J.
**Week ending:** September 14, 2026
**Project:** Project 29 — Financial Regulatory Intelligence System (`mycroft` repo,
`scripts/regulatory-intel/`)
**Source status:** Real engineering work. Every claim traces to
`B3-VERIFICATION.md` (2026-08-31) — a reverse-engineered Google News link decoder, a
classification-ordering near-miss caught before deploying, and three escalating live
verification rounds (20/20, 16/16, 6/6). See `SOURCES.md` and `FACTCHECK.md`.

## Watch

- Folder (landscape + vertical 4K deliverables): [Drive link](https://drive.google.com/open?id=1cQ5xt_bs14AGbVy4HNgD61kXYp-0fAGA) — open the GoogleNewsLinkFix subfolder inside.

This ~2.7-minute AI-generated video asks: **what does it take to actually resolve a Google
News redirect link, and what almost broke while fixing it?** It is the fifth report in the
"Layer 1 hardening" series. The old `url=([^&]+)` regex never matched modern Google News
redirect links — the stored links were dead ends, bouncing back to Google News, never the
article. The real fix required reverse-engineering how the redirect page itself resolves the
link: a signed id/timestamp/signature POSTed to an internal Google endpoint. Along the way, a
classification-ordering near-miss was caught before it ever shipped — reordering when the
source classifier runs relative to the unwrap step would have quietly broken labeling for
every Google News item the moment the fix started working.

## What this covers (and what it deliberately flags as unverified)

The fix is real and reverse-engineered, not documented/official — B04's on-screen caveat label
("reverse-engineered — not a documented/official API") is FACTCHECK-required and held for the
whole beat so it can't be missed. B05 shows both call orders side by side: the old order
(classify **after** unwrap, which never mattered while unwrapping was broken, but would have
silently mislabeled every Google News item the moment it started working) and the fixed order
(classify on the raw link **before** unwrapping). B06 walks through all three escalating
verification rounds (20/20, 16/16, 6/6), not just the strongest one. B07 keeps two honest
limitations at full weight, neither softened: this fix is **not verified against the fellow's
live n8n instance** (only the workflow file and a full local re-implementation), and it adds
**~400 extra requests per run**, sequential by deliberate choice, not parallelized.

## Production state

- Plan: **approved** — 2026-09-17 (Gate P)
- Fact-check gate: **resolved** — see `FACTCHECK.md` (B04's reverse-engineered/undocumented
  caveat strengthened with an on-screen label; B07's two limitations kept at full weight)
- Narration approval: **approved** — 2026-09-17, cleared for audio generation
- Voice: **Bella (`af_bella`)** — locked for this fellow's whole report series, unchanged from
  prior episodes
- Audio lock: **locked** — Kokoro `af_bella`, all 10 beats (measured 4.05/17.18/10.78/18.82/
  19.73/28.66/23.54/24.58/7.87/5.78s, total 160.99s)
- Previz: **complete** — 10/10 beats real Manim (no slates); `scenes.py` (landscape) and
  `vertical/scenes.py` (native portrait) both hand-authored
- Visual QC: **0 BLOCKER, 0 MAJOR** on both true clean 4K masters (20 frames sampled each,
  `--lenient`; see `_qc/REPORT.md` and `vertical/_qc/REPORT.md`) — personally spot-checked by
  extracting real frames: B04's caveat label and B05's two call-order diagrams are both clearly
  legible in the landscape and vertical masters
- Publishing: **not authorized**

## First video under the NEW toolkit submission spec

This is the first video in this fellow's series built under the toolkit's NEW submission spec
(`brutalist/docs/FELLOWS-SUBMISSION.md`, effective 2026-09-07):

- Deliverable naming is `ProjectName_VolunteerName.mp4` — no date or aspect-ratio suffix.
- Landscape and vertical masters live in separate `deliverables/landscape/` and
  `deliverables/vertical/` folders, not a single reel folder with a `-vertical` suffix.
- The vertical companion is a **true 4K, full-length, native-portrait rebuild** via
  `./art vertical` — every beat hand-authored in `vertical/scenes.py` for the 9:16 canvas, not
  the old 1080x1920 Shorts-style reformat/crop this fellow's earlier videos used. Both masters
  run the same 161.125s, same 10 beats, same narration.

## Deliverables

- `deliverables/landscape/GoogleNewsLinkFix_SaiPranaviJ.mp4` — 4K (3840x2160), 161.125s
- `deliverables/vertical/GoogleNewsLinkFix_SaiPranaviJ.mp4` — 4K full-length vertical
  (2160x3840), 161.125s
- Both ship with a matching `.verified.json` receipt (SHA-256 of the output plus every input
  clip/audio file hashed).

<!-- BEGIN BRUTALIST REBUILD GUIDE -->

# The Link That Pointed Nowhere

## What this video is about

**Topic:** Reverse-engineering a working Google News link decoder, and a classification-
ordering near-miss caught before it ever shipped, in Project 29's regulatory-intel pipeline

This is Bella, in for Humanitarians AI. Sai Pranavi found that every Google News item's stored
link was a dead end — the classifier's old regex never matched modern redirect links. The real
fix meant reverse-engineering how the redirect page itself resolves the article: a signed
id/timestamp/signature POSTed to an internal Google endpoint, not a documented API. Fixing that
surfaced a second, subtler bug — the order in which classification and unwrapping ran would
have silently broken source labeling for every Google News item the moment the link-resolution
fix started working, caught before it ever deployed. The video walks through the dead-end
setup, the discovery of the real resolution mechanism, the near-miss and its fix, three rounds
of escalating live proof, and two limitations flagged honestly rather than glossed over.

The current plan contains **10 beats** over roughly **161 seconds** (4K, 3840x2160 landscape
and a full native-portrait 2160x3840 vertical companion) — a silent title card and a spoken
executive-summary/personal-intro card up front, then hook through sign-off.

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
this project, start with `beat_sheet.json`. **Preserve it before experimenting — make a copy or
a branded variant rather than overwriting a finished plan.** If this video needs a substantially
different cut (different bug, different voice, different length), create a new sibling folder
rather than editing this one in place.

Recommended builder: **`ai-explainer`** — one tight insight, not a multi-act documentary.

## Fact-check prompt

Run this after editing the narration:

> Audit `beat_sheet.json` beat by beat. Extract every factual, numerical, and named-entity claim
> (the failing regex vs. real link shape, the id/timestamp/signature resolution mechanism, the
> classification-ordering near-miss and both call orders, the three verification round counts,
> the two honestly-flagged limitations). Check each against `B3-VERIFICATION.md` in the `mycroft`
> repo referenced in `SOURCES.md`. Produce a table with beat ID, claim, verdict (SUPPORTED /
> QUALIFY / UNSUPPORTED / OUTDATED), evidence, source, and required correction. Flag any beat
> that implies the reverse-engineered resolution mechanism is a stable, documented public API, or
> that overstates production verification beyond what the source doc supports. Do not silently
> repair the script: list every proposed change for human review.

## Build and review loop

1. **Fact-check:** resolve every claim in `FACTCHECK.md` against the actual pipeline code and the
   live verification rounds before narration is finalized. (Done for this cut — see the
   resolution notes there.)
2. **Gate P — narration review:** read every line aloud; confirm the reverse-engineered/
   undocumented framing and the honest limitations are still accurate as of build time.
3. **Generate local audio:** Kokoro voice `af_bella` (Bella), Pragmatist register.
4. **Compile the previz:** render locally; missing beats stay as honest labeled slates until
   built. (All 10 beats are real Manim scenes in both `scenes.py` and `vertical/scenes.py`.)
5. **Watch, refine, and repeat.**
6. **Publish only by human decision** — a successful local render is not upload authorization.

## Useful project files

- `beat_sheet.json` / `vertical/beat_sheet.json` — narrative and visual plan for each aspect
- `scenes.py` — Manim source for all 10 landscape beats (the actual video content)
- `vertical/scenes.py` — hand-authored native-portrait (9:16) relayout of all 10 beats
- `BUILD-LOG.md` — dated build decisions and gate history
- `FACTCHECK.md` — claim-level evidence and corrections
- `SOURCES.md` — research, repo paths, and citation status
- `SHOTLIST.md` / `vertical/SHOTLIST.md` — beat-by-beat medium/timing table for each aspect
- `PROMPTS.md` — pantry/asset status (N/A — all beats are self-contained Manim)

<!-- END BRUTALIST REBUILD GUIDE -->
