# VISUAL-PLAN — banking-domain-interview-end-to-end-v2

## Sample data 1 (B05 output) — reused verbatim from `banking-domain-sql-running-total-bug`

**Account `ACCT-50231`** — same fictional account, same four transactions, same hand-verified
arithmetic as the sibling reel (not re-invented here — see that reel's `VISUAL-PLAN.md` for the
original derivation):

| transaction_id | posted_at | amount | running_balance |
|---|---|---|---|
| T1 | 2025-11-03 | +12,400.00 | 12,400.00 |
| T2 | 2026-01-08 | −300.00 | 12,100.00 |
| T3 | 2026-02-14 | +150.00 | 12,250.00 |
| T4 | 2026-03-01 | −75.00 | 12,175.00 |

End-of-month balances shown in B05: **Jan = 12,100.00 · Feb = 12,250.00 · Mar = 12,175.00** — the
query's correct, shipped form (`running` has no `WHERE`), so there is no "wrong" value to contrast
here (unlike the sibling reel, which is the bug-teardown piece).

## Sample data 2 (B08 output) — new, invented for illustration, disclosed here

**Harborline Card Co., January 2025 origination cohort, 500 accounts** (fictional issuer name is
the book's own chapter-9 running example; the account count and bucket splits below are invented
for this video, since the chapter's worked example is schema + query + prose with no sample bucket
counts):

| months_on_book | current | 30 dpd | 60 dpd | 90+ dpd | charge_off | total | pct current |
|---|---|---|---|---|---|---|---|
| 3 | 460 | 30 | 8 | 2 | 0 | 500 | 92.0% |
| 6 | 420 | 40 | 25 | 10 | 5 | 500 | 84.0% |
| 9 | 390 | 45 | 30 | 20 | 15 | 500 | 78.0% |

Each row sums to 500 (the fixed cohort size — the point the query makes: the denominator never
changes, because it's anchored to the January 2025 cohort, not to whatever population exists in a
given calendar month). Percentages are `100 * bucket_count / 500`, rounded to 1 decimal per the
chapter's actual query (`ROUND(100 * accounts_in_bucket / cohort_total, 1)`).

## Per-beat visual plan

| Beat | Shot | Motion plan |
|---|---|---|
| B00 | Remotion `ClaudeComposerAsk` | cold open, ask already answered, output line states the hook |
| B01 | Manim `B01_TheSecondLanguage` | "SQL" and "Python" tiles slide in and lock together (a skillset that's already solid); a second, translucent layer of terms (CET1 · LCR · OCC · CFPB · charge-off) slides in ON TOP and snaps opaque, labeled "the layer banking adds" |
| B02 | Manim `B02_SixPartMap` | six labeled blocks build left-to-right into a single pipeline (Landscape → Regulation/Risk → Data Stack → Technical Prep → Behavioral/Case/Systems → Day-Of), each locking in with a soft snap as its name is spoken |
| B03 | Remotion `ClaudeComposerAsk` | composer, greeting "The ask," |
| B04 | Remotion `ClaudeCodeBeat` | Ch. 8's `running` + `last_posting_per_month` CTEs, `WHERE` line in the second CTE highlighted, sparkLine "Sum first. Filter after." |
| B05 | Manim `B05_CorrectBalance` | 3-row EOM table builds top-to-bottom (Jan/Feb/Mar), each value landing in teal: 12,100.00 / 12,250.00 / 12,175.00; small annotation ties Jan's value back to the Nov 2025 deposit crossing the year boundary |
| B06 | Remotion `ClaudeComposerAsk` | composer, `runningText: "checking against a cohort…"`, spark line carries the ask itself (CHANGE-beat exception, no separate greeting) |
| B07 | Remotion `ClaudeCodeBeat` | Ch. 9's `cohort` + `snap` + `scoped` CTEs, the `months_on_book` computation highlighted, sparkLine "Cohort survives every join." |
| B08 | Manim `B08_VintageCurve` | a 3-column (3/6/9 months) stacked-bar build, each column's segments landing bucket by bucket (current→30→60→90+→charge_off), a running "of 500" cohort-total label pinned above every column so it visibly never changes |
| B09 | Manim `B09_TwoMoves` | 2-line checklist builds with checkmarks ("get the SQL order right" / "never lose the cohort"), then the six-part map from B02 re-appears compressed beneath it as a "the rest of the book" tag |
| B10 | Remotion `ClaudeComposerAsk` | composer, greeting "Your turn.", the handoff prompt as `command` |
| B11 | Remotion `ClaudeTitleOutro` | title restate, `handle: "Supriya"` at full size (visible, not spoken-only), subline "Built with Claude — the full book: Banking Domain Data Analyst Interview Prep" |

## Resolution checklist — 16:9 master (4K, 3840×2160)

- [ ] Manim scenes render at `-qk` (3840×2160), not the default `-qh`.
- [ ] SQL in B04/B07 (`ClaudeCodeBeat`, PT Mono) stays legible at 4K, no shrink below the skill's
      ~24px legibility floor.
- [ ] Result visuals in B05/B08 (Manim) fill the canvas per FILL-THE-CANVAS/TYPESIZE LAW.
- [ ] `compile.py --height 2160` used for both review and clean master.
- [ ] WCAG contrast holds for teal/crimson-on-cream at actual rendered size.

## Resolution checklist — 9:16 Short (4K, 2160×3840) — PM's specific complaints

- [ ] Derived via `./art shorts` (cap check → likely drops B06–B08, the revision cycle) —
      **flagged to the user/PM as a length tradeoff, see PLAN.md.**
- [ ] New `ClaudeCodeBeat916.tsx` (relative font sizing off `height`) built and registered in
      `Root.tsx` BEFORE the ONDA CHECK rewires B04 — the stock `ClaudeCodeBeat` has hardcoded
      pixel code-line fonts (13/11/22px) that will underfill a 3840-tall canvas otherwise.
- [ ] Portrait Manim scene classes for whichever of B01/B02/B05 survive the cap-plan, written to
      the `ClaudeVerdictArtifact916` fill standard (font sizes as a fraction of frame height).
- [ ] Compiled at `compile.py short --review --height 3840` (true 2160×3840), not the `1920`
      shorts.py prints as its example.
- [ ] Post-render: measure actual video bitrate (`ffprobe`) and eyeball frame-fill percentage —
      target is a bitrate genuinely in the hundreds-of-kbps range at minimum, not v1's 139 kbps,
      and no beat under ~55% vertical content fill (the threshold the sibling reel's own Gate V
      run used).
