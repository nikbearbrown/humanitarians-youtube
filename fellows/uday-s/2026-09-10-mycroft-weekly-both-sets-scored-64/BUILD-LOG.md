# BUILD-LOG — Both Sets Scored 64

Skill: `cli-explainer` spine, weekly work report. Channel `claude-hai`.
Subject: mycroft @ `253ee74`. **Episode 3** of the Mycroft weekly.

## How this episode was found

Episode 2's lesson was "ask what the code refuses to do". That would not have
found this one. The centrepiece came from running steps 4 and 5 on **both**
fixture sets and diffing the outputs rather than the logs:

```
clean set      overall_score 64      3 flags
defective set  overall_score 64      8 flags
```

The corrupted set — 5 duplicates removed, 6 rows rejected, 6 quality flags —
reports the same headline number as the clean one. The arithmetic cannot tell
them apart; only the flag list can. That is the entire argument for step 5's
"loud substitutions" rule, demonstrated rather than asserted.

Recorded in PROMPTS.md as the reusable move: **run it twice on different inputs
and diff what it reports.**

## Precision over a better line

The two scores are **not identical** — the unrounded values are 63.75 and 64.0.
"Identical" would have been the stronger sentence and a small fabrication. The
narration says "the same headline number" and the on-screen figure is the
reported `overall_score`, which is what both runs emit. FACTCHECK.md row 10.

## PROOF compliance

| Criterion | This cut |
|---|---|
| Explicit framework | B02 — MEASURED OR SUBSTITUTED / DOES THE OUTPUT SAY / CAN YOU WALK IT BACK, at **21.85s**, ahead of step 4 at 49.18s |
| Reusable rubric | Applies to any number any pipeline emits |
| Worked example | Both steps scored on the same three questions |
| Falsifiability | B09 — predicted by question 1, and a callback to episode 1: the frozen corpus reaches only 5 of the 10 catalogue flags, and the 5 it misses are exactly the substitution paths |
| Active task | B11 — question 2 turned on the viewer's own numbers, GOOD/BAD |
| Friction | B08 states the result before B09 explains why it matters |

## Gate record

```
GATE L   searched before authoring; no reusable hit; 6 beats authored as Manim
GATE F   full paperwork set written up front (learned from the last reel, where
         it failed on a missing SHOTLIST)
GATE A   clean on all six, first pass
GATE W   clean on all six, first pass
GATE B   pixel-true — 0 errors, 0 warnings, FIRST PASS, no re-renders
GATE V   clean cut: 429 frames, BLOCKER 0, MAJOR 63 (58 underfill · 5 low-contrast)
```

Four reels in, the layout helpers have converged: kicker at buff 0.72,
content-adaptive box widths, `fit_src()` reserving the citation strip, every
label composed INTO the fitted group, `_fit()` scaling up as well as down, and
never a line drawn through text. Each of those cost a re-render to learn on an
earlier reel and cost nothing here — GATE B passed first time.

Underfill is 13.5% of sampled frames — build-in ramps plus the sparse outro
card. The 5 low-contrast flags co-occur with 10–11% fill readings: near-blank
frames at beat openings, not unreadable content. Documented, not silenced.

`./art run` prints "26 BLOCKER" because GATE V reads `*-slate.mp4`, the review
cut, whose timecode burn-in sits outside title-safe by construction.

## Deliverable

```
BothSetsScored64_UdaySonawane_2026-09-10.mp4   1920x1080   214.28s (3:34)
```

4K master needs no re-render: `./art final <reel>`. Nothing here publishes.
