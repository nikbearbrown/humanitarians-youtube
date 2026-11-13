# CHECKS-REPORT — Works On My Machine

Reel: `claude-gatekeeper-zero-drift` · 9 beats · **measured 118.8s (1:59)** vs 2:30 target
**GATE V (16:9): 18 frames · 0 BLOCKER · 0 MAJOR ✓**

## Deliverables

| | File | Format |
|---|---|---|
| 16:9 master | `claude-gatekeeper-zero-drift-slate.mp4` | 3840×2160 @ 24fps |
| 9:16 companion | `vertical/claude-gatekeeper-zero-drift-vertical-slate.mp4` | 1080×1920 @ 24fps |

Both aspects verified by probe. `compile.py` defaults to `--fps 24`, so the format spec
(4K UHD, 24fps) is met without a flag.

## Per-beat classification

| Beat | Class | Measured | Pattern |
|---|---|---|---|
| B00 | SHOW | 14.10s | ClaudeComposerAsk |
| B01 | SHOW | 10.35s | BrutalistHesitantWriter — ≥9s ✓ |
| B02 | SHOW | 16.26s | ThreeStageBand |
| B03 | SHOW | 7.77s | ClaudeComposerAsk — clears the ≥7s typing floor |
| B04 | **PARTIAL SLATE** | 18.01s | **CiGateSplit** (new) |
| B05 | SHOW | 17.79s | ThreeStageBand — **failure mode** (new) |
| B06 | SHOW | 11.41s | ClaudeCodeBeat |
| BHTF | SHOW | 15.74s | ClaudeComposerAsk |
| BOUT | SHOW | 7.25s | HaiTitleOutro |

**8 SHOW / 1 partial-slate / 0 PUNT.** Slots 9/9 filled.

### The one gap — B04's left panel

The **FastAPI Dockerfile was never supplied.** The script calls for it and asks that both
artifacts be "fully legible", but the file is not on disk. Writing a plausible Dockerfile
and showing it as this project's file would be a DOUBLE-CHECK LAW violation, so that panel
renders a PIPELINE request naming exactly what is needed.

**The right half is complete:** PR #44, the counter running to 164, the progress bar, and
the merge button flipping `MERGE BLOCKED` → `ALL CHECKS PASSED`.

**To resolve:** set B04's `code` prop from the repo's Dockerfile (trim to ~14 lines —
`FROM`, `WORKDIR`, the `requirements.txt` COPY + `pip install`, `CMD`) and re-render that
one beat. `CiGateSplit` swaps the slate for a listing automatically once `code` is
non-empty. The narration already fits the real file, so nothing else changes.

## Dual render — both aspects delivered

**All 9 beats rewired to registered `916` compositions. Zero flagged, zero centre-cut.**

The script asks to keep core artifacts centre-framed for 9:16. Handled by re-layout, not
cropping: `CiGateSplit` stacks its two panels, `ThreeStageBand` serializes its three axes
top-to-bottom (verified on frame that the failure state — wash, border, ✕, strikethrough,
bypass line — all survive portrait).

`CiGateSplit` sizes its code listing from **panel width against the longest line**, not
from canvas height. Height-derived type is what clipped code mid-word in an earlier reel.

## Defects found and fixed — all by reading frames

GATE V passed this reel 0 BLOCKER / 0 MAJOR while all three were on screen.

| Beat | Defect | Fix |
|---|---|---|
| B04 | **`ALL CHECKS PASSED` was invisible.** The button filled terracotta, but the label had a *later* opacity ramp, and because the audio (18.0s) is shorter than the registered composition (21s) the clip is trimmed before the ramp completes. | Fill and label now arm together at p≈0.58. Same trimming trap as before, in a new shape — it is not enough for an animation to *end* by 0.80, every dependent element must too. |
| B04 | The slate note's authored line breaks **collapsed into one unreadable paragraph**. | `white-space: pre-line`. |
| B05 | The failed axis did not read as "red" the way the script asks — only a rule and an ✕. | Terracotta wash + terracotta border on the failed panel, alongside the strikethrough and ✕. No second accent introduced. |

## Components

**Built:** `CiGateSplit` + `…916` — a file panel (with slate support) beside a PR check
run and a merge button that only arms once the count completes.

**Extended:** `ThreeStageBand` gained a **failure mode** — `failIndex` washes and strikes
one axis and stops the travelling token there; `failLine` replaces the ready line with
the bypass command. Both default to off, so the two Week 2 reels render unchanged.
Scene 4 reuses the *same* band as Scene 2 rather than a second matrix component, which is
what makes the viewer read it as the same matrix returning.

## Teaching arc

```
FRAMEWORK ✓      B01 BLUF + B02 the three axes, before the PR.
WORKED EXAMPLE ✓ B04 — PR #44 against the matrix, with the gate actually lifting.
FALSIFIABILITY ✓ B05 — bypass axis three and watch the same matrix break.
SCAFFOLDED TASK ✓ B06 runnable command + pass condition; BHTF scores the viewer's repo.
BOOKENDS ✓       B00 cold open · B01 BLUF · BHTF handoff · BOUT restate.
NO-SOURCE-NO-VERDICT ✓ only #44 and 164 are claimed; nothing else is invented.
```

## Open items

1. **Dockerfile slate** (above) — the only thing standing between this and 9/9 SHOW.
2. **Runtime 1:59 against a 2:30 target.** Not padded; duration is an output
   (`duration-planner`). B02 and B04 have room if the target is firm.
3. **Lane-mix warning (not blocking).** `remotion` carries 9/9 beats against MOTION.md's
   ~40% guidance. Deliberate — every beat is a generated diagram or UI.
4. **SKIN LINT warning (not blocking, expected).** `BOUT` uses `HaiTitleOutro`;
   `ClaudeTitleOutro` hardcodes `@NikBearBrown` and is scoped by OUTRO-LOCK.md.
5. **Paperwork.** Built with `ART_FACTS=0`. A fully gated run needs `FACTCHECK.md`,
   `SHOTLIST.md`, `PROMPTS.md`.
6. **`./art final` not run** — no label-free master yet.
7. **Minor, not fixed:** in portrait B05 the travelling `a commit` token sits close to the
   failed panel's right border. Inside the safe area and legible; cosmetic only.
