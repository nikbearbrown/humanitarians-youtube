# CHECKS-REPORT — Silent Failures

Reel: `claude-gatekeeper-tracking-alerts` · 9 beats · **measured 128.7s (2:09)** vs 2:45 target
**GATE V (16:9): 18 frames · 0 BLOCKER · 0 MAJOR ✓**

## Deliverables

| | File | Format |
|---|---|---|
| 16:9 master | `claude-gatekeeper-tracking-alerts-slate.mp4` | 3840×2160 @ 24fps |
| 9:16 companion | `vertical/claude-gatekeeper-tracking-alerts-vertical-slate.mp4` | 1080×1920 @ 24fps |

## Per-beat classification

| Beat | Class | Measured | Pattern |
|---|---|---|---|
| B00 | SHOW | 19.43s | ClaudeComposerAsk |
| B01 | SHOW | 9.15s | BrutalistHesitantWriter — ≥9s ✓ (tight) |
| B02 | SHOW | 19.37s | ThreeStageBand (**two** stages, no code change) |
| B03 | SHOW | 7.06s | ClaudeComposerAsk — just clears the ≥7s typing floor |
| B04 | SHOW | 21.40s | **AlertSplit** (new) |
| B05 | SHOW | 17.62s | GatekeeperCorpusTable + new `headers` prop |
| B06 | SHOW | 11.24s | ClaudeCodeBeat |
| BHTF | SHOW | 14.57s | ClaudeComposerAsk |
| BOUT | SHOW | 8.68s | HaiTitleOutro |

**9 SHOW / 0 HOLD / 0 PUNT.** Slots 9/9.

## Dual render

**All 9 beats rewired to `916` compositions — zero flagged, zero centre-cut.**
`AlertSplit` stacks log and alert in portrait; `GatekeeperCorpusTable` reflows its four
columns into one card per row (four columns cannot be legible at 1080px);
`ThreeStageBand` serializes its two panels.

## Data on screen is ILLUSTRATIVE — the main open item

No real `evaluation_logs` contents were supplied, so every row and count is constructed:

- **B04** rows `claim_017 / DIRECTIONAL`, `claim_018 / MAGNITUDE` — **captioned on screen**
  as "illustrative rows — replace with real log output before publish".
- **B05** four `run_01xx` rows and the **240** evaluation count.
- **B00** the `14:22:07` discarded verdict.

These show the SHAPE of a queryable ledger; they assert nothing about the project's real
error profile. To make them real: paste rows into B04/B05, set B05's `countTo`, drop
B04's `rowNote`, re-render those two beats. The narration needs no change.

Same rule applied to `ingest.py` (wk2) and the Dockerfile (wk1).

## The alert card is deliberately generic

Scene 3 asks for a "mock Slack/Discord notification". Built as a **generic** chat
notification in the Claude skin — channel line, terracotta rule, title, body, metadata.
It does not reproduce Slack's or Discord's chrome, colours or marks: a fidelity brand may
not wear another product's interface, and that interface is their trade dress. The shape
reads as "a message landed in a channel" without imitating a specific product.

## Teaching arc

```
FRAMEWORK ✓      B01 BLUF + B02 the two principles, before the pipeline run.
WORKED EXAMPLE ✓ B04 — row commits and alert fires, both moving, in one beat.
FALSIFIABILITY ✓ B05 — why workflow logs are not enough; the ledger as analytics.
SCAFFOLDED TASK ✓ B06 runnable sqlite3; BHTF turns counts into an error profile.
BOOKENDS ✓       B00 cold open · B01 BLUF · BHTF handoff · BOUT restate.
NO-SOURCE-NO-VERDICT ✓ no accuracy or volume metric claimed as measured.
```

## Reuse note

Three scenes needed **no new component**:

- Scene 2's **two** boxes — `ThreeStageBand` takes an N-length `stages` array, so two
  panels and one connector laid out with zero code change.
- Scene 4's log table — `GatekeeperCorpusTable` gained a `headers` prop (defaulted, so
  the Week 2 reel is unchanged) rather than a second table component.
- Scene 5 — `ClaudeCodeBeat`.

## Open items

1. **Replace the illustrative rows** (above) — the one thing standing between this and
   publishable data.
2. **Runtime 2:09 vs 2:45 target.** Not padded; duration is an output.
3. **B01 at 9.15s is tight** against the ≥9s law. If its narration is ever shortened,
   re-check that the correction still lands before the cut.
4. **Lane-mix warning (not blocking).** `remotion` carries 9/9 beats.
5. **SKIN LINT warning (expected).** `BOUT` uses `HaiTitleOutro`.
6. **Paperwork.** Built with `ART_FACTS=0`.
7. **`./art final` not run** — no label-free master yet.
