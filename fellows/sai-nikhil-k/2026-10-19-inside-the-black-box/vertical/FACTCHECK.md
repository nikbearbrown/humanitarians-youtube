# FACTCHECK — Inside the Black Box, Part 1

"Essay" = Wolfram 2023, archived at `research/wolfram-2023-02-14-what-is-chatgpt-doing.html`.

## Claims

| # | Claim | Where | Checked against | Result |
|---|---|---|---|---|
| 1 | ChatGPT writes one word (token) at a time | B00 | Essay: "just asking over and over again … each time adding a word. (More precisely … a 'token')" | ✅ |
| 2 | A neuron weighs inputs, adds them, applies a simple function | B01, B02 | Essay: "we compute f[w . x + b] … here we'll just use Ramp (or ReLU)" | ✅ |
| 3 | ChatGPT is a formula like that "with billions of terms" | B01 | Essay: "The neural net of ChatGPT also just corresponds to a mathematical function like this—but effectively with billions of terms." | ✅ |
| 4 | Training nudges weights downhill; ends in "some mountain lake", not always the lowest | B03 | Essay: "Like water flowing down a mountain … some local minimum … ('a mountain lake'); it might well not reach the ultimate global minimum." | ✅ |
| 5 | A toy net needed millions of examples for one simple shape | B03 | Essay figure labels 10,000 → 10,000,000 examples; "we often had to use millions of examples" | ✅ |
| 6 | Retrained nets agree on the examples, not beyond them | B03, B04 | Essay: "different-but-equivalent solutions … 'extrapolation' … dramatically different results" | ✅ |
| 7 | "There's really no way to say" which is right | B04, B06 | Essay, verbatim | ✅ |
| 8 | Ten nets trained here all fit (worst MSE 0.0022) | B05, B06 | `evidence/train_nets.out` | ✅ measured |
| 9 | Their guesses at x = 3 run from −0.43 to 2.84 | B05, B06 | `evidence/train_nets.out` (seeds 0–9, all reported) | ✅ measured |

## The math (B02)

1. `y = f(w·x + b)` — the essay's `f[w . x + b]`.
2. `f(z) = ReLU(z) = max(0, z)` — the essay's Ramp.
3. `f(0.5 − 0.8 + 0.1) = f(−0.2) = 0`, with w = (0.5, −0.8), x = (1, 1), b = 0.1 (constructed).

Asserted in `build_beats.py`: 0.5·1 + (−0.8)·1 + 0.1 = −0.2; max(0, −0.2) = 0.

**Rendered-frame math review (2026-10-25, both aspects; B02 unchanged since):**
bold upright **w**, **x**; italic y, f, b, z; upright ReLU and max; true minus
signs; no tofu or clipping; reveals at 2.6 / 6.6 / 10.3 s, inside the 15 s comp.
16:9 row 1 ≈ 8% of frame height; 9:16 rows 7.2% / 3.8% / 3.4% (floor 2%).

## The numeric case (B05)

`python3 evidence/train_nets.py > evidence/train_nets.out` — Python 3.11.5, NumPy
1.24.4, arm64 macOS 27.0.1, 2026-10-26, ~30 s. Constructed step task, 400
points; 1-32-32-1 ReLU; full-batch Adam lr 0.01, 4,000 steps; seeds 0–9.
`build_beats.py` reads the summary from the .out and asserts it.
