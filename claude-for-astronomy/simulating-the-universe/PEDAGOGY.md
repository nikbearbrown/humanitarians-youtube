# PEDAGOGY - *The Universe You Can Afford.*

**GATE P.** A human reads the narration below and signs. Audio is not generated
until the verdict line below is changed from PENDING to a pass. Kokoro is local
and free, so this gate protects quality, never spend.

> Note for anyone editing this file: `generate_audio_kokoro.py` opens GATE P on a
> plain substring match anywhere in this document, so do **not** write the passing
> verdict string in prose - spelling it out in an explanatory sentence silently
> unlocks the gate. That is why this paragraph describes it instead of quoting it.

**VERDICT: PASS**

Signed: Om Mali  Date: 09/04/2026

---

## Written to a length this time

Ep. 06 was first cut at 5:23 and the human asked for under three minutes. So this
episode was **written to a word budget** rather than trimmed afterwards: 443
words, sized against Ep. 06's own measured speech rate of 0.3843 s/word.
Predicted **2:51**, with about nine seconds of margin under the cap.

If the measured audio comes in over 3:00 anyway, the fix is a few seconds of
`--speed`, exactly as on Ep. 06 - the words you sign are the words that ship.

## What this episode is for

Ep. 07 of *AI in Astronomy & Space Science*, from `weekly_stem_videos/ideas.md`
Astronomy topic 07 - simulating the universe.

Six episodes have now shown AI **looking at observations**: triaging them,
classifying them, detecting things in them, deciding about them. This one is the
first where there is nothing to look at. You cannot run an experiment on the
universe, so a theory's only voice is a simulation - and the AI's job here is to
**stand in for the physics itself**.

That makes the limit new as well. The emulator is trained on N-body output, so it
is a compression of simulations somebody already paid for, and it cannot be
trusted outside the box of cosmologies it was shown. That is a **circularity**,
not an accuracy ceiling (Ep. 04), an unseen class (Ep. 03), an irreversible
rejection (Ep. 05) or a latency (Ep. 06).

## The spine

| Beat | Job |
|---|---|
| B00 | Self-introduction and the ask; the ask lands answered |
| B01 | Presenter; the pivot from looking at data to replacing the physics |
| B02 | BLUF: no experiment is possible, so you simulate - thousands of times |
| B03 | Why thousands: you are searching a parameter space (Quijote's scale) |
| B04 | Why each one is expensive: the loop gravity forces you into |
| B05 | The cheap answer: Zel'dovich, one straight move per particle |
| B06 | The trick: learn the difference between cheap and real |
| B07 | The result: ~5% on the standard statistics, 1/1000 of the time |
| B08 | The design tell: it learned the map, not the law |
| B09 | Where it breaks: inside haloes, which is where galaxies live |
| B10 | The deeper limit: it cannot leave the box it was trained on |
| B11 | Verdict recap |
| B12 | Handoff prompt, read verbatim |
| B13 | Title outro |

## The narration, in full - this is what you are signing

**B00.** Hi, I'm Om Mali. This video is about how AI is replacing the most expensive
calculation in cosmology — simulating a universe — and what you give up when a
network answers instead of gravity.

**B01.** This is Humanitarians AI. Six episodes about AI looking at data. This one, it
replaces the physics.

**B02.** One breath. You can't experiment on the universe, so cosmology tests a theory
by simulating it — and that takes thousands of universes. Nobody can afford
it, so a network learns the answer instead.

**B03.** Why thousands? You aren't checking one universe, you're searching a parameter
space. Quijote is forty-four thousand simulations across seven thousand
cosmologies: eight and a half trillion particles, built as training data.

**B04.** Each one is expensive because gravity has no shortcut. Every particle pulls
every other, so you deposit mass on a grid, solve for the field, nudge
everything, and repeat, hundreds of times.

**B05.** Here's the trick. There's a cheap answer — the Zel'dovich approximation. Move
every particle once, in a straight line, and stop. Very good while the
universe is smooth; badly wrong once things collapse.

**B06.** So you don't fix the physics, you fix the picture. Train a network on the
difference between the cheap guess and the real simulation, then apply that
correction. It never computes a force.

**B07.** It works. On the statistics cosmologists use — power spectrum, bispectrum,
wavelets — the emulator matches N-body within about five percent at most
scales. In a thousandth of the time.

**B08.** Now the design tell. That model has never simulated gravity. It learned the
map from a starting field to a finished one, for the universes it was shown.
Compression, not physics.

**B09.** Which tells you where it breaks. The reported errors sit inside dense haloes —
and haloes are where galaxies live. In my own two-D run, the cheap guess is
four percent off on large scales and sixty on small ones.

**B10.** The deeper limit is quieter. Training it needs N-body runs, so it's a
compression of simulations you already paid for, and you can only trust it
inside the box it was shown.

**B11.** Recap. Cosmology can't experiment, so it simulates, and that needs thousands
of runs nobody can afford. The emulator skips gravity and corrects a cheap
guess: five percent, a thousand times faster.

**B12.** Your turn. Paste this. I want to replace an expensive simulation with a
learned surrogate. Help me choose which statistics it must reproduce and to
what tolerance, how to spot an input outside its training set, and what I'd
still run the slow way. Grade it: named tolerances, an out-of-distribution
check, a slow-path audit.

**B13.** The universe you can afford. Humanitarians AI. I'm Om Mali.

## Things a reviewer should push back on

1. **"Forty-four thousand simulations"** is Quijote's published count (44,100),
   and I say "forty-four thousand" rather than the exact figure because the
   on-screen counter carries the precise number. If you would rather the voice
   said the exact figure, say so.
2. **"Within about five percent"** is the field-level emulator's reported
   agreement on the power spectrum, bispectrum and wavelet statistics *at most
   scales* - not a blanket accuracy. B07's citation line names the paper, and
   the narration says "on the statistics cosmologists use", which is the honest
   scoping. It is still the sentence most likely to be over-read.
3. **"A thousandth of the time"** is that paper's own comparison at
   (3 Gpc/h)^3 volumes. It is not a universal emulator speedup; other published
   emulators report anywhere from ~10x to ~600x.
4. **The four percent and fifty-eight percent in B09 are mine**, measured from
   the 2D particle-mesh run in `assets/gen_cosmos.py` - not from the literature.
   The narration says "in my own two-D run" and the citation line says
   "percentages measured here". They illustrate the *shape* of the Zel'dovich
   error, at the wrong scale and one dimension short.
5. **Everything on screen is a 2D toy at 512 squared.** Every beat that shows a
   plate captions it. A production run is three-dimensional with trillions of
   particles; nothing here should be read as a picture of a real survey volume.
6. **"It never computes a force"** is true of the emulator's forward pass and is
   the point of B06 and B08. It is not a criticism, and B08 says so.
7. **No published figure is reproduced.** Every plate is computed by this reel's
   own generator.

## If you want changes

Edit the narration in `beat_sheet.json`, not here - this file is the record of
what was signed. Then re-run the audio pass; measured durations are the clock.
