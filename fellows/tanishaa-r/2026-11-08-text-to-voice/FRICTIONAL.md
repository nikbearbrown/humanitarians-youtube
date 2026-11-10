# Frictional log: How a Computer Turns Text into a Voice

_Written on 2026-11-10 from the build log, after the work it describes, and drafted by Claude. Tanishaa: read it and correct anything that is not what happened._

## 2026-11-08 — Building "How a Computer Turns Text into a Voice" (written 2026-11-10)
- **Working on:** a STEM explainer on text-to-speech, using the same AI voice that narrates my videos.
- **Tried:** predicted the engine would read "I read it yesterday" in the past tense from context.
- **Resisted:** the real demo (`demo/tts_demo.py`) proved the prediction wrong: it said "reed", read "Oak Dr." as "Oak Doctor" and "$5" as "dollar five", in two different voices. The script was changed to show those mistakes instead. After watching the cut, I said the opening text didn't match the narration and the pacing was off (around 0:15). The cause was a typing animation with its own random pace and different words; it was replaced with the narration shown word for word, each word lighting up as it's spoken.
- **Contributions:** Claude drafted the script, wrote the demo, the scenes (`scenes/TtvScenes.tsx`) and the fact check, and ran the build. I chose the topic, approved the script, caught the opening mismatch and approved the fixed cut.
- **Understand now:** a voice engine guesses pronunciation from spelling and doesn't really understand context, so it gets the same words wrong in any voice. **Still unsure:** _[Tanishaa: what is still unclear to you?]_
