# PLAN — banking-interview-end-to-end (whole-book trailer)

**Status: DRAFT — awaiting user gate approval. Nothing past this file is generated yet.**

## Pattern being followed

This project is a direct clone of the existing whole-book-trailer pattern at
`reels/da-interview-trailer/` (book: `books/data-analyst-interview-prep`). Same pipeline, same
schema, same palette family, same beat arc shape — no new machinery introduced. Per README.md /
BRUTALIST.md doctrine, this is a **previz path**: own title-card stills (via Manim, matching the
existing scenes.py pattern) + Kokoro (free, local) narration, compiled with ffmpeg. No paid keys,
no fill-in request cards needed (every beat is a self-made title/statement/list card, same as the
reference example).

## Source

- Book: `books/banking-data-analyst-interview-prep/` — 15 chapters, ~35,300 words.
- Core claim (from `vision.md`): a data analyst already strong in SQL/Python/stats still fails
  banking-industry interviews for one fixable reason — missing regulatory, risk, and
  unit-economics vocabulary — and this book closes that gap with banking-flavored original
  practice.
- Structure (from `outline.md`): Part I landscape (Ch.1-3) → Part II regulation/risk/governance
  (Ch.4-6) → Part III data stack (Ch.7) → Part IV SQL/Python technical (Ch.8-10) → Part V
  case/behavioral/systems (Ch.11-14) → Part VI day-of reference (Ch.15).

## Output location

`reels/banking-interview-end-to-end/` (this directory), mirroring exactly where
`da-interview-trailer` lives — at the toolkit repo root, not nested inside the book folder, per
the toolkit's own convention ("a reel may live anywhere"; the existing whole-book-trailer example
uses this same root-level `reels/` placement).

## Persona / compliance requirement

The existing reference example (`da-interview-trailer`) carries **no spoken persona line at all**
— it opens straight on the title card. This book's trailer adds exactly one line to satisfy your
compliance requirement, spoken in Beat 1 only, nowhere else in the toolkit's persona system
(`AUTHOR.MD`-driven hai/nbb/medhavy outros) applies here since this is a plain default trailer:

> "Hi, I am Supriya and this video is about how a data analyst who already knows SQL and Python can
> close the banking-specific vocabulary gap that actually fails interviews. This is Banking Domain
> Data Analyst Interview Prep."

*(Updated 2026-08-27 per revised compliance requirement: Supriya introduces herself by name and
states the topic directly, rather than an "in for Supriya" AI-narrator framing.)*

This attributes the work to you by name in the very first line, on-screen and narrated, before any
book content starts. No other beat changes.

## Beat arc (7 beats, same shape as the reference example)

| Beat | Role | Card kind | Content |
|---|---|---|---|
| B01 | Persona + title/hook | title | "in for Supriya" line + book title + one-line promise |
| B02 | The problem | statement | Strong in SQL/stats, but blindsided by banking vocabulary |
| B03 | The structure | list | The six-part arc: landscape → regulation/risk → data stack → SQL/Python → case/behavioral/systems → day-of |
| B04 | The stakes | statement | Each stage tests something different (vocabulary vs. mechanics) |
| B05 | Why 2026 | list | CECL, post-2023 regional-bank stress (LCR/CET1), AML/fraud-analytics growth, AI-tool fluency |
| B06 | The differentiator | statement | Every practice scenario is original — invented banks/portfolios, not a question dump |
| B07 | Close | title | "15 chapters. One path." + title reprise + CTA |

Estimated total runtime: ~95-105s (slightly longer than the 10-chapter reference's ~86s, since
this book has 15 chapters and one extra beat's worth of persona narration in B01).

## Schema / files to generate (after this plan is approved)

1. `beat_sheet.json` — same top-level shape as the reference (`metadata` + `beats[]`, fields:
   `beat_id, estimated_duration_s, narration_text, shot{type:STILL,source:own,motion:hold},
   card{kind,copy,sub|items}, audio_file`). `actual_duration_s` per beat gets filled in once Kokoro
   narration is generated and measured (Gate: "hear it / lock the clock" — never estimate from
   word count for the final cut).
   - `metadata.voice_kokoro`: `af_heart` (same as reference)
   - `metadata.ground` / palette: `newsprint` values, matching the reference exactly —
     `GROUND #F3EBDD, INK #2F2A26, RED #BF3339 (crimson), OCHRE #C8860E, SEC #6B6357`
   - `metadata.aspect_ratio`: `16:9`, `fit`: `pad`
2. `scenes.py` — one `BeatScene`-derived `Scene` class per beat (`B01`..`B07`), identical
   construction pattern to the reference: ochre corner mark → `Write` headline → `GrowFromEdge`
   red rule → `FadeIn` subtitle (title/statement), or `LaggedStart` bullet build (list). Each class
   padded to its beat's `actual_duration_s` once audio is locked. No LaTeX — Text/Pango only.
3. `make_cards.py` — copied from the reference (generic cairosvg title-card renderer, not
   book-specific) as the previz-stills fallback, same as the reference project ships one.

## Gates (in order — this project will stop at each one for your sign-off)

1. **This plan** — you review and mark it passed. *(current gate)*
2. **`beat_sheet.json`** — you review narration text, card copy, and beat count/order.
3. **`scenes.py`** — you review the Manim scene code (visual treatment, not yet rendered).
4. **Render gate** — only after (3) is approved: generate Kokoro audio per beat, measure real
   durations, run the toolkit's static QC gates if available
   (`runtime/qc/static_scene_check.py`, `runtime/qc/wcag_margin_check.py`), render each scene to
   `manim/<beat_id>.mp4`, run the post-render layout audit
   (`runtime/qc/manim_layout_audit.py --png`), then compile to
   `banking-interview-end-to-end-cut.mp4`. Watching the final cut is your call, same as every
   other reel in this toolkit — never automated.

No rendering, audio generation, or compilation happens before you approve the plan, then the beat
sheet, then the scene code, in that order.
