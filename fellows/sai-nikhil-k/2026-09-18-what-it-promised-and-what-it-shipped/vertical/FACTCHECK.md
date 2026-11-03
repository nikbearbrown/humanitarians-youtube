# FACTCHECK — What It Promised, And What It Shipped

Algebra is verified **separately from the typography**, per
`docs/MATH-TYPESETTING.md`. Typography is verified by looking at rendered frames
(below, after the render); the arithmetic is verified by running it.

## The reproducible check

`python3 build_beats.py --check` asserts all of the following and refuses to
write the beat sheet if any fails:

```
P  = 0.92957            metrics.precision   (loon_v1.json, verbatim)
R  = 0.80012            metrics.recall      (loon_v1.json, verbatim)
F1 = 2PR/(P+R)          computed here; NOT on the card
```

| Assertion | Why it is there | Result |
|---|---|---|
| `abs(F1 - 0.860) < 5e-4` | the figure printed on B04 must be the figure computed | F₁ = 0.860000980985 → **0.860** ✓ |
| `min(P,R) <= F1 <= max(P,R)` | a harmonic mean must lie between its arguments; catches a swapped numerator/denominator | 0.80012 ≤ 0.86000 ≤ 0.92957 ✓ |
| `round(P,3) == 0.930 and round(R,3) == 0.800` | the rounding shown on screen must be the honest rounding of the card value | ✓ |
| `abs(1/(1-R) - 5.0) < 0.01` | "one loon in five" (B05, B06) must actually be one in five | 1/(1−0.80012) = 5.003 ✓ |
| `typeset(expr)` for all three rows | mathtext must actually set each expression; **there is no text-card fallback** — if this raises, B04 is BLOCKED, not downgraded | ✓ |
| `len(s) <= 42` for all deck strings | fixed-x SVG text in `BinaryBranch` does not reflow; a long string overprints silently and Remotion still exits 0 | all 9 strings ✓ (longest 41) |

## The three expressions on B04, and what each symbol is

Set by `runtime/scripts/typeset_math.py` (matplotlib mathtext → outlined SVG,
`svg.fonttype=path`, STIX). Real fraction bars; `TP`/`FP`/`FN` upright via
`\mathrm` because they are labels, not products of variables; `F_1` a true
subscript.

```
        TP                          TP                        2PR
P = ───────────  = 0.930    R = ───────────  = 0.800    F₁ = ───── = 0.860
     TP + FP                     TP + FN                     P + R
```

- **TP** — true positives: loons the model boxed that were loons.
- **FP** — false positives: boxes that were not loons (the reed bed, last week).
- **FN** — false negatives: loons that were there and got no box. This is the
  one B05 is about.
- The two definitions **differ by exactly one term in the denominator**, which is
  the whole point of the beat: precision is judged against what the model said,
  recall against what was actually there.

### Domain conditions (shown on the beat)
`TP + FP > 0` and `TP + FN > 0` — both denominators must be non-zero. With
P, R > 0 as given, both hold. F₁'s denominator `P + R = 1.72969 > 0`.

### What is asserted vs. what is quoted
- P, R, mAP50, mAP50-95 are **quoted** from the card. We did not recompute them
  and the reel does not claim to have validated them — B03's note names the
  source as the Ultralytics validation split stored in the checkpoint.
- F₁ is **ours**. B04's note says so ("ours, not the card's") and the narration
  says "I computed it from the two it does."
- No IoU-based figure, per-class figure, epoch curve, confusion matrix or
  field-accuracy figure appears anywhere, because none was supplied.

## Non-numeric claims checked against the artifact

| Claim | Where | How it was checked |
|---|---|---|
| "no server and no account" | B00 | No credential prompt exists in the flow; backend binds loopback; `--help` says "this is not a network service"; no remote endpoint string in the backend binary |
| "Nothing in that list reaches for a server" | B01 | Scoped deliberately to the listed components (shell, Python service, onnxruntime, weights, SQLite) — all local, all in-bundle |
| "the detector ships inside" | B00, B06 | `models/loon_v1.onnx` and `_internal/onnxruntime/` are inside `Gavia.app` |
| "ran on CPU in about an eighth of a second" | B06 | `CPUExecutionProvider` in the startup log; four warm calls at 0.124–0.143 s |
| "calls itself a prototype on every screen" | B06 | The footer "PROTOTYPE FOR CONSERVATION RESEARCH" is present in all three supplied captures |
| "AI results contain errors and should be reviewed" | B06 | Paraphrase of the About page's own "Important note" |

**Scope limit stated plainly:** all of the above was checked on one machine
(arm64 macOS), against one build, by mounting the DMG the author supplied. The
reel does not claim the app has been tested in the field.

## Frame review — math typography

`MATH-TYPESETTING.md` requires inspecting actual equation frames at their
revealed states and at 15/50/85% of the beat, **in the final output aspect**.

- [ ] B04 landscape (3840×2160) — row 1 at reveal, rows 1–2, rows 1–3
- [ ] B04 landscape — 15% / 50% / 85%
- [ ] B04 portrait (2160×3840) — same six frames, `TypesetMath916`
- [ ] Fraction bars unbroken; `TP`/`FP`/`FN` upright and unclipped; `F_1`
      subscript not colliding with the fraction; no glyph fallback boxes
- [ ] Readable at ordinary viewing size, not only at 4K

Results recorded in `_qc/REPORT.md` and any correction made here first, then in
the authored source, then re-rendered.
