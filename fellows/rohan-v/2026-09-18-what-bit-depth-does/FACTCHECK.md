# FACTCHECK — "16-bit or 24-bit: What Bit Depth Does"

Every factual claim, its basis, its verdict. Verified 2026-09-16 against the
final 7-beat cut.

**The measurement came before the script.** Quantisation noise was measured in
float64 numpy *first*, and the narration then described the result. Raw log:
[MEASUREMENTS.txt](./MEASUREMENTS.txt); method and limits:
[SOURCES.md](./SOURCES.md).

| # | Claim | Where | Basis | Verdict |
|---|---|---|---|---|
| 1 | Saving a recording will ask you for 16-bit or 24-bit | B00 | True of every common audio editor and DAW export dialog — Audacity, GarageBand, Logic, Reaper, Ableton, Pro Tools. The sentence is scoped by "save a recording", i.e. in something that records audio, not any device at all | **PASS** — scoped reading |
| 2 | Sound is air pressure rising and falling; a microphone feels that movement | B01 | Definitional | **PASS** |
| 3 | A computer stores sound as a list of numbers, and doing so needs two separate decisions: how often to measure (sample rate) and how precisely to write each measurement down (bit depth) | B01 | Definitional. Naming sample rate and explicitly setting it aside is the point of the beat | **PASS** |
| 4 | A centimetre ruler and a millimetre ruler are the same length; one just lets you be more precise | B02 | Analogy, and an exact one: quantisation step size is the ruler's marking spacing, and full scale is the ruler's length | **PASS** — analogy, stated as one |
| 5 | 8 bits gives 256 markings | B02 counter | 2⁸ = 256 | **PASS** — arithmetic |
| 6 | Every measurement has to land on a marking; anything in between is pushed to the nearest one | B02 | Definition of mid-tread uniform quantisation — exactly what `measure_bitdepth.py` performs | **PASS** |
| 7 | Every stored number is therefore slightly off | B03 | Follows from claim 6. Error is bounded by ±½ step | **PASS** |
| 8 | This happens tens of thousands of times every second — 44,100 | B03 counter | CD sample rate, and the rate used in the measurement | **PASS** |
| 9 | All those small errors together are a sound of their own: a faint hiss under the music | B03 | Established. Undithered quantisation error of a complex signal is noise-like and broadband; the measurement in claim 11 is its RMS level | **PASS** |
| 10 | The coarser the ruler, the bigger each error and the louder the hiss | B03 | Measured: a 256× coarser step (8-bit vs 16-bit) raises the floor by 47.6 dB | **PASS** — measured |
| 11 | At 8 bits the hiss sits about fifty decibels below full volume; at sixteen, about a hundred | B04 | Measured **−53.14** and **−100.75** dBFS. Narration says "about fifty" and "about a hundred"; the frame prints −53 and −101 | **PASS** — measured |
| 12 | A hundred decibels is roughly the gap between a whisper and a rock concert | B04 anchor | See the note below. Published figures put a whisper at 20–30 dB SPL and a rock concert at 100–120, so the gap is 70–100 dB. 100 is the top of that range, which is why both the narration ("roughly") and the label ("≈") hedge, and why the on-screen scale is drawn relative to full volume rather than in absolute SPL | **PASS** — hedged, see note |
| 13 | At 16 bits the hiss is already quieter than the room you are sitting in | B04 | A quiet domestic room measures ~30 dB SPL. Play a file so full scale lands at a normal listening level (~85–95 dB SPL) and its 16-bit floor sits below that room. Stated as a practical fact about listening, not a physical law | **PASS** |
| 14 | While you work, every edit rounds all over again; turn something up and you turn its hiss up with it | B05 | True of fixed-point processing: each gain change re-quantises, and gain applied to a signal applies to its noise floor too | **PASS** |
| 15 | So record and edit in 24-bit, export in 16-bit | B05 | Standard practice, and the direct consequence of claims 13 and 14. Offered as advice, labelled as such | **PASS** — advice |
| 16 | A 16-bit file is about a third smaller than 24-bit | B05 step 2 | 16 ÷ 24 = 0.667 — 33% smaller at the same sample rate and length | **PASS** — arithmetic |
| 17 | Never save down to 16-bit and then keep editing | B05 step 3 | The hiss added by the down-step is now part of the signal; later edits cannot remove it. Stated with no number attached | **PASS** — no invented figure |
| 18 | Bit depth is not quality; it is room to work in | B00, B06 | Deliberately strong phrasing, and defensible: above roughly 14 bits the noise floor is inaudible in any real room, so depth stops being a fidelity variable and becomes a headroom one. B05 says exactly where it *does* matter | **PASS** — see note |
| 19 | Narration voice is Kokoro `af_bella`, local and free | description.txt | `generate_audio_kokoro.py` reported `cost $0.00` | **PASS** |

## The two claims that needed a hedge, and got one

**Claim 12 — the whisper-to-concert anchor.** This is the reel's one appeal to
everyday experience rather than to its own measurement, and published SPL tables
disagree with each other by 30 dB at both ends. The frame does two things about
it: the narration says *roughly*, the label says *≈*, and the on-screen ladder
(rock concert / conversation / quiet room / a distant whisper) is placed against
**how far below full volume**, so it reads as a relative scale — which is the
only thing the measurement supports.

**Claim 18 — "bit depth isn't quality".** A viewer could hear this as "depth
never matters", which would be wrong, so the reel spends a whole beat (B05) on
the case where it does. The claim is about the *listener's* file, and it is the
reel's through-line, not a throwaway.

## The offset from the textbook formula

Every measured floor sits about **3 dB below** `6.02b + 1.76` (−53.1 vs −49.9;
−100.8 vs −98.1; −149.6 vs −146.2). That formula assumes a full-scale sine and an
idealised uniform error distribution; the measured signal peaks at −6 dBFS and is
rounded rather than dithered. The offset is consistent across all three depths,
which is what a systematic difference in assumptions looks like rather than an
error. **The reel reports the measured values**, and B04's on-screen MEASURED
footnote names the method.

## Honesty notes carried in the graphics themselves

- **B02 draws 16 rungs, not 256** (12 in the portrait cut, where the plot is a
  third as wide). At any legible height 256 markings are a solid grey block. The
  frame says so in its own caption, generated from the constant that draws them,
  so the caption cannot drift from the drawing.
- **B04's ladder is relative, not absolute.** It is labelled "how far below full
  volume" and carries no dB SPL figures, because the measurement is in dBFS and
  converting to SPL would require a playback level the reel does not know.
- **24-bit is measured but never claimed on screen.** The third row of
  MEASUREMENTS.txt (−149.56 dBFS) exists and is real; it was cut from the reel
  because comparing three depths was more detail than the audience needs. The
  reel's B05 recommends 24-bit for working without quoting its floor.

## Why numpy and not ffmpeg

ffmpeg's filter graph is 32-bit float internally — a 24-bit mantissa — so a
24-bit round trip is *lossless to ffmpeg* and it reports an error of `-inf`.
That is a limit of the tool, not a property of 24-bit audio. The first attempt
at this measurement hit exactly that and is recorded in
[BUILD-LOG.md](./BUILD-LOG.md); float64 numpy has the headroom to measure all
three depths honestly.

VERDICT: **PASS** — 19 of 19 claims verified. 3 measured here, 3 arithmetic,
11 definitional or established, 2 appropriately hedged advice/framing claims.
