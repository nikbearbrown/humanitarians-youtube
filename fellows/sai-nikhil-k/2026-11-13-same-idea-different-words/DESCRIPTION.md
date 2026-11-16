Ethan Mollick calls Anthropic's Fable 5.2 "almost AGI", but jagged. Jagged where? We tested one of his examples in the code he published.

In "Fable 5.2 and Jagged AGI" (One Useful Thing, 9 Nov 2026), Mollick argues that the model's weak spots are no longer made-up facts or bad maths: they are judgement. One of his examples is Portals, an endless flight through worlds built by AI agents, where three separate teams built the same idea: a cyclone of circling animals.

We cloned the Portals code (471 worlds) and checked:
- The three worlds are real: 3,000 reindeer turning in rings on a frozen lake, 200 manta rays in a turning column, storks circling up a thermal.
- A word-matching check scores two texts by the cosine of their word vectors: cos θ = a·b / (‖a‖‖b‖). With no shared word, a·b = 0, so the score is 0.
- Across all 110,685 pairs of world descriptions, 45.5% share at least one content word. The three cyclones share none: every pair scores 0.
- (The short one-line captions are different: two of them use the word "cyclone".)

The sameness is in the idea, where word matching can't see it. By Mollick's account, no agent noticed. Fable builds like a team of experts; the step back (is this too long, too repetitive, any fun?) is still a person's job.

Try it yourself: ask your AI for twenty ideas, then ask which ones are the same idea in different words. Then check its answer yourself.

Chapters:
0:00 Almost AGI, but jagged
0:12 Three worlds, one idea
0:25 How a word check scores sameness
0:45 Verdict and your turn

Sources:
Ethan Mollick, "Fable 5.2 and Jagged AGI", One Useful Thing, 9 Nov 2026 — https://www.oneusefulthing.org/p/fable-52-and-jagged-agi
Portals (code at release s8f, 471 worlds) — https://github.com/emollick/ai-portals · live: https://portals-endless-worlds.netlify.app

Images:
The Turning Herd, Inside the Manta Cyclone and A Kettle of Storks, from Portals by Ethan Mollick, built by AI agents. CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/). Rendered locally from the published code for this video; composed on a plate with captions.

Hosted by Sai. Voice: Kokoro am_onyx, free and local. AI-generated narration; motion graphics built with Remotion; the equations typeset locally as SVG. The word-overlap measurement (scikit-learn TF-IDF) was run locally on the Portals repository. No image was generated for this video. No human-performed audio or video.

Humanitarians AI: https://humanitarians.ai
Musinique: https://musinique.com
Medhavy AI: https://medhavy.com

TAGS: Fable 5.2, Claude, Anthropic, jagged AGI, Ethan Mollick, One Useful Thing, AI agents, Portals, cosine similarity, TF-IDF, AI evaluation, Humanitarians AI, weekly, Computational Skepticism

#AI #AGI #Claude #AIAgents #Mollick #HumanitariansAI #ComputationalSkepticism
