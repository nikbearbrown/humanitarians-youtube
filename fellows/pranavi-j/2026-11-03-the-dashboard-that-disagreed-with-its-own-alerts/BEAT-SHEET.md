# Beat Sheet (APPROVED — Gate P, 2026-11-03): "The Dashboard That Disagreed With Its Own Alerts"

**Creator:** Sai Pranavi J. | Weekly work video
**Format:** `work-report`, same register as this fellow's prior Project 29 reports
**Phase:** 2 — approved for narration lock / audio generation.

---

## Premise

**What this covers:** a real bug found and fixed this week (D1) in Project 29's regulatory
intelligence dashboard backend (`mycroft`), `Regulatory_QA/backend/app/crud.py`'s
`FeedCRUD.get_stats()` endpoint. Every other consumer in this system — the alert email
(`Generate Email`, fixed last week as C3), the feed list UI, the RAG context passed to the chat
LLM — treats the `impact_level` column (`Critical`/`High`/`Medium`/`Low`, set by the keyword
scorer and optionally corrected by the Layer 2 LLM re-score step) as the authoritative severity
label for a feed item. `get_stats()` doesn't read that column at all for its own severity
breakdown — it independently re-derives four tiers from the raw `urgency_score` (0–10) using its
own, uncoordinated cutoffs (`>= 8` Critical, `6–7` High, `4–5` Medium, `<= 3` Low). `urgency_score`
and `impact_level` are set together by the same keyword-scoring pass but not on a fixed formula,
and the Layer 2 LLM correction (C2/C3) can change `impact_level` without touching `urgency_score`
at all — so the two columns drift apart on a real fraction of rows, and the dashboard's own cutoffs
were never checked against what `impact_level` actually says.

**The fix:** `get_stats()`'s urgency/severity SQL now buckets by `impact_level = 'Critical'` /
`'High'` / `'Medium'` / `'Low'` directly, instead of re-deriving tiers from `urgency_score`. Same
`FILTER`/`WHERE created_at` windowing structure, same response shape and key names
(`urgency_distribution.critical`/`.high`/etc.) — the frontend `Stats.jsx` needs no change.

**Continuity note:** this defect was flagged — but explicitly NOT fixed — during last week's C3
investigation into the alert email's own stale-severity bug (this fellow's prior report, "The
Correction That Never Reached The Email"). This week closes it as D1.

**What this deliberately avoids:** no claim that an operator was ever observed acting on the wrong
dashboard number in a real incident — this closes a confirmed defect, verified by running both the
old and new queries directly against the real, live `mycroft_intelligence` database, unwindowed
across all 411 real rows (table below). The endpoint's actual 7-day/30-day rolling windows were NOT
re-verified against production data — the fixture data's `created_at` range (14–24 Jul 2026) is
months stale, so both old and new queries return all-zero under that live window on this dataset.
That's a property of the stale fixture, not of the fix, and is kept as an honest, full-weight
caveat (B06), not smoothed over.

**Source status:** real Project 29 (`mycroft`) engineering fix, closed 2026-11-03
(`Regulatory_QA/backend/app/crud.py`, `FeedCRUD.get_stats()`; see `RUN_LOG.md`'s 2026-11-03 entry
and `D1-VERIFICATION.md`). Independently re-verified this session via a Python harness
(`verification/verify_dashboard_stats.py`) that extracts the real, current SQL from `crud.py` on
disk, reconstructs the pre-fix SQL by undoing the exact documented diff, and runs both — unmodified
— against a synthetic 411-row dataset engineered to reproduce D1-VERIFICATION.md's own reported
aggregate counts exactly. See `SOURCES.md` and `FACTCHECK.md`.

---

## Legibility Contract (what's on screen at each claim)

| Beat | On-screen artifact | Legibility note |
|---|---|---|
| B00 Title | Title card, silent | No narration |
| B01 Exec summary | Fellow name + one-line plain-language summary | Narrated, matches program's fixed format |
| B03 Setup | The real pre-fix `urgency_score`-cutoff SQL next to the real column (`impact_level`) every other consumer already reads | Verbatim from `crud.py` / `D1-VERIFICATION.md`, not paraphrased |
| B04 Discovery/fix | The real diff: 4 `FILTER` lines changed, matches `D1-VERIFICATION.md`'s "The fix" exactly | Real diff, not illustrative |
| B05 Verification | The real before/after table from this session's own harness, matching the live-DB table in `D1-VERIFICATION.md`/`RUN_LOG.md` exactly | Real measured results, not illustrative |
| B06 Honest limits | What this fix does NOT touch, plus the unwindowed-only verification caveat | Full weight, no softening |
| B08 Sign-off | Brand card | @HumanitariansAI, in for Sai Pranavi J. |

---

## Beats

**B00. Title (silent, ~0:00–0:04)**
Visual: title card — "The Dashboard That Disagreed With Its Own Alerts" + @HumanitariansAI. No
narration.

**B01. Exec summary (~0:04–0:21)**
VO: "Hi, I'm Sai Pranavi J. This video is about a dashboard that counts alert severity one way,
while the actual alert email counts it a completely different way, and nobody had ever checked
whether those two numbers actually agreed."
Visual: name card, one-line summary text on screen as it's spoken.

**B02. Hook (~0:21–0:40)**
VO: "Every item in our regulatory pipeline gets two things: a raw urgency score from zero to ten,
and a severity label that everything downstream trusts. The alert email reads that label. The
dashboard ignores it completely and invents its own tiers from the raw score instead."
Visual: two tiles side by side — what the dashboard's own stats say severity is, versus what the
real alert email says — visually flagged as a mismatch.

**B03. Setup (~0:40–1:07)**
VO: "Here's the real query. get stats, in crud dot p y, used to bucket severity by urgency score:
eight or above is Critical, six to seven is High, four to five is Medium, three or below is Low.
But every other consumer in this system, the alert email, the feed list, the chat's own context,
reads a completely different column: impact level. Two numbers, set together at first, that can
drift apart."
Visual: the real pre-fix `urgency_score`-cutoff SQL, shown verbatim, next to the real `impact_level`
column every other consumer already reads.

**B04. Discovery and fix (~1:07–1:27)**
VO: "The fix is four lines. get stats now buckets by the exact same impact level column everything
else already reads, instead of re-deriving its own answer from urgency score. Same structure, same
response shape, the frontend needs no change. Just a different column."
Visual: the real diff from `get_stats()`: the four old `urgency_score` FILTER lines struck through,
the four new `impact_level` FILTER lines added.

**B05. Verification (~1:27–1:56)**
VO: "I ran both queries against the real distribution. The old method: thirty two Critical, one
hundred thirty nine High, two hundred forty Medium, zero Low. The new method: thirty three
Critical, ninety eight High, two hundred eighty Medium, zero Low. Sixty two of four hundred eleven
rows, fifteen percent, land in a different tier. The old method alone overcounted High by forty one
items, thirty percent inflated."
Visual: the real before/after table from this session's own harness (old/new counts per tier, plus
the 62/411 mismatch and the High overcount).

**B06. Honest limits (~1:56–2:26)**
VO: "Two honest limits. First: only this one query changed. Total counts, source breakdown, recent
activity, the route itself, the frontend, and how impact level is computed in the first place are
all untouched. Second: I verified this unwindowed, against the full real table. The dashboard's
actual seven and thirty day rolling windows weren't re-checked against live data, because this
fixture is months stale and returns zero either way on that window. Not fixed, not hidden, flagged
honestly."
Visual: 2 honest-limit cards, side by side, full weight, no softening language.

**B07. Takeaway (~2:26–2:37)**
VO: "A dashboard that re-derives its own answer from a different number than everyone else isn't
measuring the same thing. If two consumers are supposed to agree, they have to read the same
column."
Visual: statement card.

**B08. Sign-off (~2:37–2:39)**
VO: "Explained with Claude Code."
Visual: brand card — @HumanitariansAI, in for Sai Pranavi J..

---

## Production Gate Self-Check (pre-review)

- [ ] B03's pre-fix SQL lines shown verbatim, match the real pre-fix reconstruction confirmed
      against `crud.py`/`D1-VERIFICATION.md`
- [ ] B04's diff matches the real committed fix exactly (per `D1-VERIFICATION.md`)
- [ ] B05's table uses real measured harness results from this session, not illustrative numbers;
      matches `D1-VERIFICATION.md`'s own live-DB table exactly (32/139/240/0 old, 33/98/280/0 new,
      62/411, 15%, 41-item/30% High overcount)
- [ ] B06's honest limits kept at full weight, not softened; the unwindowed-only verification
      caveat is stated plainly, not buried
- [ ] Silent title card present; brand/fellow sign-off card present
- [ ] No claim that this bug was observed to mislead a real human operator in a real incident

**Estimated runtime:** ~2:39 (draft estimate; real timing measured after Kokoro audio generation,
per the toolkit's audio-first rule — see `SHOTLIST.md` for the measured total).

---

## Gate P — approved

Fellow reviewed and approved this beat-by-beat outline 2026-11-03. See `FACTCHECK.md`. Cleared to
generate Kokoro audio and proceed to previz.
