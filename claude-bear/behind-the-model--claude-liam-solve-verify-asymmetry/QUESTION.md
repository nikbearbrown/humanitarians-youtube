# QUESTION

**The question:** If an AI can solve a problem almost instantly, why can checking
that answer take far longer — and does a faster model ever close that gap?

**Mode:** redo — source is
`anthropics/youtube/behind-the-model/claude-liam-solve-verify-asymmetry/beat_sheet.json`
("Solve-Verify Asymmetry — AI Thinks Fast, Verification Thinks Harder",
Teardown-register, CLI-style video, `register: "Teardown"`, `brand:
"claude-liam"`, `style: "cli"`, cold open a `NikBearBrownOpen` title card,
terminal-ask (`NikBearBrownTerminalAsk`) and code-block (`NikBearBrownCodeBlock`)
beats, Manim bar-chart body beats, Your Turn, `ClaudeTitleOutro`). Source B01,
B06, B07, B08 were fully authored narration (not seeded placeholders); those
facts carry forward, compressed for the Plain register and the hai-simple
ten-beat shape used by the sibling `behind-the-model--claude-liam-*` redos.

**Why it earns a reel:** the natural shortcut is to assume that because an AI
answers fast, confirming the answer should be roughly as fast — you're just
glancing at work already done. The source's own measurement breaks that: an
experiment timing an AI's solve time against a strict, deterministic check
across problems of rising difficulty shows the check taking three to a
hundred times longer, not the same, and the gap widens with difficulty. One
early number (arithmetic, ~3x) looked suspiciously low and turned out to be a
measurement artifact (a hidden checker startup cost); removing it tightens
arithmetic to near parity while leaving every harder ratio unchanged —
confirming the gap is structural, not a glitch in the stopwatch.

**Naive framing (B00, corrected on screen):** "Claude solved it in two
seconds. So checking is fast, right?" → corrects "fast" to "harder" (the real
frame: for hard problems checking, not solving, is the harder half).

**Body facts carried from source (unchanged):**
- the experiment: ten math problems of rising difficulty, AI solve time timed
  against a deterministic verification pass (sympy/eval-style checking),
  ratio = verify time / solve time (source B02/B03) — this is the reel's
  anchor, planted with the raw ratios
- the raw ratios: arithmetic ≈3x, algebra ≈20x, quadratic ≈40x,
  combinatorics ≈100x (source B04)
- the revision: the arithmetic ratio looked too low, traced to an unwarmed
  checker inflating the "solve" side of the comparison; filtering it out
  tightens arithmetic to ≈1:1 while every harder ratio holds (source B05/B06)
  — this is the anchor's payoff, same ladder, corrected numbers
- the full proof-sketch ratio, ≈300x, overflowing the chart (source B04/B06
  combined — the source's bar chart shows this rung with an overflow arrow)
- the lesson: the gap is about problem structure, not AI speed — generating
  a candidate is comparatively cheap; deciding it's actually correct is the
  expensive part for hard problems (source B07) — this is the reel's
  carry-out, kept near-verbatim
- next steps: measure your own solve/verify ratio on trivial/medium/hard
  tasks from your own workflow; a growing ratio is the argument for
  deterministic verification gates (source B08) — folded into the carry-out
  and the your-turn handoff rather than narrated as a separate beat

**Compression, per the established hai-simple `behind-the-model` precedent
(e.g. `claude-liam-independent-verification-protocol`):** ten beats — B00
(writer) + B01–B06 (body) + BCRY + BHTF + BOUT — instead of the source's nine
numbered beats plus Your Turn and outro. B01 plants the anchor (the ratio
ladder, raw numbers); B02 states the wrong guess (checking should be as fast
as solving); B03 breaks it with the source's own measured ratios and states
the generate-vs-confirm mechanism; B04 continues the mechanism with the
measurement-artifact fix (the rigor check that proves the gap is real); B05
covers direction A (a big ratio doesn't mean the answer was wrong — it means
confirming costs more, independent of correctness); B06 covers direction B
(a faster model doesn't close the gap, it can widen it) and pays off the
anchor with the corrected ladder plus the proof-sketch overflow rung.

**No inference flag.** Every claim here restates a measured experiment and
its documented correction (a stopwatch comparison and a specific, named
measurement-artifact fix), not an inference about model internals — there is
no leap from evidence to conclusion that needs flagging. Per `simple`'s
ONE-FLAG LAW: "if the source genuinely supports everything, there is no
flag."

**No AI-video, no pantry, no paid step.** Source's CLI/terminal-chrome beats
(`NikBearBrownTerminalAsk`, `NikBearBrownCodeBlock`) are replaced by bespoke
Manim GRAPHIC beats — a general "meeting Claude for the first time" audience
doesn't need literal terminal commands or Python source; the ratio ladder and
its mechanism carry the same teaching point without simulating a dev tool.
GATE L (`./art scenes --check` on `BrutalistHesitantWriter`, `WantQuote`,
`ClaudeComposerAsk`, `OutroCTA`) confirmed all four Remotion patterns
renderable before slating.
