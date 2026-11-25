# READ-ALOUD — Reading a Twentieth of a Pixel (long film, 16:9), draft 1

Narration only, in order, as the voice will say it. Numbers in words. Read it aloud once at your own pace and mark anything that rushes, confuses or trips your tongue. **For your read, not yet the Gate P sign-off.** Every figure comes from `experiment/photon_precision.py` (our own simulation), `experiment/rotation_bars.py` (a labelled toy disk), or the public values listed in `FACTCHECK.md`.

**B00 · THE PUZZLE** (~17 s) — curious

To know a galaxy's speed to one kilometer per second, you have to find a line of light to within two thousandths of a nanometer. The pixel that catches that light can be more than twenty times wider. So how do you read a mark that is a twentieth of the ruler's smallest division?

**B01 · THE SETUP** (~13 s) — hands-on

I'm Tanmay Kulkarni, in for Humanitarians AI. I didn't use a telescope. I built the measurement: one line of light, a row of pixels, and photons arriving one at a time, so I could count exactly what each photon buys.

**B02 · THE SHIFT** (~19 s) — plain

First, what moves. In the lab, hydrogen-alpha sits at six hundred fifty-six point two eight nanometers. A galaxy shifts it by its speed divided by the speed of light, times that. Andromeda's light arrives about point six six nanometers off. That is thirteen of my pixels, easy to see. The hard part is the last kilometer per second.

**B03 · THE LINE IS A SMEAR** (~18 s) — diagnostic

A spectral line is not a spike. It is a smear, because the gas that makes it is hot and moving. I gave mine a width of a hundred kilometers per second. Each photon lands somewhere in that smear, one at a time, and I only see which pixel caught it. Never where inside the pixel.

**B04 · TEN PHOTONS** (~10 s) — deflated

Ten photons. My best guess for the center jumps around from run to run, off by about fifteen kilometers per second. That is most of a pixel. Ten photons say almost nothing.

**B05 · A HUNDRED, A THOUSAND** (~18 s) — surprised

A hundred photons, and I am off by four point six. A thousand, and I am off by one point four. A thousand photons, and my guess is good to six percent of a pixel. The pixel never got smaller. The guess got finer, because every photon is a small vote, and votes average.

**B06 · THE RULE** (~29 s) — careful

Here is the rule, and it is short. Three numbers matter. How far the line moved is the thing you want. How wide it is, and how many photons you caught, decide how well you know it. The error is the width of the line, divided by the square root of the photons. A hundred times the light buys ten times the precision. I checked it from ten photons up to a hundred thousand. It held to within about eight percent, the small cost of sorting photons into pixels.

**B07 · THE PRICE LIST** (~16 s) — measured

So here is the price list. Each tenfold gain in precision costs a hundredfold more light. Four point six kilometers per second at a hundred photons. Point four six at ten thousand. Point one four at a hundred thousand. Precision is not free. You pay for it in light.

**B08 · WHOSE SPEED** (~17 s) — careful

One more thing the shift carries: us. A shift is relative, so it includes our own motion. Measured from the Sun, Andromeda's light reads about three hundred kilometers per second toward us. Take out the Sun's own motion, and the approach is about one hundred nine. Most of that three hundred is us.

**B09 · THE EDGE OF A GALAXY** (~22 s) — curious

Now zoom out to a spinning galaxy. Each point along the disk is its own measurement, with its own photons. The bright middle has plenty. The faint edge has few. In a toy disk I drew, the bars at the edge came out ten times longer than at the center. A rotation curve is not one line. It is a row of measurements, each with its own photon budget.

**B10 · THE BOUNDARY** (~23 s) — disciplined

What this does not cover. I tested one thing real spectra have, sky glow. Add ten times as many glow photons as line photons, and my error at a thousand photons went from one point four to three point four. I did not test blended neighbors or calibration error, and I measured nothing on a telescope. These are my simulated photons, and the rule they obeyed, bent by the glow.

**B11 · YOUR TURN** (~18 s) — handed over

Your turn. Take a line a hundred kilometers per second wide. You want the speed to five. How many photons? The line's spread is about forty-two. Divide by five, then square it. About seventy-two, and closer to eighty-five once pixels get involved. Whenever you see a speed quoted that finely, ask how many photons paid for it.
