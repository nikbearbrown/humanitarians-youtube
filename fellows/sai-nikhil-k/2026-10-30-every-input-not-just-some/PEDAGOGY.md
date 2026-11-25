# PEDAGOGY — Every Input, Not Just Some

**Reel** `weekly_updates/2026-10-30-every-input-not-just-some/` · **slug** `claude-sai-every-input-not-just-some`
**Subject** Anthropic, "LLMs are making formal software verification feasible at a much larger scale" (Oct 22, 2026) · **week of** 2026-10-30, second reel (built 2026-11-09, backlog)
**Host** Sai, in his own name · **Voice** Kokoro `am_onyx`, free and local
**Chassis** Remotion + two image plates (the post's figures, credited; Theorem's repo; Commons photos), no Manim, nothing paid

---

## The ONE idea

> A test checks the inputs you try; a proof covers every input inside its
> theorem. Claude can now write such proofs at a scale no team could (239
> entry points, 123 libraries, ~180 million lines, checked by Rocq), but
> "formally verified" still isn't "bug-free": a proof covers exactly what its
> theorem says.

Sai's brief (2026-11-09): "lets work on the second video for each week. 10-30:
https://www.anthropic.com/research/formal-verification … Use as many images as
you can and go easy on math." He chose the angle and title, and chose to show
Anthropic's charts with credit (they carry no reuse licence).

## Act structure

| Beat | Act | Pattern | Why |
|---|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` | AI finds bugs; Anthropic says it can now prove their absence. What does a proof give you? |
| B01 | THE PRICE OF A PROOF | `TypesetMath` (light) | seL4: 20 ÷ 2 = 10 times the work; now 180 M lines ÷ 239 ≈ 753,000 lines each, by a model. |
| B02 | TESTS VERSUS A PROOF | plate · post illustration, dice, RISC-V board | A fuzzer samples; a proof covers every input ≤ 64 MB, about machine code. |
| B03 | THE RECIPE | `ClaudeScienceChipGrid` | Fuzz test → RISC-V binary → theorem → Claude's proof → Rocq checks; what you trust. |
| B04 | A MILLION TESTS, ONE PROOF | `ExecutedData` | Our toy: 1,000,000 random tests, 0 crashes; Z3 finds a 16 MiB crash; after the patch, none. |
| B05 | WHAT CAME OUT | plate · 3 post charts + repo screenshot | 239 entry points, hundreds of bugs; reuse; fewer tokens; 90 published so far. |
| B06 | VERIFIED IS NOT BUG-FREE | `BinaryBranch` | Inside the theorem vs outside it (x86/ARM + glibc, wrong answers, unproved code). |
| B07 | VERDICT | `ClaudeVerdictArtifact` | One page. |
| B08 | HANDOFF | `ClaudeComposerAsk` | State one property of your function; list what a proof would have to assume. |
| B09 | OUTRO | `LogoOutro` | `@HumanitariansAI`. |

## ILLUSTRATE LAW check

Claude UI at B00, B08 and the verdict only. Body beats:
`TypesetMath → images → ChipGrid → ExecutedData → images → BinaryBranch`.
No repeats; every beat has an ordered `show` block. "Go easy on math": one
two-row arithmetic beat (division only), which the math rule still requires.

## 9:16

Every Remotion pattern has a `*916` sibling; the two plates have re-composed
portrait plates in `pantry/`. B03 declares `qc.sparse` (staggered ChipGrid,
see below). Portrait-only edits: none planned.

## Evidence and honesty

- **The post's numbers are cited, not re-measured** — they describe Anthropic's
  and Theorem's own runs (239 entry points, 123 libraries, ~180 M lines, seL4
  2/20 person-years, ~40% fewer tokens, 30 of 34). On screen they are labelled
  as the post's.
- **Measured, Theorem's public index:** `evidence/theorem_index.py` at
  `f1fdc8dd`: 90 entry points in 32 libraries have published proofs; of 20,421
  statements tracked, 526 proved, 63 false, 19,600 open. B05 says "published so
  far: 90" — the post's 239 is what Claude proved; the repo releases a subset.
- **Executed locally, our toy:** `evidence/fuzz_vs_proof.py` — our decoder, not
  code from the post, and Z3, not Rocq. 1,000,000 random inputs ≤ 1 MiB: 0
  crashes (a fuzzer capped at 1 MiB cannot reach a > 16 MiB bug at all; the
  narration says "the way fuzzers cap them"). Z3 finds the smallest crash,
  16,777,220 bytes, in 0.013 s, and the replay crashes; after the fix, unsat.
- **Images:** Anthropic's four figures and a screenshot of the post, credited
  "© Anthropic PBC, shown with credit" by Sai's decision; Theorem's repo
  (MIT); three Commons photos (CC BY-SA 4.0). The proof-order chart is one
  frame (474 of 598) of the post's GIF, the first fully drawn one.
- **Interpretation kept modest:** the hero illustration's meaning isn't
  captioned in the post; the reel calls it "proving, and searching" only.

## QC declarations (2026-11-09, after GATE V refused the first final)

- **B05 — `qc.sparse` + `qc.contrast_regions`.** The staged 2×2 reveal has one
  chart up at the 50% sample (fill 21%), and Anthropic's pale charts pull the
  frame-wide ink contrast to 0.25–0.27 (floor 0.30). The beat's text is our dark
  kicker and captions, so two regions are declared: the kicker band and the first
  caption (on screen from 0 s), computed from `make_plates.placements` and valid
  in both aspects. Both pass; the 85% frame passes the fill check unaided.
- **B03, B07 — `qc.sparse`.** Staggered ChipGrid at 50%; centred verdict card (32%).
- All three live in `build_beats.py`, so `shorts.py --vertical` copies them.

## Attribution

Hosted by Sai. The post is by Anthropic's Frontier Red Team (15 authors) with
Theorem; the reel names Anthropic and Theorem. Photo credits per panel.

## Pronunciation (narration only)

- `seL4` → "S.E.L. four" · `RISC-V` → "risk five" · `ARM` → "Arm" · `AI` → "A.I.".

## Expected build noise (not bugs)

- SKIN LINT at B09 asking for `ClaudeTitleOutro` — wrong for this channel.
- B03's 50% portrait sample underfills (staggered chips); `qc.sparse` declared.

---

## Human review checklist

Nothing below has been done by the assistant.

- [ ] Anthropic's figures are shown with credit, not under a licence — still OK for the public video?
- [ ] Is the toy demo (our decoder, Z3) clearly enough labelled as ours?
- [ ] Anything here better left out of a public video?

---

## Full narration, as it will be spoken

<!-- NARRATION:BEGIN (generated from beat_sheet.json) -->

### B00 · ASK — `ClaudeComposerAsk` · 13.6s measured (50 words)

> Software is full of bugs, and A.I. keeps getting better at finding them. This
> is Sai. Anthropic now says A.I. can do something rarer: prove that a program
> won't crash, on every input. What does a proof give you that a million tests
> can't? And what doesn't it give you?

### B01 · THE PRICE OF A PROOF — `TypesetMath` · 17.7s measured (60 words)

> Start with what a proof used to cost. The S.E.L. four kernel took two person-
> years to write, and twenty to verify: ten times the work. Now the new number.
> Anthropic says Claude wrote about a hundred and eighty million lines of proof,
> for two hundred thirty-nine programs, in a few weeks. On average, around seven
> hundred fifty thousand lines each.

### B02 · TESTS VERSUS A PROOF — `image plate · hero+2` · 16.8s measured (55 words)

> Here's the difference. A fuzzer rolls dice: millions of random inputs, hunting
> for the one that crashes. However many it tries, it only knows about those. A
> proof is a statement about every input, here up to sixty-four megabytes, made
> about the compiled program itself, the risk five machine code, and checked by
> a machine.

### B03 · THE RECIPE — `ClaudeScienceChipGrid` · 18.1s measured (58 words)

> The recipe reuses tests people already wrote. Take an OSS-Fuzz test. Compile
> it to a risk five program. State the theorem: no crash, for any input up to
> sixty-four megabytes. Claude writes the proof, and the Rocq proof checker
> verifies it. Nobody reads a hundred million lines. You trust the machine
> model, the theorem's wording, and the checker.

### B04 · A MILLION TESTS, ONE PROOF — `ExecutedData` · 17.2s measured (56 words)

> We tried it at toy scale: a decoder whose bug only fires on files over sixteen
> megabytes. A million random tests under a megabyte, the way fuzzers cap them,
> found zero crashes. A solver found the crash in a hundredth of a second, and
> after the patch, proved there's no crashing input up to sixty-four megabytes.

### B05 · WHAT CAME OUT — `image plate · 2x2` · 19.2s measured (62 words)

> Here's what came out. Proofs for two hundred thirty-nine entry points in a
> hundred and twenty-three libraries, and hundreds of bugs fixed on the way. The
> proofs get cheaper: agents in a shared workspace reuse each other's files, and
> Opus five point five needs about forty percent fewer tokens than Opus five. So
> far, Theorem has published ninety of those entry points.

### B06 · VERIFIED IS NOT BUG-FREE — `BinaryBranch` · 18.1s measured (54 words)

> So does formally verified mean bug-free? The post says no, plainly. Inside the
> theorem, every input up to sixty-four megabytes is covered. Outside it: the
> x86 and Arm builds most people actually run, wrong answers that never crash,
> and entry points nobody proved. A proof is exactly as good as the theorem it
> states.

### B07 · VERDICT — `ClaudeVerdictArtifact` · 14.2s measured (49 words)

> So: proofs aren't only for avionics any more. A model can write them at a
> scale no team could, and a small checker keeps it honest. But a proof covers
> exactly what its theorem says, and today that's a risk five model of Linux,
> not the laptop you're holding.

### B08 · HANDOFF — `ClaudeComposerAsk` · 15.4s measured (56 words)

> Your turn. Pick a function you wrote, and ask an assistant to state one
> property it should hold for every input, in a single sentence. Then ask what
> you'd have to assume about the compiler, the chip and the operating system for
> a proof of it to mean anything. That second list is where proofs break.

### B09 · OUTRO — `LogoOutro` · 2.7s measured (6 words)

> Every input, not just some. Sai.

**Total: 506 words** → 153.0s measured (2:33). Audio remains the master clock.

<!-- NARRATION:END -->

---

VERDICT: __________     — reviewer: ______________  date: __________
