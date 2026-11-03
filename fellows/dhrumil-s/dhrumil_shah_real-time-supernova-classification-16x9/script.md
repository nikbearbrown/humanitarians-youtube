# script.md — Real-Time Supernova Classification

*"Seven Million Alerts a Night"* · 16 beats · landscape 16:9 · presenter Dhrumil Shah ·
voice: Kokoro `am_onyx`

**Register:** documentary. Confident, curious, precise. No hype verbs, no "revolutionising", no
claim that a model *knows* anything. Uncertainty is stated as uncertainty.

**Format:** this is the 16:9 cut. Narration, audio files and measured clock are byte-identical to
the 9:16 cut (`../real-time-supernova-classification-9x16/`); only the composition changes.

**Clock rule:** the measured durations in `audio/timings.json` are the master clock. The Remotion
composition imports that file directly; nothing in the animation is hand-timed.

**Structure:** the film opens on the presenter introduction (B00) — name, then a one-sentence
summary of what the film answers — and then runs the fifteen-beat film unchanged (B01–B15). Beat IDs
were kept stable when the intro was added, so every scene, caption, source line and fact-check row
still refers to the same content.

---

## Narration, beat by beat

Measured durations are the Kokoro output after edge-silence trimming.

### B00 · PRESENTER INTRODUCTION — *who, and what this answers* · 11.47 s
> Hi, I am Dhrumil Shah, and this video is about how artificial intelligence helps astronomers sort
> millions of nightly sky alerts, to find the exploding stars that are actually worth a telescope's
> time.

### B01 · COLD OPEN — *the flood* · 10.69 s
> Every clear night, one telescope in Chile compares the sky to the way it looked before, and
> reports what changed. At full survey operations, that is about seven million alerts before
> morning.

### B02 · THE PROBLEM — *no human team* · 8.81 s
> No group of astronomers can read seven million of anything. One alert per second, without
> sleeping, and a single night's take would keep you busy for eighty-one days.

### B03 · SCAN — *the survey* · 9.91 s
> The survey is the Legacy Survey of Space and Time. A very wide camera photographs the southern
> sky, moves on, and comes back to the same field again and again for ten years.

### B04 · REFERENCE & NEW — *the comparison* · 8.70 s
> Every new image has an ancestor. A deep template, stacked from everything seen at those
> coordinates before. The pipeline aligns the two, pixel against pixel.

### B05 · SUBTRACT — *difference imaging* · 10.24 s
> Then it subtracts. Steady stars cancel. Galaxies cancel. What survives is only what changed, and
> anything above five sigma counts as a detection, whether it got brighter or fainter.

### B06 · WHAT COULD IT BE — *six honest answers* · 10.73 s
> A leftover dot is not a discovery. It could be a supernova. A variable star. An asteroid. A
> feeding black hole. A cosmic ray striking the sensor. Or a flaw in the subtraction itself.

### B07 · ALERT — *the packet* · 11.88 s
> So the pipeline packages it instead of judging it. Position, brightness, timestamp, twelve months
> of previous measurements, and postage stamps of the template and the difference. Requirement: out
> the door within sixty seconds.

### B08 · THE STREAM — *scale and brokers* · 8.35 s
> Now multiply that by a thousand pointings a night. The stream is public, and it is caught by seven
> independent community brokers built for nothing else.

### B09 · CLASSIFY — *two models, one trade* · 11.10 s
> A broker does what a tired expert would do, at machine speed. In ALeRCE, one network reads the
> image stamps on the very first detection. A second model waits for six, and reads the light curve
> instead.

### B10 · LIGHT CURVE — *shape is the evidence* · 10.07 s
> Shape is what carries the meaning. A supernova climbs over days and fades over weeks. A variable
> star repeats itself. An asteroid simply never comes back to the same piece of sky.

### B11 · PROBABILITIES — *not a verdict* · 10.49 s
> And the answer is not a verdict. It is a set of probabilities. The stamp classifier is about
> ninety percent accurate on a balanced test set, which is a statement about the model, not about
> the star.

### B12 · RANK — *the actual contribution* · 8.70 s
> But that is enough to sort. Thousands of ordinary alerts sink quietly. A few unusual ones rise to
> the top of somebody's queue before the night is over.

### B13 · FOLLOW-UP — *the scarce measurement* · 10.14 s
> And sorting is the whole point, because the confirming measurement is rare. A spectrum splits the
> light into wavelengths and shows what is actually burning. Very few telescopes can spare the time.

### B14 · THE LIMIT — *classification is not confirmation* · 9.21 s
> Rubin may find close to a million supernovae. The overwhelming majority will never get a spectrum
> at all. A classification is a ranking. It is not a confirmation.

### B15 · CLOSE — *the line* · 6.93 s
> The machine never decides what exploded. It decides what is worth pointing a telescope at, while
> there is still something left to see.

---

## Length

| | |
|---|---|
| Narration words | **490** (B00 adds 33 to the 457-word film) — per-beat counts in `beat_sheet.json` |
| Measured speech | 157.40 s |
| Timeline with 0.32 s inter-beat gaps | 162.21 s |
| Film with 1.58 s closing tail | **163.80 s (2:43.8) · 4,914 frames at 30 fps** |
| Target band / hard ceiling | 2:20–2:50 / 2:59 — inside both |

The brief's 300–380 word target assumed ~2.2 words/second; measured `am_onyx` runs faster, so length
was governed by the *duration* band instead. No trim was needed.

**Trim order, if a future edit pushes past 2:50:** B03 (drop "for ten years") → B07 (drop "instead of
judging it") → B00 (drop "that are actually") → B06 (drop one impostor) → B10 (drop the asteroid
clause). None of these carries a cited figure.

---

## A note on the opening

The original brief (written for the vertical cut) asked for the first 3–5 seconds to open on the
scientific problem rather than on the presenter. On landscape YouTube the opening is less punishing
than on a swipe feed, but the same trade applies. The introduction was then added at the presenter's explicit request. The cost is
real — the counter hook now lands at 0:11.8 rather than 0:00 — and the intro is built to limit it:

- the greeting is one clause; the summary *is* the hook ("millions of nightly sky alerts … exploding
  stars worth a telescope's time"), so the stake is stated in the first eight seconds;
- the frame is not a talking-head card — it previews the six-stage pipeline the film then walks
  through, so the time spent is also an advance organiser;
- the intro deliberately says "millions", not "seven million", so the headline figure is still
  revealed, and qualified, by B01.

---

## Lines that carry a cited number

Every one is in `FACTCHECK.md` with its source. No other line asserts a quantity; B00 asserts none.

| Beat | Figure | Qualified on screen as |
|---|---|---|
| B01 | ~7 million alerts / night | "at full survey operations" — expectation, not measurement |
| B02 | 81 days | `DERIVED` (7,000,000 ÷ 86,400 s) |
| B05 | 5 sigma | detection threshold, positive or negative flux |
| B07 | 12 months, 60 seconds | 60 s shown as `REQUIREMENT` |
| B08 | ~1,000 pointings; 7 brokers | visits/night from DMTN-102 |
| B09 | first detection vs ≥6 detections | attributed to ALeRCE by name |
| B11 | ~90% accuracy | "on a balanced test set" — condition in the spoken line |
| B14 | ~1 million supernovae; ~30,000 spectra | "may find"; TiDES capacity |

## Words deliberately avoided

`revolutionary` · `breakthrough` · `the AI knows` · `instantly identifies` · `solves` ·
`replaces astronomers` · `discovers supernovae`. The last is the important one: the film's thesis is
that the model does not discover anything, so the intro's verb is *sort*.
