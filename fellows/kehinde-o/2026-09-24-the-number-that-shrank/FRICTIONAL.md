# The Number That Shrank — frictional log

## 2026-09-24 — building the week 4 STEM explainer

I wanted a STEM topic that connected to the fact-checking work rather than sitting beside
it, so I used my own FAERS pharmacovigilance pipeline. Chapter 25 is full of drug-record
errors; this project is the same subject approached from the data side.

The idea I wanted to land is one I got wrong myself when I built the pipeline. I assumed
the strongest safety signal would be the biggest ratio. It is not. The biggest ratios in
the output come from the thinnest evidence, and empirical Bayes shrinkage is what separates
the two.

I did not want to assert that, so I recomputed it from the committed run outputs. Warfarin
with gastrointestinal bleeding: 62 reports where 2.9 were expected, a crude ratio of 21.2,
and after shrinkage 21.0. It keeps 99% of its ratio. Esculin with heart sounds: 16 reports
where almost none were expected, a crude ratio above 55,000, and after shrinkage 2,209. It
keeps 4%. Same shrink applied to both; only one had anything to lose.

### Where the build resisted

Two things.

First, the toolkit now requires structured math rendering rather than formula strings on a
text card. That is a better rule than it sounds. The expected-count formula renders with a
real fraction bar and proper marginal-total indices, which is the difference between showing
the idea and describing it.

Second, and this one cost real time: I fed the attrition figure the raw report count,
1,619,665, and it draws one element per unit. It hung the renderer and the compile correctly
refused to produce a master with a placeholder in it. The fix was to draw the funnel in
thousands and say so on screen, "each dot is one thousand reports". The counter now steps
1620 to 1215 to 473 against the real 1,619,665 to 1,214,808 to 472,082. The narration still
speaks the exact figures. I prefer this to the alternative of quietly showing a made-up
smaller number.

Claude Code found the crash cause and proposed the thousands framing; I kept it because the
unit label makes it honest rather than merely legible.

### What I understand now

The restraint line in this video matters more than the statistics. FAERS reporting is
voluntary and disproportionality is not causality, so the video says N counts reports and
not patients, on screen, and esculin appears only as an example of thin evidence rather than
as a safety claim about a drug.
