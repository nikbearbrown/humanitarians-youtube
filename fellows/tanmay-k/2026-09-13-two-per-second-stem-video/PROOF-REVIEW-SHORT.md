# Feedback: "Three Witnesses to Two Per Second" — the Short (9:16)

**Verdict:** clear-for-public. **Trailer rubric 12/12** (explainer rubric 9/12 — see below
for why that number is the wrong question). Production gate **PASS** — scored against the
rendered master *with the platform's own UI overlaid*, not against the bare file.

One line: the Short earns its turn now that the evidence for it is in the cut, and it nearly
shipped with every source hidden behind the YouTube UI.

`two-per-second-short.mp4`, **2160×3840 @ 30 fps, 93.15s (1:33)**, h264 + aac, 7 beats,
A/V skew 21 ms.

*Narration is the parent film's, reused verbatim with the parent's measured audio. No new
words, so the Gate P signature of 09/13/2026 covers this text. Any rewritten line would need
its own read and its own signature.*

---

## The problem — found and fixed

**Every citation in the Short sat at 95% frame depth, inside the band YouTube draws its
title, channel row and progress bar over.** The sources were present in the file and
invisible to the viewer. That is a production-gate failure of the worst kind for this
particular film: it passes every check you can run on disk, and fails the moment it is on
the platform — a source that is technically there and practically absent.

It was caught by sampling every beat with the Shorts UI zones shaded over the frame instead
of reading the frame as if it were a poster. The 16:9 master cannot have this defect;
nothing overlays it.

Fixes:

- `SAFE_BOTTOM = 1600` and `SAFE_RIGHT = 880` are now constants in `scenes.py`, with `cite()`
  asserting its own position against them — so this cannot silently regress.
- Citations moved into the safe band, positioned under the evidence they support rather than
  pinned to the frame edge.
- B16's tail line collided with the serif block once lifted; the block moved up.
- B16's spread strip and B13's plot were pulled in from the action-button column, where the
  `170` and `3` labels were sitting.
- A B00 strap line was **deleted rather than relocated**. It could not fit the safe area
  without crowding the third spectrum, and a line the viewer cannot see is worse than no
  line at all.

## The second problem — the Short asserted what the film demonstrates

The first cut ran B00 → B01 → B10 → B12 → B16. B12 is the turn: the qualifier "in English"
is in the source and gone from the retelling. But **the study that shows the 2 Hz beat is
actually language-dependent was not in the cut.** The Short was making the claim and
omitting the evidence — which is, precisely, the behaviour the film exists to criticise.

`B13` (He, Buder & Bidelman 2024; English vs Mandarin, n = 34) now follows the turn. Runtime
went 76.7s → 93.0s. Worth every second of it: the Short went from asserting to demonstrating.

---

## Production gate — PASS

| Criterion | Result |
|---|---|
| Evidence legible at the moment of assertion | **PASS** — all 7 beats sampled at 55% of their own duration (past every reveal cap); content complete and holding |
| Sources on screen, not just voiced | **PASS** — every claim-bearing beat carries an attributable source **inside the safe area**, landing with the chrome rather than as a reveal step |
| Side-by-side at the moment of comparison | **PASS** — B12 stacks source against retelling, which reads better vertically than it does in 16:9; B13 holds both tracking curves on one axis |

---

## Scoring a trailer — the rubric correction

**The first version of this review scored the Short 9/12 on PROOF's explainer rubric. That
was a category error.** `PROOF.md`'s rubric is headed *"does this explainer actually teach?"*,
and its SPECIAL CASES cover cadence, fact-check formats, first cuts and learners — **there is
no short-form provision anywhere in it.** Scoring a trailer against it penalises the Short
for correctly being a trailer: it lost points for not teaching the three-question framework,
which a trailer that taught the full method would have spoiled.

Length is not the issue. Two of the three deductions were structural artifacts of the format.

The explainer scoring is kept below for comparability, followed by the standard a trailer
should actually be held to.

### Against the explainer rubric — 9/12 (recorded, not the operative score)

| Criterion | Score | Why |
|---|:--:|---|
| Explicit framework | **1** | B02 is not in the cut, so the three questions are never shown. The Short has a clear shape; it does not teach a framework |
| Reusable rubric | **1** | B16 hands over one transferable move — go to the original and look for the qualifier — but not the three axes |
| Worked example | **2** | B10 → B12 → B13 walks the speech case end to end |
| Falsifiability / edge case | **2** | B13 tests the film's own claim against Mandarin listeners, and B14's caveats are summarised in its closing line |
| Active task | **2** | B16 asks for a measurement the viewer produces |
| Friction | **1** | The `gap` box poses the question visually, but the narration answers it in the same breath. B11's silent hold — the parent's best moment — is not in this cut |

### Against a trailer standard — 12/12 after the end-card fix (operative)

A Short's job is not to teach the method; it is to carry one idea honestly and send the
viewer to the film. PROOF's non-negotiables still apply in full — no fabrication, show over
say, sources on screen — because those are about honesty, not format.

| Criterion | Score | Why |
|---|:--:|---|
| **Stands alone** | **2** | Beats were chosen so nothing dangles. B11 was excluded *because* it opens "Question three," which means nothing without B02 |
| **One idea, not a summary** | **2** | The qualifier that falls off. It does not try to compress three witnesses into 90 seconds |
| **Sourced on screen** | **2** | Every claim carries an attributable source, inside the safe area, landing with the chrome |
| **Demonstrates rather than asserts** | **2** | Only after B13 was added. The first cut made the turn and omitted the evidence for it — the exact failure the film criticises |
| **Leaves something for the film** | **2** | The framework, the locomotion witness, B07's chain-of-custody admission and the silent hold are all film-only |
| **Points at the film** | **1 → 2** | **It did not.** See below |

**The defect the wrong rubric was hiding.** Scored as an explainer, the Short's weakest axis
looked like "friction". Scored as a trailer, the real defect was obvious and much worse:
**the end card never told the viewer a film existed.** It carried the title, the presenter
and the channel handle, and stopped — ending as though it were the whole artifact. For a
trailer that is a failure of its primary job, and the teaching rubric had no criterion that
could see it.

Fixed: the end card now reads *"the full film — 4:52 / the other two witnesses, and the
silence"*. The second line names what is missing rather than just asserting there is more,
which is the same move the film makes about qualifiers.

**Friction remains the honest gap under either rubric.** B11's two-second silence is the
parent's best moment and is not in this cut, for the dangling-reference reason above. Left
deliberately — but it is the one thing that would make the Short better rather than just
longer.

---

## What works

- **Vertical suits the turn.** Two stacked cards — research above, retelling below — reads
  more naturally at 9:16 than the same comparison does in widescreen.
- **The sources now sit under their evidence** rather than at the frame edge, which is both
  safer and better composition than the 16:9 convention it inherited.
- **Nothing was re-narrated to make the Short work.** Every word was already read aloud and
  signed; the cut is an edit, not a rewrite.

---

## Review 2 — B11 added

**Friction was the one honest gap under either rubric, and it is now closed.** B11 is in the
cut, between the nested rhythm and the turn: two sentences side by side, no highlight, no
arrow, and then the frame goes quiet while the viewer looks for the difference.

**The dangling reference was solved by trimming, not rewriting.** B11 opens "Question three.
What qualifier sits in the original," which is meaningless without B02. Rather than
regenerate the line — which would put unsigned words in a signed film — the parent's audio
was cut at a **detected pause at 2.70s**, removing those two sentences. Every word heard is
the signed take; only the head is gone. The trim is recorded in the beat's `edit_note`.

The Short also carried the same stage-direction leak as the parent (`— hold —`,
`the film's only silence`) and has been cleaned the same way.

Runtime 93.0s → **109.25s (1:49)**. Order: B00 → B01 → B10 → **B11** → B12 → B13 → B16 → END.

### Trailer rubric — now 12/12

| Criterion | Score |
|---|:--:|
| Stands alone | 2 |
| One idea, not a summary | 2 |
| Sourced on screen | 2 |
| Demonstrates rather than asserts | 2 |
| Leaves something for the film | 2 |
| Points at the film | 2 |
| **Friction** — the viewer is asked to do the work before the reveal | **now present** |

The Short no longer trades friction for standalone coherence; the trim bought both.


---

## Review 3 — after the lossless audio rebuild

Recompiled on `compile_lossless.py` for the same reason as the parent film.

| Check | Before | After |
|---|---|---|
| AAC generations | 2 | **1** |
| Crest factor | 4.44 | **4.87** |
| Integrated loudness | −14.7 LUFS | −16.1 LUFS |
| True peak | −1.4 dBFS | −1.93 dBFS |
| Runtime | 1:49.3 | 1:48.5 |

**Two things the rebuild caught in this cut.** First, the B11 hold measured **2.62s** against
a two-second design, for the same reason as the parent — the beat's own audio ends with 0.64s
of silence. Added silence is now 1.36s and the measured hold is **1.98s**.

Second, and this was a regression I introduced: the first lossless `build_short.py` **ignored
`trailing_silence_s` entirely**, which silently truncated that hold and shortened the cut by
2.15s. Compiling is now `compile_lossless.py`'s job for both aspect ratios — it pins every
segment to `actual_duration_s + trailing_silence_s` — and `build_short.py` renders clips
only, with a comment saying why.

Captions regenerated: 37 cues, last at 104.46s with a 4.00s tail for the silent end card.

**Verdict unchanged: clear-for-public, trailer rubric 12/12, production gate PASS.**
