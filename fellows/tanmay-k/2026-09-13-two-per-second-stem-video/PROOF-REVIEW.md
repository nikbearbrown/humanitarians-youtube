# Feedback: "Three Witnesses to Two Per Second" — Tanmay Kulkarni, Week 22 topic-video

**Verdict:** clear-for-public. **Teaching 12/12.** Production gate **PASS** — scored against
the rendered 4K master, not against intentions.

One line: the film argues that retellings quietly drop what the source said, and it now
survives being held to that rule itself — including one place where its own documents
claimed more than the build delivered.

**Review 5 — first review with a master.** `two-per-second.mp4`, 3840×2160 @ 30 fps,
292.22s (4:52), h264 + aac, 17 of 17 beats filled, Gate P signed 09/13/2026.

*A cleared review is not permission to publish. Upload goes through the channel ledger and
the publishing gate, which are separate.*

---

## Review history

| | Found | Result |
|---|---|---|
| **1** | Promised symmetry, delivered asymmetry; verdict rounded a scope-correction into a retraction | 10/12, gate unscored |
| **2** | Both fixed; the first fix opened a selection-logic gap | 11/12, gate unscored |
| **3** | Gap closed; previz QC found 3 layout defects | 12/12, gate unscored |
| **4** | Source-coverage and frame-vs-plan audits — 4 defects; corner card did not exist | 12/12, gate unscored |
| **5** | **Motion broke the gate and was fixed** — see below | 12/12, **gate PASS** |

---

## Production gate — PASS

Scored by sampling every beat of the master against the narration clock, not by reading the
beat sheet.

| Criterion | Result |
|---|---|
| Evidence legible at the moment of assertion | **PASS** — all 17 beats sampled at 25% of their own duration; content is complete at that point and holds for the remaining 75% |
| Sources on screen, not just voiced | **PASS** — all 15 claim-bearing beats carry an attributable source, and citations now land **with the chrome**, so the source precedes the claim rather than trailing it |
| Side-by-side at the moment of comparison | **PASS** — B04 (Moelants vs Hine), B07 (2005 vs 1964), B11/B12 (source vs retelling), B13 (English vs Mandarin) each hold both terms together well beyond 2s |

### The gate failed first, and the failure was mine

The first motion render **failed criterion one outright**. Sampling B04 at 8.6 seconds — with
the narration already saying *"Moelants put preferred tapping between a hundred and twenty
and a hundred and thirty"* — the frame had no mean callout, no arrow, and **neither source
line on screen**. The claim was spoken; the evidence arrived later.

Cause: the 23 scatter dots were each being revealed as a separate step, so they ate the
entire reveal budget (9.5s of a 19s beat) and pushed the sources to the end. Worse and more
systemic: `cite()` ran through the same reveal machinery, which meant **every citation in
the film was the last thing to appear on its beat**. In a film about sources dropping out of
retellings, the sources were arriving after the claims.

Three fixes:

1. `cite()` and `footer()` now bypass the reveal machinery entirely and land with the chrome.
2. Reveal is capped in absolute seconds (1–5s by motion type), not just as a fraction, so
   content completes early regardless of step count.
3. The scatter is one reveal step, so it reads as a population rather than a queue.

**This class of defect was invisible at every earlier stage.** Slates have no time axis, so
reviews 1–4 could not have caught it; it only exists once motion and audio share a clock.
That is the argument for scoring the gate against a master and nothing else.

---

## Rubric — 12/12

| Criterion | This cut |
|---|---|
| **Explicit framework** | **2** — three questions built on screen at B02, each paired with its selection trigger, and the corner card carries the active question through B03–B15 |
| **Reusable rubric** | **2** — round number → Q1, surprising result → Q2, travelled far → Q3; handed over at B16 |
| **Worked example** | **2** — three cases, reasoning shown, not just conclusions |
| **Falsifiability / edge case** | **2** — B13 tests the film's own central claim; B08 and B14 carry the counterweights the popular version omits |
| **Active task** | **2** — B16 produces a number the viewer measures, and shows the spread it lands in |
| **Friction** | **2** — B11 holds two seconds of real silence in the master, timed, with no motion under it |

---

## Held to its own standard

The film's rule is *go to the original sentence and look for the qualifier*. Applied to itself:

- **It passes on facts.** 15 claims, every one traceable to a `FACTCHECK.md` row read to
  primary. Three candidate claims were killed during verification — one misattribution caught
  only by reading the paper, one untraceable, one overstated — and none quietly survived.
- **It passes on provenance.** B07 says out loud that its 1964 figure is cited through the
  2005 paper rather than read first-hand.
- **It has one blemish, disclosed.** Two `legibility` notes promised motion the build
  delivered differently — B15's "2 Hz rule redrawn" became a verdict tag, B16's "scatter
  returns" became a spread strip. I amended the notes to match the frames rather than
  building to the notes. That is the film's own failure mode in miniature: a document
  claiming slightly more than the thing it describes. It is recorded here and in
  `PREVIZ-QC.md` rather than smoothed over, and both substitutions are defensible on their
  merits — but the honest framing is that the promise moved, not that the build met it.

---

## Do this next

1. **[SHORT]** 9:16 cut at 2160×3840. B11–B12 is the obvious spine.
2. **[PUBLISH]** Channel ledger and publishing gate — separate from this review.
3. **[EDIT, optional]** Friction is still concentrated in B11. B04 and B08 raise tensions and
   resolve them in the same breath.

---

## What works

- **B11–B12 earns the film.** The two-second silence is real in the master, and "in English"
  is genuinely in the source and genuinely absent from the retelling.
- **The holds are doing the work, not the motion.** Reveals finish in the first few seconds
  and then the frame sits still. That is what made the gate pass, and it is worth protecting
  against the instinct to animate more.
- **B07 volunteers its own weakness** rather than hiding its chain of custody.
- **B09 and B14 quote the authors' hedges** — "speculate", the single EEG channel, n = 34.
- **The fact base survived primary sources.** Three claims died there. That is the part of
  this week that would have been easiest to fake, and wasn't.

---

## Re-review alongside the Short — 16:9 master re-checked

Run when the Short was reviewed, so both masters were held to the same standard on the same
day. The 16:9 master is unchanged since the gate passed; these are checks that had not been
run on it before.

| Check | Result |
|---|---|
| A/V skew | **5 ms** (video 292.20s, audio 292.19s) — far below the ~40 ms perceptible threshold |
| Frame integrity | 8,766 frames @ 30/1, 3840×2160, constant rate |
| Title-safe margins | body content inset 96 px of 1920 = **5.0%**, exactly the 16:9 title-safe line; nothing sits outside it |
| Platform occlusion | **not applicable** — unlike the Short, nothing is drawn over a 16:9 player by default |

**One thing the Short's review exposed that this one had not considered.** The Short nearly
shipped with every citation hidden behind the YouTube UI — a source present in the file and
invisible on the platform. That failure mode does not exist here, but it is worth recording
why: the gate question is not "is the source in the frame" but "can the viewer see it where
this will actually be watched." For 16:9 those are the same question. For 9:16 they are not,
and reviewing the file alone would have passed a film whose sourcing the audience never sees.

Audio is mono (Kokoro output), 48 kHz — expected, and handled by the platform.

**Verdict unchanged: clear-for-public, teaching 12/12, production gate PASS.**

---

## Review 6 — B11 added to the Short, and a defect it exposed in both masters

**Stage directions were being rendered into the shipped frames.** Notes written to instruct
the build were drawn for the audience to read:

| Beat | Text on screen | Status |
|---|---|---|
| B11 | `— 2 s silent hold —` and `no highlight, no arrow, no motion` | removed — the silence is performed, not captioned |
| B00 | `no logo in this beat` | removed |
| B02 | `corner reference for the rest of the film` | removed |
| B04 | `both on screen together at the moment of comparison` — occupying the **citation slot** | removed; the two real source lines were already on the frame |
| B10 | `…shown as ranges, not a point` | trimmed to the viewer-facing half |
| B13 | `both curves drawn simultaneously, not one after the other` | replaced with `same speech, same stress rates, two listener groups` |
| B07 | `the film says so out loud` | replaced with `cited through the 2005 paper, not read first-hand` |

Seven leaks across the film. They passed four reviews because every earlier pass asked
whether the evidence was legible and sourced — never whether the text on screen was *meant
for the viewer at all*. A caption that describes the frame to its own builder is not evidence;
it is a note that escaped.

B04's is the worst of them: a production note sitting in the citation slot, where a source
belongs, on the beat that carries the film's spread claim.

Both masters re-rendered and recompiled. 16:9 is unchanged in duration (292.22s); the Short
is now 109.25s.

**Verdict unchanged: clear-for-public, teaching 12/12, production gate PASS.** The removals
take text off the screen; nothing sourced or asserted changed.

---

## Review 7 — after the lossless audio rebuild

The master was recompiled on a new chain (`compile_lossless.py`) because Tanmay heard the
work Short breaking up. That turned out to be four generations of lossy audio, and this film
had two. Re-reviewed because the rebuild touched both audio and timing.

| Check | Before | After |
|---|---|---|
| AAC generations | 2 | **1** |
| Crest factor | 4.36 | **4.83** (source mp3s ~10.4) |
| A/V skew | 18 ms | **0 ms** — both streams 291.300000s, both starting at 0 |
| Integrated loudness | −14.8 LUFS | −16.2 LUFS |
| True peak | −1.4 dBFS | −1.9 dBFS |
| Runtime | 4:52.2 | 4:51.3 |

**The B11 hold was wrong and is now right.** `silencedetect` measured 2.59s of dead air at
200.7s against a design of two seconds — because B11's own audio ends with 0.64s of silence
and I had added 2.0s on top of it. The added silence is now **1.36s**, and the measured hold
is **1.98s**.

That matters for the rubric rather than just for polish: Friction scores 2 on the strength of
that hold, and the Gate P sheet told Tanmay to *"stop. Two seconds of silence, timed."* He
timed two seconds and signed it; the film was giving 2.6. The beat now delivers what was read
and approved. **The beat sheet records that `trailing_silence_s` means ADDED silence, with
the natural tail spelled out, so it is not "corrected" back later.**

Captions were regenerated and verified against the rebuilt master: cue 76 ends `00:03:21,080`
and cue 77 opens `00:03:22,440` — 201.08 + 1.36, exact. Chapters resynced; two moved by one
second. Last cue lands at 291.30s against a 291.30s video.

Frames spot-checked after the rebuild, including mid-hold at 202.0s: both sentences held, the
citation present, no highlight and no arrow. Content is unchanged — video was re-encoded from
the same clips with the same per-segment trims.

**The loudness trade, stated.** −16.2 instead of −14.8, because the audio is now normalised
once on PCM rather than across multiple AAC generations, and single-pass loudnorm on ~20 dB
crest narration undershoots. All four Week 22 cuts now sit within 0.14 dB of each other.
YouTube attenuates loud material and does not boost quiet material, so the only consequence
is that the week plays ~1.4 dB softer than Week 21's uploads.

**Verdict unchanged: clear-for-public, teaching 12/12, production gate PASS.**

---

## Review 8 — the beat chrome should never have shipped

**Tanmay watched the delivered master and found beat identifiers on screen.** Every frame
carried its beat id and act label in the top-left — `B11 WITNESS THREE — friction` — with a
hairline under them. Production chrome, drawn for whoever is building the film, rendered into
a master meant for an audience.

**Week 21's cuts carry none of it.** Cropping the top of a Week 21 frame shows content at the
frame edge and nothing else. This was a regression introduced by the `chrome()` method I
wrote for this week's `scenes.py`, not a house convention.

### Why seven reviews missed it

Review 6 removed seven leaked stage directions from these same frames and reasoned explicitly
that a caption describing the frame to its own builder is not evidence. The beat id and the
act label are that exact category, drawn by that exact method, one line above the notes that
were removed — and they were not questioned.

The production gate asks whether evidence is legible and sourced at the moment of assertion.
It does not ask **whether everything on the frame is meant for the viewer at all**, and
neither did I. Six passes scored these frames without that question being posed once.

The check that would have caught it costs about ten seconds: crop the top strip of a
previously shipped master and compare.

### Fixed

`chrome()` in all four scene files now draws only the title and, where the film promises one,
the corner card. Every beat id, act label and rule is gone. All 48 clips re-rendered, all four
cuts recompiled through the lossless chain and re-normalised.

Verified by cropping the top 14% of a frame from each of the four cuts rather than assuming
the edit took: what remains is a title or the corner card, nothing else.

**The corner card stays deliberately.** B02 promises it aloud, it lights per stage, and the
`reusable rubric` score depends on it being visible. It is viewer-facing content; the beat ids
were not.

Durations are unchanged, so captions and chapters remain valid — masters still end exactly on
their final cue.

**Verdict unchanged: clear-for-public, teaching 12/12, production gate PASS.** The gate now
passes on frames that carry nothing but the film.
