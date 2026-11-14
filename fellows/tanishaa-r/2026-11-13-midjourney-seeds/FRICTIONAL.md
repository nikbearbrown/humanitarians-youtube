# Frictional log: Why the Same Prompt Gives Four Different Images

_Drafted by Claude on 2026-11-13 from this week's chat and the build log. Tanishaa: read it and correct anything that is not what happened._

## 2026-11-13 — Building the Midjourney seeds video
- **Working on:** my Midjourney topic from the team's video split: why one prompt gives four different images, and what a seed does.
- **Tried:** my topic note said reusing a seed "is how you keep a consistent look across assets". Expected the video to teach that.
- **Resisted:** Midjourney's own Seeds page says seeds are "Not for Saving Styles": a seed only sets the starting noise, and for a consistent look it recommends style references, omni references and personalization. I chose to correct the ending ("seed = same image; references = same look") and to show no Midjourney screenshots, so the evidence is a small toy generator (`demo/seed_demo.py`), labeled as a toy. Its first version made near-identical mush and was redrawn as hills and a sun. After watching the first cut, I felt the pacing near the end was off; a check of every on-screen item against Bella's words found three problems (steps shown before she named them, a line she never says, and a your-turn prompt that typed on its own clock), and all were fixed.
- **Contributions:** Claude found the Midjourney docs, drafted the script, wrote the toy demo and the scenes (`scenes/MjScenes.tsx`), and ran the build. I gave the topic, chose the corrected ending and the no-screenshots approach, approved the script, and flagged the pacing.
- **Understand now:** the seed controls the starting noise, not the style; it's most useful as a control when testing one change. **Still unsure:** _[Tanishaa: what is still unclear to you?]_
