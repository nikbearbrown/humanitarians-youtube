# SHOTLIST — It Tested Clean

Week ending 2026-11-20 · `ai-` track · 9 beats · master 16:9 3840×2160.

SHOW authored before narration. Durations are the measured Kokoro `am_onyx`
MP3s — the master clock.

| # | Act | Scene | Audio | What the viewer WATCHES |
|---|---|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` | 18.13s | Greeting (`Bula, Jainil`) · the question types in · two output lines answer it |
| B01 | BLUF | `BrutalistHesitantWriter` | 14.17s (+0.8 lead) | Types **model**, deletes it, types **feature** |
| B02 | SETUP | `StageRail` | 14.89s | Warehouse → feature store → model, with the terracotta note *nothing compares these two* |
| B03 | BODY | `PairedBars` | 20.65s | Four skew rows · every offline bar identical at 73.4 · served bars shrinking to 41.5 |
| B04 | BODY | `ClaudeBarChart` | 20.16s | Mean predicted probability, 0.25 → 0.42, then cents at 0.99 taking the accent |
| B05 | BODY | `CardSet` | 19.78s | Two cards: the same check at the serving log vs at the warehouse |
| B06 | LAND | `StageRail` | 18.92s | Model → serving log → compare to training; *the only place both numbers exist* |
| B07 | HANDOFF | `ClaudeComposerAsk` | 20.31s | "Your turn." · the prompt types in and is read aloud |
| B08 | OUTRO | `HaiTitleOutro` | 3.33s | Title restate · `@HumanitariansAI` |

**Total 150.3s + 0.8s lead = 151.1s — 2:31.1.** Master window 2:00–5:00 ✓ ·
Short cap 3:00 ✓. Landed inside the window on the first pass.

---

## The spine

Cold open → BLUF → the two paths → the damage → the calibration collapse →
the monitoring blind spot → the fix → handoff → outro.

Typing appears in exactly three beats — the ask, the overview, the viewer's
prompt.

## B03 carries the argument

The offline bar is **the same length on every row** — 73.4, four times — while
the served bar shrinks down the stack. That repetition is the point: a viewer
sees that the number the team watches never moves, regardless of how badly the
serving path is broken. `total: null` here, because these are four independent
comparisons rather than parts of an aggregate.

## B02 and B06 are the same diagram twice

Both `StageRail`, three beats apart. B02 is the broken wiring — warehouse,
feature store, model, and nothing comparing them. B06 is the fix — model,
serving log, comparison. Same shape, opposite conclusion, and the rhyme is
what makes the fix legible as a *change to the diagram* rather than a new idea.

## What this reel does not argue

It does not say drift detection is useless. The measured result is that a
standard check **does** catch the damaging cases — when it is reading what the
model actually received. The failure is where the check is pointed, not how
sensitive it is, and B05 is built so both halves are visible side by side with
identical thresholds.

The angle I expected going in — *the quiet skews are the deadly ones* — is
false in this data and was dropped rather than written around. See
`FACTCHECK.md`, correction 2.

## Accent discipline

One terracotta moment per beat: B01 the deleted word · B02 the model stage ·
B03 the served series · B04 the cents bar · B05 the warehouse card · B06 the
comparison stage · B08 the period.

## Fill (GATE V)

`PairedBars` at four rows with no total row is a shorter stack than the
six-row Berkeley case it was built for. **This paragraph originally asserted
that it "still clears the fill floor comfortably." That was wrong, and it was
wrong because I carried the six-row arithmetic across instead of redoing it.**
GATE V measured 42% against the 55% floor and `compile.py` refused the cut.

The component now scales its row height by the number of slots actually
passed, anchored so the six-row-plus-total shape resolves to exactly 1 and
renders byte-identical. Re-measured: 65% cover at four rows. Logged as A25.

B01 and B08 carry `qc.sparse` waivers, as on every prior reel.
