# BUILD-LOG — It Never Says Pass

Skill: `cli-explainer` spine, weekly work report. Channel `claude-hai`
(@HumanitariansAI, Kokoro `am_onyx`, Pragmatist).
Subject: mycroft @ `aa0c0fe`, branch `feature/market-sentiment-human-report`.
**Episode 4 — the six-step arc closes.**

## How this episode was found

Episode 2's lesson was "ask what the code refuses to do"; episode 3's was "run
it twice and diff the outputs". This one needed a third question:

```
claude "what does this step REFUSE to conclude, and where does it say so?"
```

That surfaced the line the episode is named for — *an audit reports what it
found; it never says "pass"* — and one level down, the gate-4 note where the
report criticises one of its own gates in writing.

Three of the four episode titles came from a docstring. **Read the comments
before the diff.**

## PROOF compliance

| Criterion | This cut |
|---|---|
| Explicit framework | B02 — WHAT A RECORD SUPPORTS / WHAT YOU INFERRED / WHO DECIDES at **24.08s**, ahead of step 6 at 50.26s |
| Reusable rubric | Applies to any automated report or dashboard |
| Worked example | B04→B05 (findings split) and B07→B08 (the gates) |
| Falsifiability | B09 — gate 4 is satisfiable by doing nothing. Predicted by question 3, and a direct callback to episode 1: a validator with nothing to catch is not passing; this is a gate with nothing to fail |
| Active task | B11 — question 3 on the viewer's own dashboard, GOOD/BAD |
| Friction | B05 demotes episode 3's headline number before B08 explains why it matters |

## Gate record

```
GATE L   searched before authoring; no reusable hit; 6 beats authored as Manim
GATE F   full paperwork set written up front
GATE A   clean on all six, FIRST PASS
GATE W   clean on all six, FIRST PASS
GATE B   pixel-true — 0 errors, 0 warnings, FIRST PASS, no re-renders
GATE V   slate pass 26 BLOCKER (the review burn-in) + 2 MAJOR
```

Six reels in, the layout helpers have fully converged: kicker at buff 0.72,
content-adaptive box widths, `fit_src()` reserving the citation strip, every
label composed into the fitted group, `_fit()` scaling up as well as down, and
never a line drawn through text. Each cost a re-render to learn on an earlier
reel; this reel needed none.

## 4K master

`./art final` recompiled at 2160 from the existing slots. **No beat was
re-rendered** — every source asset was already native 4K (Manim at 2160p24,
Remotion at `--scale=2`). Verified by `ffprobe` on the finished file and by a
1:1 crop:

```
Mycroft_UdaySonawane_09_17_2026.mp4   3840x2160 @ 24fps   213.29s (3:33)   14 MB
```

The `-slate.mp4` review cut stays 1080p — it is a working artifact with
timecode burn-in, and 4K would buy nothing there.

### Note on the session

The 4K step was interrupted several times by a session-level safety classifier
that blocked shell execution regardless of the command. The compile itself
succeeded; verification and the renamed copy had to wait until the session left
auto mode. Recorded because the build timestamps in `beat_sheet.json` jump
around as a result, not because anything about the reel changed.

## Repo hygiene

Verification runs against mycroft rewrote one file's `generated_at`
(`logs/…-2026-08-27-clean.json`). Restored with `git checkout --`; the mycroft
working tree was left clean.

## The series

```
ep 1  Build the Defects First   9ef4e7f   the corpus before the validators
ep 2  Transport, Do Not Repair  bdc1bc1   what a stage refuses to do
ep 3  Both Sets Scored 64       253ee74   measured or substituted
ep 4  It Never Says Pass        aa0c0fe   evidence, inference, and who decides
```

Nothing here publishes.
