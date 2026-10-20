# PEDAGOGY — "SQL, Read Fewer Rows." (ai-explainer · claude-hai · Bella)

Reel: `fellows/supriya-k/2026-09-16-sql-query-optimization-for-analytics`
Fellow: Supriya Kushwaha · weekly report, 2026-09-16 · playlist `Fellows Research`

## The ONE insight

> **An index works on the column, not on a function of the column — and the query
> plan is the only place that difference is visible.**

Everything in the reel exists to land that sentence. The audience is the
`claude-hai` audience defined in `skills/make/ai-explainer/SKILL.md`: students and
early-career analysts who can already write *correct* SQL and have never opened a
query plan. Their failure mode is not bad syntax — it is believing that two queries
which return the same answer cost the same.

The channel's spine question ("when to use AI and when NOT to") lands here as:
**do not ask a model whether your query is slow — ask the database, then ask the
model to interpret the plan.** B02's narration says exactly that, and the B08
handoff prompt is built on it: the viewer brings the plan, Claude reads it.

## Act structure (laws, checked)

| Law | Where | Status |
|---|---|---|
| COLD OPEN LAW — B00 is `ClaudeComposerAsk`, no brand card first, RESULT lines present | B00 | ✓ three output lines; the ask lands answered |
| ILLUSTRATE LAW — UI only at cold open / ask micro-beats / verdict / handoff / outro | B00 · B02 · B07 · B08 · B09 | ✓ exactly the five exempt slots |
| ILLUSTRATE LAW — no two consecutive beats share a scheme | B01→B06 | ✓ isotype attrition → UI ask → plan capture → log scale → predict card → divergence |
| ASK → RESULT LAW | B02 → B03 | ✓ the ask micro-beat shows the real invocation; B03 is what it produced |
| SPARK-LINE LAW — no lonely asterisk on inner beats | B03 · B05 | ✓ `sparkLine` on both; B00's spark line is the greeting |
| HANDOFF LAW — second-to-last beat, `greeting: "Your turn."`, prompt READ and DISCUSSED | B08 | ✓ read verbatim, then two sentences of discussion |
| OUTRO LAW — title restate, poster serif, handle beneath | B09 | ✓ `ClaudeTitleOutro` |
| SHOW-DON'T-TELL LAW — every beat carries a `show` block authored BEFORE narration | all 10 | ✓ `shot.show` on every beat |
| THE PPT TEST | all | ✓ no beat is a headline-plus-paragraph. B05 is a deliberate HOLD (a commit device), not a slide |
| LOGO LAW | all | ⚠ **open** — see Open items |
| IN-FOR-BEAR LAW | n/a | correctly NOT armed: voice is `af_bella`, not `am_onyx` |

## SHOW before TELL — how each body beat MOVES

Motion enacts the sentence, never decorates it (MOTION.md: motion is subordinate
to information delivery).

- **B01** — 400 isotype dots don't illustrate attrition, they *perform* it: 97% of
  them fall out of frame on the spoken filter, and the counter counts down with
  them. The viewer feels the ratio before hearing the number.
- **B03** — the terracotta highlight moves from `SCAN` to `SEARCH … USING INDEX`
  on the spoken words, one accent at a time (accent law: if two things are orange,
  neither is the point). The evidence is read by the viewer; the voice only judges.
- **B04** — the markers *travel* to their values on the spoken figure, so 35×
  arrives as a distance, not as a claim. Draw-on at constant velocity per MOTION.md §4.
- **B06** — two tracks leave one origin and physically diverge at the spoken word
  "strftime". The shape of the graphic *is* the argument.

## Friction protected (germane) vs removed (extraneous)

**Kept — this friction teaches:**
- **B05 PREDICT.** The viewer commits to an answer before B06 reveals it. Costs
  13 s and is the single highest-value beat in the reel: the insight is a
  *correction* to an intuition ("I indexed the column, so I'm fine"), and
  corrections only stick if the wrong intuition is stated first.
- **B01's full 400-dot density.** Could have been a number on a card. The dot field
  is slower and the point is that it *feels* like too much work.
- **B03 shows the plan UNEDITED**, tree-drawing characters and all. Slightly harder
  to read than a cleaned-up version, and that is deliberate: the viewer has to
  recognise this output in their own terminal.

**Removed — extraneous for a one-insight reel:**
- Covered indexes, `INCLUDE` columns, and index-only scans. A second insight.
- `EXPLAIN ANALYZE`, buffer counts, and cost estimates. The reel deliberately
  claims only what `EXPLAIN QUERY PLAN` shows, which is why no cost numbers appear.
- Partitioning, materialised views, columnar stores. The real answer for many
  analytics workloads, and a different video.
- `date_trunc` entirely. It behaves identically, but it is a PostgreSQL function
  with no SQLite equivalent, so it could not be executed against this fixture —
  and an unmeasured name sitting in a list of measured ones is exactly what
  DOUBLE-CHECK LAW exists to catch. Removed from the voice and the artifact card;
  it lives in the description, labelled as documented rather than demonstrated
  (`FACTCHECK.md` row 12c, L2).
- Why `date_trunc` is sometimes fine in Postgres (expression indexes). Same
  reason as L3 — a second insight.

## Duration is an OUTPUT, not a target

Per `skills/make/duration-planner/SKILL.md`. Beats were sized by counting
interacting elements, then estimated from word count at ~160 wpm; the real clock is
the measured MP3 durations at audio lock.

- Estimated total: **209 s ≈ 3:29.**
- This is **above** the 1–3 minute band named in the build brief. The content put
  it there: one insight, but it needs a setup, a real artifact, a magnitude, a
  commit, and a mechanism. Compressing narration to reach 3:00 would be a
  production compromise with a known learning cost, and the skill says to name that
  plainly rather than do it silently.
- **If a sub-3:00 cut is wanted:** drop **B04** (20 s — genuinely restates B03's
  figures on a log axis) and **B05** (13 s) → ≈ **2:56**. Dropping B05 costs the
  prediction effect; dropping B04 costs the least. That is Supriya's call, not the
  builder's.

### Consolidation floors (duration-planner table) vs estimates

| Beat | `content_type` | Floor | Est. | Verdict |
|---|---|---|---|---|
| B01 | data | ~6–8 s | 22 s | over floor; at ceiling — it is one idea (the funnel), so it holds |
| B03 | mechanism | ~6–10 s | 21 s | over floor; two plans = two steps, correctly one beat |
| B04 | data | ~6–8 s | 20 s | over floor |
| B05 | title | ~3–5 s | 13 s | deliberate HOLD past narration — the commit needs silence |
| B06 | mechanism | ~6–10 s | 25 s | at ceiling; split candidate if audio lock runs long |

Re-run `python3 skills/make/duration-planner/scripts/pace_check.py` against
`mp3/timings.json` after audio lock — it is advisory and never edits the sheet.

## Evidence discipline

Source of record: **`demo/RESULTS.md`** — real SQLite 3.45.3 `EXPLAIN QUERY PLAN`
captures for **three** pairs of logically identical queries (`strftime` on a DATE
column, `CAST` on an INTEGER column, `UPPER` on a TEXT column), regenerable with
`python3 demo/build_demo.py` (`SEED = 20260916`). The script compares each pair's
full result sets and **exits non-zero** if a rewrite stops being equivalent, so
the evidence cannot drift silently. Only pair 1 appears on screen (B03); pairs 2
and 3 exist to make B07's spoken list of functions executed evidence rather than
analogy.
Per-claim verdicts and citations: **`FACTCHECK.md`**. Corrections applied during
authoring and the rebuild/scaling decisions: **`SOURCES.md`**.

No figure appears on screen that is not in `demo/RESULTS.md`. The one scaled
graphic (B01's isotype, 1 dot = 1,000 rows) declares its scale in `slideMeta` and
is logged in `FACTCHECK.md` row 6.

## Open items before GATE P can be signed

0. ~~**`FACTCHECK.md` L2**~~ — **CLOSED 2026-09-16.** The fixture was extended to
   three executed pairs (`strftime`, `CAST`, `UPPER`), and `date_trunc` was
   dropped from B07's spoken list *and* its artifact card, since it is a
   PostgreSQL function that can never be executed against a SQLite fixture. It
   now lives only in the video description. Every function the narration names is
   measured evidence. `NARRATION-GATE-P.md` is at **rev 2** — sign that revision,
   not rev 1. `FACTCHECK.md` **L5** (the `UPPER` rewrite is collation-dependent)
   is mitigated in the description, also closed.
1. **LOGO LAW** — every beat needs the `@HumanitariansAI` mark as a small
   low-opacity lower-right bug inside the title-safe inset. `folderLabel` puts the
   handle in the composer chrome on the UI beats, but the five body beats
   (`AttritionChain`, `SqlPlanBeat`, `ScaleComparison`, `SqlPredictCard`,
   `DivergentFates`) have no logo slot. The library patterns do not accept one.
   Logged in `TEMPLATE-MISSES.md`; resolve before render, not after.
2. **Reel-local scenes must be registered** in `runtime/remotion/src/Root.tsx`
   before `remotion_scenes.py` can render B03 and B05 — see `remotion-src/REGISTER.md`.
3. **Two overflow risks I could not verify without rendering** (rendering is out of
   scope for this scaffold): B03's plan text and B06's track labels. Both are listed
   as named QC watch items in `SHOTLIST.md` §QC watch list.
4. **Voice approval** — `fellows/README.md` requires the fellow's approval before
   the first audio generation. `af_bella` is already this fellow's series voice;
   confirm once here.

---

**VERDICT: PASS**

Signed by: **Supriya Kushwaha** (Fellow) · Date: **2026-09-16**
Voice: **af_bella confirmed as my series voice (Bella, HAI plain register).**
Reviewed: all 10 beats and this document. `NARRATION-GATE-P.md` signed at rev 2.
`FACTCHECK.md` L4 re-read complete — rows 10, 11 and 12c confirmed against the
cited documentation on 2026-09-16.

**Scope of this signature.** GATE P is the narration/pedagogy gate, and it is
PASSED. Two open items survive it deliberately and are NOT covered by it:

- **Open item 1 (LOGO LAW) is still undecided.** It does not block a review cut,
  but the reel is **not clear for a final master** until the brand bug exists on
  the five body beats. Decision recorded here when made: ________________
- **Open item 3 (overflow risks Q1/Q2)** can only be assessed from rendered
  frames. `_qc/REPORT.md` must show zero BLOCKER and zero MAJOR before the
  master is called done.

This signature authorises **audio generation and rendering**. It does not
authorise calling the master finished, and it does not authorise publishing —
there is no publishing machinery in this toolkit.

---

## Rev 3 addendum (2026-10-17, v2 rebuild)

The pedagogical shape above is unchanged: same one insight, same ten beats in the
same order, same predict → reveal device, same single takeaway. What changed is the
narration (rev 3: tightened from 180.57s to fit a full-length 9:16, plus the accuracy
fixes C1–C6 in `FACTCHECK.md`).

The rev 3 narration was signed at GATE P in `NARRATION-GATE-P.md`:
**VERDICT: PASS — Supriya Kushwaha (human, author), 2026-10-17, rev 3.**
The rev 2 signature above applies to rev 2 only.
