# BUILD-LOG — *The Signal We Imagined.*

**AI in Astronomy & Space Science · Ep. 13** · slug `seti-signal-detection`
Built with `brutalist.art` (the free-only Fellow Tier), skill `ai-explainer`,
channel `claude-hai`, Pragmatist register. Built 2026-10-16.

**Total spend: $0.00.** Kokoro TTS runs locally; every plate is computed
here; no API key was used or required at any step.

---

## What shipped

| | 16:9 | 9:16 |
|---|---|---|
| `claude-for-astronomy_OmMali_16_10_2026.mp4` | 3840 × 2160 · 141.55 s · 3397 frames · 16.3 MB | — |
| `seti-signal-detection-9x16.mp4` | — | 2160 × 3840 · 141.55 s · 3397 frames · 17.1 MB |

24 fps, h264 + AAC, −20.9 LUFS integrated, both cuts sharing one audio mix.
**2:21.5** — 38 s inside the 3:00 cap. Both masters live in this folder.
Nothing was published.

---

## The episode

Topic 13 of the brief is how AI separates alien signals from human
interference. The detective-story version skips the only hard part.

This is the first episode in the series where **the positive class does not
exist.** Every earlier limit lived in something inspectable — a biased
training set, an under-specified objective, a leaky split. Here there is no
training set to bias, no test set to leak, and nothing to validate against,
because nobody has ever observed the thing being searched for. That framing
is not mine; it is the stated motivation of the field's own toolkit:

> "Given that we have not yet detected a radio SETI signal, we must make
> assumptions about their form"
> — Brzycki et al. 2022, *AJ*

So the detector here is the real algorithm — the de-Doppler statistic a
technosignature pipeline computes — which makes the assumption a single
visible number: the range of drift rates swept.

| hypothesis | found |
|---|---|
| drifting, as searches assume | **80 / 80** |
| **drift-corrected** — what we do for our own spacecraft | **0 / 80** |
| the same signal, sweep widened by one number | **80 / 80** |
| pulsed beacon (its drift *is* searched) | 0.70 |

The control locates the blind spot exactly: recall falls 1.00 → 0.00 between
**0.06 and 0.12 Hz/s**. A cliff, not a slope. And the escape is the test the
field already uses and the one that settled BLC1 — point at the star, look
away — which scores **0.76** on the signal the morphology search scores zero
on, because it asks *where a signal came from* rather than what it looks
like.

---

## Gate results

| Gate | Result |
|---|---|
| F — paperwork set | present |
| L — beat-mix lint | clean |
| A — static pre-flight | 10/10 `rc=0`, first pass |
| W — WCAG · margins · overlap | 10/10 `rc=0`, first pass |
| B — pixel layout, both aspects | 20/20 `rc=0`, after 7 fixes |
| P — human signature | PASSED, before audio |
| Pacing — 24 fps, both aspects | 20/20 inside `−0.25 s … +0.05 s` |
| V — 16:9 master | 28 frames · 0 BLOCKER · 0 MAJOR (after a real fix) |
| V — 9:16 master | 28 frames · 0 BLOCKER · 0 MAJOR |
| Frame reading, both aspects | 2 further defects found and fixed |

**GATE T and GATE SHARPNESS were not run: they are not shipped in this
toolkit**, despite SKILL.md describing GATE T as "ALWAYS RUN".

---

## The experiment, and the four times it caught me

`gen_seti.py` asserts three claims and writes nothing if any fails.

**A claim I measured and then cut.** An earlier version argued zero drift is
*too crowded with interference to search* — the reason, I assumed, that
pipelines exclude it. The measurement refused: **6 look-alikes for a drifting
candidate against 5 for a stationary one.** No difference. The real flood of
zero-drift interference is a property of actual spectrum occupancy, which
four simulated lines do not reproduce, and raising the line count until the
claim came true would be tuning the experiment to the conclusion. The claim
went; the function stayed and is still reported. BLC1's look-alike argument
appears in the reel as a **published** result only — which it is.

**Three simulators discarded, all my errors:**

1. **A statistic that could not work.** The first detector took a single
   maximum over the whole field. The interference is brighter than the
   signal, so the maximum was always an interference line and the injected
   signal never moved it — every recall came out at 0.03–0.10. A pipeline
   returns a *hit list*; the question is whether the real signal is on it.
2. **A threshold set by the interference.** Calibrating on fields containing
   interference made the threshold track the brightest line (22.6), so
   nothing could exceed it. The interference is not meant to be *under* the
   threshold — it is the pile of hits a human sifts.
3. **An under-resolved regime.** At 16 rows and 0.15–0.60 Hz/s a signal
   drifts only 2–10 channels across the integration against a 1–2 channel
   linewidth, so de-Doppler could not separate drifting from stationary at
   all. Real surveys integrate for minutes and sweep several Hz/s; now 32
   rows at 0.6–2.0 Hz/s.

A fourth, smaller: drift was drawn with a random **sign** while the search
ranges covered only positive rates, so half of every "assumed" signal was
never searched for. It surfaced as recall 0.45 on the one hypothesis that
was supposed to work.

---

## GATE V caught a real legibility fault

The first compile failed with four MAJOR low-contrast defects on B04 and
B06 — separation 0.22–0.25 against a 0.30 floor. Not a gate quirk: at
display gamma 0.75 the spectrograms' mid-grey noise was lifted toward ink
and the interference lines were no more contrasty than the noise around them.

I read the gate's code rather than guessing. It averages **every** pixel
differing from the background by more than `INK_DELTA`, so thousands of
marginally-grey noise pixels drag the mean toward cream. Measuring directly:
gamma 1.55 → 0.237, gamma 2.20 → 0.286, **gamma 2.80 → 0.327**. One
intermediate attempt was not enough and went back through the gate and
failed again before the right value was measured.

The picture is better for it: dark interference lines against pale noise,
with the terracotta guide marking the track the viewer is told they cannot
see.

---

## Aspect discipline

**Six of the seven GATE B failures were one mistake**: a label positioned at
`pat[0] ± pw * k`. In landscape `pw` is 7 units and that lands inside a
12.3-unit frame; in portrait `pw` is 3.4 and the same expression lands
outside a 3.6-unit frame. **An offset scaled to the plate is not an offset
scaled to the safe area.**

`three.png` is 0.271, so at portrait's 3.44 units its three panels would be
1.1 across and the lean of the marked track — the whole content — stops being
readable. Portrait loads `three_v.png` instead.

---

## Pacing — a third situation

All 20 clips land −0.11 to −0.22 s under their beats. **B06 undershot at
−0.30**, outside tolerance, with RT already at the 1.55 cap and the tail
floored, so neither usual lever applied. HOLD is what grows the body there
(0.034 → 0.043 → −0.13). The three cases are now recorded in `scenes.py`:

- tail above the floor → trim (never actually observed in five episodes)
- tail floored, RT below cap → lower RT
- tail floored, RT at cap → raise HOLD

---

## Reproducing this reel

```bash
PY=.venv/Scripts/python.exe            # a Windows venv has no python3.exe
R=<this folder>

$PY assets/gen_seti.py --force         # plates; asserts three claims
$PY runtime/scripts/generate_audio_kokoro.py "$R"     # needs GATE P signed
$PY -m manim -qk --fps 24 -r 3840,2160 scenes.py <Scene>   # one at a time
$PY -m manim -qk --fps 24 -r 2160,3840 scenes.py <Scene>
$PY runtime/scripts/remotion_scenes.py "$R"
$PY runtime/scripts/compile.py "$R" --height 2160
$PY runtime/qc/final_frame_check.py "$R" \
   --mp4 "$R/claude-for-astronomy_OmMali_16_10_2026.mp4"
```

The 9:16 cut is built through `shorts.py --drop --no-endcard`, with the
portrait clips staged into `short/manim/` and `--height 3840`.

**Pass `--mp4` explicitly to the frame check. Always.** And re-run the
generator with `--force` after changing `seti.py`: the experiment is cached
in `assets/.cache_seti.npz`, and the cache does not know the physics changed.
