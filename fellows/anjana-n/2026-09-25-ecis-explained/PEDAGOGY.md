# PEDAGOGY — ECIS Episode 8: Reading Between the Lines (ai-explainer, narrated by Anjana)

Fresh build from the pre-authored `narration/*.txt` + `visuals/*.md` briefs in
this folder. One insight: for seven episodes ECIS read what management *said*.
Episode 8 turns back to the same transcript and reads *how* they said it — and
then asks the follow-up, whether the market had already worked it out before the
call.

Sequel to Episodes 1–7.

## Act structure

- B00 cold open, `ClaudeComposerAsk`, RESULT lines already resolved (COLD OPEN LAW) ✓
- ILLUSTRATE LAW: Claude UI appears only at B00 / B07 (verdict) / B08 (handoff) /
  B09 (outro). B01–B06 illustrate the mechanism — the recap and the magnifying
  glass, the three linguistic instruments, the three impact measurements, the
  drift chart, the database migration, the full-architecture close ✓
- SHOW-DON'T-TELL LAW: every body beat carries a `show` block; the evidence
  (the needles settling, the 0.5% bar beside the 12% bar, the amber pre-call
  shading with the line already climbing inside it, the query time striking
  through) lives on screen ✓
- your-turn closing standard: B07 VERDICT → B08 YOUR TURN → B09 TITLE outro ✓
- Narrator: Anjana, no channel handle. Source says `am_onyx` — overridden to
  `af_bella` per the series convention ✓
- Dark-stage deviation: B01–B06 on the dark ground, same PEDAGOGY-approved
  deviation as Episodes 1–7.
- **NARRATION BUDGET:** body beats run 51–84 words. B03 (84) and B05 (81) are
  over the 45–70 range — both logged as deviations below.
- **No real company names or tickers anywhere.**

## Three authoring decisions

**1. Palette — the same conflict as Episode 7, resolved the same way.** The
briefs again list hex values that contradict what Episodes 1–7 shipped (B01
calls the keyword reader white `#EAEAEA`, FinBERT blue, NER green; the series
has keyword blue `#3E7CB1`, FinBERT teal `#3EB8A8`, NER amber `#D9A757`). The
author confirmed for Episode 7 that the ESTABLISHED series palette wins and the
briefs' stated intent ("same shapes and colors") is honored over their hex list;
that resolution is now series law and is applied here without re-asking. The
mapping is unchanged from Episode 7's table.

`beats.json` also carries a `color_continuity` block mapping `llama: purple`,
`mistral: teal`, `qwen: amber`. No model is named anywhere in this episode's
narration, so the block is inert here; the reader colors it would affect are
already fixed by the series palette. Noted rather than applied.

**2. B06 was labelled "Your Turn" but is not one.** Same mismatch as Episode 7's
B06 and the embeddings explainer's B05: the narration is a close ("The system
now reads how management talks… Anjana here, thanks for watching") and the brief
is an architecture montage plus a title card. Built as the close. A real
your-turn handoff with a pasteable prompt was added at B08 per HANDOFF LAW, and
the sign-off moved to B09 where this series always puts it. Logged as one of the
two places the source narration was edited.

**3. B04 stops at the diagnosis, deliberately.** The source narration ends on
"the information was likely already priced in" and never says what the system
*does* with a high-drift signal — whether it discounts the score, flags it, or
just records it. **Confirmed with the author: keep it as the source has it.** No
closing behaviour was invented; the visual's "correct but already priced in"
verdict badge closes the beat instead. This is the honest stop: the episode
claims the measurement exists, not a policy built on top of it.

## Narration budget deviations

**B03 (Market Impact) runs 84 words.** It is three separate measurements —
magnitude, timing, volume — each of which needs its own sentence plus the
comparison that makes it mean something (12% versus half a percent). Splitting
it into two beats would break the "a correct signal is not always a useful
signal" frame that all three sit under. The visual is correspondingly a
three-part build, so the words are not racing a static frame.

**B05 (Infrastructure Upgrade) runs 81 words.** It is a list of five concrete
migrations and the list *is* the content — dropping any item to hit the budget
would be choosing which shipped work to omit rather than tightening prose. It is
also the only beat in eight episodes about the system's own plumbing, and the
narration is already doing it at maximum density.

## Evidence discipline (DOUBLE-CHECK LAW)

Every figure comes from the pre-authored briefs in this folder. Rows are split
into claims about the real system (confirmed by the author before audio spend)
and illustrative placeholders.

### Claims about the real system — **human-confirmed 2026-09-25**

| Claim (as scripted) | Where | Confirmed? |
|---|---|---|
| Readability scorer tracking whether complexity spikes before guidance changes | B02 | ☑ |
| Hedging index — ratio of phrases to definitive statements | B02 | ☑ |
| Tone shift detector comparing sentiment distributions across consecutive quarters | B02 | ☑ |
| All three feed the prediction model as features | B02 | ☑ |
| Reaction magnitude — excess return measured after the call | B03 | ☑ |
| Reaction timing — when the excess return accumulated | B03 | ☑ |
| Abnormal volume spikes flagged against a trailing average | B03 | ☑ |
| Pre-signal drift measured over the 5 and 10 trading days before the call | B04 | ☑ |
| Migrated SQLite → PostgreSQL, with connection pooling and composite indexes | B05 | ☑ |
| TimescaleDB hypertable with automatic partitioning for market time-series | B05 | ☑ |
| Outcome resolver reads a local database instead of live API calls for resolved dates | B05 | ☑ |
| Materialized views pre-computing dashboard aggregations | B05 | ☑ |
| Alembic schema versioning | B05 (visual only) | ☑ |
| Four readers → triangulator → pre-registered signal → graded against market (the Ep1–7 recap) | B01 | ☑ carried over, already confirmed |

### Illustrative placeholders

| Figure | Where | Status |
|---|---|---|
| Signal badge "raised, 0.82" | B01 | ☑ illustrative, carried from earlier episodes |
| Needle positions on the readability and hedging gauges | B02 | ☑ illustrative — the briefs specify "≈70% toward complex" and "moderate" as *example* settings, not measured values |
| The Q3 vs Q4 sentiment distributions | B02 | ☑ illustrative |
| +12% and +0.5% excess returns | B03 | ☑ illustrative — the briefs' own example pair; the arithmetic is what carries the point |
| The "1–3 days" marker position | B03 | ☑ illustrative |
| 3× average volume on the call-day bar | B03 | ☑ illustrative |
| The price line, +5% pre-call and +3% post-call | B04 | ☑ illustrative — the briefs' worked example of a high-drift case |
| "query: 2.3s → 0.1s" | B05 | ☑ illustrative — the briefs' figures, shown as a before/after of the same query, not a benchmark |
| v1 / v2 / v3 on the schema version bar | B05 | ☑ illustrative |

**One softening carried forward:** B01's recap again says the system grades
itself "against actual stock movement thirty days later" where Episodes 1–6
established three horizons (30 / 90 / 180 days). Kept verbatim as the same recap
compression logged in Episode 7 — thirty days is the first and most concrete
horizon.

## Friction protected

- Kept: the magnifying-glass turn at the end of B01. It is the hinge of the
  episode — the same transcript the series has read seven times, looked at
  differently — and it earns the title.
- Kept: both bars in B03's magnitude comparison. "Twelve percent is a stronger
  confirmation" is an assertion until the half-percent bar is sitting next to it
  at visibly different weight.
- Kept: the pre-call shading in B04 with the line *already climbing inside it*.
  The whole beat depends on the viewer seeing the move start before the marker.
- Kept: B05 in full, despite being the one beat about plumbing rather than
  signal. A system that quietly outgrows its database is a real thing that
  happens to real projects, and the episode is more honest for showing it.

## Sign-off notes

1. Evidence table is per-figure and split into real-system claims vs
   illustrative placeholders. **Human confirmation obtained before audio spend
   (2026-09-25)** on all thirteen rows, in two groups: the six
   linguistic/impact detectors, and the full infrastructure migration including
   TimescaleDB.
2. Palette conflict resolved per the Episode 7 precedent, which is now series
   law; the inert `color_continuity` block is noted rather than applied.
3. The B06 relabel and the moved sign-off line are logged above; B04's stop at
   diagnosis was confirmed rather than filled in.
4. Two narration-budget deviations (B03, B05) are argued above rather than
   waived.
5. Animated-slate review after `remotion_scenes.py` renders — frame-grab QC per
   VISUAL QC LAW, both orientations.

VERDICT: PASS
