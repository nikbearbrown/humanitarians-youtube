# Backwards Along the Tape — frictional log

## 2026-09-24 — building the week 5 STEM explainer

I paired this with the Chapter 30 report deliberately. Chapter 30's spine is the fourth
audit pass, the one that stopped asking whether my sources were real and started asking
whether they said what I claimed. My ember repo has the same posture: it does not claim the
gradients are right, it proves they match PyTorch.

The one idea is that backward() is a single rule applied in reverse along a recorded tape.
Multiply local derivatives along a path, add them where paths meet. I wrote the engine
because I could train a model without being able to say what that one line of code actually
did, and that is not knowing.

Every figure in the video came out of the repo's committed run logs rather than its README,
which is a rule the toolkit now enforces and which I think is right. Largest gap between my
loss curve and PyTorch's over 300 steps: 2.682e-07, from parity_log.json. Validation loss
1.8336 from 4.4910 at initialisation, from shakespeare_log.json. 97.83% on MNIST. The
uniform-guessing floor of 4.17 I computed as ln(65) for the 65-character vocabulary, which
is worth stating because it means the model starts slightly worse than guessing.

### Where the build resisted

Three things, and all three were mine.

The Manim animation died at the LaTeX step after several minutes of rendering. The scene
uses MathTex, which needs dvisvgm, and dvisvgm lives inside TinyTeX and is not on the
default PATH on this machine. Last week's animation used plain text so it never hit this.
Once the PATH was set it rendered at true 3840x2160 rather than being upscaled.

The vertical cut then failed the visual QC gate with a blocking defect: my hand-built
portrait version of that animation crossed the title-safe boundary on both sides. I had
padded it to 2100px wide with 30px margins when the safe area needs 108px. Rebuilt at
1900px, measured the content bounds directly rather than eyeballing them, and it now sits
at x 171 to 1967 inside the required 108 to 2052.

The third one taught me something about the toolkit. The overview beat types a sentence and
then corrects a word in place. I had sized the font from the line I wrote, but the line that
actually renders is the one after the correction, and "So I know how it works" becomes "So I
cannot say how it works", six characters longer. It overflowed the safe edge in portrait.
The rule I wrote down for next time is to size from the post-replacement length.

### What Claude contributed

Claude Code drafted the beat sheet, found the dvisvgm cause, and measured the title-safe
overruns rather than guessing at them. I rejected one suggestion: an earlier draft described
the project in the third person and carried my internal portfolio numbering, which reads
like a catalogue entry rather than something I wrote. Rewritten in first person.
