# PEDAGOGY — Every Box, Checked

Loon-detector weekly progress reel · week of **2026-09-04**
Slug `claude-sai-every-box-checked` · 8 beats · all-Remotion + one composed still
Two masters: **16:9 at 3840×2160** and **9:16 at 2160×3840**

> **GATE P — this file is UNSIGNED.** Audio is not to be generated until a human
> has read the narration below and signed the line at the very bottom. Claude
> does not sign it.

---

## The ONE idea

**The quality check ran before the labelling, so the set is small on purpose —
and small and clean is the only version of it that is still cheap to change.**

Week one bought the ground truth's *places and reasons*. Week two closed the
first batch of the ground truth itself. The number is not the achievement; the
**order** is. Every image in the set had to pass a check before anyone spent
time drawing a box on it, which is why there are about 136 of them and not
several hundred of mixed quality.

The reel's second argument comes from the author's own plate rather than from
his report: one class label is covering **two different detection problems** —
a bird that fills its frame, and a bird that is four dark pixels on moving
water. That is visible in the supplied mosaic, so the reel can show it instead
of asserting it.

---

## Act structure

| Beat | Act | Pattern | Portrait sibling | Carries |
|---|---|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` | `ClaudeComposerAsk916` | Cold open. "This is Sai." The week's ask typed on screen; 3 result lines. |
| B01 | THE SET | `ClaudeScienceChipGrid` | `ClaudeScienceChipGrid916` | What is in the closed set: three capture paths, one class, check-then-label, hand-drawn boxes. |
| B02 | THE LABELS | **`STILL`** (composed plate) | `pantry/B02-916.png` | The author's own label mosaic — the evidence beat. |
| B03 | TWO PROBLEMS | `DivergentFates` | `DivergentFates916` | One class label, two detection problems: close-in vs far-out. |
| B04 | TRAIN, OR WAIT | `BinaryBranch` | `BinaryBranch916` | The fork at this size — run it small, or wait for a bigger set. |
| B05 | VERDICT | `ClaudeVerdictArtifact` | `ClaudeVerdictArtifact916` | One-page recap, 4 bare sentences. |
| B06 | HANDOFF | `ClaudeComposerAsk` | `ClaudeComposerAsk916` | Sort your boxes by area. Read aloud and discussed. |
| B07 | OUTRO | `LogoOutro` | `LogoOutro916` | Humanitarians mark + `@HumanitariansAI`, sign-off "Sai." |

---

## ILLUSTRATE LAW check

- Claude UI (`ClaudeComposerAsk`) appears at **B00 and B06 only**, plus the
  verdict and outro pages. ✔
- Body beats run **ChipGrid → STILL → DivergentFates → BinaryBranch**. No two
  consecutive body beats share a pattern. ✔
- Every body beat carries an ordered `show` block. ✔
- No body beat could be a static slide with a voiceover: B01 builds a grid, B02
  *is* the evidence, B03 splits one label into two tracks, B04 opens a fork and
  resolves it. ✔

## ATTRIBUTION OVERRIDE (carried forward)

The guide's **IN-FOR-BEAR LAW** is deliberately suspended for this series,
as established 2026-07-31 and carried through weeks one and two. This is Sai's
own weekly progress report on his own project: B00 says *"This is Sai."* and
B07 signs off *"Sai."* — never "Liam, in for Bear." The **voice** is unchanged
(Kokoro `am_onyx`, free and local) and the folder chip stays
`@HumanitariansAI`. Branding rule 7 holds: the slot-1 kicker is
*Computational Skepticism*.

**OUTRO CHANGE, week three onward (decided 2026-09-04).** B07 is `LogoOutro`,
not `ClaudeTitleOutro`. Weeks one and two shipped an outro card reading
`@NikBearBrown` while every other beat read `@HumanitariansAI` — because
`ClaudeTitleOutro` **hardcodes** that handle (`OUTRO-LOCK.md`; the `handle` and
`subline` props the guide's §4b documents are stale and were silently dropped).
`OUTRO-LOCK.md` scopes that card to `claude-liam-*` slugs and says other
channels use their own outro; `LogoOutro` is it — it takes `handle` and the
humanitarians mark already exists. The author chose to keep `@HumanitariansAI`,
so the reel now carries **one handle throughout**.

`./art run` prints `SKIN LINT: … the outro is 'LogoOutro' — OUTRO LAW wants
ClaudeTitleOutro`. **That lint is this deliberate deviation, not a defect.**

**Consequence for the narration.** `LogoOutro` is a 120-frame (4.0s) card that
fades out at its end, and `remotion_scenes.py` freeze-extends a short render by
cloning the final frame — which is black. So B07's line is held to 10 words and
its audio is generated at `--speed 1.06` to land at 3.9s, inside the card. The
"about a hundred and thirty-six frames, one class" recap B07 used to carry moved
into **B05's verdict**, where a restatement belongs anyway; B05 now also says
"annotated **by hand**". The last ~3 frames of B07 are black — that is the
card's own designed fade-out, and it reads as the reel ending (and, on the 9:16
cut, as a lead-in to the dark endcard).

---

## Evidence and honesty

Full ledger in **`SOURCES.md`**. The three things a reviewer should check
hardest:

1. **The only supplied figure is "about 136 images."** No mAP, accuracy,
   precision, recall, epoch count, batch size, split ratio, instance total,
   annotation-hours or per-source count appears anywhere in the reel. None were
   supplied, and none are inferable from a label mosaic.
2. **No YOLO version is named.** The author said "the latest YOLO vision
   model." Screen and voice say *"the latest YOLO"* in all four places it comes
   up. If a version is wanted on screen, the author must supply it.
3. **Nothing is claimed to have been trained.** He said the set is *ready to
   be* trained. B05 and B07 say so outright.

**The one inference in the reel** is that the set spans three capture paths —
web, a Nikon from shore, and a drone — read off the `web_`/`nikon_`/`dji_`
filename prefixes visible on the plate. It appears on B01, B05 and in B00's
third result line. Those three places must be corrected together if it is
wrong. See `SOURCES.md` §2.

**The voice's arguments, not the author's report** (strike any that overreach):
B04's train-now-or-wait fork and its resolver; B03's claim that the far frames
are where the model gets judged; the reading that check-then-label means
"nothing was labelled that was going to be thrown away"; B06's handoff advice.
`SOURCES.md` §5 lists these in full.

**Two plate features that are not data errors** and are never treated as such:
the `corcommon loon` string on the drone cell (two box captions colliding in
the label visualiser) and the truncated filename tails (the mosaic draws
captions without clipping). `SOURCES.md` §4.

---

## The two aspect ratios

Both masters are true 4K and neither is a crop of the other.

- **16:9 — 3840×2160.** `compile.py --height 2160`; `remotion_scenes.py` picks
  a per-composition `--scale` so the 1920×1080 Claude UI scenes and the
  1280×720 deck patterns both land at 3840×2160 rather than being upscaled.
- **9:16 — 2160×3840.** `shorts.py` writes its own beat sheet into `short/` and
  rewires each beat to its registered `*916` sibling; all seven Remotion
  patterns here have one, so no new TSX is needed. Compile it with
  **`--height 3840`** — `shorts.py`'s printed hint says `--height 1920`, which
  is 1080p portrait, not 4K.
- **B02 is the one beat `shorts.py` cannot derive.** It is user media, so the
  default path would centre-cut it — keeping the middle 37.5% of the sheet's
  width and halving two of its four columns. Instead `make_plates.py` composes
  `pantry/B02-916.png`, the one human override slot `shorts.py` honours: eight
  of the sixteen cells, re-tiled 2×4 and ordered **largest subject first**, so
  the plate reads top-to-bottom as a scale ramp on a phone. Its caption says
  *8 of 16 tiles, re-tiled* — the portrait viewer is told they are seeing a
  subset.
- **B02 holds; it is not Ken-Burnsed.** The range across the whole sheet is the
  beat, and `compile.py`'s zoompan pushes ~8% outward, which would clip the
  outer cells. A focus point on a contact sheet is meaningless anyway.

---

## Human review checklist

- [ ] The week is reported accurately: annotation complete on everything
      quality-checked last week, about 136 images, ready for the latest YOLO,
      nothing trained yet.
- [ ] "About a hundred and thirty-six" is the right qualifier — the author said
      "about one thirty six".
- [ ] The three capture paths (web / Nikon / drone) are correct. This is the
      reel's one inference, taken from the filename prefixes.
- [ ] No figure appears on screen that was not supplied. No YOLO version is
      named.
- [ ] B04's train-or-wait fork is acceptable as the *voice's* argument — the
      author is not shown deciding it.
- [ ] B06's handoff is worth a viewer's time and is discussed, not just read.
- [ ] Sign-off is "Sai." — the in-for-Bear line is correctly absent.
- [ ] Both plates read: `media/B02.png` (16:9) and `pantry/B02-916.png` (9:16).

After signing, run the four build steps in `BUILD-PROMPT.md`, then **LOOK at
`_qc/`** for both cuts — a Gate V underfill warning on a centred title or
verdict card is a known false positive, and on the 9:16 cut so is an edge-bleed
warning unless it reproduces on the clean master.

---

VERDICT: PASS     — reviewer: Sai Nikhil Kunapareddy  date: 09-04-2026
