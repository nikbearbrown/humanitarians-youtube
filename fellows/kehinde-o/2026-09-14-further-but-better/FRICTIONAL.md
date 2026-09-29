# Frictional Log -- Further But Better

**Date:** September 14, 2026
**Fellow:** Kehinde Obidele
**Work:** Brutalist video (STEM/AI explainer, Week 3)

## What I set out to do

Produce a STEM/AI explainer video for Week 3, built on my own `quantlab` repository: three post-training quantization methods implemented from their original papers and measured across 34 configurations on GPT-2. The title "Further, But Better" is the finding: the method that wins ends up roughly 2.5x further from the original weights than naive rounding, and its outputs are about twice as accurate. Distance in weight space is not damage in loss space.

## What I expected

I expected the Brutalist production workflow to be routine by now. On the content
side I expected the best quantization method to be the one that keeps the
compressed weights closest to the originals, which is the intuition the whole
topic seems to rest on.

## Where it resisted

That intuition is wrong, and the measurements say so. The winning method ends up
about 2.5x further from the original weights than naive rounding, and its outputs
are about twice as accurate. Stated plainly it sounds like a mistake, which is
exactly what makes it worth a video: distance in weight space is not damage in
loss space.

The animation could not be reused as it stood. My repository ships a 1080p mp4,
and upscaling it would have failed the 4K-at-source requirement, so the Manim
scene had to be re-rendered from source at 3840x2160.

The toolkit had also changed under me. A required paperwork set had been added
upstream and blocked every master until it existed. Writing those properly was the
right outcome but it was not work I had planned for.

The vertical cut exposed a layout fault that had been latent in the earlier weeks:
components laid out for a wide frame bled past the safe area in portrait. A first
attempt at fixing it by scaling the type up made it worse.

## What I did next

I built the video around the one counterintuitive result rather than around a tour
of the three methods, and re-rendered my own animation at 4K rather than upscaling
it. For the portrait fault, the fix that worked was authoring shorter lines in the
portrait beat sheet rather than resizing the type.

## What Claude or another person contributed

Claude drafted the beat sheet, handled the 4K re-render of my animation and the
portrait layout fixes. The implementations, the 34-configuration sweep, the Manim
scene and the argument the video makes are mine.

## What I accepted, changed, or rejected

I accepted keeping my own dark violet palette in the animation rather than
retinting it to match the video styling, because the palette is part of the work.
I rejected two attempts at the portrait fix that made it worse before the
line-length approach was tried.

## Result

Week 3 STEM/AI explainer completed. Both 16:9 and 9:16 versions rendered. Uploaded
to Google Drive, source files committed to GitHub. Measured on GPT-2 only; whether
the same ordering holds at larger scale is not something this project shows.
