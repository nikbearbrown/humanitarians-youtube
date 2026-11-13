# Week 8: SQL Query Optimization for Analytics

**Date:** 2026-09-21

## Videos
Final masters are committed in this folder and also on Google Drive: https://drive.google.com/drive/folders/1hc5iSRgrSYF35AxXHg4GGKxZyQFdrHN7

| File | SHA-256 |
|---|---|
| 2026-09-21-sql-query-optimization-for-analytics.mp4 (16:9) | 0eb71b8a390d289cdefdf6fb78119001ae4aa790d13ba2e80bd54589a758a277 |
| 2026-09-21-sql-query-optimization-for-analytics-vertical.mp4 (9:16) | 9313f8682224dd2af29b7a79d51fa522909affc2a8bc2d2bb7564bbf3c5ee5f2 |

Verify: `shasum -a 256 <file>` and compare to the hash above.

## Contents
beat_sheet.json, a 400k-row SQLite fixture (demo/), PEDAGOGY.md, FACTCHECK.md, NARRATION-GATE-P.md (rev 3 signed), FRICTIONAL.md.

## Built with
brutalist.art (ai-explainer skill, Claude-hai persona, Kokoro af_bella)

---

## Full reel documentation

# SQL, Read Fewer Rows.

**Fellow:** Supriya Kushwaha · AI+1 Humanitarians AI fellow
**Weekly report:** 2026-09-16
**Skill:** `ai-explainer` (Brutalist, free-only edition)
**Channel:** `claude-hai` → `@HumanitariansAI` · playlist `Fellows Research`
**Voice:** Kokoro `af_bella` ("Bella") — this fellow's series voice
**Status:** **v2 MASTERS DELIVERED (2026-10-17).** See "v2 rebuild" below. The sections after it describe the original Sep 16 build and are kept as history.

## v2 rebuild (2026-10-17)

Moved into `brutalist.art/projects/` from `humanitarians-youtube/fellows/supriya-k/` and
rebuilt to the PM requirements. Baseline commit `fb0c727` holds the Sep 16 state.

| | v1 (Sep 16) | v2 (Oct 17) |
|---|---|---|
| 16:9 master | 0.43 Mbps · 180.57s | `2026-09-21-sql-query-optimization-for-analytics.mp4` — 3840×2160 · **1.06 Mbps** · 162.1s |
| 9:16 master | 0.39 Mbps · 180.57s | `2026-09-21-sql-query-optimization-for-analytics-vertical.mp4` — 2160×3840 · **0.96 Mbps** · 166.6s (all 10 beats + endcard) |
| Intro | "Hi, I am Supriya**,** and…" | exact: "Hi, I am Supriya and this video is about…" |
| Branding | `@HumanitariansAI` chips; Supriya only in greetings | "Supriya" chip on every beat; `@HumanitariansAI` small on outro + endcard |
| Gate V (clean cuts) | 2 accepted MAJORs (B03, B05) | **0 BLOCKER · 0 MAJOR** on both masters |

- **Bitrate:** encoded at `--vbitrate 25M`. The encoder saturates on this near-static content
  (60M → 1.17 Mbps), so ~1 Mbps is the honest ceiling without padding.
- **Narration rev 3** (GATE P signed by Supriya 2026-10-17, `NARRATION-GATE-P.md`): tightened
  180.57s → 162.1s with no beat cut; accuracy fixes C1–C6 in `FACTCHECK.md` ("compare the bare
  column", "a plain index", "costs almost nothing", no "byte for byte", no on-screen ms timings).
- **Visual fixes:** B01 per-panel figures (400,000 / 11,369 / 4,459); B03 plan text auto-fit and
  centred (cannot clip); B05 question scaled and centred; B01/B06 and all portrait headers moved
  inside the 5% title-safe inset; "Claude" model label; filled outro.
- **9:16** is built in `short/` by `./art shorts`; the old `vertical/` build folder was deleted
  after the new cut was verified (Supriya, 2026-10-17). Portrait-only prop changes are recorded
  in `beat_sheet.json` → `metadata.portrait_overrides`.
- **CRF masters kept:** `_crf16-master.mp4`, `short/_crf16-short-master.mp4`.
- **Listen check still open:** Kokoro's reading of "strftime" (B03, B06, B07) and "posted-at
  column" (B06) has not been machine-verified — the local transcriber is broken by a NumPy
  version conflict.

## The one insight

> An index works on the column, not on a function of the column — and the query
> plan is the only place that difference is visible.

## What is in here

| File | What it is |
|---|---|
| `beat_sheet.json` | The master. 10 beats, each with a `show` block, a Remotion pattern, and props. `actual_duration_s` is `null` until audio lock. |
| `NARRATION-GATE-P.md` | Every line of narration for human sign-off. **Unsigned.** Nothing generates audio until it reads `VERDICT: PASS`. |
| `PEDAGOGY.md` | Why the reel is shaped this way: the one insight, the law checks, friction kept vs cut, duration as an output, four open items. **Unsigned.** |
| `FACTCHECK.md` | Every claim, graded by how it was verified (EXECUTED / DOC / ARGUMENT), plus four stated limitations. |
| `SOURCES.md` | Primary evidence, documentation cited, toolkit doctrine followed, and nine authoring decisions logged. |
| `SHOTLIST.md` | The typed work order: ten slots, the scheme histogram, and seven named QC watch items. |
| `BUILD-PROMPT.md` | The single paste-ready prompt that takes this to a master. Gate-checks first; never publishes. |
| `demo/` | **Executable evidence.** Real SQLite, six real `EXPLAIN QUERY PLAN` captures across three query pairs. Deterministic, regenerable, self-asserting. |
| `remotion-src/` | Two reel-local scenes + `REGISTER.md`. Everything else is a library composition. |
| `*-youtube.md` | The video description, with chapters and the evidence note. |
| `media/`, `mp3/` | Empty. Machine-owned outputs. |

## Reproduce the evidence (~10 seconds, no keys, no network)

```bash
cd demo
python3 build_demo.py     # 400,000-row SQLite fixture + six EXPLAIN captures
python3 timing.py         # measured wall-clock, all pairs (supporting evidence only)
```

Expected: `rows=400000  jan2026_rows=11369`, `selectivity = 2.84%`, then three
pairs each reporting `same result set: True` and a wrapped `SCAN postings` against
a bare `SEARCH … USING INDEX`, ending in
`all pairs verified: every rewrite returns an identical result set`.

The script **exits non-zero** if any rewrite stops being equivalent — the evidence
checks itself rather than trusting the author.

## Next steps, in order

1. ~~Decide `FACTCHECK.md` L2~~ — **closed 2026-09-16.** The fixture executes
   `strftime`, `CAST` and `UPPER` as three verified pairs, and `date_trunc` was
   dropped from B07's spoken list and artifact card (it is a PostgreSQL function,
   never executable here). Every function the narration names is measured
   evidence. **`NARRATION-GATE-P.md` is now rev 2 — sign that revision.**
2. ~~`FACTCHECK.md` L5~~ — **closed.** The `UPPER` rewrite is collation-dependent;
   a two-sentence caveat now sits under the takeaway in the description, which
   costs no re-gate and no re-render.
3. Decide `PEDAGOGY.md` open item **1** (LOGO LAW — the five body patterns have no
   brand-bug slot). See `brutalist.art/TEMPLATE-MISSES.md` #3.
4. Review the narration on an **animated slate**, not on the page.
5. Sign `NARRATION-GATE-P.md` and `PEDAGOGY.md`.
6. Then, and only then, run `BUILD-PROMPT.md`.

## Accepted defects for this cut (2026-09-16)

`_qc/REPORT.md` pass 2 closed both BLOCKERs. Two MAJORs remain and are
**accepted, not fixed**, for this week's submission. Both are **cosmetic
canvas-fill only** — no evidence is hidden, no claim is misstated, no text is
clipped or occluded. Neither affects what the reel says or proves.

| Beat | Defect | Why accepted rather than fixed |
|---|---|---|
| **B03** `SqlPlanBeat` | Plan text fills only the top ~45 % of each card; mono at `H×0.0205` = 22.1 px effective at 1080, marginally under the 24 px legibility floor (legible in practice — verified by reading frames). | The fix is to raise the font size, which **re-opens the Q1 clipping risk this scene exists to avoid**. `ClaudeCodeBeat`-lineage layout uses `whiteSpace: 'pre'` + `overflow: hidden`, so long lines clip silently with no error. The longest line in the reel already lands only ~60 px inside the card border. Raising type without re-running a full QC pass on this beat risks trading a cosmetic defect for a content-destroying one. |
| **B05** `SqlPredictCard` | Content in the top ~46 %; bottom half of the frame is empty cream. | The layout belongs to the library `PredictCard`; `SqlPredictCard` is a props wrapper only. Fixing means **forking a second library component** and re-testing its motion — scope this submission does not need. The question type is large, centred and fully legible; the beat is a deliberate HOLD for the viewer to commit. |

Both are downgraded to **MINOR for this cut** on that reasoning. They are
recorded here so the decision is explicit rather than an oversight, and so a
later pass can pick them up:

- **B03** — bump the mono multiplier and re-run QC *on B03 specifically*,
  watching the `SEARCH … idx_postings_posted_at (posted_at>? AND posted_at<?)`
  line, which is the one closest to the card edge.
- **B05** — fork `PredictCard` into `remotion-src/` and re-band it vertically,
  the same way the three deck-pattern forks were done.

Still genuinely open and **not** accepted: **LOGO LAW** (no brand bug on any
beat — `PEDAGOGY.md` open item 1, `TEMPLATE-MISSES.md` #3). That one blocks
calling this a final master.

## Free-tier discipline

No API key, no paid voice, no paid service, anywhere in this reel or its evidence.
Kokoro TTS, Remotion, Manim, ffmpeg, SQLite — all free and local. If any step
appears to require a credential, that is a toolkit bug (brutalist `CLAUDE.md`
rule 7): stop and report it rather than supplying one.

**Never publishes.** There is no publishing machinery in this toolkit. The master
stays in this folder for human review.
