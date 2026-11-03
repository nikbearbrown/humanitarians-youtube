# Frictional Log — System One Models and Jev

> Append dated entries as you go; never rewrite an earlier one.

## 2026-09-26 — Building a 60-second explainer on TypeSafe's Jev, in 16:9 and 9:16

*Written 2026-09-28, after the build; drafted with Claude Code from the build record and reviewed by me.*

- **What I tried, and what I expected:**
  I wrote a brief with six points I wanted covered and asked the ai-explainer skill for 12 beats, one voice, and native 4K in both aspect ratios. My first attempt at this topic had no source on Jev, so it came out generic and I deleted it. This time I gave the specific claims and expected the vertical version to mostly fall out of the landscape one.

- **Where it resisted, and what I did next:**
  The vertical cut needed more work than I expected: some stock portrait scenes ignored the beat length and would have been center-cut, and several portrait layouts collided or ran past the safe margin. The stock outro also failed the visual check because it filled so little of the frame, so it was replaced with a fuller Humanitarians AI outro. The final length came out at 65 seconds, and I kept it rather than drop one of my points.

- **What Claude or another person contributed — and what I accepted, changed, or rejected:**
  Claude Code drafted the beat sheet and narration, wrote the custom scenes, checked my claims against TypeSafe's own post and docs, and fixed the layout problems the checks found. I accepted its suggestion to say "no type errors" instead of "never hallucinates", which some coverage claims but TypeSafe does not. I changed the greeting to "Namaskaram, Likhith" and set the channel to @HumanitariansAI.

- **What I understand now, and what I still do not:**
  I understand the difference between a typed answer and a correct one, and that a vertical video is its own beat sheet, not a crop. I haven't verified Jev's speed or calibration claims beyond TypeSafe's own statements. It's still open whether the AI voice saying "Hi, I am Likhith" is acceptable, and I haven't produced clean final masters yet.

- **Evidence:** [beat sheet](beat_sheet.json) · [vertical beat sheet](vertical/beat_sheet.json) · [build log](BUILD-LOG.md) · [fact-check](FACTCHECK.md)

## 2026-09-28 — Turning the review cuts into final masters

*Drafted with Claude Code from the build record and reviewed by me.*

- **What I tried, and what I expected:**
  I signed off the fact-check and asked for clean final masters in both formats. I expected `./art final` to be a quick re-export of the review cuts I had already checked.

- **Where it resisted, and what I did next:**
  The final is blocked until the type-lock check passes, and it didn't: terracotta text on cream failed the contrast rule, and some small words fell under the size floor, especially in portrait. The fixes were a darker terracotta for text and a few fills, rewording a couple of lines, and bigger sans-serif body text in the vertical cut.

- **What Claude or another person contributed — and what I accepted, changed, or rejected:**
  Claude Code traced each failure to the exact element, made the fixes, re-rendered, and re-ran the checks until all four cuts passed. I also had it put the AI-narration disclosure on screen, since the fellows guide asks for it. I accepted the slightly darker accent color as the cost of readable text.

- **What I understand now, and what I still do not:**
  Portrait 4K has a much stricter text-size rule than landscape, so I'll design vertical layouts with bigger text from the start. I still need YouTube's 4K processing check and a decision on the "Hi, I am Likhith" line in an AI voice.
