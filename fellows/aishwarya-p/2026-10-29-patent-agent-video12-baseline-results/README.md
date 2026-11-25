# 2026-10-29 - What the Baseline Found (patent agent progress video 12)

**Week covered:** 2026-10-24 - 2026-10-30

**Video:** `patent-agent-video12-baseline-results.mp4` (16:9) · `patent-agent-video12-baseline-results-short.mp4` (9:16)

**YouTube:** Not yet published.

**Process log:** [FRICTIONAL.md](./FRICTIONAL.md)

## Result

This week was the first real measurement of the Mycroft patent claim classifier. All 50 independent claims in the test set (16 patents) were labelled by hand, and the classifier was run on all of them once.

- **The labels:**
  - breadth: 46 narrow and 4 broad;
  - posture: all 50 defensive.
- **The baseline run:** 50 calls to `claude-sonnet-5`. The cost upper bound was $0.32; actual usage was not recorded.
- **Breadth:** accuracy 0.66, Cohen's kappa 0.08. A model that always says "narrow" would score 0.92.
- **Posture:** accuracy 0.60, Cohen's kappa 0.00. A model that always says "defensive" would score 1.00.
- **No collapse.** The collapse check did not fire.
- **The classifier leaned the other way.** It predicted broad/offensive for 11 claims, and 10 of those 11 were labelled narrow. Its reasoning treated functional wording such as "configured to" and "a protrusion" as broad, while the labels read named parts and specific limits as narrow.
- **A refusal bug was found and fixed.** Three claims on one patent (US-11766760-B2, a cryogenic grinding process) kept failing.
  - Raising the token limit didn't help.
  - One diagnostic call showed the model refusing partway through its answer (`stop_reason: "refusal"`, 155 of 1000 output tokens). That left half a JSON reply the parser couldn't read.
  - `claim_classifier.py` now treats any refusal as declined, and all 50 claims score.

**Not finished:**
- The prompt fix (Phase 4) has not started.
- The test set can't yet measure posture agreement, because every label is defensive.

---

## The built reel

| | |
|---|---|
| 16:9 master | `patent-agent-video12-baseline-results.mp4`: 3840×2160, 24fps, 145.24s |
| 9:16 short | `short/patent-agent-video12-baseline-results-short.mp4`: 2160×3840, 24fps, 149.74s; all 8 beats plus a silent end card; no channel-title overlay in the short's beat sheet |
| review cut | `patent-agent-video12-baseline-results-slate.mp4` |
| beats | 8: 4 Remotion bookends (B00A, B00, B05, B06) and 4 Manim content beats (B01-B04) |
| voice | Kokoro `af_bella` |
| build | 8 of 8 beats filled (`STATUS.md`) |
| gates | GATE P: `PEDAGOGY.md` signed `VERDICT: PASS` · GATE V master: 16 frames, 0 BLOCKER, 10 MAJOR · GATE V short: 18 frames, 0 BLOCKER, 8 MAJOR |

---

## Figure → beat map

| Beat | Act | Scene | Duration | What it argues |
|---|---|---|---|---|
| B00A | Intro | `ClaudeComposerAsk` | 14.74s | Presenter summary |
| B00 | Intro | `ClaudeComposerAsk` | 12.50s | Cold open: suspected stuck on narrow/defensive; measured leaning the other way |
| B01 | Setup | `B01_LabeledTestSet` | 22.83s | Last week's harness and $0.92 query; 50 claims from 16 patents labelled by hand |
| B02 | Method | `B02_AccuracyVsKappa` | 26.43s | Accuracy next to the majority baseline, then kappa 0.08 / 0.00 |
| B03 | Finding | `B03_LeansTheOtherWay` | 26.39s | 11 broad/offensive predictions, 10 labelled narrow; functional wording read as broad; the all-defensive caveat |
| B04 | Bug fix | `B04_RefusalBug` | 25.26s | Refusals on one grinding patent; the mid-answer refusal; the `stop_reason` fix; 50/50 scored; prompt fix next |
| B05 | Next steps | `ClaudeComposerAsk` | 12.82s | Handoff: beat the baseline before you trust the score |
| B06 | Outro | `ClaudeTitleOutro` | 4.27s | Title restate |

Manim scenes are in [scenes.py](./scenes.py).

## Things not to get wrong

1. **Accuracy 0.66 and 0.60 sound moderate, but both are below the always-same-answer baseline.**
   - The majority baselines are 0.92 (breadth) and 1.00 (posture).
   - Kappa is 0.08 and 0.00, barely better than chance.
2. **"Leaning broad/offensive" is a direction in the disagreements, not a collapse.** It rests on 11 predictions, and the collapse check did not fire.
3. **The posture result can't be read as posture agreement.** All 50 labels are defensive, so a model that always says "defensive" would score 100%. This set needs offensive and broad examples. B03 states this on screen.
4. **The labels are one person's judgment.** The disagreement is shown as a difference in reading (functional wording vs. named parts), not as the classifier simply being wrong.
5. **$0.32 is an upper bound.** The harness records no token usage, so the actual charge is lower and wasn't measured. The narration says "at most thirty-two cents".
6. **"Three claims kept failing", not "three claims refused".**
   - Claim 1: the refusal was confirmed directly by the diagnostic call.
   - Claim 7: the refusal is recorded in its cached result.
   - Claim 5: failed the same way, but wasn't tested on its own.
7. **The cause of the refusal is not known.** The video says it happened and how the code handles it now. It offers no guess at why that patent triggered it.
8. **The prompt fix is next work only.** No Phase 4 result is shown or implied.

See [PEDAGOGY.md](./PEDAGOGY.md) for the evidence table.

## Known defects

From the build's Gate V reports (`_qc/REPORT.md` for the master and `short/_qc/REPORT.md` for the short):

- **Master:** 10 MAJOR `underfill` flags (content fills less than 55% of the safe area) on B01, B02, B03, B04, B06. No BLOCKERs.
- **Short:** 8 MAJOR `underfill` flags on B01, B02, B03, B04, B06, END. No BLOCKERs.

From [FRICTIONAL.md](./FRICTIONAL.md):

- **A card overlap in portrait B03,** found by frame check and re-spaced before the short was built.

## Files

- [README.md](./README.md): this page.
- [NARRATION.md](./NARRATION.md): the approved narration, one paragraph per beat.
- [beat_sheet.json](./beat_sheet.json): the edit: 8 beats, narration, scene per beat, measured audio durations, build stamp.
- [scenes.py](./scenes.py): the four Manim content scenes (B01-B04).
- [PEDAGOGY.md](./PEDAGOGY.md): act structure, evidence table, friction protected, `VERDICT: PASS`.
- [FRICTIONAL.md](./FRICTIONAL.md): the process log for this work.
