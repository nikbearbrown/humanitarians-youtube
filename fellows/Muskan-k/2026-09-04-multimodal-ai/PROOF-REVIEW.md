# Feedback: "Multimodal AI." — Muskan (@HumanitariansAI), film 1

**Verdict:** clear-for-public. **Teaching 10/12.** Production gate **PASS.**
One line: *This film attempts to teach "what makes an AI multimodal" and largely
delivers a reusable test — because it puts the definition on screen before any
example and stress-tests it with a real counter-case — but its worked example is
a scripted illustration rather than a live artifact, which caps its friction.*

## Rubric — does this explainer actually teach?

| Criterion | What it means | This cut |
|---|---|---|
| **Explicit framework** | organizing idea shown as structure *before* examples | **2** — B01 "One Model, Many Senses" defines multimodal (one model · connects · text/image/audio/video) as a diagram at ~18s, ahead of every example. |
| **Reusable rubric** | a viewer could apply the axes to a new case | **2** — B01 + the B06 one-pager give a testable definition and the "did it see/hear it, or read a transcript?" test — applicable to any tool. |
| **Worked example** | one case walked through the framework live — the reasoning step | **1** — B03 walks image+text → model → "Step 3 feeds Step 2, arrow backwards," showing cross-modal reasoning. But the answer is *asserted on a card*, not produced by a real run; it teaches the shape, not a live artifact. |
| **Falsifiability / edge case** | framework stress-tested against a counterexample | **2** — B04 contrasts a bolt-on OCR pipeline (model never saw the image) with true multimodal, side-by-side. Exactly the case the naive definition misses. |
| **Active task** | CTA requires structured *doing*, not "ask Claude" | **2** — B07 hands over a scaffold: take a mixed-format item, ask the model to connect it, then *check* whether it used the image/audio. Explicitly "not just go ask Claude." |
| **Friction** | viewer must resolve a tension, not just receive facts | **1** — "connected or converted?" is a real tension, but the reel resolves it for the viewer; the genuine friction is deferred to the handoff check rather than forced on screen. |

**Total: 10 / 12** (ship bar is 8).

## Production gate (binary — can veto publish)

- **Evidence legible at the moment of assertion** — **PASS.** Body beats are held
  4K cards; the definition, the four asks, the worked answer, and the bolt-on/true
  split are all on screen, legibly, when the narration names them.
- **Sources on screen, not just voiced** — **PASS (n/a-heavy).** This is a
  definitional explainer, not a fact-check; it makes no external statistical or
  product claims that would need a citation, and it names no model/version that
  could date it. The "evidence" it owes is the definition itself — shown.
- **Side-by-side at the moment of comparison** — **PASS.** B04 shows bolt-on vs
  true multimodal together, held for the full beat, at the moment the narration
  draws the contrast.

Gate: **PASS.** The film passes its own standard — it shows what it asserts.

## The problem (single biggest fix)
**B03, the worked example, is illustrative, not a real artifact.** The card asserts
the model's answer ("the arrow points the wrong way") rather than showing a real
multimodal model producing it about a real image. That's what holds worked-example
and friction at 1 instead of 2.

## Do X next
1. **[RESHOOT / NEW SOURCE]** Replace B03's asserted answer with a real captured
   run: a genuine image handed to a multimodal model, its actual answer about the
   picture shown as the artifact. Moves worked-example → 2 and friction → 2 (12/12).
   *Note:* under this toolkit's REBUILD LAW / free-only pipeline a native
   illustration is the sanctioned default, so this is an optional upgrade, not a
   blocker — the current cut ships.
2. **[EDIT]** Optional friction bump without a reshoot: at B04, hold a beat on the
   question ("so — did it see it, or read a transcript?") before revealing which
   side is which, so the viewer commits before the answer lands (a PredictCard-style
   move).
3. **[EDIT]** B05 and the portrait B04 carry some upper-frame negative space; if you
   want tighter CANVAS-FILL, raise the diagram block ~4–6% of frame height.

## What works (keep)
- **Framework-first discipline.** The definition lands before any example — the
  single move most explainers skip. Keep it.
- **The falsifiability beat (B04).** The bolt-on/true contrast is the memorable,
  reusable idea and it's shown, not just said.
- **The scaffolded handoff (B07)** with a built-in check ("did it use the image?")
  — a real viewer task, not a vague pointer.
- **House fidelity.** Cream/ink/terracotta, EB Garamond, one accent per beat,
  legible 4K cards, brand chip present throughout.
