# CHECKS-REPORT — Unautomated Security

Reel: `claude-gatekeeper-ci-pipeline` · 9 beats · **measured 131.3s (2:11)** vs 2:45 target
**GATE V (16:9): 18 frames · 0 BLOCKER · 4 MAJOR (underfill, deliberate — see below)**

## Deliverables

| | File | Format |
|---|---|---|
| 16:9 master | `claude-gatekeeper-ci-pipeline.mp4` | 3840×2160 @ 24fps |
| 9:16 companion | `vertical/claude-gatekeeper-ci-pipeline-vertical.mp4` | 1080×1920 @ 24fps |

**Built straight to `./art final`** — no review cut, so no beat chip or timecode is drawn
in any frame, and GATE V ran on both aspects rather than being skipped as the `--review`
path does.

## Title

The script's Scene 1 card reads `IT WORKS ON MY MACHINE`, kept **verbatim** on screen.
The reel is **titled "Unautomated Security"** (the script's own closing line) because the
**Week 1 reel is already titled "Works On My Machine"** and two near-identical titles
collide in a playlist. Nothing the viewer sees or hears changed.

## Per-beat classification

| Beat | Class | Measured | Pattern |
|---|---|---|---|
| B00 | SHOW | 20.71s | ClaudeComposerAsk |
| B01 | SHOW | 12.61s | BrutalistHesitantWriter — ≥9s ✓ |
| B02 | SHOW | 20.50s | ThreeStageBand (two stages) |
| B03 | SHOW | 18.54s | ThreeStageBand (three stages) |
| BASK | SHOW | 7.49s | ClaudeComposerAsk — clears the ≥7s typing floor |
| B04 | SHOW | 16.62s | CiGateSplit — held MERGE BLOCKED |
| B05 | SHOW | 11.26s | ClaudeCodeBeat |
| BHTF | SHOW | 14.61s | ClaudeComposerAsk |
| BOUT | SHOW | 8.81s | HaiTitleOutro |

**9 SHOW / 0 HOLD / 0 PUNT.** Slots 9/9. No slates. **Zero new components.**

## The MAJORs are deliberate

B01's type was raised to **88px** (earlier reels used 52–58). Reaching the 55% fill floor
would require roughly four lines at ~170px spanning most of the frame, which turns a
deliberately sparse BLUF into a wall of text. `FILL-THE-CANVAS LAW` permits deliberate
negative space; it targets *accidental* dead space under **undersized** type, and at 88px
the type is not undersized. Same for the outro poster card.

Accepted and recorded, not silently ignored.

## Illustrative data

Nothing from the real repository was supplied:

- **B00** — the `4 of 19` / `15 cases` split dramatises the manual-testing gap.
- **B04** — PR `#62`, the `18 of 19` counts, and the four named tests.

The failing case is deliberately a **directional error** — the blind spot the Week 2 reel
identified — so the example is consistent with the series. The counter stops one short so
the merge button never arms, which is the beat's claim.

**To make them real:** paste the actual test names and counts into B04's props and B00's
output lines. Narration needs no change.

## Corrections carried into the reel

1. **Branch protection (B05).** Scene 4 says the pipeline blocks the merge and builds a
   perimeter regressions "cannot physically enter". True only when the Actions check is
   marked **required**; otherwise CI reports red and the merge button still works.
2. **"self-healing perimeter" not repeated as stated.** CI blocks regressions; it heals
   nothing. Narration says what the pipeline actually does.

## Teaching arc

```
FRAMEWORK ✓      B01 BLUF + B02 the harness, before any automation.
WORKED EXAMPLE ✓ B03 the pipeline building itself · B04 a PR that cannot merge.
FALSIFIABILITY ✓ B04 — one payload through and the build dies.
SCAFFOLDED TASK ✓ B05 the pytest command + the required-check setting.
BOOKENDS ✓       B00 cold open · B01 BLUF · BHTF handoff · BOUT restate.
NO-SOURCE-NO-VERDICT ✓ no pass rate, coverage or runtime claimed as measured.
```

## Open items

1. **Replace the illustrative test names and counts** with the real `test_main.py`.
2. **Runtime 2:11 vs 2:45 target.** Not padded; duration is an output.
3. **Lane-mix warning (not blocking).** `remotion` carries 9/9 beats.
4. **SKIN LINT warning (expected).** `BOUT` uses `HaiTitleOutro`.
