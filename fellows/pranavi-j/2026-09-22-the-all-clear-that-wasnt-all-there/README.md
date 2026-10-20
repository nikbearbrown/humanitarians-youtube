# Weekly Research Report: The All-Clear That Wasn't All There

**Fellow:** Sai Pranavi Jeedigunta
**Week ending:** September 22, 2026
**Project:** Project 29 — Financial Regulatory Intelligence System (`mycroft` repo,
`scripts/regulatory-intel/`)
**Source status:** Real engineering work. Every claim traces to `B5-VERIFICATION.md`
(2026-09-29) and the matching `logs/RUN_LOG.md` entry. See `SOURCES.md` and `FACTCHECK.md`.

## Watch

- Landscape (4K 16:9): [Drive link](https://drive.google.com/open?id=1HM-Vd1oQxWg8Km2WhpVQMPIclhh7QRaK)
- Vertical (4K 9:16): [Drive link](https://drive.google.com/open?id=1ixcfy8IkRX_OtyYb7ftyoQKgu1znIHUU)

This ~1.8-minute AI-generated video asks: **can a status email that says "all clear" be wrong
about what it even checked?** The pipeline's own "all clear" run-summary email — the one sent
when a scheduled scan finds nothing high-priority — has a "Monitored Sources" section, a static
hand-written grid. That grid listed only 4 of the pipeline's 5 real RSS feeds. Investment Advisor
Rules, a real working source node in the workflow, was missing from both the grid and the summary
sentence. Fixed by adding the missing card and verified by diffing every source-card label against
the workflow's actual feed-node names, one for one.

## What this covers (and what it deliberately leaves out)

B03 recreates the email's real shipped 4-card grid verbatim, not a constructed example. B04 puts
the 4 shown source names next to the workflow's real 5 RSS-feed node names, the missing 5th
(Investment Advisor Rules) clearly highlighted as absent — both lists visible together is the
point. B05 shows the fix: before (4 cards) and after (5 cards) side by side, the added card
highlighted, plus the conformance check passing. B06 is a brief aside, clearly framed as a closed,
stale note — not implied as still open: an older `FINDINGS.md` item ("apply A4/B4 to Generate
Email") was checked and confirmed already fixed since the very first hardening commit, before
`FINDINGS.md` was even written; no code change was needed there. The video deliberately leaves out
anything beyond this: it is a display-only fix to a status email — no scoring, classification, or
alert-routing logic changed.

## Production state

- Plan: **approved** — 2026-09-29 (Gate P)
- Fact-check gate: **resolved** — see `FACTCHECK.md` (B06's aside kept as drafted)
- Narration approval: **approved** — 2026-09-29, cleared for audio generation
- Voice: **Bella (`af_bella`)** — locked for this fellow's whole report series, unchanged from
  prior episodes
- Audio lock: **locked** — Kokoro `af_bella`, all 9 beats (measured 4.049/14.23/9.74/14.02/11.66/
  16.51/20.26/12.0/5.06s, total 107.537s; B00 is a silent title card)
- Previz: **complete** — 9/9 beats real Manim (no slates); `scenes.py` (landscape) and
  `vertical/scenes.py` (native portrait) both hand-authored
- Visual QC: **0 BLOCKER, 0 MAJOR** on both true clean 4K masters (18 frames sampled each,
  `--lenient`; see `_qc/REPORT.md` and `vertical/_qc/REPORT.md`) — personally spot-checked by
  extracting a real frame from every one of the 9 vertical beats: no `Text()` word-gap artifacts
  anywhere, 58-92% safe-area canvas-fill, no clustered/negative-space layouts
- Publishing: **not authorized**

## First video under the NEW toolkit submission spec

This is the first video in this fellow's series built under the toolkit's NEW submission spec
(`brutalist/docs/FELLOWS-SUBMISSION.md`, effective 2026-09-07):

- Deliverable naming is `ProjectName_VolunteerName.mp4` — no date or aspect-ratio suffix.
- Landscape and vertical masters live in separate `deliverables/landscape/` and
  `deliverables/vertical/` folders, not a single reel folder with a `-vertical` suffix.
- The vertical companion is a **true 4K, full-length, native-portrait rebuild** via
  `./art vertical` — every beat hand-authored in `vertical/scenes.py` for the 9:16 canvas, not a
  Shorts-style reformat/crop. Both masters run the same 107.708s, same 9 beats, same narration.

## Deliverables

- `deliverables/landscape/AllClearEmailFix_SaiPranaviJeedigunta.mp4` — 4K (3840x2160), 107.708s
- `deliverables/vertical/AllClearEmailFix_SaiPranaviJeedigunta.mp4` — 4K full-length vertical
  (2160x3840), 107.708s
- Both ship with a matching `.verified.json` receipt (SHA-256 of the output plus every input
  clip/audio file hashed).

<!-- BEGIN BRUTALIST REBUILD GUIDE -->

# The All-Clear That Wasn't All There

## What this video is about

**Topic:** A small, real display bug in Project 29's regulatory-intel pipeline — the "all clear"
status email's "Monitored Sources" grid quietly under-reported its own source count

This is Bella, in for Humanitarians AI. Sai Pranavi found that the pipeline's routine "all clear"
status email — the one sent when a scheduled scan finds nothing high-priority — described itself
wrong. Its "Monitored Sources" grid, a static hand-written section, listed only 4 of the 5 real
RSS feeds the pipeline actually watches. Investment Advisor Rules, a real working source node in
the workflow, was simply never added to the card. The video walks through the email as it shipped,
the real workflow node names it should have listed, the fix (the missing card, added and verified
one-for-one against the workflow), and a brief honest aside: an older open item from `FINDINGS.md`
turned out to already be fixed, confirmed rather than re-patched.

The current plan contains **9 beats** over roughly **108 seconds** (4K, 3840x2160 landscape and a
full native-portrait 2160x3840 vertical companion) — a silent title card and a spoken
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
this project, start with `beat_sheet.json`. **Preserve it before experimenting — make a copy or a
branded variant rather than overwriting a finished plan.** If this video needs a substantially
different cut (different bug, different voice, different length), create a new sibling folder
rather than editing this one in place.

Recommended builder: **`ai-explainer`** — one tight insight, not a multi-act documentary.

## Fact-check prompt

Run this after editing the narration:

> Audit `beat_sheet.json` beat by beat. Extract every factual, numerical, and named-entity claim
> (the 4-card grid as shipped, the workflow's real 5 RSS-feed node names and which one is missing,
> the fix and its one-for-one verification against the workflow, the stale `FINDINGS.md` item and
> its already-fixed status). Check each against `B5-VERIFICATION.md` in the `mycroft` repo
> referenced in `SOURCES.md`. Produce a table with beat ID, claim, verdict (SUPPORTED / QUALIFY /
> UNSUPPORTED / OUTDATED), evidence, source, and required correction. Flag any beat that implies
> the stale-note aside (B06) is a new fix shipped in this video, rather than a confirmed-closed
> check. Do not silently repair the script: list every proposed change for human review.

## Build and review loop

1. **Fact-check:** resolve every claim in `FACTCHECK.md` against the actual pipeline code and
   `B5-VERIFICATION.md` before narration is finalized. (Done for this cut — see the resolution
   notes there.)
2. **Gate P — narration review:** read every line aloud; confirm the before/after source count and
   the stale-note framing are still accurate as of build time.
3. **Generate local audio:** Kokoro voice `af_bella` (Bella), Pragmatist register.
4. **Compile the previz:** render locally; missing beats stay as honest labeled slates until
   built. (All 9 beats are real Manim scenes in both `scenes.py` and `vertical/scenes.py`.)
5. **Watch, refine, and repeat.**
6. **Publish only by human decision** — a successful local render is not upload authorization.

## Useful project files

- `beat_sheet.json` / `vertical/beat_sheet.json` — narrative and visual plan for each aspect
- `scenes.py` — Manim source for all 9 landscape beats (the actual video content)
- `vertical/scenes.py` — hand-authored native-portrait (9:16) relayout of all 9 beats
- `BUILD-LOG.md` — dated build decisions and gate history
- `FACTCHECK.md` — claim-level evidence and corrections
- `SOURCES.md` — research, repo paths, and citation status
- `BEAT-SHEET.md` / `SHOTLIST.md` — human-readable beat-by-beat outline and medium/timing table
- `PROMPTS.md` — pantry/asset status (N/A — all beats are self-contained Manim)

<!-- END BRUTALIST REBUILD GUIDE -->
