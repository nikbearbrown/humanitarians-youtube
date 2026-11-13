# NARRATION — GATE P — "SQL, Read Fewer Rows."

Reel: `projects/2026-09-21-sql-query-optimization-for-analytics`
Voice: **Bella — Kokoro `af_bella`** (free). Register: Pragmatist (HAI plain).

**Rev 3 — 2026-10-17 (v2 rebuild). SIGNED 2026-10-17 by Supriya Kushwaha.** Rev 2's signature
(2026-09-16) is void: narration changed in nine of ten beats.

Why rev 3 exists (audit 2026-10-17, decisions approved by Supriya 2026-10-17):
- **Length.** Rev 2 measured 180.57s, so the full-length 9:16 (narration + 4.5s endcard)
  could not fit under 180s. Rev 3 estimates **156.9s** at each beat's own measured
  rev-2 rate, **169.4s** with the +8% Kokoro overrun the banking rebuilds showed —
  inside the 173.5s shorts budget. No beat is cut.
- **Exact intro.** "Hi, I am Supriya**,** and this video is about…" → no comma.
- **Accuracy** (see `FACTCHECK.md`, "Rev 3 corrections"):
  1. B07 "rewrite it as a bare range" → "compare the bare column instead" (the CAST and
     UPPER rewrites are equalities, not ranges).
  2. B06 "an index works on the column…" → "a **plain** index…" (expression indexes, L3).
  3. B02 "costs nothing to run" → "costs almost nothing" (EXPLAIN still parses and plans).
  4. B00 "byte for byte" dropped (the demo compares sorted rows, not bytes).
  5. B01 "every analytics query" → "a typical analytics query".
- **Pronunciation.** `posted_at` is spoken as "the posted-at column" (screen keeps `posted_at`).
- **Trims, no content lost.** B03 drops "from a real terminal" (the capture source is on
  screen); B04 drops "the gap stops being an opinion"; B08 drops the two-sentence coaching
  aside after the prompt — **the prompt itself is still read verbatim** and matches the
  on-screen command word for word.

| Beat | Act | Words | Est. | Narration (rev 3) |
|---|---|---|---|---|
| B00 | ASK | 50 | ~19.0s | Hi, I am Supriya and this video is about SQL query optimization for analytics. Two queries, identical output: the same four thousand four hundred fifty-nine rows. One reads eleven thousand rows to get there. The other reads four hundred thousand. The SQL won't tell you which. The query plan will. |
| B01 | SETUP | 48 | ~18.3s | Here is the shape of a typical analytics query. Four hundred thousand postings. You want one month: eleven thousand rows survive the filter, and grouping by account leaves four thousand four hundred fifty-nine. Optimization is about how many of the four hundred thousand the database has to touch. |
| B02 | ASK | 26 | ~8.7s | So ask the database. EXPLAIN QUERY PLAN costs almost nothing, and it doesn't run your query. It just tells you what the engine intends to do. |
| B03 | EVIDENCE | 48 | ~18.6s | There it is. Query A: SCAN postings. Scan means every row, all four hundred thousand. Query B: SEARCH postings USING INDEX, with the date range in the parentheses. Search means the index walked to January and stopped. Same answer, and the plan said so before either query ran. |
| B04 | MAGNITUDE | 42 | ~15.8s | On a log scale, four hundred thousand rows read against eleven thousand three hundred sixty-nine is thirty-five times fewer. The answer itself is four thousand four hundred fifty-nine rows, so Plan B is near the floor. Plan A is two decades away. |
| B05 | PREDICT | 31 | ~10.1s | Before I show you why, commit to an answer. Both queries filter on the same indexed column. So what is it about Query A's WHERE clause that takes the index away? |
| B06 | INSIGHT | 51 | ~17.3s | The function. Query A wraps the posted-at column in strftime, so the database has an expression instead of a column, and evaluating it means visiting every row. Query B leaves the column bare. That is the insight: a plain index works on the column, not on a function of the column. |
| B07 | VERDICT | 61 | ~20.9s | Let's recap. Before you tune a query, run EXPLAIN and look for the word SCAN. If it shows up on a table you thought was indexed, check your WHERE clause for a function wrapped around the indexed column, like strftime, CAST or UPPER, and compare the bare column instead. That one move took four hundred thousand rows down to eleven thousand. |
| B08 | HANDOFF | 75 | ~22.5s | I'm learning to optimize analytics SQL. Here is the schema for one of my tables and the slowest query I run against it. Walk me through its EXPLAIN plan step by step, tell me which steps read every row, find any predicate that a function or a cast has made unusable by the index, and give me the smallest rewrite that turns a SCAN into a SEARCH. Run it on your slowest dashboard query tonight. |
| B09 | OUTRO | 11 | ~5.8s | SQL — read fewer rows. Thanks for watching. Supriya, for Humanitarians AI. |

Total: rev 2 **180.57s** → rev 3 est. **156.9s** (+8% allowance **169.4s**; budget 173.5s).

## Law checks on rev 3

- **Intro line, verbatim** — B00 opens "Hi, I am Supriya and this video is about SQL query
  optimization for analytics." ✓
- **HANDOFF LAW** — B08 reads the prompt aloud verbatim in full (the first 67 words equal
  `props.command` exactly), then one closing line. ✓
- **One concrete takeaway** — B07: run EXPLAIN, look for SCAN, compare the bare column. ✓
- **Every function the voice names is EXECUTED evidence** — strftime, CAST, UPPER: demo
  pairs 1–3, re-run 2026-10-17, all three `same result set: True`. ✓
- **Every figure spoken is on screen** — 400,000 · 11,369 · 4,459 · 35× · two decades. ✓
- **No timing figure spoken or shown** — the B06 "~15 ms / ~60 ms" screen labels are removed
  in v2 (FACTCHECK row 13b). ✓

---

Human sign-off required before `generate_audio_kokoro.py` runs. GATE P.

Sign **rev 3** (the table above). Any later change to any `narration_text` reopens the gate.

**VERDICT: PASS**

Signed by: **Supriya Kushwaha** (human, author) · Date: **2026-10-17**
Revision signed: **rev 3** (2026-10-17) — the narration table above.

---

## History — rev 2 (signed 2026-09-16, void as of rev 3)

### Rev 2 record — NARRATION — GATE P — "SQL, Read Fewer Rows."

Reel: `fellows/supriya-k/2026-09-16-sql-query-optimization-for-analytics`
Voice: **Bella — Kokoro `af_bella`** (free). Register: Pragmatist (HAI plain).
Channel: `claude-hai` · chip `@HumanitariansAI` · playlist `Fellows Research`.

**Rev 2 — 2026-09-16.** One narration edit since rev 1, in **B07**: the spoken
function list dropped `date_trunc`, going from *"strftime, date_trunc, CAST,
UPPER"* to **"strftime, CAST, UPPER"**. Reason (`FACTCHECK.md` L2 option 2): the
demo fixture now *executes* `strftime`, `CAST` and `UPPER` as three verified
query pairs, but `date_trunc` is a PostgreSQL function that does not exist in
SQLite and can never be executed against this fixture. Every function the voice
now names is measured evidence; `date_trunc` moved to the video description,
where a correction costs no re-render. B07's matching on-screen `artifactLines`
entry was changed the same way. **This edit was free** — it landed before GATE P
was signed. No other beat changed, and no figure in any beat changed.

**GATE P is a QUALITY gate, not a cost gate** (brutalist CLAUDE.md rule 3) — audio
here is free. Nothing is generated until a human writes `VERDICT: PASS` below.

> Review this on an ANIMATED slate that plays each beat's `show` events, not on this
> page. A slate that presents beats as static text misrepresents the reel
> (SHOW-DON'T-TELL LAW). Build the slate with
> `python3 runtime/scripts/remotion_scenes.py <REEL>` + `./art run <REEL>` — **after**
> this gate is signed, not before.

| Beat | Act | Words | Narration |
|---|---|---|---|
| B00 | ASK | 58 | Hi, I am Supriya, and this video is about SQL query optimization for analytics. Two queries. Identical output — the same four thousand four hundred fifty-nine rows, byte for byte. One of them reads eleven thousand rows to get there. The other reads four hundred thousand. Nothing in the SQL tells you which is which. The query plan does. |
| B01 | SETUP | 54 | Here is the shape of every analytics query. Four hundred thousand postings. You want one month — eleven thousand rows survive the filter, and grouping by account leaves four thousand four hundred fifty-nine. The answer is tiny. Optimization is the argument about how many of those four hundred thousand the database touches to find it. |
| B02 | ASK | 31 | So stop guessing and ask the database. EXPLAIN QUERY PLAN costs nothing to run, and it does not run your query — it just tells you what the engine intends to do. |
| B03 | EVIDENCE | 52 | There it is, from a real terminal. Query A: SCAN postings — scan means every row, all four hundred thousand. Query B: SEARCH postings USING INDEX, with the date range in the parentheses. Search means the index walked to January and stopped. Same answer, and the plan said so before either query ran. |
| B04 | MAGNITUDE | 49 | On a log scale the gap stops being an opinion. Four hundred thousand rows read, against eleven thousand three hundred sixty-nine — thirty-five times fewer. And the answer itself is only four thousand four hundred fifty-nine rows, so Plan B is near the floor. Plan A is two decades away. |
| B05 | PREDICT | 31 | Before I show you why, commit to an answer. Both queries filter on the same indexed column. So what is it about Query A's WHERE clause that takes the index away? |
| B06 | INSIGHT | 63 | The function. Query A wraps posted_at in strftime, so the database no longer has a column to look up — it has an expression, and the only way to evaluate it is to visit every row. Query B leaves the column bare and compares it to constants. That is the insight: an index works on the column, not on a function of the column. |
| B07 | VERDICT | 69 | Let's recap with Claude. One takeaway you can use today: before you optimize an analytics query, run EXPLAIN and look for the word SCAN. If it shows up on a table you thought was indexed, check your WHERE clause for a function wrapped around the indexed column — **strftime, CAST, UPPER** — and rewrite it as a bare range. That one move took four hundred thousand rows down to eleven thousand. |
| B08 | HANDOFF | 94 | I'm learning to optimize analytics SQL. Here is the schema for one of my tables and the slowest query I run against it. Walk me through its EXPLAIN plan step by step, tell me which steps read every row, find any predicate that a function or a cast has made unusable by the index, and give me the smallest rewrite that turns a SCAN into a SEARCH. Ask for the smallest rewrite, not a rewritten query — you want to see which single change moved the plan. Run it on your slowest dashboard query tonight. |
| B09 | OUTRO | 11 | SQL — read fewer rows. Thanks for watching. Supriya, for Humanitarians AI. |

## Pronunciation notes for Kokoro

Numbers and identifiers are already spelled out longhand in the narration so the
TTS reads them correctly. Two to listen for on the first pass:

- `posted_at` — should read "posted underscore at" or "posted at". If Bella says
  "posted underscore at" and it grates, change the narration to "the posted-at
  column" and regenerate that beat only.
- `strftime` — intended as "stir-eff-time". If it mangles, spell it "S-T-R-F-time"
  in `narration_text` (screen text stays `strftime`).

## Law checks on this narration

- **Intro line, verbatim** — B00 opens with "Hi, I am Supriya, and this video is
  about SQL query optimization for analytics." ✓
- **IN-FOR-BEAR LAW does not apply** — voice is Bella, not Onyx. No "Liam, in for
  Bear" anywhere; B09 signs off "Supriya, for Humanitarians AI." ✓
- **NARRATION BUDGET (45–70 words per body beat)** — B01 54 · B03 52 · B04 49 ·
  B06 63. B02 (32) is an ask micro-beat, and B00/B07/B08/B09 are bookends; both
  classes are exempt. ✓
- **HANDOFF LAW** — B08 reads the suggested prompt aloud VERBATIM in full (the
  first 67 words are the prompt, word for word identical to
  `props.command`) and then discusses it for two sentences. ✓
- **Evidence on screen, judgment in the voice** — every figure spoken by Bella is
  also on screen as a counter, marker, or verdict strip. ✓
- **One concrete takeaway** — B07: run EXPLAIN, look for SCAN, unwrap the function.
  One action, not a summary of the video. ✓
- **Every function the voice names is EXECUTED evidence** (DOUBLE-CHECK LAW) —
  B07 speaks exactly three: `strftime` (demo pair 1), `CAST` (pair 2), `UPPER`
  (pair 3). All three are real `EXPLAIN QUERY PLAN` captures on the same
  400,000-row fixture, and `demo/build_demo.py` exits non-zero if any of the
  three rewrites stops returning an identical result set. Nothing in the spoken
  list rests on analogy. ✓
- **Word counts recomputed** for this revision, excluding standalone em-dash
  tokens. Two rev-1 figures were off by a word or two (B02, B09) and are
  corrected above; no narration text changed on those beats. ✓

---

Human sign-off required before `generate_audio_kokoro.py` runs. GATE P.

Sign **rev 2** (the text in the table above). If you sign rev 2 and later change
any `narration_text`, GATE P reopens — that is the whole point of the gate.

**VERDICT: PASS**

Signed by: **Supriya Kushwaha** (Fellow) · Date: **2026-09-16**
Revision signed: **rev 2** (2026-09-16) — the narration table above, with B07's
function list reading "strftime, CAST, UPPER".
Voice: **af_bella confirmed as my series voice (Bella, HAI plain register).**
Fellow approval for first audio generation per `fellows/README.md`: **given.**
Narration reviewed: all 10 beats.

Any later change to any beat's `narration_text` reopens GATE P and voids this
signature.
