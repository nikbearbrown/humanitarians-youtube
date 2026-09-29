# Frictional Log -- What the Marks Weigh

**Date:** September 4, 2026
**Fellow:** Kehinde Obidele
**Work:** Brutalist video (STEM/AI explainer, Week 1)

## What I set out to do

Produce a STEM/AI explainer video for Week 1 using the Brutalist toolkit (Fellow tier). The video is about Yoruba diacritics: how much information a tone mark actually carries, measured rather than asserted, and why that number decides whether restoring the marks needs a model or a lookup table. It is built on my own `ami` repository, a 1.29M-parameter BiLSTM trained on MENYO-20k.

## What I expected

I expected the Brutalist workflow to be straightforward: write a beat sheet, create PEDAGOGY.md, generate audio with Kokoro, compile, and render. I expected to produce both 16:9 and 9:16 versions.

## Where it resisted

Learning the Brutalist toolkit for the first time took longer than expected. Understanding how the beat_sheet.json structure maps to the final video required reading the skill documentation carefully. The audio-first philosophy was different from how I had thought about video production before.

Getting the narration pacing right took a few iterations. Some beats were too long and needed to be split. The mandatory intro ("Hi, I am Kehinde Obidele and this video is about...") had to be the very first beat.

## What I did next

I worked through the toolkit's own build order: write the beat sheet, write PEDAGOGY.md with a learning objective and mark it VERDICT: PASS, generate the narration with Kokoro, then compile the review cut. The gate is real, not ceremonial: audio will not generate until the pedagogy review passes.

## What Claude or another person contributed

Claude helped draft the initial beat sheet narration. I revised the wording to match how I speak and checked every figure against what my own model actually measured, rather than letting a number stand because it sounded right.

## What I accepted, changed, or rejected

I accepted the audio-first workflow after seeing how it produces consistent timing. I changed some of Claude's suggested narration to be more personal and grounded in my own measurements. I rejected overly technical language that would lose a general audience.

## Result

Week 1 STEM/AI explainer video completed. Both 16:9 and 9:16 versions rendered. Video uploaded to Google Drive. Source files (beat_sheet.json, PEDAGOGY.md, README.md) committed to GitHub.
