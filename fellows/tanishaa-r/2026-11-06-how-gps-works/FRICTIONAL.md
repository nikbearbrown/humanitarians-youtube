# Frictional log: How GPS Knows Where You Are

_Written on 2026-11-10 from the build log, after the work it describes, and drafted by Claude. Tanishaa: read it and correct anything that is not what happened._

## 2026-11-08 — Building "How GPS Knows Where You Are" (written 2026-11-10)
- **Working on:** a STEM explainer on how a phone works out where it is.
- **Tried:** chose GPS from four non-music options. Predicted that three satellites would be enough. Before the build I set a rule: long narration shows only key points, each appearing exactly when Bella says it.
- **Resisted:** the demo (`demo/gps_demo.py`) showed why three isn't enough: a 1 µs clock error puts every range about 300 m off, and ignoring it left the fix 390 m off, while solving for the clock with a fourth satellite brought it to almost zero. In the build, satellites and circles ran past the safe area of the frame and had to be redrawn. After watching it, I pointed out that the "three things to keep" card showed its lines together instead of one by one; the toolkit's card ignores line timing, so a new card was written that reveals each line on its spoken words.
- **Contributions:** Claude drafted the script, wrote the demo, the scenes (`scenes/GpsScenes.tsx`) and the fact check, and ran the build. I chose the topic, set the key-points sync rule, approved the script and caught the takeaway-card problem.
- **Understand now:** the fourth satellite is there to solve for the phone's clock error, not position. **Still unsure:** _[Tanishaa: what is still unclear to you?]_
