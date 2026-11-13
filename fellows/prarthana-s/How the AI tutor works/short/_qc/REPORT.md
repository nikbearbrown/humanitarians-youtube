# Visual QC — the 9:16 short

**Derived:** 2026-09-10 from the 16:9 parent · 1080×1920 · 177.9s (**2:57.9**)
**Cap:** 180.0s hard, 2.0s planning headroom → **2.1s of margin. Tight.**
**Method:** frames sampled per beat into `_qc/frames/` and read.

---

## The cut

`--drop B04` — the predict/pause beat. It is the one beat that is a deliberate silence
rather than information, so the short loses no content by dropping it.

```
B00 16.87  B01 19.75  B02 19.61  B03 20.50  B05 22.04
B06 20.97  B07 17.54  B08 24.58  B09 11.50  END  4.50   = 177.87s
```

Only B09's audio was regenerated (the outro rewrite). Every other beat reuses the
parent's mp3 exactly, per the Shorts Law.

### Length — read this before publishing

I originally estimated 2:46 for a B04 drop. That was wrong: the auto-rewritten outro is
**11.5s** against the parent's 3.7s, and a 4.5s endcard is appended. Real total 2:57.9.

2.1s of margin against a hard cap is uncomfortable. Two ways to buy room, both one flag:

| Option | Result | Trade |
|---|---|---|
| `--no-outro-rewrite` | **2:50.1** (~10s margin) | Outro no longer names what was cut |
| also `--drop B08` | **2:33.3** (~27s margin) | Loses the handoff prompt; endcard carries the funnel |

Left as-is pending a decision — it is under the cap and valid.

### The outro copy needed overriding

The auto-rewrite defaults its "Next:" line to the dropped beat's own narration, which
produced: *"The full video also covers Before I show you, take…"* — the dropped beat's
opening words, verbatim and truncated. Overridden with
`--next "the pause to guess where your book actually lives"`.

---

## Portrait re-layouts

Three new `916` compositions were written for this cut, because generated graphics are
never centre-cut and none existed:

| Beat | Composition | Re-layout |
|---|---|---|
| B01 | `MedhavyStatementStack916` | serif lines, narrower measure |
| B02, B07 | `MedhavyCompareColumns916` | two columns → **two stacked blocks** |
| B03, B06 | `MedhavyStepFlow916` | four-across → **four-down**, vertical connectors |

`MedhavyTerminalAsk916`, `MedhavyCodeBlock916` and `MedhavyOutro916` already existed.

**The empty bottom third of every frame is deliberate.** `tokens/layout.ts` warns the
Shorts UI covers roughly the bottom 25% and right 11% at runtime, so these components lay
out inside `P916` — above y≈1430, left of x≈952. On the desktop frame that reads as dead
space; on a phone it is exactly the area the UI occupies.

---

## Defects found and fixed

| Beat | Defect | Fix |
|---|---|---|
| B08 | Command clipped at the right edge — the third question, which the narration calls "the question that bites", was cut off | Re-wrapped to ≤22 chars |
| B05 | The `keywords` line — the beat's entire point — cut at `"problem 7  eq` | Re-wrapped to ≤26 chars, single space between labels |
| B05 | Full episode title overflowed the card header | `segment` shortened to "Grounded in Your Textbook" |
| B00 | Same clipping as B08 | Re-wrapped to ≤20 chars |

**Cause:** `MedhavyTerminalAsk916` and `MedhavyCodeBlock916` render mono at a size fitting
roughly **25–26 characters** at 1080 wide, and both use `whiteSpace: 'pre'` — so an
over-long line runs off the edge instead of wrapping. The landscape sheet's wraps run to
49 characters.

These re-wraps live in **the short's own beat sheet**. The 16:9 parent keeps its own
wrapping, which is correct: the two frames have genuinely different character budgets,
and rule #4 only requires the props match the 916 schema, not that they match the parent.

## Verified after fix

- `B08_fix.png` — all four lines whole, including "exact passages used?"
- `B05_fix.png` — `"problem 7 equation 1.13",` complete; chip reads **JSON**
- `B02.png`, `B03.png` — stacked layouts legible, content above the UI line

## Remaining, minor

- B05's card header wraps to two lines with the JSON chip alongside it. Not clipped.
- Each frame's lower third is empty by design (see above).

---

## Toolkit work this cut required

Four more Windows bugs, all in `../BRUTALIST-WINDOWS-BUGS.md`:

- `shorts.py` symlinked the parent mp3s — Windows refuses without admin (WinError 1314)
- `shorts.py` read `Root.tsx` with no encoding and swallowed the failure in a bare
  `except`, so **every** portrait composition was reported missing even when registered
- `shorts.py` wrote the short's beat sheet as cp1252 — unreadable downstream
- the same unencoded text I/O across 15 runtime scripts (36 call sites, now all UTF-8)

The second of those is the one worth fixing upstream first: it does not crash, it returns
a confident wrong answer and sends you off to author components that already exist.
