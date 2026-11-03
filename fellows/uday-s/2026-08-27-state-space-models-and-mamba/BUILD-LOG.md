# BUILD-LOG — state-space-models-and-mamba

Skill: `ai-explainer` on the **`claude-hai`** channel.
Deliverable: `StateSpaceModelsAndMamba_UdaySonawane_2026-08-27.mp4`
Built 2026-08-27.

## Channel: the doctrine already had one for this

The previous weekly reel overrode the chassis defaults by hand (@HumanitariansAI
with an am_onyx voice, logged as a deliberate deviation). That was unnecessary —
`skills/make/ai-explainer/SKILL.md` defines a `claude-hai` channel key that is
exactly this configuration:

```
claude-hai   persona HAI   chip @HumanitariansAI   kokoro am_onyx   Pragmatist
audience: STUDENTS — smart people getting started with AI
spine question: when to use it, and when NOT to
```

So this reel sets `brand_key: claude-hai` and inherits it, rather than
overriding anything. No outro lock is broken: `@HumanitariansAI` is this
channel's own chip. The greeting uses the HAI word budget (shortest forms only —
`Hej, HAI`), and never spells out the handle in the greeting slot, per the law.

The channel's spine question drove B09: the verdict beat names when NOT to use
an SSM, which is the HAI register rather than a generic recap.

## Sourcing — the part that took the longest

This reel makes claims about other people's research, so the DOUBLE-CHECK LAW
and PROOF's "no source, no verdict" both bind harder than on a work report.
Nothing was narrated from memory. Three papers were checked against their own
abstracts before any narration was written:

- S4 — Gu, Goel & Ré 2021, arXiv:2111.00396
- Mamba — Gu & Dao 2023, arXiv:2312.00752
- Copying limits — Jelassi et al. 2024, arXiv:2402.01032

Two claims were **weakened** after checking (see FACTCHECK.md): "non-trivial
result on Path-X" rather than "solved Path-X", and "streaming" marked as my
inference rather than a paper claim. One claim — the 5× throughput — is
attributed on screen rather than asserted, because nothing was benchmarked here.

Four beats carry a visible arXiv citation. PROOF's rule is that a video holding
others to "no source, no verdict" must show its own sources or it is
self-refuting, so the citations are on screen at the moment of the claim, not
in a credits card at the end.

## The framework beat, and why it predicts rather than describes

PROOF's hardest criterion is an explicit framework shown before the examples,
and its pushback is specifically against frameworks reverse-engineered to fit
the cases already chosen — the tell being categories that map one-per-example.

The three axes here (STATE / UPDATE / COST) avoid that because they were chosen
to **forecast a failure**, and then did: axis 1 says the state is fixed size,
and the falsifiability beat is the proven consequence of exactly that — an SSM
cannot copy arbitrary strings unless its state grows with the sequence. The
framework is load-bearing; remove it and B08 becomes an unmotivated caveat.

Timing: B00 (5.29s) + B01 (17.69s) = **22.98s**, so the framework graphic opens
at 22.98s. PROOF asks for "the first ~20s". This is 3s over — reported rather
than rounded down. It is still ahead of every example, which is the substance
of the gate.

## Constraints carried from the toolkit environment

- **No LaTeX.** `dvisvgm` is absent, so `MathTex`/`Tex` would fail. The SSM
  equations in B04 are set as plain `Text`, which is why they read
  `h'(t) = A h(t) + B x(t)` in mono rather than as typeset math.
- **Fonts registered at runtime** via `manimpango.register_font()` — the
  toolkit's installer copies EB Garamond to a Linux path Windows ignores.
- **B01 built around a centred origin.** The static checker reads coordinates as
  authored, before `fit()` re-centres them, so axes drawn from `[0,0,0]` outward
  tripped a safe-area warning. Building around a centred origin fixed it
  properly rather than suppressing the check.

## Audio-first

```
B00  5.29   B01 17.69   B02 17.88   B03 21.29
B04 19.61   B05 22.21   B06 22.10   B07 20.78
B08 27.11   B09 18.39   B10 18.99   B11  3.97
                                    total 215.31s (3:35)
```

All nine Manim scenes passed GATE A (static) and GATE W (contrast/margins/
overlap) before render.

## Gate record (final)

**GATE A** (static pre-flight) — clean on all nine scenes. One fix: `B01` drew
its axes from `[0,0,0]` outward, and the checker reads coordinates as authored
rather than after `fit()` re-centres them, so it flagged a safe-area breach.
Rebuilt around a centred origin rather than suppressing the check.

**GATE W** (WCAG contrast / margins / overlap) — clean on all nine, first pass.

**GATE B** (post-render, pixel-true) — **0 errors, 0 warnings** on the final
pass. Three defects were caught and fixed at source along the way:

| Beat | What GATE B saw | Root cause | Fix |
|---|---|---|---|
| B07 | `label on a curve/line` ×3 | card width hard-coded narrower than its own body text, so the text sat across the border stroke | boxes sized to content; 4 claims moved to a 2×2 grid; the same guard added to the shared `card()` helper |
| B07, B08 | citation colliding with the body | `source_line()` occupies the strip the body was already using | added `fit_src()`, a shorter band for beats that carry a citation; B08's verdict composed *into* the fitted group instead of positioned after it |
| B06 | `label on a curve/line` | my first "forget" fix struck through the label — literally a line across text | struck the **link** instead of the label: a cross on the connection reads as "does not propagate", crosses no text, and keeps terracotta reserved for "propagate" |

The B06 sequence is worth recording: the *first* version of that beat passed
every gate while being pedagogically wrong — "forget" was labelled above a block
that looked identical to its neighbours, so the visual never demonstrated the
claim. No automated gate catches that. It was found by looking at the frame,
which is why the VISUAL QC LAW requires looking.

**GATE V** (frame-level, compiled cut):

```
clean cut   431 frames   BLOCKER 0   MAJOR 64  (60 underfill · 4 low-contrast)
```

The headline "24 BLOCKER" printed by `./art run` is GATE V reading
`*-slate.mp4` — the REVIEW cut, whose timecode burn-in sits outside title-safe
by construction. Against the clean cut there are no blockers.

The 4 `low-contrast` flags each co-occur with a 10–11% fill reading: they are
near-blank frames at beat openings with too little ink to measure a luminance
separation, not content that is hard to read. The 60 `underfill` frames
(~14% of samples) are staggered reveals still filling the canvas, plus the
deliberately sparse outro card. Accepted and documented rather than silenced
with `ART_STRICT=0`; see PROOF-REVIEW.md.

## Deliverable

```
StateSpaceModelsAndMamba_UdaySonawane_2026-08-27.mp4   1920x1080   215.31s
```

Copied from the clean cut (`state-space-models-and-mamba.mp4`, no review
markers). The 4K master needs no re-render — Manim rendered at 2160p24 and
Remotion at `--scale=2` — so `./art final <reel>` produces it from the same
slots whenever it is wanted.
