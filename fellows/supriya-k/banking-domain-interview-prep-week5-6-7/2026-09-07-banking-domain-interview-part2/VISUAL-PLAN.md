# VISUAL-PLAN — banking-sql-running-total-bug

## Sample data (illustrative, invented — see FACTCHECK.md)

**Account `ACCT-50231`** — one fictional account, opened before the reporting window, so the bug
has something real to truncate.

| transaction_id | posted_at | amount | note |
|---|---|---|---|
| T1 | 2025-11-03 | +12,400.00 | deposit — the pre-2026 history the bug drops |
| T2 | 2026-01-08 | −300.00 | withdrawal |
| T3 | 2026-02-14 | +150.00 | deposit |
| T4 | 2026-03-01 | −75.00 | withdrawal |

## Worked query results (hand-verified)

**FIXED query** (`running` has no `WHERE`; filter lives in `last_posting_per_month`) —
`SUM() OVER (PARTITION BY account_id ORDER BY posted_at, transaction_id ROWS UNBOUNDED PRECEDING)`
sees every row:

| after row | running_balance | arithmetic |
|---|---|---|
| T1 (2025-11-03) | 12,400.00 | 12,400.00 |
| T2 (2026-01-08) | 12,100.00 | 12,400.00 − 300.00 |
| T3 (2026-02-14) | 12,250.00 | 12,100.00 + 150.00 |
| T4 (2026-03-01) | 12,175.00 | 12,250.00 − 75.00 |

End-of-month balances reported (last row per month, Jan–Mar 2026 shown; Apr–Jun have no postings
in this sample, so no row is emitted for them — a real, if simplified, property of this exact
query shape): **Jan = 12,100.00 · Feb = 12,250.00 · Mar = 12,175.00.**

**BUGGY query** (`WHERE posted_at >= '2026-01-01' AND < '2026-07-01'` inside `running`) — T1 is
filtered out *before* `SUM() OVER` ever runs, so the window only ever sees T2–T4:

| after row | running_balance | arithmetic |
|---|---|---|
| T2 (2026-01-08) | −300.00 | −300.00 (T1 never entered the window) |
| T3 (2026-02-14) | −150.00 | −300.00 + 150.00 |
| T4 (2026-03-01) | −225.00 | −150.00 − 75.00 |

End-of-month balances reported: **Jan = −300.00 · Feb = −150.00 · Mar = −225.00.** Every one of
these is wrong — the query runs without error and returns plausible-looking negative numbers for
an account that in reality never dropped below $12,100.

## Per-beat visual plan

| Beat | Shot | Motion plan |
|---|---|---|
| B00 | Remotion `ClaudeComposerAsk` | cold open, ask already answered, output lines list the finding |
| B01 | Manim `B01_RunningBalanceStakes` | balance line draws left-to-right across a 2025→2026 timeline; at the Jan 1 2026 tick, a thin red boundary appears with no alarm/error glyph — the line keeps drawing through it uninterrupted; label fades in: "no error thrown" |
| B02 | Manim `B02_FilterOrderSplit` | split screen, ledger-row dots stream in from the left on both sides; LEFT: dots pass through a funnel (pre-2026 dots vanish) before reaching a running Σ that lands low/crimson, labeled WRONG; RIGHT: all dots reach the Σ first (lands high/teal), THEN a funnel narrows the *display* to Jan–Jun only, labeled RIGHT; brace + arrow annotate the order on each side |
| B03 | Remotion `ClaudeComposerAsk` | composer, greeting "The ask," |
| B04 | Remotion `ClaudeCodeBeat` | buggy SQL, WHERE line highlighted/annotated inline, sparkLine "Filtered before it summed." |
| B05 | Manim `B05_TruncatedBalance` | 3-row result table builds top-to-bottom (Jan/Feb/Mar), each value landing in crimson as −300.00 / −150.00 / −225.00; pulsing crimson badge: "MISSING $12,400 OF HISTORY" |
| B06 | Remotion `ClaudeComposerAsk` | composer, `runningText: "updating query…"`, no greeting (per SPARK-LINE LAW's stated exception for CHANGE beats carrying the revision prompt itself as the spark) |
| B07 | Remotion `ClaudeCodeBeat` | fixed SQL, filter-relocation highlighted, sparkLine "Summed first. Filtered after." |
| B08 | Manim `B08_CorrectedBalance` | mirrors B05's table geometry; the three crimson values ghost, strike through, and fade; teal values land in their place: 12,100.00 / 12,250.00 / 12,175.00 |
| B09 | Manim `B09_TheLesson` | 3-line checklist builds with checkmarks; italic side-note fades in beneath |
| B10 | Remotion `ClaudeComposerAsk` | composer, greeting "Your turn.", the handoff prompt as `command` |
| B11 | Remotion `ClaudeTitleOutro` | title restate, `channel_title` mark beneath (no `@handle`), subline "in for Supriya — built with Claude, taken apart" |

## Resolution checklist (4K, 3840×2160)

- [ ] Manim scenes render at `-r 3840,2160` (not the default 1920×1080) — confirm `run.sh`'s
      `-qk` flag is used, not `-qh`.
- [ ] SQL code in B04/B07 (`ClaudeCodeBeat`, PT Mono) stays legible at 4K without needing to shrink
      below the skill's stated ~24px legibility floor — check after first Remotion render.
- [ ] Result-table numbers in B05/B08 (Manim) fill the canvas per FILL-THE-CANVAS/TYPESIZE LAW —
      not a timid font over dead space.
- [ ] `compile.py --height 2160` used for both the review and clean final cuts (default is 720).
- [ ] WCAG contrast holds for crimson-on-cream and teal-on-cream at the actual rendered size (Gate
      W checks this pre-render; confirm post-render too since Gate W runs on the Manim source, not
      the Remotion output).
