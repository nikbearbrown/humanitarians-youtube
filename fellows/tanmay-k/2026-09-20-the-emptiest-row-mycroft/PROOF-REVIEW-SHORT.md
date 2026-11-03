# PROOF-REVIEW — *The Emptiest Row* (Short / trailer)

Per `[[run-proof-gate-every-iteration]]`: run before Gate P, not after — nothing is
signed yet, so anything found here can still be fixed without reopening a human
sign-off. Nothing is rendered as clips or audio yet; this is a script/beat-sheet-stage
review, against the planned narration and the 5 slate stills already rendered in
`manim/*.png`.

Scored against the **Trailer Gate** (the topic video's own Short standard), not the
long-form's 6-criterion pedagogy rubric — a trailer isn't teaching a complete method, so
"reusable rubric" / "active task" would be a category error here. Swapped
"self-contained interactivity" for "self-contained coherence," since this Short has no
guess-along moment — its actual design risk, named directly by Tanmay, is whether the
five beats read as one argument or four ideas in a trenchcoat.

---

## Continuity check — read as one continuous script, not beat by beat

Full narration, SB01→SB05, read straight through with no beat breaks:

> Hi, I'm Tanmay Kulkarni, in for Humanitarians AI. One company discloses four of its
> own AI systems, and every write-up treats that as one company doing AI. I wanted to
> know what happens if you refuse to average them, and score each one on the same two
> axes instead: is the mechanism disclosed, and does a human check the answer before a
> customer hears it. Lay four systems out that way and a pattern falls out fast.
> Athena: rich disclosure, and a human reviews every answer anyway. The HR tool and the
> complaints tool: thin, but internal, nobody outside needs to see them. And the one
> system that actually talks to customers directly: undisclosed mechanism, undisclosed
> outcome, nobody checking first. Same company. That's not an accident. So that's
> exactly the system I built a tested pipeline around, because that's where an
> undisclosed boundary actually does damage, instead of just sitting there as a
> caveat. The build passed every test on the first run, twenty-nine for twenty-nine.
> Then I attacked it on purpose with malformed input, and found the one failure that
> matters most: a bad date silently came back as no transaction found, for a
> transaction that was actually there. Not a crash. A confident, wrong answer, exactly
> the risk that empty row predicted. Fixed, named precisely, and re-tested: forty-nine
> for forty-nine, checked again independently just for this cut. That's one row, one
> bug, caught on purpose. The other three systems, the full pipeline, and the fix in
> full, all in The Emptiest Row. Tanmay Kulkarni, in for Humanitarians AI.

**Every transition checked for a named connector, not just adjacency:**
- SB01→SB02: "score each one on the same two axes" → "lay four systems out **that
  way**" — explicit backreference. Connected.
- SB02→SB03: "that's not an accident" → "**so** that's exactly the system I built..." —
  explicit causal connector. Connected.
- SB03→SB04: "does damage" → ~~"the build passed every test"~~ **"that pipeline passed
  every test"** — fixed. "The build" was a generic noun with no lexical tie back;
  "that pipeline" echoes SB03's exact word ("a tested pipeline"), matching the pattern
  every other transition already uses (an exact or near-exact noun echo, not a bare
  pronoun). See below.
- SB04→SB05: "checked again independently just for this cut" → "that's one row, one
  bug, caught on purpose" — explicit summary connector, ties back to both SB02 ("row")
  and SB04 ("bug"). Connected.

**One real finding, found and fixed before the read, not smoothed over silently:** the
SB03→SB04 seam was the weakest of the four — "the build" depended on the listener
holding "a tested pipeline" from one sentence earlier with no lexical match. Fixed by
swapping to "that pipeline," a two-word change with no new sourcing, no length change,
and no visual change needed. Named here, and in `READ-ALOUD.md`, so the fix is visible
as a fix rather than presented as if the seam was never there.

---

## Trailer Gate

| Criterion | Result |
|---|---|
| Hook lands in the first beat | **PASS** — name in the first sentence, premise ("refuse to average them") stated by the second |
| Every claim traces to FACTCHECK | **PASS** — every figure and claim (59s→20s lineage facts folded into "rich disclosure," the 29/29 and 49/49 counts, the malformed-date finding) is carried from the long's already-verified narration, not restated from scratch. SB02's "nobody outside needs to see them" reasoning is not a new inference — it's the long's own B06 line, reused |
| Self-contained coherence | **PASS, with one flagged seam** — see continuity check above. Four of five transitions have an explicit connector; one relies on a one-beat-old antecedent |
| Honest about what's withheld | **PASS** — SB05 names specifically what's not shown ("the other three systems, the full pipeline, and the fix in full") rather than a vague "watch for more" |
| Clear, accurate CTA | **PASS** — names the long's actual title, doesn't overclaim what the Short itself proved |
| Brand/technical consistency | **PASS** — name in first sentence and outro, `@HumanitariansAI` handle present, no black backgrounds, no leaked demo content across all 5 slates |

### Production gate (planned content, not rendered clips)

- **Evidence legible at assertion** — checked per beat: SB02's stacked matrix names all
  four systems as they're spoken; SB03's pipeline appears as "built a tested pipeline"
  is said; SB04's docstring is on screen for the exact claim it supports. No gaps found.
- **Sources on screen** — SB04 cites `intake.py` directly. SB01/SB02/SB03/SB05 make no
  claim that needs a citation beyond what the long-form's own sourced beats already
  cover (this is a trailer restating already-cited claims, not introducing new ones).
- **Side-by-side at comparison** — not applicable; this Short has no "X says A, reality
  is B" moment (that pattern lives in the long's B12, reused here as narration only,
  same no-before/after treatment per direct instruction).

**PASS**, pending the human read's answer to the one flagged seam.

---

## Were the other three transitions checked for the same gap, not just for "a connector"?

Asked directly after the SB03→SB04 fix, since a connector existing isn't the same as
the antecedent being *unambiguous*. Re-checked each for what kind of link it actually
is, not just whether one exists:

| Transition | Link | Kind |
|---|---|---|
| SB01→SB02 | "score...on the same two axes" → "lay four systems out **that way**" | demonstrative pointing at the immediately preceding clause — tight, one clause back |
| SB02→SB03 | "the one system that actually talks to customers directly" → "that's exactly **the system**" | exact noun echo ("the system"), two sentences back but unambiguous — only one "system" has been singled out in the whole Short |
| SB03→SB04 (fixed) | "a tested **pipeline**" → "**that pipeline**" | exact noun echo, adjacent sentence |
| SB04→SB05 | "**one row**, **one bug**" | exact noun echoes of both SB02's "row" and SB04's "bug" in the same sentence |

All four now use either an exact noun echo or a tight demonstrative — the same pattern,
not four different strategies. SB03→SB04 was the one transition that broke that
pattern (a bare, generic "the build" instead of an echo), which is what the mechanical
check caught. Nothing else in the script uses a same-shaped gap.

## Verdict — Review 1 (script stage)

**Cleared to proceed to Gate P.** One real seam named, not hidden; nothing else found.
Rubric and production gate both PASS at the script stage. Frame-level PROOF review still
required once clips and audio exist, same as every prior beat of this project.

---

## Review 2 — full pass on the actual delivered master

Gate P signed (`PEDAGOGY.md`, PASS, 2026-09-21, including the SB03→SB04 fix). Audio
generated (Kokoro, `am_onyx`, $0.00, 5/5 beats), clips rendered, compiled to
`the-emptiest-row-short.mp4`.

### Per-beat sample check (25% mark, all 5, on the actual final file)

| Beat | Sample (25%) | On screen matches spoken claim? |
|---|---:|---|
| SB01 | 4.94s | **PASS** — title card fully legible, presenter name visible |
| SB02 | 24.98s | **PASS** — full four-row matrix already on screen (reveal completes well inside this beat's own motion budget) |
| SB03 | 43.15s | **PASS at steady state** — sampled at 25% mid-reveal (only the first arrow drawn, expected for a build-in beat this short); re-checked near the beat's end (49.0s) and the full three-stage pipeline is complete well before the beat closes |
| SB04 | 56.51s | **PASS** — corrected docstring, highlight line, and 49/49 card all present |
| SB05 | 76.98s | **PASS** — title reveal, presenter name, handle |

**5/5 pass.** SB03's 25%-mark snapshot mid-animation is noted rather than silently
skipped — it reflects the beat's own build-in pacing (a pipeline assembling while its
sentence is spoken), not a legibility gap; the completed diagram is on screen for most
of the beat's remaining runtime.

### Continuity, re-checked on the actual audio (not just the text)

The SB03→SB04 fix ("that pipeline") was signed off as part of the full read-aloud
pass, not re-litigated here. Listened through the compiled file beat-to-beat: no new
seam introduced by Kokoro's phrasing or pacing.

### Technical sweep, independently verified

| Check | Result |
|---|---|
| Resolution / frame rate / codec | 2160×3840 @ 30fps, h264/aac |
| Duration | 84.89s (1:24.9) — well under the 180s Shorts cap |
| Black frames | zero, full scan |
| Loudness | −24.63 LUFS / −2.96 dBTP, on target, matching the long |
| Crest factor | 11.38 (source mp3s ~10.4) |
| Silence gaps | only natural sentence-boundary pauses (0.4–0.7s), at beat transitions — no dead air mid-beat |

### Verdict

**PASS.** All 5 beats confirmed on the actual delivered file, production gate clear,
technically clean, well under the Shorts cap.

---

## Review 3 — Trailer Gate, final numeric score

Same standard the topic video's own Short was held to: scored on what a trailer is
actually for, not the long-form's pedagogy rubric ("reusable rubric" / "active task"
would be a category error for a film that isn't teaching a complete method).

| Criterion | Score | Why |
|---|---:|---|
| Hook | **2/2** | Name and premise both land in SB01's first two sentences — no delayed reveal |
| Accuracy / no overclaim | **2/2** | Every figure (29/29, the malformed-date finding, 49/49) traces to the long's already-verified `FACTCHECK.md` rows. "Checked again independently just for this cut" is honest about scope — a re-verification, not a new claim |
| Self-contained coherence | **2/2** | The specific thing this Short was rebuilt to fix. All four beat transitions confirmed to use an exact noun echo or a tight demonstrative (Review 1's table) — one real gap (SB03→SB04) was found and fixed before Gate P, not smoothed over. Score reflects the corrected state, disclosed as corrected, same honesty standard as every other criterion here |
| Honest incompleteness | **2/2** | SB05 names specifically what's withheld (the other three systems, the full pipeline, the fix in full) rather than a vague "watch for more" |
| Clear, accurate CTA | **2/2** | Names the long's actual title; doesn't claim the Short itself proved anything the long didn't already establish |
| Brand / technical consistency | **2/2** | Name in first sentence and outro, `@HumanitariansAI` handle present, zero black frames, correct 2160×3840 portrait dimensions, no leaked demo content across all 5 beats. **Scope note:** this Short did not run through `runtime/qc/final_frame_check.py` (Gate V), for the same documented reason the long didn't — that check is calibrated for full-bleed Remotion cards, not this sub-series' spacious Manim style. Not scored down for a check this style of film has never been held to |

**12/12 on the Short's own rubric** — not the same 12 points as the long's production
gate, earned the same way: checked against the actual final file, with the one real
defect this process found (the continuity seam) disclosed and fixed rather than
smoothed over.
