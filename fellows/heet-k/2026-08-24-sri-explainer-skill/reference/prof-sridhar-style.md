# Prof Sridhar's writing style — extracted from `quantum-mechanics-vol1`

Source: `chapters/` (canonical, identical to `generic/`) and `griffiths/`
(the fuller variant that also carries the exercise apparatus), read in full
for Chapter 5 — The Infinite Square Well — and spot-checked against Chapter 1
and others. Nothing here is invented; every rule below was observed directly
in the book's own chapters. Where a rule is a video-narration TRANSLATION of
a prose convention (the book has no video), that is marked explicitly.

## A — Voice (sentence-level; carries directly into narration)

1. **Cold open on a concrete historical or physical scene** — never "In this
   chapter we will…". Ch5 opens on the 1993 IBM quantum-corral STM image;
   Ch1 opens on iron glowing in a forge.
2. The hook connects to the chapter's actual mechanism within 2–3
   paragraphs, ending with a plain statement of what will be derived.
3. **Negation before affirmation.** State what a result is NOT before
   affirming what it IS ("It is not a postulate, not an assumption… It is
   simply…"). *Video translation:* a struck-through wrong reading replaced by
   the right one, on the spoken word.
4. Confident declarative sentences; a short punch-sentence after a longer
   explanatory one for emphasis ("Still no quantization." "The walls did.").
   No hedge words ("basically," "essentially").
5. Collaborative "we" voice, present-tense narration of the derivation as it
   happens ("we ask," "notice," "keep in mind").
6. Concrete physical/sensory comparisons over abstract statement (a guitar
   string, glowing iron, a marble in a box) rather than an abstract claim on
   its own.
7. Numbers are always anchored to something felt — an eV, a room-temperature
   $k_BT \approx 0.025$ eV — never a bare symbol with no scale reference.

## B — Structure (maps directly onto the beat spine in SKILL.md)

8. `##` headers are claims or questions ("The Guitar String Analogy, and Why
   It Breaks Down"), never generic labels ("Background," "Theory").
9. Figures are placeholder-first: an HTML comment
   `<!-- → [FIGURE/IMAGE/TABLE/CHART: description] -->` immediately followed
   by a markdown image and an italic numbered caption ("Figure 5.2 — …").
   *Video translation:* REBUILD LAW governs — a real archival figure (like
   the STM image) becomes a vox beat with a provenance sidecar; a diagram
   figure gets rebuilt natively in Manim/Remotion, never screenshotted.
10. Every chapter closes with a **"What Comes Next"** section — states what
    is solved, what is still open, and which future chapter resolves it.
    Never overclaims. *Video translation:* BRIDGE-HONESTY LAW.

## C — Derivation style

11. Derivations proceed in **bold-led numbered logical beats** ("**Can $E$ be
    negative?**", "**Apply the boundary condition at $x=0$**"), each stating
    explicitly what is NOT yet established ("Still no quantization") so the
    reader can track exactly where the key result enters.
12. Trivial or nonphysical cases are ruled out explicitly before the real
    derivation ($E<0$, $E=0$ excluded) — never silently assumed away.
13. Historical postulate vs. derivation is contrasted by name and date (Bohr
    1913 postulated it; Schrödinger 1926 derived it) — a recurring move used
    to make the derivation's payoff legible.
14. Key results are boxed (`\boxed{}`); inline math `$...$`, display math
    `$$...$$`. *Video translation:* a Manim equation-morph beat lands the
    boxed result at the spoken moment it is derived.

## D — Grounding

15. At least one worked numeric example maps the abstract formula onto a
    real physical scale, and a second, contrasting example (electron vs. a 1
    g marble) establishes quantitatively where the classical limit kicks in
    — never asserted, always computed.

## E — Closing apparatus (per chapter)

16. `## References` — APA-style, each with a parenthetical note on *why*
    it's cited, not just a bibliographic entry.
17. `## Exercises` — four fixed difficulty tiers (Warm-up, Application,
    Synthesis, Challenge; minimum 3 total), each ending with an italic
    **"Tests: …"** line naming the exact skill it checks.
18. `## LLM Exercises` (fuller variant) — questions meant to be worked *with*
    an AI as a thinking partner, framed around checking/critiquing the AI's
    reasoning rather than just getting an answer. **This is the section
    HANDOFF-FROM-THE-CHAPTER LAW draws the Your Turn prompt from.**
19. `## Running Project — Build the 1D Quantum Sandbox` (fuller variant) —
    five fixed R-exercises per chapter:
    - **R1 — When to Use AI** (the judgment + "why AI works here")
    - **R2 — When NOT to Use AI** (the judgment + "why AI fails here" + "the
      tell")
    - **R3 — LLM Exercise** (a copy-paste coding prompt building the actual
      cumulative D3 simulation)
    - **R4 — CLI Exercise** (an agentic coding exercise with a
      hard-asserted golden test — never tune tolerances to force a pass)
    - **R5 — AI Validation Exercise** (a pass/fail/cannot-determine
      checklist plus a mandatory two-sentence AI-use disclosure)

## F — Cross-cutting discipline

20. **Golden-test law.** Every numerical or simulated result needs an
    independent analytic or conservation-law check. The book's own running
    system prompt (`running-project-system-prompt.md`) explicitly forbids
    asserting a result is "physically correct" without one, and forbids
    silently patching a sign or factor-of-2 error — it must be surfaced.
    *Video translation:* GOLDEN-TEST-ON-SCREEN LAW in SKILL.md.
21. **Variant law.** The same chapter is authored once canonically
    (`chapters/` = `generic/`) and then reworded sentence-by-sentence into
    other textbook "voices" (`griffiths/`) — structure, equations, and
    figures stay fixed; only prose is paraphrased. *Not directly applicable
    to video* (a video is one cut, not a multi-voice variant set), noted
    here for completeness since it is a real rule of the source material.

## What this doctrine explicitly does NOT cover

- Book-production mechanics (`architecture.md`, `chapters-spec.md`,
  `risks.md` in `quantum-mechanics-vol1` were all still template stubs
  ("[NEEDS HUMAN INPUT]") at the time this was extracted — they are Tic Toc
  process scaffolding, not writing-style rules, and were excluded).
- Anything specific to physics/QM content — this doctrine is about how
  Sridhar writes a chapter, applicable to any future Sridhar book, not only
  quantum mechanics.
