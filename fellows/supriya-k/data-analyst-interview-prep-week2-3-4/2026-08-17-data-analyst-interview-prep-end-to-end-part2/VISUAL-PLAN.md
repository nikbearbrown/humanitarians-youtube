# Visual Plan — "The SQL Interview Bug Even a Correct-Looking Query Can Hide"

## Sample data (illustrative — Loopr is the book's own invented company)

The book's `plays(user_id, track_id, played_at)` table holds one row per
play event. For teaching purposes, the beats show the **aggregated view**
(the `counts` CTE result) directly — i.e., "assume enough play events exist
that grouping by user and track gives:"

| user_id | track_id | plays |
|---|---|---|
| 101 (Maya) | T-ECHO | 5 |
| 101 (Maya) | T-NOVA | 5 |
| 101 (Maya) | T-DRIFT | 2 |
| 102 (Jon)  | T-ECHO | 7 |
| 102 (Jon)  | T-NOVA | 3 |
| 103 (Priya) | T-DRIFT | 6 |
| 103 (Priya) | T-ECHO | 4 |
| 103 (Priya) | T-NOVA | 1 |

Only user 101 has a genuine tie (T-ECHO and T-NOVA both at 5 plays) — the
other two users have a clear single maximum, so the bug is isolated to
exactly the case it's supposed to demonstrate.

## Worked query results (hand-verified — this is what the OUTPUT beats show)

**Buggy query (B04, `RANK()`):**
`RANK() OVER (PARTITION BY user_id ORDER BY plays DESC)`, filtered to `rnk = 1`.

- User 101: sorted desc → T-ECHO(5), T-NOVA(5) tied, T-DRIFT(2). RANK gives
  T-ECHO **rnk=1**, T-NOVA **rnk=1** (RANK repeats the value on a tie),
  T-DRIFT rnk=3. `WHERE rnk=1` keeps **both** tied rows.
- User 102: T-ECHO(7) rnk=1, T-NOVA(3) rnk=2 → keeps **1 row**: (102, T-ECHO, 7).
- User 103: T-DRIFT(6) rnk=1, T-ECHO(4) rnk=2, T-NOVA(1) rnk=3 → keeps
  **1 row**: (103, T-DRIFT, 6).

**Buggy output, in order shown (B05): 4 rows for 3 users**
```
(102, T-ECHO, 7)
(103, T-DRIFT, 6)
(101, T-ECHO, 5)   <- tie
(101, T-NOVA, 5)   <- tie, duplicate winner
```

**Fixed query (B07, `ROW_NUMBER()` + tiebreaker):**
`ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY plays DESC, track_id ASC)`,
filtered to `rn = 1`. `ROW_NUMBER()` never repeats a value, so ties are
broken deterministically by the added `track_id ASC` clause.

- User 101: T-ECHO(5) vs T-NOVA(5) tied on plays; tiebreaker `track_id ASC`
  → 'T-ECHO' sorts before 'T-NOVA' → T-ECHO gets **rn=1**, T-NOVA gets rn=2,
  T-DRIFT rn=3. `WHERE rn=1` keeps exactly **1 row**: (101, T-ECHO, 5).
- User 102 / 103: unchanged (no tie) → same single row each as before.

**Fixed output, in order shown (B08): 3 rows for 3 users**
```
(102, T-ECHO, 7)
(103, T-DRIFT, 6)
(101, T-ECHO, 5)   <- tie now resolved to exactly one row
```

This confirms the "moving output" in B05 and B08 is correct SQL semantics,
not an assumed or guessed result — a human reviewer can re-run both queries
against the sample rows above and get the same two outcomes.

## Per-beat visual plan

| Beat | Shot | Motion plan |
|---|---|---|
| B00 | `ClaudeComposerAsk` (Remotion) | Composer types the ask, answers with the 4-line output preview; terracotta send-button spark. |
| B01 | Manim `B01_ProblemStakes` | `plays` schema draws on; three rows for user 101 animate in, T-ECHO/T-NOVA counts climb in parallel and land on the same value (5/5); crimson tie-mark pulses between them. |
| B02 | Manim `B02_WindowVsGroupBy` | Split screen: left side collapses 3 rows into 1 (GROUP BY); right side keeps all 3 rows with a PARTITION BY bracket and an ORDER BY sort arrow. |
| B03 | `ClaudeComposerAsk` (Remotion) | Ask micro-beat, spark line "The ask,"; command text types in. |
| B04 | `ClaudeCodeBeat` (Remotion/Onda code-block) | Full buggy SQL (CTE `counts` → CTE `ranked` w/ `RANK()` → final `SELECT ... WHERE rnk = 1`), syntax-highlighted, `RANK()` line gets a brief highlight pulse. |
| B05 | Manim `B05_TopTrackBuggyOutput` | Result rows fly in one at a time in the exact order above; 102 and 103 rows land with a teal checkmark; both 101 rows land together flagged crimson with a "2 ROWS FOR ONE USER" badge; a row-count ticker reads "4 rows returned / 3 users asked for." |
| B06 | `ClaudeComposerAsk` (Remotion) | Revision ask, spark line "The change,"; command references the actual bug found in B05. |
| B07 | `ClaudeCodeBeat` (Remotion/Onda code-block) | Full fixed SQL; diff emphasis on `RANK()` → `ROW_NUMBER()` and the added `, track_id ASC`. |
| B08 | Manim `B08_TopTrackFixedOutput` | Same three rows fly in; (101, T-ECHO, 5) lands alone with a teal checkmark; the now-excluded (101, T-NOVA, 5) row appears briefly ghosted/crossed-out beside it, then fades — showing what got filtered. Ticker updates to "3 rows returned / 3 users asked for." |
| B09 | Manim `B09_Lesson` | Three checklist lines draw on in sequence ("Read the output." / "Count the rows." / "Check the case the happy path skips."); small side note citing Ch.7's AI-code-judgment line. |
| B10 | `ClaudeComposerAsk` (Remotion) | Handoff — greeting "Your turn.", full suggested prompt types in, read aloud per HANDOFF LAW. |
| B11 | `ClaudeTitleOutro` (Remotion) | Title restate, `@HumanitariansAI` handle, subline "Supriya, for Humanitarians AI." |

All output/illustration beats use **Manim or Remotion only** — no stock
photography, no paid gen-AI clips, no archive sourcing needed anywhere in
this video (consistent with the toolkit's no-paid-services rule).

## Resolution checklist (for the later render pass — not done now)

- [ ] Every beat renders natively at **3840×2160** (4K), not upscaled from 1080p.
- [ ] `compile.py [reel] --height 2160` (default is 720 — must be overridden).
- [ ] Manim scenes (`scenes.py`) render at `-qh` or higher and are confirmed
      at 3840×2160 output, not the Manim default.
- [ ] Remotion compositions (`ClaudeComposerAsk`, `ClaudeCodeBeat`,
      `ClaudeTitleOutro`) confirmed at 3840×2160 frame size before compositing.
- [ ] Spot-check each beat's rendered frame resolution (`ffprobe`) individually
      before compiling the final master — per CLAUDE.md's "check the
      resolution of every beat before compilation" rule.
- [ ] Final master mp4 confirmed 3840×2160 via `ffprobe`.
