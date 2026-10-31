# Friction Log: ECIS Episode 13

**Type:** Weekly Implementation Video
**Week:** Week 18 (Phase 18), October 25 – 31, 2026

---

## 1. Date and focus

This week's video covers the Phase 18 work on ECIS. The build finished on October 28, with all ten scenes rendered.

The episode explains four new things the system can do:
- **Confidence:** check that its confidence scores are accurate.
- **Mixed signals:** notice when signals from the same earnings call point in different directions.
- **Explanations:** explain each prediction in a plain sentence.
- **Unfamiliar calls:** recognize a call that looks unlike anything it has seen before.

## 2. What was tried, and what was expected

- **Visuals:** the visuals in the brief were expected to match the narration.
- **Colors:** the brief gave each capability its own color. These were expected to work as given.
- **Ending:** the brief ended with a fade to black. This was expected to give a clean finish.
- **Length:** the narration was to stay exactly as written, with each section expected to fit within the 45 to 70 word target.

## 3. Where things got stuck, and what was done next

**The mixed-signals scene showed the wrong count.**
The narration describes three kinds of mixed signal. The brief, though, drew only two, with a counter saying "2 detected". Both can be true, because the system can check a pattern and find nothing. On screen, though, it looked like a counting error.

The scene was rebuilt to show all three patterns being checked:
- Two are found.
- The third comes back clear, because the signals it relies on are weak in this call.
- The counter now counts what was found, instead of showing a fixed number.

The narration did not change.

**The sixth section had the wrong label.**
It was labelled "Your Turn", but the narration there is really a closing summary. It was built as the closing summary, and the viewer prompt stays in its own section later.

**The ending.**
A fade to black would have ended on an empty screen, because the final frame is held for a few seconds. Dimming the title was also ruled out, since a dimmed title can blend into the scene behind it. The video now ends on the title card at full brightness.

**Colors.**
The brief's colors were adjusted so that each new capability keeps one consistent color throughout. This makes each capability easy to follow from scene to scene.

**Numbers that appear more than once.**
The same number typed in two places can drift apart. To prevent that, each number was calculated once and reused:
- **The explanation chart:** its bars add up exactly to the final 0.75 prediction.
- **The unfamiliar-calls chart:** each point's position comes from its own penalty value, so the two always match.
- **The calibration summary figures:** they come straight from the table on screen.

**Length.**
All six main sections ran longer than the 45 to 70 word target, at between 76 and 116 words. They were kept as written, because something new appears on screen throughout each one.

The closing summary written by Claude also ran about six seconds longer than planned.

## 4. What Claude contributed, and what was kept or changed

**Who did what:**
- **Original work:** the concept, the brief, and the narration for the six main sections.
- **Claude:**
  - assembled the video using the video generation tool created by Humanitarians AI
  - wrote the opening, the closing summary, the viewer prompt and the outro
  - drafted the review, which was approved before recording

**Accepted:**
- the rebuilt mixed-signals scene
- treating the sixth section as the closing summary
- calculating repeated numbers once

**Changed from the brief:**
- the colors
- the count of patterns shown
- the ending

**Kept as written:** all of the original narration.

## 5. What is understood now, and what is still open

**Understood now:**
- **A brief can disagree with itself.** The visuals need to be checked against the narration, not just against the project.
- **It is clearer to show a check that finds nothing** than to show only the checks that find something.
- **Calculating a chart's total from its parts** means the chart always adds up.

**Still open:**
- None