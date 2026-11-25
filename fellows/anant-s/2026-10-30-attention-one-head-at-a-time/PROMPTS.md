# PROMPTS: Attention, One Head at a Time

There are no generation prompts. Every beat is machine-built:
- Remotion bookends are filled from `beat_sheet.json` props.
- Manim LEARN scenes, still to be written in `scenes.py`, are driven by `demo/evidence.json`.

Nothing goes to an image or video generator, there is no paid call, and there is no pantry request.

| Beat | Prompt |
|---|---|
| B00–BOUT | none (deterministic render) |

The only "prompt" in the film is the viewer's YOUR TURN exercise (BHTF). It is shown and read aloud, never sent:

> Write a short Python script, numpy only, for one attention head on a three-word sentence. Use small integer queries, keys and values that you choose. Before running it, predict which word each word will weight most. Then print the scores, the softmax weights, and the outputs. Finally, reverse the word order, run it again, and explain what changed and what didn't.
