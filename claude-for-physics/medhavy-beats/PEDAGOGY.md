# PEDAGOGY.md — beats (Chapter 17, Beats)

## Concept
Two tones of nearly equal frequency superpose at the listener. Their phase
relation drifts steadily, so the combined amplitude swells (crests aligned)
and collapses (crest on trough) at the beat frequency f_beat = |f2 - f1|.

## Audit against the bar
- **Single tension:** two perfectly steady notes produce a sound that is not steady -- where does the slow pulse come from?
- **Single resolution:** superposition; the drifting phase makes the sum's envelope swell and pinch at a rate equal to the frequency difference.
- **One primary visual object:** pressure-versus-time at the ear: the two component strip charts and their live sum on the same scrolling time axis.
- **<=6 elements per scene:** B00: 2 labeled waves. B01: + in/out-of-step guides + exaggeration note. B02: guides removed; faint components (pair), sum, silence bands, note. B03: + envelope, amplitude bar ("now"), equation = 6 (pair, sum, bands, envelope, bar, equation; note is a small footnote). B04: bands and note fade, summary added = 6.
- **Self-contained:** needs only sinusoids and superposition; frequency, in step / out of step, and envelope are all shown as they are named.

## Physics check (against 17-sound/6-beats.mdx)
- Textbook models y1 = A cos(k1 x - 2 pi f1 t), y2 = A cos(k2 x - 2 pi f2 t), evaluated at x = 0; the video plots exactly A cos(2 pi f t) for each tone versus time at the listener, and the sum is computed in code as the literal y1 + y2.
- Sum = 2A cos(2 pi f_avg t) cos(2 pi (|f2 - f1|/2) t); the envelope drawn is 2A|cos(pi (f2 - f1) t)|, whose maxima (loud) recur at |f2 - f1| -- Equation 17.17, f_beat = |f2 - f1|. 444 Hz - 440 Hz = 4 Hz. Correct.
- Pinch (silence) instants are where cos(pi delta-f t) = 0, i.e. crest-on-trough; grey bands and out-of-step guides are placed at exactly those instants; in-step guides at envelope maxima.
- The displayed tones use 3.0 and 3.5 cycles per screen-second (an exaggerated ratio, displayed beat 0.5 Hz); this is disclosed on screen ("frequency difference exaggerated so the drift is visible") so no false impression of the 1% real difference is given.
- Piano-tuner claim matches the section ("the beats have a lower frequency as the frequency of the note played approaches the frequency of the tuning fork"); beats vanish when f2 = f1 since f_beat = 0.
- "Amplitude doubles" where crests align: 2A, correct.

## Exclusions honored
No FM radio analogy, no heterodyning, no three-frequency beats.

## Style compliance
- Medhavy palette: teal = 440 Hz, crimson = 444 Hz, ink = sum, gold = envelope/beat, slate = out-of-step/silence. Accent rotation TEAL -> SLATE -> INK -> GOLD -> CRIMSON.
- No logo/bumper in content (house rule superseded storyboard's logo note); short gets studio intro/outro only.
- Formal narration about the physics. Voice am_michael 0.85.

## VERDICT: PASS
