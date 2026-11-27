# FACTCHECK — What Temperature Does to an AI's Answer

Every on-screen and spoken claim, traced to its source. Medhavy paths are relative to `~/Desktop/medhavy/medhavi-hub`. Code outputs are copied verbatim from `code/*.out.txt`.

## B00 · ASK
- Source: bookend (no factual claim beyond the film summary)
- Narration: Hi, I am Shubham L. and this video is about what the temperature setting really does when a language model picks its next word. The voice you're hearing is Liam, an A I narrator, reading my script. It's one number, and it changes how creative or predictable a model sounds.

## B01 · BLUF
- Source: bookend (no factual claim beyond the film summary)
- Narration: People treat temperature like a creativity dial that makes the model smarter. It changes the odds, not the knowledge. The model's scores stay the same. Temperature only decides how boldly it gambles on them.

## B02 · FRAMEWORK
- Source: standard softmax sampling; my temperature.py
- Narration: Picture the model finishing: the cat sat on the. It gives every candidate word a score. Here, mat three, sofa two, roof one point two, moon point two. Temperature divides those scores. Then they're turned into odds that add up to one, and the model rolls the dice. Temperature touches exactly one step.

## B03 · WORKED_EXAMPLE
- Source: stem-ai-2-temperature/code/temperature.out.txt (T=0.5)
- Narration: I ran it. At temperature point five, dividing makes the gaps between scores bigger. Mat jumps to eighty-six percent. Sofa twelve. Roof two. Moon rounds to zero. The model will say mat almost every time. That's what you want for facts, code, or anything that should come out the same twice.

## B04 · MECHANISM
- Source: stem-ai-2-temperature/code/temperature.out.txt (T=2.0)
- Narration: Now temperature two. Same scores, but dividing by two squeezes the gaps. Mat falls to forty-four percent, and moon climbs to eleven. One sentence in nine, the cat sits on the moon. Notice what didn't change: the order. Mat is still first. The model knows exactly what it knew before. It's just gambling more.

## B05 · FALSIFIABILITY
- Source: interpretation of my temperature.py results
- Narration: So the practical rule. Low temperature for facts, code, and extraction, where you want the same reliable answer. Higher temperature for brainstorming and stories, where variety is the point. But remember the moon. Turning temperature up never adds knowledge. It just gives unlikely words more chances, and some of those are wrong.

## B06 · VERDICT
- Source: bookend (no factual claim beyond the film summary)
- Narration: Temperature, then. The model scores the words, temperature reshapes the odds, and the dice decide. In my run, mat went from eighty-six percent to forty-four, but never lost first place. Use it to choose between predictable and varied, never to make the model know more.

## B07 · YOUR_TURN
- Source: bookend (no factual claim beyond the film summary)
- Narration: Your turn. Ask Claude for a script with five candidate words for a sentence you choose, printing the odds at four temperatures, then sampling twenty sentences at each and counting how often the top word wins. Run it twice. At low temperature the counts barely move. At high temperature, watch them wander.

## B08 · OUTRO
- Source: bookend (no factual claim beyond the film summary)
- Narration: That was What Temperature Does to an AI's Answer. Shubham L., for Humanitarians A I. Thanks for watching.

